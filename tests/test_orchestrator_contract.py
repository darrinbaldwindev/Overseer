import pytest

from src.orchestrator import run_repository_scan, TransactionState, run_delegated_transaction


def test_repository_scan_requires_fresh_snapshot():
    calls = []

    def discover(repo):
        calls.append("discover")
        return {"commit": "abc", "fresh": True}

    result = run_repository_scan(repo := "owner/repo", discover, lambda s: [s], lambda e: [], lambda f: 1.0)

    assert result.repository == repo
    assert result.status == "complete"
    assert calls == ["discover"]


def test_delegated_transaction_does_not_mark_verified_without_verification():
    states = []

    result = run_delegated_transaction(
        task_id="TEST-001",
        repository="owner/repo",
        worker="worker-a",
        base_snapshot={"commit": "abc", "fresh": True},
        execute=lambda: {"result": "ok", "commit": "def"},
        verify=lambda result: False,
        record=lambda state: states.append(state),
    )

    assert result.state is TransactionState.COMPLETED_UNVERIFIED
    assert states[-1] is TransactionState.COMPLETED_UNVERIFIED


def test_delegated_transaction_requires_fresh_base():
    with pytest.raises(ValueError, match="fresh"):
        run_delegated_transaction(
            task_id="TEST-002",
            repository="owner/repo",
            worker="worker-a",
            base_snapshot={"commit": "abc", "fresh": False},
            execute=lambda: {"result": "ok"},
            verify=lambda result: True,
            record=lambda state: None,
        )
