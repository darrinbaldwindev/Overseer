# Commercial Frontend Shared Cockpit Truth-State Contract

**Date:** 2026-09-14  
**Scope:** Tradie AI Operations + Ecommerce AI Operations  
**Status:** IMPLEMENTATION-READY PRODUCT CONTRACT / NO PRODUCTION RUNTIME ENABLEMENT

## Purpose

Define one reusable vertical cockpit truth model for Commercial Frontend work without creating a competing AgentOS frontend authority, scheduler, runtime, assurance system, authority layer, or source of execution truth.

This contract maps existing synthetic decision outcomes and canonical AgentOS frontend truth requirements into user-facing vertical states. It does not authorize any customer-system mutation.

## Architecture boundary

`vertical cockpit -> shared commercial layer -> AgentOS governance/execution/verification -> customer systems of record`

The vertical cockpit may summarize and request decisions. It must not invent execution state, permission state, Green state, PRS state, evidence, or completion.

## Core invariant

**Different verticals may show different business context, but the same underlying truth must produce the same trust state.**

Simple / Essentials / Tech Head may differ in depth, never in truth.

## Canonical state vocabulary

### 1. READY_TO_PREPARE

Source outcome: `ALLOW_PREPARE`.

Meaning:
- evidence is sufficient to prepare a proposed action;
- no external mutation has occurred;
- no approval is implied;
- proposal may still become invalid if evidence changes.

UI guidance:
- Simple: `Ready to prepare`
- Essentials: show evidence freshness + proposed action + no-action-yet status
- Tech Head: exact correlation IDs, evidence sources, timestamps/versions, rule/reason code

Must not say: `Ready to execute`, `Verified`, `Approved`, `Done`.

### 2. APPROVAL_REQUIRED

Source outcome: `REQUIRE_APPROVAL`.

Meaning:
- a bounded action is technically proposed;
- policy requires explicit human approval before mutation;
- approval must bind the exact action, target, evidence set, and attempt/correlation identity.

UI guidance:
- Simple: `Needs your approval`
- Essentials: what will happen, target, consequence, evidence freshness
- Tech Head: exact action payload hash/identity, resource IDs, approval scope, evidence IDs

Must not imply Jack/AgentOS has granted authority unless canonical AgentOS authority evidence exists.

### 3. BLOCKED_NO_ACTION

Source outcome: `BLOCK`.

Meaning:
- the system cannot safely prepare or execute the action from current evidence;
- zero external mutation is permitted;
- the user should see the concrete blocking reason, not a generic error where a specific reason is known.

Examples:
- ambiguous customer/order/SKU identity;
- missing recipient;
- partial/disputed/reversed payment;
- stale supplier evidence;
- cross-package tracking mismatch;
- missing exact hold identity;
- unproven supplier freshness.

UI guidance:
- Simple: `Blocked — needs attention`
- Essentials: blocking reason + smallest next evidence needed
- Tech Head: reason code + exact mismatched/missing identity fields

Must not downgrade BLOCK into a warning while keeping the action button active.

### 4. VERIFICATION_FAILED

Source outcome: `VERIFY_FAILED`.

Meaning:
- an expected verification/re-read did not confirm the intended state;
- prior execution/preparation must not be presented as successfully closed;
- recovery/reconciliation may be required;
- completion remains unproven.

UI guidance:
- Simple: `Couldn’t confirm the result`
- Essentials: what was expected vs observed, whether any action may have occurred
- Tech Head: exact pre/post evidence, receipt/attempt IDs if canonical, verification error/reason code

Must not say `Completed with warning` unless canonical state actually supports completion independent of this failed verification.

### 5. EVIDENCE_STALE

Meaning:
- relevant evidence exceeds the provider/workflow freshness contract or freshness cannot be established;
- stale evidence cannot authorize or sustain a current recommendation.

UI guidance:
- Simple: `Information is out of date`
- Essentials: source + age + refresh/re-read requirement
- Tech Head: source timestamp, provider sequence/version if available, observed arrival time separated from authoritative source time

Action rule: no state-changing execution from stale evidence.

### 6. EVIDENCE_SUPERSEDED

Meaning:
- later authoritative evidence replaces the evidence used for an earlier recommendation;
- earlier recommendation/approval must not silently survive.

UI guidance:
- Simple: `Situation changed — review again`
- Essentials: previous recommendation vs new evidence
- Tech Head: previous/current evidence IDs, versions/sequences/timestamps, invalidated approval identity

Action rule: invalidate any approval tied to the superseded evidence/action payload.

### 7. EVIDENCE_CONFLICT

Meaning:
- two sources or events cannot be deterministically reconciled;
- same-version contradictory evidence is never resolved by choosing the more reassuring state;
- arrival order alone does not establish authority.

UI guidance:
- Simple: `Conflicting information`
- Essentials: identify conflicting systems/records and required reconciliation
- Tech Head: exact source IDs, versions, timestamps, values, correlation tuple

Action rule: fail closed to no mutation.

### 8. CHANGED_AFTER_APPROVAL

Meaning:
- a human approved one exact proposal, but material evidence/action/target changed before execution;
- the prior approval is stale and cannot authorize the new state.

Examples:
- supplier stock changed after approval;
- tracking/order/package identity changed;
- Xero payment was reversed after receipt-send approval;
- customer/recipient identity changed;
- Shopify hold identity changed.

