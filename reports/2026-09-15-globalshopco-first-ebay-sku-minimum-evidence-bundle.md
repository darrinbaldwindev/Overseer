# GlobalShopCo — First eBay SKU Minimum Evidence Bundle

**Date:** 2026-09-15 AEST  
**Task:** M-B022  
**Status:** COMPLETE / READ-ONLY QUALIFICATION CONTRACT

## Objective
Define the smallest evidence bundle that can move one research candidate from HOLD toward eBay eligibility without contacting a supplier, purchasing stock, changing an account or publishing a listing.

## Required bundle
A candidate cannot become `EBAY-ELIGIBLE` unless all required fields are current and bound to the exact SKU/variant.

### 1. Exact identity
- supplier SKU/variant;
- exact title/variant attributes;
- GTIN/MPN/brand where applicable;
- evidence that the eBay comparison is the same product/variant, not a near match.

### 2. Supplier commercial evidence
From an already-authorised/authenticated source where required:
- current buy cost;
- GST/tax basis;
- current stock/availability semantics;
- marketplace/resale permission;
- blind-shipping/packing/seller-identity compatibility where dropshipped.

Public retail pages are not a substitute for authenticated wholesale/reseller permission.

### 3. Freight evidence
- actual or representative destination basis appropriate to first market;
- dead weight;
- dimensions/cubic basis where relevant;
- surcharge/remote-area conditions where material;
- free-delivery assumption translated into seller-paid landed cost.

### 4. eBay channel evidence
- current exact-product market comps;
- actual seller account plan/category fee basis;
- applicable final-value/integration/payment cost basis;
- listing/category constraints materially affecting saleability.

### 5. Conservative contribution calculation
Use current delivered sell-price evidence and include at least:
- acquisition cost;
- freight;
- eBay/channel fees;
- operating/returns reserve;
- GST/accounting basis as applicable;
- any known mandatory integration allocation.

Do not qualify a SKU whose viability depends on an UNKNOWN freight/fee/permission value.

### 6. Freshness + contradiction check
Every material source needs observed date/freshness. Fresher contradictory evidence overrides older favourable evidence.

## Minimum receipt
A qualification record should retain:
- exact SKU;
- evidence source identifiers/pointers;
- observed timestamps;
- calculated landed economics;
- UNKNOWN list;
- contradiction list;
- resulting status;
- reviewer/worker identity if applicable;
- no-publication-authority flag.

## Promotion rule
`EBAY-ELIGIBLE` means the research/evidence gate has cleared. It does **not** mean `PUBLISHED`, `LIVE`, `ORDERABLE`, supplier-contact authorised, or production sync enabled.

Recommended state chain:
`RESEARCH CANDIDATE → QUALIFIED FOR OWNED SITE (if applicable) → EBAY-ELIGIBLE → owner-authorised publication process → PUBLISHED`

## Current candidates
No current OXO or CARLA row has the full bundle. **0 eBay-ready SKUs remains correct.**

## Fastest unlock
The highest-value missing evidence is not more public product discovery. It is authenticated/current supplier cost + freight + permission plus actual eBay account/category fee evidence for an exact already-promising candidate.

## Disposition
**M-B022 COMPLETE. The next SKU promotion can now be deterministic and evidence-minimal without weakening the gate.**