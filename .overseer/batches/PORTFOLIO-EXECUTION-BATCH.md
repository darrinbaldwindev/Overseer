# Portfolio Execution Batch Manifest

**Purpose:** scheduled queue state for the owner-selected core projects only. Canonical procedure: `.overseer/doctrine/PORTFOLIO-BATCH-ENGINE.md`; project shaping: `.overseer/profiles/PROJECT-BATCH-PROFILES.md`; security: `.overseer/security/AGENTOS-SECURITY-GATE-MATRIX.md`. Current repository/runtime/CI evidence always outranks this file.

**Scheduled scope:** AgentOS, PRS, GlobalShopCo, GlobalShopCo-Headless, shopify_ebay, MyPrimeDelivery. All other portfolio projects are owner-manual unless the owner changes this scope.

**States:** `PENDING | ACTIVE | VERIFIED | BLOCKED | STALE | SPLIT_REQUIRED`.

**Core invariant:** **NO MODEL DECIDES ITS OWN AUTHORITY.** Functional, security and PRS state remain separate. No merge/approve/ready/rebase/deploy/credentials/security-policy changes/production writes/purchases/spend/supplier contact/live publication/physical owner-host action/production autonomy.

## Checkpoint reconciliation — 2026-09-15 10:32 Brisbane
- Owner explicitly narrowed recurring autonomous execution to the six projects above. Lane-C ventures and Shopify-to-Amazon are removed from scheduled replenishment; their durable repo state is not erased.
- **AgentOS:** PR #104 remains OPEN/DRAFT/UNMERGED at exact `4c8bcc3bc2ad2041b0a1871d3004c1db23f3c091`. Exact-head runs `34906732495` and `34906728091` are SUCCESS cross-platform. Head `4c8bcc3...` expands deterministic SG-08 false-success repair fixtures and still proves the defect: target mutation + durable success receipt can precede release-time ownership-loss detection. SG-08 remains BLOCKED. SG-01/02 authenticated actor/canonical grant binding remains BLOCKED. No overall GREEN.
- **PRS:** #17 `49fe1f8bca3ddae271d85e0f4767173060267222` remains historical immutable false-GREEN evidence, not certification of current AgentOS head. PR #24 `3039c886bdcff911f7c6dcc3e086368058e57fb6` has Validate repository run `34853865390` SUCCESS but its embedded AgentOS target is stale; exact-current-head completion assurance remains blocked pending SG-08 repair + unchanged-head Green.
- **GlobalShopCo:** #29 `15fa99eb4c4b1f96127f6f51c412cbffc94e45e2` and #30 `80c82475b98663d677885e8b4d222ae2cedb8555` remain OPEN/DRAFT research-only. #30 records no new authenticated supplier/app evidence. `0 eBay-ready SKUs` remains controlling; supplier cost/freight/permission/stock/returns evidence is the commercial blocker.
- **Headless:** bounded M3 secret-boundary exact head `4e66a67d3680bd59e3b4da923f9ef291aa6fa358`, run `34891752520` SUCCESS. No live checkout/deploy authority.
- **shopify_ebay:** prior exact `23b263ecd4e04667e6c95977f694c66cce4734e2/34885862149` SUCCESS. Fresh read-only persistence discovery found no durable replay/idempotency store in the adapter repository; `accept_once` receives caller-supplied seen IDs/hashes only. Discovery was recorded on the same bounded branch at `02087f3c1b6fa4c6b9406b7cd39698c52a72ab6a`; exact-head Fixture validation run `34913579897` SUCCESS. Restart-level durability is therefore BLOCKED until an existing upstream canonical store/caller is identified; do not invent local persistence.
- **MyPrimeDelivery:** research head `61feceb46de539948374deec86b3fe7578cf8014`, Fixture validation `34879834476` SUCCESS. Qualification funnel is coherent/fail-closed, including conflicting known ASIN denial. Research milestone is 100 distinct concepts but live `QUALIFIED=0`. WordPress fixture head `a38684c10541115f55f1d5612b72d669dced99f0` and research head are diverged (`61feceb...` is 101 commits ahead and 4 behind from that comparison), so stale overwrite prevention remains required.

