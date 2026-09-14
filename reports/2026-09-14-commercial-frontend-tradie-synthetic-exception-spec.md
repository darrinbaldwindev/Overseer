# Commercial Frontend — Tradie Synthetic Exception Fixture Specification

Date: 2026-09-14  
Role: Commercial Frontend Overseer  
Parent gate: Overseer Issue #21 / C-006  
Classification: NON-PRODUCTION SYNTHETIC SPECIFICATION

## Purpose

Define deterministic, mutation-free fixtures for the current Tradie AI Operations hypothesis: Xero-paid invoice administrative closure coordinated across Xero and ServiceM8 with explicit approval and verification.

This is not a production integration and does not authorise customer communication or system mutation.

## Candidate workflow

`Xero payment state -> ServiceM8 invoice/job/payment correlation -> assemble customer context -> determine closure action -> approval boundary -> simulated communication intent -> verification receipt`

## Deterministic outcomes

- `ALLOW_PREPARE` — prepare a non-mutating closure recommendation/draft only.
- `REQUIRE_APPROVAL` — a customer-facing or state-changing action is technically plausible but must stop for explicit approval.
- `BLOCK` — correlation/evidence/authority is insufficient or contradictory.
- `VERIFY_FAILED` — a prepared/simulated action cannot be verified by mandatory re-read.

## Fixture schema

```yaml
case_id: string
xero:
  tenant_id: string
  invoice_id: string
  invoice_number: string
  invoice_total: number
  amount_paid: number
  amount_due: number
  payment_ids: [string]
  payment_status: string
  payment_observed_at: RFC3339 timestamp
servicem8:
  job_uuid: string|null
  invoice_uuid: string|null
  customer_uuid: string|null
  customer_email: string|null
  job_payment_ids: [string]
  invoice_status: string|null
  paid_state_observed_at: RFC3339 timestamp|null
closure:
  prior_closure_intent_id: string|null
  prior_send_evidence_id: string|null
  requested_channel: email|null
authority:
  approval_required: boolean
  approval_present: boolean
correlation:
  event_id: string
  attempt_id: string
  idempotency_key: string
verification:
  reread_required: boolean
  reread_matches: boolean|null
expected:
  decision: ALLOW_PREPARE|REQUIRE_APPROVAL|BLOCK|VERIFY_FAILED
  reason_codes: [string]
```

## Fixed reason vocabulary

- `PAYMENT_FULLY_PAID`
- `PAYMENT_PARTIAL`
- `PAYMENT_REVERSED`
- `PAYMENT_DISPUTED`
- `SYNC_LAG_POSSIBLE`
- `INVOICE_IDENTITY_AMBIGUOUS`
- `JOB_IDENTITY_AMBIGUOUS`
- `CUSTOMER_IDENTITY_AMBIGUOUS`
- `RECIPIENT_MISSING`
- `SYSTEM_STATE_CONFLICT`
- `PRIOR_SEND_PRESENT`
- `REPLAY_DETECTED`
- `APPROVAL_REQUIRED`
- `APPROVAL_MISSING`
- `VERIFICATION_REREAD_FAILED`

Unknown reason values fail closed.

## Required cases

### TR-001 — Fully paid, clean match
Xero shows full payment; exact ServiceM8 job/invoice/customer match exists; ServiceM8 paid state is consistent; valid recipient exists; no prior closure intent/send exists.

Expected: `ALLOW_PREPARE` for a closure draft/recommendation only.  
Reason: `PAYMENT_FULLY_PAID`.

Any actual send would separately become `REQUIRE_APPROVAL` under the initial policy.

### TR-002 — Partial payment
Xero amount due remains greater than zero.

Expected: `BLOCK` for paid-invoice closure.  
Reason: `PAYMENT_PARTIAL`.

The system may surface an exception, but must not represent the invoice as fully paid.

### TR-003 — Reversed payment
A previously observed payment is reversed/voided or no longer supports a fully paid state.

Expected: `BLOCK`.  
Reason: `PAYMENT_REVERSED`.

Any earlier prepared closure intent becomes stale and must not be sent automatically.

### TR-004 — Disputed payment
Fixture marks the payment as disputed or otherwise not safely final.

Expected: `BLOCK`.  
Reason: `PAYMENT_DISPUTED`.

