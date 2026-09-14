# GlobalShopCo + Shopify→eBay — Marketing Readiness Delta

**Date:** 14 September 2026  
**Owner:** Marketing Overseer  
**Status:** PRELAUNCH / 0 EBAY-READY SKUS / PUBLICATION HOLD  
**Canonical coordination:** `darrinbaldwindev/Overseer#49`, `darrinbaldwindev/GlobalShopCo#17`

## Purpose

Separate technical connector progress from real SKU commercial readiness so Marketing, Content360 and downstream channel work cannot accidentally turn infrastructure evidence into product-launch claims.

## Fresh-scan reconciliation

### 1. Connector installed/account connected
**Status: VERIFIED**

Current durable evidence supersedes the older Issue #17 setup recommendation. Shopify Marketplace Connect is already installed and eBay Australia account `globalshopco` is connected.

Marketing consequence: do not recommend installing a second connector merely because older documentation preferred Omnivore/eBay LINK. The current question is assurance of the installed path.

This fact does **not** imply listings are correct, inventory/order/tracking sync is reliable or publication is authorised.

### 2. Synthetic adapter/contract behavior
**Status: VERIFIED at bounded non-production scope**

The `shopify_ebay` workstream has deterministic no-network contract evidence on non-production branch lineage. Current durable evidence includes:

- candidate mapping with explicit UNKNOWN preservation;
- audit receipts binding Shopify identity/SKU/input hash/gate result;
- inventory-change contract receipt;
- synthetic eBay-order→Shopify handoff preserving Shopify order authority;
- tracking candidate requiring exact Shopify/eBay order correlation;
- duplicate-event/idempotency denial;
- `publication_authority=False` and `network_io=False` in the bounded fixtures;
- exact-head fixture validation SUCCESS at the latest evidenced synthetic checkpoint.

Marketing consequence: this is valuable assurance design evidence, not a reason to call Marketplace Connect production-ready.

### 3. Real Marketplace Connect behavior
**Status: NOT VERIFIED / HOLD**

Still requires production-safe or otherwise authorised acceptance evidence for:

- listing field/category/image mapping;
- Shopify→eBay inventory propagation;
- eBay order import to Shopify;
- tracking/fulfilment propagation;
- cancellation/stock-out protection;
- duplicate/oversell behavior;
- exact fee/pricing rule behavior;
- reliability under current eBay/Shopify conditions.

Recent project evidence also records public reports of eBay inventory/listing/connection failures in Marketplace Connect during September 2026. Therefore connector presence should not be marketed as channel readiness.

### 4. Per-SKU commercial/channel eligibility
**Status: 0 EBAY-READY SKUS**

The key commercial gate remains exact supplier/channel/economics proof.

#### Home Organisation
Fresh exact-SKU closure for `V178-36336` (CARLA HOME 2-tier microwave rack):

- NewDeals public delivered path: A$37.99;
- exact black 2-tier retail offer observed at A$34.95 with free shipping;
- supplier/public delivered input is already A$3.04 above that exact retail offer before eBay/payment fees, returns/losses or operating margin.

Disposition: **REJECT / NOT FIRST-LAUNCH at current evidence**.

Do not revive this SKU as a marketing candidate unless materially lower authorised acquisition evidence appears.

Other Home Organisation candidates remain evidence-gated on exact comp, marketplace permission/stock model, seller identity/blind shipping, authenticated trade price, postcode freight and free-delivery contribution.

#### Southern Pet / GiGwi
Current five-candidate family remains **PERMISSION-REQUIRED / HOLD** because supplier standards require written approval for eBay/other marketplace fulfilment.

Public stock/freight evidence makes this family comparatively well specified, but trade prices remain decisive and supplier permission is not optional.

Marketing must not translate `PERMISSION-REQUIRED` into “coming soon”, “approved”, “available”, “launching” or similar forward-availability wording.

#### Eleganter
Current known owned-site dropship terms remain incompatible with eBay/Amazon/third-party marketplace fulfilment.

Disposition: **NOT ELIGIBLE** unless supplier terms materially change.

### 5. Publication authority
**Status: NONE**

No product should be published to eBay or promoted as eBay-available from this work. No paid acquisition should point to products that have not cleared channel/economics evidence and a verified purchase path.

## Marketing activation ladder

### RED — current state
Use when:
- 0 SKUs evidence-complete;
- real connector behavior not accepted;
- supplier/channel/economics fields remain UNKNOWN/HOLD;
- publication authority absent.

