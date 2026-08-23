"""Minimal in-memory portfolio state store used by the orchestration layer.

A production adapter can persist the same records to SQLite or another
append-only store without changing the domain contract.
"""

from dataclasses import dataclass, field
from typing import Any

from src.state.change_history import HistoricalState, classify_change


@dataclass
class PortfolioStore:
    scans: list[dict[str, Any]] = field(default_factory=list)
    findings: dict[str, HistoricalState] = field(default_factory=dict)

    def record_scan(self, manifest: dict[str, Any]) -> None:
        self.scans.append(dict(manifest))

    def observe_finding(self, key: str, fingerprint: str) -> str:
        previous = self.findings.get(key)
        status = classify_change(previous, fingerprint)
        self.findings[key] = HistoricalState(key, fingerprint, "OPEN")
        return status

    def resolve_finding(self, key: str) -> None:
        previous = self.findings.get(key)
        if previous:
            self.findings[key] = HistoricalState(previous.key, previous.fingerprint, "RESOLVED")
