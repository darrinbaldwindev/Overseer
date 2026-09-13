from src.scanner.evidence import extract_evidence


def test_extract_evidence_from_tree():
    result = extract_evidence([
        "README.md",
        "pyproject.toml",
        ".github/workflows/ci.yml",
        "tests/test_app.py",
        "Dockerfile",
    ])
    assert {(item.kind, item.path) for item in result} == {
        ("documentation", "README.md"),
        ("dependency_manifest", "pyproject.toml"),
        ("ci_workflow", ".github/workflows/ci.yml"),
        ("test", "tests/test_app.py"),
        ("container", "Dockerfile"),
    }


def test_root_and_nested_manifests_and_dot_prefixed_workflow_survive_normalisation():
    paths = ['./.github/workflows/test.yml', 'go.mod', 'Cargo.toml', 'app/pyproject.toml', 'notpackage.json']
    result = {(e.kind, e.path) for e in extract_evidence(paths)}
    assert result == {('ci_workflow', '.github/workflows/test.yml'), ('dependency_manifest', 'go.mod'),
                      ('dependency_manifest', 'Cargo.toml'), ('dependency_manifest', 'app/pyproject.toml')}


def test_change_detection_does_not_collapse_dotfiles_into_different_paths():
    from src.scanner.change_detection import compare_paths
    result = {(c.path, c.status) for c in compare_paths(['./.env'], ['env'])}
    assert result == {('.env', 'REMOVED'), ('env', 'ADDED')}
