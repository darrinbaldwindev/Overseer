# Commercial Frontend — Ecommerce Synthetic Exception Cockpit Specification

Date: 2026-09-14  
Role: Commercial Frontend Overseer  
Parent gate: Overseer Issue #21 / C-006  
Classification: NON-PRODUCTION SYNTHETIC SPECIFICATION

## Purpose

Define a deterministic, mutation-free acceptance surface for the current Ecommerce AI Operations hypothesis: governed supplier/fulfilment exception resolution across supplier evidence and Shopify state.

This specification does not create a connector, scheduler, queue, authority layer, customer-system write path, or production frontend. It is a fixture contract for later reuse by the canonical AgentOS execution/governance path.

## Architecture lock

`Ecommerce cockpit -> shared commercial layer -> AgentOS governance/execution/verification -> Shopify + supplier systems of record`

The cockpit may display context, evidence, recommended action, approval state and verification state. It must not become an independent execution authority or source of truth.

## Deterministic outcomes

Every fixture must resolve to exactly one primary decision:

- `ALLOW_PREPARE` — evidence is sufficiently correlated to prepare a non-mutating action proposal; no external action is authorised.
- `REQUIRE_APPROVAL` — a bounded external action may be technically feasible but must stop at an explicit approval boundary.
- `BLOCK` — identity/evidence/authority is insufficient or contradictory; zero external mutation.
- `VERIFY_FAILED` — a previously prepared/simulated action cannot be verified by required re-read; never represent success.

## Fixture schema

Each case should contain at minimum:

```yaml
case_id: string
scenario: string
shopify:
  shop_id: string
  order_id: string
  order_name: string
  fulfillment_order_ids: [string]
  line_items:
    - shopify_variant_id: string
      sku: string
      quantity: integer
  current_fulfillment_state: string
  current_hold_ids: [string]
supplier:
  provider: string
  supplier_order_id: string|null
  supplier_product_id: string|null
  supplier_variant_id: string|null
  sku: string|null
  stock_status: string|null
  stock_quantity: integer|null
  dispatch_status: string|null
  tracking_number: string|null
  tracking_url: string|null
  evidence_source: string
  evidence_observed_at: RFC3339 timestamp
  evidence_version: string|null
customer_promise:
  promised_dispatch_at: RFC3339 timestamp|null
  promised_delivery_at: RFC3339 timestamp|null
authority:
  requested_action: string
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
  proposed_action: string|null
```

## Required reason codes

Initial fixed reason vocabulary:

- `SUPPLIER_STOCK_UNKNOWN`
- `SUPPLIER_STOCK_MISMATCH`
- `SKU_IDENTITY_MISMATCH`
- `FULFILMENT_IDENTITY_AMBIGUOUS`
- `SUPPLIER_EVIDENCE_STALE`
- `SUPPLIER_EVIDENCE_CONTRADICTORY`
- `TRACKING_MISSING`
- `TRACKING_CONFLICTING`
- `TRACKING_ORDER_MISMATCH`
- `LATE_DISPATCH_RISK`
- `CUSTOMER_PROMISE_AT_RISK`
- `SPLIT_FULFILMENT_REQUIRES_DECISION`
- `HOLD_REQUIRED`
- `HOLD_IDENTITY_MISMATCH`
- `APPROVAL_REQUIRED`
- `APPROVAL_MISSING`
- `REPLAY_DETECTED`
- `VERIFICATION_REREAD_FAILED`

Unknown reason values fail closed rather than being silently accepted.

## Minimum synthetic cases

### EC-001 — Supplier stock unknown
Supplier product/variant correlation is present but no trustworthy current stock evidence exists.

Expected: `BLOCK`  
Reasons: `SUPPLIER_STOCK_UNKNOWN`  
External mutation: zero.

### EC-002 — Stock mismatch
Shopify indicates sellable quantity while supplier evidence says unavailable/zero.

Expected: `REQUIRE_APPROVAL` if exact order/fulfilment/SKU identity is proven and the recommendation is to hold; otherwise `BLOCK`.  
Reasons: `SUPPLIER_STOCK_MISMATCH`, optionally `HOLD_REQUIRED`.

### EC-003 — SKU identity mismatch
Shopify SKU/variant does not map uniquely to supplier variant.

Expected: `BLOCK`  
Reason: `SKU_IDENTITY_MISMATCH`.

### EC-004 — Tracking missing after dispatch
Supplier dispatch is evidenced but no tracking number is available after a configured synthetic threshold.

Expected: `ALLOW_PREPARE` for an exception case only; any customer message or Shopify write remains separately governed.  
Reason: `TRACKING_MISSING`.

### EC-005 — Tracking conflict
Two sources return different tracking numbers for the same supplier order/package without a trustworthy supersession chain.

