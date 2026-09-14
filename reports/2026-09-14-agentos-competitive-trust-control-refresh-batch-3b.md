# AgentOS Competitive Trust/Control Refresh — Batch 3B

**Date:** 2026-09-14 Brisbane  
**Owner:** Marketing Overseer  
**Status:** EVIDENCE REVIEW / POSITIONING INPUT

## Scope
Current primary-source review of n8n and Cline. Roo Code remains explicit TO VERIFY because no sufficiently reliable current primary documentation was retrieved in this pass.

## n8n
Current n8n documentation shows:
- Human-in-the-loop approval can pause AI Agent tool calls before execution.
- Workflows have role/permission controls and project sharing boundaries.
- Credential use is separated from credential editing; unshared credentials can constrain node editing.
- Enterprise-oriented features include SSO, external secrets, environments, log streaming and security controls.

Marketing consequence: workflow permissions, human approval, project roles and secret-management boundaries are established market patterns. AgentOS should not present those primitives alone as unique.

## Cline
Current Cline documentation shows:
- per-tool Auto Approve categories for project/all-file reads/edits, terminal commands, browser and MCP;
- explicit distinction between safe commands and commands requiring approval;
- a YOLO mode that disables normal approval friction and is explicitly described as risky;
- checkpoint snapshots for file/command changes with restore capability;
- SDK tool policies that can disable tools or require/skip approval;
- CLI/headless autonomous execution and isolated data directories;
- command-permission restriction examples for CI.

Marketing consequence: granular permission UX, autonomous mode, rollback/checkpoints and command restrictions are already real competitor capabilities. AgentOS cannot win by saying only “you stay in control.” It needs to prove the full semantics behind that phrase.

## Roo Code
**TO VERIFY / UNKNOWN IN THIS PASS.**

Do not infer that Roo lacks or has specific approval, recovery, MCP, sandbox, checkpoint or secret controls until current primary evidence is retrieved.

## Positioning impact
Further demote as standalone differentiators:
- approval prompts;
- per-tool permission categories;
- human-in-the-loop workflow pauses;
- workspace/project scoping;
- rollback/checkpoint UX;
- MCP access controls;
- RBAC and enterprise identity controls.

Keep AgentOS emphasis on the integrated lifecycle:

**explicit authority → bounded execution → durable evidence → failure/recovery semantics → replay/duplicate discipline → independent Green → independent PRS → understandable result**

The differentiator is not that each primitive exists. It is whether the complete user-visible system maintains one coherent truth through them.

## Frontend implication
Frontend should make the following distinctions legible without requiring technical knowledge:
- allowed vs requested vs effective authority;
- action attempted vs action completed;
- Stop requested vs execution actually stopped;
- completion vs Green vs PRS;
- recovered vs retried vs duplicated;
- local vs cloud vs mixed;
- capability enabled vs trusted/publisher-assured.

## Claim discipline
Safe direction:
> AgentOS is being built to put one governed control and evidence layer around AI work, rather than treating approval prompts as the end of the safety problem.

Do not claim competitors lack permissions, approval, recovery or enterprise controls.

## Next research
- retrieve Roo Code current primary documentation;
- compare concrete evidence/history/receipt semantics across Cline/Roo/n8n;
- compare interruption/recovery and duplicate/replay behavior where publicly documented;
- compare capability/plugin/MCP publisher and supply-chain controls.

**No public comparative superiority claim is authorised by this report.**