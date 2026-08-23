"""Small deterministic orchestration contract for the Manus runtime.

The Manus agent supplies GitHub adapters and persistence implementations. This
module defines the order in which those capabilities are invoked.
"""

from dataclasses import dataclass
from typing import Callable, Iterable, Any


@dataclass(frozen=True)
class ScanResult:
    repository: str
    status: str
    evidence_count: int
    finding_count: int
    health_score: float | None


def run_repository_scan(
    repository: str,
    discover: Callable[[str], Any],
    scan: Callable[[Any], Iterable[Any]],
    analyse: Callable[[Iterable[Any]], Iterable[Any]],
    score: Callable[[list[Any]], float],
) -> ScanResult:
    """Execute one scan in a fixed order without granting autonomous write authority."""
    snapshot = discover(repository)
    evidence = list(scan(snapshot))
    findings = list(analyse(evidence))
    health = score(findings)
    return ScanResult(repository, "complete", len(evidence), len(findings), health)
