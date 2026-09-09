from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_ROOT = ROOT / ".overseer" / "PROJECT-OVERSEERS"
HISTORICAL_ROOT = ROOT / ".overseer" / "project-overseers"


def test_project_overseer_live_control_root_is_explicitly_canonical():
    readme = (CANONICAL_ROOT / "README.md").read_text(encoding="utf-8")
    assert ".overseer/PROJECT-OVERSEERS/" in readme
    assert "only live Project Overseer control root" in readme
    assert ".overseer/project-overseers/" in readme
    assert "historical evidence only" in readme


def test_canonical_control_state_does_not_route_to_lowercase_root():
    for relative in (".overseer/STATE.yml", ".overseer/PORTFOLIO-REGISTRY.yml"):
        text = (ROOT / relative).read_text(encoding="utf-8")
        assert ".overseer/project-overseers/" not in text


def test_historical_lowercase_tree_is_not_mistaken_for_missing_evidence():
    # Historical material is intentionally preserved. Its presence must not be
    # interpreted as a second live control root or trigger destructive cleanup.
    assert CANONICAL_ROOT.is_dir()
    if HISTORICAL_ROOT.exists():
        assert HISTORICAL_ROOT.is_dir()
