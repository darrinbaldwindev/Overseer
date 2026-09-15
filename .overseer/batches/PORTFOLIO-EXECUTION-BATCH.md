# Portfolio Execution Batch Manifest

**Purpose:** rolling scheduled queue for owner-selected core projects only. Canonical procedure: `.overseer/doctrine/PORTFOLIO-BATCH-ENGINE.md`; shaping: `.overseer/profiles/PROJECT-BATCH-PROFILES.md`; security: `.overseer/security/AGENTOS-SECURITY-GATE-MATRIX.md`. Repository/runtime/CI evidence outranks this file.

**Scheduled scope only:** AgentOS, PRS, GlobalShopCo, GlobalShopCo-Headless, shopify_ebay, MyPrimeDelivery. All other portfolio projects are owner-manual and are not consumed/replenished here.

**States:** `PENDING | ACTIVE | VERIFIED | BLOCKED | STALE | SPLIT_REQUIRED`.

**Invariant:** **NO MODEL DECIDES ITS OWN AUTHORITY.** No merge/approve/ready/rebase/deploy/credentials/security-policy changes/production writes/purchases/spend/supplier contact/live publication/physical owner-host action/production autonomy. Functional, security, Green and PRS status remain independent.

## Checkpoint reconciliation — 2026-09-15 11:30 Brisbane
- **AgentOS:** #104 unchanged exact `4c8bcc3bc2ad2041b0a1871d3004c1db23f3c091`, OPEN/DRAFT/UNMERGED. SG-08 and SG-01/02 remain BLOCKED_STABLE; do not rediscover until head/source evidence changes. #112 remains independently ACTIVE exact `d1645450a06d00c49a7a78f176e97b44b9eaa225` and must not touch #104 mutation ownership.
- **PRS:** #24 unchanged exact `3039c886bdcff911f7c6dcc3e086368058e57fb6`; completion-grade PRS remains BLOCKED_STABLE pending repaired AgentOS head + identical-head Jess functional PASS + Michael security PASS. Historical #17 is baseline only.
- **GlobalShopCo:** #30 unchanged exact `80c82475b98663d677885e8b4d222ae2cedb8555` on #29 `15fa99eb4c4b1f96127f6f51c412cbffc94e45e2`; no authenticated supplier/app evidence closes cost+freight+permission+stock. `0 eBay-ready SKUs` remains controlling and is BLOCKED_STABLE for shortlist admission.
- **GlobalShopCo-Headless:** CHANGED. PR #1 advanced from stale `4e66a67d...` to exact `9107ca283cf20b4bb79a4c25eaf1d4340b269e04`; commit `fix: validate Shopify store authority before request`; exact-head Actions run `34916760358`, job `104215957898`, `validate` SUCCESS. Bounded Shopify-store-authority validation is VERIFIED on this exact head only; no live checkout/deploy authority.
- **shopify_ebay:** default unchanged exact `c68883f24fb3711fce567a35b1a80db74933b82a`; no open PR/new canonical durable replay owner evidenced. Persistence discovery remains BLOCKED_STABLE; do not invent local store/ledger.
- **MyPrimeDelivery:** research `61feceb46de539948374deec86b3fe7578cf8014` and WordPress fixture `a38684c10541115f55f1d5612b72d669dced99f0` remain deliberately divergent. Exact compare: `diverged`, merge base `3635c903214b06464e28674d5a6403f8539b8c1e`, research side ahead 101 / behind 4 relative to fixture. Compatibility mapping remains required; live `QUALIFIED=0`.

# AGENTOS — Level 2 P0

