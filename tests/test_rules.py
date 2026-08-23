from src.analysis.rules import generate_candidates
from src.scanner.evidence import Evidence


def test_ci_without_tests_is_candidate():
    findings = generate_candidates([Evidence("ci_workflow", ".github/workflows/ci.yml", "CI")])
    assert findings[0].rule_id == "CI-WITHOUT-TEST-EVIDENCE"
    assert findings[0].classification == "Potential"


def test_env_file_is_not_claimed_as_secret_exposure():
    findings = generate_candidates([Evidence("file", ".env", "environment file")])
    assert findings[0].rule_id == "ENV-FILE-PRESENT"
    assert findings[0].classification == "Potential"
