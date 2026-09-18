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


## Current manual checkpoint — 2026-09-18, #123 CI follow-up

WORK-PORTFOLIO completed a bounded test-only follow-up on existing AgentOS #123, head `b993632ef44d26c91cab08190968205a6316106d`, base #104 `607f2683b7d3b234fc6ffa70e2a7d42e31499c3a`. Source-backed completed Work result at #123 predecessor `e84f49d...` is bounded recovery-ownership hardening, not SG-08 closure. Fresh evidence found PR run `35334905122` failed with 22 Ubuntu cancellations despite push run `35334901641` SUCCESS; failed evidence retained. Two-call duplicate test gates now bind intended winner arrival explicitly. Local writer tests 28 PASS / zero failure/cancellation. Manual CI follow-up VERIFIED and claim released; independent functional/security certification remains PENDING. New exact-head push `35335982121` and PR `35335986661` both SUCCESS on Ubuntu Node22 and Windows Node26, including full-suite and dependency-audit steps; do not infer overall GREEN from CI.

SCHED-00 retains production ownership-fence/authority implementation; SCHED-40 retains independent assurance. Manual test-only claim source: Overseer #49 comment `5728850621`. PRS #17 intake comment `5728866719` binds changed #123 target and identifies historical workflow pins. Completion-grade PRS remains INELIGIBLE/NOT RUN until independent Jess+Michael PASS on identical current SHA and all required owner/runtime gates. SG08/SG01/02 and physical/runtime gates remain blocked; mutation disabled. No competing subsystem or protected action.

Live PRS anchors: #17 `5616ab602ca569b9a47e9cf95ad606bbb9cfa7b4`; #24 `ece88ac707cdb8c73bf23983771fcae849857fa1`; #26 `79b916f99eaea772da7786913867961a3bb714d0`. AgentOS #122 `a6d18e779c5ec112908fa1c1c0e2d863b5d5f04c` is a separate installer candidate; no assurance transfer between branches.

## Historical reconciliation checkpoint — 2026-09-18 12:32 Brisbane
AgentOS PR #104 advanced two commits from `ffe6954a4879606804fc512bf000ff3ea7e46fec` to exact `607f2683b7d3b234fc6ffa70e2a7d42e31499c3a`, remains OPEN/DRAFT/UNMERGED. Compare evidence shows a bounded installer fail-closed change in `scripts/install-local.mjs` plus regression coverage in `tests/install-local.test.mjs`: a pre-existing config with missing canonical state now raises `LOCAL_INSTALL_INCOMPLETE` and preserves existing files rather than silently synthesizing state. Exact-head AgentOS Tests run `35297751947` completed SUCCESS. This is useful functional/install recovery movement only. Exact-head identity changed, so predecessor Green/security/PRS assurance does not transfer. A-AG-01 remains BLOCKED on SG-08; A-AG-02 remains BLOCKED on SG-01/02; A-AG-03 remains VERIFYING with clean exact-head functional CI; A-PRS-02 remains PENDING fresh identical-head Jess + Michael challenge. Physical Windows acceptance remains owner-gated. AgentOS #112 remains `33eca1d257179a873a8aca2eea1a4e5e994415a0`; PRS #24 remains `3039c886bdcff911f7c6dcc3e086368058e57fb6`. Commerce/Lane-C states remain unchanged absent fresh owning-executor evidence.

## Current ledger

