# AgentOS Basic Chat Evidence Timeline — Acceptance Matrix

**Date:** 2026-09-15 AEST  
**Role:** Marketing Overseer  
**Canonical mission:** `darrinbaldwindev/Overseer#49`

## Objective

Convert the current bounded Basic Chat evidence projection into explicit user-facing acceptance criteria without inventing a second evidence store, authority system, assurance layer, recovery system or runtime source of truth.

## Core rule

Every displayed state must come from existing canonical evidence. Missing, stale, mismatched or contradictory evidence must fail closed.

## Minimum accepted timeline rows

| User-facing row | Canonical requirement | Simple | Essentials | Tech Head | Fail-closed state |
|---|---|---|---|---|---|
| Job identified | canonical `dispatch.task` identity | optional plain-language job reference | task/job identity | exact task ID | `Evidence unavailable` |
| Mission correlation | canonical matching mission ID | hidden unless useful | short mission reference | exact mission ID | do not infer |
| Wake/execution correlation | canonical matching wake trace | hidden | optional | exact wake trace | do not infer |
| Completion state | matching canonical completion evidence | `Completed` only when exact evidence supports it | status + timestamp | status + evidence pointer | `Completion not confirmed` |
| Green disposition | matching canonical Green evidence | `Passed for this job` only for exact pass | explicit Green status | exact Green disposition/pointer | `Verification pending/unavailable` |
| Completion timestamp | canonical completion timestamp | optional | visible | exact timestamp | omit |
| Blocker count | canonical blocker evidence | plain-language blocker notice | count + summary | count + pointer | unknown, never zero by assumption |

## States that MUST NOT be synthesized

The current Basic Chat timeline must not fabricate or infer:
- Henry/PRS outcome;
- successful recovery or rollback;
- durable permission revocation;
- confirmed in-flight termination;
- cost charged or avoided;
- physical Windows acceptance;
- project-file mutation readiness;
- generic run identity from `lastTaskId`;
- success from absence of errors.

## Screen-mode requirements

### Simple
- Large central chat remains primary.
- Evidence summary uses ordinary language.
- Technical IDs hidden by default.
- Never compress worker completion + Green + PRS into one `Verified` badge.

### Essentials
- Show completion and Green as separate lines.
- Show blocker state and time where available.
- Provide a `What happened` disclosure without raw prompts, secrets, credentials or arbitrary worker output.

### Tech Head
- May expose task ID, mission ID, wake trace, canonical source type and exact timestamps.
- Must still preserve the same semantic boundaries as Simple/Essentials.
- More detail must never weaken fail-closed behavior.

## Negative acceptance tests

A timeline must remain non-promotable if any of these fail:
1. no canonical `dispatch.task` but response/event appears to match;
2. task, response and event disagree on mission ID;
3. task, response and event disagree on wake trace;
4. Green artifact identity does not match current task;
5. arbitrary/non-canonical event claims completion;
6. secret/raw prompt/private metadata is present in projected user evidence;
7. PRS/recovery/revoke fields appear without canonical sources;
8. local/DRY_RUN state is presented as physical Windows readiness;
9. physical Windows acceptance is presented as project-file mutation readiness.

## Promotion rule

Marketing may call this an **Evidence Timeline MVP** only after the frontend presents the accepted rows from canonical evidence with the negative cases above covered on an exact CI-green head.

Until then, use **bounded `What happened` evidence summary**.
