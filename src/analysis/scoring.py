"""Evidence-backed health scoring primitives."""

from dataclasses import dataclass


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


def health_score(findings: list[FindingScore]) -> float:
    """Return a bounded score from 0-100 using conservative deductions."""
    score = 100.0
    for finding in findings:
        score -= SEVERITY_DEDUCTIONS.get(finding.severity, 0.0) * WEIGHTS.get(finding.area, 0.0) / 0.25
    critical = any(f.severity == "Critical" for f in findings)
    if critical:
        score = min(score, 49.0)
    return round(max(0.0, min(100.0, score)), 1)
