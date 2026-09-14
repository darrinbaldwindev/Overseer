# Portfolio Execution Batch Manifest

**Purpose:** queue state only for the fixed scheduled portfolio lanes. Canonical execution procedure: `.overseer/doctrine/PORTFOLIO-BATCH-ENGINE.md`. Project shaping: `.overseer/profiles/PROJECT-BATCH-PROFILES.md`. Security: `.overseer/security/AGENTOS-SECURITY-GATE-MATRIX.md`. Exact repository/issue/CI/runtime evidence always outranks this manifest.

**Fixed lanes:** A = AgentOS Level 2 P0 + PRS/Green assurance-adjacent work; B = GlobalShopCo/Headless/eBay/Amazon/MyPrimeDelivery; C = Affiliate-Websites AU/UK/US/Master, GhostKitchen, Franchise, GemVerse, Content360, Commercial Frontend, Marketing.

**States:** `PENDING | ACTIVE | VERIFIED | BLOCKED | STALE | SPLIT_REQUIRED`.

**Core invariant:** **NO MODEL DECIDES ITS OWN AUTHORITY.** Functional state, security state and PRS state remain separate. No merge/approve/ready/rebase/deploy/credentials/security-policy changes/production writes/purchases/spend/supplier contact/live publication/physical owner-host action/production autonomy.

## Checkpoint reconciliation — 2026-09-15 01:30 Brisbane
- Previous durable checkpoint: Overseer #49 `5665738982`; previous manifest blob `24a8830985ce076855db7c43a4967315043c4b3a`.
- Canonical batch engine, central project profiles and security matrix were re-read first; queue text was treated as hypothesis only.
- AgentOS PR #104 advanced materially since the prior checkpoint. Current evidenced lineage is OPEN/DRAFT/UNMERGED at `bbfee5221652c9bf0551ce5b31eb0b1cf6e78af1`; exact-head Tests `34857161932` SUCCESS. The bounded authority-receipt provenance slice is functionally exact-head verified, but SG-08 continuous ownership and SG-01/02 authenticated actor/canonical grant binding remain BLOCKED. No current exact-lineage Green/PRS promotion evidence closes those gates.
- AgentOS PR #111 POSIX lifecycle failure was reproduced, diagnosed as readiness being published before signal-handler registration, and repaired. Current post-concurrency head `429b6d5bc14b2790f1a9bace09b76e699cb88b8c`; exact-head Tests `34859721665` SUCCESS on Ubuntu + Windows. Functional lifecycle/readiness projection is VERIFIED on that head; security remains PENDING SG-18.
- Local-wake correlation remains narrowly VERIFIED at `a69562dfe19696b79474c1a3f01a10d67b8d8e90`; runs `34849679000`,`34849679095` SUCCESS. It does not close SG-08 or SG-01/02.
- Shopify→eBay synthetic conflict/replay lineage remains exact `8d891d782dca6799a9a4d942218fde441685e5dc` / `34856089804` SUCCESS. Real SKU readiness remains fail-closed on upstream commercial evidence.
- Shopify→Amazon synthetic compound-conflict lineage remains exact `0b52631e9a3f084d9b947227c84e7f656ebab6f5` / `34856135125` SUCCESS. Synthetic success does not establish seller/listing authority.
- GlobalShopCo default remains `79d50227fe19826d42c43e7dec15ce245ad58e40`; PR #29/#30 own current shelf/OXO research surfaces. `0 eBay-ready SKUs` remains controlling; do not duplicate active research.
- GlobalShopCo-Headless deterministic branch remains `agent/chatgpt/m3-baseline@44552d2a94dcea1445dddeb2d8a853d6d2b34d3e`; live dev-store/browser checkout proof remains externally blocked.
- MyPrimeDelivery advanced from Batch 009 baseline `f8fcce2d80ddc5955f08c020e159e440c2da2338` to exact `9b41ebbf49732d31ef3dc428636ecf31169f20c4`; Fixture validation `34860891240` SUCCESS. Identity assurance now covers 101 evidence rows -> 100 normalized-title concepts with one preserved duplicate pair and all 12 launch categories. Live authoritative Prime/rank/deal rights remain UNKNOWN; 0 live QUALIFIED products remains truthful.
- Lane C active ownership seams remain: Affiliate Master PR #17/#19, GhostKitchen PR #32, Franchise PR #24/#22, GemVerse PR #10, Content360 PR #4, Commercial Frontend PR #50. Marketing remains internal/non-public and evidence-bounded. No duplicate work is assigned onto those seams.
- Historical evidence remains preserved by exact prior manifest blob/commit history and durable #49 checkpoints; narrow predecessor heads/runs below remain valid only for their recorded scope and are never transferred to successor heads.

# LANE A — AgentOS Level 2 P0

## AgentOS Overseer subqueue

### A-AG-01 — continuous project-file ownership fence
- status: BLOCKED; owner/workstream: AgentOS / writer ownership; exact anchor: PR #104 `bbfee5221652c9bf0551ce5b31eb0b1cf6e78af1`, Tests `34857161932`, PRS stale-owner baseline `0defebe26f71e1cf5df1168fa5454bfd8de30091` / `34821646371`.
- objective: hold one crash-releasing kernel-enforced ownership fence continuously from final verification through publish/prepared recovery and durable success receipt; acceptance: replacement-after-verify, successor/three-writer, stale owner, TOCTOU, crash/replay, duplicate mutation/result and prepared-recovery stale-owner all fail closed on exact Ubuntu+Windows lineage; dependencies: real writer implementation change; safe action boundary: non-prod draft branch code/tests only; verification: adversarial ownership matrix + exact-head CI; next handoff: Green then PRS only on identical repaired lineage.
- security_gates: `SG-03,SG-08,SG-09,SG-10,SG-11,SG-14,SG-18,SG-19`; risk_class: S2; authority_required: scoped non-prod branch/test write; negative_tests: ownership matrix above; receipt_evidence: actor/task/file/pre-postimage/ownership/result lineage; green_required: yes; prs_required: yes; owner_boundary: merge/deploy/physical production; security_disposition: BLOCKED.

