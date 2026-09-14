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
- fresh pre-action scan on 2026-09-14 found no concurrent Commercial Frontend work superseding the lane.
- AgentOS PR #104 remains OPEN/DRAFT/UNMERGED and current execution/governance prerequisites are not independently proven on the current head.
- next every cycle: refresh parent batch, Issues #20/#21, Commercial Frontend reports, latest Overseer commits, and any AgentOS evidence that materially changes the shared interaction primitive.

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
- native ServiceM8/Xero receipt gap and bounded read/message primitives remain the platform basis.
- next: direct participant/observed-workflow evidence only; do not substitute public posts or synthetic fixtures.

### CF-B002 — Exact permission/read-write matrix
- status: VERIFIED / PARTIAL
- read path: Xero payment/invoice + ServiceM8 job/payment is concrete.
- ServiceM8 Messaging API email primitive confirmed; exact auth/document-generation contract requires implementation-time test.
- exact closure-state write path remains UNKNOWN/BLOCKED and must not be inferred.

### CF-B003 — Direct-validation packet
- status: VERIFIED
- durable artifact: `reports/2026-09-14-commercial-frontend-participant-capture-pack.md`.
- next: populate only with real conversations/observations; no fabricated participant rows.

### CF-B004 — Tradie synthetic exception fixture specification
- status: VERIFIED
- durable artifact: `reports/2026-09-14-commercial-frontend-tradie-synthetic-exception-spec.md`.
- specified deterministic cases for clean full payment, partial, reversed, disputed, ambiguous identity, sync lag, missing recipient, replay/prior-send, approval missing, system-state conflict and verification re-read failure.
- deterministic outcomes: `ALLOW_PREPARE`, `REQUIRE_APPROVAL`, `BLOCK`, `VERIFY_FAILED`.
- zero external Xero/ServiceM8/customer mutation authorised.
- replenished next: CF-B005 fixture-harness mapping against an existing suitable test/fixture seam only; do not create a duplicate runtime.

### CF-B005 — Tradie synthetic harness mapping
- status: PENDING
- inspect existing Overseer/AgentOS fixture/test conventions and identify the smallest reusable non-production seam for TR-001..TR-012.
- acceptance: map schema + expected results into existing test conventions with zero external provider invocation; if no suitable seam exists, produce implementation-ready mapping only and stop rather than creating a new execution system.

---

# LANE CF-C — ECOMMERCE AI OPERATIONS

### CF-C001 — Supplier/fulfilment exception evidence
- status: VERIFIED for platform/public-evidence pass; direct demand remains UNKNOWN
- current Shopify primitives remain sufficient for bounded fulfilment read/hold/release/tracking proposals.
- public merchant evidence remains signal only, not direct validation.
- next: direct participant evidence plus provider-specific supplier evidence.

### CF-C002 — Exact permission/read-write matrix
- status: VERIFIED / PARTIAL
- Shopify action surface mapped.
- supplier-side boundary is now split by provider class rather than one undifferentiated UNKNOWN.

### CF-C003 — Portfolio leverage from GlobalShopCo
- status: VERIFIED
- exact SKU/supplier identity, stock assurance, freight, fulfilment identity, dropship permission, channel permission, landed economics and HOLD-on-missing-evidence remain reusable fixture concepts only.

### CF-C004 — Ecommerce synthetic exception cockpit specification
- status: VERIFIED
- durable artifact: `reports/2026-09-14-commercial-frontend-ecommerce-synthetic-exception-spec.md`.
- covers stock unknown/mismatch, SKU mismatch, tracking missing/conflicting/wrong order, late dispatch, split fulfilment, customer promise risk, hold, wrong hold identity, stale/contradictory supplier evidence, replay and verification failure.
- deterministic outcomes and reason-code vocabulary fixed; no production connector/mutation.
- replenished next: CF-C006 fixture-harness mapping against existing suitable test conventions.

