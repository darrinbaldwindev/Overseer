# AgentOS Frontend — Evidence Projection Claim Delta

**Date:** 2026-09-14 Brisbane
**Owner:** Marketing Overseer
**Status:** CURRENT-HEAD RECONCILIATION / NO SHIPPED CLAIM

## Current exact evidence
Frontend PR #111 advanced to exact head `b14c5d81f1295ba434d6a6fd9bf5e38e4aa8ffae` and exact-head AgentOS Tests #1095 / `34827244536` completed SUCCESS.

The current frontend lineage adds a bounded presentation-only evidence projection in `runtime/basic-chat-evidence-projection.mjs`.

The projection:
- accepts canonical artifacts/events supplied by the caller;
- does not read or mutate persistence itself;
- can project task ID, mission ID, wake trace ID, completion status, Green disposition, completion timestamp and blocker count;
- chooses from existing response/Green artifacts and task-correlated events;
- remains a view over existing canonical evidence rather than a new evidence store.

## What Marketing/Frontend may now say
Safe current-scope language:
- `Basic Chat can show a bounded summary of evidence already recorded for the current task.`
- `The current frontend can surface task completion state, Green disposition and selected correlation identifiers when those canonical records exist.`
- `The evidence view is presentation-only and does not create or alter runtime/assurance state.`

## What must remain separate
### Completion
A runtime/task completion status is not automatically independent assurance.

### Green
Green disposition is an independent verification signal at its defined scope, not a synonym for task completion, PRS, publication authority or overall AgentOS readiness.

### PRS / Henry
Current Basic Chat evidence projection contains no canonical PRS/Henry result field. Do not display or claim Henry/PRS PASS from task completion or Green.

### Stop
Current Basic Chat Stop remains a request that prevents new work; it is not proven immediate in-flight termination.

### Revoke
No durable canonical authority-revoke projection exists in this slice. Do not synthesize `Permission revoked` or `No further actions authorised` from UI state alone.

## What this does NOT yet constitute
Do not call this a complete generic `Evidence Timeline` yet. Missing or unproven fields include:
- exact authority grant summary and expiry/lifetime;
- requested vs granted permission diff;
- durable revoke state;
- execution step chronology across arbitrary workers;
- files/resources changed with canonical before/after evidence;
- model/provider/capability/version provenance at each step;
- cost/budget reconciliation suitable for ordinary-user explanation;
- recovery/replay/idempotency history in one canonical projection;
- PRS/Henry result;
- independent assurance chain summary;
- user-readable source/evidence links for all claims.

## Mode guidance
### Simple
Show only:
- current result state;
- whether evidence is available;
- plain-language `Checked`/`Needs attention` style presentation only when mapped to exact canonical states;
- one expandable `What happened` surface.

Do not expose raw IDs by default.

### Essentials
May add:
- task/mission correlation;
- completion state;
- Green disposition with explanation;
- blocker count;
- completion time.

### Tech Head
May expose the exact IDs/records that the projection already proves, while clearly labeling source and scope.

All modes must represent the same canonical truth.

## Claim classification
**PROVEN at current draft scope:** bounded Basic Chat projection from supplied canonical records; exact-head tests pass.

**NEARLY PROVEN / incomplete:** useful user-readable evidence summary across broader Level 2 missions.

**PRODUCT DIRECTION:** generic Evidence Timeline spanning authority, execution, recovery, Green and PRS.

**NOT YET SUPPORTABLE:** `AgentOS always proves exactly what happened end-to-end` or `every result is independently assured`.

## Marketing consequence
This is a meaningful usability/trust improvement and should be retained as a product proof point once merged/shipped, but it does not change Founding Beta HOLD or Level 2 readiness.