### A-AG-01 — continuous project-file ownership fence
- status: BLOCKED; anchor: `AgentOS#104@4c8bcc3bc2ad2041b0a1871d3004c1db23f3c091`; objective: preserve one crash-releasing ownership fence continuously through verify -> side effect/prepared recovery -> durable success receipt -> release.
- acceptance/evidence: replacement-after-verify/publish/receipt, successor/three-writer, stale identity, TOCTOU, crash/replay and prepared-recovery negatives all deny false success; exact-head Ubuntu+Windows CI.
- next executable action: only the existing #104 owner implements the smallest SG-08 repair on the current writer seam; no competing lock/ledger/control plane.
- security: `SG-03,08,09,10,11,14,18,19`; S2; scoped branch/test grant; Green=yes; PRS=yes after identical-head Green; owner boundary merge/deploy/physical/production; security_disposition=BLOCKED.

### A-AG-02 — authenticated actor + canonical grant binding
- status: BLOCKED_STABLE; anchor: `#104@4c8bcc3...`; objective: bind only a real existing authenticated identity source and canonical grant resolver.
- acceptance/evidence: absent/spoofed/mismatch/cross-project/replay denies; issuer/source/version/request/task/mission provenance. Dependency is external/currently unevidenced canonical source.
- next executable action: none until changed source evidence; executors fall through.
- security: `SG-01,02,03,04,09,10,11,18,19`; S2; credentials/security-policy owner-only; Green=yes; PRS=yes; security_disposition=BLOCKED.

### A-AG-03 — runtime-shell eligibility consolidation
- status: ACTIVE; anchor: `AgentOS#112@d1645450a06d00c49a7a78f176e97b44b9eaa225`; objective: one canonical capability normalization/evaluation path without authority widening.
- acceptance/evidence: deterministic aliases, compatibility adapter reuses evaluator, asserted eligibility without canonical result denied, adjacent unauthorized capability denied; exact-head CI.
- next executable action: inspect current #112 CI/head; if unchanged and gaps remain, add at most 2–5 homogeneous evaluator/alias negatives, test and verify exact head.
- security: `SG-02,03,04,10,18`; S2; branch/tests only; Green only for promotion; PRS conditional on authority widening; owner boundary merge/deploy/production; security_disposition=ACTIVE.

### A-AG-04 — replay/correlation slices
- status: SPLIT_REQUIRED; anchor: current #104 lineage; objective: close only genuinely uncovered replay/correlation cases.
- acceptance/evidence: first-write provenance retained; conflicting same identity, duplicate result and restart duplicate fail closed without invented freshness source.
- next executable action: inventory existing tests, select 2–5 homogeneous uncovered cases, implement minimal validation/tests, exact-head CI; do not overlap A-AG-01.
- security: `SG-09,10,11,14,18`; S2; no new persistence/authority plane; Green=yes for promoted scope; PRS conditional; security_disposition=SPLIT_REQUIRED.

### A-AG-05 — physical Windows acceptance
- status: BLOCKED_STABLE; anchor: future repaired #104 exact head; dependency A-AG-01/02 + Jess/Michael + PRS + owner physical authority.
- next executable action: none; retain owner-run evidence contract only.
- security: `SG-03,08,10,11,14,18,20`; S2; owner physical Windows only; Green=yes; PRS=yes; security_disposition=BLOCKED.

# PRS — independent assurance

### A-PRS-01 — historical false-GREEN baseline
- status: VERIFIED; anchor: `PRS#17@49fe1f8bca3ddae271d85e0f4767173060267222`; immutable historical defect evidence only, never successor certification.
- next action: none unless target interpretation changes. security `SG-01,02,08,10,11,19`; S0.

### A-PRS-02 — changed-head bounded challenge
- status: PENDING; anchor: current `AgentOS#104@4c8bcc3...`; objective: independently challenge replay/correlation/receipt and defect-baseline behavior without completion claim.
- acceptance/evidence: immutable exact target/artifact hashes and independent outcomes; stale-owner/replay/correlation/receipt-order negatives.
- next executable action: run only if AgentOS target/evidence changed since last PRS probe; otherwise skip under changed-lineage rule.
- security: `SG-08,09,10,11,19`; S1; read/harness only; Green not prerequisite for defect confirmation; owner boundary merge/deploy; security_disposition=PENDING.