# AGENTOS / PRS

### A-AG-01 — continuous project-file ownership fence
- status: BLOCKED
- anchor: `AgentOS#104@4c8bcc3bc2ad2041b0a1871d3004c1db23f3c091`
- objective: repair the existing single writer so one crash-releasing ownership primitive remains continuously valid through final verify -> publish/prepared recovery -> durable success receipt -> release.
- acceptance: replacement after publish/receipt, successor/three-writer, stale identity, TOCTOU, crash/replay and prepared-recovery stale-owner all fail before durable success.
- current evidence: deterministic exact-head fixtures reproduce false durable success before release detects successor displacement.
- next: minimal repair on existing writer seam only, then exact-head Ubuntu+Windows CI -> independent Green -> PRS. No second lock/ledger.
- security: SG-03/08/09/10/11/14/18/19; S2; overall promotion BLOCKED.

### A-AG-02 — authenticated actor + canonical grant binding
- status: BLOCKED
- anchor: current #104 admission composition seam.
- objective: bind only a real existing authenticated actor source and canonical grant resolver.
- acceptance: no caller self-identity/self-grant; absent/spoofed/mismatch/cross-project/replay denies admission/success.
- next: architecture discovery only until real source provenance exists. No duplicate authority registry.
- security: SG-01/02/03/04/09/10/11/18/19; S2.

### A-AG-03 — bounded current-head regression preservation
- status: VERIFIED_BOUNDED
- anchor: `4c8bcc3.../34906732495/34906728091`.
- scope: replay/correlation/provenance + SG-08 defect fixtures execute successfully cross-platform; this is not readiness.
- next: preserve while A-AG-01 is repaired.

### A-AG-04 — SG-08 repair fixture pack
- status: VERIFIED_AS_DEFECT_BASELINE / REPAIR_PENDING
- anchor: `4c8bcc3...`.
- verified: after-publish and release replacement fixtures expose target mutation + false durable success ordering.
- next: drive smallest existing-writer repair; rerun fixtures unchanged first.

### A-AG-05 — replay/freshness remainder
- status: SPLIT_REQUIRED
- objective: preserve first-write provenance and conflicting replay denial; freshness remains UNKNOWN/N/A unless canonical source exists.
- next: no new replay/persistence authority.

### A-AG-06 — physical Windows acceptance
- status: BLOCKED / OWNER_REQUIRED
- dependencies: SG-08 + SG-01/02 + exact-head Green/PRS where required.
- next: checklist only until software/security closure.

### A-PRS-01 — immutable historical false-GREEN baseline
- status: VERIFIED_HISTORICAL
- anchor: `PRS#17@49fe1f8bca3ddae271d85e0f4767173060267222`.
- rule: historical target evidence cannot certify successor AgentOS heads.

### A-PRS-02 — exact-current-head bounded Green sample
- status: PENDING
- anchor: `AgentOS#104@4c8bcc3...`.
- objective: independently challenge bounded replay/correlation/provenance and the new SG-08 defect fixtures without implying completion.

### A-PRS-03 — completion-grade ownership challenge
- status: BLOCKED
- dependencies: real A-AG-01 repair + identical-head Green PASS.
- objective: rerun complete normal/prepared/successor/crash/replay ownership matrix only then.

# GLOBALSHOPCO

### B-GSC-01 — authenticated supplier evidence closure
- status: ACTIVE / EXTERNAL_EVIDENCE_LIMITED
- anchors: `#29@15fa99eb...`, `#30@80c82475...`.
- objective: exact SKU rows need authenticated trade cost, packaged freight/free-delivery basis, permission, stock identity, returns/warranty.
- current truth: no new authenticated supplier/app evidence; 0 eBay-ready SKUs.
- next: continue read-only evidence closure where sources exist; UNKNOWN/HOLD otherwise. No supplier contact without owner authority.

### B-GSC-02 — conservative delivered-margin gate
- status: PENDING
- dependency: B-GSC-01 evidence-complete row.
- acceptance: all fees/freight/returns allowance explicit; any UNKNOWN => HOLD.

