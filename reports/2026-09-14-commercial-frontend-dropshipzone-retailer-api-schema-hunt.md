# Commercial Frontend — Dropshipzone Retailer API Schema Hunt

Date: 2026-09-14

## Mission

Resolve CF-C010 without inferring retailer-side API authority from supplier documentation.

## Classification

- Retailer-side public integration surface: **VERIFIED at portal/Shopify-app workflow level**.
- Exact public retailer API schema: **UNKNOWN / NOT FOUND IN CURRENT AUTHORITATIVE PUBLIC DOCUMENTATION**.
- Supplier API documentation: **NOT VALID EVIDENCE for retailer API field authority**.
- Production connector authority: **NOT AUTHORIZED / NOT EVIDENCED**.

## Authoritative public evidence reviewed

Current Dropshipzone first-party retailer documentation exposes a large retailer guide surface covering:

- Shopify setup;
- importing products;
- price updates and auto-price sync;
- order placement and Auto Order Sync;
- order status/history;
- automatic fulfilment;
- inventory updates and automatic inventory sync;
- shipping calculator and postcode-zone mapping;
- tracking visibility in the retailer portal.

The current retailer guide index is:
`https://web.dropshipzone.com.au/learn/user-guides`

Current first-party shipping documentation states that tracking information is delivered by email and is also visible under **Dispatched** on the Orders page in the Dropshipzone retailer portal. It also documents retailer-side Shopify shipping-calculator and free-shipping-tag configuration.

Source:
`https://web.dropshipzone.com.au/user-guide/shipping`

The public site explicitly distinguishes retailer and supplier portals and roles. Retailers discover/import products and place orders; suppliers upload/manage products and fulfil retailer orders.

Sources:
- `https://web.dropshipzone.com.au/sell`
- `https://web.dropshipzone.com.au/supply`

## Schema hunt result

A fresh public-documentation search was performed for retailer API/integration documentation covering exact product/SKU/order/inventory/tracking field names, timestamps, sequence/version identifiers and retailer API authentication.

No authoritative public retailer REST/API schema was located in the reviewed current first-party material.

The public guide navigation does expose **Integrate with APIs**, but the reviewed API integration documentation belongs to the supplier integration path. It must not be promoted into a retailer adapter contract.

Therefore the following retailer-side fields remain **UNKNOWN as exact public API schema**:

- retailer account/shop identifier exposed by API;
- product identifier field name;
- SKU identifier field name;
- order identifier field name;
- line-item identifier field name;
- fulfilment/shipment identifier field name;
- tracking identifier and carrier field names;
- inventory quantity field names;
- authoritative source timestamp field names;
- event sequence/revision/version fields;
- webhook event identifiers;
- retailer API auth/scopes/rate limits.

## What is still usable now

Commercial Frontend may safely treat the following as **documented workflow evidence**, not API-field authority:

1. Dropshipzone retailer products are bound/imported into Shopify.
2. retailer inventory can be automatically synchronized into Shopify.
3. orders can be automatically synchronized from Shopify into Dropshipzone.
4. fulfilment can be automatically reflected back into Shopify.
5. tracking is surfaced in the retailer portal and email.
6. shipping rules and postcode-zone information are retailer-visible integration data.

These facts support a later mock/read-only adapter design, but not an exact production API contract.

## Fail-closed consequence

Until a retailer-side authoritative schema becomes available through public documentation or an explicitly authorized account/integration context:

- do not invent retailer REST endpoints;
- do not reuse supplier API field names;
- do not treat Shopify app behavior as proof of a public API;
- do not infer webhooks/event ordering;
- do not authorize supplier/retailer mutation from this evidence;
- preserve the exact retailer API schema as `UNKNOWN`.

## Commercial Frontend decision

CF-C010 is **VERIFIED AS NEGATIVE/UNKNOWN FINDING**.

This is useful evidence: a production Dropshipzone retailer adapter must either use a documented authorized integration mechanism available inside an approved retailer account, or remain behind a Shopify-facing/read-only abstraction until such evidence exists.

No credentials, account access, supplier contact, live API call or production mutation occurred.
