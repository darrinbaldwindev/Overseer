"""Provider-neutral transaction ledger contract for Overseer worker jobs.

This module is intentionally deterministic. It records lifecycle transitions and
rejects invalid transitions so scheduler/receiver events cannot be promoted to
worker success without evidence.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class State(str, Enum):
    CREATED = "CREATED"
    DISPATCHED = "DISPATCHED"
    RECEIVED = "RECEIVED"
    ACKNOWLEDGED = "ACKNOWLEDGED"
    EXECUTING = "EXECUTING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    BLOCKED = "BLOCKED"
    MISSED = "MISSED"
    EVIDENCED = "EVIDENCED"
    VERIFIED = "VERIFIED"


_TERMINAL_EXECUTION = {State.COMPLETED, State.FAILED, State.BLOCKED, State.MISSED}

_ALLOWED = {
    State.CREATED: {State.DISPATCHED, State.BLOCKED},
    State.DISPATCHED: {State.RECEIVED, State.MISSED, State.BLOCKED},
    State.RECEIVED: {State.ACKNOWLEDGED, State.MISSED, State.BLOCKED},
    State.ACKNOWLEDGED: {State.EXECUTING, State.BLOCKED},
    State.EXECUTING: _TERMINAL_EXECUTION,
    State.COMPLETED: {State.EVIDENCED},
    State.FAILED: {State.EVIDENCED},
    State.BLOCKED: {State.EVIDENCED},
    State.MISSED: {State.EVIDENCED},
    State.EVIDENCED: {State.VERIFIED},
    State.VERIFIED: set(),
}


@dataclass
class Transaction:
    transaction_id: str
    overseer: str
    worker: str
    repository: str
    base_commit: str
    requested_capabilities: tuple[str, ...] = ()
    state: State = State.CREATED
    events: list[dict[str, Any]] = field(default_factory=list)
    result_commit: str | None = None
    evidence: list[str] = field(default_factory=list)
    verification_evidence: list[str] = field(default_factory=list)

    def transition(self, state: State, *, evidence: str | None = None) -> None:
        if state not in _ALLOWED[self.state]:
            raise ValueError(f"invalid transition: {self.state} -> {state}")
        if state == State.VERIFIED and not self.verification_evidence:
            raise ValueError("VERIFIED requires independent verification evidence")
        if state == State.EVIDENCED and not self.evidence:
            raise ValueError("EVIDENCED requires persisted evidence")
        self.state = state
        event = {"state": state.value}
        if evidence:
            event["evidence"] = evidence
            self.evidence.append(evidence)
        self.events.append(event)

    def verify(self, evidence: str) -> None:
        if self.state != State.EVIDENCED:
            raise ValueError("verification requires EVIDENCED state")
        self.verification_evidence.append(evidence)
        self.transition(State.VERIFIED, evidence=evidence)


class TransactionLedger:
    def __init__(self) -> None:
        self._items: dict[str, Transaction] = {}

    def create(self, transaction_id: str, **kwargs: Any) -> Transaction:
        if transaction_id in self._items:
            raise ValueError(f"duplicate transaction_id: {transaction_id}")
        item = Transaction(transaction_id=transaction_id, **kwargs)
        self._items[transaction_id] = item
        return item

    def get(self, transaction_id: str) -> Transaction:
        return self._items[transaction_id]

    def counts(self) -> dict[str, int]:
        counts = {state.value: 0 for state in State}
        for item in self._items.values():
            counts[item.state.value] += 1
        return counts
