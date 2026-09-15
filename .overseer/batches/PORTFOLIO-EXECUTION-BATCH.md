# Portfolio Execution Batch Manifest

Canonical engine: `.overseer/doctrine/PORTFOLIO-BATCH-ENGINE.md`; profiles: `.overseer/profiles/PROJECT-BATCH-PROFILES.md`; security: `.overseer/security/AGENTOS-SECURITY-GATE-MATRIX.md`. Repository/runtime/CI evidence outranks this queue.

**Scheduled scope only:** AgentOS, PRS, GlobalShopCo, GlobalShopCo-Headless, shopify_ebay, MyPrimeDelivery. All other portfolio workstreams remain owner-manual and are not scheduled or consumed here.

**Invariant:** **NO MODEL DECIDES ITS OWN AUTHORITY.** No merge/approve/ready/rebase/deploy/credentials/security-policy changes/production writes/purchases/spend/supplier contact/live publication/physical owner-host action/production autonomy. Functional, security, Green and PRS status remain independent.

## Checkpoint reconciliation — 2026-09-15 17:30 Brisbane
- No scheduled project head changed since the prior durable checkpoint. Exact evidence reconfirmed: AgentOS #104 `4c8bcc3bc2ad2041b0a1871d3004c1db23f3c091`; #112 `d1645450a06d00c49a7a78f176e97b44b9eaa225`; PRS #24 `3039c886bdcff911f7c6dcc3e086368058e57fb6`; GlobalShopCo #30 `80c82475b98663d677885e8b4d222ae2cedb8555`; Headless #1 `c3f4939f1b7de8ef6e7fe6547400343dbb076348`; shopify_ebay main `c68883f24fb3711fce567a35b1a80db74933b82a`; MyPrime research `61feceb46de539948374deec86b3fe7578cf8014` and WordPress fixture `a38684c10541115f55f1d5612b72d669dced99f0`.
- Therefore no new VERIFIED movement is claimed. BLOCKED_STABLE records remain closed to rediscovery; executors fall through to independent ready slices below.

# AgentOS — Level 2 P0
### A-AG-01 continuous ownership fence — BLOCKED_STABLE
Anchor `AgentOS#104@4c8bcc3bc2ad2041b0a1871d3004c1db23f3c091`. Objective: one crash-releasing ownership fence held continuously through final verification -> side effect/prepared recovery -> durable success receipt -> release. Acceptance: replacement/successor/three-writer/TOCTOU/crash/replay/prepared-recovery negatives deny false success with exact-head Ubuntu+Windows CI. Next: only existing #104 owner may implement smallest repair on existing writer seam; no competing lock/ledger. Security `SG-03,08,09,10,11,14,18,19`; S2; Green=yes; PRS=yes after identical-head Green; merge/deploy/physical/production owner-only.
### A-AG-02 authenticated actor + canonical grant — BLOCKED_STABLE
Anchor `#104@4c8bcc3...`. Real authenticated identity source/canonical grant resolver still not evidenced. Next: none until source evidence changes. Security `SG-01,02,03,04,09,10,11,18,19`; S2; credentials/security-policy owner-only.
### A-AG-03 runtime-shell eligibility consolidation — ACTIVE
Anchor `AgentOS#112@d1645450a06d00c49a7a78f176e97b44b9eaa225`. Objective: one canonical normalization/evaluation path without authority widening. Acceptance: aliases deterministic; compatibility adapter reuses canonical evaluator; asserted eligibility without canonical result denied; adjacent unauthorized capability denied; exact-head CI. Next executable mini-batch: (1) inventory uncovered aliases/evaluator entry points, (2) add 2–5 homogeneous denial/normalization cases, (3) run exact-head CI, (4) preserve #104 hot path untouched. Security `SG-02,03,04,10,18`; S2; branch/tests only; Green for promotion.
### A-AG-04 replay/correlation slice — PENDING
Anchor #104 current lineage. Objective: uncovered first-write provenance/conflicting identity/duplicate result/restart duplicate cases only. Next: inventory then implement 2–5 homogeneous gaps without changing ownership or adding persistence. Security `SG-09,10,11,14,18`; S2.
### A-AG-05 physical Windows acceptance — BLOCKED_STABLE
Dependency repaired #104 + authenticated admission + Jess/Michael + PRS + owner physical authority. Next none. Security `SG-03,08,10,11,14,18,20`; S2.

# PRS — independent assurance
### A-PRS-01 historical false-GREEN baseline — VERIFIED
Anchor `PRS#17@49fe1f8bca3ddae271d85e0f4767173060267222`; historical only. Security `SG-01,02,08,10,11,19`; S0.
### A-PRS-02 changed-head bounded challenge — PENDING
Target only a changed AgentOS #104 lineage. Skip unchanged head; reopen automatically on changed target/evidence. Security `SG-08,09,10,11,19`; S1.
### A-PRS-03 completion-grade ownership challenge — BLOCKED_STABLE
Anchor `PRS#24@3039c886bdcff911f7c6dcc3e086368058e57fb6` plus future repaired AgentOS head. Requires identical-head Jess functional PASS + Michael security PASS first. Security `SG-08,09,10,11,18,19`; S2.
### A-PRS-04 physical evidence-contract negatives — PENDING
Anchor `PRS#24@3039c886...`. Next executable mini-batch: inventory current contract fixtures; add only missing stale/missing/mismatched AgentOS head, host/root, mutation/recovery/correlation/artifact identity cases; validate exact PRS head. No physical execution. Security `SG-10,11,19,20`; S1.