### A-AG-02 — authenticated actor + canonical grant binding
- status: BLOCKED; owner/workstream: AgentOS / authority admission; exact anchor: PR #104 `bbfee522...` + canonical authority dependency contract.
- objective: bind an existing authenticated actor source and canonical grant resolver without creating a second authority source/registry; acceptance: payload/host cannot self-supply identity/grant and missing/spoofed/mismatched/cross-project/replayed grant yields zero artifact/no success receipt; dependencies: real bindable canonical source; safe action boundary: architecture discovery + bounded branch tests; verification: provenance + spoof/mismatch/replay matrix; next handoff: AgentOS architecture/implementation.
- security_gates: `SG-01,SG-02,SG-03,SG-04,SG-09,SG-10,SG-11,SG-18,SG-19`; risk_class: S2; authority_required: canonical identity/grant read + scoped branch tests; negative_tests: host-as-auth, spoof actor, payload self-grant, absent/mismatch/cross-project/replay; receipt_evidence: issuer/source/version/request/task/mission; green_required: yes; prs_required: yes; owner_boundary: credentials/security policy; security_disposition: BLOCKED.

### A-AG-03 — Basic Chat POSIX lifecycle/readiness repair
- status: VERIFIED; owner/workstream: AgentOS / Basic Chat lifecycle; exact anchor: PR #111 `429b6d5bc14b2790f1a9bace09b76e699cb88b8c`, Tests `34859721665` SUCCESS; repair origin `7674513bcf733e423f992087865cd8125d89f6b6` / `34859603641` SUCCESS.
- objective: preserve signal handlers before readiness publication and cross-platform lock-removal semantics; acceptance: Ubuntu full suite/audit + Windows lifecycle green, no fabricated readiness, no secret/raw/PRS/recovery leakage; dependencies: none; safe action boundary: tests/small lifecycle code only; verification: exact-head CI; next handoff: A-PRS-04/Green SG-18 sample.
- security_gates: `SG-03,SG-05,SG-10,SG-11,SG-14,SG-18`; risk_class: S2; authority_required: scoped branch code/tests; negative_tests: immediate SIGINT, stale lock, fabricated readiness, correlation/leakage; receipt_evidence: exact head/run/jobs; green_required: yes; prs_required: no unless scope widens; owner_boundary: merge/deploy/runtime enablement; security_disposition: PENDING.

### A-AG-04 — authority-evidence receipt persistence/reload/recovery
- status: PENDING; owner/workstream: AgentOS / receipt provenance; exact anchor: PR #104 `bbfee522...` / `34857161932` bounded authority-receipt slice.
- objective: prove `authority_evidence_id` survives existing receipt persistence/reload/recovery without broadening generic receipt authority; acceptance: exact ID retained, stale/mismatched/missing ID cannot normalize to success, no duplicate persistence system; dependencies: current existing receipt schema only; safe action boundary: non-prod tests/small branch fix; verification: restart/reload/recovery fixtures + exact-head CI; next handoff: Green SG-18 if exact lineage remains unchanged.
- security_gates: `SG-02,SG-09,SG-10,SG-11,SG-14,SG-18`; risk_class: S2; authority_required: scoped branch tests; negative_tests: missing/stale/mismatch/cross-task authority evidence; receipt_evidence: authority evidence ID + request/task/result/receipt lineage; green_required: yes; prs_required: conditional; owner_boundary: merge/deploy; security_disposition: PENDING.

### A-AG-05 — receipt replay/correlation adjacency
- status: PENDING; owner/workstream: AgentOS / receipt correlation; exact anchor: successor of A-AG-04 only after fresh scan.
- objective: add only homogeneous replay/correlation regressions around the existing receipt primitive; acceptance: duplicate result write, replayed receipt, cross-task/cross-mission correlation mismatch and stale receipt fail closed; dependencies: A-AG-04 stable schema; safe action boundary: tests only unless minimal defect found; verification: exact-head CI; next handoff: Green/PRS based on actual risk widening.
- security_gates: `SG-09,SG-10,SG-11,SG-14,SG-18`; risk_class: S2; authority_required: scoped tests; negative_tests: replay, duplicate result, cross-task/cross-mission, stale receipt; receipt_evidence: immutable IDs/hashes/disposition; green_required: yes; prs_required: conditional; owner_boundary: merge/deploy; security_disposition: PENDING.

### A-AG-06 — local-wake correlation preservation
- status: VERIFIED; owner/workstream: AgentOS / local-wake; exact anchor: `a69562dfe19696b79474c1a3f01a10d67b8d8e90`, runs `34849679000`,`34849679095` SUCCESS.
- objective: preserve task→response→event mission/wake identity; acceptance: mismatch/replay cannot normalize into success; dependencies: none; safe action boundary: regression tests only; verification: exact regression + workflow; next handoff: sample only if surface changes.
- security_gates: `SG-09,SG-10,SG-11,SG-14,SG-18`; risk_class: S2; authority_required: branch tests; negative_tests: mission/wake mismatch, cross-task response, replay drift; receipt_evidence: exact head/two runs/identities; green_required: yes before promotion; prs_required: conditional; owner_boundary: merge/deploy; security_disposition: PENDING.

### A-AG-07 — physical Windows acceptance packet
- status: BLOCKED; owner/workstream: AgentOS / physical host acceptance; exact anchor: current PR #104 lineage + unresolved A-AG-01/A-AG-02.
- objective: maintain an exact owner-run acceptance packet only after software/security blockers clear; acceptance: exact SHA/root/mutation/recovery/correlation/no-production boundaries; dependencies: SG-08 + SG-01/02 closure + explicit owner physical authority; safe action boundary: checklist/evidence packet only; verification: future physical evidence; next handoff: owner/physical-host lane.
- security_gates: `SG-03,SG-08,SG-10,SG-11,SG-14,SG-18,SG-20`; risk_class: S2; authority_required: owner-authorized physical Windows action; negative_tests: wrong head, prod root, missing receipt; receipt_evidence: head/host/root/test/result; green_required: yes; prs_required: yes if promoted; owner_boundary: physical Windows execution; security_disposition: BLOCKED.

## PRS / Green assurance subqueue

### A-PRS-01 — immutable stale-owner false-GREEN baseline
- status: VERIFIED; owner/workstream: PRS; exact anchor: PRS `0defebe26f71e1cf5df1168fa5454bfd8de30091` / `34821646371` against historical AgentOS `83a58b8...`.
- objective: preserve immutable defect baseline without transferring outcome to successor heads; acceptance: target/artifact identity exact; dependencies: none; safe action boundary: read-only assurance; verification: hashes; next handoff: A-AG-01.
- security_gates: `SG-08,SG-10,SG-11,SG-19`; risk_class: S0; authority_required: read-only; negative_tests: normal publish + prepared recovery stale-owner; receipt_evidence: immutable hashes; green_required: no; prs_required: baseline; owner_boundary: none; security_disposition: VERIFIED.

