# Portfolio Execution Batch Manifest

**Purpose:** queue state only for the fixed scheduled portfolio lanes. Canonical execution procedure: `.overseer/doctrine/PORTFOLIO-BATCH-ENGINE.md`. Project shaping: `.overseer/profiles/PROJECT-BATCH-PROFILES.md`. Security: `.overseer/security/AGENTOS-SECURITY-GATE-MATRIX.md`. Exact repository/issue/CI/runtime evidence always outranks this manifest.

**Fixed lanes:** A = AgentOS Level 2 P0 + PRS/Green assurance-adjacent work; B = GlobalShopCo/Headless/eBay/Amazon/MyPrimeDelivery; C = Affiliate-Websites AU/UK/US/Master, GhostKitchen, Franchise, GemVerse, Content360, Commercial Frontend, Marketing.

**States:** `PENDING | ACTIVE | VERIFIED | BLOCKED | STALE | SPLIT_REQUIRED`.

**Core invariant:** **NO MODEL DECIDES ITS OWN AUTHORITY.** Functional state, security state and PRS state remain separate. No merge/approve/ready/rebase/deploy/credentials/security-policy changes/production writes/purchases/spend/supplier contact/live publication/physical owner-host action/production autonomy.

## Checkpoint reconciliation — 2026-09-15 00:30+ Brisbane
- Previous durable checkpoint: Overseer #49 `5664955013`; previous manifest blob `4367429c8f9d43d8d1f95273c348988ae7c75003`.
- Canonical batch engine and central profiles were re-read first; queue text was treated as hypothesis only.
- AgentOS PR #104 remains OPEN/DRAFT/UNMERGED at exact `83a58b8bd230550b5781a0fee700cca250819a75`; exact push Tests `34821384346` SUCCESS. PRS stale-owner false-success baseline remains controlling; SG-08 is not closed. Authenticated actor/canonical grant admission remains unproven under SG-01/02.
- AgentOS PR #111 moved to exact `146f1118d34c36fdcb579450987a72a6e656c3d7`; exact-head Tests `34853649670` FAILURE overall. Windows lifecycle and evidence/readiness projection tests passed, but Ubuntu/general lifecycle has inherited SIGINT expectation failure. Therefore exact-head frontend promotion is not VERIFIED.
- Local-wake correlation repair remains bounded VERIFIED at `a69562dfe19696b79474c1a3f01a10d67b8d8e90`; runs `34849679000` and `34849679095` SUCCESS. This does not close SG-08 or SG-01/02.
- Shopify→eBay branch `agent/chatgpt/ebay-mapper-receipts` advanced to exact `8d891d782dca6799a9a4d942218fde441685e5dc`; Fixture validation `34856089804` SUCCESS. Event-ID/payload conflict fails closed; exact benign replay remains duplicate. Synthetic S2 only; zero network/publication authority.
- Shopify→Amazon branch `agent/chatgpt/amazon-au-preflight` advanced to exact `0b52631e9a3f084d9b947227c84e7f656ebab6f5`; Amazon channel gate `34856135125` SUCCESS. Compound permission/stock/category/identifier/fulfilment/fee/source conflicts fail closed. Synthetic S2 only.
- GlobalShopCo default remains `79d50227fe19826d42c43e7dec15ce245ad58e40`; research ownership advanced beyond PR #28 to stacked PR #29 (shelf organisers) and PR #30 (OXO organiser source hunting). Do not duplicate those active research surfaces. `0 eBay-ready SKUs` remains controlling.
- GlobalShopCo-Headless default is `c3e2960961fd60ef33ddb531577173fd3ff7cb17`; deterministic branch `agent/chatgpt/m3-baseline@44552d2a94dcea1445dddeb2d8a853d6d2b34d3e`. Live dev-store/browser checkout proof remains externally blocked.
- MyPrimeDelivery previous anchor is STALE. Default branch `agent/overseer/initial-project-timeline` advanced through provider-neutral adapter / Creators API AU / Vertical Batch 009 to exact `f8fcce2d80ddc5955f08c020e159e440c2da2338`. Live authoritative Prime/rank/deal rights remain gated.
- Affiliate AU expansion artifact `2d654dee4e55f82f17351559f589f4889024a112`: Octopus Group, Pureprofile and Toluna pass current consumer reward + member-referral evidence; publisher-affiliate relationship remains UNKNOWN/HOLD. LifePoints AU currently has reward evidence but no first-party referral programme.
- Marketing vertical batch `9fb9189142d1580e5076a02eec70d1b04906d95e`; canonical Marketing log `2e3384d409998623fc8bbc45b9cb9a6d581f0496`. Creation remains non-public evidence only.

# LANE A — AgentOS Level 2 P0

## AgentOS Overseer subqueue

### A-AG-01 — continuous project-file ownership fence
- status: BLOCKED; owner/workstream: AgentOS / writer ownership.
- exact anchor: PR #104 `83a58b8bd230550b5781a0fee700cca250819a75`; Tests `34821384346`; PRS stale-owner baseline `0defebe26f71e1cf5df1168fa5454bfd8de30091` / `34821646371`.
- objective: hold one crash-releasing kernel-enforced ownership fence continuously from final verification through publish/prepared recovery and durable success receipt.
- acceptance: replacement-after-verify, successor/three-writer, stale owner, TOCTOU, crash/replay, duplicate mutation/result and prepared-recovery stale-owner all fail closed; exact Ubuntu+Windows CI; then Green and PRS on identical lineage.
- dependencies: real writer implementation change; safe action boundary: non-prod draft branch code/tests only; verification: adversarial ownership matrix + exact-head CI; next handoff: AgentOS implementation worker.
- security_gates: `SG-03,SG-08,SG-09,SG-10,SG-11,SG-14,SG-18,SG-19`; risk_class: S2; authority_required: scoped non-prod branch/test write; negative_tests: ownership matrix above; receipt_evidence: actor/task/file/pre-postimage/ownership/result lineage; green_required: yes; prs_required: yes; owner_boundary: merge/deploy/physical production; security_disposition: BLOCKED.

