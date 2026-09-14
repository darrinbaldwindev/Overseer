# AgentOS — Evidence Timeline + Pause / Stop / Revoke Language Contract

**Date:** 2026-09-14 AEST  
**Owner:** Marketing Overseer  
**Status:** PRODUCT/MARKETING CONTRACT / IMPLEMENTATION NOT CLAIMED

## Purpose
Define user-facing state language that cannot outrun technical truth. This contract is designed for Simple, Essentials and Tech Head views and is subordinate to canonical runtime/Green/PRS evidence.

## Principle
A control request is not the same thing as an effective control result. An execution result is not the same thing as verification. Marketing/UI copy must preserve those distinctions.

# Evidence Timeline taxonomy

## INTENT RECEIVED
User has stated a goal. No authority or execution implied.

Suggested copy:
- “Job received.”
- “AgentOS is preparing the plan and required access.”

Never say: “Job started” before admission/authority allows it.

## PLAN PREPARED
Planned actions/scopes are known.

Suggested copy:
- “Plan ready for review.”
- “These are the files, tools and actions AgentOS expects to use.”

## AUTHORITY CHECK
Canonical permissions/consent/policy are being evaluated.

Suggested copy:
- “Checking authority.”

## APPROVAL REQUIRED
Execution is blocked pending explicit user/authority approval.

Suggested copy:
- “Approval required before this action can run.”

## APPROVED
Approval exists for the exact represented scope.

Suggested copy:
- “Approved for this action and scope.”

Never say “fully authorised” if the approval is task/tool/path bounded.

## DENIED / BLOCKED
Action did not receive sufficient authority or policy clearance.

Suggested copy:
- “Blocked. This action was not authorised.”
- “No execution occurred for this denied action.” only when evidence proves zero invocation.

## EXECUTION STARTED
Worker invocation began.

Suggested copy:
- “Action started.”

Do not imply success.

## EXECUTION RESULT RECEIVED
Worker returned result/evidence.

Suggested copy:
- “Result received.”

Do not say “verified” or “completed” yet.

## RECEIPT PERSISTED
Durable receipt exists.

Suggested copy:
- “Execution receipt recorded.”

## VERIFICATION IN PROGRESS
Result is being checked against required evidence.

Suggested copy:
- “Checking the result.”

## VERIFIED
Use only when the canonical verification contract for that action is satisfied.

Suggested copy:
- “Verified for this task and result.”

Never imply independent Green/PRS if those stages have not occurred.

## GREEN REVIEW
Independent Green review is pending/running/complete.

Suggested copy:
- “Independent verification review in progress.”

If Green FAIL:
- “Independent review did not pass. This job is not cleared as complete.”

## PRS REVIEW
Independent adversarial assurance is pending/running/complete.

Suggested copy:
- “Independent assurance review in progress.”

If PRS FAIL:
- “Assurance did not pass. The result remains held.”

## COMPLETE
Only use when the job’s defined completion contract is satisfied.

Suggested copy:
- “Job complete for the agreed scope.”

Avoid generic “Done” when partial/held/unknown state exists.

## PARTIAL
Suggested copy:
- “Part of the job completed. These items remain unfinished or unverified.”

## RECOVERY REQUIRED
Suggested copy:
- “Work was interrupted. AgentOS has recovery information, but the job is not yet complete.”

## RECOVERED
Use only after state/result evidence proves safe recovery.

Suggested copy:
- “Recovered and reconciled. Review the evidence before continuing.”

## UNKNOWN
Suggested copy:
- “AgentOS does not have enough evidence to determine the final state.”

UNKNOWN must never be cosmetically converted to “probably complete”.

# Pause contract

## PAUSE REQUESTED
User requested pause; effect not yet proven.

Copy: “Pause requested.”

## PAUSE ACKNOWLEDGED
Control plane received/accepted request.

Copy: “Pause acknowledged. Checking active work.”

## PAUSED
Use only when new scheduled/admitted work is prevented according to the proven pause contract and the state of in-flight work is known.

Copy: “Paused. No new work will start under this job. Review in-flight status below.”

Do not say “everything has stopped” unless that is actually proven.

# Stop contract

## STOP REQUESTED
Copy: “Stop requested.”

## STOP ACKNOWLEDGED
Copy: “Stop acknowledged. AgentOS is preventing further eligible work and reconciling anything already in flight.”

## STOP EFFECTIVE
Use only when the runtime contract proves the represented effect.

Copy: “Stop is effective for new work. In-flight outcome: [state].”

Possible in-flight states:
- none active
- completed before stop took effect
- terminated and reconciled
- still resolving
- unknown — investigate

Never use “stopped instantly” unless exact evidence supports it.

# Revoke contract

## REVOKE REQUESTED
Copy: “Access revocation requested.”

## REVOKED FOR NEW ACTIONS
Copy: “Authority revoked for new actions in this scope.”

## IN-FLIGHT AUTHORITY STATUS
Must be separately represented:
- no in-flight work
- in-flight work also invalidated/terminated (only if proven)
- in-flight work retains prior grant until bounded completion (if that is the actual contract)
- unresolved/unknown

Do not imply revocation retroactively undoes side effects already completed.

# Simple / Essentials / Tech Head presentation

## Simple
Show one plain-language state plus strongest material qualifier.
Example: “Stopped for new work. One action is still being reconciled.”

## Essentials
Show state, scope, current action, verification status and next user decision.

## Tech Head
Expose canonical IDs/evidence pointers, timestamps, authority source, receipts, verification, Green/PRS state, recovery/replay details and exact residual UNKNOWNs.

All three modes must reflect the same canonical state; they differ only in detail, not truth.

# Marketing claim constraints
Until exact technical proof exists, do not say:
- “Stop instantly kills every task.”
- “Revoke immediately removes every in-flight permission.”
- “Verified means independently assured.”
- “Every AgentOS action is independently verified.”
- “Recovery guarantees no duplicate side effects.”

Safe present directional wording:
> AgentOS is being designed so authority, execution, evidence and verification are distinct, visible states rather than a single conversational “done”.

# Acceptance criteria for product implementation
1. every visible timeline state maps to one canonical runtime/evidence condition;
2. UI cannot set `VERIFIED`, Green or PRS state itself;
3. pause/stop/revoke requested and effective states are separate;
4. in-flight residual state remains visible after stop/revoke;
5. UNKNOWN is first-class and cannot be hidden by optimistic copy;
6. Simple/Essentials/Tech Head views render the same truth;
7. receipts/evidence are inspectable from user-visible state where appropriate;
8. failure/recovery never silently returns to COMPLETE without the required verification path.

**Current implementation status:** NOT ASSERTED BY THIS DOCUMENT.