### A-PRS-02 — successor ownership challenge
- status: BLOCKED; owner/workstream: PRS; exact anchor: A-PRS-01/A-AG-01.
- objective: rerun full ownership matrix only after real AgentOS writer repair and identical-head Green PASS; acceptance: normal/prepared/successor/crash/replay independently classified; dependencies: A-AG-01 + exact CI + Green; safe action boundary: assurance harness; verification: immutable target/artifact hashes; next handoff: Overseer.
- security_gates: `SG-08,SG-09,SG-10,SG-11,SG-19`; risk_class: S2; authority_required: bounded harness; negative_tests: full ownership matrix; receipt_evidence: target/artifact hash; green_required: yes prerequisite; prs_required: yes; owner_boundary: merge/deploy; security_disposition: BLOCKED.

### A-PRS-03 — admission false-GREEN challenge
- status: BLOCKED; owner/workstream: PRS; exact anchor: A-AG-02.
- objective: independently prove spoof/missing/mismatch/self-grant paths cannot produce success after canonical admission exists; acceptance: identical Green-passed head; dependencies: A-AG-02; safe action boundary: synthetic assurance; verification: immutable target + adversarial fixtures; next handoff: Overseer.
- security_gates: `SG-01,SG-02,SG-10,SG-11,SG-19`; risk_class: S2; authority_required: bounded harness; negative_tests: spoof/missing/mismatch/cross-project/replay/self-grant; receipt_evidence: exact target + outcome; green_required: yes prerequisite; prs_required: yes; owner_boundary: none; security_disposition: BLOCKED.

### A-PRS-04 — PR #111 false-readiness / evidence-leakage sample
- status: PENDING; owner/workstream: Green first, PRS conditional; exact anchor: PR #111 `429b6d5b...` / `34859721665` SUCCESS.
- objective: challenge fabricated completion/readiness and evidence leakage without treating UI availability as Level-2 authority; acceptance: missing/mismatched evidence cannot display readiness and secret/raw/PRS/recovery fields remain excluded; dependencies: exact head stable; safe action boundary: test/read only; verification: exact-head negatives; next handoff: AgentOS Overseer.
- security_gates: `SG-05,SG-10,SG-11,SG-14,SG-18`; risk_class: S1; authority_required: read/test only; negative_tests: fabricated completion, stale evidence, correlation mismatch, leakage; receipt_evidence: exact head/run/test names; green_required: yes; prs_required: no unless scope widens; owner_boundary: merge/deploy; security_disposition: PENDING.

# LANE B — Commerce

## GlobalShopCo subqueue

### B-GSC-01 — consume active PR #29/#30 evidence
- status: ACTIVE; owner/workstream: GlobalShopCo product qualification; exact anchor: default `79d50227fe19826d42c43e7dec15ce245ad58e40`, PR #29 shelf organisers, PR #30 OXO source hunt, `0 eBay-ready SKUs` controlling.
- objective: reconcile exact SKU/GTIN, authenticated/public buy cost class, freight, marketplace permission, stock/fulfilment, AU/eBay comp floor and returns/warranty; acceptance: each row promoted/rejected/HOLD with explicit missing field; dependencies: active PR ownership; safe action boundary: research/docs/tests only; verification: source/date/identity/economics table; next handoff: eBay/Amazon gates.
- security_gates: `SG-02,SG-03,SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public/read-only evidence; negative_tests: missing freight/permission/stock/seller/fee => HOLD; receipt_evidence: exact source/date/SKU/economics; green_required: no; prs_required: no; owner_boundary: supplier contact/purchase/publication; security_disposition: ACTIVE.

### B-GSC-02 — current-leader exact-SKU economics re-screen
- status: PENDING; owner/workstream: GlobalShopCo product economics; exact anchor: prior CARLA `V178-36336` lineage + PR #29/#30 current candidates.
- objective: refresh exact AU/eBay comps, weight/freight and max-buy-cost ceiling for one non-overlapping candidate at a time; acceptance: deterministic commercial disposition with permission/evidence UNKNOWNs explicit; dependencies: current public evidence; safe action boundary: read-only research/calculation; verification: reproducible calculator inputs; next handoff: pilot matrix.
- security_gates: `SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public read-only; negative_tests: stale comp, unknown freight/permission => HOLD; receipt_evidence: sources/date/calculation; green_required: no; prs_required: no; owner_boundary: supplier contact/purchase; security_disposition: PENDING.

### B-GSC-03 — comparison-ready 5–10 row pilot matrix
- status: PENDING; owner/workstream: GlobalShopCo / commercial matrix; exact anchor: B-GSC-01/02 outputs.
- objective: normalize only evidence-complete/rejected/HOLD rows; acceptance: supplier/SKU/GTIN where available, wholesale/landed, comps, freight/free-delivery contribution, permission, stock model, returns/warranty, fee basis and disposition present; dependencies: active research outputs; safe action boundary: docs/calculation only; verification: schema completeness + calculator; next handoff: channel gates.
- security_gates: `SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read/docs; negative_tests: missing material field cannot promote; receipt_evidence: row-level evidence pointers; green_required: no; prs_required: no; owner_boundary: publication/spend/contact; security_disposition: PENDING.

## Shopify→eBay subqueue

### B-EBAY-01 — synthetic replay/conflict baseline
- status: VERIFIED; owner/workstream: Shopify→eBay; exact anchor: `8d891d782dca6799a9a4d942218fde441685e5dc` / Fixture validation `34856089804` SUCCESS.
- objective: preserve event-ID/payload conflict denial and benign exact replay duplicate semantics with zero network/publication authority; acceptance: altered replay fails closed; dependencies: none; safe action boundary: synthetic fixtures; verification: exact-head CI; next handoff: B-EBAY-02.
- security_gates: `SG-02,SG-03,SG-09,SG-10,SG-11,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: non-prod branch/test; negative_tests: altered replay, stale event, correlation mismatch; receipt_evidence: event/payload hash/disposition; green_required: no for synthetic; prs_required: no; owner_boundary: network/publication; security_disposition: VERIFIED.

