# Portfolio Execution Batch Manifest

**Purpose:** bounded execution manifest consumed by existing ChatGPT schedules and manual execution cycles. Live repository/issues/runtime evidence remains authoritative. No entry grants merge/deploy/credentials/production writes/purchases/supplier contact/listing publication/campaign activation/production autonomy.

**Schedule lanes:** LANE A AgentOS Level 2 P0; LANE B GlobalShopCo/Headless/eBay/Amazon/MyPrimeDelivery; LANE C Affiliate-Websites/GhostKitchen/Franchise/GemVerse/Content360/Commercial Frontend/Marketing.

## Lifecycle
Fresh-scan before action and reconciliation. States are only `PENDING`, `ACTIVE`, `VERIFIED`, `BLOCKED`, `STALE`, `SPLIT_REQUIRED`. Scheduler firing and worker claims are not completion evidence. Repeated VERIFIED gates may replenish 2–5 homogeneous adjacent items; mixed-confidence work splits/fails closed.

# LANE A — AGENTOS LEVEL 2 P0

### A-001 — Continuous ownership fence
- status: BLOCKED
- exact evidence: AgentOS PR #104 OPEN/DRAFT/UNMERGED at `7df40bf9b1c50312983d75eb91e397a16c2d55b1`.
- blocker: check-to-publish ownership race remains; no kernel-enforced ownership primitive held continuously through publish/prepared recovery/durable success receipt.
- exact-head AgentOS Tests #974 / `34801212972` is FAILURE: Ubuntu/Node 22 passed test+audit; Windows/Node 26 failed test suite. Independent Green PASS and PRS PASS are not evidenced.
- next: only act when a real ownership primitive changes; then adversarial exact-head tests + Ubuntu/Windows CI -> independent Green -> PRS on unchanged head.

### A-002 — Ownership adversarial regressions
- status: BLOCKED
- dependency: A-001 primitive change.
- next homogeneous set after primitive exists: replacement-after-verification; three-writer successor; stale/replaced identity; crash/replay; duplicate-result/false-success.

### A-003 — Authority/admission continuation
- status: BLOCKED
- evidence: producer requires externally supplied authenticated actor context and `authoritySource.resolveGrant`; no canonical transport authenticator/grant resolver is presently evidenced as bindable without broadening the authority system.
- next: wait for/reuse a real canonical authenticated identity + grant source; do not create a duplicate authority layer or self-grant request fields.

### A-004 — Authority-source binding regressions
- status: ACTIVE
- exact evidence: `7df40bf9b1c50312983d75eb91e397a16c2d55b1` adds narrow tests for missing canonical grant fail-closed/zero durable artifacts and exact delivery/request/task/mission/wake/authority-evidence correlation.
- CI: AgentOS Tests #974 / `34801212972` FAILURE because Windows/Node 26 test suite failed while Ubuntu/Node 22 passed.
- next homogeneous set: isolate exact Windows failure; preserve missing authenticated actor, actor/grant mismatch, missing canonical grant evidence and exact correlation regressions. Do not promote until exact-head cross-platform CI passes.

# LANE B — COMMERCE PRIORITY

### B-001 — GlobalShopCo Home Organisation economics closure
- status: PENDING
- HOLD preserved: wholesale cost, candidate outbound freight, dropship/blind-shipping permission, sellable stock assurance and positive free-delivery contribution remain UNKNOWN.
- next: exact-SKU public/existing-account evidence closure only; infer nothing missing.

### B-002 — GlobalShopCo-Headless M3 checkout
- status: VERIFIED
- exact head `9799e6fe5a9c72e42e1554949697a64acce14bd4`; M3 checkout CI `34798624627` SUCCESS.
- external dev-store/browser proof remains UNKNOWN.
- replenished PENDING homogeneous work: inspect production plugin host normalization; test trailing-dot/case-normalized exact-host behavior only if ambiguous; add encoded/whitespace host confusion only if parser path permits it; preserve exact-host HTTPS fail-closed/no-purchase behavior.

### B-003 — Shopify -> eBay readiness
- status: VERIFIED
- exact evidence: `darrinbaldwindev/shopify_ebay` branch `agent/chatgpt/ebay-mapper-receipts` head `8c6d4fd2e43cfbe7e1cb9470c23574d6c3d125ad`; Fixture validation `34801871352` SUCCESS, 18/18 tests.
- verified scope: deterministic candidate mapper, denied-input fail-closed behavior, explicit UNKNOWN preservation, audit receipt binding Shopify IDs/SKU/input hash/mapper version/gate result, hard `publication_authority=False`.
- real SKU publication remains blocked by GlobalShopCo #17 supplier permission/blind-shipping/stock/freight/economics evidence. Existing Marketplace Connect path remains unassured for listing mapping, inventory propagation, order import, tracking propagation, oversell/duplicate protection and exact fee behavior.
- replenished PENDING homogeneous work: synthetic mapping/inventory/order/tracking/duplicate-protection contract fixtures only; no live publication or credentials.

