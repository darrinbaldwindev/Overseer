# Portfolio Execution Batch Manifest

**Purpose:** bounded execution manifest consumed by the existing ChatGPT schedules and manual `cont` / `continue autonomously vertically` cycles. This file is not a scheduler, authority source, mission ledger, registry, Green system, PRS system, or project source of truth. Live repository/issues/runtime evidence remains authoritative.

**Manual rule:** `cont` / `continue autonomously vertically` consumes as much safe useful work from this manifest as possible, reconciles results, then replenishes this same file before returning control.

**Schedule rule:** :00 consumes LANE A, :15 consumes LANE B, :30 reconciles/replenishes, :37 independently guards AgentOS/false-GREEN, :45 consumes LANE C.

## Batch lifecycle
1. Refresh target repo/ref/evidence before acting; stale manifest text never overrides live state.
2. Execute multiple safe items when useful; blocked work must not terminate the pass while other eligible work exists.
3. Reconcile items as `PENDING`, `ACTIVE`, `VERIFIED`, `BLOCKED`, `STALE`, or `SPLIT_REQUIRED` with exact evidence in project issues/logs and Overseer #49.
4. VERIFIED GREEN gates may expand into small homogeneous batches, normally 2–5 equivalent items.
5. Mixed-confidence/failed items are split and fail closed.
6. No batch entry grants merge/deploy/credentials/production writes/purchases/supplier contact/listing publication/campaign activation/production autonomy.

---

# LANE A — AGENTOS LEVEL 2 P0 (:00)

### A-001 — Continuous ownership fence
- status: BLOCKED
- priority: P0
- current exact head observed in manual pass: `083b7decf48038764ec846a988a5cd30d2a4fa56`
- evidence: PR #104 remains OPEN/DRAFT/UNMERGED; current PR-triggered AgentOS Tests run `34791584537` is CANCELLED; PR body records independent Green FAIL on the unresolved check-to-publish ownership race.
- blocker: no kernel-enforced ownership boundary held continuously through final verification -> publish/prepared recovery -> success-receipt persistence.
- next: implement/test the smallest ownership-preserving primitive on current exact lineage; rerun exact-head Windows+Ubuntu CI; Green only on unchanged exact head.
- batch_rule: single critical-path change until independently green.

### A-002 — Ownership adversarial regressions
- status: BLOCKED
- dependency: A-001 primitive must first change or otherwise gain new evidence.
- next batch once eligible: replacement-after-verification; three-writer successor; stale/replaced identity; crash/replay; duplicate-result/false-success.
- batch_rule: 2–5 homogeneous cases only after primitive is stable.

### A-003 — Authority/admission continuation
- status: PENDING
- priority: P1-after-A-001/A-002 or when ownership work is temporarily blocked
- action: bind trusted transport actor context and canonical grant evidence to existing authority-admission/pickup lineage; no self-granting request fields.
- acceptance: fail-closed tests, no duplicate authority layer, exact task/mission/wake correlation.

---

# LANE B — COMMERCE PRIORITY (:15)

### B-001 — GlobalShopCo Home Organisation economics closure
- status: PENDING
- priority: P0-commerce
- target: GlobalShopCo issues #9/#18
- action: advance exact-SKU candidates toward supplier identity, wholesale, freight, free-delivery economics, returns/warranty, stock and explicit UNKNOWN closure.
- acceptance: missing freight/supplier/channel evidence remains HOLD.
- batch_rule: once one candidate gate is VERIFIED GREEN, process 2–5 equivalent compact candidates.

### B-002 — GlobalShopCo-Headless M3 checkout slice
- status: VERIFIED
- exact verified head: `11214e0b4a119cf237c1d3ffa10ca1df1f375d4b`
- CI: M3 checkout validation run `34792401552` SUCCESS.
- verified property: deterministic cart/checkout handoff plus configured Shopify checkout-host enforcement.
- replenished adjacent batch (PENDING):
  1. reject checkout host with valid suffix but wrong registrable host;
  2. reject protocol downgrade / non-HTTPS checkout destination;
  3. reject missing checkoutUrl even when cart lines exist;
  4. preserve unavailable-variant fail-closed behavior with no redirect.
- boundary: non-production/test-safe only; Shopify remains source of truth.

### B-003 — Shopify -> eBay readiness
- status: PENDING
- action: deterministic candidate mapping/readiness; require marketplace permission, fulfilment identity, stock method and landed economics.
- batch_rule: 2–5 equivalent candidate records only after mapper/gate remains green.

### B-004 — Shopify -> Amazon readiness
- status: PENDING
- action: seller-of-record/category/GTIN/fulfilment/economics evidence model without seller setup.
- acceptance: owned-site/eBay/MyPrimeDelivery state cannot imply Amazon eligibility.

