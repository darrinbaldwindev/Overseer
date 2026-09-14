# Commercial Frontend — Shopify-facing supplier evidence abstraction

Date: 2026-09-14 Brisbane
Owner: Commercial Frontend Overseer
Status: PRODUCT CONTRACT / NO CONNECTOR ENABLEMENT

## Purpose
Define the smallest provider-neutral read contract for Ecommerce AI Operations when supplier state is synchronized into Shopify by an app/integration but a trustworthy retailer-facing supplier API is absent or unavailable.

This contract prevents synchronized Shopify state from being mislabeled as direct supplier truth.

## Architecture boundary
`Supplier/provider -> supplier app/integration -> Shopify system of record -> Commercial Frontend evidence projection -> AgentOS governance`

Shopify remains the merchant system of record for the Shopify object. It does not become authoritative evidence for facts that only the upstream supplier can establish unless the integration contract explicitly proves provenance and freshness.

## Evidence classes

### DIRECT_SUPPLIER_EVIDENCE
Observed from an authoritative supplier endpoint/event with exact supplier identity and provenance.

### SYNCHRONIZED_SUPPLIER_EVIDENCE
Observed in Shopify or an integration surface and explicitly attributed to an upstream supplier synchronization. Useful operationally, but weaker than direct supplier evidence when upstream provenance/version/freshness is unavailable.

### SHOPIFY_NATIVE_EVIDENCE
A Shopify-owned fact such as Shopify order ID, fulfillment order ID, inventory item ID/location state, hold/status, tracking stored on Shopify, or merchant-side timestamps. This establishes Shopify state, not necessarily supplier reality.

### INFERRED_MAPPING
A deterministic mapping between Shopify and supplier identities based on documented or captured binding fields. Must remain labeled inference/mapping unless direct supplier proof exists.

### UNKNOWN
Provenance, freshness, ordering, identity or upstream authority cannot be established.

## Minimum evidence envelope
Every supplier-derived snapshot projected into the cockpit should carry, when available:

- `provider_name`
- `provider_account_or_shop_id`
- `provider_product_id`
- `provider_variant_id`
- `provider_sku`
- `shopify_shop_id`
- `shopify_product_id`
- `shopify_variant_id`
- `shopify_inventory_item_id`
- `shopify_order_id`
- `shopify_fulfillment_order_id`
- `shopify_fulfillment_id`
- `shopify_line_item_id`
- `shopify_sku`
- `source_kind` (`DIRECT_SUPPLIER`, `SYNCED_TO_SHOPIFY`, `SHOPIFY_NATIVE`, `INFERRED`, `UNKNOWN`)
- `source_observed_at`
- `source_timestamp` if supplied by the authoritative source
- `provider_event_id` / `provider_version` / `provider_sequence` only when documented
- `shopify_updated_at` when relevant
- `integration_observed_at`
- `evidence_hash_or_fingerprint`
- `freshness_disposition`
- `confidence_reason`

Missing fields stay missing/UNKNOWN; they are not reconstructed from convenience assumptions.

## Truth rules
1. A Shopify inventory quantity synchronized by an app may truthfully be shown as `Shopify currently shows X`, not `Supplier has X`, unless direct supplier evidence supports the latter.
2. Shopify `updated_at` proves a Shopify object changed; it does not prove when the supplier state itself changed.
3. Local receipt/arrival time proves when AgentOS observed data, not when the supplier state became true.
4. An exact Shopify SKU is not sufficient supplier identity if multiple provider variants/accounts can map to that SKU.
5. Tracking saved in Shopify proves Shopify currently stores that tracking association; supplier/carrier provenance must be preserved separately when available.
6. Any missing/ambiguous provider-to-Shopify identity makes consequential mutation ineligible.
7. A later Shopify update cannot supersede direct supplier evidence solely because it arrived later; source authority and scope must be reconciled first.
8. Contradictory direct-supplier and Shopify-synchronized evidence maps to `EVIDENCE_CONFLICT`, never optimistic success.
9. Approval granted against evidence version/fingerprint A is invalid after a materially changed evidence version/fingerprint B.
10. A just-in-time system-of-record reread is required before a consequential Shopify/customer-promise action.

## Cockpit presentation

### Simple
- `Supplier status not confirmed` when only stale/ambiguous synchronized state exists.
- `Shopify shows ...` when presenting synchronized/native Shopify facts.
- `Needs attention` for conflict, stale identity, or missing mapping.

### Essentials
Add provider name, Shopify object identity, observed time, freshness state, and whether evidence is direct supplier vs synchronized.

### Tech Head
Expose complete identity tuple, source type, source/observed timestamps, hashes, provider version/sequence only when canonical, Shopify timestamps, supersession/conflict reason and approval evidence fingerprint.

All modes represent identical truth.

## Provider application

### CJdropshipping
Current first-party documentation provides stronger direct provider identities (product/variant/shop/warehouse/inventory). When those endpoints are available and authorized, direct CJ evidence can outrank an older synchronized Shopify snapshot within the same exact identity scope. Universal event ordering/version semantics remain UNKNOWN unless endpoint-specific documentation establishes them.

### Dropshipzone / New Aim
Current public retailer documentation establishes integration workflows and synchronized Shopify behavior, but the exact public retailer REST/API schema remains UNKNOWN. Therefore Shopify-visible stock/order/tracking state is classified as `SYNCHRONIZED_SUPPLIER_EVIDENCE` unless a later authoritative retailer integration contract exposes direct provider provenance.

## External evidence rechecked 2026-09-14
- Shopify Help Center distinguishes Shopify product vendor fields from supplier-specific information in its inventory tooling; supplier constructs can be app-specific rather than equivalent to product vendor truth: https://help.shopify.com/en/manual/sell-in-person/shopify-pos/inventory-management/stocky/vendors-and-suppliers
- Dropshipzone retailer guidance previously reviewed documents Shopify product/inventory/order/fulfilment integration but not a public retailer REST field contract.

## Non-goals
- no live connector;
- no production Shopify write;
- no retailer credentials;
- no supplier contact;
- no new canonical supplier database;
- no new authority/approval/assurance system.

## Acceptance
This abstraction is acceptable only if downstream logic can distinguish direct supplier truth, synchronized Shopify state, Shopify-native truth and UNKNOWN without collapsing them into one reassuring status.

Classification: `VERIFIED PRODUCT CONTRACT / IMPLEMENTATION DEFERRED`.