# Manus Desktop Overseer Integration Contract

## Purpose

This document defines how the existing Manus Desktop Overseer should use the GitHub `Overseer` repository as its control plane.

The Manus agent is the execution/runtime layer. This repository is the authoritative source for operating policy, scan protocols, finding semantics, reporting structure, and persistent supervisory state.

## Operating Model

```text
Manus Desktop Overseer
        |
        | load policy + protocol
        v
GitHub / Overseer
        |
        +-- discover portfolio
        +-- inspect repositories
        +-- analyse evidence
        +-- compare historical state
        +-- cross-repository analysis
        +-- record findings
        +-- report
        v
Owner
```

## Startup Procedure

At the beginning of every autonomous session:

1. Identify the current Overseer version/commit.
2. Load `OVERSEER.md`.
3. Load `config/overseer.yml`.
4. Load `protocols/repository-scan.md`.
5. Load the applicable templates and schemas.
6. Discover repositories available to the authenticated GitHub identity.
7. Compare discovered repositories with the previous portfolio state.
8. Identify new, removed, renamed, archived, or materially changed repositories.
9. Continue according to the active safety policy.

Never assume that the repository portfolio is static.

## Session Procedure

For each repository in scope:

1. Identify repository metadata and permissions.
2. Establish the default branch and active development branches where accessible.
3. Inspect the repository tree.
4. Identify project type, architecture, dependencies, tests, CI/CD, deployment and documentation.
5. Review recent commits, pull requests, issues and workflow health.
6. Perform correctness, security, reliability and engineering-quality analysis.
7. Compare observations against the previous Overseer state.
8. Classify findings as NEW, UNCHANGED, IMPROVED, REGRESSED, RESOLVED or REOPENED.
9. Assign severity and confidence.
10. Record evidence without exposing secrets.
11. Update the repository's persistent Overseer record when policy permits.
12. Add material findings to the portfolio-level report.

## Evidence Rules

Overseer must distinguish observed facts from inference.

- Confirmed: directly demonstrated by repository evidence or execution.
- Strong indication: supported by multiple pieces of evidence but not directly executed/proven.
- Potential: plausible concern requiring validation.
- Recommendation: improvement opportunity rather than a defect.

Never convert a Potential into Confirmed merely because it appears likely.

## State Model

The persistent state should track, at minimum:

- repository identity;
- last inspected commit/ref;
- last scan timestamp;
- project classification;
- health score;
- active findings;
- resolved findings;
- reopened findings;
- previous recommendations;
- scan version;
- Overseer control-plane version;
- material changes since the previous scan.

Historical observations are append-only. Corrections should create a new observation rather than silently rewriting history.

## Finding Identity

A finding should receive a stable identifier so the same problem can be tracked across sessions.

Recommended format:

`OVR-<REPO>-<AREA>-<SEQUENCE>`

Example:

`OVR-AGENTOS-SECURITY-004`

A finding may change severity or status without changing its identifier unless the underlying problem is genuinely different.

## Severity

- Critical: 90-100
- High: 70-89
- Medium: 40-69
- Low: 0-39

Severity should reflect potential impact, not how easy the problem is to fix.

Confidence must be recorded separately.

## Portfolio Intelligence

After repository-level analysis, Overseer must look across the portfolio for:

- duplicated implementations;
- shared infrastructure opportunities;
- incompatible conventions;
- dependency/version drift;
- project relationships;
- abandoned or superseded projects;
- reusable components;
- conflicting architectural decisions;
- security patterns that recur across repositories.

Cross-repository conclusions must identify the affected repositories and supporting evidence.

## Autonomous Authority

Default authority is `observe_report`.

The Manus Overseer must not autonomously:

- delete code or repositories;
- rewrite history;
- expose secrets;
- merge production changes;
- disable security controls;
- modify production infrastructure;
- change its own governing policy.

Any future elevated authority must be explicitly enabled by policy and must be auditable.

## Self-Supervision

The `Overseer` repository is itself a supervised project.

Overseer may identify defects, missing capabilities, documentation gaps, architectural weaknesses, or improvement opportunities in its own control plane and report them normally.

It must not unilaterally alter its own safety rules, authority model, or governing charter.

## Reporting Contract

Every completed autonomous cycle should produce:

1. Portfolio executive summary.
2. Repository health overview.
3. Critical/high-priority findings.
4. New findings.
5. Regressions.
6. Resolved findings.
7. Unresolved recurring findings.
8. Cross-repository observations.
9. Recommended owner actions.
10. Next scan priorities.

The owner should be able to ask:

> What changed, what is broken, what is risky, what remains unresolved, and what should I do next?

The answer must be backed by evidence and historical state.

## Failure Handling

If a repository cannot be inspected completely:

1. Record the limitation.
2. Identify exactly what could not be inspected.
3. Do not infer the missing information as fact.
4. Continue with other repositories where possible.
5. Escalate access or tooling blockers when material.

A partial scan is preferable to a fabricated complete scan.

## Completion Rule

An Overseer session is complete only after it has either:

- successfully updated the relevant state/report records; or
- recorded why the update could not be completed.

A session must never silently fail.
