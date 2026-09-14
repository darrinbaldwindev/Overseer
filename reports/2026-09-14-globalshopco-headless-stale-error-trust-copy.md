# GlobalShopCo Headless — Stale/Error/Trust Copy Contract

**Date:** 2026-09-14 AEST  
**Status:** PREPARED / NOT DEPLOYED

## Purpose
Provide evidence-safe customer-facing copy for the WordPress/headless presentation layer while Shopify remains canonical for catalogue, price, stock, cart and checkout.

The presentation layer must fail safely when canonical commerce data is missing, stale, conflicting or unavailable.

## Product truth rules
1. WordPress/headless must not become the source of truth for stock, price or checkout eligibility.
2. A stale cached value must not be presented as confirmed live commerce truth.
3. Missing Shopify state must not be converted into a guessed price, stock message or delivery promise.
4. A product may remain editorially visible while purchase action is withheld if canonical commerce evidence is unavailable.
5. Marketing copy must distinguish editorial suitability from commercial qualification.

## Recommended customer-facing states

### Fresh canonical commerce state
Use normal product presentation only when Shopify evidence is current enough for the product contract.

Suggested microcopy:
- `Price and availability confirmed.`
- `Checkout is handled securely through Shopify.`

Do not add this confirmation unless the implementation can actually prove the required freshness condition.

### Price unavailable
Primary:
`Price temporarily unavailable`

Support:
`We can't confirm the current price right now. Please check again shortly.`

Action:
- hide/disable price-dependent purchase CTA;
- do not substitute an old or placeholder price.

### Stock unavailable / unknown
Primary:
`Availability not confirmed`

Support:
`We can't confirm current stock right now.`

Avoid:
- `In stock` based on stale cache;
- artificial urgency;
- `Only X left` without canonical evidence.

### Product data stale
Primary:
`We're refreshing this product`

Support:
`Some product details may have changed. Purchase options will return when the latest information is confirmed.`

### Shopify checkout unavailable
Primary:
`Checkout temporarily unavailable`

Support:
`We can't open the verified checkout right now. No order has been placed.`

This state must never offer an alternate ungoverned payment route.

### Product no longer commercially qualified
Primary:
`Currently unavailable to buy`

Support:
`We're reviewing this product before offering it for sale.`

Editorial content may remain if truthful, but remove price/stock/delivery/shop-now claims that depended on the failed qualification.

### Delivery evidence incomplete
Primary:
`Delivery details not yet confirmed`

Support:
`We'll show purchase options once delivery costs and timing are verified.`

Because GlobalShopCo intends free delivery, do not display `Free delivery` until the per-SKU economics and fulfilment evidence support it.

### Returns/warranty evidence incomplete
Primary:
`Purchase details still under review`

Support:
`Returns or warranty information has not yet been fully confirmed for this product.`

Do not copy generic returns promises across suppliers unless the canonical product contract proves them.

## Trust component
A small reusable trust disclosure may say:

`Product information is shown only when we can confirm the important details. If price, stock, delivery or checkout information cannot be verified, we pause the purchase option rather than guess.`

This aligns with GlobalShopCo's strongest defensible prelaunch trust proposition: fewer, better-qualified products rather than catalogue breadth.

## Internal implementation states
Recommended presentation mapping:
- `FRESH` → normal commerce presentation;
- `STALE` → refresh warning, purchase CTA gated as required;
- `UNKNOWN` → fail closed;
- `CONFLICT` → fail closed + reconciliation message;
- `UNAVAILABLE` → no purchase action;
- `QUALIFICATION_HOLD` → editorial-only where appropriate;
- `REJECTED` → remove commercial CTA/listing surface.

These labels are implementation guidance only; reuse canonical project states if they already exist instead of creating a parallel status system.

## SEO/AEO boundary
If a product page is indexable while commerce data is stale:
- structured product offers must not assert current price/availability unless canonical data is fresh;
- avoid stale `InStock`, price, shipping or offer-validity markup;
- informational sections may remain indexable if factually current;
- canonical purchase CTA returns only after current Shopify state is available.

## Current disposition
**PREPARED / NOT DEPLOYED.** This is presentation copy and a fail-closed UX contract. It does not qualify any SKU, prove Shopify→WordPress synchronization, or authorize publication.
