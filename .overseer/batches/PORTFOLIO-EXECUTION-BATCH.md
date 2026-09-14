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
- exact-head AgentOS Tests #974 / `34801212972` now concludes SUCCESS after Windows/Node 26 retry attempt 2 job `103853915603` passed test suite + npm audit; Ubuntu/Node 22 also passed. Initial Windows failure remains unexplained/transient and does not resolve the ownership blocker.
- independent Green PASS and PRS PASS are not evidenced.
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
- status: VERIFIED
- exact evidence: `7df40bf9b1c50312983d75eb91e397a16c2d55b1` includes narrow tests for missing canonical grant fail-closed/zero durable artifacts and exact delivery/request/task/mission/wake/authority-evidence correlation.
- CI: AgentOS Tests #974 / `34801212972` SUCCESS after Windows retry attempt 2 job `103853915603`; Ubuntu/Node 22 and Windows/Node 26 test+audit both pass on unchanged exact head.
- replenished PENDING homogeneous work: preserve missing authenticated actor, actor/grant mismatch, missing canonical grant evidence, stale/replayed grant evidence and exact correlation regressions; do not invent a transport/grant authority source.

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
- exact evidence: `darrinbaldwindev/shopify_ebay` branch `agent/chatgpt/ebay-mapper-receipts` head `b57e0a47bdff4b699d8b6b346fe5e9e1a0bbacc3`; Fixture validation `34805527804` / check `103856555020` SUCCESS.
- verified scope now includes deterministic candidate mapper/receipts plus synthetic Shopify-canonical inventory-change receipt, eBay-order->Shopify handoff candidate preserving Shopify order authority, tracking candidate requiring exact Shopify/eBay order correlation, and duplicate-event/idempotency denial. Tests preserve `publication_authority=False` and `network_io=False`.
- Marketplace Connect is already installed and eBay AU `globalshopco` connected; real connector behavior remains unassured. Real SKU publication remains blocked by GlobalShopCo #17 supplier permission/blind-shipping/stock/freight/economics evidence.
- replenished PENDING homogeneous work: synthetic stale inventory event, out-of-order tracking event, duplicate order import and correlation-mismatch fixtures only; no live connector/network calls, credentials or publication.

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
- default branch remains `0033b66de8e138c199207e33c505db6d8df5345b`; homogeneous recovery batch is in child issue #9 / OPEN DRAFT UNMERGED PR #10 exact head `b1f09c3a9300a24782f5f3e4ab01619a64477319`.
- exact-head Level 2 fixture validation `34803885504` SUCCESS.
- verified additions: recovery evidence binds exact current-state SHA-256; action/current-state replay mismatch fails closed; competing-candidate denial deterministic without payload leak; strict recovery result/evidence schemas reject missing/extra fields.
- replenished PENDING homogeneous work: bind recovery decision to exact action/result correlation; reject stale recovery evidence timestamps/versions where schema supports it; duplicate recovery-result idempotency; deterministic malformed-evidence denial. Canonical AgentOS execution remains outside this fixture result.

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
- AgentOS PR #104 current head remains unassured by Green/PRS for the continuous ownership blocker; no overall GREEN.

# :30 RECONCILIATION — 2026-09-14 14:30 BRISBANE
- Fresh durable evidence superseded the previous manifest where it differed.
- LANE A: PR #104 remains exact `7df40bf...`. A-001/A-002 remain BLOCKED on continuous ownership; A-003 remains BLOCKED on absence of an evidenced canonical authenticated transport/grant source. A-004 advances ACTIVE -> VERIFIED for its narrow authority regression scope because exact-head Tests #974 now concludes SUCCESS after unchanged-head Windows retry; the original Windows failure remains unexplained. Homogeneous authority regressions are replenished PENDING without authority duplication.
- LANE B: B-003 advances to exact `b57e0a47...`, Fixture validation `34805527804` SUCCESS, adding synthetic inventory/order/tracking/idempotency contract assurance while preserving Shopify authority and zero network/publication authority. Real Marketplace Connect behavior and SKU commercial eligibility remain blocked/UNKNOWN. B-001/B-004 remain PENDING; B-002/B-005 retain verified gates plus homogeneous PENDING follow-ons.
- LANE C: C-004 materially advances in GemVerse draft PR #10 exact `b1f09c3a...`, CI `34803885504` SUCCESS for four homogeneous recovery-assurance additions; default branch remains unchanged. Other C items retain prior narrow states and useful PENDING work.
- No scheduler firing or worker claim was treated as completion evidence. Historical evidence preserved. No overall GREEN.

# NEXT PASS ORDER
1. LANE A: A-001 only on new ownership-primitive evidence; A-003 only when a real canonical auth/grant source exists; consume homogeneous A-004 authority regressions while preserving fail-closed semantics and exact correlation.
2. LANE B: B-001 exact-SKU evidence closure; B-003 homogeneous synthetic stale/out-of-order/duplicate/correlation contract assurance; B-002 production-code inspection; B-005 fixture-safe evidence/timestamp batch; B-004 bounded readiness.
3. LANE C: consume homogeneous C-001/C-002/C-003/C-004 batches; then C-005/C-006/C-007 as safe capacity remains.
4. Re-scan exact heads/issues/CI before promoting any state and preserve all HOLD/BLOCKED/UNKNOWN evidence.
