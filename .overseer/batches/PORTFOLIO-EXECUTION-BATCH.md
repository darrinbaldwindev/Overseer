# Portfolio Execution Batch Manifest

**Purpose:** queue state only for the fixed scheduled portfolio lanes. Canonical execution procedure: `.overseer/doctrine/PORTFOLIO-BATCH-ENGINE.md`. Project shaping: `.overseer/profiles/PROJECT-BATCH-PROFILES.md`. Security: `.overseer/security/AGENTOS-SECURITY-GATE-MATRIX.md`. Exact repository/issue/CI/runtime evidence always outranks this manifest.

**Fixed lanes:** A = AgentOS Level 2 P0 + PRS/Green assurance-adjacent work; B = GlobalShopCo/Headless/eBay/Amazon/MyPrimeDelivery; C = Affiliate-Websites AU/UK/US/Master, GhostKitchen, Franchise, GemVerse, Content360, Commercial Frontend, Marketing.

**States:** `PENDING | ACTIVE | VERIFIED | BLOCKED | STALE | SPLIT_REQUIRED`.

**Core invariant:** **NO MODEL DECIDES ITS OWN AUTHORITY.** Functional state, security state and PRS state remain separate. No merge/approve/ready/rebase/deploy/credentials/security-policy changes/production writes/purchases/spend/supplier contact/live publication/physical owner-host action/production autonomy.

## Checkpoint reconciliation — 2026-09-15 02:30 Brisbane
- Previous durable checkpoint: Overseer #49 `5666496495`; previous manifest blob `7c9d51dc1f670eafb12aa60f25e52b904032c972` / commit `98db9d3887c24432f25484f077cbd393fd05b210`. Historical evidence remains preserved in Git history and durable #49 checkpoints; predecessor outcomes never transfer to successor heads.
- Canonical batch engine, central project profiles and security matrix were re-read before queue state. Repo/issue/CI evidence overrode stale manifest anchors.
- **AgentOS PR #104:** OPEN/DRAFT/UNMERGED/runtime-disabled at exact `7f84f4f3fae841b18068bfe3d630ce36e8b1a07e`; AgentOS Tests `34866176685` SUCCESS. A-AG-04 receipt authority-evidence persistence/reload is narrowly functionally VERIFIED on this head. SG-08 continuous writer ownership and SG-01/02 authenticated actor/canonical grant admission remain BLOCKED; no identical-head Green/PRS promotion evidence closes them.
- **AgentOS PR #111:** stale manifest anchor corrected. Current exact head is `352c83fdbcff65dd9dc592fb3b8d65d4aa130969`; AgentOS Tests `34863648579` SUCCESS. Basic Chat lifecycle/readiness remains narrowly functionally VERIFIED; SG-18 promotion remains separate.
- **GlobalShopCo:** canonical default branch remains `agent/overseer/initial-project-timeline@79d50227fe19826d42c43e7dec15ce245ad58e40`; active product-research seams remain PR #29/#30 and `0 eBay-ready SKUs` remains controlling. No hidden freight/trade/permission field is promoted.
- **MyPrimeDelivery:** exact `agent/overseer/initial-project-timeline@c3264566f3965121a2501c72308ed116ed80d333`; Fixture validation `34867512346` SUCCESS. Qualification-depth funnel mechanics are narrowly VERIFIED S2/non-production across the 101-row/100-normalized-concept corpus; current commercial truth remains `0 live QUALIFIED products`, with authoritative ASIN/Prime/rank/deal/source-rights/outbound evidence still UNKNOWN/HOLD where absent.
- **Affiliate-Websites:** current `main@d3cf400aabe631dc6c2e37193eca8b192856eaba`; Master PR #17 exact `ef0e7306e40d696abe324ad73baee4abf04a6f6f`, Master identity/destination PR #19 exact `ea2ec9ce6ced26c4841d080abb4403193f299519`, US research PR #6 exact `602b14764bb7bb263b4e0cbd9b39550f4e0bd497`. Existing active seams are preserved; no duplicate implementation assigned.
- **GhostKitchen:** `main@dbd64153ca3f2b0e7e9152955692f62f6c9fa59a`; PR #32 exact `c1892e6b5f4489b62f613f827bea3bd714275009` remains the active economics-metadata seam. Hypothesis/reference economics remain non-promotable.
- **Franchise:** `main@0ea3b26de71f78f7eafc38cf50079805b43a7d93`; PR #24 exact `ac208a07c40e99ee1c1f70f67a1a857d8207fa6e` and PR #22 exact `7b8b07562f69ce7988f82e1f3ec71a225fb23709` remain active tenancy/territory seams. Persistence/migrations/request-context/A-B isolation remain incomplete.
- **GemVerse:** default `gemverse@b36750f01f62184e2f563ff8f8030682ba10033e`; PR #10 exact `b1f09c3a9300a24782f5f3e4ab01619a64477319` remains fixture-only recovery assurance. Canon-dependent implementation stays blocked.
- **Content360:** PR #4 current exact `133dad248e56571b9c5c5d4c9fcf8b4fd63f202d`. Stale/superseded/conflicting Marketing-source provenance denial is implemented, but exact-head check runs are still absent; predecessor success is not transferred. State remains ACTIVE/CI-pending. Live API/auth/PUBLISH/SCHEDULE/network authority remains UNKNOWN/blocked.
- **Commercial Frontend:** Overseer PR #50 exact `6391a64728faae7352b4ce5fd7dfe9903fd7377b` remains interpretation-only; direct operator frequency/friction/consequence/authority/WTP evidence remains the commercial gate.

# LANE A — AgentOS Level 2 P0

## AgentOS Overseer subqueue

### A-AG-01 — continuous project-file ownership fence
- status: BLOCKED; owner/workstream: AgentOS / writer ownership; exact anchor: AgentOS PR #104 `7f84f4f3fae841b18068bfe3d630ce36e8b1a07e`, Tests `34866176685`, historical PRS defect baseline `0defebe26f71e1cf5df1168fa5454bfd8de30091` / `34821646371`; objective: one crash-releasing kernel-enforced fence from final verification through publish/prepared recovery and durable success receipt; acceptance: replacement-after-verify, successor/three-writer, stale identity, TOCTOU, crash/replay, duplicate mutation/result and prepared-recovery stale-owner all fail closed; dependencies: real writer implementation change; safe action boundary: draft non-prod code/tests only; verification: adversarial ownership matrix + exact Ubuntu/Windows CI; next handoff: identical-head Green then PRS.
- security_gates: `SG-03,SG-08,SG-09,SG-10,SG-11,SG-14,SG-18,SG-19`; risk_class: S2; authority_required: scoped branch/test write; negative_tests: ownership matrix above; receipt_evidence: actor/task/file/pre-postimage/ownership/result lineage; green_required: yes; prs_required: yes; owner_boundary: merge/deploy/physical production; security_disposition: BLOCKED.

