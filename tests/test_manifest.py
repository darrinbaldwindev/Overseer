from src.scanner.confidence import InspectionCoverage
from src.scanner.manifest import ScanManifest


def test_manifest_records_limited_visibility():
    manifest = ScanManifest.create(
        "scan-1",
        "owner/repo",
        InspectionCoverage(10, 10, code_search_available=False),
    )
    assert manifest.repository == "owner/repo"
    assert manifest.confidence == "LIMITED"
    assert manifest.code_search_available is False
    assert manifest.as_dict()["inspected_items"] == 10
