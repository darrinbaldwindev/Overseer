from src.state.change_history import HistoricalState, classify_change


def test_new_state():
    assert classify_change(None, "abc") == "NEW"


def test_unchanged_state():
    previous = HistoricalState("f-1", "abc", "OPEN")
    assert classify_change(previous, "abc") == "UNCHANGED"


def test_reopened_state():
    previous = HistoricalState("f-1", "abc", "RESOLVED")
    assert classify_change(previous, "def") == "REOPENED"
