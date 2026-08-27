# GPTChat → GPTChat Overseer Operational Handoff

**Authoritative chain**

**You → GPTChat → GPTChat Overseer → delegated agents → repositories → verification → GPTChat Overseer → GPTChat → You**

## Purpose
This file is the durable handoff contract between GPTChat's portfolio oversight/reporting function and GPTChat Overseer's delegation function.

## GPTChat responsibilities
GPTChat is responsible for:
- portfolio/repository observation and independent analysis;
- health scoring;
- identifying issues, risks, blockers and opportunities;
- distinguishing autonomously fixed items from items requiring owner input;
- recording work actually performed by GPTChat;
- producing actionable recommendations and acceptance criteria;
- logging each report into the Overseer repository;
- updating this handoff when the operating contract materially changes.

GPTChat does **not** become the portfolio task dispatcher merely because it identifies a task.

## GPTChat Overseer responsibilities
GPTChat Overseer is the delegation and coordination layer. It should:
1. consume the latest GPTChat report;
2. convert findings into actionable work items;
3. decompose complex work;
4. select/assign the appropriate agent or project;
5. enforce owner/authority boundaries;
6. track execution and dependencies;
7. require evidence against acceptance criteria;
8. verify completed work before resolving the issue;
9. retry/reassign/fail over when permitted;
10. update shared continuity and action state;
11. return material results/escalations to GPTChat.

## Redundancy / fail-safe protocol
Until AgentOS provides a native event-driven handoff, the following durable mechanisms are required:

### Primary channel
Latest dated report under `reports/` is the authoritative GPTChat portfolio assessment for that cycle.

### Control-state channel
GPTChat Overseer should maintain an actionable state file containing, at minimum:
- report ID/date;
- issue ID;
- priority;
- target repository;
- task/decomposition;
- assigned agent;
- verifier;
- status;
- acceptance criteria;
- evidence location;
- retry/failover state;
- owner decision requirement.

### Recovery channel
If the primary report-to-delegation mechanism is unavailable, GPTChat Overseer should reconstruct pending work from:
- latest report;
- open issues;
- project continuity state;
- this handoff contract;
- repository history.

No single report, agent, or runtime should be the only source required to reconstruct the delegation queue.

## Required task envelope
Every delegated task should carry:
- `source_report`
- `priority`
- `target_repo`
- `objective`
- `acceptance_criteria`
- `executor`
- `verifier`
- `evidence_required`
- `authority_boundary`
- `dependency_ids`
- `fallback_action`

## Verification rule
A task is not considered resolved because an agent says it is resolved. Resolution requires evidence appropriate to the task and, for material work, independent verification.

## Owner escalation
Escalate to the owner only for genuine decision boundaries such as commercial/legal policy, material budget, credentials, production authority, or material architecture decisions. Routine implementation choices should remain autonomous.

## AgentOS migration target
This file is a transitional contract. AgentOS should eventually replace the file-based handoff with a machine-readable event/task protocol while preserving the same separation of responsibilities.

Target flow:

`GPTChat report → event → GPTChat Overseer queue → decomposition → delegation → execution → verification → state update → next eligible task`

Scheduled scans are a safety/reconciliation mechanism, not the primary autonomy mechanism.
