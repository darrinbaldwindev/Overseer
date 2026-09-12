# Content360 Evidence Expiry + Recheck Rules — 2026-09-12

**Owner:** Marketing Overseer  
**Status:** ACTIVE STANDARD

## Purpose

Prevent stale social content from continuing to make live commercial claims after price, stock, freight, delivery, programme terms, eligibility or product facts have changed.

## Dynamic claim classes

### Class A — Fast-changing commercial facts
Examples: price, stock, eBay availability, supplier availability, delivery time, freight basis, promo code, affiliate rate, signup bonus.

Default recheck: before publication and again before any scheduled repost older than 72 hours.

### Class B — Medium-changing programme/offer facts
Examples: country availability, minimum payout, reward method, return window, warranty period, programme eligibility.

Default recheck: before publication; every 30 days while actively promoted; immediately after known programme/store policy change.

### Class C — Product specification facts
Examples: dimensions, material, compatibility, included items.

Default recheck: against canonical product/listing source before first promotion and whenever supplier/listing identity changes.

### Class D — Stable educational/brand statements
Examples: category education, general problem-solution content, approved brand positioning.

Recheck on source-of-truth change, campaign refresh, or material product-direction change.

## Automatic marketing response to expiry

When evidence expires:
- direct conversion CTA becomes blocked;
- scheduled repost is held;
- dynamic claim is removed or qualified;
- asset status becomes `REVERIFY-EVIDENCE`;
- the relevant project workstream receives a bounded recheck request.

Expired evidence is not equivalent to false information; it means the claim is no longer sufficiently current for publication.

## Product-specific rules

### GlobalShopCo / Shopify→eBay
Price, stock, freight/delivery and current listing availability are Class A. Safety/material/specification claims require exact source matching. Missing freight evidence remains a hard promotion blocker when free-delivery economics or margin depend on it.

### Affiliate Websites
Programme availability, reward, payout and referral terms are at least Class B and may be Class A where promotions are temporary. Country eligibility must be explicit.

### AgentOS
Implementation/performance claims expire when relevant runtime, release, benchmark or product state changes. Pricing/tier claims follow the current commercial source of truth.

### GhostKitchen / Franchise
Financial/legal/compliance claims require dedicated review and should not be treated as ordinary Class A/B marketing facts.

## Repost rule

Content360 convenience must never override freshness. Before a scheduled repost, the system/operator must validate whether the post contains dynamic claims and whether their evidence remains current.
