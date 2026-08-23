"""Evidence-backed health scoring primitives."""

from dataclasses import dataclass
from typing import Iterable, Any

WEIGHTS = {
    "security": 0.25,
    "correctness": 0.25,
    "reliability": 0.20,
    "delivery": 0.15,
    "engineering_quality": 0.15,
}

SEVERITY_DEDUCTIONS = {"Critical": 25.0, "High": 12.0, "Medium": 5.0, "Low": 1.5}


@dataclass(frozen=True)
class FindingScore:
    area: str
    severity: str


def health_score(findings: Iterable[Any]) -> float:
    """Return a bounded score from 0-100 using conservative deductions.

    Accepts FindingScore values or analysis findings exposing ``area`` and
    ``severity`` attributes, keeping the scoring layer independent of the
    analysis representation.
    """
    score = 100.0
    normalized = [FindingScore(getattr(f, "area", ""), getattr(f, "severity", "")) for f in findings]
    for finding in normalized:
        score -= SEVERITY_DEDUCTIONS.get(finding.severity, 0.0) * WEIGHTS.get(finding.area, 0.0) / 0.25
    if any(f.severity == "Critical" for f in normalized):
        score = min(score, 49.0)
    return round(max(0.0, min(100.0, score)), 1)
