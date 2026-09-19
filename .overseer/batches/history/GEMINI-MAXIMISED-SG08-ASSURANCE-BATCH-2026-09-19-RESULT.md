# GEMINI MAXIMISED SG-08 ASSURANCE BATCH — EXECUTION RESULT — 2026-09-19

Controlling batch: `.overseer/batches/GEMINI-MAXIMISED-SG08-ASSURANCE-BATCH-2026-09-19.md`

Executor role: Gemini Overseer / independent assurance reviewer

## Fresh state

### AgentOS PR #104
- Branch: `agent/overseer/windows-worker-bridge`
- Exact head: `6b32b2cad54eb58bbf8d30285c82af875a211686`
- State: OPEN / DRAFT / UNMERGED
- SG-08 repair evidence is explicitly carried on separate PR #125 and must not be transferred back to #104.

### AgentOS PR #125
- Title: `fix(sg08): hold POSIX kernel fence through durable receipt`
- Branch: `work/sg08-posix-kernel-fence-integration-20260919`
- Base: `work/sg08-posix-kernel-fence-spike-20260919`
- Exact head: `203273761794cca8c7a9636d45eae0249a435a72`
- State: OPEN / DRAFT / UNMERGED
- Changed files reviewed include:
  - `runtime/posix-kernel-fence.mjs`
  - `runtime/project-file-writer.mjs`
  - `tests/posix-kernel-fence.test.mjs`
  - `tests/project-file-writer-sg08-false-success-baseline.test.mjs`
  - `tests/project-file-writer-sg08-receipt-window.test.mjs`
  - `tests/project-file-writer-three-writer-retirement.test.mjs`

## VERIFIED NOW

1. POSIX continuous-fence primitive

`runtime/posix-kernel-fence.mjs` opens the target parent directory and passes the already-open directory fd to a bounded `sh` child. The child obtains `flock --exclusive --nonblock` on that inherited fd and remains alive until release. This removes the prior dedicated pathname-lock rename/recreate race from the continuous exclusion primitive.

The primitive creates no scheduler, ledger, registry, authority source, persistence system or assurance plane.

2. Crash release / contention

Exact-head tests prove:
- concurrent acquisition is rejected as busy;
- acquisition succeeds again after release;
- different targets in the same directory intentionally share the conservative fence;
- metadata lock pathname replacement does not permit a second kernel-fence owner;
- killing the owning Node process causes kernel ownership to release and a successor can later acquire.

3. Writer integration ordering

The PR #125 writer diff shows:
- continuous fence acquisition precedes metadata-lock establishment;
- fence acquisition failure maps to fail-closed primitive-unavailable or retryable live-contention behavior;
- metadata-lock establishment failure triggers fence release attempt before returning;
- success paths retire POSIX metadata ownership before success receipt persistence while the kernel fence remains held;
- the kernel fence is released in the final cleanup after receipt persistence or failure handling.

The intended critical ordering is therefore materially stronger than the #123/#104 pathname-only POSIX design.

4. False-success regressions repaired for tested class

The exact-head SG-08 regression files no longer assert the old defect.

They now prove:
- ownership displacement during metadata retirement results in zero durable success receipts;
- successor installation after publish results in zero durable success receipts;
- prepared-order displacement preserves prepared state but writes zero durable success receipts;
- a governed successor attempting entry after verification but before durable success receipt receives `PROJECT_FILE_LIVE_CONTENTION`; the original writer may persist its valid receipt while the successor persists none.

5. Exact-head AgentOS CI

AgentOS Tests run `35420953642` / #2029:
- exact AgentOS head: `203273761794cca8c7a9636d45eae0249a435a72`;
- conclusion: SUCCESS;
- Ubuntu / Node 22: PASS;
- Windows / Node 26: PASS on unchanged-head attempt 2;
- npm audit step: PASS in both jobs.

6. Independent PRS challenge

PRS repo: `darrinbaldwindev/PRS`

