# Commercial Frontend Provider Adapter Evidence Table

**Date:** 2026-09-14  
**Providers:** CJdropshipping, Dropshipzone / New Aim  
**Scope:** current authoritative documentation only; no credentials, live calls, supplier contact, connector activation or production mutation.

## Purpose

Reduce the supplier-side UNKNOWN into exact evidence fields that could later support a provider-neutral read/evidence adapter. This is not a production connector design and does not grant authority to mutate provider state.

## Evidence classification rules

- `DOCUMENTED`: explicit in current first-party provider documentation.
- `PARTIAL`: enough evidence for bounded modelling, but ordering/version/freshness semantics are incomplete.
- `UNKNOWN`: do not infer.

A field is not authoritative merely because it exists in a UI/app. Provider sequence/version/time ordering is only authoritative if the provider documents its semantics.

---

# CJdropshipping

Authoritative documentation reviewed:
- API V2.0 interface list: `https://developers.cjdropshipping.com/en/api/api2/`
- Product / Variant / Stock: `https://developers.cjdropshipping.com/en/api/api2/api/product.html`
- Shop / Product Connection: `https://developers.cjdropshipping.com/en/api/api2/api/shop.html`
- Shopping / Order: `https://developers.cjdropshipping.com/en/api/api2/api/shopping.html`
- Logistics interface list / tracking: API V2.0 docs
- CJ Start / Sandbox / Webhook documentation navigation: `https://developers.cjdropshipping.com/en/api/start/`

## Identity and evidence table

| Evidence need | Current documented field/surface | Classification | Commercial Frontend rule |
| --- | --- | --- | --- |
| Provider identity | adapter/provider constant `CJdropshipping`; API host under `developers.cjdropshipping.com` | DOCUMENTED | bind adapter evidence to provider constant + endpoint family; never infer provider from SKU alone |
| Request identity | API error examples include `requestId` | PARTIAL | useful diagnostic evidence where returned; not documented as event-order authority |
| Product identity | `pid`, `productSku` / SPU | DOCUMENTED | preserve exact CJ product ID and SKU |
| Variant identity | `vid`, `variantSku`; `queryByVid` explicitly uses unique Variant ID | DOCUMENTED | variant-level actions/evidence must bind exact VID and SKU where available |
| Platform product mapping | Product Connection API exposes `shopId`, `platformProductId`, platform variant connection fields | DOCUMENTED | use connection record to correlate provider variant to Shopify/platform identity; mismatch => BLOCK |
| Shop identity | `shopId` in Product Connection / store surfaces | DOCUMENTED | bind supplier evidence to exact connected shop where relevant |
| Warehouse/area identity | stock response includes `areaId`, country/area, sub-warehouse `stockId`; shopping confirmation exposes storage IDs | DOCUMENTED | inventory evidence is warehouse-scoped; do not collapse separate warehouse stock without rule |
| Inventory quantity | `storageNum`, `totalInventoryNum`, `cjInventoryNum`, `factoryInventoryNum`, sub-warehouse inventory | DOCUMENTED | retain inventory type/source; do not treat factory inventory and CJ-managed inventory as interchangeable without explicit policy |
| Inventory lookup by variant | `/product/stock/queryByVid` | DOCUMENTED | preferred exact variant read seam |
| Inventory lookup by SKU | `/product/stock/queryBySku` | DOCUMENTED | SKU evidence requires exact SKU/SPU semantics; variant ambiguity must block |
| Product/variant update time | product variant object documents fields such as update/design-related timestamps; exact universal stock-event timestamp semantics not established | PARTIAL | field may support recency for that returned object only; do not invent global event ordering |
| Order identity | shopping order endpoints expose platform/client order-number inputs and provider order detail/list surfaces | DOCUMENTED/PARTIAL | preserve both platform order identity and CJ order identity when returned; no cross-order inference |
| Order status progression | platform logistics/order process documentation exists; exact event sequence semantics require endpoint-specific contract validation | PARTIAL | safe for state vocabulary modelling, not yet a universal sequence number |
| Tracking lookup | logistics `trackInfo` endpoint documented | DOCUMENTED | bind tracking evidence to exact provider/order/package context returned by endpoint |
| Webhook support | CJ Start navigation includes Webhook docs | DOCUMENTED AT CAPABILITY LEVEL | webhook event names/payload IDs/version semantics require endpoint-level validation before use |
| Sandbox support | CJ Start navigation includes Sandbox | DOCUMENTED AT CAPABILITY LEVEL | later non-production feasibility candidate; no live calls in this workstream |
| Authoritative event sequence/version | no universal documented sequence/version field established by this review | UNKNOWN | arrival time cannot substitute; contradictory same-version concept remains synthetic until provider contract proves version semantics |
| Event source timestamp | no universal provider-event source timestamp established across product/stock/order/tracking by this review | UNKNOWN/PARTIAL | use endpoint-specific timestamps only when documented and preserve semantic name |

