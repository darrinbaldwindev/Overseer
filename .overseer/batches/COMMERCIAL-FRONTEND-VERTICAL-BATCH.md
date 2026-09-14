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
- current parent item: `C-006 — Commercial Frontend workflow evidence` is PENDING.
- Issues #20 and #21 remain the canonical Commercial Frontend validation gates.
- production frontend remains HOLD.
- next every cycle: refresh parent batch, Issues #20/#21, Commercial Frontend reports, latest Overseer commits, and any AgentOS Wave-0 evidence that materially changes the shared interaction primitive.

### CF-A002 — Duplicate-work guard
- status: ACTIVE
- preserve existing architecture: vertical cockpit → shared commercial layer → AgentOS governance/execution/verification → customer systems of record.
- do not create another CRM, generic workflow builder, scheduler, authority layer, or system-of-record replacement.
- Property Maintenance stays blocked until authoritative current integration evidence exists.

---

# LANE CF-B — TRADIE AI OPERATIONS

### CF-B001 — Post-payment administrative closure evidence
- status: ACTIVE
- candidate flow: payment state → job/invoice identity verification → receipt/paid-invoice communication requirement → closure checklist → exception escalation → evidence/audit.
- verified platform gap already recorded: Xero-originated payment can sync back to ServiceM8 while native automatic receipt/paid-invoice communication remains a documented gap.
- still UNKNOWN: real operator frequency, minutes/case, actual failure cost, willingness to trial, willingness to pay.
- next batch: gather current authoritative platform evidence plus public operator/workflow evidence; classify separately from direct customer evidence.

### CF-B002 — Exact permission/read-write matrix
- status: PENDING
- map each step to required ServiceM8/Xero/communications read/write action, approval boundary, verification re-read, idempotency/replay requirement, and fail-closed behavior.
- no live customer connection or mutation.

### CF-B003 — Direct-validation packet
- status: PENDING
- convert existing validation protocol into a compact participant capture sheet and scoring template suitable for 10 interviews/observations.
- no fabricated interviews; public posts do not count as direct customer proof.

---

# LANE CF-C — ECOMMERCE AI OPERATIONS

### CF-C001 — Supplier/fulfilment exception evidence
- status: ACTIVE
- candidate flow: Shopify order → supplier/fulfilment status → tracking/ETA exception → customer-impact decision → approval → bounded Shopify/customer action → verification/audit.
- incumbent automation is already strong; generic Shopify Flow/webhook/fulfilment automation is not differentiation.
- still UNKNOWN: exception volume, supplier-system accessibility, measurable operator cost, willingness to pay.
- next batch: current platform evidence + public operator/workflow evidence for out-of-stock, late dispatch, split shipment, bad tracking, supplier substitution, return/refund reconciliation.

### CF-C002 — Exact permission/read-write matrix
- status: PENDING
- map Shopify order/fulfilment/hold/tracking/customer-communication actions and external supplier/accounting reads/writes; mark unsupported/UNKNOWN boundaries explicitly.
- no marketplace publication, refund execution, purchase or live customer mutation.

### CF-C003 — Portfolio leverage from GlobalShopCo
- status: PENDING
- inspect whether existing GlobalShopCo/Home Organisation supplier/freight/fulfilment evidence produces reusable exception taxonomy or acceptance fixtures.
- portfolio evidence may improve test design but cannot substitute for external customer demand.

---

# LANE CF-D — SHARED BUILD GATE / AGENTOS COUPLING

### CF-D001 — AgentOS Wave-0 dependency
- status: BLOCKED / MONITOR
- current AgentOS Founding Beta assessment says exact beta build identity, physical Windows acceptance, runtime worker hookup, exact-head assurance and beta security/privacy evidence remain incomplete.
- Commercial Frontend must not claim production readiness until the reusable AgentOS interaction/governance primitives needed by the wedge are proven on the relevant exact build.

### CF-D002 — Read-only prototype threshold
- status: PENDING
- only recommend a read-only/non-production prototype after at least 3 independent participants describe materially similar pain, read access is feasible, approval boundary is explicit and measurable outcome is defined.

### CF-D003 — Production build threshold
- status: BLOCKED
- requires direct evidence near the protocol target (10 relevant conversations or equivalent observations), repeated trial intent, several credible WTP signals, exact permissions/write actions, fail-closed verification design, relevant AgentOS Wave-0 proof and no critical authority/security unknown.

---

# CURRENT EXECUTION PASS — 2026-09-14

Planned consumption order:
1. CF-B001 current Tradie evidence.
2. CF-C001 current Ecommerce evidence.
3. CF-B002 / CF-C002 permission matrices where authoritative documentation allows exact mapping.
4. CF-B003 capture/scoring packet.
5. CF-C003 portfolio reuse scan.
6. Reconcile Issues #20/#21 and replenish this file.

Blocked items do not terminate the pass while eligible research/specification work remains.
