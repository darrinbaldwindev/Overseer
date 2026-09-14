# AgentOS Competitive Trust / Control Refresh — Batch 3

**Date:** 14 September 2026  
**Scope:** current primary-source trust/control evidence for Zapier, Open Interpreter and Open WebUI; n8n, Cline and Roo remain explicit follow-up UNKNOWNs where this pass did not obtain sufficiently strong primary evidence.

## Executive conclusion
Approval prompts, workspace sandboxing, RBAC, human-in-the-loop gates and tool permissions are increasingly normal agent-platform features. AgentOS should not market any one of these primitives as unique.

The defensible differentiation remains the integrated governed-execution lifecycle:
**explicit authority → bounded execution → durable evidence → recovery/replay discipline → independent Green → independent PRS → understandable result.**

## Zapier
Current Zapier documentation exposes Human in the Loop as a built-in workflow step that can pause execution for approval/decline/change, send review requests, and surface activities in an audit log. Zapier Agents documentation also supports explicit approval steps in agent instructions and account-level owner/editor/viewer roles.

### Competitive implication
- Human approval before continuation is baseline behavior.
- Auditability around approval is not unique on its own.
- Agent collaboration/role permissions are already expected in mature automation platforms.

### AgentOS opportunity
Make authority durable and semantically tied to exact mission/task/capability/evidence identities rather than treating approval as only a workflow pause. Show what authority was granted, what actually executed, what evidence was produced, and whether recovery or independent assurance changed the result.

## Open Interpreter
Current Open Interpreter documentation separates **sandbox mode** from **approval policy**. Documented sandbox postures include read-only, workspace-write and danger-full-access; approval modes include untrusted, on-request and never. Its desktop approval docs describe confirmation for state-changing actions such as file writes, messaging, form submission, deletion, purchases, shell commands and external APIs, with the exact proposed change shown.

### Competitive implication
- Workspace-scoped file access, sandbox posture and sensitive-action approval are table stakes.
- “Ask before the AI changes something” is not sufficient differentiation.
- Local/provider flexibility also overlaps with AgentOS ambitions.

### AgentOS opportunity
Differentiate on durable authority provenance, recovery semantics, duplicate/replay protection, receipts, independent assurance and a clear distinction between `requested`, `executed`, `verified`, `Green`, and `PRS` states.

## Open WebUI
Current Open WebUI documentation exposes RBAC/group permissions and explicitly warns that Workspace Tools/Functions can be root-equivalent because arbitrary Python executes with backend-process access. It supports model-attached tools with user-level access checks. Experimental Tool Permissions can switch from immediate execution to Ask for approval; denied calls are recorded back to the model as errors. Open Terminal provides an isolated Docker shell/filesystem integration.

### Competitive implication
- RBAC, tool access and optional approval are baseline platform controls.
- Extensibility supply-chain risk is a first-class concern; Open WebUI explicitly documents arbitrary-code/plugin risk.
- A generic “supports MCP/tools safely” claim would be weak unless AgentOS demonstrates stronger provenance, publisher trust, permission manifests and runtime isolation.

### AgentOS opportunity
Prioritize the Capability Store / Connector Centre trust model: signed/versioned capabilities, publisher identity, permission manifests, organization allowlists, update/rollback evidence, secrets handles, and clear external/network consequences. AgentOS can differentiate if these controls feed the same authority/evidence/recovery/Green/PRS lifecycle rather than living as disconnected admin settings.

## Comparison snapshot

| Capability | Zapier | Open Interpreter | Open WebUI | AgentOS marketing consequence |
|---|---|---|---|---|
| Human approval | Strong explicit HITL | Strong sensitive-action approval | Optional per-tool approval | baseline |
| Workspace/sandbox boundary | workflow/app scoped | explicit read-only/workspace-write/danger | isolated Open Terminal + RBAC/tool scopes | baseline-to-expected |
| Roles/RBAC | agent collaboration roles | mostly local posture | detailed groups/permissions | baseline |
| Audit/evidence | approval activity/audit | action approval visibility | message/tool denial state + admin controls | AgentOS must go deeper into durable mission evidence |
| Recovery/replay | not established in this pass as AgentOS-equivalent | not established in this pass as AgentOS-equivalent | not established in this pass as AgentOS-equivalent | potential differentiation, must be proven |
| Independent assurance | no Green/PRS equivalent established in this pass | none established | none established | strongest differentiator if real and understandable |
| Supply-chain/plugin risk | app/platform governed | integrations/commands | explicitly high-risk arbitrary code surface | AgentOS should make capability trust visible |

## Claims discipline
Safe internal conclusion:
> Agent platforms increasingly provide permissions, sandboxing and human approval. AgentOS should compete on how those controls connect to evidence, recovery, replay protection and independent assurance—not on the existence of permissions alone.

Do not claim competitors lack recovery, audit, assurance or security features merely because this bounded pass did not find an equivalent. Mark them UNKNOWN unless current primary evidence supports a negative conclusion.

## Remaining Batch 3 research
- n8n: exact current human-approval, credentials, execution history, AI-agent guardrails and enterprise control surfaces.
- Cline: exact current auto-approve/tool/MCP/browser/terminal permissions and audit/recovery model.
- Roo Code: exact current modes/auto-approve/MCP/command controls and recovery model.

These remain **UNKNOWN / TO VERIFY**, not assumed gaps.

## Product recommendations reinforced
1. Restricted Mode / explicit trust posture.
2. Temporary task-scoped authority with expiry/revocation semantics.
3. Durable Evidence Timeline from intent through independent assurance.
4. Credential broker/secret handles so models need not see reusable secrets.
5. Capability/connector provenance and supply-chain controls.
6. Reliable Stop/Revoke state machine, not merely a UI button.
7. Replay/idempotency and recovery evidence visible to ordinary users.

**Marketing status:** research complete for this subset; no public competitor-comparison campaign activated.