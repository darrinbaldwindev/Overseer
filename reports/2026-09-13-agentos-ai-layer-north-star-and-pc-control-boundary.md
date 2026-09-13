# AgentOS — AI Layer North Star & PC-Control Boundary

**Date:** 2026-09-13  
**Owner:** ChatGPT / Marketing Overseer  
**Purpose:** Durable handoff for Overseer review of the strategic north star and architectural boundary discussed after ecosystem/competitor research.

---

## 1. North-star ambition

AgentOS should be evaluated as a candidate **trusted AI layer on the computer**, not as a replacement for Windows.

Internal framing:

> Windows coordinates hardware, applications, files, processes, networking and the desktop environment.  
> AgentOS coordinates intelligence, agents, capabilities and authority.

Long-term ambition:

> **AgentOS aims to become the trusted AI layer on every computer — coordinating whichever AI, agents and tools the user chooses, while keeping the user in control.**

This is an internal architectural north star, not yet a public market claim.

Do **not** publicly claim that AgentOS is or will be "as important as Windows" until product evidence, adoption and runtime maturity justify such language.

---

## 2. Strategic consequence

A universal AI layer does not need to own every model, every tool, every automation mechanism or every low-level PC action.

The stronger architecture is hybrid:

- AgentOS owns intent, planning, policy, permissions, authority, model/tool selection, scheduling, mission state, budgets, evidence, recovery, audit and verification.
- Specialist plugins/connectors/workers perform specialised execution.
- Windows remains the underlying operating system and owns device/process/filesystem/application primitives.

Conceptual model:

> **AgentOS = AI control plane**  
> **Capabilities / plugins / workers = hands**  
> **Models = brains**  
> **Windows = underlying operating system**

Jack and Henry span this system:

- **Jack** decides what capabilities are allowed, in what scope, for how long, at what cost/risk.
- **Henry** checks whether the claimed outcome is actually supported by evidence.

---

## 3. PC-control decision

AgentOS should **not** attempt to directly control every part of the PC itself.

It should also **not** degrade into merely a plugin manager.

Recommended boundary:

### Build/own a small trusted native/local execution layer

AgentOS should retain reliable native capability for essential operations such as:

- inspect files/directories;
- controlled file modification;
- approved command execution;
- process/service inspection where appropriate;
- launch applications where authorised;
- collect local evidence;
- inspect machine state;
- stop/revoke local work;
- perform recovery-oriented actions.

This gives AgentOS a dependable minimum worker even if external integrations are unavailable.

### Delegate specialised execution

Prefer specialist capability providers for domain-specific work:

| Need | Preferred execution path |
|---|---|
| Local file inspection/edit | AgentOS local worker |
| PowerShell / bounded shell | Governed local worker |
| Git/repository work | Git capability/local worker |
| Browser interaction | Playwright/browser worker |
| Gmail | Gmail/API connector |
| Outlook / Microsoft 365 | Microsoft Graph / Office integration |
| Legacy or GUI-only Windows app | Bounded computer-use/RPA worker |
| Shopify | Shopify API/plugin |
| Workflow automation | n8n/Zapier integration |
| Secrets/passwords | Credential broker/password-manager integration |
| Cloud AI | Provider adapters |
| Local AI | Ollama/local-provider adapter |

Keep the established doctrine:

> **MCP-first, not MCP-only. Build and own the control plane; integrate, wrap or delegate specialised execution wherever practical.**

---

## 4. Why this boundary matters

Trying to build every PC capability natively would make AgentOS:

- enormous;
- brittle;
- slow to maintain;
- duplicative of mature external tools;
- difficult to secure;
- difficult to keep compatible with changing apps/services.

A control-plane architecture scales better because new capabilities can be added without changing the canonical authority, mission, recovery or assurance systems.

This also supports the "every computer" ambition: AgentOS can coordinate different models, tools and workers on different machines while preserving a stable control model.

---

## 5. What AgentOS should own canonically

The following should remain canonical AgentOS concerns rather than be delegated to arbitrary plugins:

- user intent / mission definition;
- planning/orchestration;
- capability discovery/routing;
- authority and permissions;
- risk classification;
- cost/budget governance;
- schedule/autonomy-window governance;
- durable mission state;
- retry/recovery semantics;
- duplicate/replay protection;
- evidence correlation;
- assurance/verification state;
- audit trail;
- connector/plugin trust metadata;
- capability manifests;
- stop/pause/revoke semantics;
- local/cloud/data-location truth;
- user-facing mission status.

No external worker/plugin should become a competing source of truth for these domains.

