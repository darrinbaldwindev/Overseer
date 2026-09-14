# Portfolio Execution Batch Manifest

**Purpose:** bounded execution manifest consumed by existing ChatGPT schedules and manual `cont` / `continue autonomously vertically` cycles. This file is not a scheduler, authority source, mission ledger, registry, Green system, PRS system, or project source of truth. Live repository/issues/runtime evidence remains authoritative.

**Manual rule:** `cont` / `continue autonomously vertically` means: (1) fresh thorough repository scan before action, (2) consume as much safe useful work as possible from the current manifest, (3) fresh thorough scan again before reconciliation/replenishment, (4) replenish this same file before returning control.

**Schedule rule:** :00 consumes LANE A, :15 consumes LANE B, :30 reconciles/replenishes, :37 independently guards AgentOS/false-GREEN, :45 consumes LANE C.

## Mandatory fresh-scan doctrine
Before acting on an item, refresh the relevant repository branch/head, recent commits, issues/comments/PRs, CI/workflows, and exact files/tests/contracts implicated by the item. Before replenishing an acted-on lane, scan those repositories again to catch moved heads, concurrent work, new CI, duplicate completion, stale assumptions or changed blockers. Manifest text never overrides fresh evidence.

## Batch lifecycle
1. Refresh target repo/ref/evidence before acting.
2. Execute multiple safe items when useful; blocked work must not terminate the pass while other eligible work exists.
3. Reconcile as `PENDING`, `ACTIVE`, `VERIFIED`, `BLOCKED`, `STALE`, or `SPLIT_REQUIRED` with exact evidence.
4. VERIFIED GREEN gates may expand into small homogeneous batches, normally 2–5 equivalent items.
5. Mixed-confidence/failed items split and fail closed.
6. Scan again before replenishing.
7. No batch entry grants merge/deploy/credentials/production writes/purchases/supplier contact/listing publication/campaign activation/production autonomy.

---

# LANE A — AGENTOS LEVEL 2 P0 (:00)

### A-001 — Continuous ownership fence
- status: BLOCKED
- priority: P0
- fresh exact head: `083b7decf48038764ec846a988a5cd30d2a4fa56`
- evidence: PR #104 remains OPEN/DRAFT/UNMERGED; exact-head AgentOS Tests run `34791584537` is CANCELLED; independent Green remains FAIL on unresolved check-to-publish ownership race.
- blocker: no kernel-enforced ownership boundary held continuously through final verification -> publish/prepared recovery -> success-receipt persistence.
- next: implement/test smallest ownership-preserving primitive on current lineage; rerun exact-head Windows+Ubuntu CI; Green only on unchanged exact head.
- batch_rule: single critical-path change until independently green.

### A-002 — Ownership adversarial regressions
- status: BLOCKED
- dependency: A-001 primitive must first change or gain new evidence.
- next eligible batch: replacement-after-verification; three-writer successor; stale/replaced identity; crash/replay; duplicate-result/false-success.
- batch_rule: 2–5 homogeneous cases only after primitive stability.

### A-003 — Authority/admission continuation
- status: PENDING
- priority: P1 when A-001 is externally/technically blocked
- action: bind trusted transport actor context and canonical grant evidence to existing authority-admission/pickup lineage; no self-granting request fields.
- acceptance: fail-closed tests, no duplicate authority layer, exact task/mission/wake correlation.

---

# LANE B — COMMERCE PRIORITY (:15)

### B-001 — GlobalShopCo Home Organisation economics closure
- status: PENDING / HOLD-PRESERVING
- priority: P0-commerce
- fresh issue state: GlobalShopCo #9 remains open and explicitly requires Home Organisation completion before category advance.
- current verified example: United Living / Boxsweden exact SKU `15510`, EAN `9340957115510`; supplier identity/catalogue presence and policy-level delivery/returns are evidenced.
- still UNKNOWN: wholesale cost, candidate-level outbound freight, dropship/blind-shipping permission, sellable stock assurance, positive free-delivery contribution.
- action: continue independent non-duplicate candidate evidence closure; missing freight/wholesale cannot be inferred.
- batch_rule: 2–5 candidates only after one complete gate becomes VERIFIED GREEN.

### B-002 — GlobalShopCo-Headless M3 checkout slice
- status: VERIFIED
- exact verified head: `11214e0b4a119cf237c1d3ffa10ca1df1f375d4b`
- CI: M3 checkout validation `34792401552` SUCCESS.
- verified property: deterministic cart/checkout handoff plus configured Shopify checkout-host enforcement.
- replenished adjacent batch: PENDING
  1. reject valid-looking suffix/wrong registrable checkout host;
  2. reject protocol downgrade/non-HTTPS checkout destination;
  3. reject missing checkoutUrl even with cart lines;
  4. preserve unavailable-variant fail-closed behavior with no redirect.
- boundary: non-production/test-safe; Shopify remains source of truth.

### B-003 — Shopify -> eBay readiness
- status: PENDING
- action: deterministic candidate mapping/readiness; require marketplace permission, fulfilment identity, stock method and landed economics.
- batch_rule: 2–5 equivalent candidate records only after mapper/gate remains green.

### B-004 — Shopify -> Amazon readiness
- status: PENDING
- action: seller-of-record/category/GTIN/fulfilment/economics evidence model without seller setup.
- acceptance: owned-site/eBay/MyPrimeDelivery state cannot imply Amazon eligibility.

