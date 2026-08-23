# Overseer Runtime

This directory is reserved for executable implementation of the Overseer runtime.

## Boundary

The Manus Desktop agent remains the primary autonomous runtime. Code placed here should provide deterministic tooling and state operations that the Manus agent can invoke.

## Planned modules

- `discovery/` — GitHub portfolio discovery and repository snapshots.
- `scanner/` — repository inspection primitives.
- `analysis/` — deterministic evidence extraction and scoring helpers.
- `findings/` — stable finding IDs and lifecycle operations.
- `portfolio/` — cross-repository relationship analysis.
- `state/` — persistent state and manifest operations.
- `reporting/` — owner-facing report generation.

Implementation must follow the control-plane protocols. It must not silently grant itself additional authority.
