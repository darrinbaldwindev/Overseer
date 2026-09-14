# Commercial Frontend Vertical Execution Batch

**Role:** Commercial Frontend Overseer  
**Parent manifest:** `.overseer/batches/PORTFOLIO-EXECUTION-BATCH.md` → `C-006 — Commercial Frontend workflow evidence`  
**Purpose:** maximize useful bounded work per manual Commercial Frontend cycle without creating another scheduler, authority source, mission ledger, registry, Green system, PRS system, or source of truth.

## Standing manual rule

In this workstream, `cont` / `continue autonomously` means:

1. fresh-scan the current Overseer repository before action;
2. reconcile this file against current issues, reports, commits, CI/runtime evidence and the parent portfolio batch;
3. execute as much safe useful work from this vertical batch as possible, preferring multiple adjacent tasks over one tiny task;
4. do not stop merely because one item is blocked when other eligible work exists;
5. fresh-scan relevant repo state again before reconciliation;
6. record exact evidence, preserve UNKNOWN/BLOCKED/HOLD states, and replenish this same vertical batch before returning control.

Live repository/issues/runtime evidence always overrides this file.

## Authority boundary

This batch authorizes research, evidence reconciliation, issue/report updates, non-production specifications, and bounded read-only/prototype planning only. It does **not** authorize production frontend implementation, customer-system mutation, credentials, purchases, paid campaigns, supplier/customer contact, legal commitments, merge/deploy/ready transitions, or production autonomy.

States: `PENDING`, `ACTIVE`, `VERIFIED`, `BLOCKED`, `STALE`, `SPLIT_REQUIRED`.

---

# LANE CF-A — CANONICAL RECONCILIATION

### CF-A001 — Parent-state reconciliation
- status: VERIFIED
- parent `C-006` remains PENDING and Issues #20/#21 remain canonical Commercial Frontend gates.
- production frontend remains HOLD.
- fresh pre- and post-action scans were completed on 2026-09-14; no concurrent Commercial Frontend work superseded this pass.
- next every cycle: refresh parent batch, Issues #20/#21, Commercial Frontend reports, latest Overseer commits, and any AgentOS Wave-0 evidence that materially changes the shared interaction primitive.

### CF-A002 — Duplicate-work guard
- status: VERIFIED / CONTINUOUS
- architecture preserved: vertical cockpit → shared commercial layer → AgentOS governance/execution/verification → customer systems of record.
- no CRM replacement, generic workflow builder, scheduler, authority layer or system-of-record replacement created.
- Property Maintenance remains blocked until authoritative current integration evidence exists.

---

# LANE CF-B — TRADIE AI OPERATIONS

### CF-B001 — Post-payment administrative closure evidence
- status: VERIFIED for platform/public-evidence pass; direct demand remains UNKNOWN
- durable evidence: `reports/2026-09-14-commercial-frontend-vertical-batch-001.md`.
- native ServiceM8/Xero receipt gap reconfirmed from current ServiceM8 documentation.
- ServiceM8 read primitives confirmed for jobs and job payments; Xero granular read scopes confirmed for invoices/payments.
- public Australian operator signal supports broad multi-app/admin friction but does not prove this micro-wedge frequency or WTP.
- next: direct participant/observed-workflow evidence only; do not substitute public posts.

### CF-B002 — Exact permission/read-write matrix
- status: VERIFIED / PARTIAL
- matrix recorded in Batch 001.
- read path: Xero payment/invoice + ServiceM8 job/payment is concrete.
- ServiceM8 Messaging API email primitive confirmed; exact auth/document-generation contract requires implementation-time test.
- exact closure-state write path remains UNKNOWN/BLOCKED and must not be inferred.
- replenished next: specify synthetic Tradie exception fixtures and idempotency/verification contract without live mutation.

### CF-B003 — Direct-validation packet
- status: VERIFIED
- durable artifact: `reports/2026-09-14-commercial-frontend-participant-capture-pack.md`.
- contains one-sheet participant capture, authority boundary matrix, scoring rubric, hard blockers and 10-participant aggregate dashboard.
- next: populate only with real conversations/observations; no fabricated participant rows.

### CF-B004 — Tradie synthetic exception fixture specification
- status: PENDING
- minimum cases: fully paid clean match; partial payment; reversed payment; duplicate customer/invoice identity; sync lag; disputed payment; missing recipient; prior-send replay; verification re-read failure.
- acceptance: no external mutation; each case must yield deterministic `ALLOW_PREPARE`, `REQUIRE_APPROVAL`, `BLOCK`, or `VERIFY_FAILED` plus evidence reason.

---

