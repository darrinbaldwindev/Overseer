# Portfolio Execution Batch Manifest

**Purpose:** bounded execution manifest consumed by the existing ChatGPT schedules. This file is **not** a new scheduler, queue, mission ledger, authority source, registry, Green system, PRS system, or project source of truth. Repository/issues/runtime evidence remain authoritative.

**Owner direction:** schedules stay focused on their existing priority projects. As gates become VERIFIED GREEN, equivalent work may expand into small homogeneous batches. Manual `continue autonomously vertically` remains the whole-portfolio large-batch path.

## Batch lifecycle

1. Execution schedules read this file and the latest durable project evidence before acting.
2. A schedule may claim only items in its own lane and may execute several safe items in one wake when useful.
3. Before mutation/research/test work, refresh the target repository/ref/evidence. Stale batch text never overrides current repository state.
4. Each item is reconciled as `PENDING`, `ACTIVE`, `VERIFIED`, `BLOCKED`, `STALE`, or `SPLIT_REQUIRED` with exact evidence in the appropriate project issue/log and Overseer #49.
5. The :30 Portfolio Checkpoint reconciles completed/blocked/stale items, removes no historical evidence, and **replenishes the next pass** with the highest-value safe adjacent work from the same scheduled priority lanes.
6. A VERIFIED GREEN gate may replenish 2–5 homogeneous adjacent items. Repeated clean passes may cautiously increase batch size. Any mixed-confidence or failed item is split out and fails closed.
7. No batch entry grants merge/deploy/credentials/production writes/purchases/supplier contact/listing publication/campaign activation/production autonomy.

## Replenishment policy

- Keep each execution lane supplied with at least one useful `PENDING` item when safe work exists.
- Prefer implementation/test/evidence closure over scans/status-only work.
- Do not replenish duplicate work already present in repo/issues/PRs.
- If an item is blocked by owner authority, physical host, credentials, or external commercial evidence, retain the blocker and replenish a different safe item in the same lane.
- Do not turn scheduler firing, issue creation, or worker claims into completion.
- Replenishment must preserve current priority order; it does not broaden scheduled scope to the whole portfolio.

---

# LANE A — AGENTOS LEVEL 2 P0 (:00)

### A-001 — Continuous ownership fence
- status: PENDING
- priority: P0
- target: AgentOS PR #104/successor exact current head
- action: advance the continuous ownership-preserving project-file fence across final verification -> publish/prepared recovery -> success-receipt persistence.
- acceptance: exact-head tests/CI plus no unresolved stale/replaced-owner race for the property changed.
- batch_rule: single critical-path change until independently green.

### A-002 — Ownership adversarial regressions
- status: PENDING
- priority: P0
- target: AgentOS PR #104/successor
- action: replacement-after-verification, three-writer, stale/replaced identity, crash/replay, duplicate-result and false-success tests adjacent to A-001.
- acceptance: deterministic regression coverage on unchanged exact head.
- batch_rule: may group 2–5 homogeneous regression cases only after the underlying ownership primitive is stable.

### A-003 — Authority/admission continuation
- status: PENDING
- priority: P1-after-A-001/A-002
- target: canonical remote authority-admission / pickup lineage
- action: bind trusted transport actor context and canonical grant evidence without self-granting request fields.
- acceptance: fail-closed tests and no duplicate authority layer.

---

# LANE B — COMMERCE PRIORITY (:15)

### B-001 — GlobalShopCo Home Organisation economics closure
- status: PENDING
- priority: P0-commerce
- target: GlobalShopCo issues #9/#18
- action: advance exact SKU candidates toward evidence-complete supplier identity, wholesale, freight, free-delivery economics, returns/warranty, stock and explicit UNKNOWN closure.
- acceptance: missing freight or supplier/channel evidence remains HOLD.
- batch_rule: once one gate is VERIFIED GREEN, replenish 2–5 equivalent compact candidates.

### B-002 — GlobalShopCo-Headless M3 checkout slice
- status: PENDING
- priority: P1-commerce
- target: GlobalShopCo-Headless issue #3 / active M3 branch
- action: consume current deterministic checkout/security evidence and advance the smallest non-production storefront -> Shopify checkout handoff gate.
- acceptance: Shopify remains source of truth; no arbitrary checkout destination; deterministic tests.
- batch_rule: small group of equivalent no-network edge cases after green.

### B-003 — Shopify -> eBay readiness
- status: PENDING
- priority: P1-commerce
- target: GlobalShopCo #17 + shopify_ebay
- action: advance deterministic candidate mapping/readiness and evidence-complete pilot criteria without install/account connection/listing publication.
- acceptance: marketplace permission, fulfilment identity, stock method and landed economics remain fail-closed.
- batch_rule: 2–5 equivalent candidate records only after mapper/gate is green.

