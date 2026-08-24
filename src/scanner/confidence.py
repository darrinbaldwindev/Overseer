"""Confidence model for partial or unavailable repository visibility."""

from dataclasses import dataclass


@dataclass(frozen=True)
class InspectionCoverage:
    inspected_items: int
    known_items: int
    code_search_available: bool
    direct_file_access: bool = True

    @property
    def ratio(self) -> float:
        if self.known_items <= 0:
            return 0.0
        return min(1.0, self.inspected_items / self.known_items)

    @property
    def confidence(self) -> str:
        if not self.direct_file_access:
            return "LOW"
        if not self.code_search_available:
            return "LIMITED"
        if self.ratio >= 0.9:
            return "HIGH"
        if self.ratio >= 0.5:
            return "MEDIUM"
        return "LIMITED"


def absence_claim_allowed(coverage: InspectionCoverage) -> bool:
    """Only permit a strong absence claim when inspection coverage is high."""
    return coverage.confidence == "HIGH"