### A-AG-02 — authenticated actor + canonical grant binding
- status: BLOCKED; owner/workstream: AgentOS / authority admission.
- exact anchor: PR #104 `83a58b8...`; authority dependency contract already recorded in prior batch lineage.
- objective: bind an existing authenticated actor source and canonical grant resolver without creating a second authority source or registry.
- acceptance: payload/host cannot self-supply identity or grant; missing/spoofed/mismatched/cross-project/replayed grant yields zero artifact and no success receipt.
- dependencies: real bindable canonical source; safe action boundary: architecture discovery + bounded branch tests; verification: provenance + spoof/mismatch/replay matrix; next handoff: AgentOS architecture/implementation.
- security_gates: `SG-01,SG-02,SG-03,SG-04,SG-09,SG-10,SG-11,SG-18,SG-19`; risk_class: S2; authority_required: canonical identity/grant read + scoped branch test; negative_tests: host-as-auth, spoof actor, payload self-grant, absent/mismatch/cross-project/replay; receipt_evidence: issuer/source/version/request/task/mission; green_required: yes; prs_required: yes; owner_boundary: credentials/security policy; security_disposition: BLOCKED.

### A-AG-03 — PR #111 exact-head CI repair
- status: ACTIVE; owner/workstream: AgentOS / Basic Chat frontend lifecycle.
- exact anchor: PR #111 `146f1118d34c36fdcb579450987a72a6e656c3d7`; Tests `34853649670` FAILURE; Windows lifecycle PASS; evidence/readiness projections PASS; Ubuntu inherited SIGINT assertion FAIL.
- objective: isolate whether the SIGINT result is valid supported behavior or a regression, then repair assertion/implementation without weakening lock-removal semantics.
- acceptance: exact-head Linux+Windows CI green; lock removed before exit; no fabricated readiness; evidence projection and secret-leak negatives remain green.
- dependencies: none beyond current branch; safe action boundary: non-prod tests/small lifecycle fix only; verification: targeted lifecycle test + full exact-head CI; next handoff: Green SG-18 sampling after green CI.
- security_gates: `SG-03,SG-05,SG-10,SG-11,SG-14,SG-18`; risk_class: S2; authority_required: scoped branch code/tests; negative_tests: stale lock, unsupported signal, fabricated readiness, secret/raw/PRS/recovery leakage, cross-task correlation; receipt_evidence: exact head/run/jobs + regression output; green_required: yes; prs_required: no unless authority semantics widen; owner_boundary: merge/deploy/runtime enablement; security_disposition: ACTIVE.

### A-AG-04 — local-wake correlation adjacency
- status: VERIFIED; owner/workstream: AgentOS / local-wake correlation.
- exact anchor: `a69562dfe19696b79474c1a3f01a10d67b8d8e90`; runs `34849679000`,`34849679095` SUCCESS.
- objective: preserve task→response→event mission/wake identity.
- acceptance: mismatch/replay cannot normalize into success; dependencies: none; safe action boundary: regression tests only; verification: exact regression + workflow; next handoff: Green SG-18 sample only if same surface changes.
- security_gates: `SG-09,SG-10,SG-11,SG-14,SG-18`; risk_class: S2; authority_required: branch tests; negative_tests: mission/wake mismatch, cross-task response, replay drift; receipt_evidence: exact head/two runs/identities; green_required: yes before promotion; prs_required: conditional; owner_boundary: merge/deploy; security_disposition: PENDING.

### A-AG-05 — physical Windows acceptance packet
- status: BLOCKED; owner/workstream: AgentOS / physical host acceptance.
- exact anchor: PR #104 current lineage + unresolved A-AG-01/A-AG-02.
- objective: maintain one exact owner-run acceptance packet only after software/security blockers clear.
- acceptance: exact SHA/root/mutation/recovery/correlation/no-production boundaries; dependencies: SG-08 + SG-01/02 closure and explicit owner physical authority; safe action boundary: checklist/evidence packet only; verification: future physical evidence; next handoff: owner/physical-host lane.
- security_gates: `SG-03,SG-08,SG-10,SG-11,SG-14,SG-18,SG-20`; risk_class: S2; authority_required: owner-authorized physical Windows action; negative_tests: wrong head, prod root, missing receipt; receipt_evidence: head/host/root/test/result; green_required: yes; prs_required: yes if promoted; owner_boundary: physical Windows execution; security_disposition: BLOCKED.

## PRS / Green assurance subqueue

### A-PRS-01 — immutable stale-owner false-GREEN baseline
- status: VERIFIED; owner/workstream: PRS.
- exact anchor: PRS `0defebe26f71e1cf5df1168fa5454bfd8de30091` / `34821646371` against AgentOS `83a58b8...`.
- objective: preserve exact immutable defect baseline; acceptance: never transfer PASS/FAIL to successor head; dependencies: none; safe action boundary: read-only assurance; verification: exact target/artifact hashes; next handoff: A-AG-01.
- security_gates: `SG-08,SG-10,SG-11,SG-19`; risk_class: S0; authority_required: read-only; negative_tests: normal publish + prepared recovery stale-owner; receipt_evidence: immutable hashes; green_required: no; prs_required: baseline; owner_boundary: none; security_disposition: VERIFIED.

### A-PRS-02 — successor ownership challenge
- status: BLOCKED; owner/workstream: PRS.
- exact anchor: A-PRS-01/A-AG-01.
- objective: rerun full ownership matrix only after real AgentOS writer repair and identical-head Green PASS.
- acceptance: normal/prepared/successor/crash/replay independently classified; dependencies: A-AG-01 + exact CI + Green; safe action boundary: assurance harness; verification: immutable target/artifact hashes; next handoff: Overseer.
- security_gates: `SG-08,SG-09,SG-10,SG-11,SG-19`; risk_class: S2; authority_required: bounded harness; negative_tests: full ownership matrix; receipt_evidence: target/artifact hash; green_required: yes prerequisite; prs_required: yes; owner_boundary: merge/deploy; security_disposition: BLOCKED.

