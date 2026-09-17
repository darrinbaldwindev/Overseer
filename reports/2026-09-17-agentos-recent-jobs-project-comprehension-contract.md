# AgentOS — Recent Jobs / Project Comprehension Contract

**Date:** 2026-09-17 AEST  
**Task:** M-A052  
**Status:** COMPLETE / USER-COMPREHENSION CONTRACT

## Current bounded implementation
Frontend #111 exact `f89dd5cb49ffa7efe0649ca2aee433d19cf0fd34` is OPEN/DRAFT/UNMERGED and its exact-head Tests `35097976181` are SUCCESS.

Recent Jobs is a bounded read-only projection from canonical `dispatch.task` artifacts. It requires canonical project correlation and Basic Chat scopes the view to `agentos-local`. Foreign-project or missing-project tasks fail closed.

## User-facing distinction
**Jobs** answers: `What work has AgentOS been doing in this bounded project context?`

It does not establish that a complete mainstream **Projects** product surface exists.

## Safe language
- `Recent Jobs`
- `Work for this AgentOS project`
- `Execution completed`
- `Verification` when the canonical lifecycle says verification
- `Escalated` when canonical lifecycle says escalated

## Avoid
- `All your projects` unless a canonical cross-project composition source exists;
- `Project dashboard` for the current bounded Jobs projection;
- `Verified` merely because dispatch says completed;
- `Assured by Henry` unless PRS says so;
- `Everything AgentOS has done` when the projection is intentionally bounded.

## Simple-mode explanation
> **Recent Jobs shows work AgentOS has recorded for this AgentOS project. A completed job means execution finished; verification and assurance are shown separately when available.**

## Tech Head disclosure
Expose correlation identifiers/source details progressively where useful, but do not create a frontend-owned project registry or infer missing project membership.

## Marketing rule
A screenshot of Recent Jobs must not be captioned as proof of a shipped Projects workspace. **A truthful bounded surface is stronger than a synthetic complete product.**
