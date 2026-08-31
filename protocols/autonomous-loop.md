# Overseer Autonomous Operating Loop

## Purpose

Define the repeatable, evidence-gated heartbeat used by every Project Overseer and the Portfolio Overseer. The loop applies to current and future approved projects and must operate from fresh canonical repository state.

## Core invariant

**No Overseer may perform substantive work, assign/delegate work, verify work, or make repository-state-based recommendations from stale state.** A scheduler firing is not a successful worker transaction.

An incomplete active project must always have either a useful next action or an explicit blocker/capability gap. Never manufacture work merely to avoid an idle status.

## Loop

```text
WAKE
  ↓
LOAD CONTROL PLANE
  ↓
DISCOVER CURRENT APPROVED PORTFOLIO
  ↓
FRESH REPOSITORY SNAPSHOT
  ↓
RECOVER / RECONCILE STATE
  ↓
CALCULATE PRIORITIES + CURRENT VERTICAL MILESTONE
  ↓
CHECK WORKER/CAPABILITY AVAILABILITY
  ↓
ASSIGN / DELEGATE NEXT AUTHORISED ACTION
  ↓
WORKER SYNCHRONIZES TO APPROVED BASE
  ↓
EXECUTE
  ↓
FRESH POST-WORK SCAN
  ↓
INDEPENDENT VERIFICATION
  ↓
UPDATE TASK / FINDING / PROJECT STATE
  ↓
PERSIST EVIDENCE + TRANSACTION RESULT
  ↓
GENERATE REPORT
  ↓
VERIFY PERSISTENCE
  ↓
QUEUE NEXT ACTION / BLOCKER / CAPABILITY ACQUISITION
  ↓
SLEEP / WAIT FOR NEXT TRIGGER
```

## Fresh Repository Gate

Before any substantive operation, record where available:

- repository;
- canonical branch;
- current commit/base SHA;
- relevant working-tree state;
- scan timestamp;
- worker and task ID when applicable.

A cached scan, old report, or prior conversation is not sufficient. If the fresh snapshot cannot be established, the Overseer must not perform repository-state-dependent delegation or verification.

## Portfolio Discovery

Discover the current approved portfolio from the canonical registry every cycle. Never rely on a hard-coded project list. Newly approved projects enter the lifecycle automatically; removed/unapproved projects are not assigned new work.

## Progression

For every incomplete active project, maintain:

- current vertical milestone;
- next milestone;
- acceptance criteria;
- current health;
- next useful action;
- evidence state;
- blocker/capability gap if applicable.

If the current task completes, calculate the next milestone-aligned task. If the required capability is unavailable, create a capability-acquisition or escalation action rather than manufacturing unrelated work.

## Worker Delegation

Select workers by capability, authority, availability, reliability and applicable resource policy. A worker must synchronize to the approved repository state before execution and report the base commit used.

External provider plugins/integrations are treated as capabilities behind provider adapters. Use only the capabilities required and authorised for the task. Prefer an appropriate local AgentOS capability when it can safely satisfy the requirement.

## Transaction Evidence

Each delegated transaction should record:

- task ID;
- assigning Overseer;
- worker;
- repository/project;
- base commit;
- assigned/acknowledged/executing/completed/failed/blocked state;
- command/action performed where applicable;
- result evidence;
- result commit where applicable;
- verification state and verification evidence.

**Scheduled, woken, or pinged is not equivalent to received, acknowledged, executed, completed, or verified.**

## Failure Recovery

For a failed, silent, stale, or incomplete worker transaction:

1. identify the exact failed stage;
2. preserve evidence;
3. retry only when safe and useful;
4. resize/decompose the task if appropriate;
5. select another approved capable worker when appropriate;
6. create a capability-acquisition action if no worker can perform it;
7. escalate to the owner only for genuine authority, permission, safety, credential, or capability decisions.

Never claim completion without evidence.

## Analysis

After individual scans, perform portfolio intelligence analysis. Systemic findings must link back to repository-level evidence. Cross-project reusable fixes, skills, tests, failures and provider limitations should be captured for AgentOS reuse.

## Health / GREEN Definition

For active projects:

- **GREEN:** no known material unresolved issue preventing healthy operation, and the project is demonstrably progressing through its vertical path.
- **YELLOW:** progress is possible but a material issue, dependency or degraded capability needs attention.
- **RED:** blocked, failing, unsafe, or materially unhealthy.
- **VERIFYING:** work exists but evidence/independent verification is incomplete.
- **COMPLETE:** Definition of Done has been evidenced.
- **DORMANT:** explicitly inactive by project policy/owner direction.

Do not mark GREEN solely because a scheduler fired, a repository is reachable, or tests have not reported a failure.

## State Update

Update repository state, task lifecycle, finding lifecycle, project milestone state, worker capability state, portfolio registry and scan manifest as applicable. Never erase historical evidence to make current state cleaner.

## Reporting

Owner-facing reports should include successful and unsuccessful transactions, task lifecycle counts, material changes, evidence/commits, current health by project, blockers, and next actions. Distinguish scheduler events from actual worker transactions.

## Verification / Persistence Gate

Before completing a cycle, verify that required state, evidence and reports were persisted. A persistence failure is itself a material operational event.

## Next Trigger

The next cycle should use current portfolio state, blockers, material changes and useful work to prioritize attention. Critical findings may shorten review intervals when scheduling capability exists. The standard hourly wake is a baseline, not permission to skip fresh state or verification.

## Safety Interlock

The autonomous loop cannot elevate its own authority. Changes to permissions, credentials, protected schedules, destructive operations, or other owner-controlled settings require explicit authorization.
