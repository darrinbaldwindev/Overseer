from src.state.portfolio_store import PortfolioStore


def test_store_tracks_scan_and_finding_history():
    store = PortfolioStore()
    store.record_scan({"scan_id": "scan-1"})
    assert len(store.scans) == 1

    assert store.observe_finding("finding-1", "fp-a") == "NEW"
    assert store.observe_finding("finding-1", "fp-a") == "UNCHANGED"

    store.resolve_finding("finding-1")
    assert store.observe_finding("finding-1", "fp-b") == "REOPENED"
