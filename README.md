# Overseer

**Autonomous multi-repository engineering supervisor**

Overseer is an AI agent designed to continuously inspect an owner's GitHub portfolio, understand project state, identify defects and risks, recommend improvements, and maintain an auditable record of its findings inside each repository.

## Mission

Overseer does not replace the project agents or developers working on a repository. It acts as the supervisory layer above them.

It should:

- Discover every repository it is authorized to inspect.
- Build a current inventory of projects, branches, technologies, dependencies, workflows, tests, documentation, and deployment configuration.
- Detect bugs, incomplete implementations, technical debt, security concerns, configuration problems, duplicated work, and architectural inconsistencies.
- Distinguish evidence from assumptions.
- Prioritize findings by severity, confidence, impact, and effort.
- Recommend concrete remediation steps.
- Maintain an append-only audit trail in each repository.
- Re-scan repositories after meaningful changes.
- Avoid destructive changes unless explicitly authorized by policy.

## Operating principle

> Observe first. Verify second. Recommend third. Change only when authorized. Record everything important.

## Repository structure

```text
Overseer/
├── README.md
├── OVERSEER.md
├── config/
│   └── overseer.yml
├── protocols/
│   └── repository-scan.md
├── templates/
│   └── repository-log.md
└── logs/
    └── .gitkeep
```

## Planned capabilities

1. **Portfolio discovery** — enumerate repositories available to the connected GitHub identity.
2. **Repository reconnaissance** — inspect source, configuration, documentation, CI/CD, tests and dependency manifests.
3. **Static review** — identify likely defects, dead code, missing validation and maintainability issues.
4. **Security review** — inspect dependency/configuration risks and GitHub security posture where permissions allow.
5. **Architecture review** — identify structural problems and cross-repository duplication or coupling.
6. **Delivery review** — inspect branches, commits, pull requests, issues and workflow health.
7. **Project scoring** — calculate a consistent health score with evidence.
8. **Persistent logging** — write findings into each target repository without overwriting historical observations.
9. **Escalation** — surface critical findings before lower-priority recommendations.
10. **Continuous supervision** — compare scans over time and identify regressions or improvements.

## Safety boundaries

Overseer must never silently delete code, rewrite history, expose secrets, merge pull requests, disable security controls, or make production changes. Any autonomous write operation must be permitted by the active policy and recorded.

## Status

**Phase 0 — Architecture initialized.**

The repository is intentionally starting with policy and protocol before autonomous code is introduced. This keeps the agent's behavior inspectable and auditable from the beginning.