### B-EBAY-02 — receipt persistence/correlation semantics
- status: PENDING; owner/workstream: Shopify→eBay; exact anchor: B-EBAY-01 lineage.
- objective: inspect existing persistence first, then prove replay cannot overwrite accepted identity or create duplicate durable result; acceptance: same event+same payload idempotent, same event+different payload denied, result/receipt correlation exact, no second persistence/control plane; dependencies: existing schema support; safe action boundary: fixtures/tests/small fix only; verification: exact-head CI + restart/replay if supported; next handoff: channel assurance.
- security_gates: `SG-09,SG-10,SG-11,SG-14,SG-15`; risk_class: S2; authority_required: non-prod tests; negative_tests: restart replay, duplicate result write, mismatched receipt identity; receipt_evidence: event/payload/result/receipt lineage; green_required: conditional; prs_required: no; owner_boundary: publication/network; security_disposition: PENDING.

### B-EBAY-03 — real SKU readiness gate
- status: BLOCKED; owner/workstream: Shopify→eBay commercial readiness; exact anchor: `0 eBay-ready SKUs`, GlobalShopCo PR #29/#30 active evidence.
- objective: consume only rows with marketplace permission, compliant fulfilment/stock, exact freight/economics, seller/fee evidence; acceptance: no publication-ready classification with any missing material field; dependencies: B-GSC-03; safe action boundary: read-only preflight; verification: evidence packet; next handoff: owner only if a strong row is blocked solely on owner-gated evidence.
- security_gates: `SG-02,SG-03,SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read-only; negative_tests: missing permission/freight/seller/fee/stock => HOLD; receipt_evidence: SKU evidence packet; green_required: no; prs_required: no; owner_boundary: listing/account/contact/spend; security_disposition: BLOCKED.

## Shopify→Amazon subqueue

### B-AMZ-01 — compound-conflict synthetic baseline
- status: VERIFIED; owner/workstream: GlobalShopCo / Amazon fixtures; exact anchor: `0b52631e9a3f084d9b947227c84e7f656ebab6f5`, Amazon gate `34856135125` SUCCESS.
- objective: preserve fail-closed permission/stock/category/identifier/fulfilment/fee/source conflicts while Shopify remains canonical; acceptance: compound conflicts deny; dependencies: none; safe action boundary: synthetic tests; verification: exact-head CI; next handoff: B-AMZ-02.
- security_gates: `SG-02,SG-03,SG-09,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: non-prod tests; negative_tests: compound conflicts; receipt_evidence: exact head/run/conflict code; green_required: no for synthetic; prs_required: no; owner_boundary: seller setup/listing/credentials; security_disposition: VERIFIED.

### B-AMZ-02 — evidence freshness/version/correlation denial
- status: PENDING; owner/workstream: GlobalShopCo / Amazon fixtures; exact anchor: B-AMZ-01, only if current schema already exposes evidence version/freshness.
- objective: deny stale/version-mismatched/cross-SKU evidence without inventing authority semantics; acceptance: stale/mismatched source evidence cannot pass preflight, absent schema => SPLIT_REQUIRED; dependencies: schema inspection; safe action boundary: tests/small compatible fix; verification: exact-head CI; next handoff: Amazon gate.
- security_gates: `SG-06,SG-09,SG-10,SG-11,SG-14`; risk_class: S2; authority_required: non-prod tests; negative_tests: stale source, mismatched version, cross-SKU evidence; receipt_evidence: source/version/SKU/disposition; green_required: conditional; prs_required: no; owner_boundary: credentials/listing; security_disposition: PENDING.

### B-AMZ-03 — real Amazon readiness
- status: BLOCKED; owner/workstream: GlobalShopCo / Amazon AU; exact anchor: synthetic fixture lineage only, no owner-authorized seller/provider evidence.
- objective: keep seller-of-record, permission, variant/stock, category/GTIN, fulfilment and fees/economics UNKNOWN until authoritative evidence exists; acceptance: no live-ready status from fixtures; dependencies: owner/account evidence later; safe action boundary: read-only research; verification: authoritative evidence packet; next handoff: owner if only gated account evidence remains.
- security_gates: `SG-02,SG-03,SG-06,SG-10,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read-only; negative_tests: missing seller/permission/category/fee => HOLD; receipt_evidence: evidence packet; green_required: no; prs_required: no; owner_boundary: seller account/credentials/listing; security_disposition: BLOCKED.

## GlobalShopCo-Headless subqueue

### B-HDL-01 — deterministic storefront contract baseline
- status: VERIFIED; owner/workstream: Headless; exact anchor: `agent/chatgpt/m3-baseline@44552d2a94dcea1445dddeb2d8a853d6d2b34d3e`, default `c3e2960961fd60ef33ddb531577173fd3ff7cb17`.
- objective: preserve Shopify product identity/cart/checkout host integrity and parser/host-confusion denial; acceptance: no local duplicate catalogue/order authority; dependencies: none; safe action boundary: tests; verification: deterministic suite; next handoff: B-HDL-02.
- security_gates: `SG-02,SG-03,SG-05,SG-06,SG-10,SG-14,SG-20`; risk_class: S2; authority_required: non-prod tests; negative_tests: host confusion, malformed destination, secret leakage; receipt_evidence: exact branch/tests; green_required: conditional; prs_required: no; owner_boundary: deployment/secrets/live purchase; security_disposition: VERIFIED.

### B-HDL-02 — evidence-qualified synthetic product handoff
- status: PENDING; owner/workstream: Headless; exact anchor: current deterministic lineage + GlobalShopCo evidence matrix.
- objective: prove retrieval→render→Shopify checkout URL handoff using an evidence-qualified synthetic fixture, not a live promotion; acceptance: exact product identity survives render/handoff, checkout host canonical, unavailable product cannot display purchasable; dependencies: suitable fixture; safe action boundary: local/dev tests; verification: integration fixture; next handoff: B-HDL-03.
- security_gates: `SG-03,SG-05,SG-06,SG-10,SG-14`; risk_class: S2; authority_required: non-prod tests; negative_tests: wrong product/variant, unavailable item, host substitution; receipt_evidence: fixture/result; green_required: conditional; prs_required: no; owner_boundary: deployment/live purchase; security_disposition: PENDING.

### B-HDL-03 — live dev-store/browser proof
- status: BLOCKED; owner/workstream: Headless; exact anchor: current default/work branch.
- objective: preserve real non-production browser checkout proof as external gate; acceptance: actual dev-store + owner-authorized access + exact product handoff; dependencies: owner/environment; safe action boundary: no action now; verification: future browser evidence; next handoff: owner/environment.
- security_gates: `SG-03,SG-05,SG-10,SG-14,SG-20`; risk_class: S2; authority_required: owner-authorized non-prod environment; negative_tests: prod host, wrong store, missing access; receipt_evidence: environment/product/URL/result; green_required: yes if promoted; prs_required: no; owner_boundary: access/deployment/purchase; security_disposition: BLOCKED.

## MyPrimeDelivery subqueue

### B-MPD-01 — Batch 009 identity assurance closure
- status: VERIFIED; owner/workstream: MyPrimeDelivery; exact anchor: `agent/overseer/initial-project-timeline@9b41ebbf49732d31ef3dc428636ecf31169f20c4`, Fixture validation `34860891240` SUCCESS; baseline Batch 009 `f8fcce2d80ddc5955f08c020e159e440c2da2338` / `34856148612` SUCCESS.
- objective: preserve current 101 evidence rows -> 100 normalized-title concepts, one duplicate pair, all 12 launch categories, 0 live QUALIFIED; acceptance: no ASIN guessing and unresolved identity stays fail-closed; dependencies: none; safe action boundary: tests/docs; verification: exact-head CI; next handoff: B-MPD-02.
- security_gates: `SG-02,SG-03,SG-05,SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: non-prod repo tests; negative_tests: title-only != verified identity, duplicate observation != merged ASIN; receipt_evidence: corpus/head/counts; green_required: no for bounded fixture; prs_required: no; owner_boundary: provider signup/credentials/publication; security_disposition: VERIFIED.

