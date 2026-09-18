# Commercial Frontend — Customer-Validation Reopen Matrix

Date: 2026-09-18 (Brisbane)
Status: VERIFIED AS GATE CONTRACT / NO CUSTOMER CONTACT OR PRODUCTION AUTHORITY

## Purpose
Define exactly what evidence reopens a Commercial Frontend vertical from `BLOCKED_STABLE / CUSTOMER_VALIDATION_REQUIRED` or direct-evidence block, and what evidence is insufficient.

## Tradie reopen gate — C-CF-01
Current state: `BLOCKED_STABLE / CUSTOMER_VALIDATION_REQUIRED`.

A Tradie workflow family may reopen active evaluation only when new evidence supplies all of:
1. at least one exact residual workflow class, not a generic reconciliation/admin problem;
2. direct operator/customer evidence or another authoritative dataset for real frequency/volume;
3. direct effort evidence, normally minutes/actionable case or equivalent;
4. concrete consequence evidence;
5. named approval owner/boundary;
6. measurable resolved outcome;
7. enough trial-intent/WTP evidence to justify continuing commercial validation.

Prototype eligibility remains stronger: >=3 independent materially similar direct participants/observations plus feasible reads, approval boundary and measurable outcome.

Insufficient to reopen by itself:
- another ServiceM8/Xero help article;
- another public statement that the exception exists;
- a synthetic fixture or calculator result;
- a single anecdote without frequency/effort/consequence;
- generic interest in 'AI admin';
- technical API feasibility alone.

## Ecommerce reopen/prototype gate
Current state: direct-evidence blocked.

A candidate exception family advances when real merchant/operator evidence establishes:
- repeated affected-order frequency;
- minutes/actionable case;
- systems/manual handoffs;
- customer/financial/operational consequence;
- exact approval boundary;
- measurable resolution;
- direct trial intent;
- WTP when available.

Prototype consideration requires >=3 independent materially similar direct cases/participants plus feasible reads and a clear bounded approval surface.

Insufficient by itself:
- GlobalShopCo synthetic evidence;
- supplier/provider documentation;
- Shopify feature/API documentation;
- SF/EC fixture frequency;
- hypothetical merchant economics;
- provider integration availability.

## Evidence intake dispositions
For any new record:
- `ADMIT_DIRECT` — provenance valid, independent status known, directly relevant;
- `ADMIT_CORROBORATIVE` — platform/public/portfolio evidence useful for mechanics only;
- `DUPLICATE_UPDATE` — same participant/business/case; enrich existing record, do not increment count;
- `INDEPENDENCE_UNKNOWN` — preserve but exclude from direct threshold count;
- `CONFLICT` — preserve conflicting evidence, no optimistic averaging;
- `OUT_OF_SCOPE` — does not describe the exact workflow family;
- `REJECT_SYNTHETIC_AS_DEMAND` — fixture/scenario cannot count as customer evidence.

## Reopen decision sequence
1. verify provenance/deduplication;
2. bind evidence to one exact workflow family;
3. label every material field by source class;
4. preserve UNKNOWN/CONFLICT;
5. calculate burden only from complete direct inputs;
6. test material similarity across independent records;
7. only then update the direct-validation gate.

## Build-gate separation
Reopening commercial validation does not authorize a production frontend. Production still additionally requires stronger direct evidence, credible WTP, exact permissions/write scopes, fail-closed verification, relevant AgentOS ownership/authority/physical/Green/PRS proof and no critical security unknown.

## Stop rule
If a new cycle supplies no admissible new direct evidence, retain the blocked state and do not restart horizontal incumbent research merely to generate activity.