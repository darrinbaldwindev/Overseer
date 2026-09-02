# AgentOS Demonstration Status Model

## Purpose
Prevent marketing, UX and demo surfaces from confusing proposed work, active work, completed work and independently assured outcomes.

## Canonical states

| State | Meaning | User-facing treatment |
|---|---|---|
| PROPOSED | AgentOS has suggested a plan/action but it has not been authorised or executed | Clearly labelled proposal; approval control where required |
| APPROVED | Required user/policy approval has been granted | Show approval and pending execution separately |
| RUNNING | Authorised work is actively executing | Show live/in-progress state; do not present result as complete |
| COMPLETED | Execution finished and a result was produced | Show result and relevant evidence |
| CHALLENGED | Jack/Green Agent identified an issue, uncertainty or improvement opportunity | Explain finding and required resolution; do not mark GREEN |
| ASSURED | Henry/PRS completed the applicable independent assurance check | Show assurance evidence and scope |
| BLOCKED | Work cannot proceed under current permissions, policy, dependency or assurance state | Explain blocker and safe next action |
| FAILED | Execution or validation failed | Explain what failed and what did not change |
| CONCEPT | Capability is a design/marketing concept, not an executed system action | Never style as completed product behavior |

## Rules
- A proposal is never presented as execution.
- Completed does not automatically mean assured.
- Assured does not imply universally production-ready; assurance has a defined scope.
- CHALLENGED, BLOCKED and FAILED states must be visible even in simplified presentation modes when they affect the user's work.
- Character attribution must follow actual recorded workflow events.
- Marketing screenshots and videos must use synthetic data unless authorised real data is explicitly approved.

## Dual assurance
Where a workflow is subject to the AgentOS dual-assurance gate, GREEN requires both applicable Green Agent/Jack and PRS/Henry evidence. An unresolved AMBER or RED state must not be visually represented as GREEN.

## Acceptance
A reviewer should be able to inspect any demonstration and answer: what was proposed, what was authorised, what actually ran, what result was produced, what evidence exists, what was challenged, and whether independent assurance completed.