### B-GSC-03 — bounded eBay candidate shortlist
- status: BLOCKED_UPSTREAM
- dependency: B-GSC-01/02.
- acceptance: 2–5 exact variants only after permission + stock + delivered economics + returns/warranty are complete.

# GLOBALSHOPCO-HEADLESS

### B-HDL-01 — checkout secret-boundary baseline
- status: VERIFIED_BOUNDED
- anchor: `4e66a67d3680bd59e3b4da923f9ef291aa6fa358/34891752520` SUCCESS.
- next: preserve; no live checkout/deploy authority.

### B-HDL-02 — destination/host edge inventory
- status: PENDING
- objective: identify only genuinely uncovered scheme/userinfo/port/subdomain/canonical-host confusion cases; add 2–5 homogeneous negatives max.

### B-HDL-03 — Shopify canonical checkout projection
- status: PENDING
- objective: preserve Shopify checkout authority and deny any WordPress/local order/payment authority or secret leakage.

# SHOPIFY -> EBAY

### B-EBAY-01 — upstream durable replay-store discovery
- status: VERIFIED_NONE_FOUND_IN_ADAPTER
- inspected anchor: `23b263ecd4e04667e6c95977f694c66cce4734e2`.
- durable record: `docs/REPLAY-DURABILITY-DISCOVERY.md` at `02087f3c1b6fa4c6b9406b7cd39698c52a72ab6a`.
- verification: Fixture validation `34913579897` SUCCESS.
- finding: adapter tree has no durable replay/idempotency store; `accept_once` consumes caller-supplied seen event IDs / prior hashes only.
- next: trace integration caller to an existing canonical Shopify/AgentOS-approved durable store. If none exists, remain BLOCKED rather than creating SQLite/JSON/ledger/queue locally.

### B-EBAY-02 — restart replay durability negatives
- status: BLOCKED
- dependency: B-EBAY-01 must identify an existing upstream durable store/caller.
- objective when unblocked: 2–5 restart duplicate/conflict/result-write replay tests preserving first-write provenance.

### B-EBAY-03 — evidence-complete SKU admission fixture
- status: BLOCKED
- dependency: GlobalShopCo evidence-complete SKU; controlling truth remains 0 eBay-ready SKUs.
- no live listing/network authority.

# MYPRIMEDELIVERY

### B-MPD-01 — research vs WordPress lineage reconciliation
- status: ACTIVE
- anchors: research `61feceb46de539948374deec86b3fe7578cf8014`; WordPress fixture `a38684c10541115f55f1d5612b72d669dced99f0`.
- exact compare: diverged; research side 101 commits ahead / 4 behind relative to WordPress fixture head, common ancestor before both slices.
- objective: produce compatibility/conflict map before any integration; no stale overwrite/rebase/merge.

### B-MPD-02 — authoritative source/right-to-use evidence queue
- status: PENDING / EXTERNAL_EVIDENCE_LIMITED
- current truth: 100 distinct research concepts, 0 live QUALIFIED products.
- objective: exact ASIN + current product-level Prime + freshness + owner-approved ranking + source rights + outbound destination from authorised evidence.
- editorial/historical Prime observations remain research-only.

### B-MPD-03 — coherent qualification observation tests
- status: VERIFIED_BOUNDED
- anchor: `61feceb.../34879834476` SUCCESS.
- verified: one coherent observation must carry every gate; independent observations cannot combine; conflicting known ASINs fail closed; publication authority and network IO remain false.
- next: add only genuinely uncovered freshness/identity contradictions; do not optimize raw concept count further.

## Replenishment order
1. AgentOS A-AG-01 minimal SG-08 repair; preserve A-AG-02 fail-closed discovery.
2. PRS exact-current-head bounded challenge; completion PRS waits for repaired identical-head Green.
3. GlobalShopCo supplier evidence; if externally blocked, move immediately to Headless/eBay/MyPrime rather than inventing evidence.
4. shopify_ebay trace only an existing upstream durable replay store; no local substitute.
5. MyPrimeDelivery reconcile divergent WordPress/research lineages and deepen qualification evidence; raw concept count is no longer the target.
6. Headless close only uncovered deterministic boundary cases.

No overall GREEN. Scheduled work outside these six projects is intentionally disabled.