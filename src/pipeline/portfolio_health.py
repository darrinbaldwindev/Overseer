"""Deterministic portfolio-health composition over the existing Overseer contracts.

This module does not discover repositories, execute remediations, schedule work, or
perform assurance. Callers supply independently observed check values and an
optional Project Overseer routing callback. A non-GREEN result may be routed, but
only a fresh subsequent observation can improve health.
"""

from dataclasses import dataclass
from typing import Callable, Mapping, Sequence


_REQUIRED_CHECKS = (
    "access", "tests", "security", "overseer", "evidence", "prs", "green_agent",
)


@dataclass(frozen=True)
class HealthObservation:
    repository: str
    commit: str
    checked_at: str
    checks: Mapping[str, str]
    findings: tuple[str, ...] = ()
    evidence_refs: tuple[str, ...] = ()


@dataclass(frozen=True)
class RoutedFinding:
    repository: str
    commit: str
    health: str
    findings: tuple[str, ...]
    next_action: str


def _health(checks: Mapping[str, str]) -> str:
    if checks.get("access") == "FAIL" or checks.get("overseer") == "BLOCKED":
        return "BLOCKED"
    if checks.get("tests") == "FAIL" or checks.get("security") == "FAIL" or checks.get("prs") == "FAILED" or checks.get("green_agent") == "RED":
        return "RED"
    if any(checks.get(key) in {None, "UNKNOWN"} for key in _REQUIRED_CHECKS):
        return "AMBER"
    if checks.get("overseer") == "STALE" or checks.get("evidence") in {"STALE", "MISSING"} or checks.get("prs") == "PENDING" or checks.get("green_agent") == "AMBER":
        return "AMBER"
    return "GREEN"


def build_health_record(observation: HealthObservation) -> dict:
    """Build one schema-shaped health record from explicit observed evidence."""
    health = _health(observation.checks)
    next_action = "none"
    if health != "GREEN":
        next_action = "route finding to responsible Project Overseer and require a fresh rescan after remediation"
    return {
        "schema_version": "1.0",
        "repository": observation.repository,
        "commit": observation.commit,
        "checked_at": observation.checked_at,
        "health": health,
        "checks": {key: observation.checks.get(key, "UNKNOWN") for key in _REQUIRED_CHECKS},
        "findings": list(observation.findings),
        "evidence_refs": list(observation.evidence_refs),
        "next_action": next_action,
    }


def supervise_observations(
    observations: Sequence[HealthObservation],
    canonical_repositories: Sequence[str],
    route: Callable[[RoutedFinding], None] | None = None,
) -> tuple[dict, ...]:
    """Evaluate current observations and route only current non-GREEN findings.

    Repository membership is fail-closed: observations outside the supplied
    canonical registry are rejected. Routing is a notification boundary only;
    this function never mutates project state and never treats routing as
    remediation or verification.
    """
    canonical = set(canonical_repositories)
    records = []
    for observation in observations:
        if observation.repository not in canonical:
            raise ValueError(f"NON_CANONICAL_REPOSITORY:{observation.repository}")
        record = build_health_record(observation)
        records.append(record)
        if record["health"] != "GREEN" and route is not None:
            route(RoutedFinding(
                repository=observation.repository,
                commit=observation.commit,
                health=record["health"],
                findings=observation.findings,
                next_action=record["next_action"],
            ))
    return tuple(records)
