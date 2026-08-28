# Project Overseer Heartbeat Test Matrix

**Run:** 2026-08-28 heartbeat
**Canonical protocol:** `.overseer/PROJECT-OVERSEERS/README.md`
**Autonomous loop:** `protocols/autonomous-loop.md`

## Evidence rule
A chain is only marked passed when wake, task consumption, execution, evidence, and durable response are observable. No task is marked VERIFIED merely because it was read or written.

| Project Overseer | Wake/inbox-state | Task consumption | Execution | Evidence | Durable response | Result | Next useful assignment |
|---|---|---|---|---|---|---|---|
| AgentOS | PASS | PASS | PASS (read-only inspection) | PASS | PASS; state checkpoint persisted | AWAITING_VERIFICATION | Run AgentOS test suite with execution-capable worker |
| GlobalShopCo | PASS | PASS | PASS (read-only tree inspection) | PASS | PASS; state checkpoint persisted | AWAITING_VERIFICATION | Reconcile current branch against latest Overseer protocol and run validation |
| Franchise | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED | Create canonical `.overseer/PROJECT-OVERSEERS/franchise/INBOX.md` and `STATE.yml` only under explicit portfolio assignment |
| Amazon-Affiliate | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED | Create canonical Project Overseer inbox/state only under explicit portfolio assignment |
| Overseer | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED | BLOCKED | Establish canonical self-supervision inbox/state; do not fabricate task authority |

## Portfolio findings

1. The canonical Project Overseer protocol requires every Project Overseer to have an `INBOX.md` and `STATE.yml` and defines `QUEUED -> ACKNOWLEDGED -> EXECUTING -> CHECKPOINTED -> AWAITING_VERIFICATION -> VERIFIED`.
2. The current canonical tree visibly contains only `agentos` and `globalshopco` under `.overseer/PROJECT-OVERSEERS`. The portfolio registry contains additional repositories, but registry membership is not evidence that a Project Overseer inbox/state exists.
3. A second lowercase `.overseer/project-overseers/globalshopco` tree exists with additional test/task artifacts. This is a control-plane consistency issue and must not be silently treated as canonical.
4. The top-level `.overseer/STATE.yml` and `.overseer/PORTFOLIO.md` remain stale relative to the populated registry; this is a material supervisory-state discrepancy.

## Current status

**Confirmed runnable chains:** 2/5
**Blocked by missing canonical Project Overseer state:** 3/5
**Verified:** 0/5 in this run (parent verification has not been independently observed)
**Failed:** 0/5

## Authorised next work

- Prioritise reconciliation of the duplicate uppercase/lowercase Project Overseer paths.
- Keep the three missing Project Overseers explicitly blocked rather than inventing authority.
- Use the existing skill-memory and autonomous-loop primitives rather than creating competing orchestration layers.