### B-005 — MyPrimeDelivery synthetic WordPress slice
- status: ACTIVE
- predecessor verified head: `f4692b80286677cc4d25d2292083439f1790f241`; Fixture validation run `34791382576` SUCCESS.
- manual-pass implementation head: `56cf2421348390eeebc41e0de486c5707b570b09` on `agent/overseer/initial-project-timeline`.
- work added: reusable synthetic `mpd-category-view` / `mpd-product-card` render projection, disabled positive Prime claims/CTA/local checkout for fixtures, stale-state suppression tests, CI integration.
- next: consume exact-head CI for `56cf242...`; if SUCCESS, replenish 2–5 equivalent render edge cases (missing ranking evidence, VERIFIED destination fixture without authorised URL, optional commercial-field suppression, evidence badge mapping).
- boundary: synthetic only; no live Prime/ranking/affiliate claims.

---

# LANE C — PRODUCT / CONTENT / VENTURES PRIORITY (:45)

### C-001 — Affiliate Websites governed CTA/program evidence
- status: PENDING
- action: evidence-gated programme records + reusable CTA/data contract; consumer referral != publisher affiliate.
- acceptance: stale/unknown/referral-only evidence cannot become verified publisher CTA.

### C-002 — GhostKitchen economics batch
- status: ACTIVE
- predecessor verified head: `8cd52abf37999c7f16642aaf4a8f5c389e7939af`; Economics validation run `34791727853` SUCCESS.
- manual-pass head: `0bc82e4a15f882dc5de3f44b3cdc542cfd6defd2`.
- work added: expanded homogeneous decision-support scenario batch from 3 to 5 cases, including higher-commission marketplace and direct-order/no-paid-acquisition variants; all public/hypothesis evidence remains non-commercial-pass.
- next: consume exact-head CI; if SUCCESS, add representative menu scenarios only where recipe/packaging/labour/AOV values are explicitly evidence-classified; UNKNOWN stays NOT_TESTABLE.

### C-003 — Franchise territory/tenancy validation
- status: ACTIVE
- predecessor verified head: `b9cf83bd6c00b14694c7b3b2e3a6e9fd5fb90cf5`; Territory fixture validation run `34791807480` SUCCESS.
- manual-pass head: `00730890a08ca47ce8783f9de8bdc850dc19ccc9`.
- work added: routing output now includes matched active-area IDs, candidate franchises, selected franchise and explicit selection/denial reason; tests cover successful selection, inactive denial and NO_SERVICE audit evidence.
- next: consume exact-head CI; if SUCCESS, replenish a small audit batch for version/correlation/evidence timestamp fields and synthetic tenancy-context derivation without production migration.

### C-004 — GemVerse Level 2 fixture assurance
- status: ACTIVE
- predecessor verified head: `b56c8eced601790b0c7cbafb907b58749fc916e5`; Level 2 fixture validation run `34792510122` SUCCESS.
- manual-pass head: `e8725d22c3761fd94496538e3f3316e565c0c1a8` on branch `gemverse`.
- work added: homogeneous near-miss rejection batch for truncated state, wrong project identity, skipped counter and mixed state; each rejected both as complete state and authorised pre-image.
- next: consume exact-head CI; if SUCCESS, add prepared-artifact identity/correlation and stale-replay recovery cases without altering canonical fixture state.

### C-005 — Content360 provider-neutral adapter
- status: PENDING
- action: consume official/public contract research when available; extend request/result schemas and mock failure cases; no credential/live publish.

### C-006 — Commercial Frontend workflow evidence
- status: PENDING
- action: deepen Tradie/Ecommerce cross-system exception evidence; customer pain/frequency/WTP remain UNKNOWN until evidenced.

### C-007 — AgentOS marketing objection acceptance
- status: PENDING
- target: AgentOS issue #109
- action: convert objection gates into directly testable onboarding/pricing/demo evidence; planned mitigation != product proof.

---

# INDEPENDENT PRS CHECKPOINT (non-consuming)
- status: VERIFIED for evaluator-parity cleanup only
- exact head: `a646f4033fd1b0c40135cb6f5c1286e9c7610728`
- CI: Validate repository run `34793554142` SUCCESS.
- meaning: legacy evaluator compatibility path now delegates to canonical semantics with exact-head repository validation. This is not AgentOS PR #104 assurance and does not imply overall PRS/AgentOS GREEN.

# NEXT REPLENISHER PASS
1. Harvest CI for GhostKitchen `0bc82e4...`, Franchise `0073089...`, GemVerse `e8725d2...`, MyPrimeDelivery `56cf242...`.
2. If green, expand only the adjacent small batches listed above.
3. Keep AgentOS A-001 fail-closed until a changed ownership primitive and exact-head CI + independent Green exist.
4. Continue B-001 first among unresolved commerce work; continue C-001 first among unresolved ventures work unless active CI results create an immediately executable adjacent batch.
5. Do not let blocked external/owner-evidence work starve other safe items.

**Reconciled after manual vertical batch:** 2026-09-14 10:53+10 owner-triggered cycle.