### B-MPD-02 — provider evidence identity/freshness negatives
- status: PENDING; owner/workstream: MyPrimeDelivery; exact anchor: B-MPD-01 current schema.
- objective: test ASIN/marketplace/variant/freshness mismatch denial using provider-neutral fixtures already supported; acceptance: stale/mismatched evidence fails closed and source rights stay separate from product truth; dependencies: existing adapter schema; safe action boundary: synthetic tests only; verification: exact-head test output; next handoff: qualification funnel.
- security_gates: `SG-06,SG-09,SG-10,SG-11,SG-14`; risk_class: S2; authority_required: non-prod tests; negative_tests: ASIN mismatch, marketplace mismatch, stale provider, variant conflict; receipt_evidence: source/version/product/disposition; green_required: conditional; prs_required: no; owner_boundary: live provider credentials; security_disposition: PENDING.

### B-MPD-03 — qualification funnel metrics
- status: PENDING; owner/workstream: MyPrimeDelivery; exact anchor: Batch 009/`9b41ebbf...` corpus.
- objective: count identity-resolved / rights-known / Prime-current / rank/deal-current / outbound-destination-ready candidates while preserving UNKNOWN; acceptance: reproducible funnel and unresolved families list; dependencies: current corpus; safe action boundary: analysis/docs; verification: deterministic counts; next handoff: WordPress presentation.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: read/docs; negative_tests: missing authority never promoted; receipt_evidence: corpus head + metric table; green_required: no; prs_required: no; owner_boundary: affiliate/provider account/publication; security_disposition: PENDING.

### B-MPD-04 — WordPress evidence-safe presentation fixture
- status: PENDING; owner/workstream: MyPrimeDelivery; exact anchor: B-MPD-03 funnel output + established `docs/overseer/batches/` lineage.
- objective: render only evidence-safe category/product cards with unresolved Prime/rank/deal state visibly non-qualified; acceptance: no live-deal/Prime claim without current authoritative provider evidence and outbound destination must remain explicit; dependencies: B-MPD-03; safe action boundary: non-public fixture/docs; verification: fixture snapshot/schema audit; next handoff: Marketing only after qualification.
- security_gates: `SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: non-public docs/fixture; negative_tests: stale deal, unknown Prime, unresolved destination; receipt_evidence: product/evidence/display state; green_required: no; prs_required: no; owner_boundary: publication/provider signup; security_disposition: PENDING.

# LANE C — Growth / verticals

## Affiliate-Websites Master subqueue

### C-AFF-M-01 — publication-state/CTA evidence contract
- status: ACTIVE; owner/workstream: Affiliate Master; exact anchor: draft PR #17 publication-state wiring + PR #19 `ea2ec9ce6ced26c4841d080abb4403193f299519` identity/destination lineage.
- objective: ensure UNKNOWN/non-affiliate relationships never emit monetized CTA; acceptance: fallback/non-monetized behavior deterministic and destination identity exact; dependencies: existing PR ownership; safe action boundary: branch tests/docs; verification: fixtures; next handoff: country lanes.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: non-prod branch tests; negative_tests: unknown relationship, stale destination, injected CTA; receipt_evidence: program/country/state/destination; green_required: conditional; prs_required: no; owner_boundary: signup/publication; security_disposition: ACTIVE.

### C-AFF-M-02 — country config separation
- status: PENDING; owner/workstream: Affiliate Master; exact anchor: current shared repo/model lineage.
- objective: keep AU/UK/US terms out of global canon unless explicitly global; acceptance: country eligibility/reward/disclosure fields cannot leak across regions; dependencies: Master model; safe action boundary: tests/docs; verification: cross-country fixtures; next handoff: AU/UK/US.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: S1; authority_required: repo tests/docs; negative_tests: AU→UK/US leakage, stale terms; receipt_evidence: country/program/version; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

### C-AFF-M-03 — destination integrity/fallback matrix
- status: PENDING; owner/workstream: Affiliate Master; exact anchor: PR #19 lineage + C-AFF-M-01.
- objective: preserve exact program/country/outbound mapping and deterministic non-monetized fallback; acceptance: mismatch/redirect ambiguity fails closed; dependencies: active PR ownership must be consumed first; safe action boundary: tests only; verification: deterministic fixtures; next handoff: publication gate.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: non-prod tests; negative_tests: destination mismatch, unsupported redirect, injected URL; receipt_evidence: program/country/destination/disposition; green_required: conditional; prs_required: no; owner_boundary: live CTA/publication; security_disposition: PENDING.

## Affiliate AU subqueue

### C-AU-01 — publisher-affiliate proof hunt
- status: PENDING; owner/workstream: Affiliate AU; exact anchor: expansion `2d654dee4e55f82f17351559f589f4889024a112`.
- objective: separately verify publisher/affiliate relationship for Octopus Group, Pureprofile and Toluna; acceptance: member referral never mislabeled publisher affiliate; dependencies: first-party/network evidence; safe action boundary: research only; verification: source/date/route; next handoff: Master publishability.
- security_gates: `SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research; negative_tests: referral-only != publisher affiliate; receipt_evidence: source/date/program/route; green_required: no; prs_required: no; owner_boundary: signup/contact/publication; security_disposition: PENDING.

