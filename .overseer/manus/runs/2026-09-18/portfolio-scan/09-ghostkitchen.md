# GhostKitchen fresh scan

**Scan scope and method.** Read-only GitHub API/CLI inspection of `darrinbaldwindev/GhostKitchen`, including repository metadata, `main`, open PRs/issues, recent Actions runs, branch protection, and governance/batch/handoff files. Scan date: 2026-09-18 (UTC context from GitHub timestamps). No repository or GitHub state was modified.

## Current state

| Field | Evidence | Classification |
|---|---|---|
| Repository | [darrinbaldwindev/GhostKitchen](https://github.com/darrinbaldwindev/GhostKitchen), public, not archived | **VERIFIED FACT** |
| Default branch | `main`; branch protection reported `false` | **VERIFIED FACT** |
| Exact head | `f51d4080cfb7bfb0448fd27153f4bf3c9225cf9f` | **VERIFIED FACT** |
| Repository posture | README describes a delivery-first food-business/franchise platform; current phase is architecture/scope and says working specification is under `docs/` | **VERIFIED FACT** (README at current head) |

## Open work and checks

There are **4 open PRs**: [#37](https://github.com/darrinbaldwindev/GhostKitchen/pull/37) “fix: prevent packaging provenance gaps from qualifying economics”; [#32](https://github.com/darrinbaldwindev/GhostKitchen/pull/32) “test: harden economics batch metadata contract”; [#28](https://github.com/darrinbaldwindev/GhostKitchen/pull/28) “docs: reconcile GhostKitchen project state and missions”; and [#27](https://github.com/darrinbaldwindev/GhostKitchen/pull/27) “docs: normalize ghost-kitchen unit economics”. Their open state is **VERIFIED FACT**; readiness, mergeability, and ownership beyond the visible GitHub records are not inferred.

There are **17 open non-PR issues**, including overlapping economics/evidence work: [#31](https://github.com/darrinbaldwindev/GhostKitchen/issues/31) C-002 metadata/evidence follow-on, [#29](https://github.com/darrinbaldwindev/GhostKitchen/issues/29) GK-010 calculator, [#24](https://github.com/darrinbaldwindev/GhostKitchen/issues/24) GK-009 channel economics, [#23](https://github.com/darrinbaldwindev/GhostKitchen/issues/23) GK-008 concept research, [#22](https://github.com/darrinbaldwindev/GhostKitchen/issues/22) GK-007 QA/compliance evidence, [#21](https://github.com/darrinbaldwindev/GhostKitchen/issues/21) GK-006 OS requirements, [#20](https://github.com/darrinbaldwindev/GhostKitchen/issues/20) GK-005 franchise package, [#19](https://github.com/darrinbaldwindev/GhostKitchen/issues/19) GK-004 architecture, [#18](https://github.com/darrinbaldwindev/GhostKitchen/issues/18) GK-003 operating model, [#17](https://github.com/darrinbaldwindev/GhostKitchen/issues/17) GK-002 concepts, [#16](https://github.com/darrinbaldwindev/GhostKitchen/issues/16) GK-001 unit economics, plus #8–#15. Count and titles are **VERIFIED FACTS**; issue descriptions are not authorization.

Recent Actions evidence shows the `Economics validation` workflow succeeded on current `main` head (`34918303063`, 2026-09-15T01:41:59Z) and on a newer non-main PR branch (`35283090214`, branch `work/packaging-provenance-gate-2026-09-17`, head `5b1b78c089c6e0ace7da1065c092d922f7d54a4c`, 2026-09-17T22:39:15Z). Successful checks establish only that those workflow runs concluded successfully; they do **not** establish merge/release/commercial readiness. **VERIFIED FACT / limitation.**

## Governance, handoff, and collision assessment

Relevant files present at `main` include `.overseer/VERTICAL-BATCH-ADOPTION.md`, `docs/OVERSEER.md`, `docs/overseer/CHATGPT_HANDOFF.md`, multiple `docs/batches/*`, `docs/level2/AGENTOS-WORKLOAD-2026-09-13.md`, the economics workflow, evidence-handoff tooling/tests, and economics fixtures. The repository handoff explicitly defines `CHATGPT Head Overseer → GhostKitchen Project Overseer → authorised worker(s) → verification → project log → CHATGPT Head Overseer`, requires fresh state and evidence, and says to fail closed on missing authority/gates. **VERIFIED FACT.**

The checked-in batch record says prior work observed open PR #32 and overlapping issue #31, and that the next safe dependency is field-to-record handoff/starter fixtures while physical observations remain unknown; it expressly says no duplicate implementation should be created. Current scan now shows four open PRs, including additional active docs/economics/provenance work, and 17 open issues. Therefore an active **ChatGPT/governed handoff collision is verified**: the repository has an explicit overseer chain and active batch/mission records that overlap the requested Lite scan domain. A separate “manual owner” reservation cannot be proven from GitHub alone; the visible issue/PR authors are `darrinbaldwindev`, but author identity is not equivalent to an exclusive assignment. **UNKNOWN** for any unrecorded manual reservation; **REASONABLE INFERENCE** that independent work would risk duplication, especially around economics metadata/provenance and handoff fixtures.

## Priority findings

1. **VERIFIED FACT — ownership/duplication gate:** four open PRs and 17 open issues overlap economics, evidence, documentation, and governance; #31 is explicitly an overlapping C-002 follow-on and #37/#32 directly concern provenance/metadata validation.
2. **VERIFIED FACT — governance gate:** `main` is unprotected according to the branch API. This is not proof that merging is unsafe, but it means no branch-protection evidence was found in this scan.
3. **VERIFIED FACT — evidence gate:** repository batch notes keep physical observations and comparable concept economics `UNKNOWN/BLOCKED`; successful CI cannot substitute for those observations.
4. **UNKNOWN — manual ownership:** no authoritative GitHub record proves that a specific manual worker has released any of the overlapping slices; do not infer release from issue authorship or successful checks.
5. **REASONABLE INFERENCE — safe action:** creating another economics/evidence implementation or fixture would likely duplicate active work and violate the checked-in handoff/batch direction.

## Lite disposition

**Safe independent Lite slice: BLOCKED_STABLE.** No slice is clearly unowned from the exact repository evidence. Do not implement, comment, approve, merge, rebase, deploy, contact, or create a competing handoff/control-plane record. Reassess only after an authoritative owner/mission record explicitly releases a bounded slice and reconciles PRs #27, #28, #32, #37 and issues #31/#29/#24/#23/#16.

**Overall classification: BLOCKED_STABLE**, with individual claims classified above. This report is an evidence record, not an approval or readiness certification.

## Sources

- Repository: https://github.com/darrinbaldwindev/GhostKitchen
- Current head: https://github.com/darrinbaldwindev/GhostKitchen/commit/f51d4080cfb7bfb0448fd27153f4bf3c9225cf9f
- Governance/handoff: https://github.com/darrinbaldwindev/GhostKitchen/blob/main/docs/overseer/CHATGPT_HANDOFF.md
- Batch adoption: https://github.com/darrinbaldwindev/GhostKitchen/blob/main/.overseer/VERTICAL-BATCH-ADOPTION.md
- Overseer charter: https://github.com/darrinbaldwindev/GhostKitchen/blob/main/docs/OVERSEER.md
- Workflow: https://github.com/darrinbaldwindev/GhostKitchen/blob/main/.github/workflows/economics-validation.yml