# LANE CF-C — ECOMMERCE AI OPERATIONS

### CF-C001 — Supplier/fulfilment exception evidence
- status: VERIFIED for platform/public-evidence pass; direct demand remains UNKNOWN
- durable evidence: `reports/2026-09-14-commercial-frontend-vertical-batch-001.md`.
- current Shopify API confirms bounded fulfilment read, hold, release and tracking-update primitives.
- public merchant signal specifically describes multi-supplier dispatch emails, manual VA tracking upload, $15/hour cost and 12+ hour customer-tracking delay; classified PUBLIC OPERATOR SIGNAL only.
- additional public signals cover supplier stock/SKU mismatch and severe late-delivery consequence.
- next: direct participant evidence and supplier-side connector feasibility by actual supplier stack.

### CF-C002 — Exact permission/read-write matrix
- status: VERIFIED / PARTIAL
- Shopify read/hold/tracking/release action surface mapped in Batch 001.
- relevant write fulfilment scopes + `fulfill_and_ship_orders` permission are explicit.
- supplier-side read/write boundary remains provider-specific/UNKNOWN and is a hard gate.
- replenished next: specify synthetic supplier/tracking exception fixtures without live Shopify mutation.

### CF-C003 — Portfolio leverage from GlobalShopCo
- status: VERIFIED
- GlobalShopCo Home Organisation/eBay research yields reusable fixture concepts: exact SKU/supplier identity, stock assurance, freight, fulfilment identity, dropship permission, channel permission, landed economics and HOLD on missing evidence.
- Batch 001 records a 12-category exception taxonomy.
- portfolio evidence is test-design input only, not customer-demand proof.

### CF-C004 — Ecommerce synthetic exception cockpit specification
- status: PENDING
- minimum cases: supplier stock unknown; stock mismatch; SKU mismatch; tracking missing; tracking conflicting; late dispatch/ETA risk; split fulfilment; customer promise at risk; hold required; release attempt with wrong hold identity; supplier evidence stale; verification re-read failure.
- acceptance: no production connector or mutation; deterministic evidence/status/action recommendation and explicit approval boundary.

---

# LANE CF-D — SHARED BUILD GATE / AGENTOS COUPLING

### CF-D001 — AgentOS Wave-0 dependency
- status: BLOCKED / MONITOR
- current Founding Beta assessment still says exact beta build identity, physical Windows acceptance, runtime worker hookup, exact-head assurance and beta security/privacy evidence are incomplete.
- Commercial Frontend must not claim production readiness until required AgentOS interaction/governance primitives are proven on the relevant exact build.

### CF-D002 — Read-only prototype threshold
- status: BLOCKED ON DIRECT EVIDENCE
- at least 3 independent materially similar direct participants/observations are still required, plus feasible reads, explicit approval boundary and measurable outcome.
- public operator posts do not satisfy this threshold.

### CF-D003 — Production build threshold
- status: BLOCKED
- requires approximately 10 relevant direct conversations/observations or equivalent evidence, repeated trial intent, several credible WTP signals, exact permissions/write actions, fail-closed verification design, relevant AgentOS Wave-0 proof and no critical authority/security unknown.

---

# COMPLETED EXECUTION PASS — VERTICAL BATCH 001 — 2026-09-14

Consumed in one owner-triggered cycle:
1. fresh Overseer/parent-manifest/reports scan;
2. created this dedicated vertical batch under parent C-006;
3. current Tradie platform + public operator evidence pass;
4. current Ecommerce platform + public operator evidence pass;
5. exact partial permission/read-write matrices for both wedges;
6. GlobalShopCo portfolio-reuse scan and exception taxonomy;
7. participant capture/scoring pack for 10-case validation set;
8. fresh post-action repo scan and reconciliation.

Durable commits:
- `28a3b558cc38f8b90b3f6cc96077d43b348adbdc` — vertical batch created.
- `ac1283edc3eed4d042b9b7967e7f6bf874a94eed` — Batch 001 evidence + permission matrix.
- `1c9c7427d439cb524c26f322dd0f6a809765be70` — participant capture pack.

No production frontend code, customer-system mutation, credentials, purchases, outreach, deployment or overall GREEN occurred.

# NEXT `cont` ORDER

1. Fresh scan first.
2. CF-C004 Ecommerce synthetic exception cockpit specification — priority because current public workflow signal is strongest and Shopify primitives are concrete.
3. CF-B004 Tradie synthetic exception fixture specification.
4. Deepen supplier-side connector feasibility using actual provider classes without credentials/live connections.
5. Re-check AgentOS Wave-0 dependency and Issues #20/#21.
6. Reconcile/replenish this same file before returning control.
