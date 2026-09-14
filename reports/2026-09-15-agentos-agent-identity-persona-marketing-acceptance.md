# AgentOS Agent Identity / Persona Marketing Acceptance

**Marketing task:** M-A036  
**Date:** 2026-09-15 AEST  
**Status:** OWNER-APPROVED PRODUCT DIRECTION / IMPLEMENTATION NOT YET CLAIMED

## Owner decision
AgentOS has 17 specialist agents. The user always interacts through the **Overseer**. Specialist agents operate behind that single relationship.

Each specialist should have:
- a stable machine identity (for example Agent 1…Agent 17);
- a controlled role/capability contract;
- a replaceable user-facing name;
- a replaceable appearance/avatar;
- potentially replaceable voice/personality where implemented.

Core principle:
> **Identity is stable. Role is controlled. Persona is replaceable.**

## Architecture/marketing boundary
Changing name, face, voice or personality must never change:
- role/capability contract;
- authority or permissions;
- task/mission/evidence identity;
- Green or PRS semantics;
- routing/runtime identity;
- governance or assurance;
- ability to bypass the Overseer.

Recommended conceptual naming pattern: `agent_01.planner`, `agent_02.executor`, `agent_03.guardian`, `agent_04.assurer`, with exact runtime identifiers owned by the AgentOS implementation.

## Default personas
Willow, Isla, Jack and Henry should be treated as default brand/persona presentations rather than canonical machine identities. Organisations or individuals may eventually choose alternatives such as `Planner`, `Security`, `Verifier`, or personal names without changing the role.

## Evidence/display acceptance
When customisation exists, evidence should remain attributable to stable identity + role. A user-facing display may show a custom name and role; Tech Head may additionally expose stable system ID. Historical evidence must not become ambiguous after a rename.

## Single-front-door rule
Marketing and Content360 must portray the user relationship as:

`User → Overseer → specialist agents/capabilities → Overseer → User`

Renaming a specialist must never imply direct authority-bearing chat with that specialist.

## Safe campaign language — product direction until implemented
- `Make the team yours.`
- `Roles stay consistent while names, faces and voices can be personalised.`
- `One Overseer. A specialist team behind it.`

Do not claim this is currently configurable until repo evidence proves preference storage, rendering, stable-ID preservation and migration behavior.

## Implementation evidence required before promotion
1. canonical stable agent-ID registry/source;
2. canonical role mapping;
3. persona preference storage and scope (user/family/org);
4. rename/avatar/voice persistence;
5. evidence/log rendering across renames;
6. defaults and migration behavior;
7. permissions/authority invariant tests;
8. no direct-agent Overseer bypass;
9. accessibility and fallback presentation.

**Decision:** the 17 agents should be marketed as a coherent specialist team. Persona is personalization; role and identity remain governed system facts.