### A-PRS-03 — admission false-GREEN challenge
- status: BLOCKED; owner/workstream: PRS.
- exact anchor: A-AG-02.
- objective: independently prove spoof/missing/mismatch/self-grant paths cannot produce success after canonical admission exists.
- acceptance: exact identical Green-passed head; dependencies: A-AG-02; safe action boundary: synthetic assurance; verification: immutable target + adversarial fixtures; next handoff: Overseer.
- security_gates: `SG-01,SG-02,SG-10,SG-11,SG-19`; risk_class: S2; authority_required: bounded harness; negative_tests: spoof/missing/mismatch/cross-project/replay/self-grant; receipt_evidence: exact target + outcome; green_required: yes prerequisite; prs_required: yes; owner_boundary: none; security_disposition: BLOCKED.

### A-PRS-04 — PR #111 false-readiness sample
- status: PENDING; owner/workstream: Green first, PRS conditional.
- exact anchor: PR #111 `146f1118...` / `34853649670` currently red.
- objective: after exact CI is green, challenge fabricated completion/readiness and evidence leakage without treating UI availability as Level-2 authority.
- acceptance: missing/mismatched evidence cannot display readiness; secret/raw/PRS/recovery fields remain excluded; dependencies: A-AG-03 exact-head green CI; safe action boundary: test-only; verification: exact-head negatives; next handoff: AgentOS Overseer.
- security_gates: `SG-05,SG-10,SG-11,SG-14,SG-18`; risk_class: S1; authority_required: read/test only; negative_tests: fabricated completion, stale evidence, correlation mismatch, leakage; receipt_evidence: exact head/run/test names; green_required: yes; prs_required: no unless promoted scope widens; owner_boundary: merge/deploy; security_disposition: PENDING.

# LANE B — Commerce

## GlobalShopCo subqueue

### B-GSC-01 — consume active PR #29/#30 evidence, no duplicate research
- status: ACTIVE; owner/workstream: GlobalShopCo product qualification.
- exact anchor: default `79d50227fe19826d42c43e7dec15ce245ad58e40`; stacked PR #29 shelf organisers; PR #30 OXO organiser source hunt; Marketing OXO screen `181e4507642740422e79b6a5e60377468991cb8f`.
- objective: reconcile exact SKU/GTIN, buy cost, freight, permission, stock/fulfilment, AU/eBay comp floor and returns/warranty for active rows.
- acceptance: each row promoted, rejected or HOLD with explicit missing field; no row becomes eBay-ready on public retail evidence alone.
- dependencies: active PR ownership; safe action boundary: research/docs/tests only, no supplier contact; verification: source/date/identity/economics table; next handoff: eBay readiness gate.
- security_gates: `SG-02,SG-03,SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public/read-only evidence; negative_tests: missing freight/permission/stock/seller/fee => HOLD; receipt_evidence: exact source/date/SKU/economics; green_required: no; prs_required: no; owner_boundary: supplier contact/purchase/publication; security_disposition: ACTIVE.

### B-GSC-02 — CARLA current-leader re-screen
- status: PENDING; owner/workstream: GlobalShopCo product economics.
- exact anchor: prior CARLA `V178-36336` lineage + `0 eBay-ready SKUs` controlling state.
- objective: refresh exact AU comps, freight/weight and max-buy-cost ceiling without assuming marketplace permission.
- acceptance: deterministic commercial disposition with all UNKNOWNs explicit; dependencies: current public evidence; safe action boundary: read-only research/calculation; verification: reproducible calculator inputs; next handoff: GSC matrix.
- security_gates: `SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public read-only; negative_tests: stale comp, unknown freight/permission => HOLD; receipt_evidence: sources/date/calculation; green_required: no; prs_required: no; owner_boundary: supplier contact/purchase; security_disposition: PENDING.

### B-GSC-03 — comparison-ready shortlist normalization
- status: PENDING; owner/workstream: GlobalShopCo / commercial matrix.
- exact anchor: current default + PR #29/#30 outputs.
- objective: normalize only evidence-complete/rejected/HOLD rows into one 5–10-row pilot matrix; do not broaden category count.
- acceptance: exact supplier/SKU/GTIN where available, wholesale/landed, AU/eBay comps, freight, free-delivery contribution, permission, stock model, returns/warranty, fee basis, disposition.
- dependencies: B-GSC-01/02 outputs; safe action boundary: docs only; verification: schema completeness + calculator; next handoff: eBay/Amazon channel gates.
- security_gates: `SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read/docs; negative_tests: missing material field cannot promote; receipt_evidence: row-level evidence pointers; green_required: no; prs_required: no; owner_boundary: publication/spend/contact; security_disposition: PENDING.

## Shopify→eBay subqueue

### B-EBAY-01 — replay/idempotency conflict gate
- status: VERIFIED; owner/workstream: Shopify→eBay.
- exact anchor: `8d891d782dca6799a9a4d942218fde441685e5dc`; Fixture validation `34856089804` SUCCESS.
- objective: preserve `EVENT_ID_PAYLOAD_CONFLICT` denial and benign exact replay `DUPLICATE_EVENT` behavior.
- acceptance: changed payload under reused event ID fails closed; zero network/publication authority; dependencies: none; safe action boundary: synthetic fixtures; verification: exact-head CI; next handoff: B-EBAY-02.
- security_gates: `SG-02,SG-03,SG-09,SG-10,SG-11,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: non-prod branch/test; negative_tests: altered replay, stale event, correlation mismatch; receipt_evidence: event/payload hash/disposition; green_required: no for synthetic fixture; prs_required: no; owner_boundary: network/publication; security_disposition: VERIFIED.