### A-AG-02 — authenticated actor + canonical grant binding
- status: BLOCKED; owner/workstream: AgentOS / authority admission; exact anchor: PR #104 `7f84f4f3...` + current canonical authority dependency contract; objective: bind an existing authenticated actor source and canonical grant resolver without a second authority registry; acceptance: payload/host cannot self-supply identity/grant and missing/spoofed/mismatched/cross-project/replayed grant yields no admitted artifact/success receipt; dependencies: real bindable canonical source; safe action boundary: architecture discovery + bounded branch tests; verification: provenance/spoof/mismatch/replay matrix; next handoff: AgentOS architecture/implementation.
- security_gates: `SG-01,SG-02,SG-03,SG-04,SG-09,SG-10,SG-11,SG-18,SG-19`; risk_class: S2; authority_required: canonical identity/grant read + scoped tests; negative_tests: host-as-auth, spoof actor, payload self-grant, absent/mismatch/cross-project/replay; receipt_evidence: issuer/source/version/request/task/mission; green_required: yes; prs_required: yes; owner_boundary: credentials/security policy; security_disposition: BLOCKED.

### A-AG-03 — Basic Chat lifecycle/readiness projection
- status: VERIFIED; owner/workstream: AgentOS / Basic Chat; exact anchor: PR #111 `352c83fdbcff65dd9dc592fb3b8d65d4aa130969`, Tests `34863648579` SUCCESS; objective: preserve truthful lifecycle/readiness and stale physical-acceptance fail-closed behavior; acceptance: no fabricated mutation readiness, no raw/secret/PRS/recovery leakage, cross-platform tests green; dependencies: none; safe action boundary: tests/small frontend projection fixes only; verification: exact-head CI; next handoff: A-PRS-04/Green SG-18 sample.
- security_gates: `SG-03,SG-05,SG-10,SG-11,SG-14,SG-18`; risk_class: S2; authority_required: scoped branch tests; negative_tests: immediate signal, stale physical head, fabricated readiness, correlation/leakage; receipt_evidence: exact head/run/test names; green_required: yes before promotion; prs_required: conditional; owner_boundary: merge/deploy/runtime enablement; security_disposition: PENDING.

### A-AG-04 — authority-evidence receipt persistence/reload/recovery
- status: VERIFIED; owner/workstream: AgentOS / receipt provenance; exact anchor: PR #104 `7f84f4f3fae841b18068bfe3d630ce36e8b1a07e`, substantive test commit `5e3d7c2ac6f515dceda832ef09b3087f20fb1d7b`, Tests `34866176685` SUCCESS; objective: preserve source-backed `authority_evidence_id` through existing receipt persistence/reload without broadening authority; acceptance: exact ID retained and missing/stale/mismatch cannot normalize to admitted success; dependencies: existing receipt schema only; safe action boundary: tests/small compatible fix; verification: exact-head reload/recovery fixtures + CI; next handoff: A-AG-05 then Green if unchanged.
- security_gates: `SG-02,SG-09,SG-10,SG-11,SG-14,SG-18`; risk_class: S2; authority_required: scoped branch tests; negative_tests: missing/stale/mismatch/cross-task authority evidence; receipt_evidence: authority evidence ID + request/task/result/receipt lineage; green_required: yes for promotion; prs_required: conditional; owner_boundary: merge/deploy; security_disposition: PENDING.

### A-AG-05 — receipt replay/correlation adjacency mini-batch
- status: PENDING; owner/workstream: AgentOS / receipt correlation; exact anchor: successor to PR #104 `7f84f4f3...` / A-AG-04 exact schema; objective: homogeneous replay/correlation regressions only; acceptance: duplicate result write, replayed receipt, cross-task/cross-mission mismatch and stale receipt fail closed; dependencies: fresh pre-scan proving no concurrent owner; safe action boundary: tests first, minimal fix only if defect found; verification: exact-head CI; next handoff: Green/PRS according to widened risk.
- security_gates: `SG-09,SG-10,SG-11,SG-14,SG-18`; risk_class: S2; authority_required: scoped tests; negative_tests: replay, duplicate result, cross-task/cross-mission, stale receipt; receipt_evidence: immutable IDs/hashes/disposition; green_required: yes; prs_required: conditional; owner_boundary: merge/deploy; security_disposition: PENDING.

### A-AG-06 — physical Windows acceptance packet
- status: BLOCKED; owner/workstream: AgentOS / physical host; exact anchor: PR #104 `7f84f4f3...` with A-AG-01/A-AG-02 unresolved; objective: maintain exact owner-run acceptance packet after software/security closure; acceptance: exact SHA/root/mutation/recovery/correlation/no-production boundary; dependencies: SG-08 + SG-01/02 + explicit owner physical authority; safe action boundary: checklist only; verification: future physical-host evidence; next handoff: owner/physical-host lane.
- security_gates: `SG-03,SG-08,SG-10,SG-11,SG-14,SG-18,SG-20`; risk_class: S2; authority_required: owner-authorized physical Windows action; negative_tests: wrong head, prod root, missing receipt; receipt_evidence: head/host/root/test/result; green_required: yes; prs_required: yes if promoted; owner_boundary: physical Windows execution; security_disposition: BLOCKED.

## PRS / Green assurance subqueue

### A-PRS-01 — immutable stale-owner false-GREEN baseline
- status: VERIFIED; owner/workstream: PRS; exact anchor: PRS `0defebe26f71e1cf5df1168fa5454bfd8de30091` / `34821646371` against historical AgentOS target; objective: preserve immutable defect baseline without inheritance to successors; acceptance: exact target/artifact identity retained; dependencies: none; safe action boundary: read-only assurance; verification: hashes; next handoff: A-AG-01.
- security_gates: `SG-08,SG-10,SG-11,SG-19`; risk_class: S0; authority_required: read-only; negative_tests: normal publish + prepared recovery stale-owner; receipt_evidence: immutable target/artifact hashes; green_required: no; prs_required: baseline; owner_boundary: none; security_disposition: VERIFIED.