Expected: `BLOCK`  
Reason: `TRACKING_CONFLICTING`.

### EC-006 — Tracking belongs to wrong order/package
Tracking evidence resolves to another supplier order or Shopify fulfilment.

Expected: `BLOCK`  
Reason: `TRACKING_ORDER_MISMATCH`.

### EC-007 — Late dispatch / ETA risk
Supplier has not dispatched by the synthetic promise threshold and exact order/SKU identity is valid.

Expected: `ALLOW_PREPARE` for an exception recommendation; material customer promise change requires `REQUIRE_APPROVAL`.  
Reasons: `LATE_DISPATCH_RISK`, optionally `CUSTOMER_PROMISE_AT_RISK`.

### EC-008 — Split fulfilment
One Shopify order contains multiple fulfilment orders and supplier evidence only resolves a subset.

Expected: `REQUIRE_APPROVAL` when a bounded action affects only the proven subset; `BLOCK` if proposed action would affect unresolved fulfilments.  
Reason: `SPLIT_FULFILMENT_REQUIRES_DECISION`.

### EC-009 — Hold required
Exact order/fulfilment/SKU identity is proven and supplier evidence indicates stock/dispatch exception.

Expected: `REQUIRE_APPROVAL` for a proposed Shopify fulfilment hold.  
Reasons: `HOLD_REQUIRED`, `APPROVAL_REQUIRED`.

No live call is permitted by this spec.

### EC-010 — Release with wrong hold identity
Fixture requests release of a hold ID that is absent from the exact fulfilment order.

Expected: `BLOCK`  
Reason: `HOLD_IDENTITY_MISMATCH`.

### EC-011 — Supplier evidence stale
Supplier stock/dispatch evidence predates the configured fixture freshness boundary.

Expected: `BLOCK`  
Reason: `SUPPLIER_EVIDENCE_STALE`.

Freshness is policy input; the fixture must not invent a universal real-world TTL.

### EC-012 — Verification re-read failure
A simulated approved action has an expected post-state, but required Shopify/supplier re-read is missing or disagrees.

Expected: `VERIFY_FAILED`  
Reason: `VERIFICATION_REREAD_FAILED`.

### EC-013 — Duplicate event / replay
Same idempotency key and correlated event is presented after a prior prepared/simulated action.

Expected: `BLOCK`  
Reason: `REPLAY_DETECTED`.

No second action proposal may be emitted as a new execution intent.

### EC-014 — Contradictory supplier evidence
Two nominally authoritative supplier observations for the same version/time window materially disagree and no precedence rule is evidenced.

Expected: `BLOCK`  
Reason: `SUPPLIER_EVIDENCE_CONTRADICTORY`.

## Cockpit rendering contract

For every synthetic exception, the frontend surface should be able to render:

1. exact Shopify order/fulfilment identity;
2. exact supplier/provider/order/SKU identity where known;
3. evidence source and observation time;
4. contradiction/staleness status;
5. customer-impact summary;
6. recommended action;
7. authority state (`NO_ACTION`, `APPROVAL_REQUIRED`, `APPROVED_FOR_SIMULATION`, `BLOCKED`);
8. deterministic reason codes;
9. verification requirement and result;
10. audit correlation (`case_id`, `event_id`, `attempt_id`, `idempotency_key`).

The UI must not collapse `BLOCK`, `VERIFY_FAILED`, `UNKNOWN`, and successful preparation into one generic “done” state.

## Supplier connector boundary

Supplier-side evidence must preserve provider-native identity and timestamps. Email parsing, app sync, API data, CSV/file evidence and human-entered evidence are different evidence classes and must not be silently promoted to equivalent authority.

A provider connector may later normalize facts into the fixture shape, but provider-specific objects must not become canonical AgentOS mission/authority state.

## Shopify boundary

Current platform research supports bounded fulfillment-order reads and action primitives including hold/release/tracking updates. This specification intentionally models those as proposed actions only. Technical feasibility is not commercial authority.

## Acceptance criteria

This specification is satisfied when a later fixture harness can prove:

- all required cases produce deterministic primary decisions and reason codes;
- replay does not create a second state-changing intent;
- stale/ambiguous supplier evidence fails closed;
- split fulfilment never broadens action beyond exact correlated scope;
- approval-required cases do not mutate without approval evidence;
- verification failure never emits success;
- no fixture invokes Shopify, supplier, customer messaging, payment, or production network mutation.

## Commercial evidence boundary

Passing these synthetic cases would prove only that the exception semantics are coherent enough for a bounded prototype. It would not prove workflow frequency, willingness to pay, acquisition economics, production reliability, supplier terms, or AgentOS production readiness.
