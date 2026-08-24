# Overseer

**Autonomous multi-repository engineering supervisor**

Overseer is an AI agent designed to continuously inspect an owner's GitHub portfolio, understand project state, identify defects and risks, recommend improvements, remember validated reusable skills, and maintain an auditable record of its findings inside each repository.

## Mission

Overseer does not replace the project agents or developers working on a repository. It acts as the supervisory layer above them.

It should:

- Discover every repository it is authorized to inspect.
- Build a current inventory of projects, branches, technologies, dependencies, workflows, tests, documentation, and deployment configuration.
- Detect bugs, incomplete implementations, technical debt, security concerns, configuration problems, duplicated work, and architectural inconsistencies.
- Distinguish evidence from assumptions.
- Prioritize findings by severity, confidence, impact, and effort.
- Recommend concrete remediation steps.
- Learn and reuse validated procedures without granting those procedures additional authority.
- Maintain an append-only audit trail in each repository.
- Re-scan repositories after meaningful changes.
- Avoid destructive changes unless explicitly authorized by policy.

## Operating principle

> Observe first. Verify second. Reuse validated skills where appropriate. Recommend third. Change only when authorized. Record everything important.

## Repository structure

```text
Overseer/
├── README.md
├── OVERSEER.md
├── MANUS-INTEGRATION.md
├── config/
│   └── overseer.yml
├── protocols/
│   ├── agent-governance.md
│   ├── autonomous-loop.md
│   ├── finding-lifecycle.md
│   ├── knowledge-model.md
│   ├── owner-reporting.md
│   ├── portfolio-discovery.md
│   ├── portfolio-intelligence.md
│   ├── priority-engine.md
│   ├── recommendation-policy.md
│   ├── repository-scan.md
│   ├── scan-engine.md
│   ├── scan-manifest.md
│   └── skill-memory.md
├── src/
│   ├── adapters/
│   ├── analysis/
│   ├── discovery/
│   ├── findings/
│   ├── pipeline/
│   ├── scanner/
│   └── state/
│       └── skill_memory.py
└── tests/
    └── test_skill_memory.py
```

## Current capabilities

1. **Portfolio discovery** — model repositories available to the connected GitHub identity.
2. **Repository reconnaissance** — establish repository boundaries and inspection coverage.
3. **Evidence extraction** — capture observable repository facts without turning absence into unsupported certainty.
4. **Static analysis rules** — generate conservative candidate findings from evidence.
5. **Confidence and coverage** — distinguish full, partial and limited inspection.
6. **Historical state** — detect new, unchanged, changed and reopened observations.
7. **Decision ledger** — retain evidence-backed recommendations and owner-approval boundaries.
8. **Safe dry-run orchestration** — compose discovery, evidence, analysis, scoring and state without mutation authority.
9. **Agent governance** — keep project agents subordinate to the portfolio supervisory layer.
10. **Continuous supervision** — support repeat scans and historical comparison.
11. **Reusable skill memory** — retain versioned, evidence-backed procedures; retrieve matching skills; record reuse outcomes; and keep skill memory separate from permissions and execution authority.

## Safety boundaries

The active policy is `observe_report`. Overseer must never silently delete code, rewrite history, expose secrets, merge pull requests, disable security controls, or make production changes. Autonomous writes are permitted only when explicitly enabled by policy, must be narrowly scoped, and must be recorded. Remembered skills never grant authority beyond the active policy.

## Status

**Phase 1 — Supervisory control plane and safe analysis pipeline.**

The repository contains the operating charter, Manus Desktop integration contract, governance protocols, inspection confidence model, historical state primitives, decision ledger, GitHub inventory adapter, read-only portfolio dry-run pipeline, and reusable skill-memory primitives. The next milestone remains validated live GitHub scanning with explicit coverage/limitations and owner-facing reporting; mutation authority remains disabled.
