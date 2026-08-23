"""Conservative evidence-to-candidate analysis rules."""

from dataclasses import dataclass
from typing import Iterable

from src.scanner.evidence import Evidence


@dataclass(frozen=True)
class CandidateFinding:
    rule_id: str
    classification: str
    confidence: str
    area: str
    severity: str
    title: str
    evidence_paths: tuple[str, ...]
    rationale: str


def generate_candidates(evidence: Iterable[Evidence]) -> list[CandidateFinding]:
    items = list(evidence)
    paths = {item.path for item in items}
    findings: list[CandidateFinding] = []

    env_paths = tuple(sorted(path for path in paths if path == ".env" or path.endswith("/.env") or path.endswith("/.env.local")))
    if env_paths:
        findings.append(CandidateFinding(
            "ENV-FILE-PRESENT", "Potential", "Medium", "security", "Medium",
            "Environment file present in repository tree", env_paths,
            "Environment files can contain secrets; file presence alone does not prove secret exposure.",
        ))

    workflows = tuple(sorted(item.path for item in items if item.kind == "ci_workflow"))
    has_tests = any(item.kind == "test" for item in items)
    if workflows and not has_tests:
        findings.append(CandidateFinding(
            "CI-WITHOUT-TEST-EVIDENCE", "Potential", "Low", "engineering_quality", "Low",
            "CI workflow detected without test-path evidence", workflows,
            "The tree exposes CI configuration but no recognizable test path; workflow contents must be inspected before confirmation.",
        ))

    return findings
