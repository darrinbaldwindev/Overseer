from src.analysis.scoring import FindingScore, health_score


def test_empty_portfolio_is_healthy():
    assert health_score([]) == 100.0


def test_critical_finding_caps_score():
    assert health_score([FindingScore("security", "Critical")]) <= 49.0


def test_unknown_values_do_not_create_unjustified_penalty():
    assert health_score([FindingScore("unknown", "Unknown")]) == 100.0