### B-EBAY-02 — replay receipt persistence/correlation semantics
- status: PENDING; owner/workstream: Shopify→eBay.
- exact anchor: B-EBAY-01 exact head.
- objective: prove persisted/replayed synthetic receipts cannot overwrite accepted identity or create duplicate durable result, using existing persistence only.
- acceptance: same event+same payload is idempotent; same event+different payload denied; result/receipt correlation exact; no second persistence/control plane.
- dependencies: existing schema/persistence support; safe action boundary: fixtures/tests/small branch fix only; verification: exact-head CI + restart/replay fixture if supported; next handoff: channel assurance.
- security_gates: `SG-09,SG-10,SG-11,SG-14,SG-15`; risk_class: S2; authority_required: non-prod tests; negative_tests: restart replay, duplicate result write, mismatched receipt identity; receipt_evidence: event/payload/result/receipt lineage; green_required: conditional; prs_required: no; owner_boundary: publication/network; security_disposition: PENDING.

### B-EBAY-03 — real SKU readiness remains fail-closed
- status: BLOCKED; owner/workstream: Shopify→eBay commercial readiness.
- exact anchor: `0 eBay-ready SKUs`; GlobalShopCo PR #29/#30 active evidence.
- objective: consume only rows with permission, compliant fulfilment/stock, exact freight/economics, seller/fee evidence.
- acceptance: no publication-ready classification with any missing material field; dependencies: B-GSC-03; safe action boundary: read-only preflight; verification: evidence packet; next handoff: owner only if one strong row is blocked solely on owner-gated evidence.
- security_gates: `SG-02,SG-03,SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read-only; negative_tests: missing permission/freight/seller/fee/stock => HOLD; receipt_evidence: SKU evidence packet; green_required: no; prs_required: no; owner_boundary: listing/account/contact/spend; security_disposition: BLOCKED.

## Shopify→Amazon subqueue

### B-AMZ-01 — compound-conflict assurance
- status: VERIFIED; owner/workstream: GlobalShopCo / Amazon fixtures.
- exact anchor: `0b52631e9a3f084d9b947227c84e7f656ebab6f5`; Amazon gate `34856135125` SUCCESS.
- objective: preserve fail-closed compound conflicts while Shopify remains canonical.
- acceptance: permission+stock, category+identifier, fulfilment+fee/cost and seller/source conflicts deny; dependencies: none; safe action boundary: synthetic tests; verification: exact-head CI; next handoff: B-AMZ-02.
- security_gates: `SG-02,SG-03,SG-09,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: non-prod tests; negative_tests: compound conflicts; receipt_evidence: exact head/run/conflict code; green_required: no for synthetic; prs_required: no; owner_boundary: seller setup/listing/credentials; security_disposition: VERIFIED.

### B-AMZ-02 — freshness/version/correlation denial
- status: PENDING; owner/workstream: GlobalShopCo / Amazon fixtures.
- exact anchor: B-AMZ-01; only execute if existing schema exposes evidence version/freshness fields.
- objective: deny stale or version-mismatched evidence without inventing new authority semantics.
- acceptance: stale/mismatched source evidence cannot pass preflight; absent schema => SPLIT_REQUIRED rather than invented field; dependencies: schema inspection; safe action boundary: tests/small schema-compatible fix; verification: exact-head CI; next handoff: Amazon channel gate.
- security_gates: `SG-06,SG-09,SG-10,SG-11,SG-14`; risk_class: S2; authority_required: non-prod tests; negative_tests: stale source, mismatched version, cross-SKU evidence; receipt_evidence: source/version/SKU/disposition; green_required: conditional; prs_required: no; owner_boundary: credentials/listing; security_disposition: PENDING.

### B-AMZ-03 — real Amazon readiness
- status: BLOCKED; owner/workstream: GlobalShopCo / Amazon AU.
- exact anchor: synthetic-only fixture lineage; no owner-authorized seller/provider evidence.
- objective: keep seller-of-record, permission, variant/stock, category/GTIN, fulfilment and fees/economics UNKNOWN until authoritative evidence exists.
- acceptance: no live-ready status from fixtures; dependencies: owner/account evidence later; safe action boundary: read-only research; verification: authoritative evidence packet; next handoff: owner if only gated account evidence remains.
- security_gates: `SG-02,SG-03,SG-06,SG-10,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read-only; negative_tests: missing seller/permission/category/fee => HOLD; receipt_evidence: evidence packet; green_required: no; prs_required: no; owner_boundary: seller account/credentials/listing; security_disposition: BLOCKED.

## GlobalShopCo-Headless subqueue

### B-HDL-01 — deterministic contract preservation
- status: VERIFIED; owner/workstream: Headless.
- exact anchor: `agent/chatgpt/m3-baseline@44552d2a94dcea1445dddeb2d8a853d6d2b34d3e`; default `c3e2960961fd60ef33ddb531577173fd3ff7cb17`.
- objective: preserve Shopify product identity/cart/checkout host integrity and parser/host-confusion denials.
- acceptance: no local duplicate catalogue/order authority; malformed destination denied; dependencies: none; safe action boundary: tests; verification: deterministic suite; next handoff: B-HDL-02.
- security_gates: `SG-02,SG-03,SG-05,SG-06,SG-10,SG-14,SG-20`; risk_class: S2; authority_required: non-prod tests; negative_tests: host confusion, malformed destination, secret leakage; receipt_evidence: exact branch/tests; green_required: conditional; prs_required: no; owner_boundary: deployment/secrets/live purchase; security_disposition: VERIFIED.

### B-HDL-02 — evidence-qualified product fixture handoff
- status: PENDING; owner/workstream: Headless.
- exact anchor: default `c3e296...`; parent GlobalShopCo current evidence matrix.
- objective: use a synthetic/evidence-qualified fixture to prove retrieval→render→Shopify checkout URL handoff without requiring live store access.
- acceptance: exact product identity survives render/handoff; checkout host canonical; availability false cannot display purchasable; dependencies: evidence-qualified fixture, not live SKU promotion; safe action boundary: local/dev tests; verification: integration fixture; next handoff: B-HDL-03.
- security_gates: `SG-03,SG-05,SG-06,SG-10,SG-14`; risk_class: S2; authority_required: non-prod tests; negative_tests: wrong product/variant, unavailable item, checkout host substitution; receipt_evidence: fixture/result; green_required: conditional; prs_required: no; owner_boundary: deployment/live purchase; security_disposition: PENDING.

### B-HDL-03 — live dev-store/browser proof
- status: BLOCKED; owner/workstream: Headless.
- exact anchor: current default/work branch.
- objective: preserve real non-production browser checkout proof as external evidence gate.
- acceptance: actual dev-store environment + owner-authorized access + exact product handoff; dependencies: owner/environment; safe action boundary: no action now; verification: future browser evidence; next handoff: owner/environment.
- security_gates: `SG-03,SG-05,SG-10,SG-14,SG-20`; risk_class: S2; authority_required: owner-authorized non-prod environment; negative_tests: prod host, wrong store, missing access; receipt_evidence: environment/product/URL/result; green_required: yes if used for promotion; prs_required: no; owner_boundary: access/deployment/purchase; security_disposition: BLOCKED.

## MyPrimeDelivery subqueue

### B-MPD-01 — Batch 009 reconciliation
- status: ACTIVE; owner/workstream: MyPrimeDelivery.
- exact anchor: default `agent/overseer/initial-project-timeline@f8fcce2d80ddc5955f08c020e159e440c2da2338`.
- objective: consume provider-neutral adapter / Creators API AU / Batch 009 artifacts before assigning successor work.
- acceptance: exact objective/workflow/source-rights/freshness fields recovered; no duplicate implementation; dependencies: current repo batch artifacts; safe action boundary: read-only/docs/tests; verification: exact file/head evidence; next handoff: B-MPD-02.
- security_gates: `SG-02,SG-03,SG-05,SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: repo read; negative_tests: public/editorial source cannot become Prime/rank/deal authority; receipt_evidence: artifact paths/head; green_required: no; prs_required: no; owner_boundary: provider signup/credentials/publication; security_disposition: ACTIVE.

