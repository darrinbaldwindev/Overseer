# WORK MODE CONTROL

**Owner:** Darrin  
**Effective:** 2026-09-18  
**Status:** CANONICAL OWNER DIRECTION / ACTIVE

## Decision

The ChatGPT Portfolio Overseer is the single coordination point for ChatGPT Work-mode escalation across the portfolio.

### Owner reaffirmation — 2026-09-18 16:50 Australia/Brisbane

Darrin explicitly reaffirmed: **the ChatGPT Portfolio Overseer will control Work mode from now on.**

This means the Portfolio Overseer owns Work-mode intake, triage, prioritisation, deduplication, batching, routing and reconciliation across the portfolio. Project Overseers, project chats, scheduled lanes, workers and specialist Overseers must log work that materially requires or benefits from Work mode and hand control of that escalation to the Portfolio Overseer rather than independently coordinating a competing Work flow.

This is a coordination decision only. It does not expand execution authority, bypass owner-only actions, or replace AgentOS/Green/PRS/governance controls.

Project Overseers, project chats, scheduled lanes, workers and specialist Overseers must not independently create a competing Work-mode queue or coordination process. When work is better suited to Work mode, they must durably log the requirement for Portfolio Overseer triage.

This document governs coordination only. It is not a scheduler, mission ledger, authority source, queue runtime, persistence service, Green system or PRS system.

## Escalation rule

When a project chat or scheduled executor encounters work that materially benefits from Work mode, it should record a `WORK_REQUIRED` handoff in its existing durable control record and surface portfolio-significant items to the shared Overseer coordination layer.

The Portfolio Overseer decides whether to:

1. execute through available in-chat tools;
2. allocate to an existing schedule/worker;
3. batch with other Work-required items;
4. route to ChatGPT Work;
5. keep the item blocked/held because authority, evidence or prerequisites are missing.

No project chat should ask the owner to manually coordinate multiple Work sessions when the requirement can be logged and reconciled centrally.

## Required WORK_REQUIRED record

Each escalation should contain enough information for the Portfolio Overseer to act without rediscovery:

- `project`
- `task_id` or durable local task reference
- `priority`
- `reason_work_mode_required`
- `exact_repo`
- `branch / PR / exact_head` where applicable
- `requested_outcome`
- `current_evidence`
- `tests / CI already run`
- `known_blockers`
- `authority / security boundary`
- `owner_action_required` if genuinely unavoidable
- `safe_next_actions`
- `source_log / batch / issue / PR`
- `recorded_at`

## Triage principles

Prefer Work mode for substantial multi-repository, browser/computer-use, long-running research/execution, large-file, environment-heavy, or multi-step tasks where Work materially improves useful verified movement.

Do not escalate merely because a task is difficult. If the existing project chat, connector, scheduled executor or bounded worker can complete the task safely and verifiably, execute there and log the result.

Do not use Work mode to bypass authority, consent, budgets, security, Green, PRS, production restrictions, credential restrictions, owner-only physical actions or repository governance.

Work execution remains subordinate to:

- live repository/runtime/CI evidence;
- `.overseer/batches/PORTFOLIO-TASK-LEDGER.md`;
- the canonical Portfolio Batch Engine and project profile;
- exact project vertical batches;
- owner authority and applicable Green/PRS gates.

## Portfolio Overseer responsibilities

The Portfolio Overseer must:

- scan durable project logs for `WORK_REQUIRED` items;
- deduplicate overlapping requests;
- reconcile against active scheduled/manual ownership;
- prioritize by verified useful movement and dependency criticality;
- prepare dense vertical Work batches rather than one-task handoffs where safe;
- ensure Work results are written back to durable project/portfolio evidence;
- mark items completed, blocked, superseded or replenished based on fresh evidence;
- never treat Work completion claims as overall GREEN without independent gates.

## Relationship to historical Work handoff

`.overseer/communication/CHATGPT-WORK-HANDOFF.md` is historical context only unless refreshed. It must not be treated as the current portfolio source of truth. Current Work execution starts from live repo/PR/CI evidence, the current task ledger, this control document, current owner batch, and project vertical batches.

## Governance

External execution capability provides capability, never authority.

No merge, approval, ready transition, rebase, deployment, credential/security-policy change, production write, spend, supplier/partner contact, publication, production autonomy, unrestricted elevation or invented physical-host evidence is authorized by a `WORK_REQUIRED` record or by Work-mode routing itself.

**NO MODEL DECIDES ITS OWN AUTHORITY.**
