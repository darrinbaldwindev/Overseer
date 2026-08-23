"""Auditable portfolio decision ledger primitives."""

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from hashlib import sha256
import json


@dataclass(frozen=True)
class EvidenceRef:
    repository: str
    ref: str
    path: str | None = None
    finding_id: str | None = None


@dataclass(frozen=True)
class DecisionRecord:
    decision_id: str
    created_at: str
    classification: str
    status: str
    title: str
    recommendation: str
    confidence: str
    evidence: tuple[EvidenceRef, ...]
    owner_required: bool = False

    def as_dict(self) -> dict:
        value = asdict(self)
        value["evidence"] = [asdict(item) for item in self.evidence]
        return value


def decision_fingerprint(record: DecisionRecord) -> str:
    """Create a deterministic fingerprint for duplicate/change detection."""
    canonical = json.dumps(record.as_dict(), sort_keys=True, separators=(",", ":"))
    return sha256(canonical.encode("utf-8")).hexdigest()


def new_decision_id(prefix: str = "OVR-DEC") -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"{prefix}-{timestamp}"
