# Commercial Frontend — Cross-Vertical Direct-Evidence Normalization

Date: 2026-09-18 (Brisbane)
Status: VERIFIED AS INTERPRETATION CONTRACT / DIRECT DEMAND STILL UNKNOWN

## Purpose
Provide one comparable schema for Tradie, Ecommerce and later Commercial Frontend verticals without erasing vertical-specific workflow details.

The schema is for evidence interpretation only. It does not create a customer database, CRM, authority source or production runtime.

## Shared direct-evidence fields
Every vertical record should normalize the following fields when directly supplied/observed:
- workflow_family;
- participant/business independence status;
- event/case frequency per week/month;
- actionable-case frequency, distinct from transient/non-actionable events;
- minutes per actionable case;
- operator role;
- buyer role if different;
- systems crossed;
- number/type of manual handoffs;
- current resolution path;
- consequence class: customer / financial / operational / compliance / rework;
- consequence magnitude only if directly evidenced;
- read integration feasibility;
- prospective write/action scope;
- approval owner;
- approval preference;
- measurable resolved outcome;
- trial-intent exact wording;
- WTP exact wording/amount or UNKNOWN;
- acquisition/reach signal only if directly evidenced.

## Source labels per field
Each field must retain one of:
- `OBSERVED`
- `PARTICIPANT_REPORTED`
- `PARTICIPANT_ARTIFACT`
- `DERIVED_FROM_DIRECT_INPUTS`
- `PLATFORM_EVIDENCE`
- `PORTFOLIO_EVIDENCE`
- `UNKNOWN`
- `CONFLICT`

Only the first four can contribute to direct workflow burden; only explicit participant evidence may supply trial intent/WTP.

## Comparable derived measures
Derive only where all inputs are direct and complete:
- actionable cases/week;
- manual hours/week = cases/week × minutes/case / 60;
- labour burden/week only when loaded hourly cost is directly supplied/defensible;
- directly evidenced rework/contact/refund cost;
- systems crossed count;
- handoff count.

Do not derive churn, LTV, reputation cost, probability of error, annual loss, or WTP from unsupported assumptions.

## Vertical preservation
### Tradie
Keep separate:
- T1 post-payment closure;
- T2 residual ServiceM8↔Xero exception class.
Do not merge these into one generic 'admin' bucket.

### Ecommerce
Keep separate supplier/fulfilment exception families such as:
- stock/availability mismatch;
- tracking/package identity mismatch;
- fulfilment/hold state conflict;
- returns/refund/rework reconciliation.
Do not let Shopify-native automation tasks masquerade as cross-system exception evidence.

### Future verticals
A new vertical can reuse the shared fields only if its own system-of-record, trigger, manual handoff, approval boundary and measurable outcome are separately captured.

## Cross-vertical comparison rules
Cross-vertical comparison may describe:
- repeated frequency;
- operator time burden;
- consequence evidence;
- systems/handoffs complexity;
- read feasibility;
- approval clarity;
- measurable outcome clarity;
- trial intent;
- WTP evidence completeness.

Do not create a universal weighted score that automatically selects the 'best' vertical. Direct evidence remains contextual and commercial prioritisation requires an explicit later decision using actual evidence.

## Missingness policy
Missing direct input = `UNKNOWN`, not zero.
Conflicting direct inputs = `CONFLICT`, not an average.
A platform-documented feature = incumbent/integration evidence, not participant pain.
A synthetic fixture = safety/product-contract evidence, not commercial demand.

## Current disposition
Tradie C-CF-01 remains `BLOCKED_STABLE / CUSTOMER_VALIDATION_REQUIRED`.
Ecommerce remains blocked on direct evidence.
This schema is ready to normalize future real records without fabricating them.