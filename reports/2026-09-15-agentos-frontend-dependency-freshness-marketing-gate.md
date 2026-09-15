# AgentOS — Frontend Dependency-Freshness Marketing Gate

**Date:** 2026-09-15 AEST  
**Task:** M-A043  
**Status:** COMPLETE / CLAIM + HANDOFF CONTRACT

## Why this exists
User-facing trust collapses if a current frontend screen presents a readiness, authority, physical-acceptance or assurance statement derived from a stale runtime head or stale evidence source.

Current positive movement: Frontend PR #111 exact `3efea32bec11725b5b1d221190f0424fc5eb57dc` now explicitly adds host identity/freshness and expected exact-head correlation rules. Exact-head Tests `34914794812` are SUCCESS. The PR also refreshes #104 to exact `4c8bcc3...` and correctly records the SG-08 false-success blocker.

## Marketing acceptance rule
A user-facing positive state must be bound to the evidence identity it claims to describe. At minimum, where materially applicable:
- exact runtime/implementation head;
- host/device identity;
- evidence freshness/age;
- task/mission/wake identity;
- source schema/version;
- assurance identity/lineage;
- explicit scope of what passed.

Missing, malformed, stale, mismatched or contradictory evidence fails closed.

## Required wording behavior
### Fresh + exact positive evidence
May use bounded positive wording such as `Physical Windows acceptance passed for this exact tested head` only when canonical evidence proves that exact scope.

### Stale evidence
Use `Evidence is stale` / `Current state cannot be confirmed` rather than carrying forward a prior PASS.

### Head mismatch
Use `Acceptance was recorded for a different version` rather than `Ready`.

### Host mismatch
Use `Evidence belongs to a different device/host` and block positive current-host presentation.

### Missing canonical source
Use `Not established` / `Unknown` rather than inference from nearby facts.

## Cross-source non-inference
Do not infer:
- mutation readiness from Basic Chat availability;
- physical acceptance from Windows capability;
- Green from CI;
- PRS/Henry from Green;
- durable revoke from Stop UI;
- current readiness from predecessor physical acceptance;
- current runtime truth from stale PR-body prose.

## Frontend handoff
Frontend may implement richer freshness UX, but Marketing requires the semantic invariant:

`positive claim = exact evidence identity + valid freshness + valid correlation + bounded scope`

The frontend must not create persistence merely to make evidence look current. Composition must remain read-only from canonical sources.

## Campaign / screenshot rule
Marketing and Content360 must treat screenshots/demos as evidence-bearing assets. If the screen was captured on a historical head, do not caption it as proof of current readiness unless revalidated on current exact lineage.

## Current classification
PR #111: **IMPLEMENTATION-ADVANCED / EXACT-HEAD CI PASS / FRESHNESS+HEAD-CORRELATION HARDENED / DRAFT-UNMERGED / NOT SHIPPED.**

Project-file mutation remains BLOCKED because #104 exact-head SG-08 false-success is reproducible. No frontend success may upgrade that state.