### B-MPD-02 — provider evidence identity/freshness negatives
- status: PENDING; owner/workstream: MyPrimeDelivery.
- exact anchor: Batch 009 current head.
- objective: test ASIN/marketplace/variant/freshness mismatch denial using provider-neutral fixtures already supported.
- acceptance: stale/mismatched evidence fails closed; source rights remain separate from product truth; dependencies: B-MPD-01 schema; safe action boundary: synthetic tests only; verification: exact-head test output; next handoff: research qualification funnel.
- security_gates: `SG-06,SG-09,SG-10,SG-11,SG-14`; risk_class: S2; authority_required: non-prod tests; negative_tests: ASIN mismatch, marketplace mismatch, stale provider, variant conflict; receipt_evidence: source/version/product/disposition; green_required: conditional; prs_required: no; owner_boundary: live provider credentials; security_disposition: PENDING.

### B-MPD-03 — qualification funnel metrics
- status: PENDING; owner/workstream: MyPrimeDelivery.
- exact anchor: Batch 009 current corpus.
- objective: count candidates by identity-resolved / rights-known / Prime-current / rank/deal-current / outbound-destination-ready, preserving UNKNOWN rather than raw-count optimism.
- acceptance: reproducible funnel and unresolved families list; dependencies: current corpus; safe action boundary: analysis/docs; verification: deterministic counts; next handoff: WordPress presentation queue.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: read/docs; negative_tests: missing authority never promoted; receipt_evidence: corpus head + metric table; green_required: no; prs_required: no; owner_boundary: affiliate/provider account/publication; security_disposition: PENDING.

# LANE C — Growth / verticals

## Affiliate-Websites Master subqueue
### C-AFF-M-01 — publication-state/CTA evidence contract
- status: ACTIVE; owner/workstream: Affiliate Master; exact anchor: existing draft PR #17 publication-state wiring + current shared repo lineage.
- objective: ensure UNKNOWN/non-affiliate relationships never emit monetized CTA; acceptance: fallback/non-monetized behavior deterministic; dependencies: existing PR ownership; safe action boundary: branch tests/docs; verification: fixtures; next handoff: country lanes.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: non-prod branch tests; negative_tests: unknown relationship, stale destination, injected CTA; receipt_evidence: program/country/state/destination; green_required: conditional; prs_required: no; owner_boundary: signup/publication; security_disposition: ACTIVE.
### C-AFF-M-02 — country config separation
- status: PENDING; owner/workstream: Affiliate Master; exact anchor: shared repo current profile lineage.
- objective: keep AU/UK/US terms out of global canon unless explicitly global; acceptance: country-specific eligibility/reward/disclosure fields cannot leak across regions; dependencies: Master model; safe action boundary: tests/docs; verification: cross-country fixtures; next handoff: AU/UK/US.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: S1; authority_required: repo tests/docs; negative_tests: AU→UK/US leakage, stale terms; receipt_evidence: country/program/version; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.
### C-AFF-M-03 — destination integrity
- status: PENDING; owner/workstream: Affiliate Master; exact anchor: PR #19 identity/destination determinism lineage.
- objective: preserve exact program/country/outbound destination mapping; acceptance: mismatch/redirect ambiguity fails closed; dependencies: current PR ownership; safe action boundary: tests only; verification: deterministic fixtures; next handoff: publication gate.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: non-prod tests; negative_tests: destination mismatch, unsupported redirect, injected URL; receipt_evidence: program/country/destination; green_required: conditional; prs_required: no; owner_boundary: live CTA/publication; security_disposition: PENDING.

