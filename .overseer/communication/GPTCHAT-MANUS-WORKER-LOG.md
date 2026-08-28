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

## Authority Boundary

- GPTChat Overseer owns coordination and direct task assignment to Manus.
- Manus executes within the authority and constraints stated in each task.
- No worker may claim VERIFIED without observable evidence.
- Human intervention is required only when the required action exceeds available permissions/authority/capability or requires an explicit owner decision.

## Status

Established: 2026-08-28
