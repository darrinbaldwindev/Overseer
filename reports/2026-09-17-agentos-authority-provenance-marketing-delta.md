# AgentOS — Authority Provenance Marketing Delta

**Date:** 2026-09-17 AEST  
**Task:** M-A051  
**Status:** COMPLETE / CLAIM BOUNDARY

## Fresh state
AgentOS #104 exact head at scan: `e59eea89021b89631fac865d6610f927e4103ef0`, OPEN/DRAFT/UNMERGED. Exact-head AgentOS Tests `35192316311` completed SUCCESS.

The current lineage preserves source-backed `authority_evidence_id` for authority-admitted PowerShell work and fails closed when required authority provenance is absent before receipt construction.

## What this proves
Within the tested bounded path, a receipt for authority-admitted PowerShell work does not silently invent or discard the authority-evidence identifier expected by that path.

This is valuable because evidence can remain correlated with the authority material supplied to the admission seam.

## What this does NOT prove
It does not establish:
- that the actor was authenticated by a real canonical runtime authentication source;
- that a canonical grant resolver performed the grant lookup;
- that the grant was valid outside the bounded supplied context;
- that authority remained valid through every later mutation/recovery step;
- SG-01 or end-to-end SG-02 closure;
- SG-08 closure;
- physical Windows acceptance;
- Green or PRS;
- production autonomy.

## Safe wording
> **The bounded Windows worker now preserves authority-evidence provenance through its tested admitted receipt path and fails closed when that required provenance is missing. End-to-end authenticated authority admission remains separately gated.**

## Unsafe wording
Do not say:
- `AgentOS authenticates every Windows action.`
- `Every action is cryptographically authorised.`
- `Authority is fully verified end to end.`
- `Permissions cannot be bypassed.`
- `The Windows worker is now safe for autonomous file mutation.`

## Marketing principle
**Provenance is not authentication. A receipt that correctly points to supplied authority evidence is stronger evidence plumbing, not proof that the upstream identity/grant source is real or complete.**
