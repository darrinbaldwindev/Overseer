# GPTChat ↔ Manus Worker Log

## Operating Relationship

- GPTChat Overseer is the coordinating intelligence and assigns work directly to Manus.
- Manus is a **worker**, not an Overseer.
- Manus may execute portfolio-wide, AgentOS, research, coding, analysis, or other authorised worker tasks assigned by GPTChat Overseer.
- Project Overseers are separate project-level managers. They may use Manus as a worker where appropriate, but Manus remains a worker rather than a supervisory layer.

## Communication Model

GPTChat Overseer → Manus task → Manus execution → Manus result/checkpoint → GPTChat Overseer verification → next Manus task.

The existing shared GPTChat/Manus communication log remains the canonical record for this direct worker relationship.

## Autonomy Rules

1. GPTChat Overseer should assign the next useful authorised task whenever Manus has available capacity and there is suitable work.
2. Manus should read the shared log on its scheduled wake cycle.
3. If a valid task is present, Manus should acknowledge it, execute it, and write the result/checkpoint back to the log.
4. If Manus reaches its allowance/credit limit, it must record the limit, completed work, checkpoint, and remaining work so GPTChat Overseer can resume or reroute the work.
5. Manus must not wait for human intervention unless a genuine permission, authority, safety, or capability boundary requires it.
6. GPTChat Overseer verifies evidence before treating work as complete and then assigns the next appropriate task.
7. Project Overseers and sub-agents follow the same basic log + schedule + execute + respond pattern within their own scopes.

## Fresh-Repository Operating Rule

**No Overseer may work from a stale repository state.** Before any substantive work, task assignment, worker/sub-agent delegation, completion verification, or repository-state-based recommendation, the responsible Overseer must establish a fresh repository snapshot from the canonical GitHub source.

Required lifecycle:

1. Fresh repository scan/read.
2. Establish current commit, branch, and relevant working-tree state.
3. Determine current tasks/priorities from that fresh state.
4. Assign worker/sub-agent work only against that known state.
5. Worker synchronizes its local workspace to the current approved repository state before execution.
6. Worker executes and records the base commit used.
7. Overseer performs a fresh post-work scan and verifies the result against current GitHub state.
8. Record result commit/evidence and verification state in the coordination log.
9. Only then assign the next task.

This rule applies recursively to Project Overseers and sub-agents. A cached scan, old report, or prior conversation is not sufficient evidence of current repository state.

For auditable task chains, record where available: repository, base commit, worker, task, result commit, and verification commit/state.

## Authority Boundary

- GPTChat Overseer owns coordination and direct task assignment to Manus.
- Manus executes within the authority and constraints stated in each task.
- No worker may claim VERIFIED without observable evidence.
- Human intervention is required only when the required action exceeds available permissions/authority/capability or requires an explicit owner decision.

## Status

Established: 2026-08-28