## Affiliate AU subqueue
### C-AU-01 — publisher-affiliate proof hunt
- status: PENDING; owner/workstream: Affiliate AU; exact anchor: expansion `2d654dee4e55f82f17351559f589f4889024a112`.
- objective: separately verify publisher/affiliate relationship for Octopus Group, Pureprofile and Toluna; acceptance: member referral never mislabeled publisher affiliate; dependencies: public first-party/network evidence; safe action boundary: research only; verification: source/date/route; next handoff: Master publishability.
- security_gates: `SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research; negative_tests: referral-only != publisher affiliate; receipt_evidence: source/date/program/route; green_required: no; prs_required: no; owner_boundary: signup/contact/publication; security_disposition: PENDING.
### C-AU-02 — LifePoints comparison-only contract
- status: PENDING; owner/workstream: Affiliate AU; exact anchor: same expansion; first-party FAQ currently no referral programme.
- objective: encode comparison-only disposition without monetized referral CTA; acceptance: reward evidence retained while referral qualification false; dependencies: current first-party evidence; safe action boundary: docs/tests; verification: publishability fixture; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: repo docs/tests; negative_tests: no referral route => no referral CTA; receipt_evidence: FAQ date/state; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.
### C-AU-03 — AU evidence freshness table
- status: PENDING; owner/workstream: Affiliate AU; exact anchor: current AU corpus.
- objective: normalize availability, country eligibility, reward type/economics, referral route and evidence date; acceptance: stale/unknown fields explicit; dependencies: existing corpus; safe action boundary: research/docs; verification: row audit; next handoff: Master.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: S1; authority_required: public research; negative_tests: stale/conflicting terms => HOLD; receipt_evidence: source/date/field; green_required: no; prs_required: no; owner_boundary: publication/signup; security_disposition: PENDING.

## Affiliate UK subqueue
### C-UK-01 — one reputable programme full proof packet
- status: PENDING; owner/workstream: Affiliate UK; exact anchor: current UK research lane.
- objective: verify availability, reward, publisher/referral route, attribution/disclosure and regulatory posture for one strong programme; acceptance: network listing alone not approval; dependencies: current public evidence; safe action boundary: research only; verification: first-party/network source matrix; next handoff: UK shortlist.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research; negative_tests: financial/regulatory uncertainty => HOLD; receipt_evidence: source/date/route; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: PENDING.
### C-UK-02 — network route separation
- status: PENDING; owner/workstream: Affiliate UK; exact anchor: Awin/CJ/Impact/Webgains/Tradedoubler research set.
- objective: separate programme presence from publisher eligibility/approval; acceptance: no implied partnership; safe boundary: research/docs; verification: route table; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: research; negative_tests: network presence != approval; receipt_evidence: programme/network/state; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: PENDING.
### C-UK-03 — claim-safe disclosure negatives
- status: PENDING; owner/workstream: Affiliate UK; exact anchor: UK content model.
- objective: ensure no guaranteed-income/unsupported financial claims; acceptance: evidence-limited copy only; safe boundary: tests/content drafts; verification: negative-copy fixtures; next handoff: Marketing.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: draft only; negative_tests: guaranteed earnings/unsupported availability; receipt_evidence: claim→source pointer; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## Affiliate US subqueue
### C-US-01 — one high-value paid-participation proof packet
- status: PENDING; owner/workstream: Affiliate US; exact anchor: existing US research PR #6 lineage.
- objective: verify US availability, user reward, publisher/referral route and disclosure separately; acceptance: reward value and publisher eligibility separately evidenced; safe boundary: research only; verification: source matrix; next handoff: US shortlist.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research; negative_tests: reward evidence != affiliate eligibility; receipt_evidence: source/date/program; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: PENDING.
### C-US-02 — US destination/eligibility freshness
- status: PENDING; owner/workstream: Affiliate US; exact anchor: current corpus.
- objective: verify current US eligibility/outbound destination; acceptance: geo mismatch/stale terms fail closed; safe boundary: research/docs; verification: dated evidence; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: research; negative_tests: geo mismatch, stale route; receipt_evidence: source/date/destination; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.
### C-US-03 — disclosure-safe comparison row
- status: PENDING; owner/workstream: Affiliate US; exact anchor: current model.
- objective: produce one comparison-ready non-public row with explicit UNKNOWN publisher state; acceptance: no monetized CTA if not approved; safe boundary: docs only; verification: schema audit; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: docs; negative_tests: unknown relationship => fallback; receipt_evidence: row evidence; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## GhostKitchen subqueue
### C-GK-01 — pilot-menu evidence packet consume
- status: ACTIVE; owner/workstream: GhostKitchen; exact anchor: current main lineage with deterministic pilot-menu evidence packet; draft PR #32 owns economics metadata/evidence-summary hardening.
- objective: populate only verified/synthetic-labelled recipe/yield/packaging/labour/delivery inputs; acceptance: hypothesis/reference inputs never labeled verified profitability; safe boundary: docs/fixtures; verification: evidence completeness; next handoff: economics model.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-12,SG-14,SG-20`; risk_class: S1; authority_required: repo/research read-write; negative_tests: missing input => UNKNOWN; receipt_evidence: input/source/date/class; green_required: no; prs_required: no; owner_boundary: supplier contact/spend/production; security_disposition: ACTIVE.
### C-GK-02 — representative-order sensitivity
- status: PENDING; owner/workstream: GhostKitchen.
- objective: compute contribution sensitivity across delivery fee/food/packaging/labour bands using evidence-labelled inputs; acceptance: no profitability claim; safe boundary: local calculation/docs; verification: reproducible table; next handoff: readiness gate.
- security_gates: `SG-06,SG-10,SG-12,SG-14`; risk_class: S0; authority_required: local analysis; negative_tests: missing real input => hypothesis label; receipt_evidence: assumptions/results; green_required: no; prs_required: no; owner_boundary: spend/production; security_disposition: PENDING.
### C-GK-03 — fail-closed readiness fixture
- status: PENDING; owner/workstream: GhostKitchen.
- objective: deny readiness when supplier/recipe/yield/packaging/labour/delivery evidence missing; acceptance: deterministic UNKNOWN/HOLD; safe boundary: tests/fixtures; verification: fixture suite; next handoff: Overseer.
- security_gates: `SG-06,SG-10,SG-12,SG-14`; risk_class: S1; authority_required: non-prod tests; negative_tests: each missing evidence dimension; receipt_evidence: fixture/disposition; green_required: no; prs_required: no; owner_boundary: production; security_disposition: PENDING.

