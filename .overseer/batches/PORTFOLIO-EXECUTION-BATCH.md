# Portfolio Execution Batch Manifest

**Purpose:** scheduled queue state for the owner-selected core projects only. Canonical procedure: `.overseer/doctrine/PORTFOLIO-BATCH-ENGINE.md`; shaping: `.overseer/profiles/PROJECT-BATCH-PROFILES.md`; security: `.overseer/security/AGENTOS-SECURITY-GATE-MATRIX.md`. Repository/runtime/CI evidence always outranks this file.

**Scheduled scope:** AgentOS, PRS, GlobalShopCo, GlobalShopCo-Headless, shopify_ebay, MyPrimeDelivery. All other portfolio projects are owner-manual; their durable state is untouched.

**States:** `PENDING | ACTIVE | VERIFIED | BLOCKED | STALE | SPLIT_REQUIRED`.

**Core invariant:** **NO MODEL DECIDES ITS OWN AUTHORITY.** No merge/approve/ready/rebase/deploy/credentials/security-policy changes/production writes/purchases/spend/supplier contact/live publication/physical owner-host action/production autonomy. Functional, security, Green and PRS status remain independent.

## Checkpoint reconciliation — 2026-09-15 10:32 Brisbane
- **AgentOS:** PR #104 remains OPEN/DRAFT/UNMERGED at exact `4c8bcc3bc2ad2041b0a1871d3004c1db23f3c091`; its PR text explicitly keeps SG-08 continuous ownership and SG-01/02 authenticated actor/canonical grant wiring unproven. Prior exact-head cross-platform CI is bounded functional evidence only. PR #112 is independently ACTIVE at exact `d1645450a06d00c49a7a78f176e97b44b9eaa225`, consolidating runtime-shell eligibility and rejecting asserted `eligible:true` without canonical capability results; it explicitly does not touch the #104 mutation hot path. Do not duplicate #112 work into #104.
- **PRS:** PR #24 is OPEN/DRAFT at exact `3039c886bdcff911f7c6dcc3e086368058e57fb6`; its embedded AgentOS target is historical/stale for current-head certification. PRS remains independent: completion-grade ownership assurance waits for a real SG-08 repair and identical-head Green PASS.
- **GlobalShopCo:** PR #30 remains OPEN/DRAFT at exact `80c82475b98663d677885e8b4d222ae2cedb8555`, stacked on #29 `15fa99eb4c4b1f96127f6f51c412cbffc94e45e2`. It records no new authenticated supplier/app evidence. `0 eBay-ready SKUs` remains controlling.
- **GlobalShopCo-Headless:** PR #1 remains OPEN/DRAFT at exact `4e66a67d3680bd59e3b4da923f9ef291aa6fa358`; bounded secret-boundary evidence is retained only at exact lineage. No live checkout/deploy authority.
- **shopify_ebay:** no open PRs. Default lineage is exact `c68883f24fb3711fce567a35b1a80db74933b82a`; prior bounded channel-gate/replay evidence remains non-production. No durable adapter-local replay store has been evidenced, so restart durability stays BLOCKED pending discovery of an existing upstream canonical caller/store.
- **MyPrimeDelivery:** current research lineage remains exact `61feceb46de539948374deec86b3fe7578cf8014`; latest change fails closed on conflicting known ASIN identity. Qualification remains synthetic/non-production; live `QUALIFIED=0`. Divergent WordPress/research lineage must be reconciled without stale overwrite.

# AGENTOS — Level 2 P0

### A-AG-01 — continuous project-file ownership fence
- status: BLOCKED; owner/workstream: AgentOS; anchor: `AgentOS#104@4c8bcc3bc2ad2041b0a1871d3004c1db23f3c091`.
- objective: repair the existing single writer so one crash-releasing ownership primitive remains continuously valid through final verify -> publish/prepared recovery -> durable success receipt -> release.
- acceptance: replacement after verify/publish/receipt, successor/three-writer, stale identity, TOCTOU, crash/replay and prepared-recovery stale-owner all fail before durable success.
- dependencies: existing #104 writer seam only; safe action boundary: bounded branch code/tests, no second lock/ledger/control plane; verification: unchanged negatives + exact-head Ubuntu/Windows CI; next handoff: identical head -> Green -> PRS.
- security_gates: `SG-03,SG-08,SG-09,SG-10,SG-11,SG-14,SG-18,SG-19`; risk_class: S2; authority_required: scoped branch/test write; negative_tests: ownership replacement matrix; receipt_evidence: actor/task/file/pre-postimage/ownership/result/head/run; green_required: yes; prs_required: yes; owner_boundary: merge/deploy/physical/production; security_disposition: BLOCKED.

