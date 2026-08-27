# Portfolio Scheduler — Autonomy-First Specification

## Objective
Improve autonomy across the entire repository portfolio without relying on fixed daily polling as the primary mechanism.

## Scheduling layers
1. **Event-driven:** newly logged report, new issue/PR, failed verification, dependency completion, stalled task, health regression.
2. **Condition watches:** monitor critical P0/P1 conditions and wake the delegation layer when action is warranted.
3. **Adaptive reconciliation:** frequent lightweight control-plane checks; deeper scans based on risk, activity and stale state.
4. **Daily portfolio audit:** complete health/dependency/continuity reconciliation and report generation.
5. **Weekly strategic review:** portfolio priorities, project sequencing, capability reuse and technical debt.

## Priority policy
- P0: immediate action when safe and authorised.
- P1: next available execution slot.
- P2: batch with related work where practical.
- P3: opportunistic/background.
- Owner decision: pause affected branch and present choices with GPTChat Repo Overseer recommendation.

## Adaptive frequency
Increase monitoring when:
- health score falls;
- a P0/P1 issue appears;
- delegated work stalls or repeatedly fails;
- dependencies change;
- a repository has rapid recent activity;
- a release/launch milestone is near.

Decrease monitoring when a project is stable, inactive and has no pending dependencies, while preserving daily reconciliation.

## Scheduling objective
Optimise for **unblocking portfolio progress**, not number of tasks executed. Prefer work that:
- removes a P0/P1 blocker;
- unblocks multiple projects;
- creates reusable AgentOS capability;
- reduces recurring manual intervention;
- improves verification/reliability.

## Concurrency and safety
- Do not execute conflicting tasks concurrently.
- Respect repository/project dependencies.
- Limit autonomous work by authority boundary.
- Require verification evidence before resolving material tasks.
- Preserve idempotency across retries and restarts.

## Failure handling
On failed execution:
1. record failure evidence;
2. retry only if policy permits;
3. otherwise choose an alternative capable executor;
4. increase verification scrutiny after repeated failure;
5. escalate only when the authority boundary or repeated failure requires it.

## Redundancy
The scheduler must be reconstructible from durable reports, action state, repository issues, continuity records and this specification. A runtime outage must not erase the queue.

## AgentOS target
This specification is intentionally provider/model agnostic. AgentOS should eventually implement it as a native scheduler/event bus with persistent task state, dependency graph, executor registry, verifier registry, policy engine and adaptive wake-up logic.

## Initial rollout
Start with the Overseer repository as the proving ground. Do not claim event-driven autonomy until an end-to-end test demonstrates event/report → task → delegation → execution → verification → state update and restart recovery.
