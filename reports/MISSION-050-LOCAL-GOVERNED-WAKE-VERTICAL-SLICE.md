# Mission 050 — Local Governed Wake Vertical Slice

**Date:** 2026-09-02
**Owner:** CHATGPT Overseer
**Status:** VERIFIED_FOR_REPOSITORY_AND_CI; LOCAL-HOST_EXECUTION PENDING

## Objective
Advance the AgentOS local runtime vertically rather than broadening horizontally. Replace the manual-wake execution shortcut with the canonical conflict-safe dispatch runner and add the minimum governed budget boundary required for a bounded mission execution.

## Vertical slice
Project identity → Mission → Verified Worker → Scoped Task → Budget → Execution → Verification → Audit/Result.

## Work completed
- Added `runtime/local-dispatch-store.mjs` as a durable adapter from the existing local persistence layer to the canonical `runNextTask`/`safeWriteTask` runner. No second dispatch runtime or queue was introduced.
- Refactored `runtime/local-wake.mjs` to use the canonical runner rather than directly invoking `runLocalProjectOverseerCycle`.
- Added explicit non-empty local `project_id`, mission identity, wake trace, consent mode, required capability, granted capability and bounded DRY_RUN constraints to the wake envelope.
- Added strict local envelope validation before worker execution: project identity, PRE_AUTHORIZED consent, required/granted capability matching and production-scope rejection.
- Added `runtime/mission-budget.mjs`, an additive SQLite **budget ledger only**. It is not a mission/task database and does not replace AgentOS persistence.
- Added two-phase budget control: reservation before execution and reconciliation after execution; failure path reconciles zero actual units where possible.
- Preserved response schema validation and durable response/event records, now including project and budget correlation.

## Verification
- AgentOS Tests workflow run `33635102740` completed **SUCCESS** for commit `056cd9f47b7a486dfff190ab04fb89f80a8e985c`.
- Project Overseer Wake workflow run `33635102265` completed **SUCCESS** for the same commit.
- Test job executed the repository test suite on GitHub's Node runner and completed successfully.
- Wake verification job completed successfully.
- The verification evidence is repository/CI evidence; it is not evidence that the user's physical local PC has executed the CLI.

## Evidence boundary
**GREEN:** canonical-runner integration, durable local adapter, project/mission/capability/consent envelope, additive budget reservation/reconciliation, response validation and fresh CI verification.

**YELLOW:** physical local-host execution, crash/restart proof on the user's machine, real authorized worker registry execution, independent unattended execution and production-mode authorization.

## Control decisions
- Keep DRY_RUN and `autonomyEnabled=false`.
- Do not introduce providers, credentials, production writes or a second runtime.
- Do not close Issue #64 yet; its physical/local execution acceptance remains open.
- Do not treat GitHub scheduled telemetry as GREEN without observable mailbox evidence.

## Next dependency
The next vertical dependency is the **real authorized worker boundary**: bind the bounded wake to the existing worker registry/capability authority and prove an actual local worker transaction without bypassing consent, scope or budget controls. Path authority must be enforced at the real file/tool execution boundary when that boundary is introduced.

**Source worker:** `agentos:local-wake-worker` (repository-defined deterministic worker identity; not an independently running external process).
