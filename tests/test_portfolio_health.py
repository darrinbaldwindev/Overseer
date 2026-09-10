from src.pipeline.portfolio_health import HealthObservation, build_health_record, supervise_observations


BASE_CHECKS = {
    "access": "PASS",
    "tests": "PASS",
    "security": "PASS",
    "overseer": "ACTIVE",
    "evidence": "FRESH",
    "prs": "NOT_APPLICABLE",
    "green_agent": "GREEN",
}


def observation(**overrides):
    checks = dict(BASE_CHECKS)
    checks.update(overrides.pop("checks", {}))
    return HealthObservation(
        repository=overrides.pop("repository", "owner/repo"),
        commit=overrides.pop("commit", "abcdef1234567"),
        checked_at=overrides.pop("checked_at", "2026-09-10T01:00:00Z"),
        checks=checks,
        findings=tuple(overrides.pop("findings", ())),
        evidence_refs=tuple(overrides.pop("evidence_refs", ())),
    )


def test_complete_current_evidence_can_be_green():
    record = build_health_record(observation())
    assert record["health"] == "GREEN"
    assert record["next_action"] == "none"


def test_missing_or_pending_assurance_never_infers_green():
    assert build_health_record(observation(checks={"prs": "PENDING"}))["health"] == "AMBER"
    assert build_health_record(observation(checks={"evidence": "MISSING"}))["health"] == "AMBER"
    assert build_health_record(observation(checks={"green_agent": "UNKNOWN"}))["health"] == "AMBER"


def test_failure_and_access_block_use_safer_disposition():
    assert build_health_record(observation(checks={"tests": "FAIL"}))["health"] == "RED"
    assert build_health_record(observation(checks={"access": "FAIL"}))["health"] == "BLOCKED"


def test_non_green_routes_but_routing_does_not_promote_health():
    routed = []
    first = observation(
        commit="badc0de0000001",
        checks={"evidence": "STALE", "green_agent": "AMBER"},
        findings=("STALE-EVIDENCE",),
    )
    records = supervise_observations([first], ["owner/repo"], routed.append)
    assert records[0]["health"] == "AMBER"
    assert len(routed) == 1
    assert routed[0].commit == "badc0de0000001"

    # A remediation claim is not verification. Only a fresh observation at the
    # post-remediation commit can produce a different disposition.
    second = observation(commit="f00dbabe000002", checked_at="2026-09-10T01:10:00Z")
    rescanned = supervise_observations([second], ["owner/repo"], routed.append)
    assert rescanned[0]["health"] == "GREEN"
    assert len(routed) == 1


def test_noncanonical_repository_is_rejected_before_routing():
    routed = []
    try:
        supervise_observations([observation(repository="owner/other")], ["owner/repo"], routed.append)
    except ValueError as exc:
        assert str(exc) == "NON_CANONICAL_REPOSITORY:owner/other"
    else:
        raise AssertionError("non-canonical repository must fail closed")
    assert routed == []
