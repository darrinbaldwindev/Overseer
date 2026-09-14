# AgentOS Readiness Projection — Claim & Screen Acceptance

**Marketing task:** M-A032  
**Date:** 2026-09-15 AEST  
**Status:** COMPLETE / PRODUCT-TRUTH ACCEPTANCE CONTRACT / NO SHIPMENT CLAIM

## Purpose
Prevent Frontend, Marketing and Content360 from collapsing several materially different readiness states into one optimistic `Ready` label.

## Canonical four-state model
1. **Basic Chat availability** — whether the supplied canonical chat snapshot says the local chat surface is available.
2. **Windows host capability** — whether explicit canonical host/probe evidence supports the bounded host capability being presented.
3. **Physical Windows acceptance** — whether exact-head supervised physical-Windows acceptance evidence exists for the bounded workload represented.
4. **Project-file mutation readiness** — whether a canonical mutation-readiness source proves the governed project-file mutation lifecycle at the required assurance level.

These states are **not interchangeable and are not cumulative shortcuts**. In particular, host capability or physical Windows acceptance must never promote project-file mutation readiness.

## Current evidence anchor
Frontend PR #111 current exact head observed during this cycle: `429b6d5bc14b2790f1a9bace09b76e699cb88b8c`, OPEN / DRAFT / UNMERGED. Exact-head cross-platform workflow `34859721665` is SUCCESS. The prior Ubuntu SIGINT lifecycle regression is no longer controlling on this head.

Level 2 PR #104 current exact head observed during this cycle: `bbfee5221652c9bf0551ce5b31eb0b1cf6e78af1`, OPEN / DRAFT / UNMERGED, exact-head workflow `34857161932` SUCCESS. This contains materially stronger authority and ownership mechanics, but its evidence must not be borrowed into Frontend as a mutation-readiness PASS without canonical integration and independent assurance.

## Presentation acceptance
### Simple
- Use ordinary language.
- Never reduce the four states to one generic `Ready` badge.
- If evidence is missing, say so plainly: `Not confirmed yet` / `Readiness not established`.
- A successful chat surface must not imply Windows-worker or file-mutation readiness.

### Essentials
Show the four states separately where relevant. Each state should carry enough explanation to distinguish availability, capability, supervised acceptance and mutation safety. Show blockers/unknowns rather than hiding them.

### Tech Head
May expose canonical source type, exact head/SHA where applicable, evidence identifiers, timestamps/freshness and failure reason. Technical detail must not weaken fail-closed semantics.

## Fail-closed rules
Any of the following forces UNKNOWN/HOLD for the affected state:
- missing canonical source;
- stale evidence outside the accepted freshness boundary;
- task/mission/wake/head mismatch;
- contradictory evidence;
- local or DRY_RUN evidence presented as physical acceptance;
- physical acceptance presented as mutation readiness;
- CI success presented as product/assurance readiness.

## Allowed wording now
- `Basic Chat availability is reported from canonical chat state.`
- `Windows host capability is shown separately from physical acceptance.`
- `Physical Windows acceptance requires exact-head supervised evidence.`
- `Project-file mutation readiness is a separate governed state.`

## Prohibited shortcuts
- `AgentOS is ready` solely because CI is green.
- `Windows ready` from a local/DRY_RUN or hosted-runner test.
- `Files are safe to modify` from host capability or lifecycle tests.
- `Level 2 ready` from Frontend readiness projection.
- `Verified` when only one lower-level state is proven.

## Promotion gate
A state can be shown as PASS only from its own canonical evidence contract. Marketing and Content360 may describe the separation itself now; they may not promote an unproven state.

**Decision:** exact-head CI progress is real, but readiness remains a set of independently evidenced states. Founding Beta stays HOLD until the controlling Level 2 gates clear.