### B-004 — Shopify -> Amazon readiness
- status: PENDING
- priority: P2-commerce
- target: GlobalShopCo #23
- action: advance seller-of-record/category/GTIN/fulfilment/economics evidence model without seller setup.
- acceptance: owned-site/eBay/MyPrimeDelivery state cannot imply Amazon eligibility.
- batch_rule: small equivalent candidate set after gate verification.

### B-005 — MyPrimeDelivery synthetic WordPress slice
- status: PENDING
- priority: P2-commerce
- target: MyPrimeDelivery issue #2
- action: consume exact-head fixture CI and advance synthetic WordPress rendering/schema path without claiming live Prime/ranking evidence.
- acceptance: no live commercial data/affiliate URL leaks; Prime/ranking remain evidence-gated.
- batch_rule: 2–5 synthetic equivalent fixture/render cases after green.

---

# LANE C — PRODUCT / CONTENT / VENTURES PRIORITY (:45)

### C-001 — Affiliate Websites governed CTA/program evidence
- status: PENDING
- priority: P1-ventures
- target: Affiliate-Websites master + AU/UK/US issues #8/#10/#11/#12
- action: advance evidence-gated programme records and reusable CTA/data contract; consumer referral != publisher affiliate.
- acceptance: stale/unknown/referral-only evidence cannot become verified publisher CTA.
- batch_rule: 2–5 verified-equivalent programme records once CTA gate is green.

### C-002 — GhostKitchen economics batch
- status: PENDING
- priority: P1-ventures
- target: GhostKitchen #16/#23/#24/#10
- action: advance deterministic delivery-channel/unit-economics scenarios with public benchmarks clearly separated from project-verified costs.
- acceptance: incomplete project economics = NOT_TESTABLE / decision-support only.
- batch_rule: 2–5 homogeneous scenarios after calculator/validation green.

### C-003 — Franchise territory/tenancy validation
- status: PENDING
- priority: P1-ventures
- target: Franchise #18/#19
- action: advance fail-closed tenancy/territory fixtures and auditability without production migration.
- acceptance: ambiguous overlap and inactive/unknown franchise routing fail closed.
- batch_rule: 2–5 synthetic equivalent routing/tenancy cases after green.

### C-004 — GemVerse Level 2 fixture assurance
- status: PENDING
- priority: P2-ventures
- target: GemVerse Level 2 fixture/issues
- action: advance machine-checkable exact-preimage/target/replay/recovery cases without inventing canon.
- acceptance: partial/truncated/replayed mutation cannot masquerade as successful canon update.
- batch_rule: several deterministic fixture cases after base validator green.

### C-005 — Content360 provider-neutral adapter
- status: PENDING
- priority: P2-ventures
- target: content360 issue #2
- action: consume official/public contract research when available and extend request/result schemas/mock failure cases; no credential or live publish.
- acceptance: publish/schedule remain disabled unless explicitly approved and later verified.
- batch_rule: 2–5 mock contract/error cases after adapter CI green.

### C-006 — Commercial Frontend workflow evidence
- status: PENDING
- priority: P2-ventures
- target: Overseer Commercial Frontend issue #21
- action: deepen Tradie/Ecommerce wedge evidence around real cross-system exception workflows and integration feasibility.
- acceptance: customer pain/frequency/WTP remain UNKNOWN unless evidenced.
- batch_rule: 2–5 equivalent workflow records after evidence template is stable.

### C-007 — AgentOS marketing objection acceptance
- status: PENDING
- priority: P2-ventures
- target: AgentOS issue #109
- action: turn one or more objection gates into directly testable onboarding/pricing/demo evidence without unsupported claims.
- acceptance: planned mitigation != product evidence.
- batch_rule: small homogeneous objection-test set after first acceptance surface is green.

---

# ASSURANCE (:37)

The assurance schedule does **not** consume normal implementation items. It independently challenges the newest AgentOS Level 2 result and may mark only narrowly evidenced properties as PASS/FAIL/INSUFFICIENT. PRS runs only after Green passes the identical exact head.

# CHECKPOINT / REPLENISHER (:30)

At each pass:
- reconcile exact evidence for items acted on since the prior checkpoint;
- mark stale entries when repository state moved;
- keep blocked items explicit but do not let them starve other safe work;
- replenish LANE A/B/C from their existing scheduled priority sets;
- when a gate is repeatedly VERIFIED GREEN, add the next 2–5 homogeneous adjacent items rather than one item at a time;
- never broaden the scheduled project universe merely to fill the batch;
- append a concise durable reconciliation to Overseer #49.

**Initial manifest state:** seeded 2026-09-14 from current active schedule priorities. All entries require fresh evidence before execution.