### A-AG-02 — authenticated actor + canonical grant binding
- status: BLOCKED; owner/workstream: AgentOS; anchor: `#104@4c8bcc3...` admission composition seam.
- objective: bind only an existing authenticated actor source and canonical grant resolver; acceptance: no caller self-identity/self-grant, and absent/spoofed/mismatch/cross-project/replay denies admission/success.
- dependencies: real source provenance; safe action boundary: discovery/tests only until evidenced; verification: spoof/mismatch/replay matrix; next handoff: implementation only after canonical source is identified.
- security_gates: `SG-01,SG-02,SG-03,SG-04,SG-09,SG-10,SG-11,SG-18,SG-19`; risk_class: S2; authority_required: canonical identity/grant read; negative_tests: host-as-auth/spoof/self-grant/mismatch/replay; receipt_evidence: issuer/source/version/request/task/mission; green_required: yes; prs_required: yes; owner_boundary: credentials/security policy; security_disposition: BLOCKED.

### A-AG-03 — runtime-shell eligibility consolidation
- status: ACTIVE; owner/workstream: AgentOS; anchor: `AgentOS#112@d1645450a06d00c49a7a78f176e97b44b9eaa225`.
- objective: preserve one canonical capability normalization/evaluation path without widening authority; acceptance: aliases normalize deterministically, compatibility adapter reuses canonical evaluator, asserted eligibility without canonical results is denied.
- dependencies: existing capability contracts; safe action boundary: #112 only, no #104 mutation seam; verification: exact-head CI + adjacent unauthorized-capability negatives; next handoff: bounded Green only if promotion is proposed.
- security_gates: `SG-02,SG-03,SG-04,SG-10,SG-18`; risk_class: S2; authority_required: scoped branch/test write; negative_tests: asserted eligible, alias confusion, absent canonical result, adjacent capability; receipt_evidence: exact head/run/test identities; green_required: yes for promotion; prs_required: no unless authority surface widens; owner_boundary: merge/deploy/production; security_disposition: ACTIVE.

### A-AG-04 — replay/correlation remainder
- status: SPLIT_REQUIRED; owner/workstream: AgentOS; anchor: current #104 lineage.
- objective: split conflicting replay, duplicate result, restart duplicate and freshness semantics into homogeneous slices; acceptance: first-write provenance preserved and no invented freshness source.
- dependencies: canonical recovery semantics; safe action boundary: 2–5 tests/minimal validation; verification: exact-head CI; next handoff: Green SG-09/10/11.
- security_gates: `SG-09,SG-10,SG-11,SG-14,SG-18`; risk_class: S2; authority_required: scoped tests; negative_tests: conflicting payload/same identity, duplicate result, restart duplicate; receipt_evidence: claim/recovery IDs + first-write provenance; green_required: yes; prs_required: conditional; owner_boundary: no new persistence/authority plane; security_disposition: SPLIT_REQUIRED.

### A-AG-05 — physical Windows acceptance packet
- status: BLOCKED; owner/workstream: AgentOS; anchor: current #104 lineage.
- objective: preserve owner-run checklist only; acceptance: exact SHA/root/mutation/recovery/correlation/no-production boundaries; dependencies: A-AG-01/02 + Green/PRS + explicit owner physical authority; safe action boundary: docs/checklist; verification: future owner evidence; next handoff: owner only.
- security_gates: `SG-03,SG-08,SG-10,SG-11,SG-14,SG-18,SG-20`; risk_class: S2; authority_required: explicit owner physical Windows action; negative_tests: wrong head/root/missing receipt/production target; receipt_evidence: head/host/root/result; green_required: yes; prs_required: yes; owner_boundary: physical Windows; security_disposition: BLOCKED.

# PRS — independent assurance

