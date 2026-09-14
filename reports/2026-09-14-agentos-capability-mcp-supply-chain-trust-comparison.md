# AgentOS — Capability / MCP Supply-Chain Trust Comparison

**Date:** 2026-09-14 Brisbane
**Owner:** Marketing Overseer
**Status:** CURRENT PRIMARY-EVIDENCE COMPARISON / NO PRODUCT CLAIM PROMOTION

## Purpose
Test whether AgentOS can credibly differentiate on capability/plugin/MCP trust rather than merely supporting more tools.

## Market evidence reviewed
### n8n
Current n8n evidence shows a distinction between verified and unverified community nodes. Verified community nodes are surfaced in-product and have undergone n8n vetting; workspace-owner controls apply to installation. Unverified community nodes are not available in n8n Cloud and require self-hosting. n8n has also published security advisories and maintains explicit controls around community-node risk.

### Roo Code
Current Roo documentation shows:
- MCP server configuration at global or project scope;
- MCP tool existence/schema validation;
- default approval before MCP tool execution;
- per-tool `always allow` behavior;
- server enable/disable controls;
- configurable timeouts;
- command allowlists and mode-specific tool permissions;
- checkpoint/undo behavior.

This is meaningful runtime control, but configuration-origin trust and publisher identity are separate questions from tool approval.

### Cline / other coding agents
Recent competitive work already established granular tool auto-approval, checkpoints/restore and risky bypass modes. These make `approval + rollback` baseline-class, not sufficient differentiation.

## Comparison dimensions

| Trust dimension | Market baseline observed | AgentOS opportunity / requirement |
|---|---|---|
| Publisher identity | Partial: verified-node programs exist in n8n; many MCP ecosystems remain config/package based | expose who published/provided a capability and how that identity was established |
| Installation authority | owner/admin controls common | Jack should make install/enable authority explicit and scoped |
| Tool approval | common | approval alone is table stakes; bind approval to exact authority + capability + scope + duration |
| Per-tool allowlist | common in Roo/Cline-style systems | preserve but surface risk tier and consequences |
| Version visibility | package/config ecosystems expose versions variably | make capability version first-class in evidence and rollback |
| Signed artifacts | not consistently surfaced in user-facing competitor docs reviewed | strong opportunity if implemented and evidenced; do not claim yet |
| Verified publisher programme | n8n has a clear verified-node model | adapt into governed Capability Store / publisher trust rather than copy marketplace quantity |
| Update review | uneven | require material permission/risk diff before trusted capability updates |
| Rollback | checkpoints common for workspace edits; plugin rollback varies | capability update rollback should be explicit and evidence-backed |
| Tool origin visibility | MCP/server names often visible | AgentOS should show provider/publisher/server origin in Evidence Timeline and permission UI |
| Secret handling | varies; competitors expose env/credential stores | prefer opaque secret handles and disclose whether capability receives value, handle or delegated token |
| Network/data egress | often implicit in tool/server config | Jack should surface external destination/data class before authority grant where material |
| Workspace/local scope | common | not unique; connect scope to durable evidence and revocation semantics |
| Disable/revoke | enable/disable controls common | differentiate through reliable future-action revoke + truthful in-flight state |
| Audit/evidence | logs exist widely | user-readable evidence of exact capability/version/authority/result/recovery is the stronger opportunity |
| Independent assurance | uncommon in reviewed consumer/developer UX | Green then PRS remains a meaningful intended differentiator if implemented and independently evidenced |

## Product recommendation
Do **not** market a future AgentOS Capability Store as `more plugins` or `MCP marketplace`.

If built, the stronger contract is:
> **Know who made the capability, what version is running, what it can access, what authority it has, what changed, and how to disable or roll it back.**

## Recommended minimum capability trust record
A future canonical capability record should be able to project, without becoming a duplicate authority source:
- stable capability ID;
- publisher/provider identity;
- version + digest/signature status where available;
- install source;
- requested capabilities/permissions;
- approved scope;
- local/cloud/remote execution context;
- network/data-egress class;
- secret-access mode;
- risk tier;
- installed/enabled state;
- update available + permission/risk delta;
- rollback target;
- last-used evidence pointer;
- revoke/disable state;
- assurance state pointers where applicable.

## UI implications
Frontend should eventually distinguish:
- **Verified publisher** from merely `installed`;
- **trusted for this scope** from globally trusted;
- **auto-approved** from intrinsically safe;
- **disabled for new actions** from in-flight action terminated;
- **updated** from `same authority/risk as before`;
- **local capability** from remote service receiving data.

## Claim discipline
Currently supportable:
- competitors increasingly provide tool permissions, allowlists, checkpoints and verified-extension mechanisms;
- these are baseline-class controls rather than unique AgentOS differentiation.

Product direction only:
- signed/versioned AgentOS capabilities;
- governed Capability Store;
- publisher verification;
- capability trust graph;
- update permission-diff review;
- opaque secret handles across all capability types.

Do not present those future controls as implemented until repository/runtime evidence exists.

## Strategic conclusion
The capability ecosystem can strengthen AgentOS only if it extends the same trust contract as the runtime: **identity → authority → bounded execution → evidence → recovery/rollback → independent assurance**. Quantity of plugins or MCP servers is not the moat.