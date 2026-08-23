# Overseer Scan Engine Specification

## Purpose

Define the deterministic inspection pipeline used by the Manus Desktop Overseer when supervising a GitHub repository.

This is an analysis protocol, not an instruction to make autonomous code changes.

## Pipeline

```text
DISCOVER
  -> SNAPSHOT
  -> RECONNAISSANCE
  -> UNDERSTAND
  -> CORRECTNESS
  -> SECURITY
  -> RELIABILITY
  -> ENGINEERING QUALITY
  -> DELIVERY
  -> HISTORICAL COMPARISON
  -> CROSS-REPOSITORY ANALYSIS
  -> SCORE
  -> DEDUPLICATE
  -> REPORT
  -> PERSIST
```

## 1. Discover

Capture repository metadata, default branch, visibility, archive state, permissions, primary languages, size, available branches, and relevant GitHub resources.

Do not assume a repository is active merely because it contains code.

## 2. Snapshot

Record the exact commit/ref being analysed. The snapshot is the anchor for all subsequent findings.

Record the Overseer control-plane commit and scan protocol version alongside it.

## 3. Reconnaissance

Inspect the repository tree before interpreting individual files.

Prioritize:

- README/documentation;
- package and dependency manifests;
- application entry points;
- source directories;
- test directories;
- configuration;
- environment templates;
- Docker/container definitions;
- CI/CD workflows;
- infrastructure;
- database/schema/migrations;
- API definitions;
- automation scripts.

## 4. Understand

Build a concise project model:

- purpose;
- application category;
- architecture;
- runtime and language;
- entry points;
- major components;
- data stores;
- external services;
- authentication/authorization;
- build path;
- deployment path;
- test strategy.

If evidence is insufficient, mark the field unknown.

## 5. Correctness

Look for evidence of:

- runtime errors;
- broken imports/references;
- invalid state transitions;
- inconsistent interfaces;
- missing error handling;
- unsafe assumptions;
- incomplete implementations;
- dead/unreachable code with material impact;
- TODO/FIXME items that represent real unfinished behavior.

Prefer concrete evidence such as failing tests, broken references, contradictory contracts, or unreachable execution paths.

## 6. Security

Inspect for:

- exposed credentials or tokens;
- insecure authentication/authorization;
- injection risks;
- unsafe command execution;
- unsafe deserialization;
- sensitive data exposure;
- dangerous defaults;
- weak secret handling;
- dependency/security configuration concerns.

Never reproduce secret values. Report location and type only, with redaction.

## 7. Reliability

Assess:

- startup and initialization failure modes;
- timeout/retry behavior;
- external-service failure handling;
- data-loss scenarios;
- migration safety;
- idempotency where relevant;
- logging and observability;
- health/readiness checks;
- recovery behavior.

## 8. Engineering Quality

Assess:

- test strategy and important untested paths;
- duplication;
- coupling;
- complexity;
- dependency hygiene;
- naming and structure;
- documentation;
- maintainability;
- configuration consistency.

Do not turn stylistic preference into a defect unless it creates measurable risk or maintenance cost.

## 9. Delivery

Inspect:

- recent commits;
- active branches;
- pull requests;
- issues where accessible;
- workflow runs;
- release/deployment configuration.

Identify stalled work, repeated CI failures, unresolved review concerns, abandoned branches, and deployment blockers.

## 10. Historical Comparison

Compare against the previous repository state.

Use stable finding IDs to determine whether observations are:

- NEW
- UNCHANGED
- IMPROVED
- REGRESSED
- RESOLVED
- REOPENED

A finding must not become NEW solely because wording changed.

## 11. Cross-Repository Analysis

After repository-level analysis, compare the project with the current portfolio.

Look for duplication, shared infrastructure, incompatible versions, copied code, architectural drift, dependencies, abandoned projects, and reusable capabilities.

## 12. Finding Generation

For every candidate observation:

1. Gather evidence.
2. Determine classification.
3. Determine confidence.
4. Determine impact.
5. Assign severity.
6. Generate a stable ID or match an existing ID.
7. Write a concrete recommendation.
8. Define the next validation/remediation action.

## 13. Finding Quality Gate

Before reporting a finding, ask:

- What exact evidence supports it?
- Could the evidence have another explanation?
- Is this a defect, risk, uncertainty, or recommendation?
- Is the severity proportional to impact?
- Is confidence separate from severity?
- Can the owner act on the recommendation?
- Does this duplicate an existing finding?

Discard or downgrade findings that fail the evidence standard.

## 14. Health Score

The initial portfolio health model uses five dimensions:

| Dimension | Weight |
|---|---:|
| Security | 25% |
| Correctness | 25% |
| Reliability | 20% |
| Delivery | 15% |
| Engineering quality | 15% |

Start from 100 and apply evidence-backed deductions. Critical risks may impose a severe cap on the final score.

The score is a communication aid, not a substitute for the finding list.

## 15. Report

Produce:

1. executive summary;
2. health score and rationale;
3. critical/high findings;
4. new/regressed findings;
5. resolved/improved findings;
6. unresolved recurring findings;
7. cross-repository observations;
8. recommended actions;
9. limitations;
10. scan metadata.

## 16. Persist

Persist the repository state and portfolio state only after the analysis is internally consistent.

If persistence fails, report the failure explicitly. Never claim a scan is complete if its required state could not be recorded.
