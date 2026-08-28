# Project Overseer Inbox Protocol

This directory is the persistent communication layer between the GPTChat Overseer and individual Project Overseers.

## Operating rule

Every Project Overseer must have a persistent inbox and state file. Its scheduled wake cycle must:

1. Read its inbox and state.
2. Identify the newest valid task assigned to it.
3. Acknowledge the task before execution when possible.
4. Execute within its authorised boundary.
5. Record the result, evidence, blockers, allowance state, and next action.
6. Leave a durable checkpoint.
7. Return to waiting for the next scheduled cycle unless another authorised task is already queued.

## Permission rule

Do not stop merely because a capability is unavailable. Record the exact missing permission/tool/access required, mark the task `blocked`, and continue any independent work that is permitted. Human intervention is required only when the missing capability genuinely cannot be supplied by the available agents/tools.

## Status protocol

`QUEUED -> ACKNOWLEDGED -> EXECUTING -> CHECKPOINTED -> AWAITING_VERIFICATION -> VERIFIED`

Failure/blocking states:

`FAILED` or `BLOCKED`

Never mark a task `VERIFIED` without observable evidence.

## Parent/child loop

GPTChat Overseer assigns tasks. Project Overseers execute and respond. GPTChat Overseer verifies the response and writes the next task. Sub-agents follow the same protocol beneath their Project Overseer.

## No-human-wait rule

A scheduled wake is an execution opportunity, not a request for permission. If a valid task is present and within authority, execute it without waiting for the owner.

## Canonical files

Each Project Overseer should have:

- `INBOX.md` — human-readable task queue and responses.
- `STATE.yml` — machine-readable current state/checkpoint.

The files are intentionally simple. AgentOS may later replace them with a database/event bus without changing the protocol.
