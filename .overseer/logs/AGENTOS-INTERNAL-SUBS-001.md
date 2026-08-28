# AGENTOS-INTERNAL-SUBS-001

Date: 2026-08-28
Owner: GPTChat Overseer

## Decision
AgentOS should use a small internal, provider-agnostic sub-worker pool with no separate user-facing chat windows.

## Initial roles
- REPO-CODE
- QA-TEST
- RESEARCH
- ARCHITECTURE
- SKILLS
- SECURITY-HEALTH

## Operating model
Project/AgentOS Overseer -> worker role -> task -> execution -> evidence -> checkpoint -> response -> verification.

These are ready-to-dispatch worker roles, not claims of six continuously running hidden model instances. Provider workers such as Manus, Amazon Q and Gemini may execute a role when appropriate.

## Requirements
- Reuse existing task, log, checkpoint and verification mechanisms.
- Do not create a parallel task router.
- Do not claim a worker executed unless evidence exists.
- Reuse existing skill-memory and repository-scan primitives.
- Expand the worker pool only when workload demonstrates a need.

## Test requirement
AgentOS should next test dispatch of each of the six roles using a harmless evidence-only task, then record PASS/FAIL/BLOCKED for each role.

## Status
DESIGN LOGGED — runtime dispatch not yet proven.
