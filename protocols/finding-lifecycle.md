# Finding Lifecycle

## Objective

Ensure Overseer can track a problem across repeated scans without creating duplicate noise or losing history.

## Lifecycle

```text
CANDIDATE
   |
   v
VALIDATED
   |
   +--> NEW
   |
   +--> MATCH EXISTING
             |
             +--> UNCHANGED
             +--> IMPROVED
             +--> REGRESSED
             +--> REOPENED
             +--> RESOLVED
```

## Candidate Matching

Match candidates using, in order:

1. stable finding ID;
2. normalized repository + area + location + problem signature;
3. semantic similarity when exact matching is unavailable.

Semantic matching must not override strong contradictory evidence.

## Status Definitions

- NEW: first validated observation.
- UNCHANGED: still materially the same condition.
- IMPROVED: condition remains but evidence shows meaningful reduction in impact/risk.
- REGRESSED: condition materially worsened.
- RESOLVED: evidence indicates the condition is no longer present.
- REOPENED: previously resolved condition has returned.

## Resolution Rule

Do not mark a finding RESOLVED merely because the relevant file changed or a commit message claims a fix. Require evidence that the underlying condition is gone or materially addressed.

## Reopening Rule

If a resolved finding returns, retain the original ID and mark it REOPENED. Record the new evidence and the change that caused the regression where determinable.

## History Rule

Every status transition is recorded with timestamp, scan reference, evidence summary, and confidence.

Historical records are append-only.