### A-PRS-03 — completion-grade ownership challenge
- status: BLOCKED_STABLE; anchor: `PRS#24@3039c886bdcff911f7c6dcc3e086368058e57fb6` contract + future repaired AgentOS head.
- acceptance: identical-head Jess functional PASS + Michael security PASS first, then independent normal/prepared/successor/crash/replay matrix with exact hashes.
- next executable action: none until prerequisites change.
- security: `SG-08,09,10,11,18,19`; S2; Green prerequisite; PRS=yes; owner boundary merge/deploy; security_disposition=BLOCKED.

### A-PRS-04 — physical Windows evidence contract freshness
- status: PENDING; anchor: `PRS#24@3039c886...`; objective: contract rejects stale/missing/mismatched AgentOS head, host/root, mutation/recovery/correlation or artifact identity.
- next executable action: add/verify only missing contract-negative fixtures; no physical execution.
- security: `SG-10,11,19,20`; S1; docs/tests only; owner physical host; security_disposition=PENDING.

# GLOBALSHOPCO

### B-GSC-01 — authenticated supplier evidence closure
- status: ACTIVE; anchor: `#29@15fa99eb...`, `#30@80c82475...`; objective: close exact SKU rows only with authenticated trade cost, packaged freight/free-delivery basis, permission, stock identity, returns/warranty.
- acceptance/evidence: source/date/SKU/cost/freight/status traceable; any missing material field => HOLD.
- next executable action: process only newly available authenticated evidence for existing candidates; do not repeat public-source rediscovery when unchanged.
- security: `SG-02,06,10,12,13,14,15,20`; S1; read-only; supplier contact/purchase/Shopify mutation owner-only; security_disposition=ACTIVE.

### B-GSC-02 — conservative delivered-margin gate
- status: PENDING; anchor: #29/#30 evidence-complete rows; objective: calculate delivered contribution only where inputs are complete.
- acceptance: fees/freight/returns allowance explicit; unknown/stale/negative economics => HOLD.
- next executable action: apply deterministic calculator to any newly evidence-complete row; otherwise skip.
- security: `SG-10,12,13,14,20`; S1; non-production calculation; spend/listing owner-only; security_disposition=PENDING.

### B-GSC-03 — bounded eBay shortlist
- status: BLOCKED_STABLE; anchor: `0 eBay-ready SKUs`; dependency B-GSC-01/02.
- next executable action: none until at least one exact variant has permission+stock+delivered economics+returns/warranty.
- security: `SG-02,06,10,12,13,14,15,20`; S1; publication/contact/spend owner-only; security_disposition=BLOCKED.

### B-GSC-04 — compact pet-accessory evidence mini-batch
- status: PENDING; anchor: #30 next-cycle direction; objective: 2–5 compact/light AU-stock candidates, not category expansion.
- acceptance: exact identity, supplier provenance, freight, permission, stock, returns captured or HOLD.
- next executable action: one homogeneous 2–5 candidate research batch, prioritizing authenticated evidence routes; stop if sources remain retail/syndicated only.
- security: `SG-06,10,12,13,14,15,20`; S1; research only; contact/purchase/listing owner-only; security_disposition=PENDING.

# GLOBALSHOPCO-HEADLESS

### B-HDL-01 — Shopify store-authority pre-request validation
- status: VERIFIED; anchor: `#1@9107ca283cf20b4bb79a4c25eaf1d4340b269e04`, commit `fix: validate Shopify store authority before request`, Actions `34916760358` / job `104215957898` SUCCESS.
- objective/acceptance: preserve exact configured Shopify store authority validation before request; bounded exact-head CI evidence only.
- next handoff: B-HDL-02/03; no live checkout inference.
- security: `SG-02,05,06,10,14,20`; S1; test/non-production only; secrets/deploy/live purchase owner-only; security_disposition=VERIFIED.