### A-PRS-02 — successor ownership challenge
- status: BLOCKED; owner/workstream: PRS; exact anchor: current AgentOS PR #104 `7f84f4f3...` plus A-PRS-01; objective: rerun full ownership matrix only after real writer repair and identical-head Green PASS; acceptance: normal/prepared/successor/crash/replay independently classified; dependencies: A-AG-01 + exact CI + Green; safe action boundary: assurance harness; verification: immutable target/artifact hashes; next handoff: Overseer.
- security_gates: `SG-08,SG-09,SG-10,SG-11,SG-19`; risk_class: S2; authority_required: bounded harness; negative_tests: full ownership matrix; receipt_evidence: exact target/artifact hash; green_required: yes prerequisite; prs_required: yes; owner_boundary: merge/deploy; security_disposition: BLOCKED.

### A-PRS-03 — admission + frontend false-GREEN mini-batch
- status: PENDING; owner/workstream: Green first / PRS conditional; exact anchors: A-AG-02 and PR #111 `352c83fd...` / `34863648579`; objective: (1) queue admission spoof/missing/mismatch/self-grant assurance after canonical admission exists and (2) immediately executable read-only Basic Chat fabricated-readiness/leakage sample; acceptance: no false readiness/authority or evidence leak; dependencies: admission half blocked, frontend half actionable; safe action boundary: tests/read only; verification: immutable exact-head negatives; next handoff: AgentOS Overseer.
- security_gates: `SG-01,SG-02,SG-05,SG-10,SG-11,SG-18,SG-19`; risk_class: S1; authority_required: read/test only; negative_tests: fabricated readiness, stale evidence, spoof/self-grant when available, leakage; receipt_evidence: exact target/run/test outcomes; green_required: yes; prs_required: conditional; owner_boundary: merge/deploy; security_disposition: PENDING.

# LANE B — Commerce

## GlobalShopCo subqueue

### B-GSC-01 — active product evidence consumption
- status: ACTIVE; owner/workstream: GlobalShopCo qualification; exact anchor: `agent/overseer/initial-project-timeline@79d50227fe19826d42c43e7dec15ce245ad58e40`, PR #29/#30, `0 eBay-ready SKUs`; objective: reconcile exact SKU/GTIN, buy-cost class, freight, marketplace permission, stock/fulfilment, AU/eBay comps, returns/warranty; acceptance: each row PROMOTE/REJECT/HOLD with every missing field explicit; dependencies: active PR ownership; safe action boundary: research/docs/calculation; verification: source/date/identity/economics table; next handoff: channel gates.
- security_gates: `SG-02,SG-03,SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public/read-only evidence; negative_tests: missing freight/permission/stock/seller/fee => HOLD; receipt_evidence: exact source/date/SKU/economics; green_required: no; prs_required: no; owner_boundary: supplier contact/purchase/publication; security_disposition: ACTIVE.

### B-GSC-02 — exact-SKU economics mini-batch
- status: PENDING; owner/workstream: GlobalShopCo economics; exact anchor: GSC `79d50227...` + current PR #29/#30 candidates; objective: re-screen 2–5 non-overlapping candidates with exact AU/eBay comps, weight/freight and max-buy-cost ceiling; acceptance: deterministic disposition and UNKNOWN permission/freight explicit; dependencies: public evidence; safe action boundary: read-only research/calculation; verification: reproducible calculator inputs; next handoff: B-GSC-03.
- security_gates: `SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public read-only; negative_tests: stale comp/unknown freight/permission => HOLD; receipt_evidence: sources/date/calculation; green_required: no; prs_required: no; owner_boundary: supplier contact/purchase; security_disposition: PENDING.

### B-GSC-03 — comparison-ready pilot matrix
- status: PENDING; owner/workstream: GlobalShopCo matrix; exact anchor: GSC `79d50227...` + B-GSC-01/02 outputs; objective: normalize 5–10 evidence-complete/rejected/HOLD rows; acceptance: supplier/SKU/GTIN, landed inputs, comps, freight/free-delivery contribution, permission, stock, returns/warranty, fee basis, disposition; dependencies: qualification outputs; safe action boundary: docs/calculation only; verification: schema completeness + calculator; next handoff: eBay/Amazon.
- security_gates: `SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read/docs; negative_tests: missing material field cannot promote; receipt_evidence: row-level evidence pointers; green_required: no; prs_required: no; owner_boundary: publication/spend/contact; security_disposition: PENDING.

## Shopify→eBay subqueue

### B-EBAY-01 — synthetic replay/conflict baseline
- status: VERIFIED; owner/workstream: Shopify→eBay; exact anchor: `8d891d782dca6799a9a4d942218fde441685e5dc` / Fixture validation `34856089804` SUCCESS; objective: preserve event-ID/payload conflict denial and benign exact replay with zero network/publication authority; acceptance: altered replay fails closed; dependencies: none; safe action boundary: synthetic fixtures; verification: exact CI; next handoff: B-EBAY-02.
- security_gates: `SG-02,SG-03,SG-09,SG-10,SG-11,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: non-prod tests; negative_tests: altered replay, stale event, correlation mismatch; receipt_evidence: event/payload hash/disposition; green_required: no for synthetic; prs_required: no; owner_boundary: network/publication; security_disposition: VERIFIED.

### B-EBAY-02 — receipt persistence/correlation mini-batch
- status: PENDING; owner/workstream: Shopify→eBay; exact anchor: B-EBAY-01 `8d891d...`; objective: inspect existing persistence then test restart replay, duplicate result and mismatched receipt identity; acceptance: same event+same payload idempotent, changed payload denied, exact result/receipt correlation, no second persistence plane; dependencies: schema support; safe action boundary: fixtures/tests/minimal compatible fix; verification: exact-head CI; next handoff: channel assurance.
- security_gates: `SG-09,SG-10,SG-11,SG-14,SG-15`; risk_class: S2; authority_required: non-prod tests; negative_tests: restart replay, duplicate result, mismatched receipt; receipt_evidence: event/payload/result/receipt lineage; green_required: conditional; prs_required: no; owner_boundary: publication/network; security_disposition: PENDING.