### A-PRS-01 — historical false-GREEN baseline
- status: VERIFIED; owner/workstream: PRS; anchor: `PRS#17@49fe1f8bca3ddae271d85e0f4767173060267222`.
- objective: preserve immutable historical ownership/admission defect evidence without successor certification; acceptance: exact target/artifact identity stable; dependencies: none; safe action boundary: read-only; verification: hashes; next handoff: A-AG-01/02.
- security_gates: `SG-01,SG-02,SG-08,SG-10,SG-11,SG-19`; risk_class: S0; authority_required: read; negative_tests: historical stale-owner/admission cases; receipt_evidence: exact hashes; green_required: no; prs_required: baseline; owner_boundary: none; security_disposition: VERIFIED.

### A-PRS-02 — current-head bounded challenge
- status: PENDING; owner/workstream: PRS; anchor: `AgentOS#104@4c8bcc3...` plus current #104 evidence.
- objective: independently challenge bounded replay/correlation/receipt and defect-baseline behavior without claiming completion; acceptance: exact target identity and independent classifications; dependencies: unchanged target; safe action boundary: harness/read/test; verification: immutable target/artifact hashes; next handoff: AgentOS Overseer.
- security_gates: `SG-08,SG-09,SG-10,SG-11,SG-19`; risk_class: S1; authority_required: read/test; negative_tests: stale owner/replay/correlation/receipt ordering; receipt_evidence: target/artifact/outcome hashes; green_required: no for defect confirmation; prs_required: yes; owner_boundary: merge/deploy; security_disposition: PENDING.

### A-PRS-03 — completion-grade ownership challenge
- status: BLOCKED; owner/workstream: PRS; anchor: `PRS#24@3039c886bdcff911f7c6dcc3e086368058e57fb6` contract + future repaired AgentOS head.
- objective: rerun normal/prepared/successor/crash/replay ownership matrix only after real SG-08 repair and identical-head Green PASS; acceptance: no inherited claims; dependencies: A-AG-01 + Green; safe action boundary: assurance harness; verification: exact hashes; next handoff: Overseer #49.
- security_gates: `SG-08,SG-09,SG-10,SG-11,SG-18,SG-19`; risk_class: S2; authority_required: bounded harness; negative_tests: full ownership matrix; receipt_evidence: target/artifact/Green lineage; green_required: prerequisite; prs_required: yes; owner_boundary: merge/deploy; security_disposition: BLOCKED.

### A-PRS-04 — physical Windows evidence contract freshness
- status: PENDING; owner/workstream: PRS; anchor: `PRS#24@3039c886...`.
- objective: ensure the contract requires exact AgentOS head, host/root, mutation/recovery/correlation and independent artifact identity; acceptance: stale/missing/mismatched evidence cannot pass; dependencies: none; safe action boundary: docs/tests; verification: repository validation; next handoff: owner-run acceptance only after gates close.
- security_gates: `SG-10,SG-11,SG-19,SG-20`; risk_class: S1; authority_required: docs/test; negative_tests: stale head, wrong host/root, missing artifact; receipt_evidence: contract version/head; green_required: no; prs_required: yes when executed; owner_boundary: physical host; security_disposition: PENDING.

# GLOBALSHOPCO

### B-GSC-01 — authenticated supplier evidence closure
- status: ACTIVE; owner/workstream: GlobalShopCo; anchor: `#29@15fa99eb4c4b1f96127f6f51c412cbffc94e45e2`, `#30@80c82475b98663d677885e8b4d222ae2cedb8555`.
- objective: close exact SKU rows only with authenticated trade cost, packaged freight/free-delivery basis, permission, stock identity, returns/warranty; acceptance: source/date/identity traceable, missing material field => HOLD.
- dependencies: current research rows; safe action boundary: read-only research/data/docs; verification: provenance audit; next handoff: B-GSC-02.
- security_gates: `SG-02,SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read-only evidence; negative_tests: retail-as-wholesale/contradictory freight/inferred permission/stale stock; receipt_evidence: source/date/SKU/cost/freight/status; green_required: no; prs_required: no; owner_boundary: supplier contact/purchase/Shopify mutation; security_disposition: ACTIVE.

### B-GSC-02 — conservative delivered-margin gate
- status: PENDING; owner/workstream: GlobalShopCo; anchor: `#29/#30`.
- objective: calculate delivered contribution only for evidence-complete rows; acceptance: fees/freight/returns allowance explicit and UNKNOWN => HOLD; dependencies: B-GSC-01; safe action boundary: deterministic calculator/data; verification: missing/contradiction fixtures; next handoff: B-GSC-03.
- security_gates: `SG-10,SG-12,SG-13,SG-14,SG-20`; risk_class: S1; authority_required: non-production calculation; negative_tests: unknown freight/fee/cost, negative margin, stale quote; receipt_evidence: inputs/calculator/disposition; green_required: no; prs_required: no; owner_boundary: spend/listing; security_disposition: PENDING.

