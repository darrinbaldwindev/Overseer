"""Deterministic portfolio discovery primitives for Overseer.

The Manus Desktop agent remains the orchestrator. This module defines the
normalization contract that runtime adapters should satisfy.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable


@dataclass(frozen=True)
class RepositorySnapshot:
    repository_id: int | str
    full_name: str
    default_branch: str
    visibility: str
    archived: bool
    permissions: dict[str, bool] = field(default_factory=dict)
    first_seen: str | None = None
    last_seen: str | None = None
    last_commit: str | None = None

    @classmethod
    def from_github(cls, repository: dict[str, Any]) -> "RepositorySnapshot":
        permissions = repository.get("permissions") or {}
        now = datetime.now(timezone.utc).isoformat()
        return cls(
            repository_id=repository.get("id", repository.get("full_name", "unknown")),
            full_name=repository.get("full_name", "unknown/unknown"),
            default_branch=repository.get("default_branch", "main"),
            visibility=repository.get("visibility", "unknown"),
            archived=bool(repository.get("archived", False)),
            permissions={
                "admin": bool(permissions.get("admin", False)),
                "maintain": bool(permissions.get("maintain", False)),
                "push": bool(permissions.get("push", False)),
                "triage": bool(permissions.get("triage", False)),
                "pull": bool(permissions.get("pull", False)),
            },
            first_seen=now,
            last_seen=now,
        )


def normalize_repositories(items: Iterable[dict[str, Any]]) -> list[RepositorySnapshot]:
    """Normalize raw GitHub repository objects and return stable ordering."""
    snapshots = [RepositorySnapshot.from_github(item) for item in items]
    return sorted(snapshots, key=lambda item: item.full_name.lower())


def portfolio_delta(
    previous: Iterable[dict[str, Any]], current: Iterable[RepositorySnapshot]
) -> dict[str, list[str]]:
    """Return conservative repository-level portfolio changes."""
    previous_by_id = {str(item.get("id")): item for item in previous if item.get("id") is not None}
    current_by_id = {str(item.repository_id): item for item in current}

    added = [item.full_name for key, item in current_by_id.items() if key not in previous_by_id]
    removed = [item.get("full_name", key) for key, item in previous_by_id.items() if key not in current_by_id]

    return {
        "ADDED": sorted(added, key=str.lower),
        "REMOVED_FROM_ACCESS": sorted(removed, key=str.lower),
    }
