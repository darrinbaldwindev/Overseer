# AgentOS Competitive Trust / Control Refresh — Batch 2

**Date:** 14 September 2026  
**Marketing purpose:** identify which trust/control ideas are already becoming market baseline and where AgentOS still has a defensible product story.  
**Evidence rule:** current public product documentation only; absence of evidence is recorded as UNKNOWN rather than inferred.

## Executive conclusion

Batch 2 reinforces the earlier conclusion: **permission prompts, local-computer access, command execution, tool connectivity and administrative allow-lists are no longer sufficient differentiation on their own.**

The AgentOS opportunity remains the coherent product loop:

> **explicit authority → bounded execution → durable evidence → recovery/replay discipline → independent Green → independent PRS → understandable result**

AgentOS should copy good interaction patterns where useful, but differentiate on the integrity of the complete chain rather than feature count.

---

## Raycast

### Current observed product behavior

Raycast AI Extensions expose three tool-permission modes: `Ask`, `Auto` and `Always Allow`. Individual chats can override the global permission setting. `Auto` may run read-only actions, working-directory edits and ordinary shell commands automatically, while credential/private-key access and destructive actions require approval. Approval cards expose an AI-generated action description; shell actions can reveal the exact command. Users can allow once, always allow, or deny, and globally allowed tools can later be removed/reset.

Raycast also exposes enterprise controls including AI-provider allow-lists and extension allow-lists; organization managers can centrally configure AI controls and MCP servers. Current individual pricing is Free, Pro, Plus and Max, with Max positioned for heavier AI usage.

### AgentOS implication

**COPY / ADAPT:**
- one-time vs persistent tool approval;
- exact-command visibility before shell execution;
- understandable global allow-list management;
- provider and capability allow-lists for managed environments;
- progressive disclosure rather than forcing permission internals into every turn.

**DIFFERENTIATE:**
Raycast's mature permission UX means AgentOS cannot treat approval prompts as a unique governance story. AgentOS should show how permission/authority connects to durable receipts, recovery, Green and PRS rather than ending the trust story at “the user clicked Allow.”

**WATCH:**
Raycast is explicitly evolving from question-answer AI toward longer agentic task completion. Treat it as a serious adjacent competitor for the everyday productivity layer, not merely a launcher.

---

## Manus — My Computer

### Current observed product behavior

Manus documents a local-computer mode based primarily on command-line execution. After a user authorizes folders, Manus can read/edit local files, build local applications and orchestrate work on the machine remotely. Commands in an authorized folder can run automatically; sensitive commands still request confirmation. Risky-operation permission can be scoped to the current task or current path.

### AgentOS implication

**COPY / ADAPT:**
- human-readable folder/path authorization;
- temporary authority scoped to the current task;
- remote-to-local workflow as an understandable user concept;
- avoid prompting on every harmless read-only action while retaining explicit gates for higher-risk work.

**DIFFERENTIATE:**
Local execution itself is not distinctive. AgentOS needs to make its stronger claims only where it can show precise authority provenance, durable mission state, replay/duplicate behavior, recovery state and independent assurance.

**PRODUCT WARNING:**
“Can work on your computer” is already a competitive category promise. AgentOS should not build acquisition around that phrase alone.

---

## n8n / Zapier

### Current status in this batch

**PARTIAL / NOT PROMOTED TO DETAILED COMPARISON.**

Both remain strategically relevant to workflow automation and agent/tool orchestration, but this cycle did not collect sufficiently clean current evidence across authority, approval, recovery, replay and secrets dimensions to justify a precise row-by-row comparison.

Do not fill the gaps from memory. Keep them in the next research tranche.

### Existing strategic implication

AgentOS should not compete by recreating mature workflow/RPA breadth. Use/integrate specialist automation where appropriate while AgentOS retains its own orchestration, authority, evidence and assurance boundary.

---

## Cline / Roo Code

### Current status in this batch

**PARTIAL / HOLD FOR DEEPER SOURCE REVIEW.**

These remain important developer-agent comparisons, particularly around terminal/browser/MCP execution and approval/auto-approval UX, but this batch does not promote detailed claims without a clean primary-source evidence set.

### AgentOS implication

Developer agents are rapidly normalising high-capability tool execution. AgentOS should avoid “AI can edit code/run commands” as differentiation and instead prove why governed multi-worker execution is safer and more understandable for broader users.

---

## Open Interpreter / Open WebUI Computer / local-model shells

### Current status in this batch

**PENDING / UNKNOWN IN THIS REPORT.**

No product capability claim is made from stale memory. These remain queued because local execution, model freedom and computer-control functionality are directly relevant to AgentOS's table-stakes boundary.

---

# Competitive pattern update

## Increasingly baseline

- tool permission prompts;
- allow once / persistent allow;
- local folder/workspace scoping;
- local command execution;
- remote initiation of local tasks;
- MCP/extensions/tool ecosystems;
- provider choice/BYOK;
- organization allow-lists;
- local models;
- administrative AI controls.

## Still valuable AgentOS differentiation if actually proven

1. **Authority as a durable first-class object**, not only an approval dialog.
2. **Evidence attached to the exact job and side effect.**
3. **Explicit incomplete/recovery-required states instead of silent success.**
4. **Replay/duplicate protection that is visible and testable.**
5. **Independent Green verification after execution.**
6. **Independent PRS adversarial assurance after Green.**
7. **Provider neutrality across free, local and paid models.**
8. **A user-facing Evidence Timeline that explains the above without requiring engineering logs.**

## Marketing recommendation

Lead with the problem:

> AI agents can increasingly use your files, tools and computer. The harder question is how you stay in control and know what actually happened.

Then position AgentOS directionally:

> AgentOS is being built to put explicit authority, evidence, recovery and independent assurance around real AI work.

Do not currently convert this into guarantees of complete Windows autonomy, instant stopping, perfect recovery or universal verification.

# Next research tranche

Priority evidence gaps:
1. n8n current human-approval / credential / execution-history / recovery semantics;
2. Zapier Agents current action approval and audit/control model;
3. Cline and Roo Code exact auto-approve/tool/MCP/browser controls;
4. Open Interpreter computer/local execution safety controls;
5. Open WebUI Computer and representative local-model shells;
6. current pricing/onboarding comparison where materially relevant.

# Status

**VERIFIED FOR RAYCAST + MANUS SUBSET / PARTIAL FOR REMAINING TARGETS / NO PRODUCT CLAIM PROMOTION / NO OVERALL GREEN.**
