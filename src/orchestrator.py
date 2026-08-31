"""Deterministic orchestration and evidence-gated transaction contracts.

The worker supplies repository discovery, execution and persistence adapters.
This module defines the safety-critical order in which those capabilities may
be used. It deliberately does not grant autonomous permission to change
credentials, permissions, protected schedules, or other owner-controlled state.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Callable, Iterable, Any


@dataclass(frozen=True)
class ScanResult:
    repository: str
    status: str
    evidence_count: int
    finding_count: int
    health_score: float | None


class TransactionState(str, Enum):
    ASSIGNED = "assigned"
    ACKNOWLEDGED = "acknowledged"
    EXECUTING = "executing"
    COMPLETED_UNVERIFIED = "completed_unverified"
    VERIFIED = "verified"
    FAILED = "failed"
    BLOCKED = "blocked"


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


def run_delegated_transaction(
    *,
    task_id: str,
    repository: str,
    worker: str,
    base_snapshot: Any,
    execute: Callable[[], Any],
    verify: Callable[[Any], bool],
    record: Callable[[TransactionState], None],
) -> Any:
    """Run a worker transaction only from a fresh base and never overclaim verification.

    The caller owns the actual repository/provider adapters. This contract makes
    the lifecycle observable and prevents a successful execution from being
    treated as VERIFIED until an independent verifier returns true.
    """
    del task_id, repository, worker  # retained as audit context at adapter level
    if not isinstance(base_snapshot, dict) or not base_snapshot.get("fresh"):
        raise ValueError("delegated transaction requires a fresh repository snapshot")
    if not base_snapshot.get("commit"):
        raise ValueError("delegated transaction requires a base commit")

    record(TransactionState.ACKNOWLEDGED)
    record(TransactionState.EXECUTING)
    try:
        result = execute()
    except Exception:
        record(TransactionState.FAILED)
        raise

    if verify(result):
        record(TransactionState.VERIFIED)
        return result

    record(TransactionState.COMPLETED_UNVERIFIED)
    return result
