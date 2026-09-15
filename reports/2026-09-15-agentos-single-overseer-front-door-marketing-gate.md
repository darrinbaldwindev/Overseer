# AgentOS — Single Overseer Front-Door Marketing Gate

**Date:** 2026-09-15 AEST  
**Marketing task:** M-A039  
**Status:** COMPLETE / PRODUCT-MARKETING HANDOFF GATE

## Product rule
The user-facing relationship is with the **Overseer**. Specialist agents/capabilities may be coordinated behind it. Presentation persona must never become a new authority identity or a bypass around canonical governance.

Conceptual path:

`user intent → Overseer → canonical authority/routing → specialist capability/agent → canonical evidence/assurance → Overseer → user`

This is a product/marketing contract, not a claim that every runtime seam is already shipped.

## Marketing acceptance
A surface passes this gate only when it:
- presents the Overseer as the primary conversational relationship;
- describes specialists as roles/capabilities behind that relationship;
- keeps permission/authority decisions tied to canonical evidence, not persona preference;
- keeps Jack/guardian state separate from worker completion;
- keeps Henry/PRS separate from Green and worker success;
- keeps `Stop requested` distinct from confirmed termination;
- keeps readiness states separate;
- does not create a second scheduler, queue, registry, authority source, ledger, memory, Green or PRS through UI language.

## Disallowed patterns
- `Message Isla directly to bypass the Overseer.`
- `Switch to Jack to grant permanent access.`
- `Henry says it is verified` without canonical PRS evidence.
- Persona-specific permission stores.
- Persona rename causing a new security identity.
- Voice mode bypassing the same approval/evidence lifecycle.
- A specialist claiming its own completion is independent assurance.

## Persona customisation
Allowed product direction:
- display name;
- avatar/appearance;
- tone/personality;
- voice where implemented.

Must remain invariant:
- stable system identity;
- role/capability contract;
- authority and permission source;
- task/mission/evidence correlation;
- audit provenance;
- Green/PRS semantics.

## Frontend handoff
Frontend owns the interaction design. Marketing requires the user to be able to understand:
1. `Who am I talking to?`
2. `Which specialist is helping, if relevant?`
3. `What is it allowed to do?`
4. `What actually happened?`
5. `What remains unverified or blocked?`

Simple mode may hide specialist detail by default. Essentials may reveal role-level detail. Tech Head may expose canonical identifiers/provenance where supported. All three preserve the same authority truth.

## Content360 handoff
Content360 may produce persona-led creative such as `Meet Jack` or `Isla can help execute`, but every asset must preserve the single-front-door model. Character-led creative is explanatory branding, not a direct authority channel.

## Negative campaign tests
Reject an asset if a reasonable user could infer that:
- the mascot is the permission system;
- choosing a different persona changes what AgentOS is authorised to do;
- a specialist can bypass the Overseer;
- a worker can self-certify Green/PRS;
- voice has weaker permission requirements than text;
- a specialist count is equivalent to 17 simultaneous autonomous workers.

## Promotion gate
Do not promote `single governed front door` from product contract to fully PROVEN runtime behavior until end-to-end implementation evidence demonstrates the same canonical authority/evidence path across supported interaction modalities.

## Marketing classification
**PRODUCT CONTRACT / CLAIM GATE.** Safe for design and campaign preparation; runtime completeness remains evidence-gated.