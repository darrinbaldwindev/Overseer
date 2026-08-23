# Overseer Owner Reporting Protocol

## Objective

Turn portfolio analysis into concise, actionable information for the owner.

## Report Structure

### 1. Executive Status

State the overall portfolio condition in plain language.

### 2. What Changed

List material repository, architecture, dependency, deployment and finding changes since the previous cycle.

### 3. What Needs Attention

Rank actions by priority and explain why they matter.

### 4. What Improved

Identify findings that improved or resolved.

### 5. Recurring Problems

Highlight findings that remain unresolved across multiple scans.

### 6. Portfolio Intelligence

Report systemic issues, duplication, reuse opportunities and architectural relationships worth owner review.

### 7. Overseer Status

Report whether the Overseer cycle completed successfully, partially, or failed, including tooling or access limitations.

### 8. Next Actions

State what Overseer intends to inspect next and why.

## Noise Control

Do not repeatedly report unchanged low-severity findings unless:

- the owner requested them;
- their age becomes material;
- they contribute to a systemic problem;
- their severity/confidence changed;
- they block higher-level work.

## Evidence

Every material claim must be traceable to a repository snapshot, finding, scan or portfolio event.

## Language

Use direct language. Separate facts, risks and recommendations.

Avoid claiming certainty where evidence is incomplete.
