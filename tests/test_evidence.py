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