### B-005 — MyPrimeDelivery synthetic WordPress slice
- status: VERIFIED
- exact verified head: `3207255476326e96490260ea665b5ceb56d44053`
- CI: Fixture validation `34795489707` SUCCESS.
- verified work: reusable fixture render projection; no local checkout; no live commercial fields; stale VERIFIED evidence now suppresses positive Prime claim, ranking presentation and outbound CTA.
- replenished adjacent batch: PENDING
  1. category-level STALE/UNKNOWN must suppress positive ranking framing;
  2. missing/invalid ranking position must fail closed before render ordering;
  3. BLOCKED freshness must suppress verified outbound action;
  4. explicit fixture disclosure remains present on every synthetic product card.
- boundary: synthetic only; no live Prime/ranking/affiliate claim.

---

# LANE C — PRODUCT / CONTENT / VENTURES PRIORITY (:45)

### C-001 — Affiliate Websites governed CTA/program evidence
- status: PENDING
- action: evidence-gated programme records + reusable CTA/data contract; consumer referral != publisher affiliate.
- acceptance: stale/unknown/referral-only evidence cannot become verified publisher CTA.

### C-002 — GhostKitchen economics batch
- status: VERIFIED
- exact verified head: `9fb23afd4f9eead58b47c8152e059c13d1bf40c4`
- CI: Economics validation `34795358739` SUCCESS.
- reconciliation: first expanded batch head `0bc82e4...` failed because a positional test accidentally selected a newly inserted calculated scenario; corrected tests now bind by scenario ID and exercise all four decision-support scenarios plus the UNKNOWN delivery fail-closed case.
- verified property: public-reference/hypothesis scenarios never become commercial-pass; UNKNOWN required input remains NOT_TESTABLE.
- replenished adjacent batch: PENDING
  1. representative menu/AOV scenario with every project-specific cost explicitly evidence-classified;
  2. packaging-cost UNKNOWN case remains NOT_TESTABLE;
  3. labour-cost UNKNOWN case remains NOT_TESTABLE;
  4. negative contribution with VERIFIED_PROJECT inputs must never become commercial-pass.
- boundary: public/hypothesis benchmarks are decision support, not project economics proof.

### C-003 — Franchise territory/tenancy validation
- status: VERIFIED
- exact verified head: `a70d0726145efcdae2ad0ccc6dec8ca4b370ab69`
- CI: Territory fixture validation `34795399126` SUCCESS.
- reconciliation: first audit-test head `0073089...` failed because test expected non-existent case ID `no-service`; corrected to canonical fixture ID `unserviceable`.
- verified property: routing output includes matched active-area IDs, candidate franchises, selected franchise and explicit selection/denial reason; active overlap/unknown franchise/inactive franchise/no-service fail closed.
- replenished adjacent batch: PENDING
  1. add territory/version used to every decision record;
  2. add deterministic correlation ID for synthetic routing decision;
  3. add evidence timestamp/source marker for fixture decision context;
  4. derive synthetic tenancy context without creating production tenancy or migration.

### C-004 — GemVerse Level 2 fixture assurance
- status: VERIFIED
- exact verified head: `2d008aebd593115b71c72a86aab581dd42da5fdc`
- CI: Level 2 fixture validation `34795508014` SUCCESS.
- verified work: deterministic initial->target mutation, idempotent replay, near-miss state rejection, prepared-record mission/project/preimage/target hash binding, and stale prepared replay rejection.
- replenished adjacent batch: PENDING
  1. duplicate complete-target recovery stays idempotent;
  2. prepared artifact with correct hashes but missing required identity field fails closed;
  3. recovery decision records original/prepared chosen state deterministically;
  4. canonical fixture file remains unchanged after all synthetic recovery tests.

### C-005 — Content360 provider-neutral adapter
- status: PENDING
- action: consume official/public contract research when available; extend request/result schemas and mock failure cases; no credential/live publish.

### C-006 — Commercial Frontend workflow evidence
- status: PENDING
- action: deepen Tradie/Ecommerce cross-system exception evidence; customer pain/frequency/WTP remain UNKNOWN until evidenced.

### C-007 — AgentOS marketing/product objection acceptance
- status: PENDING
- target: AgentOS issue #109
- action: convert objection gates into directly testable onboarding/pricing/demo evidence; planned mitigation != product proof.

---

# INDEPENDENT PRS CHECKPOINT (non-consuming)
- status: VERIFIED for evaluator-parity cleanup only
- exact head: `a646f4033fd1b0c40135cb6f5c1286e9c7610728`
- CI: Validate repository `34793554142` SUCCESS.
- meaning: legacy evaluator compatibility path delegates to canonical semantics with exact-head validation. This is not AgentOS PR #104 assurance and does not imply overall PRS/AgentOS GREEN.

# NEXT PASS ORDER
1. Fresh-scan all target repos before action.
2. LANE A: A-001 if new ownership primitive evidence exists; otherwise A-003 without bypassing A-001.
3. LANE B: B-001 first; use B-002/B-005 green adjacent batches while commercial evidence remains blocked.
4. LANE C: C-001 first among unresolved ventures; C-002/C-003/C-004 green adjacent batches are now eligible for 2–4 homogeneous items each.
5. Fresh-scan every touched repo again before replenishment.
6. Preserve explicit HOLD/BLOCKED/UNKNOWN states; do not let them starve other safe work.

**Reconciled and replenished after manual vertical batch:** 2026-09-14 owner-triggered cycle following pre-action and pre-replenishment fresh scans.
