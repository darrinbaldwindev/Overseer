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
- evidence: PR #104 remains OPEN/DRAFT/UNMERGED; exact-head AgentOS Tests run `34791584537` (#971) is CANCELLED; independent Green remains FAIL on unresolved check-to-publish ownership race.
- blocker: no kernel-enforced ownership boundary held continuously through final verification -> publish/prepared recovery -> success-receipt persistence.
- next: implement/test smallest ownership-preserving primitive on current lineage; rerun exact-head Windows+Ubuntu CI; Green only on unchanged exact head.
- batch_rule: single critical-path change until independently green.

### A-002 — Ownership adversarial regressions
- status: BLOCKED
- dependency: A-001 primitive must first change or gain new evidence.
- next eligible batch: replacement-after-verification; three-writer successor; stale/replaced identity; crash/replay; duplicate-result/false-success.
- batch_rule: 2–5 homogeneous cases only after primitive stability.

### A-003 — Authority/admission continuation
- status: ACTIVE
- priority: P1 while A-001 is technically blocked
- evidence: bounded producer/pickup seam inspection remains current; existing admission fails closed on actor/grant provenance and replay, but authenticated transport identity plus canonical grant evidence are not wired to the producer/pickup seam.
- action: bind trusted transport actor context and canonical grant evidence to existing authority-admission/pickup lineage; no self-granting request fields.
- acceptance: fail-closed tests, no duplicate authority layer, exact delivery/request/task/mission/wake correlation.

### A-004 — Authority-source binding regression set
- status: PENDING
- dependency: A-003 implementation seam identified; does not bypass A-001.
- action: missing authenticated actor, actor/grant mismatch, missing canonical grant evidence, and correlation preservation through pickup.
- batch_rule: test/evidence closure only; no alternate authority producer or registry.

---

# LANE B — COMMERCE PRIORITY (:15)

### B-001 — GlobalShopCo Home Organisation economics closure
- status: PENDING / HOLD-PRESERVING
- priority: P0-commerce
- target: GlobalShopCo #9/#18.
- current verified example: United Living / Boxsweden SKU `15510`, EAN `9340957115510`; supplier identity/catalogue presence and policy-level delivery/returns evidenced.
- still UNKNOWN/HOLD: wholesale cost, candidate-level outbound freight, dropship/blind-shipping permission, sellable stock assurance, positive free-delivery contribution.
- action: continue independent non-duplicate candidate evidence closure; missing freight/wholesale cannot be inferred.
- batch_rule: 2–5 candidates only after one complete gate becomes VERIFIED GREEN.

### B-002 — GlobalShopCo-Headless M3 checkout slice
- status: VERIFIED
- fresh exact head: `4053441d7959801a735882c14abc7d0fad2579de`
- CI: M3 checkout validation `34795412636` SUCCESS.
- consumed in concurrent scheduled pass: suffix-confusable checkout host, HTTP downgrade, missing checkoutUrl, and unavailable-variant output assertions all fail closed; 11 deterministic cases now pass.
- replenished adjacent batch: PENDING
  1. reject checkout URL userinfo/credential-host confusion;
  2. reject configured-host mismatch through explicit unexpected port or malformed host normalization;
  3. preserve no-checkout/no-purchase rendering for malformed checkout URL syntax.
- external gate: controlled dev-store product -> Shopify-hosted checkout browser proof remains UNKNOWN and must not be fabricated.

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
- fresh exact head: `b812158d18733e34d2a549a3acc44a05550dd296`
- CI: Fixture validation `34796288111` SUCCESS.
- consumed manual batch: category STALE/UNKNOWN/BLOCKED suppresses ranking; invalid/missing/non-positive ranking position fails closed before render ordering; BLOCKED freshness suppresses outbound action; every synthetic card and category now carries explicit fixture disclosure.
- replenished adjacent batch: PENDING
  1. duplicate ranking positions must fail closed rather than silently reorder;
  2. VERIFIED outbound destination with non-VERIFIED evidence status must not render action;
  3. missing/false fixture-only disclosure must fail closed in the synthetic renderer;
  4. category evidence-status/freshness contradictions must not create positive ranking framing.
- boundary: synthetic only; no live Prime/ranking/affiliate claim.