# GlobalShopCo
### B-GSC-01 authenticated supplier evidence closure — ACTIVE
Anchors `#29@15fa99eb4c4b1f96127f6f51c412cbffc94e45e2`, `#30@80c82475b98663d677885e8b4d222ae2cedb8555`. Process only newly available authenticated trade cost, packaged freight/free-delivery basis, permission, stock identity, returns/warranty. Missing material field => HOLD. Security `SG-02,06,10,12,13,14,15,20`; S1; read-only.
### B-GSC-02 delivered-margin gate — PENDING
Dependency evidence-complete B-GSC-01 row. Calculate fees/freight/returns allowance only after completeness; unknown/stale/negative => HOLD. Security `SG-10,12,13,14,20`; S1.
### B-GSC-03 eBay shortlist — BLOCKED_STABLE
Truth `0 eBay-ready SKUs`; reopen only when exact variant has permission+stock+delivered economics+returns/warranty. Security `SG-02,06,10,12,13,14,15,20`; S1.
### B-GSC-04 compact AU-stock evidence mini-batch — PENDING
Next executable: 2–5 compact/light candidates only where authenticated evidence routes exist; capture exact identity/provenance/freight/permission/stock/returns or HOLD; stop at retail/syndicated-only evidence. Security `SG-06,10,12,13,14,15,20`; S1.

# GlobalShopCo-Headless
### B-HDL-01 configured Shopify store authority — VERIFIED
Anchor `#1@c3f4939f1b7de8ef6e7fe6547400343dbb076348`; bounded non-production only. Security `SG-02,05,06,10,14,20`; S1.
### B-HDL-02 malformed configured checkout authority — VERIFIED
Same anchor; bounded configured authority negatives only. Security `SG-02,06,10,14,20`; S1.
### B-HDL-03 canonical checkout projection — PENDING
Next executable mini-batch: inventory current tests then add 2–5 uncovered cases proving canonical Shopify checkout only, no local payment/order mutation, alternate host/local-order denial; exact-head CI. Security `SG-02,05,06,10,14,20`; S1.
### B-HDL-04 product identity/availability contradictions — PENDING
Next: 2–5 homogeneous variant mismatch, stale availability, duplicate cart identity fixtures; exact-head CI. Security `SG-06,09,10,14`; S1.
### B-HDL-05 dev-store/browser acceptance — BLOCKED_STABLE
Needs genuine dev-store/browser evidence plus owner-authorized credentials/environment. Security `SG-05,10,14,20`; S2.

# shopify_ebay
### B-EBAY-01 upstream durable replay owner — BLOCKED_STABLE
Anchor main `c68883f24fb3711fce567a35b1a80db74933b82a`. No evidenced canonical upstream persistence owner; no new ledger permitted. Security `SG-02,09,10,11,14`; S1.
### B-EBAY-02 restart replay durability negatives — BLOCKED_STABLE
Dependency B-EBAY-01. Security `SG-09,10,11,14`; S2.
### B-EBAY-03 evidence-complete SKU admission — BLOCKED_STABLE
Dependency GlobalShopCo evidence-complete variant; current truth zero. Security `SG-02,06,10,12,13,14,15,20`; S1.
### B-EBAY-04 synthetic mapper identity regression — PENDING
Next executable mini-batch: inventory mapper coverage then implement 2–5 uncovered variant mismatch/malformed ID/conflicting hash/duplicate event cases using fixtures only; run repo tests. No live API/publication/persistence. Security `SG-06,09,10,14`; S1.

# MyPrimeDelivery
### B-MPD-01 divergent-lineage compatibility map — ACTIVE
Anchors research `61feceb46de539948374deec86b3fe7578cf8014`, fixture `a38684c10541115f55f1d5612b72d669dced99f0`, merge base `3635c903214b06464e28674d5a6403f8539b8c1e`. Next executable mini-batch: compare presentation/data contracts path-by-path; classify compatible/conflicting/fixture-only; select smallest compatible presentation-contract port; no merge/rebase/stale overwrite. Security `SG-10,11,14,20`; S1.
### B-MPD-02 authoritative source/right-to-use evidence — PENDING
Truth `0 live QUALIFIED`; process only newly available authorized coherent product observations. Editorial/public pages never become Prime/rank/deal authority. Security `SG-02,06,10,12,14,15,20`; S1.
### B-MPD-03 coherent qualification baseline — VERIFIED
Anchor research `61feceb...`; one-observation coherence and conflicting-known-ASIN denial only. Security `SG-06,09,10,14`; S1.
### B-MPD-04 WordPress non-production presentation adapter — PENDING
Dependency B-MPD-01. After compatibility map, port only compatible contract; HOLD/UNKNOWN cannot emit monetized/live CTA; exact outbound destination; no secret leakage. Security `SG-05,06,10,14,15,20`; S2; Green if promoted.
### B-MPD-05 freshness/identity contradiction mini-batch — PENDING
Next: inventory validator coverage; add 2–5 genuine stale Prime/rank/deal or identity/outbound contradictions; exact-head fixture CI. Security `SG-06,09,10,14`; S1.

## Execution order / starvation control
1. AgentOS A-AG-01 remains P0 BLOCKED_STABLE; execute A-AG-03 then A-AG-04 while ownership source is unchanged.
2. PRS does not recertify unchanged #104; execute A-PRS-04 fixture gaps independently.
3. Headless has recent VERIFIED movement; execute B-HDL-03/04 adjacent deterministic slices.
4. GlobalShopCo consumes authenticated evidence only; otherwise execute one bounded B-GSC-04 source-route batch and stop at public-only evidence.
5. shopify_ebay executes B-EBAY-04 while persistence/SKU blockers remain stable; never create persistence.
6. MyPrimeDelivery executes B-MPD-01 before B-MPD-04; B-MPD-05 may run independently.

**No new VERIFIED movement this checkpoint. No overall GREEN. Manual projects remain untouched.**