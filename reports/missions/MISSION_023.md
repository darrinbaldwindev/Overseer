# Mission 023 — Wake Runner CI Verification

**Date:** 2026-09-01
**Status:** BLOCKED / REMEDIATION REQUIRED

## Objective
Verify the newly scheduled Project Overseer wake runner using actual GitHub Actions evidence and close any regressions before enabling write-capable autonomy.

## Evidence
GitHub Actions runs `33508320323` and `33508332925` executed the AgentOS test suite. Both failed with **188 passed / 3 failed**.

All three failures share the same root cause: the current dispatch validator requires `acceptance_criteria` and `mission_id`, while the new local/GitHub wake test fixtures omit them. The failure originates in `validateDispatchTask` and reaches `MemoryDispatchStore` / `runGitHubWakeCycle`.

The current canonical dispatch validator requires `task_id`, issuer, target, objective, priority, scope, constraints, acceptance criteria, authority, status and mission ID; it also requires `authority.granted_capabilities` to be an array. This is an intentional safety contract and should not be weakened to make the new tests pass.

## Action
Created AgentOS P0 Issue #58 requiring the fixtures to be brought up to the canonical dispatch contract and the full suite rerun.

## Decision
Do **not** declare the wake runner GREEN. Do **not** enable write-capable autonomous execution. The failure is actionable contract drift in the newly added tests.

## Next action
Update `tests/local-cycle.test.mjs` and `tests/github-wake.test.mjs` fixtures with the required canonical fields, preserve failure-path coverage, rerun the full suite, and capture commit-scoped successful CI evidence.
