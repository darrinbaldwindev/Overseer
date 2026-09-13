# GlobalShopCo Headless — Marketing Readiness Gate

**Date:** 2026-09-13  
**Owner:** Marketing Overseer / ChatGPT Overseer  
**Status:** PRE-PRODUCTION PREPARATION ONLY / NOT PUBLISHED

## Current source-of-truth boundary

The GlobalShopCo-Headless repository currently authorises only a non-production vertical slice:

1. retrieve a controlled test product through an approved Shopify Storefront API path;
2. present approved product fields and safe failure states in WordPress;
3. hand purchase back to approved Shopify cart/checkout.

Shopify remains authority for catalogue, product, price, inventory, cart, checkout and orders.

No production deployment, WordPress installation, Shopify credential, product publication, payment processing, analytics, bulk catalogue migration or release process is authorised by the repository’s existence.

Marketing must therefore treat this lane as **architecture/experience preparation**, not a live acquisition channel.

---

## Marketing work safe to prepare now

### Information architecture

Prepare reusable headless structures without binding them to unapproved products:

- Home
- Category landing
- Product detail
- Comparison / guide
- Delivery / returns information
- About / trust
- Contact / support

Potential niche families already aligned with portfolio direction may include Baby / Pet / Safety, but pages must not imply stocked/approved inventory until Shopify evidence exists.

### Product-page contract for Marketing

Marketing content may consume only approved Shopify fields plus explicitly approved editorial fields.

Product page should be designed to clearly separate:

- canonical product title/specs/price/availability from Shopify;
- editorial explanation/use-case content;
- delivery/returns statements sourced from current policy/evidence;
- purchase CTA handing off to Shopify checkout.

Marketing must not create an independent price/stock database in WordPress.

### SEO/AEO preparation

Prepare templates for:

- canonical title/meta fields;
- product structured data derived from canonical Shopify data;
- category intro copy;
- FAQ only where answers are supported by policy/product evidence;
- comparison methodology disclosure;
- internal linking rules;
- index/noindex behavior for test/staging pages;
- canonical URL strategy to avoid duplicate-commerce confusion.

### Trust UX

A headless storefront should make clear:

- current price/availability comes from the commerce source of truth;
- checkout occurs through Shopify;
- delivery/returns terms are evidence-backed and current;
- unavailable/error states do not silently show stale purchase information.

---

## Measurement preparation

Analytics is not currently authorised, but Marketing can define the future measurement plan:

- landing page → product detail;
- product detail → Shopify checkout handoff;
- category → product clickthrough;
- comparison/guide → product intent;
- checkout handoff success/failure;
- source/campaign attribution;
- content-assisted conversion.

Implementation must wait for analytics/release authority and privacy/consent requirements.

---

## Content360 role

Content360 may later optimise approved editorial/headless content after:

- page exists in an authorised environment;
- product facts are sourced from Shopify;
- claims pass evidence checks;
- destination URL is valid;
- publication gate exists.

It must not create independent product truth or publish around the headless prototype prematurely.

---

## Activation gate

Marketing channel activation requires at minimum:

1. authorised WordPress/headless environment;
2. approved Shopify Storefront integration;
3. tested canonical product/price/inventory rendering;
4. safe failure/stale-data behavior;
5. tested Shopify checkout handoff;
6. legal/privacy/trust pages;
7. SEO/canonical/indexing checks;
8. analytics/consent authority if analytics is enabled;
9. real approved products suitable for the target niche;
10. owner publication approval.

## Current blocker

This lane is prepared but remains non-production. The next marketing action belongs to Affiliate Websites or GhostKitchen while Headless implementation remains gated.
