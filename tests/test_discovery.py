from src.discovery.portfolio import normalize_repositories, portfolio_delta


def test_normalize_repositories_is_stable():
    items = [
        {"id": 2, "full_name": "zeta/project", "default_branch": "main", "visibility": "private"},
        {"id": 1, "full_name": "alpha/project", "default_branch": "main", "visibility": "public"},
    ]
    result = normalize_repositories(items)
    assert [item.full_name for item in result] == ["alpha/project", "zeta/project"]


def test_portfolio_delta_detects_added_and_removed():
    previous = [{"id": 1, "full_name": "alpha/project"}]
    current = normalize_repositories([
        {"id": 2, "full_name": "beta/project", "default_branch": "main", "visibility": "private"},
    ])
    assert portfolio_delta(previous, current) == {
        "ADDED": ["beta/project"],
        "REMOVED_FROM_ACCESS": ["alpha/project"],
    }
