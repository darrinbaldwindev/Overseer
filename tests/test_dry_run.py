from src.pipeline.dry_run import run_dry_scan
from src.state.portfolio_store import PortfolioStore


class Finding:
    rule_id = "RULE-1"


def test_dry_run_is_read_only_by_contract():
    calls = []

    def discover(repo):
        calls.append("discover")
        return {"repo": repo}

    def scan(snapshot):
        calls.append("scan")
        return ["evidence"]

    def analyse(evidence):
        calls.append("analyse")
        return [Finding()]

    result = run_dry_scan(
        "owner/repo", discover, scan, analyse,
        lambda finding: "fp-1", lambda findings: 99.0, PortfolioStore()
    )

    assert calls == ["discover", "scan", "analyse"]
    assert result.finding_states == ("NEW",)
    assert result.health_score == 99.0