### B-GSC-03 — bounded eBay shortlist
- status: BLOCKED; owner/workstream: GlobalShopCo; anchor: controlling truth `0 eBay-ready SKUs`.
- objective: produce 2–5 candidates only after upstream evidence clears; acceptance: exact variant/SKU + permission + stock + delivered economics + returns/warranty; dependencies: B-GSC-01/02; safe action boundary: shortlist only; verification: fail-closed schema; next handoff: shopify_ebay fixture.
- security_gates: `SG-02,SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read; negative_tests: any missing field => HOLD; receipt_evidence: candidate packet; green_required: no; prs_required: no; owner_boundary: publication/contact/spend; security_disposition: BLOCKED.

### B-GSC-04 — compact pet-accessory evidence mini-batch
- status: PENDING; owner/workstream: GlobalShopCo; anchor: #30 next-cycle direction.
- objective: evaluate 2–5 compact/light AU-stock candidates without widening category count; acceptance: exact identity, supplier provenance, freight, permission, stock and returns captured or HOLD; dependencies: public/authenticated evidence availability; safe action boundary: research only; verification: row provenance audit; next handoff: B-GSC-01.
- security_gates: `SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read-only research; negative_tests: syndicated identity conflict, missing freight, inferred permission; receipt_evidence: source/date/SKU/status; green_required: no; prs_required: no; owner_boundary: contact/purchase/listing; security_disposition: PENDING.

# GLOBALSHOPCO-HEADLESS

### B-HDL-01 — checkout secret-boundary baseline
- status: VERIFIED; owner/workstream: Headless; anchor: `#1@4e66a67d3680bd59e3b4da923f9ef291aa6fa358` + prior exact-head bounded CI.
- objective: preserve denial of secret-shaped values in cart/GraphQL/HTTP errors; acceptance: regression remains fail-closed; safe action boundary: tests; verification: exact-head CI; next handoff: B-HDL-02.
- security_gates: `SG-05,SG-06,SG-14`; risk_class: S1; authority_required: read/test; negative_tests: error-path leaks; receipt_evidence: exact head/run; green_required: no; prs_required: no; owner_boundary: secrets/deploy/live purchase; security_disposition: VERIFIED.

### B-HDL-02 — destination/host edge inventory
- status: PENDING; owner/workstream: Headless; anchor: `4e66a67d...`.
- objective: identify only genuinely uncovered scheme/userinfo/port/subdomain/canonical-host confusion cases; acceptance: 2–5 homogeneous gaps max; dependencies: suite inventory; safe action boundary: read/test; verification: exact-head CI; next handoff: Headless Overseer.
- security_gates: `SG-06,SG-10,SG-14`; risk_class: S1; authority_required: tests; negative_tests: malformed destination/host confusion; receipt_evidence: coverage map/head/run; green_required: no; prs_required: no; owner_boundary: deploy/live checkout; security_disposition: PENDING.

### B-HDL-03 — Shopify canonical checkout projection
- status: PENDING; owner/workstream: Headless; anchor: `#1@4e66a67d...` architecture boundary.
- objective: prove WordPress cannot become order/payment authority; acceptance: only canonical Shopify checkout destination accepted, local payment/order mutation absent; dependencies: existing contract; safe action boundary: synthetic tests/docs; verification: host/order/payment negatives; next handoff: project Overseer.
- security_gates: `SG-02,SG-05,SG-06,SG-10,SG-14,SG-20`; risk_class: S1; authority_required: test/docs; negative_tests: local order authority, alternate checkout host, secret leakage; receipt_evidence: contract/head/run; green_required: no; prs_required: no; owner_boundary: Shopify mutation/deploy/live purchase; security_disposition: PENDING.

### B-HDL-04 — exact product identity/availability contradictions
- status: PENDING; owner/workstream: Headless; anchor: current M3 contract.
- objective: add 2–5 deterministic stale/mismatched product/variant/availability negatives; acceptance: no stale/mismatched item can form checkout payload; dependencies: fixture schema; safe action boundary: synthetic tests; verification: exact-head CI; next handoff: B-HDL-03.
- security_gates: `SG-06,SG-09,SG-10,SG-14`; risk_class: S1; authority_required: tests; negative_tests: variant mismatch/stale availability/duplicate cart identity; receipt_evidence: fixture/head/run; green_required: no; prs_required: no; owner_boundary: production commerce; security_disposition: PENDING.

