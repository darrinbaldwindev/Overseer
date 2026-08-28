# Internal Sub-Worker Runtime Plan

Date: 2026-08-28
Status: TARGET / RUNTIME GAP IDENTIFIED

## Objective
Move from six documented worker roles to genuinely dispatchable workers without pretending that hidden continuously-running model instances already exist.

## Worker roles
REPO-CODE, QA-TEST, RESEARCH, ARCHITECTURE, SKILLS, SECURITY-HEALTH.

## Runtime contract
1. Overseer creates/claims a task.
2. Capability router selects a worker role.
3. An available execution provider is selected independently of the role.
4. Worker receives task and canonical context.
5. Worker executes within authority boundaries.
6. Worker writes checkpoint/evidence to the canonical control plane.
7. Project Overseer verifies the evidence.
8. GPTChat Overseer performs parent verification where required.
9. Worker returns to READY state.

## State model
READY -> ASSIGNED -> EXECUTING -> CHECKPOINTED -> VERIFIED/FAILED/BLOCKED -> READY

No state transition to VERIFIED without evidence.

## Scheduling
Use the adopted five-minute cascade as the heartbeat target:
GPTChat :00 -> Project Overseers :05 -> Workers :10, repeating every 15 minutes with phase offsets. Event-driven dispatch may occur earlier.

## Current limitation
The repository currently defines worker roles and task/control-plane primitives, but a persistent hidden worker runtime cannot be claimed solely from repository files. The implementation milestone is therefore to prove dispatch using available execution providers before representing a worker as continuously active.

## Acceptance test
For each worker role, dispatch one harmless evidence-only task and record:
ASSIGNED, EXECUTING, CHECKPOINTED, evidence, verification, and READY.

A role is considered operational only after its complete lifecycle is independently evidenced.
