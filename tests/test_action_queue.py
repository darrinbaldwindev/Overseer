from src.state.action_queue import ingest_report, stable_task_id


def finding():
    return {
        "finding_id": "F-001",
        "target_repo": "darrinbaldwindev/AgentOS",
        "priority": "P0",
        "objective": "Implement executable delegation loop",
        "acceptance_criteria": ["Delegation state transitions are persisted", "Verification evidence is required"],
        "evidence_required": ["test output", "commit SHA"],
    }


def test_task_id_is_stable():
    assert stable_task_id("report-1", "F-001", "darrinbaldwindev/AgentOS") == stable_task_id("report-1", "F-001", "darrinbaldwindev/AgentOS")


def test_ingestion_is_idempotent():
    first = ingest_report("report-1", [finding()])
    second = ingest_report("report-1", [finding()], first)
    assert list(second) == list(first)
    assert len(second) == 1


def test_verified_requires_evidence():
    task = next(iter(ingest_report("report-1", [finding()]).values()))
    try:
        task.transition("verified")
        assert False, "verification without evidence must fail"
    except ValueError as exc:
        assert "evidence" in str(exc)


def test_verified_task_carries_evidence():
    task = next(iter(ingest_report("report-1", [finding()]).values()))
    task = task.transition("queued")
    task = task.__class__(**{**task.to_dict(), "evidence": ("commit:abc123",)})
    verified = task.transition("verified")
    assert verified.status == "verified"
