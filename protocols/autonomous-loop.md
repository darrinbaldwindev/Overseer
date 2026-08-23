# Overseer Autonomous Operating Loop

## Purpose

Define the repeatable heartbeat used by the Manus Desktop Overseer.

## Loop

```text
WAKE
  ↓
LOAD CONTROL PLANE
  ↓
DISCOVER PORTFOLIO
  ↓
RECOVER STATE
  ↓
CALCULATE PRIORITIES
  ↓
EXECUTE SCANS
  ↓
ANALYSE FINDINGS
  ↓
COMPARE HISTORY
  ↓
CROSS-ANALYSE PORTFOLIO
  ↓
UPDATE STATE
  ↓
GENERATE REPORT
  ↓
VERIFY PERSISTENCE
  ↓
SLEEP / WAIT FOR NEXT TRIGGER
```

## Wake

A cycle may begin from a scheduled run, an owner request, a repository change, a detected failure, or another explicitly authorized trigger.

Record the trigger in the scan manifest.

## Load Control Plane

Load the current charter, configuration, integration contract, scan engine and applicable protocols before acting.

If control-plane files cannot be loaded reliably, do not perform privileged autonomous actions.

## Recover State

Load the previous portfolio registry, repository state, active findings and most recent scan manifest.

If state is missing or corrupted, initialize conservatively and record the limitation.

## Prioritization

Prioritize work using:

1. Critical/high active findings.
2. Security-sensitive changes.
3. Repositories with material changes since the previous scan.
4. Failed or incomplete previous scans.
5. Newly discovered repositories.
6. Regressions.
7. Remaining repositories according to cadence.

Priority must never silently exclude repositories forever. Deferred repositories remain in the queue.

## Scan Execution

Execute the repository scan protocol against each selected repository.

Independent repository scans may be performed concurrently when the runtime permits, but persistence operations for the same state record must remain serialized and auditable.

## Analysis

After individual scans, perform portfolio intelligence analysis.

Systemic findings must link back to their repository-level evidence.

## State Update

Update repository state, finding lifecycle events, portfolio registry and scan manifest.

Never erase historical evidence to make current state cleaner.

## Reporting

The owner-facing report should emphasize:

- what changed;
- what is broken;
- what is risky;
- what improved;
- what remains unresolved;
- what requires owner attention;
- what Overseer will inspect next.

Avoid flooding the owner with unchanged low-value observations.

## Verification

Before completing a cycle, verify that required state and reports were persisted.

A persistence failure is itself a material operational event.

## Next Trigger

The next cycle should be selected based on policy and portfolio state rather than an arbitrary fixed sequence.

Critical findings and material regressions should shorten the next review interval when scheduling capability exists.

## Safety Interlock

The autonomous loop cannot elevate its own authority.

Changing from `observe_report` to a more permissive mode requires an explicit policy change outside the autonomous reasoning loop.