### B-EBAY-03 — real SKU readiness gate
- status: BLOCKED; owner/workstream: Shopify→eBay live readiness; exact anchor: GSC `79d50227...`, `0 eBay-ready SKUs`; objective: consume only rows with permission, fulfilment/stock, exact freight/economics and seller/fee evidence; acceptance: no publication-ready classification with missing material field; dependencies: B-GSC-03; safe action boundary: read-only preflight; verification: evidence packet; next handoff: owner only if solely owner-gated evidence remains.
- security_gates: `SG-02,SG-03,SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read-only; negative_tests: missing permission/freight/seller/fee/stock => HOLD; receipt_evidence: SKU evidence packet; green_required: no; prs_required: no; owner_boundary: listing/account/contact/spend; security_disposition: BLOCKED.

## Shopify→Amazon subqueue

### B-AMZ-01 — compound-conflict synthetic baseline
- status: VERIFIED; owner/workstream: GlobalShopCo / Amazon fixtures; exact anchor: `0b52631e9a3f084d9b947227c84e7f656ebab6f5` / `34856135125` SUCCESS; objective: preserve permission/stock/category/identifier/fulfilment/fee/source conflict denial while Shopify stays canonical; acceptance: compound conflicts deny; dependencies: none; safe action boundary: synthetic tests; verification: exact CI; next handoff: B-AMZ-02.
- security_gates: `SG-02,SG-03,SG-09,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: non-prod tests; negative_tests: compound conflicts; receipt_evidence: head/run/conflict code; green_required: no for synthetic; prs_required: no; owner_boundary: seller/listing/credentials; security_disposition: VERIFIED.

### B-AMZ-02 — freshness/version/correlation mini-batch
- status: PENDING; owner/workstream: GlobalShopCo / Amazon fixtures; exact anchor: B-AMZ-01 `0b52631...`; objective: deny stale/version-mismatched/cross-SKU evidence only where schema already exposes those fields; acceptance: mismatch fails closed, absent schema => SPLIT_REQUIRED; dependencies: schema inspection; safe action boundary: tests/small compatible fix; verification: exact CI; next handoff: Amazon gate.
- security_gates: `SG-06,SG-09,SG-10,SG-11,SG-14`; risk_class: S2; authority_required: non-prod tests; negative_tests: stale source, mismatched version, cross-SKU evidence; receipt_evidence: source/version/SKU/disposition; green_required: conditional; prs_required: no; owner_boundary: credentials/listing; security_disposition: PENDING.

### B-AMZ-03 — real Amazon readiness
- status: BLOCKED; owner/workstream: GlobalShopCo / Amazon AU; exact anchor: synthetic-only `0b52631...`; objective: keep seller-of-record, permission, variant/stock, category/GTIN, fulfilment and fee/economics UNKNOWN until authoritative evidence; acceptance: fixtures never imply live-ready; dependencies: owner/account evidence later; safe action boundary: read-only research; verification: authoritative packet; next handoff: owner when needed.
- security_gates: `SG-02,SG-03,SG-06,SG-10,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read-only; negative_tests: missing seller/permission/category/fee => HOLD; receipt_evidence: evidence packet; green_required: no; prs_required: no; owner_boundary: seller account/credentials/listing; security_disposition: BLOCKED.

## GlobalShopCo-Headless subqueue

### B-HDL-01 — deterministic storefront contract
- status: VERIFIED; owner/workstream: Headless; exact anchor: `agent/chatgpt/m3-baseline@44552d2a94dcea1445dddeb2d8a853d6d2b34d3e`; objective: preserve Shopify product/cart/checkout authority and host/parser denial; acceptance: no local duplicate catalogue/order authority; dependencies: none; safe action boundary: tests; verification: deterministic suite; next handoff: B-HDL-02.
- security_gates: `SG-02,SG-03,SG-05,SG-06,SG-10,SG-14,SG-20`; risk_class: S2; authority_required: non-prod tests; negative_tests: host confusion, malformed destination, secret leakage; receipt_evidence: exact branch/tests; green_required: conditional; prs_required: no; owner_boundary: deployment/secrets/live purchase; security_disposition: VERIFIED.

### B-HDL-02 — synthetic Shopify checkout handoff mini-batch
- status: PENDING; owner/workstream: Headless; exact anchor: `44552d2a...` + GSC evidence matrix; objective: 2–5 homogeneous identity/availability/host handoff fixtures; acceptance: exact product/variant survives render→Shopify checkout, unavailable item cannot appear purchasable, host canonical; dependencies: suitable synthetic fixture; safe action boundary: local/dev tests; verification: integration fixtures; next handoff: B-HDL-03.
- security_gates: `SG-03,SG-05,SG-06,SG-10,SG-14`; risk_class: S2; authority_required: non-prod tests; negative_tests: wrong product/variant, unavailable, host substitution; receipt_evidence: fixture/result; green_required: conditional; prs_required: no; owner_boundary: deployment/live purchase; security_disposition: PENDING.

### B-HDL-03 — live dev-store/browser proof
- status: BLOCKED; owner/workstream: Headless; exact anchor: `44552d2a...`; objective: real non-prod browser checkout proof; acceptance: owner-authorized dev store + exact product handoff; dependencies: owner/environment; safe action boundary: none now; verification: future browser evidence; next handoff: owner/environment.
- security_gates: `SG-03,SG-05,SG-10,SG-14,SG-20`; risk_class: S2; authority_required: owner-authorized non-prod environment; negative_tests: prod host, wrong store, missing access; receipt_evidence: environment/product/URL/result; green_required: yes if promoted; prs_required: no; owner_boundary: access/deployment/purchase; security_disposition: BLOCKED.

## MyPrimeDelivery subqueue

### B-MPD-01 — identity corpus baseline
- status: VERIFIED; owner/workstream: MyPrimeDelivery; exact anchor: branch `agent/overseer/initial-project-timeline@c3264566f3965121a2501c72308ed116ed80d333`, predecessor identity closure `9b41ebbf49732d31ef3dc428636ecf31169f20c4` / `34860891240`; objective: preserve 101 evidence rows→100 normalized concepts, duplicate observation separation, all 12 categories, no ASIN guessing; acceptance: unresolved identity remains fail-closed; dependencies: none; safe action boundary: tests/docs; verification: exact corpus checks; next handoff: B-MPD-02.
- security_gates: `SG-02,SG-03,SG-05,SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: non-prod tests; negative_tests: title-only != verified identity, duplicate observation != merged ASIN; receipt_evidence: corpus/head/counts; green_required: no; prs_required: no; owner_boundary: provider signup/credentials/publication; security_disposition: VERIFIED.

### B-MPD-02 — provider identity/freshness negatives
- status: PENDING; owner/workstream: MyPrimeDelivery; exact anchor: current `c3264566...` schema; objective: homogeneous ASIN/marketplace/variant/freshness mismatch denial using provider-neutral fixtures; acceptance: stale/mismatched evidence fails closed and source rights stay separate from product truth; dependencies: existing adapter schema; safe action boundary: synthetic tests; verification: exact-head output; next handoff: qualification evidence gap export.
- security_gates: `SG-06,SG-09,SG-10,SG-11,SG-14`; risk_class: S2; authority_required: non-prod tests; negative_tests: ASIN mismatch, marketplace mismatch, stale provider, variant conflict; receipt_evidence: source/version/product/disposition; green_required: conditional; prs_required: no; owner_boundary: live provider credentials; security_disposition: PENDING.

