# AgentOS Basic Chat Evidence Timeline — Gap to MVP

Date: 2026-09-14 AEST
Owner: Marketing Overseer
Status: PRODUCT/CLAIM CONTRACT / NOT IMPLEMENTATION AUTHORITY

## Purpose
Define the smallest truthful Evidence Timeline that can be presented from current canonical Basic Chat evidence without inventing runtime state, recovery, PRS or authority semantics.

## Current exact frontend evidence
PR #111 current descendant has a bounded read-only projection keyed to the canonical dispatch task identity. Current evidence can support:
- task identity;
- mission correlation;
- wake correlation;
- bounded completion status;
- Green disposition;
- completion timestamp when canonically present;
- blocker count when canonically present.

The projection fails closed where task/mission/wake identity conflicts or canonical dispatch identity is absent. It does not treat `lastTaskId` as a generic run ID.

## Smallest truthful MVP timeline
A first Evidence Timeline may contain only evidence-backed stages such as:
1. **Job started** — only when canonical task evidence exists.
2. **Job identity** — task/mission/wake identifiers, progressively disclosed.
3. **Work result recorded** — only from the task-correlated canonical response/event projection.
4. **Completion check** — show exact completion state, not a generic success badge.
5. **Green check** — show exact Green disposition separately.
6. **Finished at** — only when a canonical completion timestamp exists.
7. **Needs attention** — when canonical blocker evidence exists.

Simple mode may collapse these into human language; Essentials may show stage + explanation; Tech Head may reveal canonical identifiers. The truth must remain identical across modes.

## Required fail-closed states
When evidence is absent or conflicting, use states such as:
- `Unable to confirm what happened`
- `Evidence unavailable`
- `Evidence conflicts — needs attention`
- `Completion not confirmed`
- `Green check not available`

Do not substitute optimistic UI state for missing evidence.

## Explicitly absent from current Basic Chat evidence
The current projection does not provide sufficient canonical data for:
- Henry / PRS result;
- recovery attempt/state/timeline;
- rollback result;
- durable authority revoke receipt/effect;
- confirmation that in-flight execution stopped;
- capability/publisher identity history;
- exact cost incurred/budget reconciliation timeline;
- generic multi-run Evidence Timeline;
- physical Windows Level 2 readiness;
- project-file mutation proof.

These must not appear as completed timeline stages until canonical sources exist.

## Completion/assurance language
Permitted narrow language when exact canonical evidence supports it:
- `Passed for this job` only where completion is COMPLETED and Green disposition is PASS on the same canonical task.
- `Henry/PRS: Not shown in Basic Chat` while no PRS field is available.

Do not use `VERIFIED` as an umbrella synonym for worker success, completion, Green or PRS.

## Stop/revoke boundary
A timeline may record `Stop requested` if that canonical request state exists. It must not record `Execution stopped` without canonical confirmation of effective termination. There is no current durable Revoke source in Basic Chat, so no Revoke event should be synthesized.

## Physical/local boundary
The timeline must preserve the current Basic Chat scope: local DRY_RUN/test path is not evidence of physical Windows worker readiness. The current frontend explicitly states physical Windows readiness is not established.

## Acceptance tests before calling the timeline MVP
1. Wrong-task evidence cannot appear.
2. Mission/wake conflicts fail closed.
3. Missing canonical dispatch identity fails closed.
4. Green cannot be inferred from worker success.
5. PRS cannot be inferred from Green.
6. Recovery cannot be inferred from a later success.
7. Stop requested cannot render as stopped.
8. Raw prompts, secrets, credentials and unrestricted worker output are excluded by default.
9. Simple/Essentials/Tech Head differ only in depth, never truth.
10. No physical-readiness implication from Basic Chat local evidence.

## Marketing disposition
The wired bounded projection is enough to support a useful **What happened** panel and the first narrow Evidence Timeline MVP. It is not enough to support a claim that AgentOS has a complete end-to-end evidence timeline, independent assurance display, recovery history or Windows Level 2 proof.
