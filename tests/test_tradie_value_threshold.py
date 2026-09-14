import unittest

from tools.commercial_frontend.tradie_value_threshold import (
    STATUS_INTERPRETATION_ONLY,
    STATUS_NOT_TESTABLE,
    UNKNOWN,
    calculate_value_threshold,
)


class TradieValueThresholdTests(unittest.TestCase):
    def test_unknown_material_input_fails_closed(self):
        result = calculate_value_threshold({
            "payments_per_week": 25,
            "manual_closure_rate": UNKNOWN,
            "minutes_per_case": 6,
            "loaded_admin_cost_per_hour": 42,
        })
        self.assertEqual(result.status, STATUS_NOT_TESTABLE)
        self.assertIsNone(result.admin_cost_per_week)
        self.assertEqual(result.wtp_status, UNKNOWN)
        self.assertEqual(result.demand_evidence_status, UNKNOWN)
        self.assertFalse(result.production_authority)

    def test_synthetic_numbers_calculate_but_never_become_demand_or_wtp_evidence(self):
        result = calculate_value_threshold({
            "payments_per_week": 30,
            "manual_closure_rate": 0.4,
            "minutes_per_case": 5,
            "loaded_admin_cost_per_hour": 48,
            "consequence_notes": "synthetic fixture only",
            "source_ref": "fixture:TR-VALUE-001",
        })
        self.assertEqual(result.status, STATUS_INTERPRETATION_ONLY)
        self.assertEqual(result.manual_cases_per_week, 12.0)
        self.assertEqual(result.admin_hours_per_week, 1.0)
        self.assertEqual(result.admin_cost_per_week, 48.0)
        self.assertEqual(result.admin_cost_per_year, 2496.0)
        self.assertEqual(result.wtp_status, UNKNOWN)
        self.assertEqual(result.demand_evidence_status, UNKNOWN)
        self.assertFalse(result.production_authority)

    def test_manual_closure_rate_above_one_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "manual_closure_rate exceeds allowed maximum"):
            calculate_value_threshold({
                "payments_per_week": 30,
                "manual_closure_rate": 1.01,
                "minutes_per_case": 5,
                "loaded_admin_cost_per_hour": 48,
            })

    def test_negative_cost_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "loaded_admin_cost_per_hour must be non-negative"):
            calculate_value_threshold({
                "payments_per_week": 30,
                "manual_closure_rate": 0.4,
                "minutes_per_case": 5,
                "loaded_admin_cost_per_hour": -1,
            })

    def test_unknown_fields_fail_closed_instead_of_expanding_authority(self):
        with self.assertRaisesRegex(ValueError, "unsupported fields:publish_now"):
            calculate_value_threshold({
                "payments_per_week": 30,
                "manual_closure_rate": 0.4,
                "minutes_per_case": 5,
                "loaded_admin_cost_per_hour": 48,
                "publish_now": True,
            })


if __name__ == "__main__":
    unittest.main()