| Task | Project | Priority | State | Owner | Exact anchor / dependency | Acceptance boundary / next transition |
|---|---|---:|---|---|---|---|
| A-AG-01 | AgentOS | P0 | BLOCKED | SCHED-00-AGENTOS | `AgentOS#123@b993632ef44d26c91cab08190968205a6316106d` on #104 `607f2683...`; SG-08 | Fresh identical-head continuous-ownership evidence required; one existing ownership primitive through verify→side effect/prepared recovery→durable success→release. No predecessor assurance transfer. |
| A-AG-02 | AgentOS | P0 | BLOCKED | SCHED-00-AGENTOS | `#104@607f2683...`; SG-01/02 | Authenticated actor + canonical grant source not evidenced end-to-end. No invented identity/grant registry. |
| A-AG-03 | AgentOS | P0 | VERIFYING | SCHED-00-AGENTOS | `#104@607f2683...`; run `35297751947` SUCCESS | Exact-head functional CI clean. Installer now fails closed on config-present/state-missing partial install. Inventory remaining replay/result/correlation and install/recovery negatives without widening authority. Promotion still requires applicable Green/security/PRS evidence. |
| A-AG-04 | AgentOS | P0 | BLOCKED_STABLE | SCHED-00-AGENTOS | repaired #104 + admission + Jess/Michael + PRS + owner physical authority | Physical Windows install/scheduler acceptance is owner-gated; no simulated evidence. |
| A-AG-05 | AgentOS | P0 | ACTIVE | SCHED-00-AGENTOS | existing #104 authority-receipt lineage | Preserve exact source-backed authority evidence/correlation; do not duplicate A-AG-01/02. |
| A-AG-06 | AgentOS | P0 | PENDING | SCHED-00-AGENTOS | after A-AG-01 repair | Recovery-state/authority-generation cross-bind; stale/mismatched or cross-spliced generations fail closed; exact-head Ubuntu+Windows CI. |
| A-AG-07 | AgentOS | P0 | PENDING | SCHED-00-AGENTOS | after A-AG-01 repair | Authority revocation at durable-success linearization; false success denied. |
| A-AG-08 | AgentOS | P0 | ACTIVE | SCHED-00-AGENTOS | `AgentOS#112@33eca1d257179a873a8aca2eea1a4e5e994415a0` | Runtime-shell eligibility/capability-contract consolidation. Independent lineage; do not duplicate or touch #104 hot path. |
| A-PRS-01 | PRS | P0 | VERIFIED | SCHED-40-ASSURANCE | historical `PRS#17@49fe1f8bca3ddae271d85e0f4767173060267222` | Historical false-GREEN baseline only. |
| A-PRS-02 | PRS | P0 | PENDING | SCHED-40-ASSURANCE | `AgentOS#123@b993632ef44d26c91cab08190968205a6316106d` | Fresh identical-head Jess + Michael challenge required; never certify worker self-report. |
| A-PRS-03 | PRS | P0 | BLOCKED | SCHED-40-ASSURANCE | `PRS#24@ece88ac707cdb8c73bf23983771fcae849857fa1` + stabilized AgentOS head | Completion-grade PRS requires identical-head Jess functional PASS + Michael security PASS + owner/runtime gates. |
| A-PRS-04 | PRS | P0 | PENDING | SCHED-40-ASSURANCE | `PRS#24@ece88ac7...` | Evidence-bundle substitution/mix-and-match plus prepared-recovery envelope splice; fixtures only; no physical execution. |
| B-GSC-01 | GlobalShopCo | P1 | ACTIVE | SCHED-15-COMMERCE | authenticated trade evidence lineage | Authenticated trade evidence only; missing material field => HOLD/UNKNOWN. |
| B-GSC-02 | GlobalShopCo | P1 | PENDING | SCHED-15-COMMERCE | evidence-complete B-GSC-01 row | Delivered-margin calculation only after evidence completeness. |
| B-GSC-03 | GlobalShopCo | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | current durable truth `0 eBay-ready SKUs` | Reopen only on exact evidence-complete variant. |
| B-GSC-04 | GlobalShopCo | P1 | PENDING | SCHED-15-COMMERCE | authenticated source routes only | 2–5 compact/light AU-stock candidates; capture identity/provenance/freight/permission/stock/returns or HOLD. |
| B-HDL-01 | GlobalShopCo-Headless | P1 | VERIFIED | SCHED-15-COMMERCE | bounded non-production checkout-authority lineage | Configured Shopify authority; bounded non-production only. |
| B-HDL-02 | GlobalShopCo-Headless | P1 | VERIFIED | SCHED-15-COMMERCE | same bounded lineage | Malformed checkout authority + canonical projection denials verified; zero network on denied inputs. |
| B-HDL-03 | GlobalShopCo-Headless | P1 | PENDING | SCHED-15-COMMERCE | current non-production lineage | 2–5 variant mismatch/stale availability/duplicate-cart contradictions; fail closed before network; exact-head CI. |
| B-HDL-04 | GlobalShopCo-Headless | P1 | PENDING | SCHED-15-COMMERCE | after B-HDL-03 | 2–5 stale variant token/product-variant/cart-to-checkout correlation negatives; fixtures/no network. |
| B-HDL-05 | GlobalShopCo-Headless | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | owner-authorized dev-store/browser environment | Real browser acceptance owner-gated. |
| B-EBAY-01 | shopify_ebay | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | canonical upstream replay owner absent | No evidenced canonical upstream replay persistence owner; no new ledger permitted. |
| B-EBAY-02 | shopify_ebay | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | B-EBAY-01 | Restart replay durability waits for canonical upstream owner. |
| B-EBAY-03 | shopify_ebay | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | GlobalShopCo evidence-complete SKU | Current durable truth zero eligible SKUs. |
| B-EBAY-04 | shopify_ebay | P1 | PENDING | SCHED-15-COMMERCE | existing mapper lineage | 2–5 uncovered malformed-ID/variant mismatch/conflicting hash/duplicate-event fixtures; repo tests; no live API/publication/persistence. |
| B-MPD-01 | MyPrimeDelivery | P1 | ACTIVE | SCHED-15-COMMERCE | existing divergent research/fixture lineages | Compatibility map before presentation integration; no stale overwrite/merge/rebase. |
| B-MPD-02 | MyPrimeDelivery | P1 | PENDING | SCHED-15-COMMERCE | authorized coherent observations only | Public/editorial pages are not Prime/rank/deal authority; UNKNOWN remains HOLD. |
| B-MPD-03 | MyPrimeDelivery | P1 | VERIFIED | SCHED-15-COMMERCE | synthetic coherence baseline | Synthetic coherence baseline only. |
| B-MPD-04 | MyPrimeDelivery | P1 | PENDING | SCHED-15-COMMERCE | B-MPD-01 | Compatible non-production presentation adapter; HOLD/UNKNOWN cannot emit monetized/live CTA. |
| B-MPD-05 | MyPrimeDelivery | P1 | PENDING | SCHED-15-COMMERCE | existing validator lineage | 2–5 freshness/identity/outbound contradiction fixtures. |
| C-AFF-01 | Affiliate-Websites Master/AU/UK/US | P1 | ACTIVE | PROJECT-CHAT:Affiliate-Websites / WORK-PORTFOLIO | current Master/AU/UK/US seams | Preserve country compliance/disclosure/UNKNOWN CTA HOLD; do not compete while ACTIVE. |
| C-GK-01 | GhostKitchen | P1 | BLOCKED_STABLE | SCHED-45-VENTURES | current durable blocker | Reopen only on real workflow/evidence-path repair or materially changed lineage. |
| C-FR-01 | Franchise | P1 | PENDING | PROJECT-CHAT:Franchise / WORK-PORTFOLIO | GhostKitchen template evidence | Gate-3 reusable franchise acceptance; synthetic/non-production; no competing lineage. |
| C-GEM-01 | GemVerse | P2 | PENDING | PROJECT-CHAT:GemVerse / WORK-PORTFOLIO | current canon/recovery lineage | Exact recovery identity; competing/ambiguous state fails closed. |
| C-C360-01 | content360 | P1 | ACTIVE | PROJECT-CHAT:Content360 / WORK-PORTFOLIO | current PR lineage + Marketing provenance | Do not compete while ACTIVE; no live PUBLISH/SCHEDULE/network authority. |
| C-CF-01 | Commercial Frontend | P2 | PENDING | PROJECT-CHAT:Commercial Frontend / WORK-PORTFOLIO | residual ServiceM8↔Xero evidence gate | Prove residual exception, frequency, minutes/case, consequence, approval owner, WTP and exact scopes; otherwise HOLD. No customer contact. |
| C-MKT-01 | Marketing | P2 | ACTIVE | PROJECT-CHAT:Marketing / WORK-PORTFOLIO | canonical capability/pricing evidence | Do not compete while ACTIVE; draft/research only. |
| C-CAR-01 | Car Rental | P2 | BLOCKED_STABLE | PROJECT-CHAT:Car Rental / WORK-PORTFOLIO | no canonical repo visible | Research-only; no substitute repo/purchase/contact/finance/listing. |
| OVR-01 | Overseer | P0 | ACTIVE | SCHED-30-REPLENISH | this ledger + project batches + #49 | Fresh-fetch before shared writes; coordination only. |

