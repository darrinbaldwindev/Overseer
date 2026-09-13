"""Conservative change detection helpers."""

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Change:
    path: str
    status: str


def compare_paths(previous: Iterable[str], current: Iterable[str]) -> list[Change]:
    def normalize(path):
        path = path.strip()
        while path.startswith("./"):
            path = path[2:]
        return path
    old = {normalize(p) for p in previous}
    new = {normalize(p) for p in current}
    changes = [Change(p, "ADDED") for p in new - old]
    changes += [Change(p, "REMOVED") for p in old - new]
    return sorted(changes, key=lambda item: (item.status, item.path))
