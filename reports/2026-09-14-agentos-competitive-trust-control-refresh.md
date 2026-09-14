# AgentOS Competitive Trust / Control Refresh

**Date:** 2026-09-14  
**Owner:** Marketing Overseer  
**Status:** CURRENT RESEARCH / POSITIONING INPUT

## Purpose
Refresh AgentOS differentiation against current agent/developer-tool governance patterns. This is not a feature parity claim. It identifies what is now table stakes, what competitors currently expose, and where AgentOS should copy, adapt, differentiate or ignore.

## Current evidence reviewed

### Cursor
Current Cursor agent-security documentation states that sensitive actions require manual approval by default, code-reading/search generally does not, and agents can modify workspace files without approval except configuration files. Cursor warns that auto-reload may execute agent changes before review. This makes permission boundaries and reversible version-control workflows a current competitive baseline rather than unique AgentOS territory.

### OpenHands
Current OpenHands documentation exposes explicit confirmation policies (`AlwaysConfirm`, `NeverConfirm`, `ConfirmRisky`) and a security analyzer. It also recommends Docker sandbox isolation, while warning that process mode has no isolation and that mounted files can be modified/deleted. OpenHands also provides secrets management, but custom secrets are exposed to the runtime as environment variables. This is strong evidence that sandboxing, risk-based confirmations and secrets handling are active competitive surfaces.

### Microsoft Copilot Studio / Agent 365
Microsoft now frames Agent 365 as a central control plane for observing, governing and securing Copilot Studio agents. Current documentation includes agent identities, Conditional Access, RBAC/ABAC, governance workflows, data policies, connector dependency visibility, audit logging, risk assessment, autonomous-agent governance and publishing controls. Microsoft guidance also explicitly recommends scoped permissions, authentic triggers, human oversight for critical actions, audit logging and staged rollout.

### Claude Code
Current Claude Code CLI documentation exposes allowed/disallowed tool controls, permission modes, directory scoping, a permission-prompt tool and an explicit `--dangerously-skip-permissions` escape hatch. Claude Code also supports gateway patterns for centralized authentication, usage tracking, budgets, audit logs and model routing.

## Strategic conclusion
The following are now clearly insufficient as primary differentiation on their own:
- agent approvals;
- tool allow/deny lists;
- sandboxing;
- local file access;
- terminal execution;
- MCP/tool connectivity;
- audit logging;
- cost controls;
- provider/model routing;
- enterprise data-policy governance.

AgentOS must combine these into a more coherent user-facing trust contract rather than market any one of them as novel.

## COPY / ADAPT / DIFFERENTIATE / IGNORE

### COPY — proven industry patterns worth matching
1. **Risk-tiered approval UX** — OpenHands/Cursor show users expect configurable confirmation, not one approval mode for everything.
2. **Explicit sandbox/local-risk visibility** — OpenHands distinguishes isolated Docker from unsafe host-process execution. AgentOS should make execution boundary obvious.
3. **Admin policy and connector governance** — Microsoft demonstrates the importance of data policies, connector dependency awareness, identity and centralized controls.
4. **Allowed/disallowed tool policy** — Claude Code exposes clear operator controls at tool level.
5. **Budget/usage governance** — gateway and enterprise products increasingly expose spend and usage controls.

### ADAPT — fit to AgentOS architecture
1. **Risk-based confirmations → Jack authority model.** Do not bolt on generic confirmations; express them through canonical authority, mission, tool and scope state.
2. **Sandbox visibility → Local / Cloud / Mixed + Restricted Mode.** Show both where work runs and what that execution boundary allows.
3. **Enterprise connector controls → Connector Centre + Trust Graph.** AgentOS can unify user, device, connector, publisher and capability trust rather than expose scattered settings.
4. **Audit logs → Evidence Timeline.** Convert machine-oriented logs into user-readable proof linked to mission/task/result and verification state.
5. **Secrets management → opaque secret handles.** Prefer architecture where workers do not receive reusable plaintext values unless absolutely required.

### DIFFERENTIATE — strongest defensible direction
1. **Authority + evidence + recovery as one contract.** Competitors commonly expose permission and/or sandbox controls; AgentOS should make completion require evidence and recoverable durable state, not merely execution.
2. **Independent Green then PRS.** Independent verification and adversarial assurance remain more distinctive than execution-instance self-report, provided the implementation actually enforces this.
3. **Replay/duplicate protection as product trust.** Most competitors discuss permissions more visibly than durable exactly-what-happened/replay semantics. AgentOS should surface duplicate/recovery state to users, not hide it in internals.
4. **Provider neutrality under one governance layer.** Routing multiple models/providers is not unique; enforcing the same authority/evidence/recovery contract across them is more valuable.
5. **Human-readable VERIFIED semantics.** “Done” should mean a defined evidence state, not a conversational assertion.
6. **Reliable Stop/Revoke semantics with visible final state.** The value is not merely having a stop button, but making its actual effect auditable and understandable.

### IGNORE — weak differentiation traps
- number of supported models;
- generic MCP support counts;
- raw terminal access;
- broad “computer use” claims;
- local-model support by itself;
- generic command palette parity;
- claiming superiority from having more agents/mascots/tools.

## Product recommendations

### P0 trust/control
- Evidence Timeline bound to canonical mission/task/worker/result IDs.
- explicit Pause / Stop / Revoke state and post-stop outcome.
- Restricted Mode for untrusted content and lower-confidence connectors.
- temporary/scoped authority with visible expiry/revocation.
- opaque credential handles and visibility policy.
- connector/capability trust metadata and publisher provenance.
- device trust and Local/Cloud/Mixed boundary.
- durable recovery/replay state with duplicate-action visibility.

### P1 usability
- permission explanations in plain user language;
- preflight summary: what AgentOS intends to access/change;
- postflight summary: what changed, what failed, what remains unverified;
- searchable permission/settings centre;
- saved governed Jobs/Recipes only after exact permission inheritance rules are proven.

## Marketing implications

### Keep
**Give AgentOS a real job.**  
**Stay in control. See what it did.**

These remain directionally stronger than generic “one interface for many AIs” because they point toward governed execution and evidence.

### Strengthen later, only with proof
Potential future line:
> AgentOS coordinates AI work under explicit authority, records what happened, and separates execution from independent verification.

Do not use as an unqualified current feature statement until the exact marketed scope is proven.

### Avoid
- “the only governed agent platform”;
- “safer than Cursor/OpenHands/Copilot” without comparative evidence;
- “fully verified AI execution”;
- “zero-risk computer control”;
- “unique permission system”.

## Competitive risk
Microsoft is rapidly strengthening enterprise governance and agent identity. Cursor/OpenHands/Claude Code already make permission/sandbox controls visible to technical users. Therefore AgentOS cannot wait for generic governance features alone to create differentiation. The advantage must be the integrated trust loop:

`intent → explicit authority → bounded execution → durable evidence → recovery/replay discipline → Green → PRS → understandable result`

That loop is a product direction until each marketed component is independently evidenced.

## Research limits
This refresh is intentionally evidence-led and non-exhaustive. It prioritizes directly documented trust/control surfaces rather than broad feature/pricing comparison. OpenHands, Cursor, Microsoft and Claude Code evidence was strong enough for this cycle; remaining competitors should be added in later homogeneous refreshes rather than filled with assumptions.