## Ready ordering
1. **AgentOS #123 continuous fence:** SCHED-00 owning lane; current `b993632ef44d26c91cab08190968205a6316106d`; recorder displacement and durable-receipt/pre-release successor races; existing primitive only, mutation disabled.
2. **Jess functional challenge:** SCHED-40; identical #123 head, bounded positive path plus prepared recovery, metadata loss, replay/crash/result-write and successor negatives; no inherited PASS.
3. **Michael security challenge:** SCHED-40; identical #123 head, continuous ownership and real canonical authority provenance; no synthetic identity/grant.
4. **PRS conditional refresh:** existing immutable probe lineage; historical workflow pins cannot certify changed #123/#122; completion-grade run only after independent identical-head PASS plus applicable owner/runtime gates.
5. **GlobalShopCo supplier evidence closure:** existing shortlist, authenticated cost/freight/permission/stock/returns evidence; absent input => HOLD, no supplier contact or further horizontal expansion.
6. **Headless/shopify_ebay/MyPrimeDelivery:** existing owning commerce lane; exact candidate CI and uncovered identity/freshness/correlation negatives; compatibility map before UI port, no new persistence.
7. **Affiliate/GhostKitchen/Franchise/GemVerse:** next unclaimed repository-backed non-production acceptance/economics/canon slice; fresh scan and preserve active project ownership.
8. **Content360/Marketing/Car Rental:** existing provider contract/provenance/research lane; no live publication, credentials, contact or spend.

## Security / authority
Security is cross-cutting. S0/S1 read-only/synthetic work; S2 non-production branch/tests/docs requires scoped grant and Green where promotion applies. Production/publication/contact/spend/credentials/security-policy/physical-host actions remain owner-only. Functional success never upgrades security, Green or PRS status.

**NO MODEL DECIDES ITS OWN AUTHORITY.** No merge/approve/ready/rebase/deploy, credentials/security-policy mutation, production writes/autonomy, purchases/spend, supplier/seller contact, live listing/publication/campaign activation, unrestricted elevation or invented physical Windows evidence without explicit owner authorization. No overall GREEN is implied.