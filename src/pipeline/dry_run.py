"""End-to-end dry-run pipeline with no repository mutation authority."""

from dataclasses import dataclass
from typing import Any, Callable, Iterable

from src.state.portfolio_store import PortfolioStore


@dataclass(frozen=True)
class DryRunResult:
    repository: str
    evidence_count: int
    finding_count: int
    finding_states: tuple[str, ...]
    health_score: float


def run_dry_scan(
    repository: str,
    discover: Callable[[str], Any],
    scan: Callable[[Any], Iterable[Any]],
    analyse: Callable[[Iterable[Any]], Iterable[Any]],
    fingerprint: Callable[[Any], str],
    score: Callable[[list[Any]], float],
    store: PortfolioStore,
) -> DryRunResult:
    snapshot = discover(repository)
    evidence = list(scan(snapshot))
    findings = list(analyse(evidence))
    states = tuple(store.observe_finding(finding.rule_id, fingerprint(finding)) for finding in findings)
    store.record_scan({
        "repository": repository,
        "evidence_count": len(evidence),
        "finding_count": len(findings),
        "dry_run": True,
    })
    return DryRunResult(repository, len(evidence), len(findings), states, score(findings))