### TR-005 — Duplicate invoice/customer identity
More than one ServiceM8 invoice/job/customer candidate satisfies the available identifiers.

Expected: `BLOCK`.  
Reasons: one or more of `INVOICE_IDENTITY_AMBIGUOUS`, `JOB_IDENTITY_AMBIGUOUS`, `CUSTOMER_IDENTITY_AMBIGUOUS`.

No “best guess” matching is permitted.

### TR-006 — Sync lag
Xero has a recent full payment but ServiceM8 has not yet reflected paid state within the fixture's configured observation window.

Expected: `BLOCK` pending later re-read.  
Reasons: `SYNC_LAG_POSSIBLE`, optionally `SYSTEM_STATE_CONFLICT`.

The fixture must not invent a universal real-world timeout; freshness/lag thresholds are policy/config input.

### TR-007 — Missing recipient
Exact invoice/job/customer is known, but no approved/valid customer email address is available.

Expected: `BLOCK`.  
Reason: `RECIPIENT_MISSING`.

### TR-008 — Prior send/replay
Exact payment event/idempotency key was already converted into a closure intent or verified send evidence.

Expected: `BLOCK`.  
Reasons: `PRIOR_SEND_PRESENT` and/or `REPLAY_DETECTED`.

No duplicate communication intent may be produced.

### TR-009 — Approval missing
The fixture proposes a simulated customer send but approval is required and absent.

Expected: `BLOCK`.  
Reasons: `APPROVAL_REQUIRED`, `APPROVAL_MISSING`.

### TR-010 — Simulated send approved
Exact identities/evidence are coherent and approval is present for a dry-run send simulation.

Expected: `REQUIRE_APPROVAL` until approval is consumed; after simulated consumption the harness may produce an immutable communication intent/receipt but must perform zero external send.

### TR-011 — Xero/ServiceM8 state conflict
Xero indicates full payment while ServiceM8 evidence materially contradicts the expected invoice/job/payment relationship and no evidenced precedence rule resolves it.

Expected: `BLOCK`.  
Reason: `SYSTEM_STATE_CONFLICT`.

### TR-012 — Verification re-read failure
After a simulated approved action, required evidence re-read is missing or does not match the expected state.

Expected: `VERIFY_FAILED`.  
Reason: `VERIFICATION_REREAD_FAILED`.

## Idempotency contract

The later harness must bind idempotency to the exact cross-system event and intended closure action. At minimum it should include the stable Xero payment/invoice identity, ServiceM8 job/invoice identity, closure action type and policy version.

The same correlated event must not produce more than one executable communication intent. Changed business state must create a new governed decision, not mutate historical evidence silently.

## Verification contract

A successful simulated closure path requires evidence that:

1. exact Xero invoice/payment still supports the decision;
2. exact ServiceM8 job/invoice/customer correlation still holds;
3. approval evidence matches the exact action/attempt;
4. no prior-send/replay evidence appeared between preparation and simulated execution;
5. simulated receipt persistence succeeded.

If required evidence cannot be re-read or differs materially, return `VERIFY_FAILED` or `BLOCK`, never success.

## Cockpit rendering contract

The frontend should be able to show:

- Xero payment/invoice identity and current paid/amount-due state;
- ServiceM8 job/invoice/customer match confidence as deterministic evidence, not a hidden score;
- missing/contradictory evidence;
- proposed closure action;
- recipient identity where permitted;
- approval state;
- replay/idempotency state;
- verification state;
- immutable reason codes and correlation IDs.

## Acceptance criteria

A later synthetic harness must prove:

- clean fully paid case produces one non-mutating closure proposal;
- partial/reversed/disputed cases cannot produce paid-invoice closure;
- ambiguous identity produces zero action;
- sync lag produces wait/re-read behavior rather than guessed success;
- missing recipient produces zero send intent;
- replay/prior-send cases cannot duplicate intent;
- approval evidence is exact-action/attempt bound;
- verification failure cannot be represented as success;
- zero Xero, ServiceM8, email/SMS, payment, or production network mutation occurs.

## Commercial evidence boundary

Passing synthetic fixtures would validate workflow semantics only. Frequency, minutes saved, complaint reduction, willingness to pay, OAuth/write-scope acceptance, customer trust, acquisition economics and production readiness remain UNKNOWN until directly evidenced.
