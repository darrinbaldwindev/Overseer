"""Bridge a GPTChat report into the durable Overseer action queue.

This module intentionally stops before delegation: GPTChat Repo Overseer produces
findings; GPTChat Overseer owns executor selection and delegation.
"""
from __future__ import annotations

from pathlib import Path
from typing import Mapping, Sequence

from src.state.action_store import ActionStore


def ingest_gptchat_report(
    report_id: str,
    findings: Sequence[Mapping[str, object]],
    state_path: str | Path = ".overseer/action-state.json",
) -> dict:
    """Persist actionable report findings idempotently and return task state."""
    store = ActionStore(state_path)
    return {task_id: task.to_dict() for task_id, task in store.ingest(report_id, findings).items()}
