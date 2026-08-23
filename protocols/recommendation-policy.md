# Overseer Recommendation Policy

## Purpose

Define how Overseer turns evidence into owner recommendations without confusing recommendations with decisions.

## Recommendation Classes

### R0 — Informational

No action required. Record useful context.

### R1 — Monitor

A condition warrants continued observation but evidence does not justify intervention.

### R2 — Recommended Action

Evidence supports a concrete engineering, documentation or process change.

### R3 — Owner Decision Required

The evidence indicates a material commercial, architectural, financial, legal, security or product decision.

Overseer recommends and explains; the owner decides.

## Evidence Requirements

A recommendation must identify:

- evidence;
- affected repository/project;
- confidence;
- expected benefit;
- risk of acting;
- risk of not acting;
- dependencies;
- whether owner approval is required.

## No False Certainty

Do not state that a recommendation is mandatory unless a higher-level policy explicitly makes it mandatory.

Separate:

```text
FACT
OBSERVATION
INFERENCE
RECOMMENDATION
DECISION
```

## Cross-Repository Recommendations

When recommending consolidation or shared infrastructure, compare:

- actual duplication;
- ownership boundaries;
- security implications;
- coupling introduced;
- operational cost;
- migration complexity;
- reversibility.

Similarity alone is insufficient justification for consolidation.

## Action Boundary

Creating an issue or draft proposal may be automated where authorized. Production changes, deletion, commercial commitments and other consequential actions require the authority specified by the applicable project policy.
