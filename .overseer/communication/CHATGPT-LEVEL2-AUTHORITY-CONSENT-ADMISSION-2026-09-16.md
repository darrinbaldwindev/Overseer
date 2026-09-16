# AgentOS Level 2 Authority / Consent / Admission Reconciliation

**Scan date:** 2026-09-16 (fresh live GitHub scan)

**Scope:** `darrinbaldwindev/AgentOS`, `darrinbaldwindev/Overseer`, Overseer issue #49, the current maximum batch, and AgentOS PRs #104, #112, and #121. This was a read-only reconciliation. No repository code, branches, PRs, issues, credentials, schedules, deployments, physical hosts, or production systems were changed.

## Executive conclusion

The Level 2 authority/consent/admission path is **not ready for promotion or runtime enablement**. The fresh scan confirms that the active work remains split across three open draft PRs and that the controlling blocker is semantic rather than mechanical: the current remote admission path can validate an authority/grant-shaped input but does not provide a canonical source for `consent_mode`, while the existing local-wake envelope requires `PRE_AUTHORIZED` for the relevant non-PowerShell execution path. PR #121 documents that `target` and `acceptance_criteria` have canonical dispatch provenance, but `consent_mode` provenance is still unknown/blocking. Copying fixture defaults into admission would manufacture governance evidence and is prohibited.

The safe disposition is **BLOCKED_STABLE / OWNER DECISION REQUIRED for canonical consent provenance**. PR #112 remains an independently scoped runtime-shell capability-evaluation lineage; PR #104 remains the Windows/remote-bridge lineage and is not runtime-enabled or physical-Windows-proven. No new authority source, consent source, scheduler, queue, adapter/control plane, or mutation path should be created to bridge the gap.

## Fresh exact-head state

| Item | Current exact revision | State | Fresh checks | Interpretation |
|---|---|---|---|---|
| AgentOS `main` | `962cb3820b83506f9e6d90f50e003690dd85a8a1` | branch head | Repository API read | Current comparison baseline |
| AgentOS PR #104 | `86005652d7454c0be4862d49846bd5bccc1daec7` | OPEN / DRAFT / `clean` | `test` success on runs `34596812506` and `34596806294` | Bounded Windows/remote-bridge lineage; not merged or runtime-enabled |
| AgentOS PR #112 | `33eca1d257179a873a8aca2eea1a4e5e994415a0` | OPEN / DRAFT / `clean` | `test` and `wake` success on runs `34849679095` and `34849679000` plus related exact-head checks | Bounded runtime-shell/capability consolidation; no authority widening |
| AgentOS PR #121 | `fd616b27c58264c2ebe873b546f85779ceeab8c0` | OPEN / DRAFT / `unstable` | Later exact-head `test` success on Ubuntu 22 and Windows 26 in run `35047237300`; earlier run `35047234103` had Ubuntu failure and Windows success | Documentation/evidence-only probe; do not infer production repair or merge readiness |
| Overseer `main` | `5f6bf8542870ffe99b6bcf95cfbb8650a6b323d4` | branch head | Repository API read | Current coordination baseline |
| Overseer issue #49 | current issue record | OPEN | Issue API read | Level 2 remains P0/immediate priority |

**Evidence limitation:** GitHub check runs establish CI results for the named revisions; they do not establish authenticated transport provenance, canonical consent provenance, physical Windows execution, Green, PRS, security approval, or release readiness.

## Evidence classification

### Verified facts

1. The current heads above are fresh API results and supersede historical SHAs in the maximum batch and older PR comments.
2. PR #104 currently changes the Windows PowerShell worker, remote authority admission, local wake, persistence, receipt, recovery, claim, and project-file governance seams. Its current head has successful visible `test` checks, but the PR remains draft/open/unmerged.
3. PR #112 currently changes `runtime/runtime-shell.mjs`, `runtime/shell-contract.mjs`, capability contracts, local wake, boot, tests, and coordination documents. Its current head has successful visible `test` and `wake` checks and remains draft/open/unmerged.
4. PR #121 adds only `docs/server/ADMISSION-WAKE-COMPAT-PROBE-2026-09-16.md` at its current head. Its document records a reproduced admission-to-local-wake contract mismatch and explicitly keeps the branch evidence-only.
5. The PR #121 evidence document identifies `target` and `acceptance_criteria` as source-authored canonical dispatch semantics from `.agentos/dispatch/schema.md` and durable task fixtures, while stating that current remote admission does not preserve them.
6. The same evidence document states that no equivalent canonical `consent_mode` source was evidenced. The remote bridge deliberately excludes untrusted remote consent input, and local wake requires `PRE_AUTHORIZED` for the affected path.
7. The required safe repair boundary is to preserve source-authored target and acceptance criteria, bind consent only from an explicit canonical source, preserve correlation, add deterministic negative tests, and prove no worker/process side effect on denied inputs.
8. The current coordination records classify PR #104's SG-08 continuous ownership and SG-01/02 authenticated actor plus canonical grant provenance as stable blockers; PR #112 is an independent bounded runtime-shell lineage rather than a source of authority.

