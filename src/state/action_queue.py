"""Durable, deterministic action-queue primitives for GPTChat -> Overseer handoff.

The queue is storage-agnostic: the runtime can persist the returned dictionaries in
JSON/YAML/database storage. Idempotency is based on a stable task ID derived from
(report, finding, target repository). This keeps report ingestion safe to retry.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from hashlib import sha256
from typing import Iterable, Mapping

STATUSES = {
    "discovered",
    "queued",
    "delegated",
    "executing",
    "verification",
    "verified",
    "failed",
    "blocked",
}

TERMINAL = {"verified"}


@dataclass(frozen=True)
class ActionTask:
    task_id: str
    source_report: str
    finding_id: str
    priority: str
    target_repo: str
    objective: str
    acceptance_criteria: tuple[str, ...]
    executor: str | None = None
    verifier: str | None = None
    evidence_required: tuple[str, ...] = ()
    authority_boundary: str = "autonomous_within_delegated_scope"
    dependency_ids: tuple[str, ...] = ()
    fallback_action: str = "escalate_to_overseer"
    status: str = "discovered"
    evidence: tuple[str, ...] = ()
    attempts: int = 0
    metadata: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.status not in STATUSES:
            raise ValueError(f"invalid task status: {self.status}")
        if not self.task_id:
            raise ValueError("task_id is required")

    def transition(self, status: str) -> "ActionTask":
        if status not in STATUSES:
            raise ValueError(f"invalid task status: {status}")
        if self.status == "verified" and status != "verified":
            raise ValueError("verified tasks cannot regress")
        if status == "verified" and not self.evidence:
            raise ValueError("verification requires evidence")
        return ActionTask(**{**asdict(self), "status": status})

    def to_dict(self) -> dict:
        value = asdict(self)
        value["acceptance_criteria"] = list(self.acceptance_criteria)
        value["evidence_required"] = list(self.evidence_required)
        value["dependency_ids"] = list(self.dependency_ids)
        value["evidence"] = list(self.evidence)
        return value


def stable_task_id(source_report: str, finding_id: str, target_repo: str) -> str:
    """Return a retry-safe deterministic task identifier."""
    raw = f"{source_report}\n{finding_id}\n{target_repo}".encode()
    return "TASK-" + sha256(raw).hexdigest()[:20]


def task_from_finding(report_id: str, finding: Mapping[str, object]) -> ActionTask:
    """Convert a finding into a durable task envelope without selecting an agent."""
    finding_id = str(finding.get("finding_id") or finding.get("id") or "unknown")
    target_repo = str(finding.get("target_repo") or finding.get("repository") or "")
    if not target_repo:
        raise ValueError("finding target_repo/repository is required")
    objective = str(finding.get("objective") or finding.get("title") or finding.get("description") or "")
    if not objective:
        raise ValueError("finding objective/title/description is required")
    criteria = finding.get("acceptance_criteria") or ["Issue is resolved and evidence is recorded"]
    if isinstance(criteria, str):
        criteria = [criteria]
    return ActionTask(
        task_id=stable_task_id(report_id, finding_id, target_repo),
        source_report=report_id,
        finding_id=finding_id,
        priority=str(finding.get("priority") or "P2"),
        target_repo=target_repo,
        objective=objective,
        acceptance_criteria=tuple(str(x) for x in criteria),
        evidence_required=tuple(str(x) for x in (finding.get("evidence_required") or [])),
        authority_boundary=str(finding.get("authority_boundary") or "autonomous_within_delegated_scope"),
        dependency_ids=tuple(str(x) for x in (finding.get("dependency_ids") or [])),
        fallback_action=str(finding.get("fallback_action") or "escalate_to_overseer"),
    )


def ingest_report(report_id: str, findings: Iterable[Mapping[str, object]], existing: Mapping[str, ActionTask] | None = None) -> dict[str, ActionTask]:
    """Idempotently ingest actionable findings into an existing task map."""
    queue = dict(existing or {})
    for finding in findings:
        task = task_from_finding(report_id, finding)
        queue.setdefault(task.task_id, task)
    return queue