# SHOPIFY -> EBAY

### B-EBAY-01 — upstream durable replay-store discovery
- status: BLOCKED; owner/workstream: shopify_ebay; anchor: default `c68883f24fb3711fce567a35b1a80db74933b82a`; no open PRs.
- objective: trace the integration caller to an existing canonical Shopify/AgentOS-approved durable replay store; acceptance: exact owner/source/schema/lifecycle identified or explicit NONE; dependencies: integration topology; safe action boundary: read-only discovery; verification: code/path provenance; next handoff: B-EBAY-02 only if a real store exists.
- security_gates: `SG-02,SG-09,SG-10,SG-11,SG-14`; risk_class: S1; authority_required: read; negative_tests: caller-supplied seen IDs treated as durable, invented local store; receipt_evidence: caller/store/path/head; green_required: no; prs_required: no; owner_boundary: no new ledger/persistence/production; security_disposition: BLOCKED.

### B-EBAY-02 — restart replay durability negatives
- status: BLOCKED; owner/workstream: shopify_ebay; anchor: `c68883f...`.
- objective: 2–5 restart duplicate/conflict/result-write replay tests preserving first-write provenance; acceptance: durable store survives process restart and conflicts fail closed; dependencies: B-EBAY-01; safe action boundary: synthetic tests only; verification: exact-head CI; next handoff: bounded Green if authority surface changes.
- security_gates: `SG-09,SG-10,SG-11,SG-14`; risk_class: S2; authority_required: scoped test write; negative_tests: restart duplicate/conflict/result-write failure; receipt_evidence: event/hash/first-write/head/run; green_required: conditional; prs_required: no; owner_boundary: production publication; security_disposition: BLOCKED.

### B-EBAY-03 — evidence-complete SKU admission fixture
- status: BLOCKED; owner/workstream: shopify_ebay; anchor: `c68883f...`, GlobalShopCo `0 eBay-ready SKUs`.
- objective: map one real evidence-complete Shopify variant only when supplied; acceptance: exact SKU/variant, permission, stock, economics, seller/fulfilment evidence; dependencies: B-GSC-03; safe action boundary: fixture only; verification: fail-closed gate; next handoff: no live listing.
- security_gates: `SG-02,SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: non-production fixture; negative_tests: missing permission/stock/fee/freight/seller; receipt_evidence: mapping packet/head/run; green_required: no; prs_required: no; owner_boundary: eBay network/listing/spend; security_disposition: BLOCKED.

### B-EBAY-04 — synthetic mapper identity regression
- status: PENDING; owner/workstream: shopify_ebay; anchor: `c68883f...` + prior channel-gate tests.
- objective: preserve exact variant/SKU/event mapping under malformed/duplicate inputs; acceptance: 2–5 homogeneous identity negatives only, no live API; dependencies: existing fixtures; safe action boundary: tests; verification: exact-head fixture CI; next handoff: B-EBAY-01/03.
- security_gates: `SG-06,SG-09,SG-10,SG-14`; risk_class: S1; authority_required: tests; negative_tests: variant mismatch, duplicate event, malformed ID, conflicting hash; receipt_evidence: fixture/head/run; green_required: no; prs_required: no; owner_boundary: publication/network; security_disposition: PENDING.

# MYPRIMEDELIVERY

### B-MPD-01 — research vs WordPress lineage reconciliation
- status: ACTIVE; owner/workstream: MyPrimeDelivery; anchors: research `61feceb46de539948374deec86b3fe7578cf8014`; WordPress fixture `a38684c10541115f55f1d5612b72d669dced99f0`.
- objective: produce compatibility/conflict map before integration; acceptance: exact common ancestor, changed paths/contracts and conflict classes recorded; dependencies: both lineages; safe action boundary: read/docs/tests, no merge/rebase/stale overwrite; verification: exact compare + fixture checks; next handoff: B-MPD-04.
- security_gates: `SG-10,SG-11,SG-14,SG-20`; risk_class: S1; authority_required: read/docs; negative_tests: stale overwrite/wrong ancestor/fixture drift; receipt_evidence: heads/ancestor/path map; green_required: no; prs_required: no; owner_boundary: merge/deploy/publication; security_disposition: ACTIVE.

### B-MPD-02 — authoritative source/right-to-use evidence queue
- status: PENDING; owner/workstream: MyPrimeDelivery; anchor: research `61feceb...`; current truth `100 concepts / 0 live QUALIFIED`.
- objective: exact ASIN + current product-level Prime + freshness + owner-approved ranking + source rights + outbound destination from authorised evidence; acceptance: one coherent observation carries every gate; dependencies: authoritative sources; safe action boundary: read-only evidence; verification: provenance/freshness audit; next handoff: qualification fixture.
- security_gates: `SG-02,SG-06,SG-10,SG-12,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read-only authorised evidence; negative_tests: editorial-as-authority/stale Prime/conflicting ASIN/missing rights; receipt_evidence: source/date/ASIN/Prime/rank/rights/destination; green_required: no; prs_required: no; owner_boundary: provider signup/credentials/publication; security_disposition: PENDING.

