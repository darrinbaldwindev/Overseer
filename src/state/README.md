# State Layer

The state layer is responsible for reading and writing the schemas defined under `.overseer/schemas/` and maintaining append-only scan/finding history.

Required properties:

- deterministic serialization;
- schema validation;
- atomic update semantics where supported;
- explicit failure reporting;
- no secret persistence;
- historical records are never silently deleted.