### B-MPD-03 — qualification-depth funnel mechanics
- status: VERIFIED; owner/workstream: MyPrimeDelivery; exact anchor: `c3264566f3965121a2501c72308ed116ed80d333`, Fixture validation `34867512346` SUCCESS; objective: separately count identity/current Prime/freshness/ranking/source-rights/outbound-destination gates without allowing historical/editorial/UNKNOWN evidence to satisfy them; acceptance: synthetic all-gates remains `publication_authority=false`, `network_io=false`, current live qualified count remains zero absent authoritative evidence; dependencies: current corpus; safe action boundary: analysis/tests; verification: deterministic funnel output + CI; next handoff: B-MPD-04.
- security_gates: `SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: non-prod repo tests; negative_tests: historical/event/editorial/UNKNOWN cannot qualify; receipt_evidence: corpus head + gate counts + run; green_required: no for bounded fixture; prs_required: no; owner_boundary: provider/account/publication; security_disposition: VERIFIED.

### B-MPD-04 — WordPress evidence-safe presentation
- status: PENDING; owner/workstream: MyPrimeDelivery; exact anchor: `c3264566...` / `34867512346`; objective: render category/product fixtures from qualification states without Prime/deal/rank claims lacking current authoritative evidence; acceptance: unresolved gates visibly non-qualified and outbound destination explicit; dependencies: current funnel output; safe action boundary: non-public fixture/docs; verification: snapshot/schema audit; next handoff: Marketing only after qualification.
- security_gates: `SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: non-public fixture/docs; negative_tests: stale deal, unknown Prime, unresolved destination; receipt_evidence: product/evidence/display state; green_required: no; prs_required: no; owner_boundary: publication/provider signup; security_disposition: PENDING.

# LANE C — Growth / verticals

## Affiliate-Websites Master subqueue

### C-AFF-M-01 — publication-state / CTA evidence contract
- status: ACTIVE; owner/workstream: Affiliate Master; exact anchors: `main@d3cf400aabe631dc6c2e37193eca8b192856eaba`, PR #17 `ef0e7306e40d696abe324ad73baee4abf04a6f6f`, PR #19 `ea2ec9ce6ced26c4841d080abb4403193f299519`; objective: UNKNOWN/non-affiliate relationships never emit monetized CTA and country/destination identity stays exact; acceptance: deterministic non-monetized fallback; dependencies: active PR ownership; safe action boundary: branch tests/docs; verification: fixtures/CI; next handoff: country lanes.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: non-prod tests; negative_tests: unknown relationship, stale destination, injected CTA; receipt_evidence: program/country/state/destination; green_required: conditional; prs_required: no; owner_boundary: signup/publication; security_disposition: ACTIVE.

### C-AFF-M-02 — country separation mini-batch
- status: PENDING; owner/workstream: Affiliate Master; exact anchor: `main@d3cf400a...`, PR #19 `ea2ec9ce...`; objective: 2–5 AU/UK/US cross-country leakage/freshness fixtures; acceptance: country eligibility/reward/disclosure cannot bleed across regions; dependencies: current model; safe action boundary: tests/docs; verification: cross-country fixtures; next handoff: AU/UK/US.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: S1; authority_required: tests/docs; negative_tests: AU→UK/US leakage, stale terms; receipt_evidence: country/program/version; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

### C-AFF-M-03 — destination integrity/fallback matrix
- status: PENDING; owner/workstream: Affiliate Master; exact anchor: PR #19 `ea2ec9ce...`; objective: exact program/country/outbound mapping and deterministic fallback; acceptance: mismatch/ambiguous redirect/injected URL fails closed; dependencies: active seam settled; safe action boundary: tests; verification: deterministic fixtures; next handoff: publication gate.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: non-prod tests; negative_tests: destination mismatch, unsupported redirect, injected URL; receipt_evidence: program/country/destination/disposition; green_required: conditional; prs_required: no; owner_boundary: live CTA/publication; security_disposition: PENDING.

## Affiliate AU subqueue

### C-AU-01 — publisher-affiliate proof packets
- status: PENDING; owner/workstream: Affiliate AU; exact anchor: repo `main@d3cf400a...`, AU expansion `2d654dee4e55f82f17351559f589f4889024a112`; objective: verify publisher relationship separately for Octopus Group, Pureprofile, Toluna; acceptance: member referral never mislabeled publisher affiliate; dependencies: first-party/network evidence; safe action boundary: public research; verification: source/date/route; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: research; negative_tests: referral-only != publisher affiliate; receipt_evidence: source/date/program/route; green_required: no; prs_required: no; owner_boundary: signup/contact/publication; security_disposition: PENDING.

### C-AU-02 — comparison-only negative fixtures
- status: PENDING; owner/workstream: Affiliate AU; exact anchor: `main@d3cf400a...` + current AU first-party corpus; objective: encode reward-present/referral-absent comparison-only cases including LifePoints; acceptance: no monetized referral CTA; dependencies: current evidence; safe action boundary: docs/tests; verification: publishability fixture; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: docs/tests; negative_tests: no referral route => no referral CTA; receipt_evidence: source/date/state; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

### C-AU-03 — evidence freshness table
- status: PENDING; owner/workstream: Affiliate AU; exact anchor: `main@d3cf400a...`; objective: normalize 3–8 rows for availability, eligibility, reward economics, referral route and evidence date; acceptance: stale/unknown explicit; dependencies: public evidence; safe action boundary: research/docs; verification: row audit; next handoff: Master.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: S1; authority_required: research; negative_tests: stale/conflicting terms => HOLD; receipt_evidence: source/date/field; green_required: no; prs_required: no; owner_boundary: publication/signup; security_disposition: PENDING.

## Affiliate UK subqueue

### C-UK-01 — technology vertical evidence packet
- status: ACTIVE; owner/workstream: Affiliate UK; exact anchor: `main@d3cf400aabe631dc6c2e37193eca8b192856eaba` (`docs(uk): record technology vertical slice batch`); objective: consume current technology slice and verify programme availability/reward/publisher route/disclosure/regulatory posture; acceptance: network listing never equals approval and unsupported earnings claims absent; dependencies: current evidence; safe action boundary: research/docs; verification: source matrix; next handoff: UK shortlist/Master.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research; negative_tests: regulatory/financial uncertainty => HOLD; receipt_evidence: source/date/route; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: ACTIVE.