## Franchise subqueue
### C-FR-01 — active membership/tenancy fail-closed
- status: ACTIVE; owner/workstream: Franchise; exact anchor: draft PR #24 duplicate-active-membership handling + PR #22 territory-status/determinism fixtures.
- objective: preserve tenancy/membership prerequisite before territory routing; acceptance: duplicate/overlap/inactive tenant denied; safe boundary: synthetic tests; verification: exact fixture tests; next handoff: C-FR-02.
- security_gates: `SG-06,SG-07,SG-10,SG-12,SG-14,SG-20`; risk_class: S2; authority_required: non-prod tests; negative_tests: duplicate active membership, overlap, stale tenant; receipt_evidence: tenant/territory/version/disposition; green_required: conditional; prs_required: no; owner_boundary: production tenancy/routing; security_disposition: ACTIVE.
### C-FR-02 — territory overlap matrix
- status: PENDING; owner/workstream: Franchise.
- objective: expand homogeneous synthetic cases for exact/partial/nested territory overlap; acceptance: deterministic deny/route result with version correlation; safe boundary: fixtures; verification: test matrix; next handoff: audit receipt.
- security_gates: `SG-09,SG-10,SG-11,SG-12,SG-14`; risk_class: S2; authority_required: non-prod tests; negative_tests: duplicate/overlap/stale version; receipt_evidence: tenant/territory/version/result; green_required: conditional; prs_required: no; owner_boundary: production; security_disposition: PENDING.
### C-FR-03 — deterministic audit handoff
- status: PENDING; owner/workstream: Franchise.
- objective: ensure synthetic routing decision carries exact tenancy/territory/evidence version; acceptance: mismatch/stale version cannot be success; safe boundary: tests/docs; verification: receipt fixture; next handoff: Overseer.
- security_gates: `SG-10,SG-11,SG-14`; risk_class: S1; authority_required: non-prod tests; negative_tests: stale/mismatch evidence; receipt_evidence: exact IDs/version; green_required: no; prs_required: no; owner_boundary: production; security_disposition: PENDING.

## GemVerse subqueue
### C-GV-01 — current recovery assurance ownership
- status: ACTIVE; owner/workstream: GemVerse; exact anchor: draft PR #10 fixture recovery assurance; current project workload definition remains non-production.
- objective: consume existing PR work, not duplicate it; acceptance: exact preimage/target identity, replay/idempotence and competing candidate denial remain explicit; safe boundary: fixtures/tests; verification: exact PR CI; next handoff: C-GV-02.
- security_gates: `SG-06,SG-07,SG-09,SG-10,SG-11,SG-14,SG-20`; risk_class: S2; authority_required: non-prod tests; negative_tests: stale preimage, competing candidate, replay/recovery; receipt_evidence: source/target/preimage/result; green_required: conditional; prs_required: no; owner_boundary: production mutation; security_disposition: ACTIVE.
### C-GV-02 — canon dependency packet
- status: BLOCKED; owner/workstream: GemVerse.
- objective: distinguish verified creator/source canon from documentation hypothesis; acceptance: no executable implementation claim absent canon; dependencies: verified canon; safe boundary: read/docs only; verification: evidence pointers; next handoff: project owner when canon exists.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-20`; risk_class: S1; authority_required: read-only; negative_tests: docs-only source cannot authorize implementation; receipt_evidence: canon source/version; green_required: no; prs_required: no; owner_boundary: product canon/production; security_disposition: BLOCKED.
### C-GV-03 — Level-2 fixture readiness
- status: PENDING; owner/workstream: GemVerse.
- objective: keep governed mutation fixture ready for AgentOS acceptance without creating alternate control plane; acceptance: bounded files, expected pre/postimage, rollback/replay/receipt oracle; dependencies: existing fixture only; safe boundary: fixture docs/tests; verification: deterministic local test; next handoff: AgentOS only after Level-2 mutation gate clears.
- security_gates: `SG-03,SG-09,SG-10,SG-11,SG-14`; risk_class: S1; authority_required: fixture-only; negative_tests: wrong preimage/replay/out-of-scope file; receipt_evidence: fixture IDs/hashes; green_required: no; prs_required: no; owner_boundary: physical/production execution; security_disposition: PENDING.

## Content360 subqueue
### C-C360-01 — current mock secret-isolation baseline
- status: VERIFIED; owner/workstream: Content360; exact anchor: PR #4 `6b72ea670ddeec5fe1699d8a13fa403e37d437d3`; Tests `34846314212` SUCCESS.
- objective: preserve opaque credential references/no secret persistence; acceptance: no secret in prompt/log/receipt/fixture; safe boundary: mocks/tests; verification: exact CI; next handoff: C-C360-02.
- security_gates: `SG-05,SG-06,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: non-prod tests; negative_tests: secret in metadata/log/result; receipt_evidence: redacted mock receipt; green_required: conditional; prs_required: no; owner_boundary: credentials/live provider/publish; security_disposition: VERIFIED.
### C-C360-02 — prompt-injection/provider-output boundary
- status: PENDING; owner/workstream: Content360.
- objective: adversarially prove provider/content output cannot authorize PUBLISH/SCHEDULE/tool escalation; acceptance: READ/OPTIMISE remains bounded; safe boundary: mocked tests; verification: fixture suite; next handoff: adapter.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15,SG-17`; risk_class: S2; authority_required: mock tests; negative_tests: publish instruction, secret request, memory write, capability escalation; receipt_evidence: request/result/disposition; green_required: conditional; prs_required: no; owner_boundary: live network/account mutation; security_disposition: PENDING.
### C-C360-03 — correlation/idempotency failure fixtures
- status: PENDING; owner/workstream: Content360.
- objective: verify duplicate request/result, timeout/retry and mismatched correlation do not fabricate successful optimization; acceptance: deterministic PARTIAL/FAIL/duplicate disposition; safe boundary: mocks/tests; verification: exact CI; next handoff: adapter evidence.
- security_gates: `SG-09,SG-10,SG-11,SG-17`; risk_class: S2; authority_required: mock tests; negative_tests: duplicate, timeout, replay, mismatch; receipt_evidence: request/result IDs/status; green_required: conditional; prs_required: no; owner_boundary: live provider; security_disposition: PENDING.
### C-C360-04 — official API/auth capability evidence
- status: BLOCKED; owner/workstream: Content360.
- objective: keep live API/auth/PUBLISH/SCHEDULE capabilities UNKNOWN until official evidence/owner authority; acceptance: no inference from mock adapter; safe boundary: public documentation research only; verification: official docs; next handoff: owner if credentials/account action becomes necessary.
- security_gates: `SG-02,SG-05,SG-06,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public docs only; negative_tests: mock capability != live authority; receipt_evidence: official docs/date/capability; green_required: no; prs_required: no; owner_boundary: credentials/account/live publish; security_disposition: BLOCKED.

