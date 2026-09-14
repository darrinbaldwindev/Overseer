# Commercial Frontend — Ecommerce exception value-threshold model

Date: 2026-09-14 Brisbane
Owner: Commercial Frontend Overseer
Status: INTERPRETATION MODEL / NOT CUSTOMER EVIDENCE

## Purpose
Provide a deterministic way to compare future merchant interview/observation evidence for the Ecommerce AI Operations exception wedge without inventing frequency, economics, ROI or willingness-to-pay.

This model does not prove demand. It only normalizes direct evidence once collected.

## Required direct inputs
For each participant/workflow, capture:
- `orders_per_week`
- `exception_rate` (fraction of orders needing manual cross-system intervention)
- `minutes_per_exception`
- `loaded_admin_cost_per_hour`
- `rework_cases_per_week` if separately observed
- `minutes_per_rework_case`
- `customer_contact_cases_per_week` if separately observed
- `minutes_per_customer_contact`
- `refund_or_credit_cost_per_week` if directly known
- `customer_promise_breach_cases_per_week` if directly observed
- `operator_role`
- `systems_touched`
- `approval_required`
- `current_resolution_path`
- `trial_interest`
- `stated_wtp` only when participant actually states it

Critical absent values remain `UNKNOWN`.

## Core deterministic calculations

### Manual exception cases/week
`exception_cases_per_week = orders_per_week × exception_rate`

### Direct exception handling hours/week
`exception_hours_per_week = exception_cases_per_week × minutes_per_exception / 60`

### Direct exception handling labour cost/week
`exception_labour_cost_per_week = exception_hours_per_week × loaded_admin_cost_per_hour`

### Optional observed rework labour cost/week
`rework_labour_cost_per_week = rework_cases_per_week × minutes_per_rework_case / 60 × loaded_admin_cost_per_hour`

### Optional observed customer-contact labour cost/week
`customer_contact_labour_cost_per_week = customer_contact_cases_per_week × minutes_per_customer_contact / 60 × loaded_admin_cost_per_hour`

### Known weekly operational burden
Where every included term is directly evidenced:
`known_weekly_burden = exception_labour_cost_per_week + rework_labour_cost_per_week + customer_contact_labour_cost_per_week + refund_or_credit_cost_per_week`

Do not substitute assumed refund, churn, reputation, chargeback or lifetime-value figures.

## UNKNOWN propagation
- Missing `orders_per_week`, `exception_rate`, `minutes_per_exception`, or `loaded_admin_cost_per_hour` => direct labour value = `UNKNOWN`.
- Missing optional consequence inputs do not become zero; show them as `UNKNOWN / NOT INCLUDED`.
- If exception-rate evidence is anecdotal rather than measured, label the result `PARTICIPANT ESTIMATE`, not verified operational data.
- If one participant has multiple materially different exception classes, calculate them separately before any roll-up.

## Interpretation bands
No universal commercial threshold is imposed.

Instead, compare direct participants on:
1. repeated exception frequency;
2. time burden;
3. consequence severity;
4. number of systems/handoffs;
5. approval clarity;
6. ability to measure success;
7. trial intent;
8. stated WTP.

A high modeled burden without trial/WTP evidence is still not commercial validation. A lower labour burden may still matter where promise breach, refund or customer-impact consequences are directly evidenced.

## Suggested evidence output per participant
- direct evidence classification;
- calculated cases/week;
- calculated hours/week;
- calculated direct labour cost/week;
- separately listed known consequence cost;
- unknown consequence fields;
- current tools/systems;
- exact manual handoffs;
- approval boundary;
- smallest desired outcome;
- trial interest;
- stated WTP or `UNKNOWN`.

## Example mechanics only
A worked example may be used in testing only when every number is marked synthetic. Synthetic examples must never be rolled into customer averages or demand claims.

## Build-gate relationship
This model cannot clear CF-D002 by itself. Prototype eligibility still requires at least 3 independent materially similar direct participants/observations plus feasible reads, a clear approval boundary and measurable outcome.

Production eligibility remains stronger: approximately 10 relevant direct cases/equivalent, repeated trial intent, credible WTP signals, exact permission/write actions, fail-closed verification and relevant AgentOS proof.

Classification: `VERIFIED INTERPRETATION MODEL / DIRECT DEMAND UNKNOWN`.