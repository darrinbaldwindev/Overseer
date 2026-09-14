# AgentOS Marketing Claim + Frontend Delta — 14 September 2026

## Purpose

Reconcile the newest live AgentOS Level 2 and Frontend Overseer evidence before any marketing claim, Founding Beta, Content360 or acquisition state is promoted.

## Exact live evidence

### AgentOS Level 2 — PR #104

- PR: `darrinbaldwindev/AgentOS#104`
- State: **OPEN / DRAFT / UNMERGED**
- Exact head reviewed and post-scan reconfirmed: `9f53df16ae37ee6a86e66d2a808ca7f62f203d76`
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

The AgentOS Frontend Overseer owns detailed interaction design. Marketing supplies promise/claim/trust boundaries and does not create a competing UI product authority.

### PR #110 — Frontend batch + trust-state contract

- State: **OPEN / DRAFT / UNMERGED**
- Exact head reviewed: `b43bdf1ab8c148af0f1e4bbed3b662b89013ad7b`
- AgentOS Tests #1010 / `34814554479` = SUCCESS.
- Project Overseer Wake #362 / `34814554467` = SUCCESS.
- This is documentation/product-contract evidence, not proof that the described complete frontend is shipped.

### PR #111 — ordinary-user Basic Chat presentation

- State: **OPEN / DRAFT / UNMERGED**
- Post-execution fresh-scan head: `a639753edfbb1e9e52bea4da38597f0800279921`.
- Scope includes ordinary-user Chat copy, truthful Stop-requested semantics, safe next-action errors, a bounded `What happened` evidence summary and explicit completion-check vs independent-assurance separation.
- It explicitly avoids synthesizing generic `VERIFIED`, Henry/PRS PASS or confirmed termination where canonical state does not support them.
- It refuses to invent a full Evidence Timeline or synthetic Jack permission card where required canonical fields are absent.
- Predecessor head `a3b5f3f92936f5dfa2dc0da1dbbac5800cc20eaa` had AgentOS Tests #1012 FAILURE due inherited Ubuntu SIGINT lifecycle behavior; Windows Basic Chat lifecycle and UI-specific assertions passed.
- Current exact head `a639753...` has **two completed successful AgentOS Tests runs**: #1019 / `34820034755` and #1020 / `34820035998`.

Marketing classification for PR #111 is therefore upgraded from CI-AMBER to:

**IMPLEMENTATION-ADVANCED / EXACT-HEAD CI PASS / DRAFT-UNMERGED / NOT SHIPPED.**

This is a frontend implementation/evidence upgrade only. It does not clear AgentOS Level 2, Founding Beta or production-release gates.

## Claim decisions

### Safe / unchanged

> AgentOS is being built around governed execution rather than simply giving AI unrestricted computer access.

Narrow engineering statement:

> Current AgentOS development includes bounded governed execution primitives, exact-correlation checks and fail-closed authority/admission regressions on active draft lineages.

This must not imply release readiness, full Windows autonomy or a completed Level 2 worker.

### Frontend claim update

The current PR #111 exact head now has successful exact-head CI for its draft presentation slice. Marketing may describe that work internally as **tested draft frontend implementation**.

Marketing must still not say the capability is shipped, production-ready, fully integrated, or evidence-complete across Jack/Green/Henry because canonical runtime fields and broader Level 2 gates remain incomplete.

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

Frontend exact-head CI success is welcome but cannot substitute for the Level 2 ownership/admission/Windows reliability/physical acceptance/Green/PRS entry gate. PR #104 itself remains exact-head CI-failing on Windows.

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
2. Recognize PR #111 as exact-head CI-passing draft frontend work, while preserving `NOT SHIPPED`.
3. Treat PR #104's exact-head Windows failure as a product-trust signal; do not smooth it over in UX or marketing.
4. Let Frontend continue honest incomplete/unknown/recovery states rather than optimistic completion states.
5. Re-run the claim gate after any new PR #104 or #111 head and after physical Windows, Green or PRS movement.

## Publication state

**PREPARED / FRONTEND DRAFT CI-PASS / NOT SHIPPED / FOUNDING BETA HOLD / NO PAID CAMPAIGN / NO OVERALL GREEN.**
