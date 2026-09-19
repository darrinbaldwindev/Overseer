# GEMINI MAXIMISED SG-08 ASSURANCE BATCH — 2026-09-19

Owner: Darrin / ChatGPT Portfolio Overseer  
Executor role: Gemini Overseer / independent assurance reviewer  
Mode: maximum safe vertical assurance execution  
Canonical coordination: `darrinbaldwindev/Overseer` + live AgentOS PR/CI/runtime evidence

## Mission

Use the full useful capacity of this batch to independently reconcile and challenge AgentOS SG-08 continuous project-file ownership without mutating production behavior, self-certifying Green, or duplicating governance/control planes.

Operating loop:

`FRESH SCAN -> RECONCILE -> IDENTIFY CURRENT CANDIDATE -> REVIEW DIFF/TESTS -> VERIFY EXACT-HEAD CI -> CHALLENGE FALSE-GREEN -> CLASSIFY -> RECORD -> RE-SCAN -> NEXT ASSURANCE TARGET`

Repository/runtime/CI evidence outranks this file. Refresh exact branch/head immediately before every assurance claim.

## Hard boundaries

Do NOT merge, approve, mark-ready, rebase, deploy, change credentials/security policy, enable production autonomy, perform physical Windows actions, or claim Green/PRS/production readiness from CI alone.

Do NOT create a second scheduler, queue, ledger, authority source, permission system, worker registry, persistence plane, Green system, PRS system, ownership registry, or recovery plane.

Worker success is not completion. CI success is not assurance. Missing material evidence remains UNKNOWN/BLOCKED.

## Current reconciliation baseline

The earlier controlling #104 head `607f2683b7d3b234fc6ffa70e2a7d42e31499c3a` reproduced SG-08 stale-owner false-success on POSIX: a durable `MUTATED_VERIFIED` receipt could persist after pathname ownership displacement and before release detected loss.

Fresh state moved the SG-08 repair onto draft PR #125:

- PR: #125 `fix(sg08): hold POSIX kernel fence through durable receipt`
- branch: `work/sg08-posix-kernel-fence-integration-20260919`
- exact head at batch creation: `203273761794cca8c7a9636d45eae0249a435a72`
- base: `work/sg08-posix-kernel-fence-spike-20260919`
- status: OPEN / DRAFT / UNMERGED

PR #104 remains canonical broader Windows-worker lineage, but SG-08 repair evidence must be judged on #125 exact head and must not be transferred backward to #104.

## P0 — Verify repair shape

### G-SG08-01 — Kernel fence primitive

Review `runtime/posix-kernel-fence.mjs` and prove the primitive is bounded and composition-only.

Required properties:
- POSIX only;
- kernel advisory exclusion;
- no lock-state registry;
- no PID-age takeover;
- crash/process-death release;
- successor cannot acquire while owner holds fence;
- metadata lock pathname replacement cannot create a second kernel-fence owner;
- release failure is explicit;
- unavailable/busy primitive fails closed.

Important implementation-specific challenge: the current candidate uses an already-open parent-directory fd and `flock --exclusive --nonblock` in a child `sh` process. Treat `sh`/`flock` availability as an execution prerequisite, not an assumed universal POSIX property.

### G-SG08-02 — Continuous critical-window ordering

Review `runtime/project-file-writer.mjs` diff.

Required invariant:

`kernel fence acquire -> metadata ownership -> prepare/verify -> publish/recovery -> postwrite verify -> metadata retirement -> durable success receipt -> kernel fence release`

A governed successor must not enter between postwrite verification and receipt persistence.

The metadata lock may be retired before receipt only if the kernel fence remains continuously held and excludes all cooperating project-file writers until receipt persistence completes.

### G-SG08-03 — False-success regressions

Review exact-head versions of:
- `tests/project-file-writer-sg08-false-success-baseline.test.mjs`
- `tests/project-file-writer-sg08-receipt-window.test.mjs`
- `tests/project-file-writer-three-writer-retirement.test.mjs`
- `tests/posix-kernel-fence.test.mjs`

Required results:
- displaced metadata owner cannot persist success receipt;
- after-publish displacement cannot persist success receipt;
- prepared-order displacement preserves prepared intent without false success;
- governed successor attempting entry during success-receipt window receives live contention and writes no receipt;
- same-directory writer serialization is explicit and accepted as a bounded tradeoff;
- kernel fence releases after owner SIGKILL;
- metadata-lock rename/recreate does not bypass kernel fence.

Do not rewrite defect tests merely to make them green. Confirm assertions changed from reproducing false success to rejecting it.

## P0 — Exact-head verification

### G-SG08-04 — AgentOS CI

Verify exact-head workflow identity and both matrix jobs.