### B-HDL-02 — destination/host edge inventory
- status: PENDING; anchor: `#1@9107ca283cf20b4bb79a4c25eaf1d4340b269e04`; objective: identify only uncovered scheme/userinfo/port/subdomain/canonical-host confusion cases.
- acceptance: 2–5 homogeneous uncovered negatives, no duplicate coverage; exact-head CI.
- next executable action: inventory current tests after 9107ca; implement only genuine gaps.
- security: `SG-06,10,14`; S1; tests only; deploy/live checkout owner-only; security_disposition=PENDING.

### B-HDL-03 — Shopify canonical checkout projection
- status: PENDING; anchor: `#1@9107ca...`; objective: prove WordPress cannot become order/payment authority.
- acceptance: canonical Shopify checkout destination only; local payment/order mutation absent; alternate host/local-order negatives fail closed.
- next executable action: add 2–5 synthetic authority-boundary tests adjacent to new store-authority preflight, then exact-head CI.
- security: `SG-02,05,06,10,14,20`; S1; tests/docs; Shopify mutation/deploy/live purchase owner-only; security_disposition=PENDING.

### B-HDL-04 — product identity/availability contradictions
- status: PENDING; anchor: current M3 contract at `9107ca...`; objective: stale/mismatched product/variant/availability cannot form checkout payload.
- next executable action: add 2–5 homogeneous variant mismatch/stale availability/duplicate cart identity fixtures; exact-head CI.
- security: `SG-06,09,10,14`; S1; synthetic tests only; production commerce owner-only; security_disposition=PENDING.

### B-HDL-05 — non-production acceptance packet
- status: BLOCKED_STABLE; anchor: current #1 lineage; dependency genuine dev-store/browser evidence + owner-authorized credentials/environment.
- next executable action: none; preserve checklist, fall through to deterministic tests.
- security: `SG-05,10,14,20`; S2; owner-gated environment/credentials; no deploy/live purchase; security_disposition=BLOCKED.

# SHOPIFY -> EBAY

### B-EBAY-01 — upstream durable replay-store discovery
- status: BLOCKED_STABLE; anchor: default `c68883f24fb3711fce567a35b1a80db74933b82a`; objective: use only an existing canonical upstream replay store/caller.
- acceptance: exact owner/source/schema/lifecycle identified or explicit NONE; caller-supplied seen IDs are not durable evidence.
- next executable action: none until integration topology/source changes; no repeated rediscovery.
- security: `SG-02,09,10,11,14`; S1; no new ledger/persistence/production; security_disposition=BLOCKED.

### B-EBAY-02 — restart replay durability negatives
- status: BLOCKED; dependency B-EBAY-01; objective: restart duplicate/conflict/result-write replay preserves first-write provenance.
- next executable action: none until canonical store exists.
- security: `SG-09,10,11,14`; S2; synthetic tests only after dependency; publication owner-only; security_disposition=BLOCKED.

### B-EBAY-03 — evidence-complete SKU admission fixture
- status: BLOCKED_STABLE; anchor: `c68883f...` + GlobalShopCo `0 eBay-ready SKUs`; dependency B-GSC-03.
- next executable action: none until real evidence-complete Shopify variant exists.
- security: `SG-02,06,10,12,13,14,15,20`; S1; fixture only; eBay network/listing/spend owner-only; security_disposition=BLOCKED.

### B-EBAY-04 — synthetic mapper identity regression
- status: PENDING; anchor: `c68883f...`; objective: exact variant/SKU/event mapping under malformed/duplicate inputs.
- acceptance: 2–5 genuinely uncovered identity negatives; no live API.
- next executable action: inventory existing mapper tests; implement homogeneous gaps such as variant mismatch/malformed ID/conflicting hash, exact-head fixture CI.
- security: `SG-06,09,10,14`; S1; tests only; publication/network owner-only; security_disposition=PENDING.

# MYPRIMEDELIVERY

