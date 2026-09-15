# Commercial Frontend — Ecommerce Direct-Evidence Wedge Comparison Scorecard

Date: 2026-09-16 (Brisbane)
Status: VERIFIED AS DIRECT-EVIDENCE INTERPRETATION CONTRACT / NO WINNER

## Purpose
Compare only exception classes actually observed/reported by real Ecommerce operators. Synthetic EC/SF fixtures prove safety semantics, not commercial frequency or demand.

## Candidate families
These are capture buckets, not ranked recommendations:
- E1 supplier stock/availability mismatch affecting a Shopify customer promise;
- E2 fulfilment/tracking/package identity exception requiring supplier + Shopify reconciliation;
- E3 order hold/release or fulfilment-state conflict across supplier/app/Shopify;
- E4 returns/refund/rework exception crossing Shopify + supplier + finance/accounting;
- E5 another participant-described cross-system exception, recorded verbatim and assessed for incumbent overlap before inclusion.

Generic Shopify automation, tagging or workflow-builder tasks are not sufficient wedges because incumbent automation already covers substantial native workflow territory.

## Required direct fields per exception family
- independent participant count describing materially similar case;
- affected orders/week or month;
- exception rate if participant can support it;
- minutes/manual case;
- number and identity of systems crossed;
- manual handoffs;
- customer-promise consequence;
- refund/rework/customer-contact consequence where directly evidenced;
- approval owner and required approval boundary;
- exact read feasibility;
- prospective write/action scope;
- measurable resolved outcome;
- trial intent exact wording;
- stated WTP exact amount/wording or UNKNOWN;
- acquisition/reach signal if directly evidenced.

## Evidence labels
Each cell must be one of:
- `OBSERVED`
- `PARTICIPANT_REPORTED`
- `DERIVED_FROM_DIRECT_INPUTS`
- `PLATFORM_EVIDENCE` (integration/incumbent boundary only)
- `PORTFOLIO_EVIDENCE` (fixture/safety semantics only)
- `UNKNOWN`

`PLATFORM_EVIDENCE` and `PORTFOLIO_EVIDENCE` cannot supply frequency, burden, trial intent or WTP.

## Comparison table
| Dimension | E1 | E2 | E3 | E4 | E5 |
|---|---|---|---|---|---|
| independent materially similar participants | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| affected orders / period | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| minutes / actionable case | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| consequence evidence | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| systems crossed | PARTIAL platform evidence | PARTIAL platform evidence | PARTIAL platform evidence | PARTIAL platform evidence | UNKNOWN |
| incumbent overlap | PARTIAL | PARTIAL | PARTIAL | PARTIAL | UNKNOWN |
| exact read feasibility | PARTIAL | PARTIAL | PARTIAL | PARTIAL | UNKNOWN |
| approval boundary | HYPOTHESIS | HYPOTHESIS | HYPOTHESIS | HYPOTHESIS | UNKNOWN |
| measurable outcome | HYPOTHESIS | HYPOTHESIS | HYPOTHESIS | HYPOTHESIS | UNKNOWN |
| trial intent | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| WTP | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |

Current commercial winner: `NONE — DIRECT EVIDENCE REQUIRED`.

## Selection rule
No weighted score is computed while controlling fields are UNKNOWN. A family becomes prototype-eligible only after at least 3 independent materially similar direct cases/participants establish repeated pain plus feasible reads, a clear approval boundary and measurable outcome. If multiple families qualify, compare them descriptively using the same direct fields; do not allow synthetic fixture frequency to break ties.

## Fail-closed commercial rules
1. Supplier/app documentation proves mechanics, not merchant pain.
2. GlobalShopCo fixtures are portfolio evidence, not independent customer demand.
3. Shopify-synchronized supplier state cannot be presented as direct supplier evidence.
4. Missing WTP remains UNKNOWN; trial interest is not silently converted to WTP.
5. A technically easy integration does not imply a commercially valuable wedge.
6. No production frontend, connector or customer mutation follows from this scorecard.

## Current disposition
Direct demand remains UNKNOWN. This scorecard is ready to consume records from `reports/2026-09-14-commercial-frontend-ecommerce-direct-validation-packet.md` when real participant evidence becomes available.