---

## 6. What should generally remain external/integrated

AgentOS should not become a replacement for:

- Windows itself;
- full IDEs;
- email clients;
- CRM systems;
- project-management suites;
- password managers;
- cloud-storage services;
- low-level window managers;
- full RPA suites;
- vendor-specific business platforms;
- proprietary model hosting where existing providers are sufficient.

AgentOS should coordinate these systems when useful.

---

## 7. Product-interface implication

The emerging interaction model remains coherent:

> **Chat for intent.**  
> **Palette for speed.**  
> **Inbox for attention.**  
> **Jobs for repetition.**  
> **Jack for authority.**  
> **Isla for execution.**  
> **Henry for proof.**

This allows a universal AI operating layer without forcing every capability into the main chat window.

---

## 8. Strategic feature test

Because the ambition is broader than a normal AI app, evaluate new proposals using two questions:

1. **Does this help sell/use AgentOS now?**
2. **Would a universal AI operating layer eventually need this?**

Features that likely belong to the core include:

- identity;
- permissions;
- capability discovery;
- model routing;
- durable jobs;
- device trust;
- credential handling;
- evidence;
- recovery;
- connector management;
- cost governance;
- extension security.

Features that are better as integrations include:

- CRM;
- IDE;
- email client;
- window manager;
- cloud storage;
- project-management UI;
- mature domain-specific applications.

This distinction should prevent product sprawl.

---

## 9. Public-claim discipline

Safe current language:

- "Put AI to work."
- "Give AgentOS a real job."
- "One platform. Every AI." only where provider support is qualified and truthful.
- "Stay in control. See what it did." as positioning direction.

Internal target only, not yet proven marketing claim:

> AgentOS can perform useful real work on a user's computer while staying inside explicit authority, showing what happened, detecting when work is not actually complete, stopping when told, and recovering without silently duplicating or losing work.

Avoid for now:

- "replaces Windows";
- "as important as Windows";
- "controls every app";
- "fully autonomous computer";
- "works with every AI";
- "always chooses the best AI";
- "guaranteed savings";
- "completely private" unless scope is explicitly proven.

---

## 10. Architecture guardrails for Overseer

Overseer should resist any future proposal that:

- creates a second scheduler/queue/mission ledger;
- makes a plugin own canonical mission state;
- grants connector install == mission authority;
- gives an external worker final GREEN authority;
- stores long-lived plaintext credentials for convenience;
- uses GUI/computer-use when a safer structured/API path exists;
- duplicates mature tools merely to increase feature count;
- introduces vendor lock-in inconsistent with provider neutrality.

---

## 11. Recommended hierarchy for execution

When AgentOS needs to perform work, prefer in this order where practical:

1. deterministic/native bounded capability;
2. official API/connector;
3. MCP/tool interface with explicit manifest/permissions;
4. browser automation;
5. GUI/computer-use/RPA fallback.

Lower levels in this list generally increase ambiguity, fragility and risk and therefore should require stronger Jack controls and Henry evidence.

---

## 12. Implication for Level 2

Level 2 does not require AgentOS to become a universal desktop automation framework.

Level 2 requires proving that AgentOS can safely govern useful real work performed through one or more bounded execution capabilities.

The acceptance emphasis should remain:

- exact authority;
- real Windows execution;
- evidence;
- safe stop/revoke;
- failure/recovery;
- duplicate protection;
- assurance;
- no false-GREEN.

Once these primitives are trustworthy, additional capabilities can expand horizontally without changing the control-plane model.

---

## 13. Overseer decisions requested

Please consider formalising the following strategic statements:

1. AgentOS is an **AI control plane / AI operating layer**, not a Windows replacement.
2. The long-term north star is a trusted AI layer suitable for broad deployment on personal computers.
3. AgentOS owns governance/orchestration/state/evidence/assurance; specialist capabilities may be delegated.
4. AgentOS retains a small trusted native local worker as a minimum capability baseline.
5. APIs/MCP/structured capabilities are preferred over GUI control where possible.
6. Computer-use remains a governed fallback/specialised capability, not the core architecture.
7. New features should pass both the immediate-use test and the universal-AI-layer test.
8. Public language remains evidence-bound; the Windows analogy is internal strategy, not a current superiority claim.

---

## 14. Current status

This document records strategic direction for Overseer consideration only.

It does **not** authorise:

- implementation;
- merge;
- deployment;
- credential changes;
- production autonomy;
- public claims;
- vendor contact;
- purchases.

No overall GREEN is asserted.