Allowed work:
- research;
- product-value proposition shells;
- title/attribute schema;
- category/keyword research;
- organic/prelaunch content architecture;
- email capture plan;
- Content360 templates with claim locks;
- buyer FAQ structures;
- launch measurement plan.

Not allowed:
- live listing claims;
- “available now”;
- “free delivery” unless exact economics/delivery coverage are verified;
- discount claims;
- profit/margin claims;
- supplier-approved claims;
- paid product campaigns;
- eBay listing publication.

### AMBER — first candidate evidence-complete but connector acceptance incomplete
Use only when at least one real SKU clears supplier/channel/economics gates but real Marketplace Connect behavior still lacks required acceptance.

Allowed:
- final copy proofing;
- listing draft payloads outside production;
- channel-specific image/attribute checklist;
- Content360 optimisation of already verified facts.

Still prohibited:
- production listing/publication;
- paid acquisition to eBay;
- “now on eBay” claims.

### ACTIVATION-READY
Requires both:

1. at least one SKU with complete supplier/channel/economics evidence and positive conservative free-delivery contribution; and
2. real connector acceptance for the intended listing/inventory/order/tracking path under authorised test conditions.

Then Marketing must still obtain explicit publication/campaign authority before activation.

## First-launch SKU marketing contract

A SKU cannot enter final marketing production without these fields:

- canonical Shopify product/variant ID;
- exact supplier;
- exact SKU + GTIN/EAN where applicable;
- supplier marketplace/eBay permission evidence;
- stock ownership/pre-purchase compatibility;
- blind-shipping / seller-identity / packing evidence;
- current stock-control method;
- dispatch origin;
- handling time;
- tracking method;
- delivery exclusions;
- authorised trade/wholesale cost + GST treatment;
- freight/landed cost by required zones;
- eBay + integration + payment cost allowance;
- conservative returns/loss allowance;
- proposed selling price;
- verified free-delivery contribution;
- returns policy;
- warranty;
- compliance/category constraints;
- evidence freshness/date;
- remaining UNKNOWNs;
- publication authority state.

If any field that materially affects legality, availability, delivery or economics is UNKNOWN, Marketing treats the SKU as HOLD.

## Content360 boundary

Content360 may receive only fields already cleared by Marketing against current project evidence.

It may optimise:
- verified title structure;
- factual feature/use-case wording;
- channel formatting;
- SEO keyword placement;
- approved FAQs;
- social variants;
- approved image captions/alt text.

It may not infer:
- stock availability;
- supplier permission;
- discount/savings;
- free-delivery viability;
- profitability;
- eBay-readiness;
- delivery coverage;
- warranty/returns not backed by current evidence.

## Organic prelaunch work that is safe now

While product activation remains blocked, Marketing can prepare:

1. Home Organisation problem/solution editorial topics without naming unqualified products as available;
2. category-level keyword clusters;
3. buyer guides that explain what to check in storage/organisation products;
4. email/waitlist capture language framed around future store updates, not a specific unapproved SKU;
5. product-page and eBay-listing templates with locked evidence fields;
6. launch analytics/measurement definitions;
7. FAQ structures around delivery, returns and warranty that pull from verified per-SKU data at publication time.

## Immediate next marketing actions

1. Consume the next exact-SKU closure from the GlobalShopCo lane and remove rejected candidates promptly.
2. Prepare first-launch copy only for a candidate that passes supplier/channel/economics evidence; do not keep writing final copy for likely rejects.
3. Maintain a strict distinction between connector assurance and SKU readiness in every Content360/eBay handoff.
4. When a first evidence-complete SKU appears, immediately produce the full listing/product-page/social/email asset set, but leave production activation gated until connector acceptance and explicit authority are both present.

## Status summary

- Marketplace Connect installed/account connected: **VERIFIED**.
- Synthetic adapter/contracts: **VERIFIED at bounded fixture scope**.
- Real connector behavior: **NOT VERIFIED / HOLD**.
- eBay-ready SKUs: **0**.
- Home Organisation `V178-36336`: **REJECT / NOT FIRST-LAUNCH** at current economics.
- Southern Pet family: **PERMISSION-REQUIRED / HOLD**.
- Eleganter current candidates: **NOT ELIGIBLE**.
- Paid acquisition: **HOLD**.
- Listing publication: **NOT AUTHORISED**.
- Overall GREEN: **NOT CLAIMED**.