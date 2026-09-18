# PROJECT CHAT VERTICAL BATCH HANDOFF

## Canonical standard
Every portfolio Project Overseer/project chat must read and apply these sources in order:

1. `darrinbaldwindev/Overseer/.overseer/doctrine/PORTFOLIO-BATCH-ENGINE.md`
2. `darrinbaldwindev/Overseer/.overseer/profiles/PROJECT-BATCH-PROFILES.md` — read only the matching project/workstream profile
3. `darrinbaldwindev/Overseer/.overseer/doctrine/VERTICAL-BATCH-EXECUTION.md` for the broader doctrine and governance rationale
4. `darrinbaldwindev/Overseer/.overseer/communication/WORK-MODE-CONTROL.md` for Work-mode escalation and central triage
5. the project's own live vertical batch file and current repo/issue/PR/CI/runtime evidence
6. `darrinbaldwindev/Overseer#49` for portfolio-significant dependencies and handoffs

The canonical engine is the common procedure. Project profiles customize only the project-specific 10–20%. Local batch files hold current work, not alternate operating doctrine.

## First receipt / refresh procedure
1. Read the canonical engine.
2. Read the matching project profile.
3. Read `WORK-MODE-CONTROL.md`.
4. Fresh-scan the project before trusting old chat/batch state.
5. Locate the established local batch path. Prefer `.overseer/batches/VERTICAL-EXECUTION-BATCH.md`; preserve a documented established alternate path until deliberately migrated.
6. Reconcile the local batch from fresh evidence.
7. Show the owner a compact **Current Batch** in the chat window: ACTIVE NOW, NEXT, BLOCKED/HOLD/UNKNOWN, VERIFIED SINCE LAST CYCLE, and BATCH SOURCE.
8. Execute the fullest safe coherent work permitted by the engine/profile.
9. If a task materially benefits from or requires ChatGPT Work, do not create an independent Work coordination path. Add a durable `WORK_REQUIRED` record with the exact project/task/repo/head/outcome/evidence/blockers/authority/next-actions fields required by `WORK-MODE-CONTROL.md`. Surface portfolio-significant escalation to the shared Overseer coordination layer.
10. Verify exact changed state.
11. Fresh-scan again.
12. Replenish the same local batch.
13. Show the compact **Updated Batch** in the chat window: what moved, what remains blocked, what is queued next, and any `WORK_REQUIRED` items sent to Portfolio Overseer control.
14. Log material progress in the project's durable control record and surface portfolio-significant state to Overseer #49.

Owner messages `cont`, `continue`, `continue autonomously`, and `continue autonomously vertically` trigger that complete cycle automatically.

## Work-mode routing rule
The ChatGPT Portfolio Overseer is the single coordination point for Work-mode escalation across the portfolio.

Project Overseers, project chats, scheduled lanes and specialist workers must log Work-required items rather than asking the owner to manually coordinate separate Work sessions or creating competing Work queues. The Portfolio Overseer reconciles those entries against active schedules and existing work, deduplicates them, chooses the appropriate execution surface, and batches them for Work where that produces the most verified useful movement.

A `WORK_REQUIRED` record grants no new authority. Work remains subordinate to owner authorization, repository governance, budgets, security, Green, PRS and physical/production restrictions.

## Visibility rule — how Overseers see changes
Project Overseers must not rely on chat memory for the standard. They discover it through durable repository pointers:

- existing `.overseer/VERTICAL-BATCH-ADOPTION.md` files point here/the doctrine;
- project batch headers should identify the canonical engine/profile;
- scheduled :00/:15/:45 execution prompts read the Overseer doctrine/handoff/bootstrap and local batch state;
- :30 reconciliation reads the shared manifest, Work-required escalations and #49, where project-significant batch changes are logged;
- :40 Jess/Michael assurance reads the exact evidence lineage produced by the execution lanes rather than trusting execution claims.

When an Overseer-role chat is active, it must project the current durable batch into the owner-facing response. This projection is for visibility only and never becomes a competing source of truth. Ordinary unrelated chats in the same ChatGPT Project do not inherit this behavior simply because they are open.

If the canonical engine/profile changes, the next fresh cycle must re-read it before executing. A copied older project script does not override the central engine.

## Governance
Do not create duplicate schedulers, queues, authority systems, registries, mission ledgers, persistence/memory systems, governance layers, Green systems or PRS systems to implement this standard. Repository/runtime/CI evidence outranks batch text. No merge/approve/ready/rebase/deploy/credential changes/production writes/spend/outreach/publication/production autonomy without explicit authority.

**NO MODEL DECIDES ITS OWN AUTHORITY.**

## Owner one-line alignment instruction
> Read the canonical Portfolio Batch Engine, your matching Project Batch Profile, and `WORK-MODE-CONTROL.md` from `darrinbaldwindev/Overseer`; fresh-scan this project; reconcile and show me the Current Batch; execute the local vertical batch; log any `WORK_REQUIRED` items for Portfolio Overseer control; verify; fresh-scan again; replenish; show me the Updated Batch; and durably log the checkpoint. My `cont` / `continue autonomously` messages trigger that full cycle.