UI guidance:
- Simple: `Changed after approval — approve again`
- Essentials: what changed and why previous approval no longer applies
- Tech Head: approval ID, old/new payload/evidence hashes, exact changed fields

Action rule: require new approval or block according to policy.

### 9. REPLAY_DENIED

Meaning:
- a duplicate/replayed event, recommendation, approval, or attempt was detected;
- the same state-changing action must not be repeated merely because an input/event was delivered twice.

UI guidance:
- Simple: `Duplicate ignored`
- Essentials: show that no repeat action was taken
- Tech Head: idempotency/attempt/event identity and prior disposition

Must not present replay denial as an error requiring a user to retry the same action.

### 10. EXECUTION_PENDING_VERIFICATION

Meaning:
- canonical execution evidence says an action was attempted/performed, but required re-read/verification has not completed;
- this state can only be driven by canonical runtime evidence, never synthetic Commercial Frontend inference.

UI guidance:
- Simple: `Action sent — checking result`
- Essentials: executed action + verification pending
- Tech Head: exact execution receipt/correlation + verification status

Must not show `Complete`, Green or PRS.

### 11. EXECUTION_CONFIRMED

Meaning:
- canonical execution + required execution verification for this vertical action are complete at the applicable scope;
- this is not automatically Green, PRS, mission completion, or broader AgentOS readiness.

UI guidance:
- Simple: `Action confirmed`
- Essentials: result + evidence summary + any assurance still pending/not applicable
- Tech Head: execution/verification receipt lineage

Avoid generic `VERIFIED` because it is ambiguous with independent assurance.

### 12. ASSURANCE_UNKNOWN / ASSURANCE_PENDING / ASSURANCE_PASS / ASSURANCE_FAIL

These states belong to canonical Green/PRS evidence only when the vertical surface is entitled to expose them.

Rules:
- worker/execution success cannot synthesize Green;
- Green cannot synthesize PRS;
- absence of an assurance failure is not PASS;
- stale/mismatched scope assurance is UNKNOWN, not PASS;
- Commercial Frontend never fabricates Jack/Henry state.

## Approval-card minimum contract

Any state-changing approval card should show, when canonical fields exist:
1. exact proposed action;
2. exact business target/resource;
3. why it is needed;
4. evidence supporting it;
5. evidence freshness / conflict status;
6. meaningful consequence/risk;
7. whether customer communication, money, credentials, inventory/fulfilment promise, or irreversible effect is involved;
8. approval scope and whether a later evidence change invalidates it.

If these fields are unavailable, use a bounded generic approval state or block stronger claims rather than inventing them.

## Tradie mapping

- TR clean fully paid case -> `READY_TO_PREPARE` -> `APPROVAL_REQUIRED` before external customer communication.
- partial/reversed/disputed payment -> `BLOCKED_NO_ACTION`.
- ambiguous job/invoice/customer -> `BLOCKED_NO_ACTION`.
- sync lag/unproven final state -> `EVIDENCE_STALE` or `BLOCKED_NO_ACTION` depending evidence contract.
- prior-send replay -> `REPLAY_DENIED`.
- verification re-read failure -> `VERIFICATION_FAILED`.
- payment/customer evidence changes after approval -> `CHANGED_AFTER_APPROVAL`.

## Ecommerce mapping

- clean current supplier/order match -> `READY_TO_PREPARE`.
- customer-promise material action/Shopify hold/release/tracking mutation -> `APPROVAL_REQUIRED` by default for first MVP unless later policy explicitly authorizes a narrower class.
- stock/SKU/fulfilment identity ambiguity -> `BLOCKED_NO_ACTION`.
- stale supplier/tracking evidence -> `EVIDENCE_STALE`.
- later authoritative stock/tracking event -> `EVIDENCE_SUPERSEDED` for earlier recommendation.
- contradictory same-version supplier evidence -> `EVIDENCE_CONFLICT`.
- exact state changes after approval -> `CHANGED_AFTER_APPROVAL`.
- duplicate event/recommendation -> `REPLAY_DENIED`.
- post-action re-read mismatch -> `VERIFICATION_FAILED`.

## Deterministic truth invariants

1. `BLOCK`, `VERIFY_FAILED`, stale/conflicting evidence never expose an active state-changing execution control.
2. Same canonical input state produces same truth state across Simple/Essentials/Tech Head.
3. Mode changes presentation depth only.
4. No vertical state can create/upgrade AgentOS authority, Green, PRS, completion, or execution truth.
5. Evidence source time/version/sequence outranks local arrival time only where provider contract explicitly supports it.
6. Changed material evidence invalidates prior recommendation and approval.
7. Replay/idempotency denial is a safe terminal disposition for that duplicate attempt, not a request to retry.
8. Missing evidence is explicit; UNKNOWN does not collapse to success.
9. A receipt is not independent assurance.
10. External mutation remains impossible from synthetic fixtures/specifications in this workstream.

## Build gate

This truth-state contract is reusable product specification only. It does not satisfy direct customer validation, AgentOS Wave/Level-2 readiness, connector production authority, physical Windows acceptance, Green, PRS, or production Commercial Frontend build gates.

**Classification:** `SHARED-COCKPIT-TRUTH-CONTRACT-READY / PRODUCTION-HOLD`.
