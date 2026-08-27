"""File-backed persistence for the Overseer action queue.

The file store is deliberately small and deterministic so it can serve as a
recovery layer until AgentOS supplies a transactional event/task store.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, Mapping

from .action_queue import ActionTask, ingest_report


class ActionStore:
    def __init__(self, path: str | Path = ".overseer/action-state.json") -> None:
        self.path = Path(path)

    def load(self) -> dict[str, ActionTask]:
        if not self.path.exists():
            return {}
        payload = json.loads(self.path.read_text(encoding="utf-8"))
        return {item["task_id"]: ActionTask(**item) for item in payload.get("tasks", [])}

    def save(self, tasks: Mapping[str, ActionTask]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = {"version": 1, "tasks": [tasks[k].to_dict() for k in sorted(tasks)]}
        temporary = self.path.with_suffix(self.path.suffix + ".tmp")
        temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        temporary.replace(self.path)

    def ingest(self, report_id: str, findings: Iterable[Mapping[str, object]]) -> dict[str, ActionTask]:
        tasks = ingest_report(report_id, findings, self.load())
        self.save(tasks)
        return tasks
