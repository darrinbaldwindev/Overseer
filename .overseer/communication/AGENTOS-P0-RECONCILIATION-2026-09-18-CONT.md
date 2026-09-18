# AgentOS P0 Reconciliation — 2026-09-18 continuation

Status: DURABLE RECONCILIATION / NO OVERALL GREEN
Scope: AgentOS Level 2 + PRS assurance freshness

## Fresh exact state

- AgentOS PR #104 remains OPEN / DRAFT / UNMERGED at exact head `607f2683b7d3b234fc6ffa70e2a7d42e31499c3a`.
- PRS PR #17 current head is `1242e077e9f1e0eb7c189539a442b02b83757c18` and records exact-current-head adversarial evidence against AgentOS `607f2683...`.
- PRS exact-current-head project-file probe reproduces the SG-08 false-success defect on normal publish and prepared recovery: target mutation and success receipt can occur before release detects successor displacement. Continuous ownership remains FAIL.
- PRS exact-current-head admission probe reproduces the remote-admission -> local-wake contract gap: canonical admitted non-PowerShell tasks omit `consent_mode`, `acceptance_criteria`, and `target`, while local-wake requires them. Compatibility remains FAIL.
- Authenticated transport and canonical grant-source provenance remain NOT PROVEN end to end.
- Physical owner-Windows scheduler/local-wake acceptance remains NOT PROVEN.

## Install-recovery side lane

- AgentOS PR #122 is OPEN / DRAFT / UNMERGED at current head `bec3cbc8e2cc0f157365cbb78bcfd09a57a61fe0`.
- Exact-head AgentOS Tests run `35313309829` completed SUCCESS for `bec3cbc8...`.
- PRS PR #26 is OPEN / DRAFT / UNMERGED at current head `669617266b9183c3b25ac1b674b66a83d2f76628`.
- PRS workflow `Validate AgentOS install recovery` run `35305874628` completed SUCCESS, but its exact repair target was the older AgentOS #122 head `8168fdf310041a083bf993d24664bb9a940714ad`, not current `bec3cbc8...`.
- Therefore the install-recovery repair has current exact-head functional CI, but independent PRS repair evidence does NOT transfer from `8168fdf...` to `bec3cbc8...` without a fresh exact-current-head challenge.

## Reconciled dispositions

- SG-08 continuous ownership: BLOCKED / defect reproduced on exact current #104.
- SG-01/02 authenticated actor + canonical grant provenance: BLOCKED / not proven end to end.
- admission -> local-wake compatibility: BLOCKED / defect reproduced on exact current #104.
- #122 install-recovery functional repair: VERIFYING / exact-head AgentOS CI PASS.
- #122 independent install-recovery assurance: PENDING fresh exact-head PRS challenge on `bec3cbc8...`.
- physical Windows acceptance: BLOCKED_STABLE / owner-gated and upstream defects unresolved.
- completion-grade Green/PRS: NOT ELIGIBLE while the above controlling failures remain.

## Next safe actions

1. Keep the SG-08 repair single-threaded on existing #104 lineage; do not invent another ownership system.
2. Repair admission/local-wake only from a canonical source for consent, acceptance criteria and target; do not synthesize defaults.
3. Refresh PRS #26 against current #122 head `bec3cbc8...` before treating install-recovery assurance as current.
4. After any #104 mutation: exact-head Ubuntu+Windows CI -> independent unchanged-head functional/security challenge -> PRS only if preceding gates pass.
5. Keep physical Windows acceptance separate until upstream runtime defects are cleared.

## Governance

No merge, approve, ready transition, rebase, deploy, credentials/security-policy mutation, production writes/autonomy, unrestricted PowerShell, physical-host action or overall GREEN is authorized or claimed by this reconciliation.
