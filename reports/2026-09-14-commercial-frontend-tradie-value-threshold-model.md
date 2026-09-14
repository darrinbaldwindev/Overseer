# Commercial Frontend — Tradie Value-Threshold Interpretation Model

Date: 2026-09-14

## Mission

Define CF-B007: a deterministic interpretation model for future direct-validation evidence on the Xero-paid invoice administrative-closure wedge.

This is **not customer evidence** and must never be used as proof of demand, willingness-to-pay, ROI or market size.

## Inputs

All inputs are supplied from a real participant/observed workflow. Missing critical inputs remain `UNKNOWN`.

Required quantitative inputs:

- `payments_per_week`
- `manual_closure_rate` as a fraction from 0 to 1
- `minutes_per_manual_case`
- `loaded_admin_cost_per_hour`

Optional consequence inputs:

- `error_cases_per_month`
- `minutes_per_error_case`
- `loaded_error_handler_cost_per_hour`
- `complaints_per_month`
- `minutes_per_complaint`
- `loaded_complaint_handler_cost_per_hour`
- qualitative consequence notes: delayed receipt, duplicated communication, accounting confusion, customer complaint, rework, manager escalation.

Commercial validation inputs, recorded separately and never inferred:

- `trial_interest`: yes/no/conditional/unknown
- `willingness_to_pay_signal`: exact participant wording or explicit amount/unknown
- `approval_preference`: automatic / approval-first / read-only / unknown
- `buyer_role`
- `current_operator_role`

## Deterministic calculations

### Manual closure cases per week

`manual_cases_per_week = payments_per_week × manual_closure_rate`

### Manual admin hours per week

`manual_hours_per_week = manual_cases_per_week × minutes_per_manual_case / 60`

### Manual admin labour cost per week

`manual_labour_cost_per_week = manual_hours_per_week × loaded_admin_cost_per_hour`

### Annualized labour-equivalent value

`annual_manual_labour_cost = manual_labour_cost_per_week × operating_weeks_per_year`

`operating_weeks_per_year` must be participant-supplied or explicitly selected as a scenario assumption. It is not silently fixed at 52.

### Optional error/rework cost

When all relevant error inputs are present:

`error_cost_per_month = error_cases_per_month × minutes_per_error_case / 60 × loaded_error_handler_cost_per_hour`

### Optional complaint handling cost

When all relevant complaint inputs are present:

`complaint_cost_per_month = complaints_per_month × minutes_per_complaint / 60 × loaded_complaint_handler_cost_per_hour`

These are labour-equivalent interpretation values only. They exclude goodwill, churn, late-payment effects, legal/compliance consequences and accounting correction costs unless directly evidenced.

## UNKNOWN propagation

If any required input for a metric is missing, that metric is `UNKNOWN`.

Examples:

- known payments/week + unknown manual closure rate -> manual cases/week UNKNOWN;
- known cases + unknown minutes/case -> hours and labour cost UNKNOWN;
- known hours + unknown loaded cost -> time value known, labour-dollar value UNKNOWN;
- qualitative complaint pain without complaint frequency -> complaint-cost metric UNKNOWN.

A missing input must never be replaced by an industry average without separately labeling that average as a scenario/hypothesis.

## Evidence quality labels

Each input must carry one of:

- `OBSERVED` — directly observed from workflow/system records;
- `PARTICIPANT_REPORTED` — stated by operator/business participant;
- `DERIVED` — mathematically derived from observed/reported inputs;
- `SCENARIO_ONLY` — intentionally hypothetical sensitivity input;
- `UNKNOWN`.

No `SCENARIO_ONLY` value may be promoted into direct customer evidence.

## Interpretation bands

This model does not define universal commercial pass/fail dollar thresholds. Instead it supports comparison between participants and surfaces where more evidence is needed.

Recommended interpretation:

### Low-frequency / low-friction

If direct evidence shows very few manual cases and trivial minutes/case, the wedge may be too narrow even if technically elegant. Do not broaden the claim; test the next Tradie exception workflow.

### Frequent but cheap

If cases are frequent but labour-equivalent value is small, investigate whether error prevention, complaint avoidance, owner attention or multi-step context switching is the actual value driver. Do not invent those values.

### Frequent and material

If multiple independent businesses show meaningful weekly admin hours/cost plus trial interest, the workflow becomes stronger prototype evidence, subject to the existing ≥3 participant gate and technical integration/authority conditions.

### High pain but rare

A rare workflow with serious consequence may still matter, but it is a separate risk/exception product hypothesis. Do not blend it into the routine admin-time ROI metric.

## Participant comparison row

For each direct-validation participant capture:

| Field | Value |
|---|---|
| participant/workflow ID | |
| evidence type | OBSERVED / PARTICIPANT_REPORTED |
| payments/week | |
| manual closure rate | |
| manual cases/week | DERIVED |
| minutes/case | |
| manual hours/week | DERIVED |
| loaded admin cost/hour | |
| labour-equivalent cost/week | DERIVED |
| current operator | |
| approval preference | |
| error/complaint consequence | |
| trial interest | |
| WTP signal | exact evidence / UNKNOWN |
| confidence/notes | |

## Prototype-gate use

This model supports, but does not replace, the existing Commercial Frontend gate.

A read-only/prototype recommendation still requires at least three independent materially similar participants/observations showing:

- the same or materially similar pain;
- enough frequency/consequence to matter;
- feasible integration reads;
- a clear approval boundary;
- a measurable outcome.

The calculator alone cannot satisfy any of those conditions.

## Production-gate use

Production still requires the broader direct-evidence threshold, repeated trial intent, credible WTP signals, exact permission/write contracts, fail-closed verification and relevant AgentOS safety/assurance evidence.

## Decision

CF-B007 is **VERIFIED AS INTERPRETATION MODEL / DIRECT DEMAND STILL UNKNOWN**.

No participant values, frequency, savings, ROI or willingness-to-pay were invented.