### B-MPD-01 — divergent-lineage compatibility map
- status: ACTIVE; anchors: research `61feceb46de539948374deec86b3fe7578cf8014`, WordPress fixture `a38684c10541115f55f1d5612b72d669dced99f0`, merge base `3635c903214b06464e28674d5a6403f8539b8c1e`; exact compare `diverged`, research side ahead 101/behind 4.
- objective: record changed paths/contracts and compatibility/conflict classes before integration; no stale overwrite/merge/rebase.
- acceptance/evidence: exact heads/base/path map + explicit compatible/conflicting/fixture-only classifications.
- next executable action: produce path-level compatibility map and identify the smallest presentation-contract port that does not import stale fixture assumptions.
- security: `SG-10,11,14,20`; S1; read/docs/tests; merge/deploy/publication owner-only; security_disposition=ACTIVE.

### B-MPD-02 — authoritative source/right-to-use evidence
- status: PENDING; anchor: research `61feceb...`; truth `0 live QUALIFIED`.
- objective: one coherent observation must carry exact ASIN + current product-level Prime + owner-approved rank/deal freshness + source rights + outbound destination.
- acceptance: editorial/public pages never become Prime/rank/deal authority; missing gate => HOLD.
- next executable action: process only newly available authorized evidence; no raw-concept expansion for its own sake.
- security: `SG-02,06,10,12,14,15,20`; S1; read-only; signup/credentials/publication owner-only; security_disposition=PENDING.

### B-MPD-03 — coherent qualification baseline
- status: VERIFIED; anchor: research `61feceb...`; objective: preserve one-observation coherence and conflicting-known-ASIN denial.
- next action: only genuinely uncovered contradictions; no repeat certification.
- security: `SG-06,09,10,14`; S1; test/read; live publication/network owner-only; security_disposition=VERIFIED.

### B-MPD-04 — WordPress non-production presentation adapter
- status: PENDING; dependency B-MPD-01 compatibility map; anchor fixture `a38684c...` plus research qualification schema.
- objective: render only QUALIFIED fixture data without inventing Prime/rank/deal authority.
- acceptance: HOLD/UNKNOWN never produces monetized/live CTA; outbound destination exact; no secret leakage.
- next executable action: after B-MPD-01, port only compatible presentation contract into a bounded fixture/test slice; no merge/rebase/live WordPress.
- security: `SG-05,06,10,14,15,20`; S2; non-production template/tests; Green if promoted; credentials/publication owner-only; security_disposition=PENDING.

### B-MPD-05 — freshness/identity contradiction mini-batch
- status: PENDING; anchor: research `61feceb...`; objective: 2–5 uncovered homogeneous stale Prime/rank/deal or identity/outbound contradictions fail closed.
- next executable action: inventory validator coverage, add only genuine gaps, run exact-head fixture CI.
- security: `SG-06,09,10,14`; S1; tests only; publication/network owner-only; security_disposition=PENDING.

## Execution order / starvation control
1. AgentOS A-AG-01 remains P0 but BLOCKED owner seam must not starve independent #112 A-AG-03 and replay/correlation test slices.
2. PRS follows changed AgentOS lineages only; unchanged heads are skipped. Completion-grade PRS requires identical-head Jess PASS + Michael PASS first.
3. Headless receives raised priority this window because it has fresh VERIFIED movement at `9107ca...`; consume adjacent deterministic authority/host/identity negatives while confidence class is homogeneous.
4. GlobalShopCo processes new authenticated evidence only; stable external evidence gaps are not rediscovered. `0 eBay-ready SKUs` remains truth.
5. shopify_ebay executes mapper identity tests while durable replay/SKU admission blockers remain stable; never add a persistence plane.
6. MyPrimeDelivery prioritizes the exact divergent-lineage compatibility map before presentation work; qualification authority remains fail-closed.

**No overall GREEN. Scheduled work outside these six projects remains untouched.**