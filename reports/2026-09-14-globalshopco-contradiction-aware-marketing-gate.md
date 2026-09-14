# GlobalShopCo — Contradiction-Aware Marketing Gate

Date: 2026-09-14 AEST
Owner: Marketing Overseer
Status: ACTIVE MARKETING CLAIM GATE / NO PRODUCTION AUTHORITY

## Purpose
Mirror the current synthetic Shopify→eBay fail-closed evidence precedence into Marketing status language so a favourable flag can never override contradictory marketplace, source-identity or inventory evidence.

## Core rule
**Contradictory evidence outranks favourable evidence.**

A row cannot become `READY`, `ELIGIBLE`, `IN STOCK`, `MARKETPLACE APPROVED`, `FREE DELIVERY VIABLE` or `SHOP NOW` merely because one current-looking source says so when another material source conflicts.

## Contradiction classes that force HOLD
1. **Marketplace permission conflict**
   - one source suggests marketplace resale is allowed while another supplier/account/channel source restricts or conditions it.
2. **Product identity conflict**
   - SKU/GTIN/model/pack-count/size/included-component/title conflicts across sources.
3. **Inventory conflict**
   - Shopify, supplier feed, current catalogue or channel evidence disagree materially on availability/ownership.
4. **Freight/weight conflict**
   - actual/packed/cubic/shipping weight or destination freight evidence conflicts enough to change economics.
5. **Price/cost conflict**
   - trade/GST/cost basis is inconsistent or stale and the discrepancy can change contribution.
6. **Seller/fulfilment identity conflict**
   - evidence disagrees about who is seller of record, packing identity or fulfilment model.
7. **Returns/warranty conflict**
   - supplier/category/channel policies conflict materially with customer-facing promises.

## Status precedence
From strongest to weakest:
1. `REJECT` — evidence proves incompatibility or economics/risk are unacceptable.
2. `HOLD-CONTRADICTORY` — material evidence conflicts and canonical truth is unresolved.
3. `HOLD-UNKNOWN` — a required field lacks evidence.
4. `RESEARCH CANDIDATE` — identity is coherent enough for further evidence gathering but gates remain open.
5. `QUALIFIED FOR OWNED SITE` — only after owned-site gates pass; does not imply eBay.
6. `EBAY-ELIGIBLE` — only after all channel, ownership/fulfilment, economics, stock, seller identity, returns and account-path gates pass.
7. `PUBLISHED` — only after explicit publication authority and actual channel state prove it.

No lower-evidence state may be rendered or marketed as a higher state.

## Required Marketing language
When conflict exists:
- `Details conflict — not ready for sale`
- `Marketplace permission needs confirmation`
- `Product details do not match across current sources`
- `Stock cannot be confirmed`
- `Delivery cost cannot be confirmed`
- `Economics cannot be confirmed`

Avoid:
- `Available now`
- `eBay ready`
- `Approved`
- `Free delivery` as a product promise
- `Best price` / `profitable`
- `In stock`
unless the exact claim is supported by coherent current canonical evidence.

## Examples from current GlobalShopCo research
- CARLA HOME rotating-organiser rows with contradictory jar/pack descriptions remain blocked before economics.
- Bulky laptop-desk candidate remains rejected for the first pilot rather than being retained to enlarge the matrix.
- Southern Pet rows remain permission-required/HOLD even though public product and stock evidence exists.
- OXO organiser candidates may have cleaner identity evidence but remain HOLD/AMBER where authorised wholesale/economics/channel evidence is incomplete.

## Connector wording boundary
`CONNECTED ≠ SYNTHETIC CONTRACT VERIFIED ≠ REAL SYNC VERIFIED ≠ SKU ELIGIBLE ≠ PUBLISHED`.

Synthetic connector tests may prove fail-closed handling. They do not prove real SKU eligibility, production-safe sync or publication authority.

## Headless / Content360 consequence
Contradictory commerce evidence blocks:
- Product/Offer schema that asserts current transactional truth;
- Shop Now CTAs;
- current stock/price/delivery promotional snippets;
- paid product acquisition;
- Content360 product-specific transactional amplification.

Editorial content that does not depend on the disputed claim may remain usable.

## Current commercial state
**0 eBay-ready SKUs / PILOT NOT READY / PUBLICATION HOLD.**

No supplier contact, account mutation, purchase, listing, paid campaign or production write is authorized by this gate.
