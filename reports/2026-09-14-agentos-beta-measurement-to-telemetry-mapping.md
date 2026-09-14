# AgentOS Founding Beta — Measurement-to-Telemetry Mapping

**Date:** 2026-09-14 AEST  
**Lane:** Marketing → Frontend/Product evidence  
**Status:** PREPARED / DO NOT ENABLE TELEMETRY

## Purpose
Map the Founding Beta measurement contract onto AgentOS's existing telemetry/privacy primitives without creating a second telemetry, authority, identity or analytics source of truth.

## Existing canonical primitives reviewed
Current AgentOS telemetry code already provides:
- consent levels: `none`, `performance`, `improvement`;
- telemetry OFF by default (`none`);
- transmission gating through `shouldTransmit(...)`;
- sanitisation to a fixed field set;
- exclusion of arbitrary input fields such as prompt/conversation content in current tests.

Current sanitised schema fields are limited to:
`schemaVersion`, `taskCategory`, `workerType`, `workerId`, `quality`, `confidence`, `cost`, `latencyMs`, `tokens`, `success`, `retries`.

## Marketing/Beta interpretation
This foundation is directionally compatible with privacy-minimal beta measurement, but it does **not yet prove** that all desired Founding Beta trust metrics can be captured safely or accurately.

Do not create a parallel analytics database or frontend-owned telemetry state.

## Required beta measures and canonical-source rule

| Beta measure | Desired signal | Existing telemetry fit | Required source of truth | Current disposition |
|---|---|---|---|---|
| real task attempted | user attempted a real job | partial via task category/success | canonical mission/task state | MAP ONLY |
| permission comprehension | tester understood requested authority before action | not represented | explicit beta UX response / research instrument | ADD ONLY WITH CONSENT |
| Stop comprehension | user understands Stop requested vs effective | not represented | canonical control state + explicit tester response | ADD ONLY WITH CONSENT |
| Revoke comprehension | user understands authority revocation semantics | canonical Revoke not yet exposed in Basic Chat | canonical authority state + tester response | BLOCKED |
| evidence comprehension | user can explain what happened | not represented | Evidence UI state + tester response | ADD ONLY WITH CONSENT |
| safe failure/recovery | job fails/restarts without false success | partial success/retries insufficient | canonical mission/recovery/evidence events | BLOCKED UNTIL RUNTIME TRUTH IS PROJECTED |
| duplicate/replay protection | repeated action did not create duplicate side effect | not represented safely by existing schema | canonical mission/replay evidence | BLOCKED |
| independent second real job | tester voluntarily uses AgentOS again | can be derived only from pseudonymous/session-safe event correlation | canonical beta session identity with privacy review | DESIGN REQUIRED |

## Privacy contract
Founding Beta instrumentation should remain:
- opt-in;
- OFF by default;
- event/metric oriented rather than content oriented;
- no raw prompt;
- no raw conversation;
- no file contents;
- no credentials/secrets/tokens;
- no arbitrary environment dumps;
- no hidden device fingerprinting;
- no marketing profiling beyond the beta research purpose;
- deletion/retention period explicitly declared before activation.

## Minimal proposed event vocabulary
These are **product requirements**, not new runtime authority:
- `beta.task_attempted`
- `beta.permission_comprehension_recorded`
- `beta.stop_comprehension_recorded`
- `beta.evidence_comprehension_recorded`
- `beta.safe_failure_observed`
- `beta.recovery_observed`
- `beta.second_real_job_attempted`

Each event must reference opaque canonical IDs only where privacy review permits, and must never carry prompt/file/message content.

## Important boundary
A beta analytics event must never create or override:
- mission state;
- authority state;
- Stop/Revoke state;
- Green;
- PRS;
- verification status;
- completion.

Analytics observes canonical state; it does not certify it.

## Activation gate
Do not enable beta telemetry until:
1. technical Founding Beta entry gate clears;
2. event schema is reconciled against canonical runtime fields;
3. Frontend shows clear consent and telemetry state;
4. privacy/retention/deletion text is approved;
5. tests prove prompt/conversation/file/secret exclusion for every new event field;
6. telemetry OFF remains the fresh-install default;
7. no event can promote a runtime or assurance state.

## Current conclusion
**PREPARED / NOT ACTIVATED.** Existing AgentOS telemetry is a useful privacy-conscious base. The correct next step is to extend it only where canonical state and beta research require it, not to build a new analytics subsystem.
