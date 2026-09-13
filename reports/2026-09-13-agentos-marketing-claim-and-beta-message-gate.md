# AgentOS Marketing Claim & Beta Message Gate — 2026-09-13

**Owner:** Marketing Overseer / ChatGPT Overseer  
**Canonical coordination:** `darrinbaldwindev/Overseer#49`  
**Status:** ACTIVE / NOT PUBLISHED  
**Technical P0:** AgentOS Level 2  
**Strategic end-state:** Level 5

## Purpose

Give Marketing a deterministic way to upgrade claims only when repository/runtime evidence crosses named proof gates.

This document does not certify technical completion. Product/Engineering/Green/PRS evidence controls status.

## Current safe positioning

### Public-safe now

- **AgentOS is being built around governed AI execution.**
- **AgentOS is designed to coordinate models, agents and tools while keeping the user in control.**
- **AgentOS is provider/model neutral by direction and architecture.**
- **Give AgentOS a real job.**
- **Stay in control. See what it did.**

### Use with scope qualifier

- AgentOS current development work includes a bounded governed Windows/PowerShell worker on draft lineage.
- Current bounded operations on PR #104 include repository status/diff, tests/audits and process/service inspection.
- Successful governed execution is designed to retain stdout/stderr/exit-code evidence and require receipt + verification before returning VERIFIED at that bounded scope.

Do not collapse these bounded statements into a broad current claim that AgentOS controls Windows autonomously end-to-end.

---

## Claim ladder

| Claim area | Current status | Current safe wording | Upgrade evidence required | Future wording once evidence passes |
|---|---|---|---|---|
| Governed execution | PROVEN as architecture/current bounded direction | “Built around governed execution rather than unrestricted AI access.” | Existing architecture + active governed worker evidence | Keep; broaden only with shipped runtime scope |
| Windows inspection | NEARLY PROVEN / bounded | “Current development includes bounded governed Windows inspection operations.” | exact-head CI + physical Windows acceptance + Green/PRS | “AgentOS can inspect approved Windows/repository state under governed permissions.” |
| Controlled file mutation | NOT YET SUPPORTABLE | Do not claim current file-edit autonomy | approved-root canonical containment; atomic write; mutation receipt; rollback/recovery; exact correlation; Green + PRS | “AgentOS can make approved project-file changes and verify them.” |
| Inspect→modify→test→verify | NOT YET SUPPORTABLE | Describe as Level 2 target only | end-to-end fixture acceptance on exact head; receipts for mutation + tests; independent assurance | “Give AgentOS a bounded development job: it can inspect, edit, test and verify within approved scope.” |
| Recovery | NOT YET SUPPORTABLE | “Recovery is a design/proof target.” | crash/partial-write/result-write/restart acceptance; checkpoint/reconciliation evidence | “AgentOS can resume or reconcile supported interrupted jobs without silently claiming completion.” |
| Duplicate protection | NOT YET SUPPORTABLE | “Duplicate/replay protection is a proof target.” | idempotency/replay/concurrency tests including side effects; PRS false-GREEN challenge | “AgentOS protects supported governed actions against duplicate execution.” |
| Verification | NEARLY PROVEN at bounded components | “AgentOS is designed to separate execution from verification.” | exact semantics for VERIFIED + independent Green evidence across supported job type | “AgentOS shows evidence and independently verifies supported job outcomes before calling them VERIFIED.” |
| PRS assurance | PRODUCT DIRECTION / active architecture | “PRS/Henry independently challenges evidence and false-GREEN conditions in the AgentOS governance model.” | shipped user-facing assurance path + exact evidence | “Henry independently challenges supported job results before final assurance.” |
| Stop/revoke | NOT YET SUPPORTABLE broadly | “Stop/revoke is a beta proof target.” | worker-local stop; queue cancellation; authority revoke; external side-effect semantics tested and disclosed | “You can stop or revoke supported AgentOS work, with clear limits where an external action is already committed.” |
| Credential safety | PROVEN architecture / NOT fully proven end-to-end | “AgentOS architecture uses credential references and excludes secrets from specified persisted operational state.” | broker/runtime enforcement; model/tool visibility tests; log redaction; connector scope proof | “AgentOS keeps supported credentials out of model-visible/job-visible state and exposes scoped revocation.” |
| Cost governance | PRODUCT DIRECTION / partial systems | “AgentOS is designed to manage cost alongside capability and quality.” | runtime budget enforcement + receipts | “Set bounded budgets for supported jobs/providers and AgentOS enforces them.” |
| Night Shift / unattended work | NOT YET SUPPORTABLE generally | Do not claim broad unattended autonomy | scheduler + governed worker + recovery + stop/revoke + evidence + physical acceptance | “Let supported AgentOS jobs run during approved Autonomy Hours and review the evidence afterward.” |
| Provider neutrality | PROVEN architecture direction; integration coverage varies | “AgentOS is designed to coordinate free, local and paid AI rather than lock you to one provider.” | provider-specific shipped integrations for named claims | Name only integrations actually shipped/tested |

