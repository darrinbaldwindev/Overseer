# Overseer Scan Manifest

## Purpose

A scan manifest makes every Overseer run reproducible and auditable.

## Required Fields

```yaml
schema_version: 1
scan_id: OVR-SCAN-YYYYMMDD-HHMMSS
started_at: timestamp
completed_at: timestamp
control_plane_commit: git_sha
scan_engine_version: version
mode: observe_report
portfolio_discovery:
  status: complete|partial|failed
  repository_count: integer
repositories:
  - full_name: owner/name
    repository_id: github_id
    ref: commit_or_branch
    status: complete|partial|failed|skipped
    reason: optional
    findings_generated: integer
    findings_changed: integer
```

## Reproducibility

A future investigator should be able to determine:

- what Overseer version ran;
- what control-plane version governed it;
- what repositories were in scope;
- what exact refs were inspected;
- what failed or was skipped;
- how many findings were generated or changed.

## Partial Runs

A run may be partial. The manifest must identify the incomplete repositories and the reason.

## Idempotency

Re-running a scan against the same repository ref should not create duplicate findings solely because a new scan occurred.
