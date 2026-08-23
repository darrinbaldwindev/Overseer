"""Finding lifecycle primitives.

These helpers deliberately avoid making semantic decisions about whether a
finding is valid; the evidence/review layer supplies those decisions.
"""

from dataclasses import dataclass


VALID_STATUSES = {
    "NEW",
    "UNCHANGED",
    "IMPROVED",
    "REGRESSED",
    "RESOLVED",
    "REOPENED",
}


@dataclass(frozen=True)
class FindingKey:
    repository: str
    area: str
    signature: str

    def stable_id(self) -> str:
        repo = self.repository.split("/", 1)[-1].upper().replace("-", "_")
        area = self.area.upper().replace(" ", "_")
        signature = self.signature.upper().replace(" ", "_")[:48]
        return f"OVR-{repo}-{area}-{signature}"


def validate_status(status: str) -> str:
    if status not in VALID_STATUSES:
        raise ValueError(f"Unsupported finding status: {status}")
    return status
