# AgentOS — Trust Objection + Frontend Handoff Matrix

**Date:** 2026-09-14 Brisbane  
**Owner lane:** Marketing Overseer  
**Consumer lane:** AgentOS Frontend Overseer  
**Canonical coordination:** `darrinbaldwindev/Overseer#49`

## Purpose
Keep public/product language aligned with what the AgentOS frontend can truthfully show. This is a marketing/product-language contract, not runtime authority or frontend implementation evidence.

## Fresh evidence boundary
- AgentOS `main` observed at `6e94e00fc5d81f9de9fc03ff6efc929a2a7ddcc1`.
- Frontend Overseer is now ACTIVE and durably acknowledged in Overseer #49.
- Frontend PR #110 is OPEN/DRAFT and documentation/product-contract only; its reviewed head was `47ed12dc8b0ad210bb37e752c2a4a48adc12600b`.
- Frontend PR #111 is OPEN/DRAFT on the Basic Chat Windows-repair lineage. During this Marketing cycle a review-found test assertion defect was independently confirmed and repaired on that branch in commit `08267446471bda9c0d0c422975762994f2ae3ba2`; fresh exact-head CI was queued, so no PASS is claimed here.
- AgentOS PR #104 remains OPEN/DRAFT/UNMERGED and Level 2 remains gated. Current frontend work must not imply that draft Windows-worker capability is shipped.

## Responsibility boundary
Marketing owns the promise and claim discipline. Frontend owns how the user sees and interacts with that promise. Runtime/authority/Green/PRS remain canonical elsewhere. Marketing should not create competing frontend specifications where the Frontend Overseer now owns the interaction surface; instead it supplies objection, comprehension and claim requirements.

## Trust objection matrix

| User question | Safe current answer | UI evidence needed | Forbidden shortcut |
|---|---|---|---|
| What can AgentOS access? | AgentOS is being built around explicit, bounded authority. The UI should show the scope actually granted for the current job. | Human-readable permission/scope summary; technical detail on demand. | “AgentOS only accesses what you want” unless runtime can prove that exact statement across all capabilities. |
| How do I know what it changed? | For governed work, AgentOS should expose durable evidence of actions and results; the current product is still building the complete user-facing evidence experience. | Evidence Timeline sourced from canonical receipts/events; files/actions/results separated. | A frontend-only activity log presented as canonical proof. |
| Can I stop it? | Stop can prevent new work according to the proven runtime boundary, but an action already in progress may finish. | Requested → acknowledged → effective stop state; unknown/failure state if effectiveness cannot be confirmed. | “Stop immediately” or showing STOPPED merely because the button was pressed. |
| Can I pause it? | Pause should mean no new actions begin once the canonical pause boundary is effective; do not imply the current action is frozen unless proven. | Requested/acknowledged/effective distinction. | Treating UI state as execution state. |
| What happens after a crash? | Recovery is an explicit AgentOS design goal, but complete safe recovery is not yet a public guarantee. | Recovery-required, recovering, recovered, unresolved states backed by canonical evidence. | “Automatically recovers from crashes” as a current universal claim. |
| Can AI see my passwords or secrets? | AgentOS is being designed to minimise unnecessary secret exposure and govern capability access; universal credential isolation is not yet a supportable claim. | Secret/credential boundary, broker/handle state where implemented, connector scope. | “Your passwords are never visible to AI” without exact proof. |
| Who checks the result? | Execution evidence and independent assurance are distinct. Green verifies completion evidence; PRS/Henry provides an independent adversarial assurance role where applicable. | Separate execution, verification, Green and Henry/PRS states. | A single generic VERIFIED badge that collapses these layers. |
| What if the model is wrong? | AgentOS is designed so model output alone does not determine governed completion. Evidence and assurance gates are intended to reduce false-success risk. | Model output visually separated from evidence and assurance. | “AgentOS prevents AI mistakes.” |
| Is my work local or in the cloud? | This depends on the selected model/capability/job. The UI should state Local, Cloud or Mixed from canonical routing/execution evidence. | Local / Cloud / Mixed indicator with detail. | Inferring “local” from the desktop app itself. |
| How much will this cost? | AgentOS aims to coordinate free, local and paid capability choices and make cost understandable; exact cost controls must reflect real provider/runtime evidence. | Estimate vs incurred cost clearly distinguished. | Presenting estimates as final charges or claiming cheapest routing universally. |
| Why was my job blocked? | A block is preferable to silently exceeding authority or claiming success without proof. | Plain-language reason, owner action if any, technical detail expandable. | Generic “Something went wrong” when a canonical denial reason exists. |
| Why isn't this marked complete? | Completion must remain separate from worker success when verification/Green/PRS evidence is still pending or failed. | Work finished / checking / Green / PRS states separated. | COMPLETE because a worker returned success. |

## Marketing-to-Frontend acceptance requirements
1. Simple, Essentials and Tech Head must share the same underlying truth; modes change detail, not facts.
2. `UNKNOWN`, stale or missing canonical state fails closed to neutral/attention wording, never success wording.
3. `Stop requested` is not `Stopped`.
4. Worker success is not automatically `Complete`.
5. Green and PRS/Henry must not be collapsed into decorative trust icons.
6. Local/Cloud/Mixed must come from execution/routing evidence, not branding.
7. Permission copy must say what is granted, for what scope and, when known, for how long.
8. Evidence Timeline must be a projection of canonical evidence, not a frontend-owned ledger.
9. Ordinary-user language should lead; technical state can remain available progressively.
10. Any marketing promise that cannot be represented truthfully in the current UI remains acquisition copy HOLD.

## Frontend Overseer handoff
The Frontend Overseer should consume this matrix as input to its own vertical batch. It remains free to improve interaction design, but any proposed stronger wording should be returned to Marketing with the exact runtime/evidence gate that supports it.

High-value frontend surfaces for this matrix:
- first-run permission explanation;
- current-job header/status;
- Evidence Timeline;
- Pause/Stop/Revoke control states;
- completion/Green/Henry assurance presentation;
- Local/Cloud/Mixed indicator;
- cost estimate/incurred display;
- failure/recovery/blocked explanation;
- Restricted Mode and connector trust.

## Current status
**MARKETING CONTRACT: PREPARED**  
**FRONTEND IMPLEMENTATION: OWNED BY FRONTEND OVERSEER / DRAFT LINEAGE**  
**FOUNDING BETA: HOLD**  
**NO OVERALL GREEN**
