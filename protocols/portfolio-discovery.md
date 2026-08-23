# Portfolio Discovery Protocol

## Objective

Discover the complete set of GitHub repositories available to the authenticated Overseer identity without relying on a hard-coded list.

## Discovery Rules

1. Query the authenticated GitHub identity for accessible repositories.
2. Capture repository identity, visibility, permissions, default branch and archive status.
3. Include repositories where the identity has sufficient inspection access.
4. Record repositories that cannot be inspected and the reason.
5. Compare the result with the previous portfolio registry.

## Portfolio Changes

Classify repository-level changes as:

- ADDED
- REMOVED_FROM_ACCESS
- RENAMED
- ARCHIVED
- UNARCHIVED
- DEFAULT_BRANCH_CHANGED
- PERMISSION_CHANGED
- UNCHANGED

## No Hard-Coding

Known repositories may be used as an initial baseline, but discovery must remain authoritative. New repositories must automatically enter the candidate scan queue according to policy.

## Priority

1. New repositories.
2. Repositories with critical/high historical findings.
3. Repositories with material changes since the last scan.
4. Repositories with failed or incomplete previous scans.
5. Remaining repositories according to scan cadence.

## Completion

Portfolio discovery is complete only when the discovery result and any limitations have been persisted or explicitly reported as unable to be persisted.
