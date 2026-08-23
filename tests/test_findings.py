from src.findings.lifecycle import FindingKey, validate_status


def test_finding_key_is_stable():
    key = FindingKey("darrinbaldwindev/AgentOS", "security", "secret handling")
    assert key.stable_id() == "OVR-AGENTOS-SECURITY-SECRET_HANDLING"


def test_status_validation():
    assert validate_status("NEW") == "NEW"

    try:
        validate_status("INVALID")
    except ValueError:
        pass
    else:
        raise AssertionError("invalid status must fail validation")
