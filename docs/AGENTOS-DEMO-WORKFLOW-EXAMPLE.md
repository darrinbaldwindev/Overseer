# AgentOS Demonstration Workflow Example

## Status
Illustrative workflow specification. This is not evidence that the workflow is currently implemented.

## Scenario
A user asks AgentOS to prepare a small business administrative task involving information from multiple authorised sources and produce a recommendation for user approval.

## Demonstration sequence

### 1 — Request
User states the desired outcome in natural language through first-class AgentOS chat.

**UI state:** PROPOSED

### 2 — Plan
Willow interprets the request, identifies required information, constraints, dependencies and an execution plan.

**UI state:** PROPOSED

### 3 — Intelligence routing
AgentOS determines which available intelligence source(s) are appropriate, based on task requirements, policy, entitlement and available capability.

**UI state:** PROPOSED → APPROVED where required

### 4 — Authorised execution
After required approval, Isla coordinates the permitted actions. Each consequential action remains governed by identity, permission and policy controls.

**UI state:** RUNNING → COMPLETED

### 5 — Challenge
Jack reviews the proposed/resulting work for inconsistencies, missing information, risk or improvement opportunities.

**UI state:** CHALLENGED if an issue is found; otherwise applicable check evidence is recorded.

### 6 — Independent assurance
Henry independently verifies the applicable result/evidence within the defined assurance scope.

**UI state:** ASSURED only when the required assurance evidence exists.

### 7 — Result
AgentOS presents the outcome, evidence, assurance status and any remaining user action.

**Preferred response structure:**
1. What I understood.
2. What was proposed/done.
3. Current status.
4. Evidence/result.
5. Required user action.
6. Optional technical detail.

## Visualisation
The demo should make the workflow legible at a glance:

**Request → Willow plans → Intelligence selected → Isla executes → Jack challenges → Henry assures → Result**

Use explicit status labels rather than relying on character animation or decorative colour alone.

## Safety / claim boundary
This scenario must remain labelled CONCEPT until the underlying capability is demonstrated. Do not manufacture logs, provider calls, approvals, assurance evidence, customer outcomes or integration activity for marketing purposes.

## Acceptance
A visitor can follow the complete workflow without needing to understand AgentOS internals, while an expert can inspect the underlying status/evidence when the Tech Head presentation is shown.
