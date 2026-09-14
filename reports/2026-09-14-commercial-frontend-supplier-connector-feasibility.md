# Commercial Frontend — Supplier-Side Connector Feasibility Pass

Date: 2026-09-14  
Role: Commercial Frontend Overseer  
Scope: Ecommerce AI Operations discovery only  
Classification: CURRENT PUBLIC-DOC FEASIBILITY / NO LIVE CONNECTION

## Objective

Reduce the supplier-side UNKNOWN in the Ecommerce exception wedge without credentials, live accounts, customer mutation or production integration.

The question is not whether a supplier platform can be connected in general. The useful question is whether supplier evidence can support a governed exception loop with exact identity, freshness, correlation, bounded action recommendation and verification.

## Evidence classes

- VERIFIED PLATFORM EVIDENCE — first-party/current public provider docs.
- PORTFOLIO EVIDENCE — current GlobalShopCo supplier/product work; useful for fixture design, not market demand.
- UNKNOWN — anything requiring credentials, account configuration, commercial terms, provider-specific enablement, or live behavior.

## Provider class 1 — Dropshipzone / New Aim ecosystem

### Verified public surface

Current Dropshipzone retailer documentation exposes operational guides covering:
- Shopify setup;
- automatic price synchronisation;
- automatic order synchronisation;
- order status/history;
- automatic fulfilment;
- automatic inventory updates;
- tracking-information workflows;
- shipping calculator / postcode mapping;
- API integration guidance.

This is sufficient to classify Dropshipzone as a plausible first-wave AU supplier connector target because the operational objects needed by the exception wedge — products, inventory, orders, fulfilment/tracking and shipping — are part of the documented retailer integration surface.

### What remains UNKNOWN

- exact public API resource schemas and authentication contract available to this account tier;
- event/webhook coverage versus polling;
- exact timestamp/version semantics for stock/order/tracking observations;
- whether all required APIs are enabled for GlobalShopCo's eventual commercial relationship;
- rate limits and retry/idempotency behavior;
- production blind-shipping/dropship permissions per SKU/supplier;
- whether supplier-side cancellation/hold semantics exist and are appropriate for AgentOS action.

### Commercial Frontend implication

For a first MVP, treat Dropshipzone primarily as a **supplier evidence source**, not an execution authority. Read inventory/order/tracking evidence first; leave supplier-side mutations BLOCKED until exact APIs, account permissions and terms are evidenced.

## Provider class 2 — CJdropshipping

### Verified platform evidence

CJ's current developer documentation exposes a substantially richer API surface:

- product catalogue and product-detail retrieval;
- product/variant identity;
- real-time inventory queries;
- warehouse information;
- store/shop binding and Shopify shop metadata;
- product-connection records mapping CJ products/variants to platform products/variants;
- order creation and order synchronization flows;
- shipping/waybill information;
- sandbox support;
- inventory synchronization settings and tracking-related shop configuration.

CJ's documented product synchronization flow explicitly ends in real-time inventory query. Its order synchronization documentation also requires inventory checks and exact product/store connection before fulfilment. The shop API exposes product-connection records and shop state including inventory-sync metadata.

### Strong fit for synthetic/adapter validation

CJ is the clearest current public example for proving the normalized supplier-evidence contract because it exposes:
- stable supplier product/variant IDs;
- platform product/variant connection records;
- stock queries;
- supplier order identity;
- store identity;
- tracking/order flows;
- sandbox-oriented operations.

This makes it suitable for later **mock/sandbox adapter tests**, subject to explicit authorization and separate implementation review.

### Important fail-closed cases implied by current docs

- platform product not connected to a CJ product;
- variant identity mismatch;
- shop authorization expired/deactivated;
- inventory sync disabled or not authoritative for the current shop configuration;
- warehouse/source identity mismatch;
- order exists but product connection is invalid/unresolved;
- tracking state cannot be correlated to exact supplier order/platform fulfilment;
- configuration changes mean evidence source behavior differs from prior assumptions.

### What remains UNKNOWN

- exact commercial suitability for an Australian first-wave catalogue;
- provider terms and operational reliability for the user's target categories;
- whether API/sandbox access is available without commercial/account prerequisites;
- exact webhook delivery/replay guarantees for all needed events;
- whether supplier-side writes should ever be in the first commercial wedge.

## Provider class 3 — DSers / AliExpress-style orchestration

A live first-party documentation pass did not yield enough authoritative API-level evidence in this cycle to define a safe exact supplier evidence contract comparable to CJ. Do not infer public API/write capability from product marketing or app-level Shopify integration.

Status: `INSUFFICIENT CURRENT AUTHORITATIVE API EVIDENCE` for this build gate.

This provider class can remain a later discovery target, but it should not block the synthetic cockpit specification.

## Normalized supplier evidence contract

A future provider adapter should emit facts into a provider-neutral envelope without promoting provider-native objects into canonical AgentOS state:

```yaml
provider: string
shop_or_account_id: string|null
supplier_order_id: string|null
supplier_product_id: string|null
supplier_variant_id: string|null
platform_product_id: string|null
platform_variant_id: string|null
sku: string|null
stock_status: string|null
stock_quantity: integer|null
dispatch_status: string|null
tracking_number: string|null
tracking_url: string|null
warehouse_or_source_id: string|null
observed_at: RFC3339 timestamp
evidence_version: string|null
source_method: api|webhook|app_sync|email|csv|manual
source_reference: string
```

Required invariants:
- provider-native IDs are preserved;
- source method is explicit;
- observation time is mandatory for CURRENT claims;
- no inferred SKU mapping without exact mapping evidence;
- conflicting provider observations remain conflict evidence rather than being silently overwritten;
- stale evidence cannot authorize a state-changing action;
- adapter output cannot set approval, Green, PRS or mission-completion state.

## First supplier-connector sequence

Recommended order if/when implementation becomes authorised:

1. synthetic normalized supplier evidence fixture;
2. mock provider adapter;
3. CJ sandbox/read-only adapter because public API identity/stock/order surfaces are well documented;
4. Dropshipzone read-only adapter once exact account/API contract is evidenced;
5. exact Shopify + supplier cross-correlation tests;
6. stale/duplicate/out-of-order supplier event tests;
7. independent AgentOS governance/verification review before any write path;
8. supplier-side mutation remains excluded unless a specific business case and exact authority contract justify it.

## Current conclusion

Supplier-side feasibility is no longer a single undifferentiated UNKNOWN:

- **CJdropshipping:** PARTIAL PASS for public API-level read/identity/sandbox feasibility; no production authority implied.
- **Dropshipzone/New Aim:** PARTIAL PASS for documented Shopify/inventory/order/tracking integration surface; exact API/account contract still UNKNOWN.
- **DSers/AliExpress-style class:** UNKNOWN / insufficient authoritative API evidence this cycle.

This is enough to proceed with synthetic cross-system exception modelling. It is not enough to claim production supplier integration readiness or commercial viability.

## Sources checked

- Dropshipzone retailer user guides and API-integration guide index, checked 2026-09-14.
- CJdropshipping developer documentation: API introduction, products synchronization, orders synchronization, product inventory, shop/product-connection resources, checked 2026-09-14.
