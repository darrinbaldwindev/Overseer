# AgentOS Marketing — Level 2 Claim Delta

**Date:** 14 September 2026 (Australia/Brisbane)  
**Role:** Marketing Overseer  
**Canonical coordination:** `darrinbaldwindev/Overseer#49`

## Purpose

Reconcile the current AgentOS Level 2 marketing claim boundary against live repository evidence and define the exact evidence needed before Marketing may upgrade external claims or open the Founding Beta.

## Live evidence snapshot

AgentOS PR #104 remains **OPEN / DRAFT / UNMERGED**.

Exact head observed for this marketing cycle:

`71c463a77b31ebeac2bfe00da13c684512daccf7`

Current PR evidence supports a bounded governed Windows/PowerShell foundation, including a fixed operation catalogue, approved-root enforcement, non-interactive/non-elevated execution, timeout/output bounds, execution evidence and authority/approval fail-closed behavior at the stated scope.

The PR also records material unresolved limits:

- project-file mutation remains **AMBER** because a stale-ownership race can allow publish/success-receipt persistence after ownership has effectively been lost;
- prepared-write recovery has the same ownership-gap class;
- authenticated transport and canonical grant lookup are not yet wired into admission;
- emitted admission state is not yet sufficient for the existing non-PowerShell local-wake path;
- physical Windows acceptance was performed only on an older predecessor head, not the current runtime-changing head;
- no exact-head independent Green PASS is established for the current head;
- no independent PRS PASS is established for the current head;
- the PR remains draft and mutation must not be enabled.

## Marketing claim status

### PROVEN / safe now

**Architectural/product-direction wording:**

> AgentOS is being built around governed execution rather than simply giving AI unrestricted computer access.

**Narrow implementation wording:**

> AgentOS currently has a bounded governed Windows/PowerShell worker foundation under active development, with explicit authority and execution evidence at a limited operation scope.

These descriptions must not be expanded into end-to-end autonomy or Level 2 completion claims.

### NEARLY PROVEN / acceptance-gated

The following remain advanced but not public present-tense capability claims:

- controlled project-file mutation;
- inspect → modify → test → verify workflows;
- persistent/recoverable Level 2 development work;
- exact mission/task/worker/result correlation across the full runtime path;
- dependable duplicate/replay protection around mutations;
- physical-Windows current-head acceptance.

### NOT YET SUPPORTABLE

Do not publicly claim that AgentOS:

- safely controls a Windows PC autonomously end-to-end;
- is already a complete Level 2 governed development worker;
- guarantees every result is verified;
- always recovers safely after crashes or interrupted writes;
- completely prevents duplicate side effects;
- provides proven current-head stop/revoke semantics for every in-flight task;
- has current-head Green + PRS assurance for the full Level 2 path.

## Exact promotion gate

Marketing may consider promoting Level 2 execution language only after repository evidence shows, on the same exact candidate head:

1. kernel-enforced ownership remains valid through publish/recovery/success-receipt persistence;
2. stale-owner/success-receipt and successor-displacement adversarial cases fail closed;
3. runtime admission is bound to canonical authenticated identity + grant evidence;
4. exact task/mission/worker/result correlation is demonstrated through the real runtime path;
5. controlled mutation, interruption/restart recovery and duplicate/replay behavior pass exact-head tests;
6. physical Windows acceptance is rerun on that exact runtime-changing head;
7. full CI/test/audit evidence passes at that same head;
8. independent Green passes the exact head;
9. independent PRS passes after Green, without self-certification.

Only then should the Founding Beta entry gate be reconsidered.

## Founding Beta status

**HOLD.**

The beta message remains valid as positioning but not as an activation signal:

**“Give AgentOS a real job.”**  
**“Stay in control. See what it did.”**

The beta should open only when the first testers can safely exercise real jobs under current-head proof, including permission denial, containment, interruption/recovery, replay/duplicate resistance, evidence comprehension and independent verification.

## Highest-value Marketing action while blocked

Do not spend effort inventing stronger capability copy. Prepare acquisition assets around the *problem and promise* rather than unsupported completion claims:

- problem: AI can act, but users need authority, evidence and recovery;
- promise: AgentOS is being built to put governed execution around real AI work;
- proof invitation: Founding Beta testers will be asked to bring real jobs and test whether the controls and evidence actually hold.

No public activation, paid campaign or beta recruitment should occur until the technical beta entry gate is cleared.

## Status

**Marketing:** PREPARED / CLAIMS HELD TO EVIDENCE  
**Founding Beta:** HOLD  
**Publication:** NOT ACTIVATED  
**Overall AgentOS GREEN:** NOT ISSUED
