from src.state.decision_ledger import DecisionRecord, EvidenceRef, decision_fingerprint


def make_record():
    return DecisionRecord(
        decision_id="OVR-DEC-1",
        created_at="2026-08-24T00:00:00Z",
        classification="R2",
        status="OPEN",
        title="Example recommendation",
        recommendation="Inspect the affected integration",
        confidence="High",
        evidence=(EvidenceRef("owner/project", "abc123", "src/app.py", "OVR-PROJECT-SECURITY-EXAMPLE"),),
    )


def test_decision_fingerprint_is_stable():
    assert decision_fingerprint(make_record()) == decision_fingerprint(make_record())


def test_evidence_is_embedded_in_record():
    record = make_record()
    assert record.as_dict()["evidence"][0]["path"] == "src/app.py"
