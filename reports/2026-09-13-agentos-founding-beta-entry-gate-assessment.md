# AgentOS Founding Beta — Entry Gate Assessment

**Date:** 2026-09-13
**Purpose:** Determine whether the current AgentOS implementation is ready to admit the first external Founding Beta testers (Wave 0).
**Status:** NOT YET READY FOR WAVE 0 / NARROW BLOCKER SET

## Executive decision

Do not recruit external Wave 0 testers yet.

The project has substantial deterministic implementation evidence, a Basic Chat release-candidate lineage, a governed remote/local bridge lineage, and a bounded Windows PowerShell worker lineage with current successful CI. However, the evidence required for safe external beta admission is incomplete in the areas that matter most to a real Windows user: physical-host acceptance, runtime hookup of the Windows worker, exact shipped-feature definition, onboarding/known-limitations presentation, and final beta security/privacy/incident handling.

The correct next target is not broader product development. It is a bounded **Founding Beta Wave 0 acceptance package** that proves a small, clearly declared capability envelope on a real Windows laptop.

## Evidence reviewed

### Current AgentOS main

Current main observed at assessment time:

`fd88a05754adf44dc5feb22952b2658c121b7207`

The latest main commit is documentation/research work and does not by itself establish external-beta runtime readiness.

### PR #87 — Basic Chat V1 RC

PR #87 remains open and draft.

It contains:
- Basic Chat local server/UI;
- loopback-only HTTP;
- chat to canonical local wake path;
- persistent conversation layout;
- pause/resume/stop;
- conversation restore without replay;
- prior deterministic test evidence.

Its own acceptance statement says it is **not V1 GREEN** and that independent adversarial review, physical Windows acceptance and PRS assurance remain pending.

### PR #91 — governed remote/local bridge

PR #91 remains open and draft.

Evidence includes:
- fail-closed admission;
- host eligibility;
- durable claims;
- stale-claim recovery classification;
- exact wake/task selection;
- serialized JSON persistence with revision CAS;
- Green failure blocking completed receipts;
- 348 local tests reported passing plus a successful historical exact-head CI run.

Its own limitations explicitly state:
- DRY_RUN fixture only;
- autonomy disabled;
- no authenticated remote transport / production writer;
- mobile-to-physical-Windows acceptance open;
- REMOTE PHYSICAL EXECUTION NOT PROVEN;
- no overall GREEN.

### PR #104 — governed bounded Windows PowerShell worker

PR #104 remains open and draft.

Bounded operations currently include:
- `repo.status`
- `repo.diff`
- `test.run`
- `audit.run`
- `process.list`
- `service.list`

Safety properties include:
- fixed operation catalogue;
- approved-root enforcement;
- non-interactive/non-elevated PowerShell;
- timeout and output bounds;
- evidence retention;
- zero invocation on authority/approval denial;
- receipt + verification required for VERIFIED.

The current observed head is:

`6b7aae6edd6f57ed5f9e44dfc4a6ee29a61ba238`

AgentOS Tests run `34732468678` completed successfully on this head.

But PR #104 deliberately does **not** enable scheduler pickup of PowerShell work and explicitly leaves physical Windows laptop acceptance as a separate gate.

## Founding Beta entry gate

### Gate A — exact beta build identity

**Status: RED**

A tester-facing build/ref has not yet been declared as the Wave 0 candidate. Current functionality is distributed across main and open draft PR lineages.

Required evidence:
- exact beta candidate SHA/ref;
- installation package/build identity;
- rollback/recovery instruction;
- declared shipped feature envelope.

### Gate B — install and first launch on real Windows

**Status: RED**

Repository and CI evidence do not establish clean installation and first-run success on a physical Windows laptop.

Required evidence:
- clean physical Windows install;
- launch from intended user path;
- uninstall/reinstall behavior;
- state/import behavior if relevant;
- no hidden developer-only prerequisites;
- receipt/log capture for install failure.

### Gate C — Basic Chat / first-job path

**Status: AMBER**

Basic Chat exists on the RC lineage and has deterministic tests, but physical acceptance is not proven.

Required Wave 0 acceptance:
- tester can open the intended UI;
- submit a bounded real job;
- understand status;
- pause/stop safely;
- restore conversation without replay;
- see a truthful outcome state.

### Gate D — governed Windows worker

**Status: AMBER-RED**

The bounded worker is well constrained and current CI passes, but runtime pickup is intentionally not connected and physical-host proof remains open.

Required evidence:
- canonical capability evidence replaces/reconciles synthetic probe;
- bounded DRY_RUN/runtime pickup wiring through existing scheduler/local-wake path;
- no alternate queue/scheduler/authority layer;
- physical Windows execution of the allowed operation set;
- denial = zero invocation;
- failure and timeout paths produce truthful states;
- duplicate/replay behavior proven;
- receipt-write / crash / recovery paths retain fail-closed behavior.

### Gate E — stop/pause/authority controls

**Status: AMBER**

Basic Chat declares pause/resume/stop and the worker lineage declares authority denial = zero invocation. External-user comprehension and physical behavior remain unproven.

