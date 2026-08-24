from src.state.skill_memory import Skill, SkillMemory, stable_skill_id


def make_skill(**overrides):
    values = dict(
        name="Repository reconnaissance",
        description="Inspect a repository and establish its boundaries.",
        triggers=("repository reconnaissance", "repo inspection"),
        prerequisites=("github_read",),
        steps=("discover repository", "inspect structure", "record evidence"),
        outputs=("reconnaissance report",),
        validation=("all required evidence fields are populated",),
        safety_constraints=("read-only",),
        scope="repository",
        status="validated",
        confidence=0.9,
        evidence_refs=("scan-001",),
    )
    values.update(overrides)
    return Skill(**values)


def test_skill_id_is_deterministic():
    assert stable_skill_id("Repository reconnaissance", "repository") == stable_skill_id(
        " repository reconnaissance ", "REPOSITORY"
    )


def test_skill_rejects_unsafe_counter_state():
    try:
        make_skill(success_count=2, usage_count=1)
    except ValueError as exc:
        assert "success_count" in str(exc)
    else:
        raise AssertionError("invalid counters were accepted")


def test_memory_prefers_validated_skills():
    memory = SkillMemory()
    memory.add(make_skill(status="candidate", confidence=1.0))
    memory.add(make_skill(name="Validated reconnaissance", confidence=0.8))

    results = memory.search(("repository", "reconnaissance"), ("github_read",))
    assert results[0].status == "validated"


def test_outcome_updates_usage_without_mutating_original():
    original = make_skill()
    updated = original.record_outcome(True, "2026-08-24T06:00:00Z")

    assert original.usage_count == 0
    assert updated.usage_count == 1
    assert updated.success_count == 1
    assert updated.success_rate == 1.0
