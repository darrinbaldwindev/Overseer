import pytest

from src.transactionLedger import State, TransactionLedger


def make_transaction():
    ledger = TransactionLedger()
    tx = ledger.create(
        "TEST-006-TX-001",
        overseer="GPTChat Overseer",
        worker="Manus",
        repository="darrinbaldwindev/Overseer",
        base_commit="fresh-base",
        requested_capabilities=("repository.read", "repository.write"),
    )
    return ledger, tx


def test_verified_requires_full_evidence_gated_lifecycle():
    ledger, tx = make_transaction()
    tx.transition(State.DISPATCHED)
    tx.transition(State.RECEIVED)
    tx.transition(State.ACKNOWLEDGED)
    tx.transition(State.EXECUTING)
    tx.transition(State.COMPLETED, evidence="result-created")
    tx.transition(State.EVIDENCED, evidence="persisted-result")
    tx.verify("independent-verification")

    assert tx.state is State.VERIFIED
    assert ledger.counts()[State.VERIFIED.value] == 1


def test_completion_without_evidence_cannot_be_marked_evidenced():
    _, tx = make_transaction()
    tx.transition(State.DISPATCHED)
    tx.transition(State.RECEIVED)
    tx.transition(State.ACKNOWLEDGED)
    tx.transition(State.EXECUTING)
    tx.transition(State.COMPLETED)
    with pytest.raises(ValueError, match="EVIDENCED requires persisted evidence"):
        tx.transition(State.EVIDENCED)


def test_verification_without_independent_evidence_is_rejected():
    _, tx = make_transaction()
    tx.transition(State.DISPATCHED)
    tx.transition(State.RECEIVED)
    tx.transition(State.ACKNOWLEDGED)
    tx.transition(State.EXECUTING)
    tx.transition(State.COMPLETED, evidence="result")
    tx.transition(State.EVIDENCED, evidence="persisted")
    # Deliberately exercise the guard directly; no verifier evidence exists yet.
    tx.verification_evidence.clear()
    with pytest.raises(ValueError, match="VERIFIED requires independent verification evidence"):
        tx.transition(State.VERIFIED)


def test_duplicate_transaction_id_is_rejected():
    ledger, _ = make_transaction()
    with pytest.raises(ValueError, match="duplicate transaction_id"):
        ledger.create(
            "TEST-006-TX-001",
            overseer="GPTChat Overseer",
            worker="Manus",
            repository="darrinbaldwindev/Overseer",
            base_commit="fresh-base",
        )


def test_missed_transaction_remains_distinct_from_success():
    ledger = TransactionLedger()
    tx = ledger.create(
        "TEST-006-TX-SILENT",
        overseer="GPTChat Overseer",
        worker="Manus",
        repository="darrinbaldwindev/Overseer",
        base_commit="fresh-base",
    )
    tx.transition(State.DISPATCHED)
    tx.transition(State.MISSED, evidence="ack-window-expired")
    tx.transition(State.EVIDENCED, evidence="miss-persisted")

    counts = ledger.counts()
    assert counts[State.MISSED.value] == 0
    assert counts[State.EVIDENCED.value] == 1
    assert counts[State.VERIFIED.value] == 0
