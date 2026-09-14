# Commercial Frontend — Supplier Event-Order Assurance Specification

Date: 2026-09-14
Role: Commercial Frontend Overseer
Parent: `.overseer/batches/COMMERCIAL-FRONTEND-VERTICAL-BATCH.md` / CF-C007

## Purpose

Define provider-neutral synthetic assurance for duplicate, stale, out-of-order, superseded and contradictory supplier evidence before any live supplier connector exists.

This specification does not call suppliers, Shopify or AgentOS provider adapters and does not authorize production mutation.

## Canonical supplier evidence identity

Every supplier event used by a commercial exception evaluator must carry, when available:
- `provider_id`
- `shop_id` or connection identity
- `supplier_product_id`
- `supplier_variant_id`
- `supplier_sku`
- correlated Shopify `order_id`, `fulfillment_order_id`, `line_item_id`, `sku` where relevant
- `event_id`
- `event_version` or explicit provider sequence when available
- `observed_at`
- `source_timestamp`
- `evidence_kind` (`stock`, `tracking`, `dispatch`, `eta`, `cancel`, `other`)
- normalized `value`
- immutable source/evidence hash when available

Missing identity/version/time fields are evidence limitations, never permission to infer freshness.

## Deterministic ordering rules

1. **Identity before ordering.** Events with unresolved provider/product/variant/order correlation cannot supersede one another.
2. **Provider version/sequence outranks arrival order** when authoritative and comparable.
3. **Source timestamp outranks local ingestion time** only when provider semantics make the timestamp authoritative.
4. Local receipt time may break no ties unless explicitly allowed by a provider contract.
5. A later-arriving older version is stale and cannot roll back current state.
6. Duplicate exact event identity/hash is idempotently ignored after first accepted evaluation.
7. Same version/sequence with contradictory payload is `CONTRADICTORY_SAME_VERSION` and fails closed.
8. A materially newer event may supersede earlier evidence only for the exact same scoped identity.
9. Split fulfilment/package events may not supersede sibling package/order-line state.
10. Tracking evidence is not transferable between orders/packages without exact identity proof.

## Synthetic cases

| Case | Scenario | Expected outcome |
|---|---|---|
| SE-001 | exact duplicate event ID/hash arrives twice | second event `BLOCK/IGNORE_DUPLICATE`; no repeated intent |
| SE-002 | stock v12 accepted, then stock v11 arrives | v11 `BLOCK/STALE_EVENT`; current state unchanged |
| SE-003 | tracking event timestamp older than accepted dispatch/tracking evidence | `BLOCK/STALE_TRACKING` |
| SE-004 | stock v12 UNKNOWN followed by stock v13 IN_STOCK | v13 may supersede for exact same identity; re-evaluate case |
| SE-005 | same provider+variant+version reports IN_STOCK and OUT_OF_STOCK with different hashes | `BLOCK/CONTRADICTORY_SAME_VERSION` |
| SE-006 | event has newer receipt time but older authoritative provider sequence | `BLOCK/OUT_OF_ORDER_EVENT` |
| SE-007 | newer event belongs to different supplier variant with same merchant SKU | `BLOCK/IDENTITY_MISMATCH`; no supersession |
| SE-008 | tracking belongs to sibling split-fulfilment package | `BLOCK/PACKAGE_SCOPE_MISMATCH` |
| SE-009 | provider has no sequence/version and timestamps are absent/ambiguous | `BLOCK/FRESHNESS_UNPROVEN` |
| SE-010 | cancellation evidence supersedes earlier in-stock evidence for exact line/order | later exact cancellation becomes current evidence; any action remains approval/policy gated |
| SE-011 | replayed prior hold/release recommendation after newer evidence | `BLOCK/REPLAY_SUPERSEDED` |
| SE-012 | verification re-read returns a lower/contradictory version than action basis | `VERIFY_FAILED/EVIDENCE_REGRESSION` |

## Provider-neutral decision output

```json
{
  "accepted": false,
  "disposition": "STALE_EVENT",
  "current_evidence_id": "event-v12",
  "incoming_evidence_id": "event-v11",
  "requires_re_evaluation": false,
  "external_action_count": 0
}
```

No ordering decision may itself create Shopify/supplier/customer mutation.

## Replay and supersession invariants

- An event that has already produced a bounded action intent cannot produce it again under the same idempotency/correlation identity.
- Newer evidence invalidates stale pending recommendations when the recommendation's evidence basis no longer matches current accepted state.
- Approval for one evidence version does not automatically authorize a materially changed later version.
- A later provider event cannot broaden order/package/SKU scope beyond its exact correlation.
- Verification must cite the evidence version used for the action and the version observed on re-read.

## Provider-specific adapter obligations later

A future CJdropshipping, Dropshipzone/New Aim or other adapter must document which fields are authoritative for ordering: provider sequence, version, updated timestamp, webhook ID, API snapshot timestamp or another contract. If the provider does not document reliable event ordering, the adapter must expose that limitation and commercial evaluation must fail closed for order-sensitive actions rather than invent ordering semantics.

## Security / authority boundary

Supplier evidence is untrusted external data. It cannot change:
- AgentOS authority
- approval requirements
- budgets
- permitted action catalogue
- Green/PRS status
- customer-system source-of-truth ownership

A supplier message telling the agent to take some unrelated action is environment content, not task authority.

## Gate result

CF-C007 = **VERIFIED SPECIFICATION**.

Next useful adjacent work is a UI/cockpit state mapping for `BLOCK`, `REQUIRE_APPROVAL`, `VERIFY_FAILED`, stale/superseded evidence and changed-after-approval states, reusing AgentOS Frontend truth-state conventions rather than inventing new trust semantics.