---

# LANE C — PRODUCT / CONTENT / VENTURES PRIORITY (:45)

### C-001 — Affiliate Websites governed CTA/program evidence
- status: PENDING
- action: evidence-gated programme records + reusable CTA/data contract; consumer referral != publisher affiliate.
- acceptance: stale/unknown/referral-only evidence cannot become verified publisher CTA.

### C-002 — GhostKitchen economics batch
- status: VERIFIED
- fresh exact head: `3328870f11849f268a308576d9d9793121371ef6`
- CI: Economics validation `34796325179` SUCCESS.
- consumed manual batch: packaging UNKNOWN and labour UNKNOWN remain NOT_TESTABLE; fully VERIFIED_PROJECT negative contribution remains ineligible for commercial pass; fully verified positive fixture remains eligible only at project-evidence level.
- replenished adjacent batch: PENDING
  1. zero-revenue verified scenario must not create a positive pass;
  2. invalid evidence class must fail closed;
  3. multiple simultaneous UNKNOWN required inputs must all be reported deterministically;
  4. decimal/rounding boundary scenarios must remain deterministic and never flip eligibility from rounding alone.
- boundary: public/hypothesis benchmarks are decision support, not project economics proof.

### C-003 — Franchise territory/tenancy validation
- status: VERIFIED
- fresh exact head: `154cf4d4dfb18a363542f54dee2c42c59fc0c46e`
- CI: Territory fixture validation `34796386872` SUCCESS.
- consumed manual batch: decision records now carry matched area versions, deterministic correlation ID, explicit synthetic evidence source/timestamp, and synthetic tenancy context; missing evidence context and invalid area versions fail closed.
- replenished adjacent batch: PENDING
  1. duplicate active area IDs must fail closed;
  2. duplicate postcode token within one area must not create duplicate evidence/correlation ambiguity;
  3. correlation must change when territory version changes;
  4. evidence timestamp/source must remain synthetic-only and never imply production tenancy migration.

### C-004 — GemVerse Level 2 fixture assurance
- status: VERIFIED
- fresh exact head: `2c5ee83d815c15fc9733bc6f89fada5986e3f70a`
- CI: Level 2 fixture validation `34796309971` SUCCESS.
- consumed manual batch: duplicate complete-target recovery is idempotent; prepared records missing mission/project identity fail closed; recovery records deterministic `PROMOTE_PREPARED` versus `ALREADY_COMPLETE`; synthetic recovery leaves canonical fixture unchanged.
- replenished adjacent batch: PENDING
  1. metadata-correct but payload-hash-mismatched prepared artifact must fail closed;
  2. non-canonical prepared target must fail closed before recovery decision;
  3. competing prepared artifacts with different correlations must not be silently selected;
  4. repeated recovery decision must remain byte-for-byte deterministic.

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

# MANUAL RECONCILIATION — 2026-09-14
- Fresh pre-action scan prevented duplicate Headless work: schedule had already advanced B-002 to `4053441d...` with CI SUCCESS.
- Manual execution advanced B-005, C-002, C-003 and C-004; all four exact post-action heads have CI SUCCESS after the mandatory second scan.
- A-001/A-002 remain fail-closed; A-003/A-004 remain safe AgentOS work while the ownership primitive is unresolved.
- B-001 remains commercial HOLD because freight/wholesale/dropship/stock/free-delivery contribution evidence is incomplete.
- No scheduler firing or worker claim was treated as completion. No overall GREEN.

# NEXT PASS ORDER
1. Fresh-scan all target repositories before action.
2. LANE A: A-001 only if new ownership-primitive evidence exists; otherwise A-003/A-004 without bypassing A-001.
3. LANE B: B-001 first; B-002/B-005 adjacent fail-closed batches remain safe while external commerce evidence is blocked.
4. LANE C: C-001 first unresolved venture; then the replenished C-002/C-003/C-004 homogeneous batches; C-005/C-006/C-007 remain useful PENDING work.
5. Fresh-scan every touched repo again before replenishment.
6. Preserve HOLD/BLOCKED/UNKNOWN states; no merge/deploy/credentials/production writes/purchases/supplier contact/live publication/production autonomy.
