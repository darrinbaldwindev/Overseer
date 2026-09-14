# AgentOS Founding Beta — Measurement Instrumentation Contract

**Date:** 2026-09-14 Brisbane  
**Owner:** Marketing Overseer  
**Canonical mission:** `darrinbaldwindev/Overseer#49`  
**Status:** PREPARED / ACTIVATION HOLD

## Purpose
Define the minimum evidence needed to learn whether Founding Beta users understand, trust and reuse AgentOS without turning beta telemetry into conversation surveillance.

This contract is downstream of the runtime, authority, Frontend, Green and PRS sources of truth. It does not create a new mission/job/authority/assurance store.

## Privacy rule
Beta measurement should be **opt-in, privacy-minimal and content-blind by default**.

Do not capture:
- raw prompts or conversation bodies;
- file contents;
- secret values or credentials;
- clipboard contents;
- unrestricted command/output bodies;
- personal document text;
- external message contents.

Prefer boolean/enumerated events and pseudonymous beta-session identifiers. Retention, export and deletion controls must be explicitly defined before collection is enabled.

## Core measurement events

| Signal | Minimum event | What it answers | Must not imply |
|---|---|---|---|
| real-job attempt | `job_attempted` + job-class enum | Did tester bring a real job? | job completed |
| permission comprehension | `permission_prompt_shown`, `permission_decision`, optional 1-question comprehension result | Did the tester understand scope/authority? | permission safety proved |
| scope containment | `scope_denied` / `scope_allowed` + reason class | Did the boundary behave visibly as expected? | whole system contained |
| Stop comprehension | `stop_requested`, `stop_state_seen`, post-task question | Did tester understand requested vs effective stop? | immediate termination |
| Revoke comprehension | only after canonical revoke exists: `revoke_requested`, `revoke_effective` | Did tester understand authority withdrawal? | revoke exists today |
| evidence comprehension | `evidence_opened`, `evidence_comprehension_result` | Could tester explain what happened? | independent verification passed |
| failure/recovery | `failure_state_seen`, `recovery_state_seen`, `user_next_action` | Did failure remain understandable/actionable? | safe recovery proved unless canonical runtime says so |
| replay/duplicate | `duplicate_detected_or_denied` from canonical receipt pointer | Was duplicate handling visible? | no duplicate side effects globally |
| assurance comprehension | `green_state_seen`, `prs_state_seen` only from canonical values | Did user understand completion vs assurance? | Green/PRS inferred by frontend |
| second real job | `second_real_job_attempted` within beta observation window | Did user voluntarily return? | retention/product-market fit by itself |

## North-star early signal

**Primary:** `% of testers who attempt a second real job without prompting.`

Required denominator: testers who completed onboarding and attempted at least one genuine job. Exclude forced demo repetitions.

Supporting signals:
- permission-comprehension pass rate;
- evidence-comprehension pass rate;
- percentage who can correctly distinguish `Stop requested` from confirmed stop;
- percentage who can correctly distinguish completion from Green/PRS assurance;
- proportion of failures where tester identifies the correct next action without facilitator correction;
- voluntary second-job latency bucket (`same session`, `<24h`, `1–7d`, `>7d`).

## Event semantics
1. Frontend may emit presentation events only for states actually shown.
2. Runtime outcomes must be referenced by canonical IDs/pointers; telemetry must not manufacture execution truth.
3. Green and PRS events must be copied from canonical independent assurance state, never derived from worker success.
4. `stop_requested` and `stop_effective` are separate events.
5. Unknown/stale state must remain UNKNOWN; analytics must not coerce missing values into false/zero/failed.
6. If local-only operation is selected, measurement must not silently upload protected local content.

## Tester-facing consent requirements
Before Wave 0 measurement:
- tell testers what categories of usage metadata are collected;
- state what is deliberately not collected;
- state purpose: product safety/usability learning;
- provide opt-out without losing core product access where practical;
- define retention period and deletion path;
- identify any cloud processor if telemetry leaves the device.

## Beta dashboard — allowed aggregates
- invited / onboarded / first-real-job / second-real-job counts;
- task-class distribution;
- permission comprehension pass/fail/unknown;
- evidence comprehension pass/fail/unknown;
- Stop-state comprehension pass/fail/unknown;
- failure/recovery usability categories;
- assurance-comprehension categories;
- unresolved blocker counts.

Do not display raw user content in the beta dashboard.

## Activation gate
Instrumentation is **PREPARED, NOT ENABLED** until:
1. Founding Beta technical entry gate clears;
2. Frontend states used by the measurements exist on the tested lineage;
3. canonical IDs/state pointers are available;
4. consent/privacy wording is reviewed;
5. storage/retention/deletion behavior is specified;
6. no telemetry path bypasses Local/Cloud/Mixed disclosure.

## Marketing use
Marketing may use aggregate beta learning only after sample size/context are stated. Do not convert a handful of successful tasks into claims such as “users trust AgentOS” or “AgentOS always recovers safely.”

## Current decision
**PREPARED / DO NOT ACTIVATE / FOUNDING BETA HOLD / NO TELEMETRY COLLECTION AUTHORISED BY THIS DOCUMENT.**