### C-AU-02 — LifePoints comparison-only contract
- status: PENDING; owner/workstream: Affiliate AU; exact anchor: same expansion + first-party FAQ no-referral evidence.
- objective: encode comparison-only disposition without monetized referral CTA; acceptance: reward evidence retained while referral qualification false; dependencies: current first-party evidence; safe action boundary: docs/tests; verification: publishability fixture; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: repo docs/tests; negative_tests: no referral route => no referral CTA; receipt_evidence: FAQ date/state; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

### C-AU-03 — AU evidence freshness table
- status: PENDING; owner/workstream: Affiliate AU; exact anchor: current AU corpus.
- objective: normalize availability, eligibility, reward economics, referral route and evidence date; acceptance: stale/unknown fields explicit; dependencies: existing corpus; safe action boundary: research/docs; verification: row audit; next handoff: Master.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: S1; authority_required: public research; negative_tests: stale/conflicting terms => HOLD; receipt_evidence: source/date/field; green_required: no; prs_required: no; owner_boundary: publication/signup; security_disposition: PENDING.

## Affiliate UK subqueue

### C-UK-01 — one reputable programme full proof packet
- status: PENDING; owner/workstream: Affiliate UK; exact anchor: current UK research lane.
- objective: verify availability, reward, publisher/referral route, attribution/disclosure and regulatory posture for one strong programme; acceptance: network listing alone not approval; dependencies: public evidence; safe action boundary: research only; verification: first-party/network matrix; next handoff: UK shortlist.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research; negative_tests: financial/regulatory uncertainty => HOLD; receipt_evidence: source/date/route; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: PENDING.

### C-UK-02 — network route separation
- status: PENDING; owner/workstream: Affiliate UK; exact anchor: Awin/CJ/Impact/Webgains/Tradedoubler research set.
- objective: separate programme presence from publisher eligibility/approval; acceptance: no implied partnership; dependencies: current network evidence; safe action boundary: research/docs; verification: route table; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: research; negative_tests: network presence != approval; receipt_evidence: programme/network/state; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: PENDING.

### C-UK-03 — claim-safe disclosure negatives
- status: PENDING; owner/workstream: Affiliate UK; exact anchor: UK content model.
- objective: ensure no guaranteed-income/unsupported financial claims; acceptance: evidence-limited copy only; dependencies: verified source claims; safe action boundary: tests/content drafts; verification: negative-copy fixtures; next handoff: Marketing.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: draft only; negative_tests: guaranteed earnings/unsupported availability; receipt_evidence: claim→source pointer; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## Affiliate US subqueue

### C-US-01 — high-value paid-participation proof packet
- status: PENDING; owner/workstream: Affiliate US; exact anchor: existing US research PR #6 lineage.
- objective: verify US availability, user reward, publisher/referral route and disclosure separately for one strong programme; acceptance: reward value and publisher eligibility separately evidenced; dependencies: current public evidence; safe action boundary: research only; verification: source matrix; next handoff: US shortlist.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research; negative_tests: reward evidence != affiliate eligibility; receipt_evidence: source/date/program; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: PENDING.

### C-US-02 — destination/eligibility freshness
- status: PENDING; owner/workstream: Affiliate US; exact anchor: current corpus.
- objective: verify current US eligibility/outbound destination; acceptance: geo mismatch/stale terms fail closed; dependencies: public evidence; safe action boundary: research/docs; verification: dated evidence; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: research; negative_tests: geo mismatch, stale route; receipt_evidence: source/date/destination; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

### C-US-03 — disclosure-safe comparison row
- status: PENDING; owner/workstream: Affiliate US; exact anchor: current model.
- objective: produce one comparison-ready non-public row with explicit UNKNOWN publisher state; acceptance: no monetized CTA if not approved; dependencies: C-US-01/02; safe action boundary: docs only; verification: schema audit; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: docs; negative_tests: unknown relationship => fallback; receipt_evidence: row evidence; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## GhostKitchen subqueue

