# PORTFOLIO BATCH ENGINE

## Status
Canonical execution procedure for every portfolio Project Overseer and project chat.

This file contains the common execution engine. Project-specific differences belong in `.overseer/profiles/PROJECT-BATCH-PROFILES.md` and in the project's live vertical batch. Do not fork this engine into project-specific variants unless the owner explicitly changes the portfolio architecture.

## Read order for every cycle
Every Project Overseer must read, in this order:
1. this canonical engine;
2. its matching project profile in `darrinbaldwindev/Overseer/.overseer/profiles/PROJECT-BATCH-PROFILES.md`;
3. the project's current repository/control issue/PR state;
4. the project's live vertical batch file, normally `.overseer/batches/VERTICAL-EXECUTION-BATCH.md`, or its documented established alternate path;
5. relevant canonical portfolio evidence in `darrinbaldwindev/Overseer#49`.

Repository/runtime/CI evidence outranks batch text. The batch is a hypothesis, never authority.

## Universal cycle
Owner triggers `cont`, `continue`, `continue autonomously`, or `continue autonomously vertically` mean:

**FRESH SCAN -> RECONCILE -> EXECUTE DEEPLY -> VERIFY -> FRESH SCAN -> REPLENISH -> DURABLE LOG -> HANDOFF**

### 1. Fresh scan
Refresh current default branch, active branches/PRs, exact heads, relevant issue comments, CI/workflow evidence, implicated files/tests/contracts, known blockers/UNKNOWN/HOLD states, and concurrent portfolio work.

### 2. Reconcile
Correct stale batch assumptions before execution. Never overwrite newer concurrent evidence. Split mixed-confidence items instead of promoting siblings together.

### 3. Execute deeply
Consume the highest-value safe coherent work. Normally complete 2–5 homogeneous adjacent items, or one critical item plus its tests/evidence closure. If the top item blocks, record the blocker and immediately continue to independent safe work.

### 4. Verify
Use the strongest applicable evidence: runtime/physical acceptance, exact-head CI, exact committed tests/fixtures, authoritative repo/issue/PR state, then authoritative external research. Worker claims and scheduler firing are leads, not completion evidence.

### 5. Fresh scan again
Re-read heads, CI, concurrent commits, batch file, issue state and newly exposed blockers before writing replenishment.

### 6. Replenish
Keep the same live project batch populated with the next highest-value safe work. Preserve BLOCKED/HOLD/UNKNOWN truth. Do not create a second batch/control system because one item is blocked.

### 7. Durable log
Record material results in the project's established control log/issue and surface portfolio-significant state to `darrinbaldwindev/Overseer#49`.

### 8. Handoff
Leave exact current heads/evidence, blockers, next tasks, and owning schedule/Project Overseer clear enough for another execution context to continue without chat history.

## Universal task fields
Every substantive batch item should carry, where applicable:
- task ID and state;
- objective;
- exact repo/branch/PR/head anchor;
- dependencies;
- acceptance criteria;
- evidence required;
- applicable security/governance gates;
- negative/adversarial cases;
- owner/protected boundary;
- next handoff.

Recommended states: `PENDING | ACTIVE | VERIFIED | BLOCKED | HOLD | STALE | SPLIT_REQUIRED`.

## Universal governance
Unless explicitly authorized, no batch permits merge, approval, ready transition, rebase, deployment, credential/security-setting changes, production writes, publication/listing activation, purchases/spend, supplier/customer/partner outreach, campaign activation, unrestricted elevation, or production autonomy.

**NO MODEL DECIDES ITS OWN AUTHORITY.**

Do not create duplicate scheduler, queue, authority source, registry, mission ledger, persistence/memory system, governance layer, Green system or PRS system.

## Assurance rule
Functional verification, security assurance and independent PRS assurance are separate dimensions. Passing one never silently promotes another. Exact-head identity/evidence lineage must be preserved where assurance matters.

## Research/commercial rule
Capture exact identities, source/date/freshness, permissions/eligibility, economics/fees/freight, returns/warranty/compliance and explicit UNKNOWNs appropriate to the project. Missing material evidence must not be replaced by optimistic inference.

## Content/marketing rule
Separate creation from evidence. Content may be drafted/optimized/tested without implying publication, partner status, market validation, conversion proof or campaign success.

## Concurrency rule
If another schedule/worker changes a target or batch while a cycle is running, re-read and reconcile. Never force stale state over newer verified evidence.

## Completion rule
A cycle is complete only when safe useful work has been consumed as far as current tools/authority allow, exact state has been verified, the batch has been replenished, and material progress/blockers are durably logged.

Scheduler firing alone never means the portfolio or project advanced, and never implies GREEN.