### CF-C005 — Supplier connector feasibility
- status: VERIFIED / PARTIAL
- durable artifact: `reports/2026-09-14-commercial-frontend-supplier-connector-feasibility.md`.
- CJdropshipping: PARTIAL PASS for current public API-level product/variant identity, real-time stock, shop/product connection, order flows and sandbox/read-oriented feasibility. Production authority/terms remain UNKNOWN.
- Dropshipzone/New Aim: PARTIAL PASS for documented Shopify setup, auto inventory/order/fulfilment/tracking and API-integration surface. Exact API/account/event semantics remain UNKNOWN.
- DSers/AliExpress-style provider class: insufficient current authoritative API-level evidence this cycle; remains UNKNOWN rather than inferred from app marketing.
- next: define provider-neutral stale/duplicate/out-of-order evidence fixtures; do not create live connectors.

### CF-C006 — Ecommerce synthetic harness mapping
- status: PENDING
- inspect existing portfolio fixture/test conventions and map EC-001..EC-014 into the smallest reusable non-production seam.
- acceptance: deterministic decisions/reason codes, replay denial, stale-evidence denial, split-fulfilment scope preservation and verify-failure semantics with zero network/provider mutation.

### CF-C007 — Supplier event-order assurance specification
- status: PENDING
- define provider-neutral fixtures for duplicate supplier event, out-of-order stock event, stale tracking event, later superseding evidence, and contradictory same-version evidence.
- bind exact provider/order/product/variant identity and evidence timestamp/version; no provider write path.

---

# LANE CF-D — SHARED BUILD GATE / AGENTOS COUPLING

### CF-D001 — AgentOS dependency
- status: BLOCKED / MONITOR
- fresh 2026-09-14 check: AgentOS PR #104 remains OPEN/DRAFT/UNMERGED.
- current PR evidence continues to report the continuous ownership race, incomplete authenticated transport/grant binding, current-head physical Windows acceptance gap and absent independent current-head Green/PRS completion.
- Commercial Frontend must not claim production readiness until required AgentOS interaction/governance primitives are proven on the relevant exact build.

### CF-D002 — Read-only prototype threshold
- status: BLOCKED ON DIRECT EVIDENCE
- at least 3 independent materially similar direct participants/observations are still required, plus feasible reads, explicit approval boundary and measurable outcome.
- public operator posts and synthetic fixture success do not satisfy this threshold.

### CF-D003 — Production build threshold
- status: BLOCKED
- requires approximately 10 relevant direct conversations/observations or equivalent evidence, repeated trial intent, several credible WTP signals, exact permissions/write actions, fail-closed verification design, relevant AgentOS proof and no critical authority/security unknown.

---

# COMPLETED EXECUTION PASS — VERTICAL BATCH 002 — 2026-09-14

Consumed in one owner-triggered cycle:
1. fresh Overseer parent/vertical batch, Issues #20/#21 and recent-commit scan;
2. fresh AgentOS PR #104 dependency check;
3. Ecommerce synthetic exception cockpit specification (`EC-001..EC-014`);
4. Tradie synthetic exception fixture specification (`TR-001..TR-012`);
5. current supplier-side connector feasibility split across Dropshipzone/New Aim, CJdropshipping and DSers/AliExpress-style provider classes;
6. provider-neutral supplier evidence envelope and first implementation sequence;
7. vertical batch reconciliation/replenishment.

Durable commits:
- `73860a60d538e71d877b901acb29e02217ab202d` — Ecommerce synthetic exception cockpit spec.
- `a71d28ac8470a5614bdd327b163acb5664b66d1a` — Tradie synthetic exception fixture spec.
- `a07395af2a714d4b2086dab2317626bc75f08b55` — supplier connector feasibility pass.

No production frontend code, customer-system mutation, credentials, purchases, outreach, deployment, connector activation or overall GREEN occurred.

# NEXT `cont` ORDER

1. Fresh scan first.
2. CF-C006 — map Ecommerce synthetic cases into an existing suitable fixture/test seam without creating a runtime.
3. CF-B005 — map Tradie synthetic cases into the same or existing suitable fixture/test conventions.
4. CF-C007 — supplier duplicate/out-of-order/stale/supersession evidence assurance spec.
5. Re-check direct-evidence gate and AgentOS dependency.
6. Fresh re-scan, record exact evidence, and replenish this same file before returning control.
