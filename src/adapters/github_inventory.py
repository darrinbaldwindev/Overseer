"""Adapter contract for turning GitHub repository metadata into scan targets."""

from dataclasses import dataclass
from typing import Any, Iterable


@dataclass(frozen=True)
class RepositoryTarget:
    full_name: str
    default_branch: str
    size_kb: int
    private: bool
    archived: bool
    code_search_indexed: bool


def targets_from_github(repositories: Iterable[dict[str, Any]]) -> tuple[RepositoryTarget, ...]:
    return tuple(
        RepositoryTarget(
            full_name=repo["repository_full_name"],
            default_branch=repo["default_branch"],
            size_kb=repo.get("size", 0),
            private=repo.get("visibility") == "private",
            archived=repo.get("archived", False),
            code_search_indexed=repo.get("is_code_search_indexed", False),
        )
        for repo in repositories
    )
