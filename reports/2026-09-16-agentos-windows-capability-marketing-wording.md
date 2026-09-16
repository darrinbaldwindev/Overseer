# AgentOS — Windows Capability Marketing Wording

**Date:** 2026-09-16 AEST  
**Task:** M-A050  
**Status:** COMPLETE / CLAIM-SAFE WORDING / NO READINESS PROMOTION

## Fresh evidence context
Frontend #111 has advanced beyond the earlier Cycle-012 checkpoint and now includes further fail-closed Jobs/project isolation work. Current exact frontend head at scan: `f89dd5cb49ffa7efe0649ca2aee433d19cf0fd34`; exact-head AgentOS Tests `35097976181` completed SUCCESS.

AgentOS #104 current exact head at scan: `86005652d7454c0be4862d49846bd5bccc1daec7`; exact-head AgentOS Tests `35093331168` completed SUCCESS. Its PR description still explicitly says project-file mutation remains AMBER/BLOCKED, SG-08 continuous ownership is not proven, authenticated transport/canonical grant lookup are not wired, and physical Windows acceptance is separate.

## Safe bounded wording
> **AgentOS has a tested bounded Windows/PowerShell worker foundation under active development. Current readiness presentation requires explicit host/tool evidence and fails closed when required evidence is missing or mismatched.**

Where detail is useful:
> **The bounded worker currently exposes a small allowlisted PowerShell operation set and preserves authority/evidence correlation through the tested path. This is not proof of unrestricted computer control or project-file mutation readiness.**

## What exact-head CI supports
CI supports statements about tested code on the exact tested head. It does not establish:
- physical Windows acceptance;
- safe project-file mutation;
- end-to-end authenticated authority admission;
- Green PASS;
- PRS PASS;
- unrestricted PowerShell;
- production autonomy;
- full Windows control.

## Frontend language
Safe:
- `Windows capability evidence is available for this environment.`
- `Required tool identity is confirmed.` when canonical evidence supports it.
- `Physical acceptance not established.`
- `Project-file mutation readiness unknown.`

Unsafe:
- `Windows ready` as an umbrella status;
- `AgentOS can safely control your Windows PC`;
- `Fully verified` from CI;
- `Safe to edit files` from tool capability alone;
- `Stopped` from a Stop request alone.

## Marketing ladder
1. bounded worker implementation + exact-head CI;
2. physical Windows acceptance for exact head/host;
3. mutation-safety ownership/recovery/concurrency gates;
4. independent Green on unchanged eligible head;
5. PRS after Green;
6. only then broader readiness language within proven scope.

## Current classification
**BOUNDED WINDOWS FOUNDATION / EXACT-HEAD CI PASS / MUTATION BLOCKED / PHYSICAL ACCEPTANCE SEPARATE / NOT SHIPPED AS FULL WINDOWS AUTONOMY.**