Required evidence:
- one-click visible stop/pause for Wave 0;
- action does not continue unexpectedly after stop;
- user can identify when approval is required;
- denied approval cannot be bypassed;
- recovery after interruption is understandable.

### Gate F — false-success / assurance

**Status: AMBER**

Green/ledger/receipt protections exist in the active lineages, but no overall GREEN has been declared and arbitrary real-world objectives are not independently certified.

Wave 0 minimum:
- no completed/success state without required evidence;
- test a failed operation;
- test result-write/receipt-write failure;
- test Green failure;
- test unrelated task attribution;
- test duplicate/replay attempt;
- independent PRS/assurance review of exact beta head.

### Gate G — security and privacy

**Status: AMBER-RED**

The technical lineages show strong least-privilege intent, but the external beta requires a tester-facing security/privacy package tied to the actual build.

Required before recruitment acceptance:
- exact permissions requested by the build;
- what local files/data can be accessed;
- what leaves the device and when;
- provider/API-key handling;
- log/diagnostic contents and redaction rules;
- secrets exclusion;
- vulnerability reporting route;
- incident-response owner;
- known limitations and prohibited test data;
- beta terms/privacy review.

NDA is a separate decision. It is not a substitute for security/privacy controls.

### Gate H — beta onboarding content

**Status: AMBER**

The product concept is defined, but the tester-facing onboarding package must be locked against the exact beta feature envelope.

Use plain-language roles:
- Willow plans.
- Isla does the work.
- Jack watches permissions, risk and limits.
- Henry checks the result.

Before Wave 0, confirm:
- what AgentOS can do in this build;
- what it cannot do;
- how to stop it;
- how permissions work;
- how to report problems;
- what data not to use in beta;
- how the Operator completion reward works.

### Gate I — beta operations

**Status: AMBER**

The Founding Beta operating programme and readiness playbook exist, but the operational endpoints are not yet instantiated.

Required:
- tester intake form;
- screening/selection owner;
- help/support channel;
- bug/confusion/trust reporting channel;
- same-day S0/trust escalation route;
- Day 0/1/3/7/14 messaging;
- acceptance/waitlist/rejection templates;
- incentive fulfilment process;
- exit survey/interview mechanism.

## Recommended Wave 0 capability envelope

Do not wait for every future AgentOS capability.

Wave 0 should deliberately test a narrow, real product slice:

1. Install/launch on Windows.
2. Basic Chat.
3. One bounded local/repository job path.
4. Explicit authority/permission step where appropriate.
5. Pause/stop.
6. Evidence/verification outcome.
7. Recovery from one safe interruption/failure.
8. Conversation/state restoration without replay.

Exclude from Wave 0 unless independently proven on the exact build:
- broad autonomous Windows control;
- unrestricted shell;
- production remote execution;
- broad Night Shift claims;
- unattended consequential actions;
- arbitrary email/browser/desktop action;
- savings/ROI guarantees.

## Smallest safe path to first testers

### Step 1 — choose one exact beta candidate lineage

Prefer convergence around the strongest existing Basic Chat + remote bridge + bounded Windows worker lineage rather than another new architecture.

### Step 2 — produce a Wave 0 feature manifest

Every tester-visible capability must be one of:
- INCLUDED AND VERIFIED
- INCLUDED WITH KNOWN LIMITATION
- DISABLED
- NOT IN THIS BUILD

### Step 3 — complete exact-head assurance

Run AgentOS tests plus independent PRS/Green adversarial cases against the exact candidate head.

### Step 4 — physical Windows acceptance

Use a clean or controlled laptop and capture:
- install;
- launch;
- first job;
- authority denial;
- successful bounded job;
- failed bounded job;
- pause/stop;
- restart/recovery;
- evidence/receipt state.

### Step 5 — internal Day 0 dry run

Use 2–3 internal/trusted people to execute the entire tester journey:

invitation → consent/terms → install → onboarding → real job → feedback → bug/trust report → support response → exit/checkpoint.

### Step 6 — security/privacy sign-off

Confirm beta-specific security, privacy, NDA/confidentiality decision, incident route and prohibited data guidance.

### Step 7 — admit 5–8 Wave 0 testers

Only after Steps 1–6 pass.

## Recruitment timing

Research and relationship mapping may continue now.

Do not open general applications or make public beta promises yet.

It is acceptable to maintain a private prospect list or non-committal future-interest list, but actual Wave 0 invitations should only be sent after the entry gate passes.

## Decision

**Current state: NOT READY FOR EXTERNAL WAVE 0.**

**Reason:** deterministic implementation is encouraging, but external-user physical-Windows acceptance and exact beta-build convergence are not yet proven.

**Next milestone:** `WAVE-0-ENTRY-CANDIDATE` — one exact build/ref with physical Windows acceptance, exact-head assurance, locked feature manifest, beta security/privacy package and completed internal Day 0 dry run.

When that milestone is independently evidenced, recruit 5–8 Wave 0 testers immediately; do not wait for full public-launch readiness.
