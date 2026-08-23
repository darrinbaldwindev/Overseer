# Overseer Knowledge Model

## Purpose

Define the persistent entities Overseer uses to reason about repositories across time.

## Entities

### Repository

Represents a GitHub project and its current portfolio state.

Key fields:

- stable GitHub repository ID;
- full name;
- default branch;
- permissions;
- project classification;
- current health;
- current scan state.

### Snapshot

Represents a repository at an exact commit/ref and scan timestamp.

A snapshot is immutable once recorded.

### Finding

Represents an evidence-backed observation, risk, defect or recommendation tracked across scans.

### Finding Event

Represents a state transition for a finding, such as NEW, REGRESSED or RESOLVED.

### Component

Represents a meaningful subsystem, service, package, application, workflow or infrastructure unit discovered in a repository.

### Dependency

Represents an internal or external dependency used by a component.

### Relationship

Represents a meaningful connection between portfolio entities.

Examples:

- repository depends_on repository;
- repository shares_component repository;
- repository duplicates repository;
- repository supersedes repository;
- component uses dependency;
- finding affects component.

### Scan

Represents one complete or partial Overseer inspection cycle.

## Evidence Principle

The knowledge model stores observations and references, not unsupported conclusions.

Every material finding must be traceable to a scan and repository snapshot.

## Temporal Principle

Current state is a view over historical events. Historical evidence must remain recoverable.

## Confidence Principle

Confidence belongs to individual observations and findings. It must not be inferred from severity.

## Relationship Confidence

Cross-repository relationships should include confidence:

- High: directly demonstrated.
- Medium: strongly supported.
- Low: plausible candidate requiring validation.

Low-confidence relationships must never be presented as established architecture.
