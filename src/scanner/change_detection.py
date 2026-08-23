"""Conservative change detection helpers."""

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Change:
    path: str
    status: str


def compare_paths(previous: Iterable[str], current: Iterable[str]) -> list[Change]:
    old = {p.strip().lstrip("./") for p in previous}
    new = {p.strip().lstrip("./") for p in current}
    changes = [Change(p, "ADDED") for p in new - old]
    changes += [Change(p, "REMOVED") for p in old - new]
    return sorted(changes, key=lambda item: (item.status, item.path))
