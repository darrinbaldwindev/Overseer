"""Persistent-model primitives for reusable Overseer skills.

This module intentionally contains no storage backend and no execution authority.
It defines deterministic, auditable skill records and conservative retrieval.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import sha256
from typing import Iterable, Mapping


VALID_STATUSES = {"candidate", "validated", "deprecated", "blocked"}
SCOPES = {"portfolio", "repository", "component", "task"}


def stable_skill_id(name: str, scope: str) -> str:
    """Return a stable identifier for a canonical skill name and scope."""
    key = f"{scope.strip().lower()}::{name.strip().lower()}".encode("utf-8")
    return "skill-" + sha256(key).hexdigest()[:16]


@dataclass(frozen=True)
class Skill:
    """An auditable reusable procedure, independent of execution authority."""

    name: str
    description: str
    triggers: tuple[str, ...]
    prerequisites: tuple[str, ...]
    steps: tuple[str, ...]
    outputs: tuple[str, ...]
    validation: tuple[str, ...]
    safety_constraints: tuple[str, ...]
    scope: str = "task"
    status: str = "candidate"
    confidence: float = 0.0
    version: int = 1
    provenance: tuple[str, ...] = ()
    evidence_refs: tuple[str, ...] = ()
    usage_count: int = 0
    success_count: int = 0
    last_used_at: str | None = None
    skill_id: str = field(init=False)

    def __post_init__(self) -> None:
        if self.scope not in SCOPES:
            raise ValueError(f"invalid scope: {self.scope}")
        if self.status not in VALID_STATUSES:
            raise ValueError(f"invalid status: {self.status}")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        if self.version < 1 or self.usage_count < 0 or self.success_count < 0:
            raise ValueError("version and usage counters must be non-negative")
        if self.success_count > self.usage_count:
            raise ValueError("success_count cannot exceed usage_count")
        if not self.name.strip() or not self.steps:
            raise ValueError("name and at least one procedure step are required")
        object.__setattr__(self, "skill_id", stable_skill_id(self.name, self.scope))

    @property
    def success_rate(self) -> float:
        return self.success_count / self.usage_count if self.usage_count else 0.0

    def matches(self, task_terms: Iterable[str], available_capabilities: Iterable[str] = ()) -> bool:
        """Conservatively match a skill using trigger and prerequisite vocabulary."""
        terms = {str(x).strip().lower() for x in task_terms if str(x).strip()}
        capabilities = {str(x).strip().lower() for x in available_capabilities if str(x).strip()}
        trigger_text = " ".join(self.triggers).lower()
        prereq_text = {p.lower() for p in self.prerequisites}
        return bool(terms & set(trigger_text.split())) and prereq_text <= capabilities

    def record_outcome(self, success: bool, used_at: str) -> "Skill":
        """Return a new skill record with one audited reuse outcome."""
        return Skill(
            name=self.name,
            description=self.description,
            triggers=self.triggers,
            prerequisites=self.prerequisites,
            steps=self.steps,
            outputs=self.outputs,
            validation=self.validation,
            safety_constraints=self.safety_constraints,
            scope=self.scope,
            status=self.status,
            confidence=self.confidence,
            version=self.version,
            provenance=self.provenance,
            evidence_refs=self.evidence_refs,
            usage_count=self.usage_count + 1,
            success_count=self.success_count + (1 if success else 0),
            last_used_at=used_at,
        )


@dataclass
class SkillMemory:
    """Small in-memory registry used by tests and future persistent adapters."""

    skills: dict[str, Skill] = field(default_factory=dict)

    def add(self, skill: Skill) -> None:
        self.skills[skill.skill_id] = skill

    def get(self, skill_id: str) -> Skill | None:
        return self.skills.get(skill_id)

    def search(
        self,
        task_terms: Iterable[str],
        available_capabilities: Iterable[str] = (),
        include_candidates: bool = True,
    ) -> list[Skill]:
        matches = [
            skill
            for skill in self.skills.values()
            if (include_candidates or skill.status == "validated")
            and skill.status not in {"deprecated", "blocked"}
            and skill.matches(task_terms, available_capabilities)
        ]
        return sorted(
            matches,
            key=lambda s: (
                s.status != "validated",
                -s.confidence,
                -s.success_rate,
                -s.usage_count,
                s.skill_id,
            ),
        )
