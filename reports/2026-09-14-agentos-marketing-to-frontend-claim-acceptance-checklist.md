# AgentOS Marketing → Frontend Claim Acceptance Checklist

**Purpose:** keep user-facing AgentOS language synchronized with canonical runtime evidence without Marketing taking over Frontend implementation.

Frontend may use different visual treatment and concise wording, but it should satisfy these truth conditions before a user-facing state is considered Marketing-safe.

## 1. Completion

### Required
- `Finished`, `Complete` or equivalent must be backed by the canonical completion state required by that surface.
- A worker saying it succeeded is not sufficient.
- If verification/Green/PRS is still pending, the UI must preserve that distinction.

### Must not
- generic `VERIFIED` when only execution verification exists;
- `Done and verified` when independent assurance is pending/absent;
- optimistic completion inferred from the absence of an error.

## 2. Green

### Required
- Green state must come from canonical Green evidence for the exact job/build/scope.
- Missing/stale/mismatched Green = unknown/not shown/pending, not PASS.

### Must not
- infer Green from worker success;
- infer Green from normal CI alone;
- use a green colour/icon as a disguised PASS when the assurance state is unknown.

## 3. Henry / PRS

### Required
- Henry/PRS PASS must come from canonical PRS evidence at the applicable exact scope.
- If the current frontend contract does not expose PRS state, say `Not shown`, `Not available here` or equivalent truthful absence.

### Must not
- use Henry as a decorative “all good” mascot;
- synthesize assurance from Green or execution success.

## 4. Stop

### Required
Distinguish where evidence supports it:
- Stop available;
- Stop requested;
- no new actions authorized;
- current action may still finish;
- stopped/effective only after canonical confirmation.

### Must not
- `Stopped` immediately after button press without effectiveness evidence;
- `Stop immediately` unless the runtime actually guarantees immediate termination;
- hide residual in-flight work.

## 5. Pause / Resume

### Required
- explain whether pause prevents new work, pauses scheduling, pauses a mission, or affects an in-flight action;
- resume should describe what scope is being resumed.

### Must not
- imply current execution was interrupted if only future/new work was blocked.

## 6. Revoke authority

### Required
Distinguish:
- revoke requested;
- authority removed for new actions;
- in-flight effects still possible/unknown;
- fully effective/confirmed when evidenced.

### Must not
- present revoke as retroactively undoing completed side effects.

## 7. Permission / Jack

### Required
A meaningful approval should tell the user, when canonical data exists:
- what action/capability is requested;
- what resource/path/account it affects;
- why it is needed;
- whether it is one-time/task/path/persistent;
- meaningful risk/consequence;
- whether external communication, credentials, money or irreversible effects are involved.

If the runtime does not expose enough fields, Frontend should show a bounded generic state or block stronger permission-card claims rather than invent the missing data.

### Must not
- fabricate expiry/duration/reversibility;
- imply a credential will remain invisible unless that property is actually guaranteed;
- collapse user consent and canonical execution authority into one vague `Allowed` state.

## 8. Evidence / What happened

### Required
- evidence shown to a user must be correlated to the same job/task/mission as the status being summarized;
- user-readable summary may simplify canonical evidence but cannot change its meaning;
- missing evidence is explicit.

### Must not
- attach unrelated logs/tests to make the current job look verified;
- call a generic run ID the current task ID without a proven mapping;
- treat a receipt as independent assurance.

## 9. Recovery / crashes

### Required
Distinguish:
- interrupted;
- recovery available;
- recovery required;
- recovered;
- completion re-verified after recovery;
- unable to determine.

### Must not
- `Recovered safely` from restart alone;
- hide abandoned/stale lock or ownership uncertainty;
- imply exactly-once execution unless proven.

## 10. Local / Cloud / Mixed

### Required
- labels must describe actual execution/data path for the job, not account preference or selected model alone;
- Mixed should be used when meaningful work/data crosses local and remote boundaries.

### Must not
- call work `Local` merely because the UI runs locally while a remote model/service processed the content.

## 11. Cost

### Required
Separate where possible:
- estimate;
- authorized budget/ceiling;
- incurred/observed cost;
- unknown/pending cost.

### Must not
- imply `free` when the user is consuming their own subscription/API/compute unless the exact scope is clear;
- turn budget remaining into a guarantee of final cost.

## 12. Stale / missing / conflicting state

### Required
Fail closed into understandable states such as:
- `Unable to confirm status`;
- `Evidence unavailable`;
- `Needs attention`;
- `State changed — refresh required`;
- `Conflicting evidence`.

### Must not
Choose the most reassuring state when canonical sources conflict.

## Simple / Essentials / Tech Head invariant

The three modes may expose different **depth**, not different **truth**.

- **Simple:** plain-language result + next action + important warning.
- **Essentials:** adds authority/evidence/verification/recovery summary.
- **Tech Head:** adds identifiers, exact evidence, provider/runtime/receipt details.

A job that is incomplete in Tech Head cannot appear complete in Simple.

## Current Frontend lineage application

PR #111's current approach is directionally aligned because it:
- uses plain language;
- keeps technical detail available progressively;
- treats Stop as requested rather than instant termination;
- separates completion check from independent assurance;
- refuses to synthesize Henry/PRS;
- fails closed where canonical evidence fields are unavailable.

That is a Marketing truth assessment only. PR #111 remains draft/unmerged and current exact-head CI is AMBER overall; no release claim follows from this checklist.

## Acceptance status

**MARKETING CONTRACT READY / FRONTEND IMPLEMENTATION OWNED BY FRONTEND OVERSEER / RUNTIME TRUTH OWNED BY CANONICAL SYSTEMS / NO OVERALL GREEN.**
