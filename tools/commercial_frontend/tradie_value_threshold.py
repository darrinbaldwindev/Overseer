#!/usr/bin/env python3
"""Deterministic interpretation-only calculator for Commercial Frontend direct evidence.

This utility never creates demand proof, WTP proof, customer evidence, or production authority.
UNKNOWN material inputs propagate to NOT_TESTABLE.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any

UNKNOWN = "UNKNOWN"
STATUS_NOT_TESTABLE = "NOT_TESTABLE"
STATUS_INTERPRETATION_ONLY = "INTERPRETATION_ONLY"


@dataclass(frozen=True)
class ThresholdResult:
    status: str
    manual_cases_per_week: float | None
    admin_hours_per_week: float | None
    admin_cost_per_week: float | None
    admin_cost_per_year: float | None
    wtp_status: str
    demand_evidence_status: str
    production_authority: bool

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _number_or_unknown(value: Any, field: str, *, max_value: float | None = None) -> float | str:
    if value == UNKNOWN:
        return UNKNOWN
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a non-negative number or UNKNOWN")
    numeric = float(value)
    if numeric < 0:
        raise ValueError(f"{field} must be non-negative")
    if max_value is not None and numeric > max_value:
        raise ValueError(f"{field} exceeds allowed maximum {max_value}")
    return numeric


def calculate_value_threshold(record: dict[str, Any]) -> ThresholdResult:
    """Calculate comparable admin-friction value from direct evidence inputs.

    Required fields:
      payments_per_week
      manual_closure_rate          # fraction 0..1
      minutes_per_case
      loaded_admin_cost_per_hour

    Any material UNKNOWN returns NOT_TESTABLE. Calculated output remains
    interpretation-only and cannot supply WTP, demand, or production authority.
    """

    allowed = {
        "payments_per_week",
        "manual_closure_rate",
        "minutes_per_case",
        "loaded_admin_cost_per_hour",
        "consequence_notes",
        "source_ref",
    }
    unknown_fields = sorted(set(record) - allowed)
    if unknown_fields:
        raise ValueError(f"unsupported fields: {','.join(unknown_fields)}")

    payments = _number_or_unknown(record.get("payments_per_week", UNKNOWN), "payments_per_week")
    closure_rate = _number_or_unknown(record.get("manual_closure_rate", UNKNOWN), "manual_closure_rate", max_value=1.0)
    minutes = _number_or_unknown(record.get("minutes_per_case", UNKNOWN), "minutes_per_case")
    admin_cost = _number_or_unknown(record.get("loaded_admin_cost_per_hour", UNKNOWN), "loaded_admin_cost_per_hour")

    if any(value == UNKNOWN for value in (payments, closure_rate, minutes, admin_cost)):
        return ThresholdResult(
            status=STATUS_NOT_TESTABLE,
            manual_cases_per_week=None,
            admin_hours_per_week=None,
            admin_cost_per_week=None,
            admin_cost_per_year=None,
            wtp_status=UNKNOWN,
            demand_evidence_status=UNKNOWN,
            production_authority=False,
        )

    manual_cases = float(payments) * float(closure_rate)
    hours = manual_cases * float(minutes) / 60.0
    weekly_cost = hours * float(admin_cost)

    return ThresholdResult(
        status=STATUS_INTERPRETATION_ONLY,
        manual_cases_per_week=round(manual_cases, 4),
        admin_hours_per_week=round(hours, 4),
        admin_cost_per_week=round(weekly_cost, 2),
        admin_cost_per_year=round(weekly_cost * 52.0, 2),
        wtp_status=UNKNOWN,
        demand_evidence_status=UNKNOWN,
        production_authority=False,
    )
