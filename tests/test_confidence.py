from src.scanner.confidence import InspectionCoverage, absence_claim_allowed


def test_unindexed_repository_is_limited_confidence():
    coverage = InspectionCoverage(10, 10, code_search_available=False)
    assert coverage.confidence == "LIMITED"
    assert absence_claim_allowed(coverage) is False


def test_high_coverage_allows_absence_claim():
    coverage = InspectionCoverage(95, 100, code_search_available=True)
    assert coverage.confidence == "HIGH"
    assert absence_claim_allowed(coverage) is True
