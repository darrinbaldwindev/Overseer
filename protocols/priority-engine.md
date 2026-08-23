# Overseer Priority Engine

## Objective

Determine what Overseer should inspect next when the portfolio is larger than one scan cycle can reasonably process.

## Priority Inputs

Each repository receives priority signals from:

- active finding severity;
- finding age;
- recent code changes;
- security-sensitive changes;
- failed CI/deployment signals;
- previous scan failures;
- new repository status;
- recent regression;
- owner-requested priority;
- project lifecycle status.

## Priority Bands

### P0 — Immediate

Critical security, data-loss, production-blocking or severe reliability evidence.

### P1 — High

High-severity findings, material regressions, repeated deployment failures, or significant security-sensitive changes.

### P2 — Normal

Changed repositories, new repositories, unresolved medium findings and routine review work.

### P3 — Background

Stable repositories with no significant active findings.

## Fairness Rule

P0/P1 work can pre-empt lower-priority work, but P3 repositories must still receive periodic inspection.

## Owner Override

An explicit owner request may elevate a repository or scan task.

Owner priority should be recorded separately from automated priority.

## Explainability

Every priority decision should be explainable using the underlying signals.

Do not use opaque priority changes without recording their reason.

## No Permanent Starvation

A repository repeatedly deferred by higher-priority work must accumulate a review-due signal so it eventually receives attention.
