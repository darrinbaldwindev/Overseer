# Level 2 incomplete-install recovery checkpoint — 2026-09-18

Canonical mission: `darrinbaldwindev/Overseer#49`  
Controlling batch: `.overseer/batches/OWNER-START-WORK-BATCH-2026-09-15.md`  
Disposition: bounded verified movement; no overall GREEN

## Fresh reconciliation

- AgentOS `main`: `962cb3820b83506f9e6d90f50e003690dd85a8a1`.
- AgentOS PR #104: OPEN / DRAFT / UNMERGED at `607f2683b7d3b234fc6ffa70e2a7d42e31499c3a`.
- AgentOS PR #111: OPEN / DRAFT / UNMERGED at `3ac4d306087ac0ef34d65ba63c76b704bc821e4a`.
- AgentOS PR #112: OPEN / DRAFT / UNMERGED at `33eca1d257179a873a8aca2eea1a4e5e994415a0`.
- PRS PR #17: OPEN / DRAFT / UNMERGED at `12889cb4c732d3e3de271c31160d05cf8ea694e5`.
- PRS PR #24: OPEN / DRAFT / UNMERGED at `3039c886bdcff911f7c6dcc3e086368058e57fb6`.

The current #104 lineage already materially implements the batch's bounded PowerShell composition and local-wake work. Project-file mutation remains blocked by SG-08 continuous-ownership assurance. Canonical authenticated actor/grant provenance (SG-01/02) and physical owner-Windows acceptance remain unproven.

## AgentOS bounded repair

Draft PR: `darrinbaldwindev/AgentOS#122`  
Branch: `work/pr104-install-recovery-contradictions`  
Base: AgentOS PR #104 exact head `607f2683b7d3b234fc6ffa70e2a7d42e31499c3a`  
Head: `8168fdf310041a083bf993d24664bb9a940714ad`

Files:

- `scripts/install-local.mjs`
- `tests/install-local.test.mjs`

Defect reproduced: #104 blocked `config exists / canonical state missing`, but the inverse partial-install state silently synthesized a new config beside preserved canonical state and reported success.

Repair: when canonical state exists but config is missing, non-force installation now fails closed as `LOCAL_INSTALL_INCOMPLETE`, leaves config absent, and preserves state byte-for-byte. Explicit `force` recovery semantics are unchanged.

Evidence:

- focused local installer suite: 4 passed;
- full local AgentOS suite: 633 passed, 2 skipped, 0 failed (635 total);
- `git diff --check`: PASS;
- exact-head AgentOS Tests run `35305662966` / #1933: SUCCESS;
- Ubuntu/Node 22: 633 passed, 2 skipped; npm audit 0 vulnerabilities;
- hosted Windows/Node 26: 630 passed, 5 skipped; npm audit 0 vulnerabilities.

Hosted Windows CI is not physical owner-laptop acceptance.

## Independent PRS challenge

Draft PR: `darrinbaldwindev/PRS#26`  
Branch: `work/pr122-install-assurance`  
Base: PRS PR #17 exact head `12889cb4c732d3e3de271c31160d05cf8ea694e5`  
Head: `669617266b9183c3b25ac1b674b66a83d2f76628`

Files:

- `scripts/challenge-agentos-install-recovery.mjs`
- `.github/workflows/validate-agentos-install-recovery.yml`

The immutable probe pins both AgentOS targets:

- `607f2683...` -> `INSTALL_RECOVERY_DEFECT_REPRODUCED`;
- `8168fdf3...` -> `INSTALL_RECOVERY_PASS`.

The PASS requires explicit incomplete-install rejection, no synthesized config, and byte-preserved canonical state. Evidence records exact commit/tree/module identity and explicitly sets `assurance_certified:false`, `production_promotion_allowed:false`, and `overall_agentos_green:false`.

Evidence:

- local immutable baseline and repair probes: PASS;
- local PRS Python suite: 210 passed;
- exact-head install-recovery run `35305874628` / #1: SUCCESS;
- exact-head repository run `35305874500` / #166: SUCCESS;
- all twelve other PR #26 adversarial workflows: SUCCESS.

## Exact status

| Item | Status | Evidence boundary |
|---|---|---|
| Symmetric partial-install rejection | TESTED + bounded independently challenged | AgentOS #122 and PRS #26 exact heads |
| SG-08 continuous mutation ownership | BLOCKED | Existing independent false-success evidence remains controlling |
| SG-01/02 canonical actor/grant provenance | BLOCKED | No authenticated transport or canonical grant resolver proven end to end |
| Physical Windows scheduler acceptance | NOT PROVEN | Hosted CI is not owner-laptop evidence |
| Green / completion-grade PRS | NOT ELIGIBLE | Controlling security/runtime gates remain open |
| Overall AgentOS GREEN | NOT CLAIMED | Evidence is intentionally bounded |

## Next executable items

1. Preserve the single active SG-08 repair lane; do not duplicate its ownership primitive.
2. Obtain identical-head Jess and Michael challenge only after SG-08 repair and exact-head Ubuntu/Windows CI.
3. Bind admission only to an evidenced existing authenticated actor source and canonical grant resolver; do not invent either source.
4. Refresh completion-grade PRS only after the AgentOS target changes and independent prerequisites pass.
5. Keep the owner physical Windows checklist on HOLD until software prerequisites are genuinely ready.
6. Review PR #122 and PRS #26 as bounded stacked drafts; do not merge, approve, mark ready, rebase, deploy, or enable production execution from this checkpoint.
