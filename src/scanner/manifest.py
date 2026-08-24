"""Machine-readable scan manifest and coverage reporting."""

from dataclasses import asdict, dataclass
from datetime import datetime, timezone

from src.scanner.confidence import InspectionCoverage


@dataclass(frozen=True)
class ScanManifest:
    scan_id: str
    repository: str
    started_at: str
    inspected_items: int
    known_items: int
    code_search_available: bool
    direct_file_access: bool
    confidence: str

    @classmethod
    def create(cls, scan_id: str, repository: str, coverage: InspectionCoverage) -> "ScanManifest":
        return cls(
            scan_id=scan_id,
            repository=repository,
            started_at=datetime.now(timezone.utc).isoformat(),
            inspected_items=coverage.inspected_items,
            known_items=coverage.known_items,
            code_search_available=coverage.code_search_available,
            direct_file_access=coverage.direct_file_access,
            confidence=coverage.confidence,
        )

    def as_dict(self) -> dict:
        return asdict(self)