## CJ adapter conclusion

`PARTIAL PASS FOR PROVIDER-NEUTRAL READ/EVIDENCE MODELLING`.

Strong identity primitives exist for product, variant, shop connection, warehouse, inventory and order/logistics surfaces. The remaining critical UNKNOWN is a universal authoritative event-order/version contract. Therefore the Commercial Frontend may model snapshot freshness and exact identity, but must not claim strict provider event ordering solely from local arrival order.

---

# Dropshipzone / New Aim

Authoritative documentation reviewed:
- API integration guide: `https://web.dropshipzone.com.au/user-guide/integrate-with-apis`
- Retailer inventory guide: `https://web.dropshipzone.com.au/user-guide/managing-inventory`
- Retailer Shopify binding/import guide: `https://web.dropshipzone.com.au/user-guide/importing-products`
- Supplier shipping/fulfilment guide: `https://web.dropshipzone.com.au/user-guide/shipping-and-fulfilment`
- Dropshipzone FAQ: `https://www.dropshipzone.com.au/faq`

## Important provider-side distinction

Dropshipzone documentation contains both **Supplier** and **Retailer** integration surfaces. Commercial Frontend Ecommerce work for GlobalShopCo is normally retailer-side. Supplier API documentation must not automatically be treated as retailer API authority.

## Identity and evidence table

| Evidence need | Current documented field/surface | Classification | Commercial Frontend rule |
| --- | --- | --- | --- |
| Provider identity | Dropshipzone account/app/API surface | DOCUMENTED | bind provider explicitly; do not infer from product SKU alone |
| Auth identity | supplier API guide documents `/auth`, access token, JWT header, token lifetime of roughly 8 hours | DOCUMENTED FOR SUPPLIER API | not automatically a retailer API contract; no credentials used here |
| API functional domains | supplier integration guide lists Auth, Category, Order, Product, Shipping | DOCUMENTED FOR SUPPLIER API | demonstrates structured API surface, but exact retailer endpoint schema remains UNKNOWN from this guide |
| Product/SKU identity | retailer guides consistently use SKU as binding/update unit | DOCUMENTED | exact SKU is core identity; unbound/mismatched SKU must block automated recommendation |
| Shopify binding identity | retailer app uses `Bound` / `Unbound`; products imported through app are automatically bound | DOCUMENTED | bound state is required context for reliable Shopify auto price/inventory sync |
| Inventory quantity/current stock | retailer portal/product listing/All SKU list; API can retrieve stock level; Shopify app syncs stock | DOCUMENTED | preserve source and observation time; do not call an unbound Shopify quantity provider-authoritative |
| Inventory history window | retailer inventory guide says API can retrieve stock-level records for the past 10 days only | DOCUMENTED | history older than 10 days cannot be assumed queryable through that surface |
| Inventory update cadence | retailer guide: Dropshipzone API updates hourly; SKU list hourly; Shopify app updates when DSZ account inventory changes; supplier app has hourly sync | DOCUMENTED | one-hour cadence is not an event sequence/version; freshness policy can use documented cadence conservatively |
| Product revision signal | retailer notification page exposes SKU updates and a `Revision` column describing change type | DOCUMENTED AT UI LEVEL | useful human evidence; exact machine-readable revision/version semantics are UNKNOWN |
| Retailer order identity | user guides refer to order number, order SKU, order date, order status | DOCUMENTED AT PORTAL LEVEL | preserve exact order number + SKU; API field names for retailer side remain UNKNOWN unless integration docs expose them |
| Order statuses | supplier fulfilment guide documents Canceled, Complete and Pending Pay, Processing, Invoiced | DOCUMENTED FOR SUPPLIER PORTAL | do not assume retailer-side status model is identical without explicit docs |
| Tracking identity | supplier guide records carrier + tracking number on shipment/order | DOCUMENTED FOR SUPPLIER PORTAL | tracking must bind exact order/SKU/package context; retailer API event contract remains UNKNOWN |
| Customer communication boundary | FAQ says Retailer is responsible for customer relationships and Dropshipzone does not communicate with customer | DOCUMENTED | supports vertical rule that customer communication remains merchant-controlled |
| Real-time vs delayed processing | supplier API guide says most data real-time; retailer orders delayed a few minutes due to scheduled job sync | DOCUMENTED FOR SUPPLIER API | useful delay expectation, not strict ordering/version authority |
| Authoritative event sequence/version | no exact retailer-side machine-readable sequence/version contract established in reviewed docs | UNKNOWN | do not resolve contradictory inventory/tracking by arrival order alone |
| Event source timestamp | portal exposes order date and UI histories; exact retailer API event/source-time fields not established | PARTIAL/UNKNOWN | preserve known dates but do not invent event-time semantics |
| Retailer public API endpoint schema | not established from current reviewed authoritative public docs | UNKNOWN | no live adapter implementation; next evidence task should target retailer integration-guide schema if publicly exposed |

