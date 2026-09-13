# Commercial Frontend Build Gate Reconciliation — 2026-09-13

**Role:** Commercial Frontend Overseer  
**Status:** HOLD PRODUCTION FRONTEND / CONTINUE BOUNDED DISCOVERY  
**Canonical dependencies:** Overseer Issues #20 and #21; AgentOS Founding Beta Wave 0 entry gate

## Executive decision

Do not start a separate production Commercial Frontend build yet.

The current portfolio evidence still supports a commercial product direction based on **governed cross-system execution** rather than another vertical CRM or workflow builder. However, AgentOS itself has now reached a narrower and more urgent product milestone: prove one exact Founding Beta Wave 0 capability envelope on a physical Windows machine.

Commercial Frontend should therefore converge on, not compete with, that milestone.

The next commercial-frontend objective is to define and validate the minimum **approval / visibility cockpit contract** that can reuse the proven AgentOS interaction model once Wave 0 establishes it.

## Repository reconciliation

### Issues #20 and #21

Both remain open.

Their substantive gate is unchanged:
- Tradie AI Operations integration surface is promising, but customer pain / willingness-to-pay still require direct evidence.
- Ecommerce AI Operations integration surface is promising, but customer pain / supplier-system feasibility / willingness-to-pay still require direct evidence.
- Property Maintenance remains blocked until authoritative integration evidence exists.
- No production frontend is authorised by either issue.

### Existing wedge reports

The strongest current Tradie micro-wedge remains:

`Xero payment/status event -> ServiceM8 verification -> receipt/paid-invoice or closure recommendation -> human approval where needed -> bounded action -> re-read verification -> audit/evidence`

The strongest parallel Ecommerce wedge remains:

`Shopify order -> supplier/fulfilment exception -> customer impact assessment -> approval -> bounded fulfilment/customer action -> verification/audit`

Both remain commercial hypotheses until workflow frequency, measurable cost/friction and willingness-to-pay are directly evidenced.

## New AgentOS dependency

The current AgentOS Founding Beta entry assessment reports that Wave 0 is not yet ready. The narrow blocker set includes:
- exact beta build/ref and shipped-feature envelope;
- physical Windows install and first-launch acceptance;
- physical Basic Chat / first-job acceptance;
- governed Windows worker runtime pickup through the existing scheduler/local-wake path;
- exact-head Green/PRS assurance and false-success testing;
- tester-facing security/privacy/known-limitations package;
- internal Day 0 dry run.

This matters commercially because the proposed Commercial Frontend is an approval/visibility cockpit over governed execution. The portfolio should not build a second interaction shell before the canonical AgentOS interaction, stop/pause, approval, evidence and recovery semantics are proven with real users.

## Revised Commercial Frontend gate

### Gate CF-A — canonical interaction primitives

**Status: BLOCKED ON AGENTOS WAVE 0**

Before commercial vertical UI implementation, prove the reusable primitives in the canonical AgentOS surface:
- submit a real bounded job;
- understand status;
- see when approval is required;
- approve/deny safely;
- pause/stop;
- see truthful success/failure;
- restore state without replay;
- inspect evidence/verification outcome.

### Gate CF-B — vertical workflow evidence

**Status: AMBER / DISCOVERY ALLOWED**

For the Tradie and Ecommerce candidates, direct evidence is still required for:
- workflow frequency/volume;
- admin time or financial cost;
- failure consequence;
- actual systems used together;
- exact read/write permissions available;
- approval policy;
- willingness-to-pay;
- likely acquisition route.

Public documentation can verify incumbent capabilities and APIs. It cannot substitute for customer demand evidence.

### Gate CF-C — connector feasibility

**Tradie:** CONDITIONAL PASS FOR READ-ONLY / TEST-SPEC WORK.  
ServiceM8 + accounting integration is sufficiently evidenced to continue a bounded connector/test specification, but not live customer mutation.

**Ecommerce:** CONDITIONAL PASS FOR READ-ONLY / TEST-SPEC WORK.  
Shopify integration is sufficiently evidenced; supplier-system access remains variable and must be treated per supplier.

**Property:** BLOCKED.  
Do not design against assumed PropertyMe API/write capabilities without authoritative evidence.

### Gate CF-D — differentiated commercial value

**Status: NOT PROVEN**

Do not claim that the product wins because it adds AI to ServiceM8 or Shopify. Both ecosystems already contain meaningful AI and automation.

The current differentiation hypothesis is:

> AgentOS safely coordinates work **across** existing systems, presents exceptions/approvals in one place, executes only bounded authorised actions, verifies the result, and retains evidence.

This remains a hypothesis until customers show repeated pain and willingness to pay for it.

## Minimum reusable cockpit contract

Do not design a full product shell yet. The future vertical cockpit should be able to reuse a small set of AgentOS primitives:

1. **Work queue** — jobs/exceptions requiring attention.
2. **Context packet** — what happened, systems involved, relevant evidence.
3. **Recommended action** — proposed next bounded step and expected effect.
4. **Authority state** — automatic / approval required / blocked.
5. **Approve / deny / edit** — explicit human decision where policy requires it.
6. **Execution state** — pending / executing / stopped / failed / verified.
7. **Verification evidence** — re-read result, receipts/log references, mismatch explanation.
8. **Recovery state** — retry/reconcile/escalate without duplicate execution.
9. **Audit trail** — who/what/when/why/outcome.

These should be product-level primitives owned by AgentOS governance semantics, with vertical products supplying domain context and connectors rather than inventing alternate authority/state models.

## Next bounded work

Allowed now:
- keep Issues #20/#21 as the canonical commercial discovery thread;
- specify read-only connector proofs and representative fixtures for the Tradie and Ecommerce wedges;
- define direct-customer validation scripts and evidence fields;
- map the minimum cockpit contract to AgentOS Wave 0 interaction primitives;
- identify which frontend primitives can be reused unchanged across Tradie, Ecommerce, Franchise, Logistics and Hospitality.

Not authorised now:
- production vertical frontend implementation;
- alternate scheduler/queue/mission/authority system;
- live customer-system mutation;
- unsupported commercial claims;
- PropertyMe-based implementation assumptions;
- broad autonomous financial/customer actions.

## Build decision

**Commercial Frontend production build: HOLD.**

**Discovery/specification: CONTINUE.**

### Unlock condition

Start implementation only when both are true:

1. **AgentOS interaction proof:** the exact Wave 0 candidate demonstrates the reusable job/status/approval/stop/verification/recovery primitives on physical Windows with independent assurance; and
2. **Vertical commercial proof:** at least one candidate workflow has direct evidence of recurring pain, measurable outcome, feasible permissions and willingness-to-pay.

The preferred first candidate remains **Tradie AI Operations — post-payment / exception administrative closure**, because it is the smallest currently evidenced cross-system wedge. It is not yet a validated business.

## Portfolio architecture rule

Preserve:

`Vertical cockpit -> shared commercial layer -> AgentOS governance/execution/verification -> customer systems of record`

Do not invert this by making a vertical UI its own orchestration or authority layer.