### Contributor/owner claims, not independently promoted

- PR review and coordination comments describe earlier bounded-green or exact-head closures for selected tests and capability-evidence repairs. These are accepted as claims only to the extent directly corroborated by the current check-run metadata above.
- Historical comments cite older PR #104 and #112 heads, including `59aa2fc`, `83a58b8...`, `832847f...`, and other predecessor revisions. Those are not current authority for this scan.
- PR cleanliness (`clean`) is a merge-state property, not proof of authorization, security, runtime readiness, or Level 2 completion.

### Unknown or blocking facts

- No canonical authenticated actor/session source was independently evidenced for the remote transport boundary.
- No durable canonical `resolveGrant` authority source was independently evidenced on the canonical runtime path.
- No canonical consent authority/source was evidenced that can legitimately produce `consent_mode = PRE_AUTHORIZED` for the affected task class.
- Physical Windows execution, host pickup, and runtime enablement remain unproven.
- Continuous SG-08 ownership through final verification, side effect or prepared recovery, durable success receipt, and release remains unresolved.
- Independent Jess/Michael/PRS evidence on an unchanged candidate is not established by these repository/API checks.

## Reconciled authority / consent / admission path

The intended path remains:

`remote request/candidate -> authenticated actor -> canonical grant -> admitted task -> existing scheduler/local wake -> canonical worker -> bounded operation -> durable result/receipt -> independent verification`

The fresh evidence supports the following boundaries:

| Seam | Fresh disposition | Why |
|---|---|---|
| Remote candidate supplies actor/issuer/grant | **FAIL CLOSED** | Untrusted candidate data must not establish its own authority provenance. |
| Authenticated actor source | **BLOCKED** | A real canonical transport/session authenticator was not evidenced. |
| Canonical grant resolver | **BLOCKED** | Existing admission is a consumer/composition seam; no independent canonical resolver source was evidenced. |
| `target` | **PRESERVE SOURCE-AUTHORED** | Canonical dispatch schema and fixtures evidence its ownership; admission currently drops it. |
| `acceptance_criteria` | **PRESERVE SOURCE-AUTHORED** | Canonical dispatch schema and fixtures evidence its ownership; admission currently drops it. |
| `consent_mode` | **BLOCKED / UNKNOWN** | Local wake requires `PRE_AUTHORIZED`, but no canonical source permits deriving it from a grant, issuer, or authentication alone. |
| Capability evidence | **BOUNDED** | PR #112 consolidates canonical capability evaluation and rejects contradictory recognized evidence; this does not grant authority or consent. |
| Task/mission/wake/worker/result correlation | **MUST REMAIN EXACT** | Existing receipt and local-wake paths carry correlation fields, but current evidence does not authorize claiming end-to-end authenticated-authority-to-receipt provenance. |
| Replay/idempotency/concurrent ownership | **UNRESOLVED** | Existing PR work adds bounded stores/receipts/tests, but SG-08 and complete replay/crash proof remain gated. |

## Disposition by active lineage

### PR #104 — Windows / remote bridge

**Disposition:** `ACTIVE — DO NOT COMPETE; BLOCKED_STABLE on adjacent authority/runtime prerequisites.`

The current exact head is `86005652d7454c0be4862d49846bd5bccc1daec7`. Visible exact-head checks are successful, and the PR remains draft/open/unmerged. Its changed-file set includes bounded PowerShell execution, host/worker seams, remote admission, local wake, claim/recovery, persistence, receipt, and project-file governance. The current evidence does not show runtime pickup enabled or physical Windows execution. Because the active lineage already owns adjacent work and the canonical actor/grant and SG-08 prerequisites remain unresolved, this scan does not alter #104.

### PR #112 — Runtime-shell consolidation

**Disposition:** `ACTIVE — INDEPENDENT BOUNDED LINEAGE; NO AUTHORITY PROMOTION.`

The current exact head is `33eca1d257179a873a8aca2eea1a4e5e994415a0`. The visible exact-head `test` and `wake` checks succeed. The changed scope consolidates capability evaluation and shell-contract extraction and includes homogeneous tests. This is useful evidence for fail-closed capability handling, but it cannot be used as an authenticated actor source, canonical grant resolver, consent source, scheduler, or admission authority.