### C-UK-02 — network route separation mini-batch
- status: PENDING; owner/workstream: Affiliate UK; exact anchor: `main@d3cf400a...` + Awin/CJ/Impact/Webgains/Tradedoubler corpus; objective: 2–5 programme/network rows separating presence from publisher eligibility/approval; acceptance: no implied partnership; dependencies: current network evidence; safe action boundary: research/docs; verification: route table; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: research; negative_tests: network presence != approval; receipt_evidence: programme/network/state; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: PENDING.

### C-UK-03 — claim-safe disclosure negatives
- status: PENDING; owner/workstream: Affiliate UK; exact anchor: `main@d3cf400a...`; objective: negative fixtures for guaranteed-income/unsupported availability/financial claims; acceptance: evidence-limited copy only; dependencies: verified source claims; safe action boundary: drafts/tests; verification: claim→source audit; next handoff: Marketing.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: draft only; negative_tests: guaranteed earnings, unsupported availability; receipt_evidence: claim/source pointer; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## Affiliate US subqueue

### C-US-01 — paid-participation / B2B proof packets
- status: ACTIVE; owner/workstream: Affiliate US; exact anchors: repo `main@d3cf400a...`, PR #6 `602b14764bb7bb263b4e0cbd9b39550f4e0bd497`; objective: verify reward value, publisher/referral route and disclosure separately for strong consumer and B2B research-tool candidates; acceptance: reward evidence != publisher eligibility, first-party rate evidence required; dependencies: public evidence; safe action boundary: research; verification: source matrix; next handoff: US shortlist.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: research; negative_tests: reward evidence != affiliate approval; receipt_evidence: source/date/program; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: ACTIVE.

### C-US-02 — destination/eligibility freshness mini-batch
- status: PENDING; owner/workstream: Affiliate US; exact anchor: PR #6 `602b1476...`; objective: verify 2–5 US eligibility/outbound routes with dates; acceptance: geo mismatch/stale terms fail closed; dependencies: public evidence; safe action boundary: research/docs; verification: dated table; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: research; negative_tests: geo mismatch, stale route; receipt_evidence: source/date/destination; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

### C-US-03 — disclosure-safe comparison rows
- status: PENDING; owner/workstream: Affiliate US; exact anchor: PR #6 `602b1476...`; objective: produce 2–5 comparison-ready non-public rows with publisher UNKNOWN explicit where appropriate; acceptance: no monetized CTA without approval; dependencies: C-US-01/02; safe action boundary: docs; verification: schema audit; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: docs; negative_tests: unknown relationship => fallback; receipt_evidence: row evidence; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## GhostKitchen subqueue

### C-GK-01 — active economics metadata seam
- status: ACTIVE; owner/workstream: GhostKitchen; exact anchors: `main@dbd64153ca3f2b0e7e9152955692f62f6c9fa59a`, PR #32 `c1892e6b5f4489b62f613f827bea3bd714275009`; objective: consume active metadata/evidence-summary work without overlap; acceptance: hypothesis/reference inputs never become verified profitability; dependencies: active PR; safe action boundary: docs/fixtures/tests; verification: evidence completeness/CI; next handoff: C-GK-02.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-12,SG-14,SG-20`; risk_class: S1; authority_required: repo/research write; negative_tests: missing input => UNKNOWN; receipt_evidence: input/source/date/class; green_required: no; prs_required: no; owner_boundary: supplier contact/spend/production; security_disposition: ACTIVE.

### C-GK-02 — provenance-labelled economics mini-batch
- status: PENDING; owner/workstream: GhostKitchen; exact anchor: `main@dbd64153...`, PR #32 seam; objective: add 2–5 recipe/yield/packaging/labour/delivery evidence records only where provenance exists and compute representative-order sensitivity; acceptance: no profitability claim; dependencies: active seam settled/non-overlap; safe action boundary: research/calculation/docs; verification: reproducible table; next handoff: readiness gate.
- security_gates: `SG-06,SG-10,SG-12,SG-14`; risk_class: S1; authority_required: local analysis/research; negative_tests: missing real input => hypothesis/UNKNOWN; receipt_evidence: assumptions/sources/results; green_required: no; prs_required: no; owner_boundary: spend/production; security_disposition: PENDING.

### C-GK-03 — fail-closed readiness fixtures
- status: PENDING; owner/workstream: GhostKitchen; exact anchor: `main@dbd64153...`; objective: deny readiness when supplier/recipe/yield/packaging/labour/delivery evidence is missing; acceptance: deterministic UNKNOWN/HOLD; dependencies: existing schema; safe action boundary: tests/fixtures; verification: fixture suite; next handoff: Overseer.
- security_gates: `SG-06,SG-10,SG-12,SG-14`; risk_class: S1; authority_required: non-prod tests; negative_tests: each missing evidence dimension; receipt_evidence: fixture/disposition; green_required: no; prs_required: no; owner_boundary: production; security_disposition: PENDING.

## Franchise subqueue

### C-FR-01 — active tenancy/territory seams
- status: ACTIVE; owner/workstream: Franchise; exact anchors: `main@0ea3b26de71f78f7eafc38cf50079805b43a7d93`, PR #24 `ac208a07c40e99ee1c1f70f67a1a857d8207fa6e`, PR #22 `7b8b07562f69ce7988f82e1f3ec71a225fb23709`; objective: preserve duplicate-membership/status/determinism fail-closed behavior without overlapping active ownership; acceptance: duplicate/overlap/inactive/stale tenant denied; dependencies: active PRs; safe action boundary: synthetic tests; verification: exact fixtures/CI; next handoff: C-FR-02.
- security_gates: `SG-06,SG-07,SG-10,SG-12,SG-14,SG-20`; risk_class: S2; authority_required: non-prod tests; negative_tests: duplicate membership, overlap, stale tenant/status; receipt_evidence: tenant/territory/version/disposition; green_required: conditional; prs_required: no; owner_boundary: production tenancy/routing; security_disposition: ACTIVE.

### C-FR-02 — isolation/overlap negatives mini-batch
- status: PENDING; owner/workstream: Franchise; exact anchor: `main@0ea3b26d...`, PR #24/#22; objective: 2–5 non-overlapping exact/partial/nested territory and A/B isolation evidence fixtures after active seam stability; acceptance: deterministic deny/route with version correlation; dependencies: active lineage stable; safe action boundary: fixtures/tests only; verification: matrix; next handoff: audit receipt.
- security_gates: `SG-09,SG-10,SG-11,SG-12,SG-14`; risk_class: S2; authority_required: non-prod tests; negative_tests: duplicate/overlap/stale version/cross-tenant; receipt_evidence: tenant/territory/version/result; green_required: conditional; prs_required: no; owner_boundary: production/persistence migration; security_disposition: PENDING.