## Dropshipzone adapter conclusion

`PARTIAL PASS FOR IDENTITY/FRESHNESS MODELLING / RETAILER API CONTRACT STILL INCOMPLETE`.

Retailer-side documentation strongly establishes SKU binding, inventory sync behavior and cadence, product revision notifications, and Shopify binding requirements. The reviewed public API guide is explicitly supplier-oriented, so it must not be promoted into a retailer API write/read contract without further exact documentation.

---

# Provider-neutral evidence envelope

A later read/evidence adapter should emit only documented fields and preserve provider semantics rather than normalising away uncertainty:

```text
provider
provider_account_or_shop_id?      # only when documented/available
platform_shop_id?
provider_product_id?
provider_variant_id?
provider_sku
platform_product_id?
platform_variant_id?
provider_order_id?
platform_order_id?
package_or_fulfilment_id?
warehouse_or_storage_id?
evidence_kind                     # stock/order/tracking/connection/revision
observed_value
evidence_source
provider_source_time?             # only endpoint-specific documented semantics
provider_version_or_sequence?     # UNKNOWN unless explicitly documented
affected_sku_or_variant
observed_at                       # local observation; never silently upgraded to provider authority
request_id?                       # diagnostic only unless provider contract says otherwise
```

## Fail-closed rules

1. Missing exact product/variant/SKU identity -> BLOCK.
2. Platform/provider connection mismatch -> BLOCK.
3. Warehouse/package/order ambiguity -> BLOCK or manual reconciliation.
4. Local arrival timestamp does not establish authoritative provider ordering.
5. Provider version/sequence may only be used when documented by that provider/endpoint.
6. Snapshot freshness may use documented update cadence as a conservative limit, but cadence is not exactly-once/event-order evidence.
7. Supplier-side Dropshipzone API documentation must not be treated as retailer-side authority.
8. No provider document reviewed here authorizes autonomous Commercial Frontend writes.

## Result

- CJdropshipping: `PARTIAL PASS` for exact identity + snapshot evidence modelling; universal event-order/version remains UNKNOWN.
- Dropshipzone/New Aim: `PARTIAL PASS` for retailer SKU/binding/inventory freshness modelling; exact public retailer API event schema/order/version remains UNKNOWN.
- No connector activation, credentials, write authority, supplier contact or production readiness is established.

**Classification:** `PROVIDER-EVIDENCE-MODEL-READY / CONNECTOR-PRODUCTION-HOLD`.
