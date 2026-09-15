# PORTFOLIO TASK LEDGER

Status: ACTIVE coordination index
Owner: Portfolio Overseer

This ledger coordinates claims only. It is **not** a scheduler, queue runtime, authority source, mission ledger, persistence service, Green system or PRS system. Repository/runtime/CI evidence outranks it.

States: `PENDING -> CLAIMED -> ACTIVE -> VERIFYING -> VERIFIED`; holding/terminal: `BLOCKED | BLOCKED_STABLE | SUPERSEDED | REJECTED`. Changed code head invalidates predecessor verification unless evidence explicitly covers the successor. No task self-promotes authority, Green, security or PRS.

## Executor ownership
- `SCHED-00-AGENTOS` — AgentOS Level 2.
- `SCHED-15-COMMERCE` — GlobalShopCo / Headless / Shopify-eBay / MyPrimeDelivery.
- `SCHED-30-REPLENISH` — coordination only; no competing implementation.
- `SCHED-40-ASSURANCE` — Jess + Michael / PRS assurance.
- `SCHED-45-VENTURES` — Lane-C/Ventures only where latest owner instruction permits and no exact task is already claimed.
- `WORK-PORTFOLIO` / `PROJECT-CHAT:<name>` — owner/manual execution.

## Reconciliation checkpoint — 2026-09-16 01:30 Brisbane
Changed evidence only: AgentOS PR #112 advanced from ledger predecessor `a7736d3747008f25f57290adbe37271447519303` to exact `832847fc613c1673379f065e49e093cdcc62d239`. PR remains OPEN/DRAFT/UNMERGED. Exact-head checks are completed SUCCESS (`wake` job `104372184304`; `test` jobs `104372184211`, `104372170032`). Therefore A-AG-08 remains ACTIVE with current exact-head functional CI evidence only; predecessor verification is invalidated except where successor evidence explicitly covers it, and no Green/security/authority/PRS promotion is claimed. AgentOS #104 remains BLOCKED_STABLE on SG-08 and SG-01/02; PRS must not recertify unchanged #104. Other durable rows remain unchanged and ready fall-through is preserved.

## Current ledger

