# AgentOS Hybrid Install — Ollama + Optional Libra Worker Handoff

**Date:** 2026-09-12
**Role:** Marketing Overseer
**Status:** RECOMMENDATION / ARCHITECTURAL REVIEW REQUIRED / LICENSING REVIEW REQUIRED

## Updated owner direction

The preferred hybrid-install concept is now:

- AgentOS remains the canonical orchestration, authority, mission, governance and assurance layer.
- Ollama remains the recommended local-model inference path for hybrid installs.
- Libra OS is **not** part of the mandatory hybrid baseline.
- Libra OS is an **optional bounded local/self-hosted worker/runtime candidate** only where installed, licensed, eligible and architecturally approved.
- Cloud/free APIs and paid/BYOK providers remain additional capability sources where authorised.

## Important evidence boundary

Current AgentOS main was checked for Ollama and Libra references. No current main-branch references were found that establish Ollama as implemented hybrid-install functionality, and no Libra references were found.

Therefore this record does **not** claim implementation.

Classification:
- **Ollama:** intended/recommended local AI component; implementation status not established by the current repo scan.
- **Libra OS:** optional candidate worker/runtime; not currently recorded in AgentOS main.
- **Hybrid install:** AgentOS + local AI capability, with optional governed workers such as Libra.

## Deep-research conclusion on Libra

Libra can complement AgentOS well **only if it remains subordinate**.

Technical fit is strong because Libra exposes API/SDK surfaces, supports local/self-hosted operation, can use OpenAI-compatible model endpoints, and can itself use local Ollama-backed models.

However, Libra also includes its own orchestration, agents, model routing, memory/knowledge, governance, approvals and audit functions. Those overlap directly with AgentOS-owned concerns.

Therefore Libra must **not** become a second control plane.

### Collision risks to avoid

1. Two authority systems — AgentOS/Jack versus Libra approvals/governance.
2. Two routers — AgentOS capability/model routing versus Libra internal model tiers/router.
3. Two memory systems — AgentOS canonical state versus Libra persistent employee/knowledge state.
4. Side-effect bypass — Libra filesystem/custom/external tools executing outside AgentOS authority gates.
5. Assurance confusion — Libra audit/citations are worker evidence, not Henry/PRS assurance.
6. User-role confusion — Libra digital employees must not compete with Willow/Isla/Jack/Henry in the product experience.
7. Install complexity — Libra is materially heavier than simply adding Ollama and should not become a mandatory baseline dependency.

## Licensing warning

Libra licensing requires explicit review before any commercial bundle or redistribution.

Research indicates:
- Libra SDK/CLI/OpenAPI components are permissively licensed.
- The Libra server/runtime has separate commercial/licensing conditions.
- Personal/self-hosted use being available does **not** automatically establish AgentOS rights to redistribute, bundle or embed Libra inside a paid $99 product.

Before any official bundling, obtain written clarification covering:
- redistribution rights;
- automatic installation;
- embedding in a paid AgentOS product;
- commercial single-user installs;
- OEM/partner rights;
- white-label/API use;
- whether end users need separate Libra licensing.

Until resolved, Libra is **OPTIONAL / USER-SUPPLIED / EXPERIMENTAL**, not bundled.

## Recommended architecture

AgentOS remains in control:

`AgentOS Overseer -> Jack authority/policy gate -> capability router -> Ollama / optional Libra worker / cloud worker -> result/evidence -> Henry assurance -> Green/PRS as required`

Libra must **not** become a second Overseer, scheduler, mission ledger, worker registry, authority engine, persistence system, Green system, PRS system or source of truth.

## Intended roles

### Ollama

Candidate role:
- local model inference;
- privacy-sensitive tasks;
- free/local capacity;
- offline-capable workloads where supported;
- low-cost routine tasks where local hardware is adequate.

### Libra OS

Candidate role:
- optional bounded local/self-hosted worker runtime;
- specialist document/RAG/research workloads;
- local multi-stage reasoning using Ollama where useful;
- structured report generation;
- specialist bounded agent execution.

Initial integration should **not** expose:
- Libra scheduler;
- Libra canonical memory as AgentOS source of truth;
- Libra direct filesystem mutation;
- Libra direct external writes/messages;
- Libra approval authority;
- Libra mission orchestration above AgentOS.

## Smallest safe integration contract

Recommended worker class: `libra-local`

First prototype capabilities:
- grounded document analysis;
- source-cited research over local documents;
- structured report generation;
- bounded specialist-agent execution;
- local Ollama-backed reasoning where appropriate.

AgentOS must retain:
- mission/task IDs;
- canonical state;
- capability registry;
- worker eligibility;
- user authority/consent;
- Jack policy decision;
- global budget;
- scheduler/Night Shift;
- queues/correlation IDs;
- durable AgentOS receipts;
- Henry assurance;
- Green/PRS;
- commercial entitlement;
- final result state.

## Hybrid install concept

Preferred stack:

1. AgentOS core
2. Ollama local inference
3. Optional governed workers, including Libra where installed/licensed/eligible
4. Free cloud/API providers where legitimate capacity is available
5. Paid/BYO providers when authorised
6. AgentOS capability registry and routing select among them by capability, authority, privacy, availability, health, user preference and cost

Commercial/affiliate relationships must never influence technical worker ranking.

## Marketing significance

This supports the broader AgentOS positioning:

- use free, paid and local AI together;
- provider/model agnostic;
- local + cloud hybrid;
- one governed control layer;
- AgentOS as the AI operating layer on the user's computer.

Do not market Libra as bundled/implemented until licensing, architecture, runtime and assurance evidence support that claim.

## Handoff to ChatGPT / AgentOS Overseer

Please treat this as the corrected architecture/product handoff replacing any interpretation that Libra should be bundled by default.

Requested next actions:

1. Keep Ollama under review as the official local-inference baseline or install profile.
2. Evaluate Libra only as a bounded subordinate worker through existing provider/worker adapter and capability-registry abstractions.
3. Confirm no duplicate scheduler, queue, worker registry, mission ledger, authority layer, persistence layer, Green system or PRS system is introduced.
4. Prototype only read/analysis/reporting capability first; no direct side-effecting Libra tools.
5. Resolve commercial/OEM/redistribution licensing before any bundled install.
6. Keep defaults fail-closed and local/autonomy disabled unless explicitly authorised.
7. Add deterministic tests for authority bypass, tool bypass, routing ambiguity, state divergence, result correlation and missing evidence.
8. Require independent Green/PRS challenge before any promotion or user-facing implementation claim.
9. Preserve graceful degradation: AgentOS must continue to operate if Libra is absent or unavailable.

## Governance

No merge, approval, ready transition, rebase, deployment, credential change, production write, purchase or production autonomy is authorised by this record.

**Overall status: AMBER — prototype-worthy as an optional worker; mandatory bundling rejected pending architecture and licensing evidence.**
