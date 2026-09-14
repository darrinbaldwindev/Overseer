# AgentOS Marketing Claim + Frontend Delta — 14 September 2026

## Purpose

Reconcile the newest live AgentOS Level 2 and Frontend Overseer evidence before any marketing claim, Founding Beta, Content360 or acquisition state is promoted.

## Exact live evidence

### AgentOS Level 2 — PR #104

- PR: `darrinbaldwindev/AgentOS#104`
- State: **OPEN / DRAFT / UNMERGED**
- Exact head reviewed: `9f53df16ae37ee6a86e66d2a808ca7f62f203d76`
- Latest narrow implementation at that head adds regression coverage for exact delivery/request/task/mission/wake/authority-evidence correlation and fail-closed untrusted-issuer/out-of-policy capability admission.
- Predecessor exact head `a4d1a1baa104d76ae7667d5e079df4ffe87688a0` had AgentOS Tests #978 / `34811602354` SUCCESS.
- Current exact-head AgentOS Tests #1014 / `34816222109` = **FAILURE**.
- Ubuntu / Node 22 job = SUCCESS.
- Windows / Node 26 job = FAILURE.
- Failure: `tests/remote-scheduler-execution.test.mjs` — `eight real scheduler processes cannot execute a delivery twice`.
- The observed Windows run produced one `COMPLETED` delivery and multiple duplicate/active-claim denials, but one process failed with `EPERM: operation not permitted, mkdir ...\state\agentos.json.lock`; the test therefore failed. This is not treated as proof of a duplicate side effect, but it is exact-head cross-platform failure evidence and blocks any stronger reliability claim.

### Remaining Level 2 gates

Still unresolved / not cleared by the new correlation tests:

1. continuous kernel-enforced ownership through mutation publish/recovery/success receipt;
2. bindable canonical authenticated transport + grant source at admission;
3. exact-head Windows reliability after the new CI failure;
4. current runtime-changing physical Windows acceptance;
5. independent Green exact-head PASS;
6. independent PRS after Green;
7. end-to-end Level 2 acceptance without borrowing evidence from predecessor heads.

## Frontend Overseer reconciliation

The AgentOS Frontend Overseer is now active and should own detailed interaction design. Marketing supplies promise/claim/trust boundaries and should not create a competing UI product authority.

### PR #110 — Frontend batch + trust-state contract

- State: **OPEN / DRAFT / UNMERGED**
- Exact head reviewed: `b43bdf1ab8c148af0f1e4bbed3b662b89013ad7b`
- AgentOS Tests #1010 / `34814554479` = SUCCESS.
- Project Overseer Wake #362 / `34814554467` = SUCCESS.
- This is documentation/product-contract evidence, not proof that the described complete frontend is shipped.

### PR #111 — ordinary-user Basic Chat presentation

- State: **OPEN / DRAFT / UNMERGED**
- Exact head reviewed: `a3b5f3f92936f5dfa2dc0da1dbbac5800cc20eaa`
- Scope has advanced beyond copy-only work into a bounded user-facing evidence summary while keeping completion checks distinct from independent assurance.
- Current design explicitly avoids synthesizing generic `VERIFIED`, Henry/PRS PASS or confirmed termination where canonical state does not support them.
- It also refuses to invent a full Evidence Timeline or synthetic Jack permission card where required canonical fields are absent.
- AgentOS Tests #1012 / `34814629921` = **FAILURE** overall.
- The Windows Basic Chat lifecycle job succeeded and the ordinary Basic Chat UI assertions in the main test job passed.
- The failing Ubuntu test is the inherited Basic Chat lifecycle SIGINT assertion (`signalCode` observed `SIGINT` rather than expected `null`).

Marketing classification for PR #111: **IMPLEMENTATION-ADVANCED / CI-AMBER / NOT SHIPPED**.

## Claim decisions

### Safe / unchanged

**PROVEN as product/architecture direction at exact stated scope:**

> AgentOS is being built around governed execution rather than simply giving AI unrestricted computer access.

**PROVEN narrow engineering evidence:**

> Current AgentOS development includes bounded governed execution primitives, exact-correlation checks and fail-closed authority/admission regressions on active draft lineages.

This wording must not imply release readiness, full Windows autonomy or a completed Level 2 worker.

### Improved but not promotable to broad capability

The newest admission-correlation tests materially improve evidence that identifiers and authority provenance are preserved or fail closed in the tested path. Classification: **NEARLY PROVEN / integration-gated** for the broader real-runtime admission story.

Frontend PR #111 materially improves the truthful user presentation of local/test/background state, Stop semantics, completion checks and assurance boundaries. Classification: **PRODUCT IMPLEMENTATION ON DRAFT LINEAGE / CI-AMBER**, not shipped capability.

### NOT YET SUPPORTABLE

Do not claim that AgentOS currently:

- safely controls Windows autonomously end-to-end;
- provides a completed dependable Level 2 development worker;
- guarantees no duplicate execution or side effects;
- always recovers safely from crashes/contention;
- guarantees immediate Stop/Revoke effectiveness;
- guarantees every result is independently verified;
- has current-head Green + PRS assurance;
- exposes a complete Evidence Timeline or full Jack/Henry permission/assurance UX in the shipped product.

## Founding Beta decision

**HOLD remains mandatory.**

Reasons now include both the pre-existing Level 2 ownership/admission/assurance gates and the fresh exact-head Windows CI failure at PR #104.

The Frontend Overseer may continue preparing the controlled tester experience, but UI readiness must never substitute for technical entry-gate evidence.

## Marketing ↔ Frontend operating boundary

### Marketing owns
- evidence-safe promise and positioning;
- claim categories and promotion gates;
- beta expectation language;
- trust objections and plain-language answers;
- acquisition/content wording;
- commercial implications of UX gaps.

### Frontend Overseer owns
- screen hierarchy and interaction implementation;
- Simple / Essentials / Tech Head presentation;
- Chat, Inbox, Jobs, Palette and Evidence Timeline interaction design;
- Jack/Isla/Henry presentation;
- accessibility/responsive states;
- fail-closed UI mappings from canonical state.

### Canonical runtime systems own
- execution truth;
- authority and permission truth;
- mission/job state;
- receipts/evidence;
- Green;
- PRS;
- Stop/Revoke effectiveness.

## Immediate recommendations

1. Keep Founding Beta recruitment assets prepared but unsent.
2. Treat PR #104 exact-head Windows failure as a product-trust signal; do not smooth it over in UX or marketing.
3. Let Frontend continue building honest incomplete/unknown/recovery states rather than optimistic completion states.
4. Marketing should focus next on competitor trust/control differentiation and beta/trust messaging, not duplicate Frontend implementation.
5. Re-run the claim gate after any new PR #104 head, Windows CI result, physical acceptance, Green or PRS result.

## Publication state

**PREPARED / NOT PUBLICLY ACTIVATED / FOUNDING BETA HOLD / NO PAID CAMPAIGN / NO OVERALL GREEN.**
