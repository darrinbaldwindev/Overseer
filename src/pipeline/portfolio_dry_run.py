"""Portfolio-level dry-run composition for the Overseer domain layers."""

from dataclasses import dataclass
from typing import Any, Callable, Iterable

from src.analysis.rules import generate_candidates
from src.pipeline.dry_run import run_dry_scan
from src.scanner.evidence import extract_evidence
from src.state.portfolio_store import PortfolioStore


@dataclass(frozen=True)
class PortfolioDryRun:
    results: tuple[Any, ...]
    repositories_scanned: int


def fingerprint_finding(finding: Any) -> str:
    import hashlib
    import json
    payload = {
        "rule_id": finding.rule_id,
        "classification": finding.classification,
        "confidence": finding.confidence,
        "area": finding.area,
        "severity": finding.severity,
        "title": finding.title,
        "evidence_paths": finding.evidence_paths,
        "rationale": finding.rationale,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=list)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def run_portfolio_dry_run(
    repositories: Iterable[str],
    discover_paths: Callable[[str], Iterable[str]],
    score: Callable[[list[Any]], float],
    store: PortfolioStore | None = None,
) -> PortfolioDryRun:
    state = store or PortfolioStore()

    def discover(repo: str) -> list[str]:
        return list(discover_paths(repo))

    def scan(paths: Iterable[str]) -> list[Any]:
        return extract_evidence(paths)

    results = []
    for repository in repositories:
        result = run_dry_scan(
            repository,
            discover,
            scan,
            generate_candidates,
            fingerprint_finding,
            score,
            state,
        )
        results.append(result)
    return PortfolioDryRun(tuple(results), len(results))
