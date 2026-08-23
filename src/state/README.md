# State Layer

The state layer is responsible for reading and writing the schemas defined under `.overseer/schemas/` and maintaining append-only scan/finding/decision history.

Required properties:

- deterministic serialization;
- schema validation;
- atomic update semantics where supported;
- explicit failure reporting;
- no secret persistence;
- historical records are never silently deleted;
- evidence references must remain resolvable to the repository/ref/path available at the time of observation.

## Decision Ledger

`decision_ledger.py` provides the minimum record shape for owner-facing recommendations and decisions.

A recommendation must retain its evidence references so that a later reviewer can reconstruct why Overseer made it.

The ledger is a record of reasoning and authority, not a substitute for GitHub's authoritative repository history.
