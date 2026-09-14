# GlobalShopCo / eBay — Southern Pet Plan-Aware Break-Even Gate

**Date:** 14 September 2026 (Brisbane)  
**Status:** INTERNAL COMMERCIAL SCREEN / 0 EBAY-READY SKUS / NO PUBLICATION AUTHORITY

## Purpose
Upgrade the existing five-SKU Southern Pet economics screen for eBay Australia's May 2026 fee structure without inventing wholesale cost, marketplace permission or account-plan status.

## Canonical candidate set
- `GDAG2600` GiGwi Crunchy Neck Plush Duck Small — 0.4 kg — stock evidence exists — permission REQUIRED.
- `GDAG2522` GiGwi Duraspikes Dino T-Rex — 0.49 kg — permission REQUIRED.
- `GDAG2515` GiGwi Duraspikes Elephant — 0.49 kg — permission REQUIRED.
- `GDAG2505` GiGwi Duraspikes Rabbit — 0.49 kg — permission REQUIRED.
- `GDAG2610` GiGwi Crunchy Neck Plush Duck Large — 0.9 kg — permission REQUIRED.

All authorised trade/wholesale prices remain UNKNOWN. Southern Pet's published marketplace policy requires prior written approval for eBay/other marketplaces, therefore none is activation-eligible.

## Current eBay AU plan reality
Current eBay AU documentation materially changes the economics gate:
- qualifying Australia-based non-Pro sellers with <= A$25,000 rolling 12-month sales can sell without transaction fees, but generally must use eBay shipping labels and do not receive the full Pro integration feature set;
- Pro Starter has no monthly fee and a 13.4% final value fee;
- Pro Basic costs A$27.45/month and advertises category-dependent 8.0–13.1% final value fees;
- eBay lists API and third-party integrations as a Pro Basic-or-higher feature.

Therefore Marketing must not calculate the Shopify→eBay production case from the free-seller fee regime. The exact GlobalShopCo eBay plan and exact category fee must be verified from the account before commercial approval.

## Screening assumptions inherited from the commercial lane
These are stress-test assumptions, not owner-approved final targets:
- target contribution reserve: 20% of delivered sale price;
- operating/returns reserve: 5%;
- free delivery to customer;
- no optional promoted-listing fee;
- monthly Pro/integration allocation excluded from the per-unit thresholds below and must be added before final approval;
- exact cubic-weight freight can override simple weight-band screens.

## Plan-aware combined acquisition + outbound-freight ceiling
Formula:
`max combined stock+freight = sale price × (1 - FVF - 20% contribution - 5% operating/returns reserve)`

At Pro Starter 13.4%, the ceiling is 61.6% of delivered sale price. At the previously used conservative Pro Basic upper-bound 13.1%, it is 61.9%. The difference is small; the larger unresolved variables remain trade cost, cubic freight, actual category fee, plan/monthly allocation and marketplace permission.

| SKU | Screen sale price | Pro Starter 13.4% max stock+freight | Pro Basic 13.1% max stock+freight | Current commercial interpretation |
|---|---:|---:|---:|---|
| GDAG2600 | A$20.99 | A$12.93 | A$12.99 | severe price pressure; likely fragile |
| GDAG2522 | A$29.95 | A$18.45 | A$18.54 | trade cost decisive |
| GDAG2515 | A$27.50 | A$16.94 | A$17.02 | trade cost decisive |
| GDAG2505 | A$30.75 | A$18.94 | A$19.03 | strongest current screen among evidenced mid-price rows |
| GDAG2610 | A$30.45 | A$18.76 | A$18.85 | 0.9 kg freight materially harder |

## Dropship-freight stress using published Southern Pet bands
Published examples are ex-GST and final cubic/destination treatment still controls. For a conservative indicative GST-inclusive screen:
- VIC/NSW capital 0–0.49 kg: A$7.60 ex GST ≈ A$8.36 incl GST.
- VIC/NSW capital 0.5–0.99 kg: A$9.35 ex GST ≈ A$10.29 incl GST.

Subtracting only those indicative freight amounts from the Pro Starter ceiling gives an approximate **maximum trade-cost screen**, not an approval threshold:

| SKU | Indicative freight used | Approx max trade cost before monthly/integration/packaging exceptions |
|---|---:|---:|
| GDAG2600 | A$8.36 | A$4.57 |
| GDAG2522 | A$8.36 | A$10.09 |
| GDAG2515 | A$8.36 | A$8.58 |
| GDAG2505 | A$8.36 | A$10.58 |
| GDAG2610 | A$10.29 | A$8.47 |

These ceilings demonstrate why a low retail price can kill a SKU even when stock and supplier fulfilment exist. They do **not** prove supplier economics because authenticated trade prices are unavailable and cubic freight can be higher.

## Decision gate per SKU
A SKU may move from HOLD to comparison-ready only when all of the following are evidenced:
1. written eBay marketplace permission;
2. eBay-compatible stock ownership/pre-purchase/fulfilment model;
3. seller identity, packing and buyer-data handling compatible with eBay rules;
4. authenticated trade cost + GST;
5. parcel/cubic freight for representative AU zones;
6. exact eBay plan/category fee and any Marketplace Connect/integration allocation;
7. return/warranty reserve treatment;
8. current exact market/eBay comparison evidence;
9. positive free-delivery contribution at the owner-approved minimum contribution target;
10. verified Shopify→eBay purchase/order/stock path before publication authority.

## Commercial conclusion
- `GDAG2600` should be treated as **high-risk / likely first cut** unless authenticated trade pricing is exceptionally low; the low-end public retail market leaves very little room after free-delivery freight.
- `GDAG2505`, `GDAG2522` and `GDAG2515` remain more useful quote-screen candidates.
- `GDAG2610` remains stress-sensitive because its 0.9 kg freight band consumes more of the contribution envelope.
- None is eBay-ready today.

## Owner-decision boundary
Supplier contact is still not authorised. Once no-contact evidence is exhausted, the smallest owner decision is whether to authorise controlled supplier/account evidence gathering for written marketplace permission and authenticated trade prices. Until then, do not broaden catalog marketing or imply availability/profitability.

**Production status:** NO LISTINGS / NO SUPPLIER CONTACT / NO PURCHASE / NO PAID ACQUISITION / NO CONNECTOR MUTATION / NO OVERALL GREEN.