### C-FR-03 — persistence/DB-backed tenancy completion
- status: BLOCKED; owner/workstream: Franchise; exact anchor: `main@0ea3b26d...` + PR #24 body boundary; objective: keep schema/migrations/DB-backed request context/tenant-scoped repository methods/A-B persistence isolation explicit as incomplete; acceptance: no tenancy-ready claim from synthetic resolver tests; dependencies: responsible app implementation lineage; safe action boundary: evidence/design only until owner seam available; verification: future persistence tests; next handoff: Franchise App owner.
- security_gates: `SG-02,SG-03,SG-10,SG-12,SG-14,SG-20`; risk_class: S2; authority_required: scoped non-prod app implementation when free; negative_tests: cross-tenant persistence, missing context, duplicate membership; receipt_evidence: tenant/request/store/result lineage; green_required: yes if promoted; prs_required: conditional; owner_boundary: deployment/migration/production data; security_disposition: BLOCKED.

## GemVerse subqueue

### C-GV-01 — active recovery assurance seam
- status: ACTIVE; owner/workstream: GemVerse; exact anchors: `gemverse@b36750f01f62184e2f563ff8f8030682ba10033e`, PR #10 `b1f09c3a9300a24782f5f3e4ab01619a64477319`; objective: consume existing fixture recovery assurance without duplicate implementation; acceptance: exact preimage/state hash, replay mismatch, competing-candidate denial and strict recovery schemas; dependencies: active PR; safe action boundary: fixtures/tests; verification: exact PR CI; next handoff: C-GV-03.
- security_gates: `SG-06,SG-07,SG-09,SG-10,SG-11,SG-14,SG-20`; risk_class: S2; authority_required: non-prod tests; negative_tests: stale preimage, competing candidate, replay/recovery; receipt_evidence: source/target/preimage/result; green_required: conditional; prs_required: no; owner_boundary: production mutation; security_disposition: ACTIVE.

### C-GV-02 — canon dependency packet
- status: BLOCKED; owner/workstream: GemVerse; exact anchor: `gemverse@b36750f...`; objective: separate verified creator/source canon from documentation hypothesis; acceptance: no canon-dependent executable claim absent verified source; dependencies: verified canon; safe action boundary: read/docs; verification: evidence pointers; next handoff: owner when canon exists.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-20`; risk_class: S1; authority_required: read-only; negative_tests: docs-only source cannot authorize implementation; receipt_evidence: canon source/version; green_required: no; prs_required: no; owner_boundary: product canon/production; security_disposition: BLOCKED.

### C-GV-03 — Level-2 fixture mini-batch
- status: PENDING; owner/workstream: GemVerse; exact anchor: PR #10 `b1f09c3a...`; objective: 2–5 fixture-only stale identity/recovery/competing-candidate/out-of-scope-file cases while canon is blocked; acceptance: bounded files, expected pre/postimage, rollback/replay/receipt oracle; dependencies: existing fixture only; safe action boundary: fixture docs/tests; verification: deterministic local/CI test; next handoff: AgentOS only after mutation gate clears.
- security_gates: `SG-03,SG-09,SG-10,SG-11,SG-14`; risk_class: S1; authority_required: fixture-only; negative_tests: wrong preimage/replay/out-of-scope file/competing candidate; receipt_evidence: fixture IDs/hashes; green_required: no; prs_required: no; owner_boundary: physical/production execution; security_disposition: PENDING.

## Content360 subqueue

### C-C360-01 — secret-isolation baseline
- status: VERIFIED; owner/workstream: Content360; exact historical anchor: PR #4 `6b72ea670ddeec5fe1699d8a13fa403e37d437d3`, Tests `34846314212` SUCCESS; current PR head `133dad248e56571b9c5c5d4c9fcf8b4fd63f202d`; objective: preserve opaque credential references/no secret persistence; acceptance: no secret in prompt/log/receipt/fixture; dependencies: none; safe action boundary: mocks/tests; verification: regression suite; next handoff: C-C360-02.
- security_gates: `SG-05,SG-06,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: non-prod tests; negative_tests: secret in metadata/log/result; receipt_evidence: redacted mock receipt; green_required: conditional; prs_required: no; owner_boundary: credentials/live provider/publish; security_disposition: PENDING on current head.

### C-C360-02 — current Marketing-source provenance gate
- status: ACTIVE; owner/workstream: Content360; exact anchor: PR #4 `133dad248e56571b9c5c5d4c9fcf8b4fd63f202d`, base `8dd031bb1efaf7d0909bdc411365faf3da497f84`, exact-head check-runs currently `0`; objective: fail closed on stale revision, SUPERSEDED/CONFLICTED source or hidden supersession/conflict metadata; acceptance: only exact CURRENT source revision is consumable and synthetic Marketing fixtures never become live truth; dependencies: exact-head CI; safe action boundary: mocks/tests/docs; verification: wait for exact-head CI, never borrow predecessor run; next handoff: C-C360-03 if green.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: non-prod branch tests; negative_tests: stale revision, superseded, conflict refs, hidden replacement metadata; receipt_evidence: source/revision/state/replacement/conflict/disposition; green_required: conditional; prs_required: no; owner_boundary: publication/network/account/credentials; security_disposition: PENDING_CI.

### C-C360-03 — provenance receipt + claim-strength mini-batch
- status: PENDING; owner/workstream: Content360; exact anchor: successor to PR #4 `133dad248e...` only after exact-head CI; objective: (1) deterministic non-secret provenance receipt, then (2) claim-strength guard, then 2–5 homogeneous source-version/replacement fixtures; acceptance: correlation/idempotency exact, stale/conflicting source cannot yield successful optimization or stronger claim, no publication authority; dependencies: C-C360-02 exact-head success and fresh no-concurrency scan; safe action boundary: mocks/tests; verification: exact-head CI; next handoff: Marketing/adapter evidence.
- security_gates: `SG-05,SG-06,SG-07,SG-09,SG-10,SG-11,SG-14,SG-15,SG-17`; risk_class: S2; authority_required: mock tests; negative_tests: duplicate, timeout, replay, mismatch, unsupported claim strengthening, stale replacement; receipt_evidence: request/source/result/provenance IDs/status; green_required: conditional; prs_required: no; owner_boundary: live provider/publish/network; security_disposition: PENDING.