### PR #121 — Server admission/wake compatibility probe

**Disposition:** `EVIDENCE-ONLY; BLOCKED_STABLE.`

The current exact head is `fd616b27c58264c2ebe873b546f85779ceeab8c0`. It adds one documentation probe. The probe's exact-head later run shows Ubuntu and Windows success, but the PR is still reported as `unstable` because an earlier run had an Ubuntu failure and because a documentation check is not runtime evidence. The reproduced mismatch is material and should remain visible: mechanically populating missing fields from local-wake defaults would manufacture governance evidence.

## Owner decision required

1. **Identify or explicitly authorize the canonical consent evidence source** that can legitimately bind `consent_mode = PRE_AUTHORIZED` for the affected task class. This decision must identify ownership, provenance, scope, freshness/replay semantics, and the exact existing interface; it must not create a parallel authority plane.
2. **Identify the canonical authenticated actor/session source and grant resolver** for remote admission, or explicitly keep SG-01/02 blocked until an existing owner-controlled source is available.
3. **Decide the canonical ownership point** for preserving source-authored `target` and `acceptance_criteria` across request composition, admission, persistence, and local wake.
4. **Keep runtime enablement and physical Windows acceptance gated** until the above evidence, SG-08 continuous ownership, exact correlation, and independent Green/PRS controls are satisfied.

## Safe next steps, in priority order

1. Map the existing AgentOS authority/governance contracts to locate a real canonical consent source; do not implement a substitute.
2. Map the existing transport authentication/session and `resolveGrant` primitives; record exact files/interfaces or retain `BLOCKED_STABLE` if absent.
3. Define the single canonical preservation point for source-authored `target` and `acceptance_criteria`, with no authority semantics added by those fields.
4. Add only deterministic normalization/admission negatives for missing, malformed, conflicting, or source-mismatched target/criteria/consent once the canonical source contract is established.
5. Prove denied inputs invoke no worker/process and cannot create success receipts; preserve exact request/delivery/project/mission/task/wake/host/worker/code/actor/authority correlation.
6. Reconcile PR #112 capability evidence independently; do not transfer its bounded test result into authority, consent, physical-worker, Green, or PRS status.
7. Re-scan PR #104 only for changed SG-08 or actor/grant evidence; do not recertify unchanged claims or compete with its active mutation lineage.
8. Obtain independent Jess/Michael/PRS evidence on the exact unchanged candidate before any completion or promotion claim.

## Explicit non-actions and safety boundary

No merge, approval, ready transition, rebase, deploy, credential/security-policy change, production write, physical Windows action, unrestricted shell/elevation, runtime enablement, new scheduler/queue/authority/persistence plane, or Green/PRS/security/release certification was performed or implied.

A documentation probe, repository scan, clean merge state, successful CI run, synthetic fixture, or receipt schema is **not proof of runtime readiness, authorization, security, production safety, or Level 2 completion**.

## Primary sources

- [Overseer issue #49 — Portfolio Mission / AgentOS Work-Style Capability Ladder](https://github.com/darrinbaldwindev/Overseer/issues/49)
- [Existing maximum batch](https://github.com/darrinbaldwindev/Overseer/blob/main/.overseer/batches/MANUS-MAXIMUM-VERTICAL-BATCH-2026-09-16.md)
- [AgentOS PR #104](https://github.com/darrinbaldwindev/AgentOS/pull/104) — current head `86005652d7454c0be4862d49846bd5bccc1daec7`
- [AgentOS PR #112](https://github.com/darrinbaldwindev/AgentOS/pull/112) — current head `33eca1d257179a873a8aca2eea1a4e5e994415a0`
- [AgentOS PR #121](https://github.com/darrinbaldwindev/AgentOS/pull/121) — current head `fd616b27c58264c2ebe873b546f85779ceeab8c0`
- [PR #121 exact evidence document](https://github.com/darrinbaldwindev/AgentOS/blob/fd616b27c58264c2ebe873b546f85779ceeab8c0/docs/server/ADMISSION-WAKE-COMPAT-PROBE-2026-09-16.md)
- [AgentOS current main](https://github.com/darrinbaldwindev/AgentOS/tree/962cb3820b83506f9e6d90f50e003690dd85a8a1)
- [Overseer current main](https://github.com/darrinbaldwindev/Overseer/tree/5f6bf8542870ffe99b6bcf95cfbb8650a6b323d4)

---

**Handoff status:** `BLOCKED_STABLE / OWNER DECISION REQUIRED` for canonical consent provenance; no executor-ready production/runtime mutation is authorized by current evidence.