### B-004 — Shopify -> Amazon readiness
- status: PENDING
- next: seller-of-record/category/GTIN/fulfilment/economics evidence model; no seller setup/publication.

### B-005 — MyPrimeDelivery synthetic WordPress slice
- status: VERIFIED
- exact head `a0791c11624d751e36abc2d7d4c5b793b568c760`; Fixture validation `34799420919` SUCCESS.
- replenished PENDING: validate marketplace enum/scope; require ranking-method status/source to remain fixture-safe; require timestamps when product evidence claims CURRENT/VERIFIED; preserve deterministic ranking order under harmless input ordering.
- synthetic only; no live Prime/ranking/affiliate claim.

# LANE C — PRODUCT / CONTENT / VENTURES

### C-001 — Affiliate Websites governed CTA/program evidence
- status: VERIFIED
- exact head `d901b3e2c0c772cdc43019dd96cf2b19bdded0a6`; Commercial CTA fixture CI `34798980244` SUCCESS.
- replenished PENDING: publisher timestamp/future evidence validation; country evidence mismatch; blocked audit destination/tracking stripping; deterministic program-identity ordering.

### C-002 — GhostKitchen economics batch
- status: VERIFIED
- exact head `ddfb2d872ca116b2cf18d3a98d53670b0c228237`; Economics validation `34799531732` SUCCESS.
- replenished PENDING: validate allowed batch status enum; validate source_note type/emptiness without treating prose as authority; reject unknown keys inside evidence items; add batch evidence summary that cannot upgrade scenario eligibility.

### C-003 — Franchise territory/tenancy validation
- status: VERIFIED
- exact head `29fa0546f0d7abe03fcc1af3d0770e7e50925c31`; Territory fixture CI `34799016286` SUCCESS.
- replenished PENDING: duplicate inactive area IDs; franchise status enum; delivery-area status enum; deterministic case ordering.

### C-004 — GemVerse Level 2 fixture assurance
- status: VERIFIED
- exact head `0033b66de8e138c199207e33c505db6d8df5345b`; Level 2 fixture CI `34799040874` SUCCESS.
- replenished PENDING: bind recovery evidence to exact current-state hash; reject action/state replay mismatch; deterministic competing-candidate denial without payload leak; strict recovery-result schema.

### C-005 — Content360 provider-neutral adapter
- status: PENDING
- next: official/public contract evidence -> request/result schema + mocked failures; no credential/live publish.

### C-006 — Commercial Frontend workflow evidence
- status: PENDING
- next: deepen Tradie/Ecommerce cross-system exception evidence; pain/frequency/WTP remain UNKNOWN.

### C-007 — Marketing / AgentOS objection acceptance
- status: PENDING
- target: AgentOS #109.
- next: turn objections into testable onboarding/pricing/demo acceptance evidence; planned mitigation is not proof.

# INDEPENDENT PRS CHECKPOINT
- status: VERIFIED only for evaluator-parity cleanup at `a646f4033fd1b0c40135cb6f5c1286e9c7610728`, CI `34793554142` SUCCESS.
- AgentOS PR #104 current head remains unassured; no overall GREEN.

# :30 RECONCILIATION — 2026-09-14 13:32 BRISBANE
- Fresh durable evidence superseded the previous manifest where it differed.
- LANE A: PR #104 advanced from `083b7dec...` to `7df40bf...`. A-001/A-002 remain BLOCKED. A-003 is BLOCKED on absence of an evidenced canonical authenticated transport/grant source. A-004 is ACTIVE after the bounded authority regression commit, but exact-head CI #974 is RED on Windows while Ubuntu passes; exact failure detail remains to be isolated.
- LANE B: B-003 advanced materially and is VERIFIED only for its synthetic mapper/receipt gate at `8c6d4fd...`, CI `34801871352` SUCCESS, 18/18. Real eBay readiness remains fail-closed on supplier/freight/economics and live Marketplace Connect assurance. B-001/B-004 remain PENDING; B-002/B-005 retain verified fixture gates plus homogeneous PENDING follow-ons.
- LANE C: no newer exact repository/CI evidence found in the durable coordination state than the currently recorded verified gates; C-001/C-002/C-003/C-004 retain homogeneous PENDING follow-ons and C-005/C-006/C-007 remain PENDING.
- No scheduler firing or worker claim was treated as completion evidence. Historical evidence preserved. No overall GREEN.

# NEXT PASS ORDER
1. LANE A: isolate Windows failure on exact `7df40bf...`; A-001 only on new ownership-primitive evidence; A-003 only when a real canonical auth/grant source exists; continue bounded A-004 regressions without authority duplication.
2. LANE B: B-001 exact-SKU evidence closure; B-003 homogeneous synthetic Marketplace Connect contract assurance; B-002 production-code inspection; B-005 fixture-safe evidence/timestamp batch; B-004 bounded readiness.
3. LANE C: consume homogeneous C-001/C-002/C-003/C-004 batches; then C-005/C-006/C-007 as safe capacity remains.
4. Re-scan exact heads/issues/CI before promoting any state and preserve all HOLD/BLOCKED/UNKNOWN evidence.
