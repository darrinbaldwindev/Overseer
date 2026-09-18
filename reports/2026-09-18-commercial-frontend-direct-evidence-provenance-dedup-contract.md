# Commercial Frontend — Direct Evidence Provenance & Deduplication Contract

Date: 2026-09-18 (Brisbane)
Status: VERIFIED AS VALIDATION-SAFETY CONTRACT / NO OUTREACH OR PRODUCTION AUTHORITY

## Purpose
Prevent duplicate participants, recycled anecdotes, copied platform examples, synthetic fixtures or repeated observations from inflating Commercial Frontend customer-validation evidence.

This contract applies to Tradie, Ecommerce and future verticals.

## Evidence classes admitted
Only these classes may contribute to direct-validation counts:
- `OBSERVED_WORKFLOW` — a real workflow directly observed by the researcher/operator;
- `PARTICIPANT_REPORTED` — a real operator/customer describes their own actual workflow;
- `PARTICIPANT_ARTIFACT` — participant-supplied evidence such as anonymised screenshots, logs, reports or workflow exports, where provenance is clear.

These do **not** count toward direct-participant thresholds:
- platform/vendor documentation;
- public forum posts where participant identity/independence cannot be established;
- synthetic fixtures;
- portfolio examples such as GlobalShopCo internal test cases;
- analyst scenarios;
- copied summaries of another interview;
- worker/agent-generated hypothetical records.

## Minimum provenance envelope
Every direct-evidence record must carry:
- `evidence_record_id` — unique local record ID;
- `participant_key` — privacy-preserving stable pseudonymous key;
- `business_key` — privacy-preserving stable business key where known;
- `evidence_class`;
- `captured_at`;
- `captured_by`;
- `source_surface` — interview, observation, artifact, other;
- `workflow_family` — exact candidate wedge/family;
- `source_reference` — durable notes/artifact reference;
- `independence_status` — independent / same participant / same business / unknown;
- `raw_claim_hash` or equivalent fingerprint of the captured claim set;
- explicit UNKNOWNs for missing material fields.

Do not place personal secrets, credentials or unnecessary identifying data in the evidence record.

## Deduplication rules
1. Multiple statements from the same participant in one session count as one participant.
2. Follow-up sessions with the same participant do not increase independent participant count; they may strengthen/modify that participant's evidence.
3. Multiple employees from the same business are not automatically independent businesses. Record both participant and business keys.
4. The same incident described by multiple people counts as one incident but may provide multiple role perspectives.
5. A participant describing several distinct exception classes may contribute evidence to multiple workflow families, but only one participant count per family.
6. Repeated artifacts/screenshots from the same underlying case must not create new cases.
7. Public/vendor documentation can corroborate mechanics but never increases participant count.
8. Synthetic fixtures and portfolio test data always remain `PORTFOLIO_EVIDENCE` and contribute zero direct participants.
9. If independence cannot be established, classify `INDEPENDENCE_UNKNOWN` and exclude from threshold counts until resolved.
10. Conflicting follow-up evidence must preserve both versions and mark the affected field `CONFLICT` until reconciled; do not silently overwrite history.

## Material-similarity rule
Records may be grouped as materially similar only when they share the same core manual problem and resolution boundary. Similarity requires at least:
- same primary systems/handoff class;
- same operational trigger/exception family;
- substantially similar manual coordination burden;
- comparable approval boundary;
- comparable measurable resolution outcome.

Do not group merely because both cases are 'admin', 'reconciliation', 'fulfilment' or 'exceptions'.

## Threshold accounting
Prototype threshold remains at least 3 **independent, materially similar** direct participants/observations. A threshold summary must state:
- independent participant count;
- independent business count where known;
- observed-workflow count;
- participant-reported count;
- excluded duplicate/unknown-independence count;
- material-similarity rationale;
- controlling UNKNOWNs.

Production consideration still requires stronger direct evidence (approximately 10 relevant conversations/observations or equivalent), repeated trial intent, credible WTP, exact scopes and applicable AgentOS proof. Raw counts alone never satisfy the gate.

## WTP and trial-intent integrity
- preserve exact participant wording where practical;
- 'sounds useful' is not trial intent;
- trial intent is not WTP;
- budget speculation by the researcher is not WTP;
- inferred company affordability is not WTP;
- missing amount/terms remain UNKNOWN.

## Fail-closed examples
- 3 interviews from the same owner across three days => independent participant count = 1.
- 4 staff from one company reporting one shared incident => 4 role perspectives, 1 business incident; do not present as four independent businesses.
- one Reddit thread with 20 comments => public signal, not 20 validated participants.
- one GlobalShopCo synthetic exception reproduced 10 times => zero direct participants.

## Authority boundary
This document only governs evidence interpretation. It creates no CRM, customer registry, identity authority, outreach permission, production write path, publication right or AgentOS authority.