# Control-Plane Versioning

## Purpose

Ensure the Manus Desktop Overseer and GitHub control plane can determine exactly which governing instructions were used for a scan.

## Required Scan Metadata

Every completed scan should record:

- Overseer control-plane commit;
- configuration version;
- applicable protocol versions or content hashes;
- target repository/ref;
- scan trigger;
- inspection coverage;
- resulting confidence.

## Authority

The GitHub `Overseer` repository is the authoritative control plane for the Manus Desktop Overseer. The runtime must not silently substitute local or stale instructions when current control-plane files are available.

## Change Safety

Changes to `OVERSEER.md`, `MANUS-INTEGRATION.md`, `config/overseer.yml`, safety protocols, or authority protocols are governance changes. They must be reviewed as control-plane changes and must not be generated as an incidental side effect of an ordinary repository scan.

## Runtime Mismatch

If the runtime's loaded control-plane version differs from the version recorded in a persisted scan manifest, report the mismatch. Do not silently combine findings produced under incompatible policies.

## Self-Supervision Boundary

Overseer may report defects in its own control plane. It may propose improvements. It may not autonomously grant itself additional authority by modifying its governing policy.
