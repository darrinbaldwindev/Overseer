# AgentOS Voice Conversation — Marketing Claim Gate

**Marketing task:** M-A037  
**Date:** 2026-09-15 AEST  
**Status:** OWNER-APPROVED PRODUCT DIRECTION / NOT SHIPPED

## Product direction
AgentOS should eventually support natural verbal conversation. The user still speaks to the **Overseer**, not directly to specialist agents.

Canonical interaction principle:

`User speaks → Overseer interprets intent → canonical authority/governance → specialist work → evidence/assurance → Overseer responds`

Voice is an input/output modality. It must not become a second, weaker control plane.

## Governance requirements
Voice must preserve the same boundaries as typed interaction:
- identity/session binding;
- authority and permission checks;
- explicit confirmation where required;
- Jack/governance boundaries;
- task/mission correlation;
- duplicate/replay protection;
- Green/PRS separation;
- durable evidence;
- truthful Stop/Pause/Revoke semantics;
- fail-closed handling when speech is ambiguous.

A spoken `yes` must not grant broader authority than the equivalent explicit typed approval contract.

## Consequential actions
For sending messages, purchases, file mutation, credential use, external communication or other consequential work, voice must not weaken the existing approval boundary. The Overseer should be able to restate material scope before accepting confirmation when required.

## Evidence requirement
Even when the conversation is verbal, important action/evidence state should remain available visually/durably. Voice output must not be the only record of what happened.

## Accessibility and demographic value
Voice can materially improve accessibility and lower the prompting barrier for novice, busy and mobility/vision-constrained users. Marketing must not equate age with inability or imply medical/accessibility outcomes that are not proven.

## Required implementation evidence before availability claims
1. speech-to-text path and supported platforms;
2. text-to-speech path and supported platforms;
3. microphone permission/privacy/mute behavior;
4. user/session identity binding;
5. interruption and turn-taking behavior;
6. ambiguous-speech fail-closed behavior;
7. authority/approval binding for spoken confirmations;
8. replay/deduplication behavior;
9. error/status presentation;
10. durable transcript/evidence privacy contract;
11. accessibility acceptance;
12. end-to-end tests proving voice cannot bypass the Overseer/governance path.

## Allowed now
Marketing may discuss voice as **future/product direction**, for example:
- `AgentOS is being designed so natural conversation can become another way to work through the Overseer.`
- `The goal is to let people talk naturally without creating a separate authority path.`

## Not supportable now
Do not publish claims such as:
- `Talk to AgentOS today`;
- `hands-free computer control`;
- `voice control for Windows`;
- `speak and AgentOS safely does it`;
- `voice approvals are secure`;
- supported-device/language claims without exact evidence.

## Future multimodal direction
Voice should ultimately coexist with typing, files, screen context and other modalities while preserving one Overseer conversation and one governance/evidence lifecycle.

**Decision:** verbal conversation is strategically important for mass adoption, but remains PRODUCT DIRECTION until implementation and exact evidence justify availability claims.