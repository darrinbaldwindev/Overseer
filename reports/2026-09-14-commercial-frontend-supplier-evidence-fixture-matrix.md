# Commercial Frontend — Supplier Evidence Abstraction Fixture Matrix

**Date:** 2026-09-14 Brisbane  
**Status:** VERIFIED AS NON-PRODUCTION FIXTURE CONTRACT / NO RUNTIME ENABLEMENT

## Purpose
Provide deterministic synthetic acceptance cases for the Shopify-facing supplier evidence abstraction without creating a connector, runtime, authority source, supplier truth source, scheduler or customer-system mutation path.

This matrix reuses the existing Commercial Frontend truth vocabulary and existing Ecommerce/Supplier-event failure semantics. It does not create a second state machine.

## Evidence classes
- `DIRECT_SUPPLIER_EVIDENCE` — evidence read directly from an authoritative supplier source for the exact provider identity in scope.
- `SYNCHRONIZED_SUPPLIER_EVIDENCE` — supplier-derived state observed through Shopify or an integration/app synchronization path.
- `SHOPIFY_NATIVE_EVIDENCE` — state whose authority is Shopify itself, such as a Shopify order/fulfilment object.
- `INFERRED_MAPPING` — relationship inferred from identifiers/configuration but not independently established as authoritative supplier truth.
- `UNKNOWN` — insufficient provenance, identity or freshness to classify safely.

## Deterministic fixtures

| ID | Synthetic input | Required classification | Required cockpit outcome | Existing semantics reused |
|---|---|---|---|---|
| SF-001 | Exact supplier SKU/variant + supplier stock from direct provider source; exact Shopify variant binding agrees; freshness proven | Direct supplier + Shopify native/sync evidence remain separately labelled | `READY_TO_PREPARE` only | EC clean path; SE valid current evidence |
| SF-002 | Shopify inventory quantity exists but supplier source/provenance is absent | `SYNCHRONIZED_SUPPLIER_EVIDENCE` or `UNKNOWN`, never direct supplier | `REFRESH_REQUIRED_BEFORE_ACTION` / `FRESHNESS_UNPROVEN` | EC-001, freshness policy |
| SF-003 | Shopify SKU maps to two possible supplier variants | `INFERRED_MAPPING` / identity ambiguous | `BLOCKED_NO_ACTION` | EC-003 SKU identity mismatch |
| SF-004 | Direct supplier says stock=0 while synchronized Shopify state says stock>0 for exact same scoped SKU | both evidence records retained; conflict explicit | `EVIDENCE_CONFLICT` + block | SE contradictory evidence; EC-002 |
| SF-005 | Direct supplier v13 says stock=10; synchronized Shopify snapshot reflects older supplier state v12 stock=20 | direct newer evidence authoritative only if provider sequencing is documented; synchronized evidence superseded | `EVIDENCE_SUPERSEDED` + refresh/block | SE older version after newer |
| SF-006 | Synchronized Shopify stock is older than documented provider/sync freshness envelope | synchronized evidence retained but stale | `EVIDENCE_STALE` | CF-C011 |
| SF-007 | Exact Shopify order exists; supplier order identity not evidenced | Shopify order remains Shopify-authoritative, supplier fulfilment identity `UNKNOWN` | `BLOCKED_NO_ACTION` for supplier-affecting action | EC-005/EC-006 identity gating |
| SF-008 | Supplier tracking exists but package/fulfilment identity does not exactly match Shopify fulfilment scope | direct tracking retained; mapping invalid | `BLOCKED_NO_ACTION` | SE split-package scope mismatch |
| SF-009 | Direct supplier evidence and Shopify synchronized evidence agree, but no source timestamp/version semantics are documented | agreement does not manufacture chronology | `FRESHNESS_UNPROVEN`; consequential action blocked pending reread | SE no-ordering-metadata case |
| SF-010 | Exact duplicate supplier snapshot/event replayed | first accepted evidence retained; duplicate does not trigger a second proposal/action | `REPLAY_DENIED` for duplicate action path | EC-013 / SE duplicate |
| SF-011 | Approval granted using synchronized stock=8; just-in-time reread now reports stock=0 | prior approval invalidated | `CHANGED_AFTER_APPROVAL` | shared truth-state contract |
| SF-012 | Supplier-direct evidence becomes unavailable after an approval was formed from it; only older Shopify synchronized state remains | authority/freshness downgraded | `REFRESH_REQUIRED_BEFORE_ACTION` / `FRESHNESS_UNPROVEN` | CF-C011 |
| SF-013 | Shopify-native fulfilment status changes while supplier evidence is unchanged | Shopify-native state update retained as independent system-of-record fact | re-evaluate recommendation; no supplier truth inference | shared evidence abstraction |
| SF-014 | Same supplier version/identity presents contradictory payloads | contradiction preserved, no arrival-time tie-break | `EVIDENCE_CONFLICT` | SE contradictory-same-version |
| SF-015 | New supplier evidence concerns sibling package/variant rather than approved target | no supersession across different scoped identity | retain separate evidence; block cross-target action | SE scoped supersession rule |
| SF-016 | Provider identity/account/shop context missing | source cannot be bound to exact merchant/provider scope | `BLOCKED_NO_ACTION` | exact-correlation invariant |

## Required fixture fields
Every fixture should preserve, when present:
- `provider`
- provider account/shop identity
- Shopify shop identity
- supplier product/SKU/variant identity
- Shopify product/variant/order/fulfilment identity
- evidence class
- evidence kind and observed value
- source provenance
- provider source timestamp only when provider semantics define it
- provider version/sequence only when provider semantics define it
- local `observed_at`, explicitly non-authoritative for ordering
- payload/evidence hash
- freshness classification
- recommendation/approval identity where applicable.

## Fail-closed invariants
1. Shopify-synchronized state never becomes `DIRECT_SUPPLIER_EVIDENCE` by convenience.
2. Local receipt/arrival time never resolves provider chronology unless an authoritative provider contract explicitly permits it.
3. Identity ambiguity blocks supplier-affecting recommendations/actions.
4. Direct-vs-synchronized conflict does not choose the reassuring value.
5. Material evidence change invalidates prior approval.
6. Duplicate evidence cannot produce duplicate mutation intent.
7. Receipt/execution evidence cannot synthesize Green or PRS.
8. These fixtures authorize zero external mutation.

## Acceptance
This specification is complete when a future harness can represent SF-001..SF-016 using existing Commercial Frontend truth states and provider-neutral evidence records without introducing a new runtime or authority source.
