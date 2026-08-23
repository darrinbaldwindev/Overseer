from src.scanner.reconnaissance import classify_paths


def test_reconnaissance_extracts_project_signals():
    evidence = classify_paths([
        "README.md",
        "pyproject.toml",
        "src/main.py",
        "tests/test_main.py",
        ".github/workflows/ci.yml",
        "Dockerfile",
    ])

    assert "python" in evidence.languages
    assert evidence.signals["has_tests"] is True
    assert evidence.signals["has_ci"] is True
    assert evidence.signals["has_documentation"] is True
    assert evidence.signals["has_infrastructure"] is True
    assert evidence.entrypoint_candidates == ("src/main.py",)
