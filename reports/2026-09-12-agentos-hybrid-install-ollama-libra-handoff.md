# AgentOS Hybrid Install — Ollama + Libra Handoff

**Date:** 2026-09-12
**Role:** Marketing Overseer
**Status:** RECOMMENDATION / ARCHITECTURAL REVIEW REQUIRED

## Owner direction

The preferred hybrid-install concept is now:

- AgentOS remains the canonical orchestration, authority, mission, governance and assurance layer.
- Ollama is the recommended local-model inference path for hybrid installs.
- Libra OS is a new candidate for an optional local/self-hosted worker/runtime layer.
- Cloud/free APIs and paid/BYOK providers remain additional capability sources where authorised.

## Important evidence boundary

Current AgentOS main was checked for Ollama and Libra references. No current main-branch references were found that establish Ollama as implemented hybrid-install functionality, and no Libra references were found.

Therefore this record does **not** claim implementation.

Classification:
- **Ollama:** intended/recommended local AI component; implementation status not established by the current repo scan.
- **Libra OS:** new candidate worker/runtime; not currently recorded in AgentOS main.
- **Hybrid install with both:** product/architecture recommendation only until reviewed, implemented and verified.

## Recommended architecture

AgentOS should remain in control:

`AgentOS Overseer -> Jack authority/policy gate -> capability router -> Ollama / Libra / cloud worker -> result/evidence -> Henry assurance`

Libra must **not** become a second Overseer, scheduler, mission ledger, worker registry, authority engine, persistence system, Green system, PRS system or source of truth.

## Intended roles

### Ollama

Candidate role:
- local model inference
- privacy-sensitive tasks
- free/local capacity
- offline-capable workloads where supported
- low-cost routine tasks where local hardware is adequate

### Libra OS

Candidate role:
- optional bounded local/self-hosted worker runtime
- specialist multi-agent/document/research workloads where its capabilities are useful
- external capability behind AgentOS policy and evidence boundaries

Libra should be treated as a subordinate worker/capability provider, not as canonical governance.

## Hybrid install concept

Potential stack:

1. AgentOS core
2. Ollama local inference
3. Optional Libra OS worker/runtime
4. Free cloud/API providers where legitimate capacity is available
5. Paid/BYO providers when authorised
6. AgentOS capability registry and routing select among them by capability, authority, privacy, availability, health, user preference and cost

Commercial/affiliate relationships must never influence technical worker ranking.

## Marketing significance

This supports the broader AgentOS positioning:

- use free, paid and local AI together
- provider/model agnostic
- local + cloud hybrid
- one governed control layer
- AgentOS as the AI operating layer on the user's computer

Do not market Ollama or Libra as bundled/implemented hybrid-install features until repository/runtime evidence proves that.

## Handoff to ChatGPT / AgentOS Overseer

Please review this as an architecture/product handoff.

Requested next actions:

1. Determine whether Ollama belongs in the official hybrid-install baseline or as an optional install profile.
2. Evaluate Libra OS as a bounded subordinate worker/runtime behind existing AgentOS capability, authority, mission, persistence and assurance systems.
3. Confirm no duplicate scheduler, queue, worker registry, mission ledger, authority layer, persistence layer, Green system or PRS system would be introduced.
4. Define the smallest integration contract if approved, preferably through the existing provider/worker adapter and capability registry abstractions.
5. Keep defaults fail-closed and local/autonomy disabled unless explicitly authorised.
6. Add deterministic tests and independent Green/PRS challenge before any production or user-facing implementation claim.
7. Update installation/product docs only after architectural review and implementation evidence.

## Governance

No merge, approval, ready transition, rebase, deployment, credential change, production write, purchase or production autonomy is authorised by this record.

**Overall status: AMBER — commercially promising, architecture review and implementation evidence required.**
