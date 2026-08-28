# SUBWORKER-SKILLS-001

## Assigned by
GPTChat Overseer

## Role
Sub-worker task. Do not act as an Overseer.

## Objective
Design and initiate the AgentOS Skills Agent system using the reusable capabilities already identified across the Overseer/AgentOS work.

## Required work
1. Inspect the current Overseer/AgentOS repository material relevant to skills, reusable capabilities, task decomposition, routing, checkpoints, verification, repo scanning, scheduling, allowance/failover and worker handoffs.
2. Identify which capabilities should become reusable Skills Agents versus ordinary worker procedures.
3. Produce a provider-agnostic Skills Agent architecture: skill registry, capability schema, task contract, invocation/return contract, evidence requirements, lifecycle, permissions and verification.
4. Map existing candidate skills to priority tiers and identify gaps.
5. Design the smallest practical first Skills Agent that can be tested without introducing unnecessary complexity.
6. Define a deterministic test for skill discovery → assignment → execution → evidence → verification → result.
7. Do not claim implementation unless actual repository changes are made and evidenced.
8. Do not modify production/project repositories as part of this design task unless explicitly authorised.

## Acceptance criteria
- Clear Skills Agent architecture and boundaries.
- Reusable-skill inventory with priorities.
- First implementation/test recommendation.
- Evidence from repository inspection.
- Structured result and checkpoint returned to GPTChat Overseer.
- Status must be COMPLETED, PARTIALLY_COMPLETED or BLOCKED based on actual evidence.

## Operating rule
Continue autonomously within authorised scope. If one part is blocked, complete all independent portions and record the exact blocker.