PRS PR #30 targeted AgentOS PR #125 exact head. The target manifest on PRS head `be1932504213b64b89089834a2c3d9969a2da834` binds:
- `agentos_target = 203273761794cca8c7a9636d45eae0249a435a72`
- `pr = 125`

PRS workflow run `35421118895`, `Validate AgentOS project-file assurance target`, completed SUCCESS.

Artifact:
- name: `prs-agentos-project-file-target-35421118895-1`
- artifact ID: `10577488000`
- digest: `sha256:5fe3c9ae6bb37c5e2fbbc22be3a8a4811a74c46df56f8cafbc708939bf073703`

The PRS carrier explicitly reports bounded `NEGATIVE_CASES_PASS`, including continuous commit ownership with `defect_count: 0`, while retaining `assurance_certified: false` and `production_promotion_allowed: false`.

7. Dependency / primitive scan

AgentOS `package.json` contains no external dependency declarations. `package-lock.json` contains only the root package.

Therefore there is no installed npm locking library to reuse. The current repair depends on Node core APIs plus the POSIX environment providing `sh` and `flock`.

## CLASSIFICATION

`SG08-BOUNDED-REPAIR-PASS-CANDIDATE`

Meaning: the specific stale-owner false-success class reproduced on the predecessor lineage is no longer reproduced by the reviewed exact-head deterministic tests and independent PRS negative-case probes on AgentOS PR #125 head `203273761794cca8c7a9636d45eae0249a435a72`.

This is not overall AgentOS Green, merge readiness, completion-grade PRS certification, or production readiness.

## RESIDUAL / UNKNOWN

1. `sh` and `flock` are explicit POSIX environment prerequisites. The implementation fails closed if the child cannot establish the fence, but dedicated exact tests for absent `sh`, absent `flock`, and pre-READY abnormal exit were not independently established in this batch.
2. Same-directory serialization is intentionally conservative and may reduce parallel throughput; this is accepted as a safety tradeoff for this bounded repair candidate.
3. Hard process death after publish but before durable receipt remains a distinct recovery window requiring continued evidence. Existing prepared/recovery governance must remain controlling; no blind replay is authorized.
4. A durable receipt followed by death before fence release should be handled by idempotent receipt replay after kernel release; completion-grade recovery evidence should still challenge this explicitly.
5. PR #125 POSIX evidence does not transfer to Windows ownership semantics or to broader PR #104.
6. Hosted Windows CI is not physical Windows owner-machine acceptance.
7. Independent Green/security review on the unchanged #125 head remains pending unless separately evidenced.
8. PRS probe evidence is bounded/non-certifying and is not overall PRS PASS.

## DURABLE ACTION TAKEN

A Gemini Overseer independent assurance checkpoint was posted to AgentOS PR #125 as issue comment ID `5742342420`, recording the bounded PASS-CANDIDATE and residual limits.

## NEXT EXECUTABLE ASSURANCE TASKS

1. Add/verify deterministic negative fixtures for missing `sh`, missing `flock`, and child exit before READY; require zero mutation/receipt and fail-closed primitive-unavailable classification.
2. Challenge receipt-persistence failure while POSIX kernel fence remains held; prove no false success and clean fence release/recovery-required outcome.
3. Add/verify hard process-kill fixture after publish but before success receipt and require deterministic recovery without duplicate mutation.
4. Add/verify kill after durable receipt but before explicit fence release; require replay to return durable receipt with zero second write.
5. Run independent Green/security review against unchanged AgentOS #125 head.
6. Only after identical-head Green evidence, run any required completion-grade PRS challenge without reusing predecessor assurance.
7. Keep physical Windows acceptance separate; do not infer it from hosted CI.

## SAFETY BOUNDARY

No merge. No approval. No ready transition. No rebase. No deploy. No credential/security-policy change. No production write. No physical-host action. No production autonomy. No overall AgentOS GREEN.
