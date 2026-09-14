# AgentOS Jack Permission Card — Canonical Field Gap

Date: 2026-09-14 AEST
Owner: Marketing Overseer
Status: PRODUCT REQUIREMENT / NO AUTHORITY CHANGE

## Goal
Translate the currently evidenced authority data into the minimum user-facing Jack permission-card contract without inventing a second authority source.

## Canonical fields already evidenced on the active governed Windows-worker lineage
Current authority/admission evidence can already support presentation of:
- authenticated actor identity/provenance as supplied by the canonical admission path;
- issuer/project provenance;
- requested capabilities;
- granted capabilities;
- authority evidence ID;
- mission/task/delivery/request correlation;
- host target;
- scope / constraints / objective;
- admission timestamp.

These fields are useful, but not sufficient for a complete ordinary-user permission decision.

## Missing canonical user-facing fields
A trustworthy Jack card still needs canonical support for:
1. **Lifetime / expiry** — when authority ends and whether it expires automatically.
2. **Revocation semantics** — what can be revoked, by whom, and the durable receipt proving revocation.
3. **Already-running-work behavior** — whether revocation blocks only new work or can terminate in-flight work.
4. **Reversibility** — whether the requested action can be undone and what rollback guarantees actually exist.
5. **Credential consequence** — whether credentials/secrets are needed, which opaque handles are used, and what the model/tool can actually see.
6. **External communication** — whether the action sends email/messages, publishes, contacts a third party or transmits data outside the device/workspace.
7. **Data disclosure** — what files/records/content may leave the local boundary and to what destination class.
8. **Money/cost consequence** — whether the action can incur spend, consume paid API budget or create a purchase/financial commitment.
9. **Capacity/rate consequence** — material quota/rate-limit/budget effects where relevant.
10. **Next approval boundary** — whether this approval covers one action, this task, this path/resource, a time window, or future repeated actions.
11. **Mutation boundary** — exactly which files/resources/accounts may change.
12. **Assurance expectation** — what evidence/Green/PRS checks will be required before completion can be claimed.

## Minimum card structure
### What AgentOS wants to do
Plain-language action + exact capability.

### Where
Canonical resource/path/account/host scope.

### Why
Task objective and reason this authority is needed.

### How long / how much
Lifetime/expiry and cost/budget consequence when canonically available. If unavailable: `Not established` rather than an invented duration/cost.

### What could happen
Irreversibility, external communication, data disclosure, credential use and other meaningful consequences.

### Your control
One-time/task/path/persistent scope only when the canonical authority model supports that exact option. Revoke/Stop controls appear only when their semantics and receipts exist.

### What AgentOS will check
Evidence + Green + PRS expectations stated separately; no assurance result is implied before it exists.

## Fail-closed UX rules
- Unknown lifetime -> `Expiry not established`; never imply session-only.
- Unknown revoke effect -> do not claim `Permission revoked`.
- Unknown reversibility -> `Reversibility not established`; never imply undo is guaranteed.
- Missing secret isolation proof -> do not say credentials are hidden from every model/tool.
- Missing egress proof -> do not say `stays on your computer`.
- Missing cost evidence -> distinguish estimate, ceiling, incurred cost and unknown.
- Current action may continue after Stop/revoke request unless canonical runtime proves otherwise.

## Simple / Essentials / Tech Head
All modes use the same canonical permission record.
- Simple: action, place, risk/consequence, scope, Allow/Deny when supported.
- Essentials: add duration, cost, data/external-action and next approval boundary.
- Tech Head: add IDs, exact capability, authority evidence, constraints and assurance pointers.

No mode may expose a stronger authority claim than another.

## Marketing disposition
Jack can already be positioned as the intended guardian/authority surface, but Marketing must not claim a complete permission-card experience or durable revocation contract until the missing fields are canonically produced and the Frontend presents them fail-closed.

## Engineering handoff principle
Extend the existing canonical authority/admission/receipt systems only. Do not create a frontend-only permission registry, synthetic expiry model or parallel revoke state.