### C-GK-01 — consume active economics/evidence-summary seam
- status: ACTIVE; owner/workstream: GhostKitchen; exact anchor: draft PR #32 + deterministic pilot-menu evidence packet.
- objective: populate only verified/synthetic-labelled recipe/yield/packaging/labour/delivery inputs without overlapping PR ownership; acceptance: hypothesis/reference inputs never labeled verified profitability; dependencies: active PR; safe action boundary: docs/fixtures; verification: evidence completeness; next handoff: C-GK-02.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-12,SG-14,SG-20`; risk_class: S1; authority_required: repo/research read-write; negative_tests: missing input => UNKNOWN; receipt_evidence: input/source/date/class; green_required: no; prs_required: no; owner_boundary: supplier contact/spend/production; security_disposition: ACTIVE.

### C-GK-02 — representative-order sensitivity
- status: PENDING; owner/workstream: GhostKitchen; exact anchor: C-GK-01 evidence-labelled inputs.
- objective: compute contribution sensitivity across delivery fee/food/packaging/labour bands; acceptance: no profitability claim and unknown real inputs remain explicit; dependencies: C-GK-01; safe action boundary: local calculation/docs; verification: reproducible table; next handoff: readiness gate.
- security_gates: `SG-06,SG-10,SG-12,SG-14`; risk_class: S0; authority_required: local analysis; negative_tests: missing real input => hypothesis label; receipt_evidence: assumptions/results; green_required: no; prs_required: no; owner_boundary: spend/production; security_disposition: PENDING.

### C-GK-03 — fail-closed readiness fixture
- status: PENDING; owner/workstream: GhostKitchen; exact anchor: existing pilot evidence schema.
- objective: deny readiness when supplier/recipe/yield/packaging/labour/delivery evidence is missing; acceptance: deterministic UNKNOWN/HOLD; dependencies: current schema; safe action boundary: tests/fixtures; verification: fixture suite; next handoff: Overseer.
- security_gates: `SG-06,SG-10,SG-12,SG-14`; risk_class: S1; authority_required: non-prod tests; negative_tests: each missing evidence dimension; receipt_evidence: fixture/disposition; green_required: no; prs_required: no; owner_boundary: production; security_disposition: PENDING.

## Franchise subqueue

### C-FR-01 — active membership/tenancy fail-closed seam
- status: ACTIVE; owner/workstream: Franchise; exact anchor: draft PR #24 duplicate-active-membership handling + PR #22 territory-status/determinism fixtures.
- objective: preserve tenancy/membership prerequisite before territory routing without overlapping active ownership; acceptance: duplicate/overlap/inactive tenant denied; dependencies: active PRs; safe action boundary: synthetic tests; verification: exact fixtures; next handoff: C-FR-02.
- security_gates: `SG-06,SG-07,SG-10,SG-12,SG-14,SG-20`; risk_class: S2; authority_required: non-prod tests; negative_tests: duplicate active membership, overlap, stale tenant; receipt_evidence: tenant/territory/version/disposition; green_required: conditional; prs_required: no; owner_boundary: production tenancy/routing; security_disposition: ACTIVE.

### C-FR-02 — territory overlap matrix
- status: PENDING; owner/workstream: Franchise; exact anchor: successor only after PR #24/#22 seam settles.
- objective: expand homogeneous synthetic exact/partial/nested overlap cases; acceptance: deterministic deny/route with version correlation; dependencies: active tenancy lineage stable; safe action boundary: fixtures; verification: test matrix; next handoff: audit receipt.
- security_gates: `SG-09,SG-10,SG-11,SG-12,SG-14`; risk_class: S2; authority_required: non-prod tests; negative_tests: duplicate/overlap/stale version; receipt_evidence: tenant/territory/version/result; green_required: conditional; prs_required: no; owner_boundary: production; security_disposition: PENDING.

### C-FR-03 — deterministic audit handoff
- status: PENDING; owner/workstream: Franchise; exact anchor: existing territory/audit contract.
- objective: ensure synthetic routing decision carries exact tenancy/territory/evidence version; acceptance: mismatch/stale version cannot be success; dependencies: C-FR-02; safe action boundary: tests/docs; verification: receipt fixture; next handoff: Overseer.
- security_gates: `SG-10,SG-11,SG-14`; risk_class: S1; authority_required: non-prod tests; negative_tests: stale/mismatch evidence; receipt_evidence: exact IDs/version; green_required: no; prs_required: no; owner_boundary: production; security_disposition: PENDING.

## GemVerse subqueue

### C-GV-01 — consume current recovery assurance seam
- status: ACTIVE; owner/workstream: GemVerse; exact anchor: draft PR #10 current fixture recovery assurance.
- objective: consume existing PR work rather than duplicate it; acceptance: exact preimage/target identity, replay/idempotence and competing-candidate denial explicit; dependencies: active PR; safe action boundary: fixtures/tests; verification: exact PR CI; next handoff: C-GV-03.
- security_gates: `SG-06,SG-07,SG-09,SG-10,SG-11,SG-14,SG-20`; risk_class: S2; authority_required: non-prod tests; negative_tests: stale preimage, competing candidate, replay/recovery; receipt_evidence: source/target/preimage/result; green_required: conditional; prs_required: no; owner_boundary: production mutation; security_disposition: ACTIVE.

### C-GV-02 — canon dependency packet
- status: BLOCKED; owner/workstream: GemVerse; exact anchor: current documentation/canon boundary.
- objective: distinguish verified creator/source canon from documentation hypothesis; acceptance: no executable implementation claim absent canon; dependencies: verified canon; safe action boundary: read/docs only; verification: evidence pointers; next handoff: project owner when canon exists.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-20`; risk_class: S1; authority_required: read-only; negative_tests: docs-only source cannot authorize implementation; receipt_evidence: canon source/version; green_required: no; prs_required: no; owner_boundary: product canon/production; security_disposition: BLOCKED.

### C-GV-03 — Level-2 governed mutation fixture readiness
- status: PENDING; owner/workstream: GemVerse; exact anchor: existing governed mutation workload + PR #10 lineage.
- objective: keep fixture ready for AgentOS acceptance without alternate control plane; acceptance: bounded files, expected pre/postimage, rollback/replay/receipt oracle; dependencies: existing fixture only; safe action boundary: fixture docs/tests; verification: deterministic local test; next handoff: AgentOS only after mutation gate clears.
- security_gates: `SG-03,SG-09,SG-10,SG-11,SG-14`; risk_class: S1; authority_required: fixture-only; negative_tests: wrong preimage/replay/out-of-scope file; receipt_evidence: fixture IDs/hashes; green_required: no; prs_required: no; owner_boundary: physical/production execution; security_disposition: PENDING.

## Content360 subqueue

### C-C360-01 — mock secret-isolation baseline
- status: VERIFIED; owner/workstream: Content360; exact anchor: PR #4 `6b72ea670ddeec5fe1699d8a13fa403e37d437d3`, Tests `34846314212` SUCCESS.
- objective: preserve opaque credential references/no secret persistence; acceptance: no secret in prompt/log/receipt/fixture; dependencies: none; safe action boundary: mocks/tests; verification: exact CI; next handoff: C-C360-02.
- security_gates: `SG-05,SG-06,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: non-prod tests; negative_tests: secret in metadata/log/result; receipt_evidence: redacted mock receipt; green_required: conditional; prs_required: no; owner_boundary: credentials/live provider/publish; security_disposition: VERIFIED.

### C-C360-02 — prompt-injection/provider-output boundary
- status: PENDING; owner/workstream: Content360; exact anchor: PR #4 current mock adapter lineage.
- objective: prove provider/content output cannot authorize PUBLISH/SCHEDULE/tool escalation; acceptance: READ/OPTIMISE remains bounded; dependencies: current mocks; safe action boundary: mocked tests; verification: fixture suite; next handoff: adapter.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15,SG-17`; risk_class: S2; authority_required: mock tests; negative_tests: publish instruction, secret request, memory write, capability escalation; receipt_evidence: request/result/disposition; green_required: conditional; prs_required: no; owner_boundary: live network/account mutation; security_disposition: PENDING.

### C-C360-03 — correlation/idempotency failure fixtures
- status: PENDING; owner/workstream: Content360; exact anchor: PR #4 current request/result schema.
- objective: verify duplicate request/result, timeout/retry and mismatched correlation do not fabricate successful optimization; acceptance: deterministic PARTIAL/FAIL/duplicate disposition; dependencies: existing schema; safe action boundary: mocks/tests; verification: exact CI; next handoff: adapter evidence.
- security_gates: `SG-09,SG-10,SG-11,SG-17`; risk_class: S2; authority_required: mock tests; negative_tests: duplicate, timeout, replay, mismatch; receipt_evidence: request/result IDs/status; green_required: conditional; prs_required: no; owner_boundary: live provider; security_disposition: PENDING.

