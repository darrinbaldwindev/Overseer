# Repository Scan Protocol

## Stage 0 — Identify

Record repository name, visibility, default branch, repository size, primary languages, and available permissions.

## Stage 1 — Reconnaissance

Inspect the repository tree and locate:

- README and project documentation
- package/dependency manifests
- source directories
- tests
- environment/configuration files
- Docker/container definitions
- CI/CD workflows
- infrastructure/deployment files
- database migrations/schema
- API definitions
- scripts and automation

## Stage 2 — Project understanding

Determine:

- intended purpose;
- application type;
- major components;
- execution path;
- external services;
- data stores;
- authentication/authorization model;
- build and deployment path;
- testing strategy.

If intent cannot be established confidently, state the uncertainty instead of inventing it.

## Stage 3 — Correctness review

Search for:

- unreachable code;
- obvious runtime errors;
- invalid assumptions;
- missing error handling;
- race/concurrency hazards;
- unsafe input handling;
- broken state transitions;
- inconsistent types/contracts;
- incomplete implementations;
- TODO/FIXME markers with meaningful impact.

## Stage 4 — Security review

Check for:

- committed secrets;
- insecure authentication/authorization patterns;
- unsafe deserialization or command execution;
- injection risks;
- exposed sensitive data;
- dangerous defaults;
- missing security controls;
- dependency/security configuration gaps.

Do not copy secret values into the report. Redact them and identify the location.

## Stage 5 — Reliability review

Assess:

- startup failures;
- missing health checks;
- weak retry/timeout behavior;
- unhandled failures;
- fragile external integrations;
- data-loss scenarios;
- migration risks;
- insufficient logging/observability.

## Stage 6 — Engineering quality

Assess:

- test coverage strategy;
- duplication;
- coupling;
- complexity;
- naming and structure;
- dependency hygiene;
- documentation;
- maintainability.

## Stage 7 — Delivery review

Inspect commits, branches, pull requests and workflows for signs of:

- stalled work;
- repeated failures;
- abandoned branches;
- unresolved review concerns;
- broken CI;
- missing release/deployment safeguards.

## Stage 8 — Historical comparison

Compare the current state with the previous Overseer record where available.

Classify findings as:

- NEW
- UNCHANGED
- IMPROVED
- REGRESSED
- RESOLVED
- REOPENED

## Stage 9 — Cross-repository review

Compare related repositories for duplication, incompatible conventions, shared dependencies, architectural drift, and opportunities for consolidation.

## Stage 10 — Report

Produce prioritized findings. Each finding should contain:

```text
ID:
Status:
Severity:
Confidence:
Area:
Evidence:
Impact:
Recommendation:
Suggested next action:
```

Finish with a short executive summary and the recommended next actions.
