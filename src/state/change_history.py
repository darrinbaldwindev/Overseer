"""Historical change classification for findings and recommendations."""

from dataclasses import dataclass


@dataclass(frozen=True)
class HistoricalState:
    key: str
    fingerprint: str
    status: str


def classify_change(previous: HistoricalState | None, current_fingerprint: str) -> str:
    if previous is None:
        return "NEW"
    if previous.fingerprint == current_fingerprint:
        return "UNCHANGED"
    if previous.status == "RESOLVED":
        return "REOPENED"
    return "CHANGED"