### C-C360-04 — official API/auth capability evidence
- status: BLOCKED; owner/workstream: Content360; exact anchor: mock-only current evidence.
- objective: keep live API/auth/PUBLISH/SCHEDULE capabilities UNKNOWN until official evidence/owner authority; acceptance: no inference from mock adapter; dependencies: official docs/owner later; safe action boundary: public documentation research only; verification: official docs; next handoff: owner if credentials/account action becomes necessary.
- security_gates: `SG-02,SG-05,SG-06,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public docs only; negative_tests: mock capability != live authority; receipt_evidence: official docs/date/capability; green_required: no; prs_required: no; owner_boundary: credentials/account/live publish; security_disposition: BLOCKED.

## Commercial Frontend subqueue

### C-CF-01 — consume active Tradie value-threshold seam
- status: ACTIVE; owner/workstream: Commercial Frontend; exact anchor: Overseer draft PR #50.
- objective: consume active value-threshold work before adjacent implementation; acceptance: pain/demand/WTP remain hypothesis unless externally evidenced; dependencies: active PR; safe action boundary: docs/fixtures/prototype only; verification: evidence packet; next handoff: C-CF-02.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-12,SG-14,SG-20`; risk_class: S1; authority_required: repo docs/prototype; negative_tests: internal hypothesis != demand proof; receipt_evidence: claim/evidence source; green_required: no; prs_required: no; owner_boundary: customer contact/deployment; security_disposition: ACTIVE.

### C-CF-02 — bounded exception-workflow packet
- status: PENDING; owner/workstream: Commercial Frontend; exact anchor: PR #50 successor scope after fresh scan.
- objective: define one Tradie/service-ops exception input→recommended correction→receipt with no production action; acceptance: measurable time/error/value hypothesis fields explicit; dependencies: active seam stable; safe action boundary: synthetic artifact; verification: fixture walkthrough; next handoff: integration feasibility.
- security_gates: `SG-06,SG-10,SG-11,SG-12,SG-14`; risk_class: S1; authority_required: non-prod prototype/docs; negative_tests: unsupported correction/authority escalation; receipt_evidence: input/correction/result; green_required: no; prs_required: no; owner_boundary: deployment/account mutation; security_disposition: PENDING.

### C-CF-03 — operator evidence gap register
- status: PENDING; owner/workstream: Commercial Frontend; exact anchor: current hypothesis/value-threshold evidence.
- objective: make frequency/friction/WTP UNKNOWNs explicit and separate technical feasibility from market proof; acceptance: no commercial-ready claim; dependencies: current evidence; safe action boundary: research synthesis; verification: evidence-gap table; next handoff: future owner-authorized validation.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-20`; risk_class: S0; authority_required: read/research; negative_tests: internal assumptions cannot become WTP evidence; receipt_evidence: source/gap/date; green_required: no; prs_required: no; owner_boundary: customer contact; security_disposition: PENDING.

## Marketing subqueue

### C-MKT-01 — AgentOS readiness/claim reconciliation
- status: ACTIVE; owner/workstream: Marketing; exact anchor: Marketing batch `9fb9189142d1580e5076a02eec70d1b04906d95e`, log `2e3384d409998623fc8bbc45b9cb9a6d581f0496`, AgentOS #104 `bbfee522...`/`34857161932`, #111 `429b6d5b...`/`34859721665`.
- objective: keep claims consistent with functional evidence while SG-08/SG-01/02/SG-18 remain unresolved; acceptance: no shipped/Level-2-ready/overall-GREEN claim from bounded CI; dependencies: exact AgentOS evidence; safe action boundary: internal copy/docs; verification: claim→evidence pointer; next handoff: Marketing assets.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: internal drafts only; negative_tests: shipped/ready claim without full evidence; receipt_evidence: claim/evidence IDs; green_required: no; prs_required: no; owner_boundary: campaign/publication/spend; security_disposition: ACTIVE.

### C-MKT-02 — GlobalShopCo claim-safe product messaging
- status: PENDING; owner/workstream: Marketing; exact anchor: `0 eBay-ready SKUs`, PR #29/#30 current evidence queue.
- objective: prepare evidence-safe non-paid internal templates requiring exact SKU/price/availability/freight/returns/assets before insertion; acceptance: no approved-supplier/eBay-ready claim without evidence; dependencies: GSC qualification; safe action boundary: drafts; verification: negative-copy checklist; next handoff: Content360 only after product qualification.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: internal drafts; negative_tests: missing freight/stock/permission/assets => omit claim; receipt_evidence: placeholder/evidence schema; green_required: no; prs_required: no; owner_boundary: publication/campaign/spend; security_disposition: PENDING.

### C-MKT-03 — Affiliate country claim-evidence pointer index
- status: PENDING; owner/workstream: Marketing; exact anchor: AU `2d654dee...` + UK/US current proof-gated lanes.
- objective: map each reward/referral/publisher/disclosure claim to country-specific evidence; acceptance: member referral never implied publisher partnership and stale/unknown evidence suppresses claim; dependencies: country evidence; safe action boundary: internal docs; verification: pointer audit; next handoff: Content360/affiliate pages.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: internal docs; negative_tests: cross-country leakage, unsupported partner claim; receipt_evidence: claim/source/date/country; green_required: no; prs_required: no; owner_boundary: publication/outreach; security_disposition: PENDING.

## Lane health after replenishment
- **Lane A:** multiple actionable PENDING items remain: A-AG-04/A-AG-05 receipt provenance/replay work and A-PRS-04 Green false-readiness assurance; SG-08, SG-01/02 and physical-host blockers stay explicit.
- **Lane B:** multiple actionable PENDING items remain across GSC exact-SKU economics, eBay receipt semantics, Amazon freshness, Headless synthetic handoff and MyPrime identity/funnel/presentation work. Permission/freight/provider/live-environment blockers do not starve safe closure.
- **Lane C:** every scheduled workstream has at least one actionable next item or explicit blocker; active PR ownership is preserved and adjacent work is split to avoid duplicate ACTIVE execution.

**No overall GREEN.**