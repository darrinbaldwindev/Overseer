# PORTFOLIO BATCH ENGINE

## Status
Canonical execution procedure for every portfolio Project Overseer and Overseer-role project chat.

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

**FRESH SCAN -> RECONCILE -> SHOW CURRENT BATCH -> EXECUTE DEEPLY -> VERIFY -> FRESH SCAN -> REPLENISH -> SHOW UPDATED BATCH -> DURABLE LOG -> HANDOFF**

### 1. Fresh scan
Refresh current default branch, active branches/PRs, exact heads, relevant issue comments, CI/workflow evidence, implicated files/tests/contracts, known blockers/UNKNOWN/HOLD states, and concurrent portfolio work.

### 2. Reconcile
Correct stale batch assumptions before execution. Never overwrite newer concurrent evidence. Split mixed-confidence items instead of promoting siblings together.

### 3. Chat-facing Current Batch view
Every Overseer-role chat must make the live batch visible to the owner in the chat window whenever it is actively handling that project/workstream. Do not require the owner to open GitHub merely to understand the queue.

After the fresh scan/reconciliation, include a compact **Current Batch** section with, where present:
- **ACTIVE NOW** — the item(s) being executed in this cycle;
- **NEXT** — the highest-value PENDING items already queued;
- **BLOCKED / HOLD / UNKNOWN** — exact blockers that matter;
- **VERIFIED SINCE LAST CYCLE** — newly evidenced completions only;
- **BATCH SOURCE** — local batch path plus relevant exact head/PR/evidence anchor.

Keep this view compact. It is a human-readable projection of durable state, not a second source of truth. Never invent tasks from chat memory. If the batch is stale, first reconcile it from current evidence, then show the corrected view.

At the end of the cycle, show an **Updated Batch** summary identifying what moved, what remains blocked, and what is queued next. If nothing materially changed, say so explicitly rather than manufacturing movement.

This visibility rule applies to Project Overseers, Specialist Overseers and scheduled Overseer execution contexts when they produce owner-facing output. It does **not** apply to ordinary unrelated chats merely because they are open in the same ChatGPT Project.

### 4. Execute deeply
Consume the highest-value safe coherent work. Normally complete 2–5 homogeneous adjacent items, or one critical item plus its tests/evidence closure. If the top item blocks, record the blocker and immediately continue to independent safe work.

### 5. Verify
Use the strongest applicable evidence: runtime/physical acceptance, exact-head CI, exact committed tests/fixtures, authoritative repo/issue/PR state, then authoritative external research. Worker claims and scheduler firing are leads, not completion evidence.

### 6. Fresh scan again
Re-read heads, CI, concurrent commits, batch file, issue state and newly exposed blockers before writing replenishment.

### 7. Replenish
Keep the same live project batch populated with the next highest-value safe work. Preserve BLOCKED/HOLD/UNKNOWN truth. Do not create a second batch/control system because one item is blocked.

### 8. Durable log
Record material results in the project's established control log/issue and surface portfolio-significant state to `darrinbaldwindev/Overseer#49`.

### 9. Handoff
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
A cycle is complete only when safe useful work has been consumed as far as current tools/authority allow, exact state has been verified, the batch has been replenished, the owner-facing chat view has been updated when applicable, and material progress/blockers are durably logged.

Scheduler firing alone never means the portfolio or project advanced, and never implies GREEN.