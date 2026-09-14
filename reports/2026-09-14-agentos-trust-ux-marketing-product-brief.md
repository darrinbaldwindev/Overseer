# AgentOS — Trust UX Marketing/Product Brief

**Date:** 14 September 2026  
**Owner:** Marketing Overseer  
**Status:** PRODUCT DIRECTION / EVIDENCE-GATED  
**Canonical mission:** `darrinbaldwindev/Overseer#49`

## Purpose

Translate repeated trust, authority and evidence gaps into a user-facing product/marketing brief. This document does not claim these capabilities are implemented. It defines what users need to understand and what evidence Marketing would need before promoting the corresponding promise.

## Core interaction model

> **Chat for intent. Palette for speed. Inbox for attention. Jobs for repetition. Jack for authority. Isla for execution. Henry for proof.**

This model should reduce the need for users to understand model/tool plumbing while making authority and proof more visible, not less.

## 1. Evidence Timeline

### User need
A normal user should be able to answer:
- What did AgentOS do?
- What did it touch?
- What succeeded or failed?
- What evidence supports the result?
- What remains unverified?

### Product requirement
Provide a chronological, human-readable evidence surface that distinguishes intent, approval, execution, mutation, test/verification, Green state, PRS state, recovery and unresolved blockers.

### Marketing promise only after proof
“See what AgentOS did and what evidence supports the result.”

### Proof gate
User-readable evidence must correlate to exact task/mission/worker/result state and cannot show success before required durable receipts/verification exist.

## 2. Pause / Stop / Revoke

### User need
Users must know the difference between:
- pausing future work;
- stopping an active task;
- revoking authority for future actions;
- cancelling something that cannot be safely rolled back.

### Product requirement
Use precise labels and state transitions. Do not present a single red button whose real semantics vary silently by capability.

### Marketing promise only after proof
“You stay in control of what AgentOS may continue doing.”

### Proof gate
Exact tested semantics for queued, admitted, in-flight and externally committed actions; durable evidence of what stopped and what did not.

## 3. Restricted Mode / Untrusted Content

### User need
Users need a clear way to handle unknown websites, files, prompts or third-party content without silently granting them broad influence over tools/credentials.

### Product requirement
A visible restricted/untrusted mode with constrained capability access and explicit elevation path.

### Marketing promise only after proof
“Treat untrusted content differently from trusted work.”

### Proof gate
Demonstrated policy boundaries, prompt-injection tests, capability denial and no secret/tool escalation through untrusted content.

## 4. Permission explanations

### User need
Users should understand why AgentOS needs a permission, what exact resource it covers, and how long it lasts.

### Product requirement
Plain-language permissions mapped to real enforcement scope. Prefer temporary, task-scoped or capability-scoped authority over vague blanket approval.

### Marketing promise only after proof
“Approve the job, not unlimited access.”

### Proof gate
Enforcement must match the wording; expired/revoked authority must fail closed.

## 5. Connector Centre

### User need
Users should see which connectors/capabilities exist, what they can access, whether they are local/cloud, and which jobs currently depend on them.

### Product requirement
One governed view for connector identity, publisher/source, permissions, scopes, status, last use, trust level and update/version information.

### Marketing promise only after proof
“Know what AgentOS can connect to and what each connection is allowed to do.”

### Proof gate
Connector scope and authority must be canonical and enforced; UI cannot be decorative metadata only.

## 6. Local / Cloud / Mixed indicator

### User need
Users increasingly care where files, prompts and execution go.

### Product requirement
Show whether a job is local-only, cloud-only or mixed, with meaningful details when a boundary matters.

### Marketing promise only after proof
“See where the job is running.”

### Proof gate
Runtime routing evidence must support the displayed state. Do not infer from model branding alone.

## 7. Exact VERIFIED meaning

### User need
“Verified” must not mean “the worker said it finished.”

### Product requirement
Define VERIFIED narrowly and consistently. Candidate model:
- execution produced expected receipt/evidence;
- required verification checks passed;
- exact correlation is intact;
- no unresolved blocking error;
- assurance state is clearly separated from execution result.

### Marketing promise only after proof
“AgentOS can show the difference between completed, verified and independently assured.”

### Proof gate
The UI and canonical state machine must prevent self-asserted execution from being rendered as independent assurance.

## 8. Credentials / Secret Handles

### User need
Users should not have to paste reusable secrets into arbitrary model context.

### Product requirement
Prefer brokered credential handles, narrow scopes, explicit connector ownership and minimal model visibility.

### Marketing promise only after proof
“Use governed connections without exposing reusable secrets to every model/tool.”

### Proof gate
Evidence of secret-handling boundaries across model, tool, logs, receipts and recovery paths.

## 9. Device and connector trust

### User need
A capability on a trusted local device is not equivalent to an unknown remote worker or third-party connector.

### Product requirement
Represent device identity, connector/publisher trust, capability scope and current authority separately.

### Marketing promise only after proof
“AgentOS considers who is acting, where, with which capability and under what authority.”

### Proof gate
Trust signals must feed enforceable policy, not just badges.

## 10. Recovery state

### User need
After a crash/interruption, users need an answer to: “Did it actually happen?”

### Product requirement
Recovery UX must distinguish:
- definitely not executed;
- executed and durably recorded;
- partially executed;
- outcome unknown;
- safe to retry;
- retry could duplicate side effects.

### Marketing promise only after proof
“When something goes wrong, AgentOS is designed to make the recovery state explicit rather than silently guessing.”

### Proof gate
Crash/restart/replay tests plus exact receipts and ownership/idempotency semantics.

## Recommended information hierarchy

### Simple view
- current job;
- what AgentOS is allowed to do;
- current status;
- stop/revoke control;
- result + evidence summary.

### Essentials view
Adds:
- files/resources touched;
- model/capability route;
- cost/time;
- recovery state;
- Green/PRS summary.

### Tech Head view
Adds:
- exact task/mission/worker/result correlation;
- receipts;
- policy/authority decisions;
- connector identity/scopes;
- detailed verification/assurance evidence;
- replay/recovery metadata.

The same canonical truth must underpin all three views.

## Marketing priority order

P0 before broad beta:
1. permission clarity;
2. Evidence Timeline;
3. exact VERIFIED semantics;
4. stop/revoke clarity;
5. recovery state.

P1:
6. Local/Cloud/Mixed;
7. Connector Centre;
8. credentials/secret UX;
9. restricted mode.

P2:
10. richer trust graph/publisher/device reputation and governed capability-store presentation.

## Positioning consequence

AgentOS should not compete primarily on “AI can click/type/run commands.” The stronger proposition is that useful execution is bounded, inspectable and independently checkable.

Working architecture-level line:

> **AgentOS is being built to put governed execution around real AI work.**

Do not convert that architecture statement into guarantees about every current action until the corresponding proof gates pass.

## Status

- Product direction: PREPARED.
- Implementation claim: NOT MADE.
- Public campaign activation: NO.
- Founding Beta activation: HOLD.
- Overall GREEN: NOT CLAIMED.