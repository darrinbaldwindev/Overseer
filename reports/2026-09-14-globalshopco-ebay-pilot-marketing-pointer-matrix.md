# GlobalShopCo eBay Pilot — Marketing Evidence Pointer Matrix

**Date:** 14 September 2026  
**Purpose:** Marketing-only pointer layer over canonical GlobalShopCo/eBay evidence.  
**Authority rule:** this report does not become supplier, stock, freight, economics, connector or publication source of truth.

## Current launch state

**0 eBay-ready SKUs / PILOT NOT READY / PUBLICATION HOLD.**

Fresh Issue #17 evidence still ranks the Southern Pet GiGwi family as the closest commercial path but explicitly requires written marketplace permission and authenticated trade cost. The newest source-hunt batches state the active pilot is capped at eight candidates, but do not publish a fresh authoritative eight-member roster in the latest checkpoint. Marketing therefore does **not** guess which three backups currently join the five Southern Pet SKUs.

That distinction is intentional: a pointer matrix must fail closed rather than turn historical candidate lists into a false current shortlist.

## Tier A — current strongest five

| Supplier / SKU | Canonical evidence state | Marketing state | Allowed copy before clearance | Locked copy | Next evidence |
|---|---|---|---|---|---|
| Southern Pet / `GDAG2600` | Current stock/weight and freight framework publicly evidenced; eBay use requires prior written approval; trade cost login-only | PERMISSION-REQUIRED / HOLD | factual product attributes from verified source only | available on eBay; free delivery; profitable; supplier approved; in stock for sale | written eBay permission; authenticated trade cost+GST; exact GTIN; eBay comps; owned/prepurchase compatibility; returns/warranty; contribution |
| Southern Pet / `GDAG2522` | Same family gate; compact ~0.49kg class; current stock evidence exists | PERMISSION-REQUIRED / HOLD | verified factual attributes only | price/delivery/availability/approval/profit claims | same full gate |
| Southern Pet / `GDAG2515` | Same family gate; compact ~0.49kg class; current stock evidence exists | PERMISSION-REQUIRED / HOLD | verified factual attributes only | price/delivery/availability/approval/profit claims | same full gate |
| Southern Pet / `GDAG2505` | Same family gate; compact ~0.49kg class; current stock evidence exists | PERMISSION-REQUIRED / HOLD | verified factual attributes only | price/delivery/availability/approval/profit claims | same full gate |
| Southern Pet / `GDAG2610` | Same family gate; ~0.9kg makes zone/cubic freight more sensitive | PERMISSION-REQUIRED / HOLD | verified factual attributes only | price/delivery/availability/approval/profit claims | same full gate plus conservative zone/cubic freight |

### Marketing caution within Tier A

`GDAG2600` has especially strong retail-price pressure in current public evidence, so it must not be assumed commercially viable merely because it is compact and stocked. `GDAG2610` remains compact enough for modelling but is more freight-sensitive than the 0.4–0.49kg group.

## Tier B — historical project shortlist / current-membership not reasserted

The project previously ranked these as Priority-2 candidates:

- K&A `KAMP061`
- K&A `KAK103`
- K&A `H9016`
- CWS `SG118655`
- United Living `15510`

Their last durable classification is **UNKNOWN / HOLD** pending marketplace permission plus reliable freight/fulfilment economics.

Because newer source-hunt checkpoints say the active pilot is capped at eight but do not restate exact membership, Marketing records these five as **historical shortlist pointers, not the current active-three backups**.

No product-specific acquisition asset should be built for them until project evidence re-identifies current membership and freshness.

## Newer Home Organisation research — not admitted by Marketing

- `V178-36336` — REJECT / NOT FIRST-LAUNCH at current economics.
- `V178-36126` — demoted by retail compression.
- `V178-36023` — HOLD; authenticated trade/freight/permission missing.
- `V178-36045` — HOLD / secondary; freight-sensitive.
- `V178-36110` — HOLD / secondary; retail pressure.
- `V178-36219` — HOLD / likely first-wave reject unless authenticated trade economics are exceptional.
- `CAH-67362` — HOLD / secondary; not admitted.
- `CAH-67361` — REJECT first wave / research hold.

These are useful commercial research, not evidence that they belong to the current eight-SKU pilot.

## Connector boundary

Current Marketplace Connect/eBay AU connection is an existence fact only.

Newest adjacent synthetic `shopify_ebay` fixtures have progressed to exact head `ba904a8585a9bd2810ecd7f152028145ff6fa953` with Fixture validation SUCCESS for fail-closed stale inventory revision, duplicate order import, tracking-correlation mismatch and out-of-order tracking. The fixtures retain `publication_authority=False` and `network_io=False`.

Therefore the Marketing state machine remains:

> **CONNECTED ≠ SYNTHETIC CONTRACT VERIFIED ≠ REAL SYNC VERIFIED ≠ SKU ELIGIBLE ≠ PUBLISHED**

## Rapid-release trigger

A product may move from shell-only preparation to activation preparation only after canonical evidence closes all material fields:

1. exact supplier + SKU/GTIN;
2. explicit marketplace permission;
3. compatible ownership/prepurchase/fulfilment model;
4. seller identity / packing / buyer-data compliance;
5. authenticated stock method;
6. trade cost + GST;
7. destination-aware freight/landed cost;
8. eBay/integration/payment allowance;
9. returns/loss/warranty allowance;
10. proposed price and positive free-delivery contribution;
11. purchase path / real connector acceptance;
12. owner publication authority.

Any material UNKNOWN keeps final product marketing on HOLD.

## Next Marketing action

Consume the next project-owned exact roster/economics closure. If the canonical active eight is restated, update this pointer matrix immediately. Until then, concentrate product-shell preparation only on the five Southern Pet SKUs and non-product-specific Home Organisation editorial content.

**Status: VERIFIED POINTER LAYER / 5 PERMISSION-REQUIRED / ACTIVE-8 EXACT ROSTER PARTIALLY UNKNOWN / 0 EBAY-READY / NO PUBLICATION.**