| Task | Project | Priority | State | Owner | Exact anchor / dependency | Acceptance boundary / next transition |
|---|---|---:|---|---|---|---|
| A-AG-01 | AgentOS | P0 | BLOCKED_STABLE | SCHED-00-AGENTOS | `AgentOS#104@4c8bcc3bc2ad2041b0a1871d3004c1db23f3c091`; SG-08 | One existing ownership primitive continuously through verify→side effect/prepared recovery→durable success→release. Reopen only on changed candidate/evidence. |
| A-AG-02 | AgentOS | P0 | BLOCKED_STABLE | SCHED-00-AGENTOS | `#104@4c8bcc3...`; SG-01/02 | Authenticated actor + canonical grant source not wired end-to-end. No invented identity/grant registry. |
| A-AG-03 | AgentOS | P0 | PENDING | SCHED-00-AGENTOS | changed A-AG-01 candidate | 2–5 ownership/crash/replay/result-write/correlation negatives; exact-head Ubuntu+Windows CI; no new persistence/control plane. |
| A-AG-04 | AgentOS | P0 | BLOCKED_STABLE | SCHED-00-AGENTOS | repaired #104 + admission + Jess/Michael + PRS + owner physical authority | Physical Windows install/scheduler acceptance is owner-gated; no simulated evidence. |
| A-AG-05 | AgentOS | P0 | ACTIVE | SCHED-00-AGENTOS | existing #104 authority-receipt lineage | Preserve exact source-backed authority evidence/correlation; do not duplicate A-AG-01/02. |
| A-AG-06 | AgentOS | P0 | PENDING | SCHED-00-AGENTOS | after A-AG-01 repair | Recovery-state/authority-generation cross-bind; stale/mismatched generations fail closed; exact-head Ubuntu+Windows CI. |
| A-AG-07 | AgentOS | P0 | PENDING | SCHED-00-AGENTOS | after A-AG-01 repair | Authority revocation at durable-success linearization; false success denied. |
| A-AG-08 | AgentOS | P0 | ACTIVE | SCHED-00-AGENTOS | `AgentOS#112@832847fc613c1673379f065e49e093cdcc62d239`; exact-head checks SUCCESS | Runtime-shell eligibility/capability-contract consolidation. Next: inventory only genuinely uncovered evaluator/alias entry points; implement 2–5 homogeneous denial/normalization cases if gaps remain; rerun exact-head CI; keep #104 hot path untouched. |
| A-PRS-01 | PRS | P0 | VERIFIED | SCHED-40-ASSURANCE | historical `PRS#17@49fe1f8bca3ddae271d85e0f4767173060267222` | Historical false-GREEN baseline only. |
| A-PRS-02 | PRS | P0 | BLOCKED_STABLE | SCHED-40-ASSURANCE | unchanged `AgentOS#104@4c8bcc3...` | Reopen only on changed AgentOS mutation candidate. |
| A-PRS-03 | PRS | P0 | BLOCKED_STABLE | SCHED-40-ASSURANCE | `PRS#24@3039c886bdcff911f7c6dcc3e086368058e57fb6` + future repaired AgentOS head | Completion-grade PRS requires identical-head Jess functional PASS + Michael security PASS + owner/runtime gates. |
| A-PRS-04 | PRS | P0 | PENDING | SCHED-40-ASSURANCE | `PRS#24@3039c886...`; #49 handoff `5677299519` | Evidence-bundle substitution/mix-and-match + whole-bundle replay negatives; fixtures only. |
| B-GSC-01 | GlobalShopCo | P1 | ACTIVE | SCHED-15-COMMERCE | `#29@15fa99eb4c4b1f96127f6f51c412cbffc94e45e2`; `#30@80c82475b98663d677885e8b4d222ae2cedb8555` | Authenticated trade evidence only; missing material field => HOLD/UNKNOWN. |
| B-GSC-02 | GlobalShopCo | P1 | PENDING | SCHED-15-COMMERCE | evidence-complete B-GSC-01 row | Delivered-margin calculation only after evidence completeness. |
| B-GSC-03 | GlobalShopCo | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | current truth `0 eBay-ready SKUs` | Reopen only on exact evidence-complete variant. |
| B-GSC-04 | GlobalShopCo | P1 | PENDING | SCHED-15-COMMERCE | authenticated source routes only | 2–5 compact/light AU-stock candidates; capture identity/provenance/freight/permission/stock/returns or HOLD. |
| B-HDL-01 | GlobalShopCo-Headless | P1 | VERIFIED | SCHED-15-COMMERCE | `#1@708d32207e1e01bcbf8f9052698ffb29e98a8270`; run `34951837218` SUCCESS | Configured Shopify authority; bounded non-production only. |
| B-HDL-02 | GlobalShopCo-Headless | P1 | VERIFIED | SCHED-15-COMMERCE | same exact head/run | Malformed checkout authority + canonical projection denials verified; zero network on denied inputs. |
| B-HDL-03 | GlobalShopCo-Headless | P1 | PENDING | SCHED-15-COMMERCE | `#1@708d322...` | 2–5 variant mismatch/stale availability/duplicate-cart contradictions; fail closed before network; exact-head CI. |
| B-HDL-04 | GlobalShopCo-Headless | P1 | PENDING | SCHED-15-COMMERCE | after B-HDL-03 | 2–5 stale variant token/product-variant/cart-to-checkout correlation negatives; fixtures/no network. |
| B-HDL-05 | GlobalShopCo-Headless | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | owner-authorized dev-store/browser environment | Real browser acceptance owner-gated. |
| B-EBAY-01 | shopify_ebay | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | main `c68883f24fb3711fce567a35b1a80db74933b82a` | No evidenced canonical upstream replay persistence owner; no new ledger permitted. |
| B-EBAY-02 | shopify_ebay | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | B-EBAY-01 | Restart replay durability waits for canonical upstream owner. |
| B-EBAY-03 | shopify_ebay | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | GlobalShopCo evidence-complete SKU | Current truth zero eligible SKUs. |
| B-EBAY-04 | shopify_ebay | P1 | PENDING | SCHED-15-COMMERCE | existing mapper lineage | 2–5 uncovered malformed-ID/variant mismatch/conflicting hash/duplicate-event fixtures; repo tests; no live API/publication/persistence. |
| B-MPD-01 | MyPrimeDelivery | P1 | ACTIVE | SCHED-15-COMMERCE | research `61feceb46de539948374deec86b3fe7578cf8014`; fixture `a38684c10541115f55f1d5612b72d669dced99f0`; merge base `3635c903214b06464e28674d5a6403f8539b8c1e` | Compatibility map before presentation integration; no stale overwrite/merge/rebase. |
| B-MPD-02 | MyPrimeDelivery | P1 | PENDING | SCHED-15-COMMERCE | authorized coherent observations only | Current live `QUALIFIED=0`; public/editorial pages are not Prime/rank/deal authority. |
| B-MPD-03 | MyPrimeDelivery | P1 | VERIFIED | SCHED-15-COMMERCE | research `61feceb...` | Synthetic coherence baseline only. |
| B-MPD-04 | MyPrimeDelivery | P1 | PENDING | SCHED-15-COMMERCE | B-MPD-01 | Compatible non-production presentation adapter; HOLD/UNKNOWN cannot emit monetized/live CTA. |
| B-MPD-05 | MyPrimeDelivery | P1 | PENDING | SCHED-15-COMMERCE | existing validator lineage | 2–5 freshness/identity/outbound contradiction fixtures. |
| C-AFF-01 | Affiliate-Websites Master/AU/UK/US | P1 | ACTIVE | PROJECT-CHAT:Affiliate-Websites / WORK-PORTFOLIO | current Master/AU/UK/US seams | Preserve country compliance/disclosure/UNKNOWN CTA HOLD; do not compete while ACTIVE. |
| C-GK-01 | GhostKitchen | P1 | BLOCKED_STABLE | SCHED-45-VENTURES | `GhostKitchen#32@766f69b92fe3ea5a98aca0cd611727cdf61c879d`; handoff `GhostKitchen#31 comment 5677347199` | Reopen only on real workflow/evidence-path repair or materially changed lineage. |
| C-FR-01 | Franchise | P1 | PENDING | PROJECT-CHAT:Franchise / WORK-PORTFOLIO | GhostKitchen template evidence | Gate-3 reusable franchise acceptance; synthetic/non-production. |
| C-GEM-01 | GemVerse | P2 | PENDING | PROJECT-CHAT:GemVerse / WORK-PORTFOLIO | current canon/recovery lineage | Exact recovery identity; competing/ambiguous state fails closed. |
| C-C360-01 | content360 | P1 | ACTIVE | PROJECT-CHAT:Content360 / WORK-PORTFOLIO | current PR lineage + Marketing provenance | Do not compete while ACTIVE; no live PUBLISH/SCHEDULE/network authority. |
| C-CF-01 | Commercial Frontend | P2 | PENDING | PROJECT-CHAT:Commercial Frontend / WORK-PORTFOLIO | Overseer commercial-frontend evidence | Evidence packets/bounded correction only; demand/WTP remain hypotheses. |
| C-MKT-01 | Marketing | P2 | ACTIVE | PROJECT-CHAT:Marketing / WORK-PORTFOLIO | canonical capability/pricing evidence | Do not compete while ACTIVE; draft/research only. |
| C-CAR-01 | Car Rental | P2 | BLOCKED_STABLE | PROJECT-CHAT:Car Rental / WORK-PORTFOLIO | no canonical repo visible | Research-only; no substitute repo/purchase/contact/finance/listing. |
| OVR-01 | Overseer | P0 | ACTIVE | SCHED-30-REPLENISH | this ledger + project batches + #49 | Fresh-fetch before shared writes; coordination only. |

## Ready ordering
1. AgentOS: #104 blockers stay stable; execute independent #112 A-AG-08 and replay/correlation gaps without competing with exact active mutation work.
2. PRS: do not recertify unchanged #104; A-PRS-04 is independent fixture work.
3. Commerce: Headless B-HDL-03 then B-HDL-04; eBay B-EBAY-04; MyPrime B-MPD-01/B-MPD-05; GSC only authenticated evidence routes.
4. Lane-C/manual state remains coordinated but is not consumed by this replenisher merely because visible.

## Security / authority
Security is cross-cutting. S0/S1 read-only/synthetic work; S2 non-production branch/tests/docs requires scoped grant and Green where promotion applies. Production/publication/contact/spend/credentials/security-policy/physical-host actions remain owner-only. Functional success never upgrades security, Green or PRS status.

**NO MODEL DECIDES ITS OWN AUTHORITY.** No merge/approve/ready/rebase/deploy, credentials/security-policy mutation, production writes/autonomy, purchases/spend, supplier/seller contact, live listing/publication/campaign activation, unrestricted elevation or invented physical Windows evidence without explicit owner authorization. No overall GREEN is implied.