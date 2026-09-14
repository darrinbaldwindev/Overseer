# Commercial Frontend — Tradie Synthetic Harness Mapping

Date: 2026-09-14
Role: Commercial Frontend Overseer
Parent: `.overseer/batches/COMMERCIAL-FRONTEND-VERTICAL-BATCH.md` / CF-B005

## Decision

**IMPLEMENTATION-READY MAPPING ONLY / NO NEW RUNTIME CREATED**

A fresh scan found no existing Commercial Frontend runtime that should become a new system of record for Xero/ServiceM8 closure decisions. The existing AgentOS deterministic test contract provides the right test style: local-only, provider-free, idempotent, fail-closed, and separate from live provider adapters. This report maps TR-001..TR-012 into that style without wiring ServiceM8, Xero or customer communication.

## Proposed fixture envelope

```json
{
  "case_id": "TR-001",
  "xero": {
    "invoice_id": "xinv-001",
    "payment_id": "xpay-001",
    "amount_paid": 100.0,
    "amount_due": 100.0,
    "payment_status": "SETTLED",
    "observed_at": "2026-09-14T00:00:00Z"
  },
  "servicem8": {
    "job_id": "job-001",
    "invoice_id": "s8inv-001",
    "job_payment_id": "s8pay-001",
    "customer_id": "cust-001",
    "recipient": "customer@example.invalid",
    "paid_state": true
  },
  "prior_closure": null,
  "approval": "NOT_REQUESTED",
  "verification": "NOT_RUN",
  "expected": {
    "decision": "ALLOW_PREPARE",
    "reason_code": "FULL_PAYMENT_EXACT_MATCH",
    "external_action_count": 0
  }
}
```

## Future pure evaluator contract

Only when a canonical reusable seam exists:

`evaluateTradieClosure(fixture) -> { decision, reason_code, closure_intent, approval_required, verification_required, evidence_identity }`

Allowed decisions:
- `ALLOW_PREPARE`
- `REQUIRE_APPROVAL`
- `BLOCK`
- `VERIFY_FAILED`

The evaluator must not send email/SMS, post diary entries, mutate Xero/ServiceM8, create payment records, change invoice state, or infer approval.

## Case mapping

| Case | Condition | Expected decision | Required assertion |
|---|---|---|---|
| TR-001 | fully paid, exact invoice/job/customer match | ALLOW_PREPARE | communication intent only; no send |
| TR-002 | partial payment | BLOCK | no paid-in-full closure |
| TR-003 | reversed/voided payment | BLOCK | reversal supersedes prior payment evidence |
| TR-004 | disputed payment | BLOCK | dispute cannot be treated as settled |
| TR-005 | duplicate/ambiguous invoice or customer identity | BLOCK | exact correlation required |
| TR-006 | Xero↔ServiceM8 sync lag | BLOCK | stale/missing counterpart state remains UNKNOWN |
| TR-007 | missing recipient | BLOCK | no guessed address/contact |
| TR-008 | prior send/closure already evidenced | BLOCK | idempotency prevents duplicate intent |
| TR-009 | approval required but absent | REQUIRE_APPROVAL | no external action |
| TR-010 | Xero and ServiceM8 materially conflict | BLOCK | contradiction retained |
| TR-011 | exact prepared action approved in fixture | REQUIRE_APPROVAL until canonical approval token is bound | fixture cannot self-authorize |
| TR-012 | verification re-read fails | VERIFY_FAILED | never emit completed/success |

## Required assertions

1. Exact invoice/payment/job/customer identity must be preserved in every decision.
2. Partial, reversed, disputed, ambiguous, stale or conflicting states cannot be coerced into a clean closure.
3. A prepared communication is not a sent communication.
4. Approval state must come from canonical authority/approval evidence; a fixture field cannot create authority by itself.
5. Replayed payment/closure identity cannot generate a second communication intent.
6. Verification failure cannot be rewritten as success.
7. Missing recipient or attachment/document evidence fails closed.
8. No live provider invocation, credentials, URLs, environment secrets or child process access in deterministic evaluation.
9. `BLOCK` and `VERIFY_FAILED` imply zero external action count.
10. Evaluator output cannot set Green, PRS or mission completion.

## Placement recommendation

Do not create a Tradie runtime in Overseer.

When a reusable vertical decision seam is approved, map fixtures into the existing product/test structure, preserving the canonical AgentOS authority/approval/evidence model. Until then this document plus the TR fixture specification is the implementation-ready contract.

## Gate result

CF-B005 = **VERIFIED AS MAPPING / IMPLEMENTATION DEFERRED**.

Direct pain, frequency, time saved and willingness-to-pay remain UNKNOWN. No production integration or customer communication is authorized.