---

## Founding Beta message gate

### Before Wave 0 — HOLD

Do not recruit externally until the Founding Beta entry gate passes.

Marketing must have current evidence for:

1. pinned beta build;
2. shipped-feature matrix;
3. known-limitations list;
4. install/setup path on intended hardware;
5. stop/revoke instructions;
6. permission explanation;
7. no unresolved S0 trust issue;
8. first real-job path internally proven;
9. false-success handling;
10. privacy/data-handling notice;
11. incident/support route;
12. internal 2–3 person Day 0 dry run.

### Wave 0 recruitment language

Primary:

> **AgentOS Founding Beta — Give AgentOS a real job.**

Supporting:

> Bring something you genuinely need done. We want to learn whether AgentOS keeps you in control, shows what happened, and handles failure honestly.

Do not recruit with “fully autonomous”, “hands-free Windows”, “never fails”, “always verified”, “guaranteed savings” or “replaces all your AI subscriptions”.

### Wave 0 proof questions

- Did the tester understand what AgentOS was about to do?
- Did they understand what it was allowed to access/change?
- Did they understand what it could not do?
- Did they know how to stop/revoke it?
- Did the result distinguish executed vs verified?
- Was evidence understandable?
- Did Green verification increase trust?
- Did PRS challenge expose a real issue or increase confidence?
- What happened after an intentional failure/restart?
- Did the tester voluntarily give AgentOS a second real job?

### Beta claim upgrade rule

A claim may become **BETA-PROVEN** only when:

- it is exercised by real external testers on a pinned build;
- the supporting instrumentation/evidence is retained;
- failures and exclusions are counted, not discarded;
- the exact scope is stated;
- Product/Engineering/Green/PRS do not contradict the interpretation.

---

## Commercial message discipline

Owner-current ladder for Marketing:

**Free → $29 → $99 → subscriptions**

- `$99` = expected/mainstream sale.
- `$29` = second-bite conversion option for someone not ready for `$99`.
- Do not position `$29` as “the normal plan”.
- Do not call the full product “basic”.
- Universal trust/security controls must not be deliberately weakened to force an upgrade.

### Pricing research in beta

Ask perceived value/willingness-to-pay before showing the proposed price ladder. Then reveal the ladder and ask again. Do not tell testers in advance that `$99` is the expected sale.

---

## Competitive discipline

Do not differentiate AgentOS merely on:

- multi-model chat;
- MCP support;
- local models;
- local files;
- PowerShell/terminal access;
- browser automation;
- scheduled/background agents;
- command palette;
- clipboard/OCR conveniences.

Treat these as increasingly common capabilities.

Prioritise proof around:

- explicit bounded authority;
- durable mission state;
- evidence/receipts;
- independent verification;
- adversarial assurance;
- recovery;
- duplicate/replay protection;
- cost/capability controls;
- provider/model neutrality;
- useful coordination of free + paid AI.

---

## Content360 release rule

Content360 receives only an evidence-approved message packet containing:

- claim status;
- exact scope;
- proof source/date;
- expiry/recheck date where factual claims can go stale;
- prohibited extrapolations;
- channel objective;
- required approval/publication gate.

Content360 may optimise wording and format. It may not promote a claim status or invent product facts.

---

## Next Marketing action

While AgentOS Level 2 proof remains technically blocked, keep beta/recruitment assets prepared but unpublished and move commercial work to GlobalShopCo + Shopify→eBay using exact SKU/freight/marketplace evidence gates.