### B-MPD-03 — coherent qualification regression preservation
- status: VERIFIED; owner/workstream: MyPrimeDelivery; anchor: `61feceb46de539948374deec86b3fe7578cf8014` + prior fixture validation.
- objective: preserve fail-closed coherent observation and conflicting-known-ASIN denial; acceptance: independent observations cannot combine and conflicting identity cannot qualify; dependencies: none; safe action boundary: tests; verification: exact-head fixture CI; next handoff: only genuinely uncovered contradictions.
- security_gates: `SG-06,SG-09,SG-10,SG-14`; risk_class: S1; authority_required: test/read; negative_tests: split evidence/conflicting ASIN/stale observation; receipt_evidence: exact head/run/fixture; green_required: no; prs_required: no; owner_boundary: live publication/network; security_disposition: VERIFIED.

### B-MPD-04 — WordPress non-production presentation adapter
- status: PENDING; owner/workstream: MyPrimeDelivery; anchor: B-MPD-01 compatibility map + WordPress `a38684c...`.
- objective: project only QUALIFIED fixture data into WordPress presentation without inventing Prime/rank/deal authority; acceptance: HOLD/UNKNOWN never renders monetized/live CTA and outbound destination is exact; dependencies: B-MPD-01 + qualification schema; safe action boundary: fixture/template tests only; verification: stale/HOLD/destination negatives; next handoff: owner review, not publication.
- security_gates: `SG-05,SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: non-production fixture/template write; negative_tests: HOLD render, stale deal, destination mismatch, secret leakage; receipt_evidence: source row/template/head/run; green_required: yes if promoted; prs_required: no; owner_boundary: WordPress credentials/live publication; security_disposition: PENDING.

### B-MPD-05 — freshness/identity contradiction mini-batch
- status: PENDING; owner/workstream: MyPrimeDelivery; anchor: `61feceb...`.
- objective: add 2–5 genuinely uncovered homogeneous contradictions without increasing raw concept count; acceptance: stale Prime/rank/deal or identity conflict fails closed; dependencies: existing validator; safe action boundary: fixtures/tests; verification: exact-head CI; next handoff: B-MPD-02/04.
- security_gates: `SG-06,SG-09,SG-10,SG-14`; risk_class: S1; authority_required: tests; negative_tests: freshness boundary/conflicting source/outbound mismatch; receipt_evidence: fixture/head/run; green_required: no; prs_required: no; owner_boundary: publication/network; security_disposition: PENDING.

## Replenishment order
1. AgentOS A-AG-01 remains P0; A-AG-03 (#112) may continue independently because it does not touch the blocked mutation seam. A-AG-02 remains fail-closed discovery only.
2. PRS may run bounded current-head defect challenges; completion certification waits for repaired identical-head Green.
3. GlobalShopCo closes authenticated supplier evidence; external blockage must not starve Headless/eBay/MyPrime safe fixture work.
4. shopify_ebay must discover an existing upstream durable replay owner/store or remain BLOCKED; never invent local persistence.
5. MyPrimeDelivery reconciles divergent lineages, then deepens authoritative qualification evidence; raw concept count is not the target.
6. Headless closes only uncovered deterministic boundary cases while Shopify remains canonical checkout/commercial authority.

**No overall GREEN. Scheduled work outside these six projects remains untouched.**