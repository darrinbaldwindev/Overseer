# Commercial Frontend — Ecommerce Direct-Validation Packet

**Date:** 2026-09-14 Brisbane  
**Status:** PARTICIPANT EVIDENCE CAPTURE / NO CUSTOMER EVIDENCE YET

## Purpose
Capture real merchant/operator evidence for the Ecommerce AI Operations wedge: supplier/fulfilment exceptions that require coordination across Shopify and external supplier/fulfilment systems.

This packet operationalizes the existing Ecommerce value-threshold model. It does not treat public documentation, GlobalShopCo fixtures, synthetic exception cases or provider capability research as direct customer evidence.

## Candidate workflow under test
`Shopify order -> supplier/fulfilment exception -> exact identity/provenance check -> customer-promise impact assessment -> human approval -> future bounded Shopify/customer action -> reread verification`

## Participant eligibility
Prefer participants who directly operate or supervise:
- Shopify stores with external suppliers, dropship providers or fulfilment partners;
- order exception handling;
- inventory/stock reconciliation;
- fulfilment/tracking reconciliation;
- customer communication/refund/rework arising from supplier exceptions.

Record participant role and actual systems used. Do not assume all Shopify merchants have the same workflow.

## Evidence classes
- `VERIFIED CUSTOMER EVIDENCE` — direct interview or observed workflow.
- `VERIFIED PLATFORM EVIDENCE` — provider/Shopify documentation supporting feasibility only.
- `PORTFOLIO EVIDENCE` — GlobalShopCo or other internal project observations; not customer validation.
- `INFERENCE`
- `HYPOTHESIS`
- `UNKNOWN`

## Core capture fields
For each participant/observed workflow record:
1. business type and approximate order volume band;
2. participant role;
3. Shopify plan/setup if relevant and voluntarily known;
4. supplier/fulfilment systems actually used;
5. affected orders per week/month;
6. exception rate or count;
7. top exception types, ranked by frequency;
8. systems/screens checked per exception;
9. manual steps/handoffs;
10. minutes per case;
11. people/roles involved;
12. current workaround;
13. customer-promise consequence;
14. refund/replacement/rework consequence;
15. support/customer-contact consequence;
16. margin consequence only when participant can evidence it;
17. approval decision and who owns it;
18. what action must never happen automatically;
19. acceptable read-only/preparation automation;
20. acceptable approval-gated action;
21. measurable outcome the participant would trust;
22. willingness to trial;
23. stated WTP or budget context, if directly supplied;
24. integration/security objections;
25. evidence confidence and notes.

## Exception taxonomy prompt
Ask which of these occur in the participant's real operation; never mark one present merely because it exists in a synthetic fixture:
- supplier stock unknown/mismatch;
- SKU or variant identity mismatch;
- freight/cost unknown;
- supplier fulfilment identity unknown;
- supplier/channel permission problem;
- tracking missing;
- tracking stale/conflicting;
- late dispatch/customer promise at risk;
- split fulfilment/package ambiguity;
- order/hold/release exception;
- duplicate/replayed update;
- refund/replacement/rework coordination;
- other participant-defined exception.

## Value-threshold interpretation
Only when the participant supplies sufficient direct inputs, calculate:

`weekly manual exception cases = orders/week × directly evidenced exception rate`

`weekly admin hours = weekly manual exception cases × minutes/case / 60`

`weekly admin cost = weekly admin hours × participant-provided loaded admin hourly cost`

If any material input is absent, the derived result is `UNKNOWN / NOT TESTABLE`.

Consequences such as refunds, replacements, customer contacts or margin impact remain separate observed fields. Do not invent churn, LTV, average refund cost, contribution margin or WTP.

## Workflow observation template
For one real exception, capture the sequence without credentials/secrets:
- trigger/event noticed;
- first system checked;
- exact identity used to correlate order/SKU/variant/package;
- second/third systems checked;
- ambiguity or stale-state point;
- decision made;
- approval owner;
- action taken manually;
- verification step;
- evidence retained today;
- time elapsed and operator time;
- failure/rework if any.

## Product-fit questions
Ask in plain language:
- How often does this happen?
- Which exception costs you the most operator time?
- Which one creates the most customer trouble?
- Where do you have to compare two or more systems before deciding?
- What information do you not trust until you re-check it?
- Which action would you want prepared but not executed automatically?
- What would you need to see before approving an action?
- How would you know the tool actually fixed the case?
- Would you trial an approval-first exception cockpit on this workflow?
- If it reliably handled this bounded workflow, would you pay for it? What pricing model or budget range would be realistic?

## Prototype gate
The Ecommerce wedge can move to a read-only/approval-prototype recommendation only when at least 3 independent participants/observations show materially similar pain and:
- frequency is directly evidenced;
- manual coordination is non-trivial;
- at least two systems/sources are genuinely crossed;
- read feasibility is credible;
- approval boundary is clear;
- a measurable operator/customer outcome exists;
- repeated trial intent exists.

## Production gate
Production remains blocked until the broader Commercial Frontend production threshold is met: stronger direct sample (approximately 10 relevant cases/conversations or equivalent), repeated trial/WTP signals, exact scopes/write actions, fail-closed verification, relevant AgentOS runtime/authority/assurance proof and no critical security unknowns.

## Current disposition
`DISCOVERY READY / DIRECT DEMAND UNKNOWN / PRODUCTION HOLD`

No live connector, customer-system write, supplier contact, credential use, purchase, deployment or external outreach is authorized by this packet.
