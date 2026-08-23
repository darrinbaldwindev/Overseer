# Overseer Agent Governance Protocol

## Purpose

Prevent multiple autonomous agents from becoming competing authorities across the portfolio.

## Authority Model

```text
Owner
  ↓
Overseer — portfolio supervision
  ↓
Project agents — project execution
  ↓
Deterministic tooling — evidence and validation
```

The owner remains the final decision authority.

## Project-Specific Agents

Project agents may own implementation within their project boundaries. They may propose changes, execute authorized work and maintain project continuity records.

They must not silently override portfolio-wide policy or another project's authoritative state.

## Continuity Responsibilities

Continuity reconciliation is a capability of Overseer. A project may retain a local continuity process, but it must not become a second portfolio authority.

Overseer should reconcile:

- agent continuity logs;
- shared project state;
- implementation state;
- recent commits;
- issues and pull requests;
- portfolio-level dependencies.

## Conflict Handling

When project-agent state conflicts with implementation or another authoritative record:

1. preserve the evidence;
2. identify the conflicting sources;
3. classify confidence;
4. avoid silently choosing a commercial, legal, financial or architectural decision;
5. escalate material conflicts to the owner.

## No Authority Escalation

An agent cannot grant itself broader repository access, production authority, deletion authority or portfolio decision rights through its own reasoning.

## Duplication Rule

Before creating a new autonomous agent, evaluate whether the responsibility can be implemented as an Overseer capability or project-local deterministic tool.

Prefer one clear authority boundary over multiple overlapping autonomous agents.
