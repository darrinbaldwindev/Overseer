# Scanner Layer

The scanner layer converts repository metadata and tree contents into structured evidence for the Manus Overseer.

## Current capability

- deterministic tree/path reconnaissance;
- conservative project-language signals;
- package/dependency manifest detection;
- test/CI/infrastructure/documentation signals;
- entrypoint candidates.

## Planned capability

- exact repository snapshots;
- file-level evidence extraction;
- workflow and dependency inspection;
- change-aware scanning;
- security evidence extraction;
- scan result serialization.

The scanner reports evidence. It does not decide severity or make owner decisions.