Current evidence to verify:
- AgentOS Tests run `35420953642` / #2029
- exact head `203273761794cca8c7a9636d45eae0249a435a72`
- Ubuntu Node 22 PASS
- Windows Node 26 PASS on unchanged-head rerun
- npm audit step PASS on both jobs

A rerun on unchanged code is acceptable evidence for that head, but record attempt semantics and any prior unrelated fixture timeout separately.

### G-SG08-05 — Independent PRS evidence

Verify, where connector evidence is available, the claimed PRS exact-head negative-case challenge and ensure it explicitly remains non-certifying.

Required distinction:
- `NEGATIVE_CASES_PASS` for specific probes may support bounded defect-class repair;
- it must not be promoted to overall PRS PASS, Green, merge readiness, or production readiness unless the canonical assurance process explicitly provides those exact-head receipts.

## P0 — Architecture/dependency decision

### G-SG08-06 — Existing primitive/dependency scan

Inspect AgentOS package/dependency state and runtime ownership primitives.

Current evidence:
- `package.json` declares no runtime dependencies;
- `package-lock.json` contains only the root package;
- no existing npm lock package is available to reuse.

Therefore the POSIX fence candidate is not an npm-library reuse. It relies on OS `sh` + `flock` and Node child-process/file-descriptor inheritance. This is acceptable only if the target supported POSIX environments explicitly require/probe those tools and fail closed when unavailable.

Do not add a new locking dependency in this assurance batch.

## P0 — Residual-risk challenge

### G-SG08-07 — Required residual checks

Challenge and classify:

1. `flock` absent -> fail closed, no mutation.
2. `sh` absent -> fail closed, no mutation.
3. child exits before READY -> fail closed.
4. fence busy -> `PROJECT_FILE_LIVE_CONTENTION`, no mutation/receipt.
5. metadata lock establishment fails after fence acquisition -> fence release attempted, no mutation.
6. receipt persistence fails -> kernel fence release after failure path; result remains recovery-required, never success.
7. process killed after publish before receipt -> no automatic blind rewrite; prepared/postimage evidence governs recovery.
8. process killed after receipt before fence release -> durable receipt/idempotency prevents duplicate mutation after kernel release.
9. different target files in same directory are serialized by design; record throughput tradeoff, not safety defect.
10. Windows path stays on existing Windows-handle ownership implementation; POSIX `flock` claims must not be generalized to Windows.

Any untested item remains INSUFFICIENT EVIDENCE, not PASS.

## P1 — Green / PRS / physical gates

### G-SG08-08 — Promotion sequencing

After bounded implementation evidence:

`exact-head AgentOS tests -> independent Green/security review on unchanged head -> PRS completion-grade challenge if doctrine requires -> physical Windows acceptance where applicable`

Do not transfer assurance between different heads or PRs.

Physical Windows remains a separate owner/runtime gate and is not created by hosted Windows CI.

## Execution log — initial batch pass

Fresh reconciliation found:

- #104 advanced to `6b32b2cad54eb58bbf8d30285c82af875a211686` and explicitly points SG-08 repair evidence to separate #125.
- #125 exact head `203273761794cca8c7a9636d45eae0249a435a72`, OPEN/DRAFT/UNMERGED.
- #125 adds `runtime/posix-kernel-fence.mjs` and integrates it into the existing project-file writer.
- The kernel fence uses a parent-directory fd inherited by `sh`, with `flock --exclusive --nonblock`; the child remains alive until release, so lock lifetime is process-held rather than pathname-held.
- Exact-head SG-08 tests now assert zero false-success receipts for the old displacement cases.
- Success-receipt-window regression now attempts a real governed successor and requires `PROJECT_FILE_LIVE_CONTENTION` plus zero successor receipt.
- AgentOS Tests run `35420953642` is SUCCESS on exact head; Ubuntu/Node22 and Windows/Node26 jobs both PASS, including npm audit steps.
- AgentOS has no npm dependencies or existing lock library to reuse.

## Batch classification rule

Possible outcomes:

- `SG08-BOUNDED-REPAIR-PASS-CANDIDATE`: specific reproduced false-success class no longer reproduces, exact-head CI passes, independent negative-case assurance supports it, residual environment prerequisites are explicit/fail-closed.
- `SG08-PARTIAL`: repair works for tested window but residual crash/recovery or environment-prerequisite gaps remain unproven.
- `SG08-BLOCKED`: false-success still reproduces, fence can be bypassed, unavailable primitive does not fail closed, or exact-head evidence is missing.

None of these equals overall AgentOS GREEN.

## Durable handoff requirements

At batch end record:
- exact #104 head;
- exact #125 head;
- exact CI run/jobs;
- files reviewed;
- defect-class evidence;
- residual risks / UNKNOWNs;
- physical Windows status;
- Green/PRS status;
- next 3–8 executable assurance tasks.

No merge. No approval. No ready transition. No rebase. No deployment. No production writes. No credential changes. No overall GREEN.
