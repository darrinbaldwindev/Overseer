# Commercial Frontend — Tradie Shared Direct-Evidence Form

Date: 2026-09-16 (Brisbane)
Status: VERIFIED AS CAPTURE CONTRACT / NO OUTREACH EXECUTED

## Purpose
Use one real participant/observed-workflow record to compare the two bounded Tradie hypotheses without duplicate interviews and without converting platform documentation, synthetic fixtures or assumptions into demand evidence.

T1 — post-payment administrative closure:
`Xero payment -> ServiceM8 paid state -> missing customer closure/receipt action -> approval -> bounded communication intent -> verification`

T2 — residual ServiceM8↔Xero exception handling:
`invoice/accounting-sync exception -> exact context assembly -> human decision -> bounded corrective intent -> reread/verification`

Current portfolio evidence has narrowed T2 to real residual exception classes such as zero-value invoice export failure, wrong-Xero-organisation export, invoice-number uniqueness conflict, and ServiceM8 Pay clearing-account/grouped-payout exceptions. Their commercial frequency, effort, consequence and WTP remain UNKNOWN.

## Evidence header
- participant/observation ID:
- date:
- evidence mode: `OBSERVED | PARTICIPANT_REPORTED`
- business type/trade:
- respondent role:
- buyer role if different:
- systems actually used: ServiceM8 / Xero / other
- approximate business/job/invoice volume only if participant supplies it:
- source notes/evidence reference:

Never record synthetic scenario values as participant evidence.

## Shared workflow questions
1. Which ServiceM8↔Xero handoffs do you personally check or fix in a normal week/month?
2. Show or describe the last real example you handled. What triggered your attention?
3. Which systems/screens did you open, and in what order?
4. Who was responsible for deciding what to do?
5. What could go wrong if nobody handled it?
6. Which step, if any, would you allow software to prepare automatically?
7. Which step must require human approval?
8. What outcome would prove the case was actually resolved?

## T1 — post-payment closure fields
Record independently; if not observed/supplied, write `UNKNOWN`.
- Xero-originated payments per week/month:
- proportion/count requiring manual post-payment closure:
- minutes per manual case:
- operator role performing closure:
- exact manual steps:
- customer communication/document normally sent:
- duplicate/missed-send consequence:
- complaints/rework attributable to missed closure, if participant supplies evidence:
- current measurable resolution outcome:
- acceptable automation boundary:
- approval owner/preference:
- would trial an approval-first assistant for this exact workflow? exact response:
- stated WTP for this exact workflow/product, exact amount/wording or `UNKNOWN`:

## T2 — residual sync/accounting exception fields
For each real exception type separately:
- exception class/name in participant's words:
- observed trigger/signal:
- cases per week/month:
- transient vs actionable-aged distinction:
- minutes per actionable case:
- systems/screens crossed:
- manual investigation/correction steps:
- financial/customer/operational consequence:
- operator/approval owner:
- measurable resolution outcome:
- acceptable preparation/automation boundary:
- would trial an approval-first exception assistant? exact response:
- stated WTP, exact amount/wording or `UNKNOWN`:

## Comparable derived fields
Only derive when the underlying participant inputs are complete and labelled.
- cases/week;
- minutes/case;
- admin hours/week;
- loaded admin cost/week only when participant supplies a defensible loaded hourly cost;
- consequence counts/costs only when directly supplied/observed.

Do not invent annualisation, loaded cost, complaint rates, error rates, churn, LTV or WTP.

## T1/T2 comparison disposition
For each participant:
- T1 evidence completeness: COMPLETE / PARTIAL / UNKNOWN
- T2 evidence completeness: COMPLETE / PARTIAL / UNKNOWN
- repeated pain described: exact evidence only
- trial intent: exact response only
- WTP: exact response only
- participant-level preference between T1/T2, only if explicitly stated

Across participants, no winner is selected until materially similar direct evidence repeats. Platform documentation establishes feasibility/incumbent boundaries only.

## Gate rules
- Prototype consideration requires at least 3 independent materially similar direct participants/observations plus feasible reads, approval boundary and measurable outcome.
- Production consideration remains stronger: approximately 10 relevant direct cases/conversations or equivalent, repeated trial intent, credible WTP, exact scopes/write actions, fail-closed verification and relevant AgentOS proof.
- Current C-CF-01 portfolio state is `BLOCKED_STABLE / CUSTOMER_VALIDATION_REQUIRED`; this form is the reopen path, not evidence by itself.

No outreach, customer contact, production mutation or commercial claim is authorized by this document.