### C-C360-04 — official API/auth capability evidence
- status: BLOCKED; owner/workstream: Content360; exact anchor: PR #4 `133dad248e...` remains mock-only, issue #1/live capabilities unresolved; objective: keep live API/auth/PUBLISH/SCHEDULE capabilities UNKNOWN until official evidence/owner authority; acceptance: no inference from mocks; dependencies: official docs/owner later; safe action boundary: public docs research only; verification: official documentation; next handoff: owner if account/credential action becomes necessary.
- security_gates: `SG-02,SG-05,SG-06,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public docs only; negative_tests: mock capability != live authority; receipt_evidence: official docs/date/capability; green_required: no; prs_required: no; owner_boundary: credentials/account/live publish; security_disposition: BLOCKED.

## Commercial Frontend subqueue

### C-CF-01 — active Tradie value-threshold seam
- status: ACTIVE; owner/workstream: Commercial Frontend; exact anchor: Overseer PR #50 `6391a64728faae7352b4ce5fd7dfe9903fd7377b`, issue #21; objective: consume interpretation-only value work while pain/frequency/integration/authority/value/WTP remain externally gated; acceptance: synthetic arithmetic never becomes demand/WTP proof; dependencies: active PR; safe action boundary: docs/fixtures/prototype; verification: evidence packet/tests; next handoff: C-CF-02.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-12,SG-14,SG-20`; risk_class: S1; authority_required: non-prod docs/prototype; negative_tests: internal hypothesis != demand proof; receipt_evidence: claim/evidence source; green_required: no; prs_required: no; owner_boundary: customer contact/deployment; security_disposition: ACTIVE.

### C-CF-02 — operator evidence gap register
- status: PENDING; owner/workstream: Commercial Frontend; exact anchor: PR #50 `6391a647...`, issue #21; objective: prioritize direct operator frequency/friction/consequence/authority/WTP gaps over more synthetic feasibility; acceptance: no commercial-ready/build-ready claim; dependencies: current evidence; safe action boundary: research synthesis only, no outreach; verification: evidence-gap table; next handoff: future owner-authorized validation.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-20`; risk_class: S0; authority_required: read/research; negative_tests: internal assumptions cannot become WTP evidence; receipt_evidence: source/gap/date; green_required: no; prs_required: no; owner_boundary: customer contact; security_disposition: PENDING.

### C-CF-03 — bounded exception-workflow fixture
- status: PENDING; owner/workstream: Commercial Frontend; exact anchor: PR #50 `6391a647...`; objective: one Tradie/service-ops exception input→recommended correction→receipt with no production action; acceptance: measurable time/error/value hypothesis explicit; dependencies: active seam stable; safe action boundary: synthetic artifact; verification: fixture walkthrough; next handoff: integration feasibility only after evidence.
- security_gates: `SG-06,SG-10,SG-11,SG-12,SG-14`; risk_class: S1; authority_required: non-prod prototype/docs; negative_tests: unsupported correction/authority escalation; receipt_evidence: input/correction/result; green_required: no; prs_required: no; owner_boundary: deployment/account mutation; security_disposition: PENDING.

## Marketing subqueue

### C-MKT-01 — AgentOS claim/readiness reconciliation
- status: ACTIVE; owner/workstream: Marketing; exact anchors: Overseer `main@98db9d3887c24432f25484f077cbd393fd05b210` pre-checkpoint, AgentOS PR #104 `7f84f4f3...` / `34866176685`, PR #111 `352c83fd...` / `34863648579`; objective: keep product-direction/marketing claims distinct from shipped Level-2/security/PRS status; acceptance: no shipped/Level-2-ready/overall-GREEN claim while SG-08/SG-01/02/SG-18 remain open; dependencies: exact AgentOS evidence; safe action boundary: internal copy/docs; verification: claim→evidence pointer; next handoff: internal assets only.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: internal drafts; negative_tests: shipped/ready claim without evidence; receipt_evidence: claim/evidence IDs; green_required: no; prs_required: no; owner_boundary: campaign/publication/spend; security_disposition: ACTIVE.

### C-MKT-02 — Marketing→Content360 provenance handoff
- status: PENDING; owner/workstream: Marketing; exact anchors: Overseer M-A035/M-A036/M-A037 movement on `98db9d38...`, Content360 PR #4 `133dad248e...`; objective: provide source revision/state/claim/evidence-class pointers compatible with Content360’s stale/conflict gate without treating prepared assets as approved/live truth; acceptance: superseded/conflicted/stale source suppressed; dependencies: C-C360-02 exact-head CI then stable contract; safe action boundary: internal docs/fixtures; verification: pointer audit; next handoff: Content360.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: internal docs; negative_tests: stale/superseded/conflicted source, unsupported claim strength; receipt_evidence: source/revision/state/claim/evidence pointer; green_required: no; prs_required: no; owner_boundary: publication/campaign/spend; security_disposition: PENDING.

### C-MKT-03 — commerce + affiliate claim-evidence mini-batch
- status: PENDING; owner/workstream: Marketing; exact anchors: GSC `79d50227...` with `0 eBay-ready SKUs`, Affiliate `main@d3cf400a...` / PR #6 `602b1476...`; objective: 2–5 internal claim templates mapping SKU/reward/referral/publisher/disclosure claims to exact evidence; acceptance: missing freight/stock/permission or unknown publisher state suppresses claim; dependencies: project evidence; safe action boundary: internal drafts; verification: negative-copy/pointer audit; next handoff: Content360 only after project qualification.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: internal drafts; negative_tests: unsupported approved-supplier/eBay-ready/partner/reward claim; receipt_evidence: claim/source/date/country/SKU; green_required: no; prs_required: no; owner_boundary: publication/outreach/campaign/spend; security_disposition: PENDING.

## Lane health after replenishment
- **Lane A:** A-AG-05 and A-PRS-03 frontend half are immediately useful PENDING work; SG-08 ownership, SG-01/02 admission and physical-host blockers remain explicit. A-AG-04 is VERIFIED only for bounded receipt reload/provenance, not Level-2 readiness.
- **Lane B:** multiple useful PENDING items remain across GSC economics/matrix, eBay receipt semantics, Amazon freshness, Headless synthetic handoff and MyPrime provider/presentation work. External permission/freight/provider/live-environment blockers do not starve safe closure.
- **Lane C:** every scheduled workstream has actionable PENDING work or an explicit blocker. Active PR ownership is preserved. Content360 remains ACTIVE/CI-pending on exact `133dad248e...`; no predecessor CI is borrowed.

**No overall GREEN.**