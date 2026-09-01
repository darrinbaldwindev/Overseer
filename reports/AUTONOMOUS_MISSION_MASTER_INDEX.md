# Autonomous Mission Master Index

**Created:** 2026-09-01
**Purpose:** Durable index of CHATGPT Overseer autonomous portfolio batches.

## Mission index

| Mission | Date | Scope | Result | Evidence boundary |
|---|---|---|---|---|
| 001–026 | 2026-09-01 | Prior AgentOS/portfolio control work | Recorded previously | See individual mission history |
| 027 | 2026-09-02 | Atomic lease-store reference hardening | COMPLETE | Deterministic in-memory lease store + tests; production distributed atomicity unproven |
| 028 | 2026-09-02 | Lease integration into GitHub wake | PARTIALLY_COMPLETE | Lease enforced in wake path; adapter-level regression added subsequently |
| 029 | 2026-09-02 | Idempotency reference hardening | COMPLETE | Deterministic in-memory idempotency store + tests; distributed persistence unproven |
| 030 | 2026-09-02 | Idempotent GitHub wake integration | COMPLETE | Wake path now rejects previously completed task IDs; deterministic regression test added |

## Mission 030 summary

Integrated the idempotency guard into `src/dispatch/github-wake.mjs` alongside the lease guard. A task must acquire a lease and pass the idempotency begin check before execution. On completion, the canonical response is persisted through the idempotency store before the durable response audit event is emitted. A repeated wake for the same task is rejected as `already_completed` without invoking inspection/action.

Added `tests/github-wake-idempotency.test.mjs` proving that a completed task cannot be completed twice through the wake path.

**Evidence boundary:** this proves deterministic in-process lease/idempotency orchestration. It does not prove distributed atomicity between independent GitHub runners. The next gate is an actual persistence adapter with conditional atomic operations plus fresh CI evidence.

## Control rules

1. Mission numbers are sequential and never reused.
2. Gemini mission numbering is separate.
3. Historical missions are not fabricated.
4. CLAIMED, IMPLEMENTED, VERIFIED and ASSURED remain separate.
5. Accessibility never equals GREEN.
6. Green Agent and PRS remain independent assurance requirements.
7. Material changes require fresh verification.
8. Owner-controlled production credentials/permissions remain outside autonomous authority unless separately authorised.
9. Missing evidence cannot be promoted to GREEN by inference.
10. Project Overseers cannot self-declare GREEN.
11. No duplicate runtime/router/assurance engine may be introduced.
12. A GitHub-backed adapter is not equivalent to a live wake service.
13. A workflow definition is not evidence of a completed workflow run.
14. A lease primitive is not equivalent to atomic distributed locking until the backing store provides the required concurrency semantics.
15. An in-memory idempotency store is not evidence of distributed idempotency.

## Next mission target

Introduce an explicit persistence interface for leases/idempotency so the GitHub adapter can supply atomic conditional operations, then add adapter-level competing-runner tests and fresh CI verification.