## Commercial Frontend subqueue
### C-CF-01 — existing Tradie value-threshold work
- status: ACTIVE; owner/workstream: Commercial Frontend; exact anchor: Overseer draft PR #50.
- objective: consume active value-threshold work before adding adjacent implementation; acceptance: pain/demand/WTP remain hypothesis unless externally evidenced; safe boundary: docs/fixtures/prototype only; verification: evidence packet; next handoff: C-CF-02.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-12,SG-14,SG-20`; risk_class: S1; authority_required: repo docs/prototype; negative_tests: internal hypothesis != demand proof; receipt_evidence: claim/evidence source; green_required: no; prs_required: no; owner_boundary: customer contact/deployment; security_disposition: ACTIVE.
### C-CF-02 — bounded exception-workflow packet
- status: PENDING; owner/workstream: Commercial Frontend.
- objective: define one Tradie/service-ops exception from input→recommended correction→receipt with no production action; acceptance: measurable time/error/value hypothesis fields explicit; safe boundary: synthetic artifact; verification: fixture walkthrough; next handoff: integration feasibility.
- security_gates: `SG-06,SG-10,SG-11,SG-12,SG-14`; risk_class: S1; authority_required: non-prod prototype/docs; negative_tests: unsupported correction/authority escalation; receipt_evidence: input/correction/result; green_required: no; prs_required: no; owner_boundary: deployment/account mutation; security_disposition: PENDING.
### C-CF-03 — operator evidence gap register
- status: PENDING; owner/workstream: Commercial Frontend.
- objective: make frequency/friction/WTP UNKNOWNs explicit and separate technical feasibility from market proof; acceptance: no commercial-ready claim; safe boundary: research synthesis; verification: evidence-gap table; next handoff: future owner-authorized validation.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-20`; risk_class: S0; authority_required: read/research; negative_tests: internal assumptions cannot become WTP evidence; receipt_evidence: source/gap/date; green_required: no; prs_required: no; owner_boundary: customer contact; security_disposition: PENDING.

## Marketing subqueue
### C-MKT-01 — AgentOS readiness/claim reconciliation
- status: ACTIVE; owner/workstream: Marketing; exact anchor: Marketing batch `9fb9189142d1580e5076a02eec70d1b04906d95e`; log `2e3384d409998623fc8bbc45b9cb9a6d581f0496`; PR #111 `146f1118...` CI red.
- objective: keep claims consistent with exact #104/#111 readiness; acceptance: no Founding Beta/shipped/Level-2-ready claim while gates/CI red; safe boundary: internal copy/docs; verification: claim→evidence pointer; next handoff: Marketing assets.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: internal drafts only; negative_tests: shipped/ready claim without exact evidence; receipt_evidence: claim/evidence IDs; green_required: no; prs_required: no; owner_boundary: campaign/publication/spend; security_disposition: ACTIVE.
### C-MKT-02 — GlobalShopCo claim-safe product messaging
- status: PENDING; owner/workstream: Marketing.
- exact anchor: `0 eBay-ready SKUs`; OXO screen `181e450...`; CARLA/OXO evidence queue.
- objective: prepare only evidence-safe non-paid internal messaging templates that require exact SKU/price/availability/freight/returns/assets before insertion; acceptance: no named approved supplier/eBay-ready claim; safe boundary: drafts; verification: negative-copy checklist; next handoff: Content360 after product qualification.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: internal drafts; negative_tests: missing freight/stock/permission/assets => omit claim; receipt_evidence: placeholder/evidence schema; green_required: no; prs_required: no; owner_boundary: publication/campaign/spend; security_disposition: PENDING.
### C-MKT-03 — Affiliate country claim-evidence pointer index
- status: PENDING; owner/workstream: Marketing.
- exact anchor: AU `2d654dee...` + UK/US current proof-gated lanes.
- objective: map each reward/referral/publisher/disclosure claim to country-specific evidence; acceptance: member referral never implied publisher partnership; stale/unknown evidence suppresses claim; safe boundary: internal docs; verification: pointer audit; next handoff: Content360/affiliate pages.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: internal docs; negative_tests: cross-country leakage, unsupported partner claim; receipt_evidence: claim/source/date/country; green_required: no; prs_required: no; owner_boundary: publication/outreach; security_disposition: PENDING.

## Lane health after replenishment
- **Lane A:** multiple actionable PENDING items remain (A-AG-03, A-AG-04 assurance adjacency, A-PRS-04) while SG-08/SG-01/02/physical blockers remain explicit.
- **Lane B:** multiple actionable PENDING items remain across GSC economics, eBay receipt semantics, Amazon freshness, Headless synthetic handoff and MyPrime evidence/funnel work. External permission/freight/provider/live environment blockers do not starve synthetic/read-only closure.
- **Lane C:** every scheduled workstream has at least one actionable next item or explicit blocker, with active-PR ownership preserved and no duplicate work assigned.

**No overall GREEN.**