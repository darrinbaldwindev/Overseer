from src.adapters.github_inventory import targets_from_github


def test_github_inventory_preserves_repository_boundaries():
    targets = targets_from_github([
        {
            "repository_full_name": "owner/project",
            "default_branch": "main",
            "size": 42,
            "visibility": "private",
            "archived": False,
            "is_code_search_indexed": True,
        }
    ])
    assert targets[0].full_name == "owner/project"
    assert targets[0].default_branch == "main"
    assert targets[0].private is True
    assert targets[0].code_search_indexed is True
