# GlobalShopCo Headless — SEO/AEO Vertical Page Contract

**Date:** 2026-09-14 Brisbane
**Owner:** Marketing Overseer
**Status:** PREPARED / NOT DEPLOYED / SHOPIFY REMAINS CANONICAL

## Purpose
Define a WordPress/headless page contract that can rank and answer useful questions without becoming a second source of product, price, stock, delivery or checkout truth.

## Source-of-truth rule
Shopify remains canonical for:
- product identity and publication state;
- current title/variant data where approved;
- price;
- stock/availability;
- cart/checkout destination;
- current commercial status.

WordPress/headless may own editorial explanation, comparison context, how-to content, FAQs and internal-link structure. It must fail closed when canonical commerce data is stale, missing or conflicting.

## Vertical page structure
1. **H1:** user problem/category, not an unsupported product superlative.
2. **Opening answer:** concise explanation of who the category is for and how to choose.
3. **Selection criteria:** dimensions, use case, materials, maintenance, delivery considerations, returns/fit risks where relevant.
4. **Current qualified products:** only products whose canonical eligibility is current.
5. **Comparison table:** only current evidenced attributes; unknown fields display as unknown or are omitted.
6. **How we qualify products:** transparent trust block linking to evidence/qualification methodology.
7. **FAQ:** question-led content suitable for AEO.
8. **Related guides:** editorial cluster links.
9. **Commerce handoff:** canonical Shopify product/cart/checkout link only when current state permits it.

## Commerce freshness contract
A product/Offer block may render only when the retrieval layer proves:
- canonical Shopify product id/variant id;
- product is publication-eligible for the owned site;
- price was retrieved within the defined freshness window;
- availability is current enough for the chosen wording;
- checkout handoff URL is valid;
- no conflicting hold/research tags are present.

If any required field is absent or stale, render the prepared fail-closed trust state rather than cached commerce claims.

## Schema contract
### Allowed without live product eligibility
- `WebPage`
- `CollectionPage` where appropriate
- `Article`
- `FAQPage` only for genuine visible FAQ content and where current search-engine policy permits use
- `BreadcrumbList`
- `Organization`/site identity from canonical brand data

### Product schema
`Product` may be emitted only for a real, currently eligible product represented faithfully on-page.

### Offer schema
`Offer`/`AggregateOffer` must **not** be emitted from stale, inferred, placeholder or editorial pricing. Require canonical current price/currency/availability and valid purchase path.

Do not manufacture:
- `InStock` from supplier public stock when Shopify/canonical channel state is unknown;
- price from competitor retail pages;
- free-shipping claims from site-wide intent unless current SKU economics/fulfilment support the promise;
- ratings/reviews not belonging to the exact product/seller context.

## SEO copy rules
Safe wording:
- `How to choose...`
- `What to measure before buying...`
- `Things to check before ordering...`
- `Compare current qualified options`
- `Availability and prices can change; current purchase details are shown when verified.`

Locked until evidence:
- `best price`
- `lowest price`
- `in stock now`
- `fast delivery`
- `free delivery` at product level
- `best seller`
- `top rated`
- unsupported warranty/return promises

## AEO question families
For Home Organisation:
- What size organiser fits a standard drawer/pantry/fridge shelf?
- How should I measure before buying an organiser?
- What materials are easiest to clean?
- When are stackable bins useful?
- What makes an organiser expensive to ship?
- What should I check in returns policies for storage products?

Answers should remain product-agnostic unless a current qualified product can be referenced.

## Stale-state behavior
If Shopify data becomes stale or unavailable:
- keep editorial content visible;
- hide or neutralise transactional price/stock claims;
- display `Current purchase details are temporarily unavailable` or equivalent truthful state;
- do not substitute cached competitor/supplier data;
- preserve canonical checkout handoff only when validated.

## Internal linking
Vertical page should link to:
- measurement guide;
- material/cleaning guide;
- delivery/economics explainer where useful;
- relevant subcategory guide;
- qualification-methodology page;
- current qualified product pages only.

## Acceptance tests before deployment
1. stale Shopify price cannot render as current Offer;
2. unavailable Shopify retrieval cannot produce `InStock`;
3. research/HOLD product cannot appear as purchasable;
4. competitor/supplier retail price cannot become site Offer price;
5. Product/Offer schema disappears or fails closed when canonical commerce state expires;
6. editorial content remains usable during commerce outage;
7. checkout button cannot point to noncanonical purchase path;
8. free-delivery wording is SKU/channel evidence-gated;
9. unknown returns/warranty fields do not become generic promises;
10. visible page text and structured data remain semantically consistent.

## Launch posture
This template is ready for implementation planning, but no vertical is commercially launch-ready until at least one real qualified product proves Shopify retrieval → truthful headless display → canonical checkout handoff end-to-end.

**NO DEPLOYMENT / NO PRODUCT ACTIVATION / NO SECOND COMMERCE SOURCE OF TRUTH.**