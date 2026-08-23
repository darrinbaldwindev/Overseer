"""Scan manifest primitives."""

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import uuid


@dataclass(frozen=True)
class ScanManifest:
    scan_id: str
    started_at: str
    control_plane_commit: str
    scan_engine_version: str
    mode: str = "observe_report"

    @classmethod
    def start(cls, control_plane_commit: str, scan_engine_version: str) -> "ScanManifest":
        now = datetime.now(timezone.utc).isoformat()
        return cls(
            scan_id=f"OVR-SCAN-{uuid.uuid4().hex[:12].upper()}",
            started_at=now,
            control_plane_commit=control_plane_commit,
            scan_engine_version=scan_engine_version,
        )

    def as_dict(self) -> dict[str, str]:
        return asdict(self)
