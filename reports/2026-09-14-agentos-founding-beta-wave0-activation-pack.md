# AgentOS — Founding Beta Wave 0 Activation Pack

**Date:** 14 September 2026  
**Owner:** Marketing Overseer  
**Status:** PREPARED / ACTIVATION HOLD  
**Canonical mission:** `darrinbaldwindev/Overseer#49`  

## Purpose

Prepare AgentOS Founding Beta Wave 0 so recruitment can begin quickly once the technical beta-entry gate clears, without weakening claim discipline or recruiting against capabilities that are not yet proven.

This document is an activation pack, not publication authority and not evidence that Level 2 is complete.

## Current evidence boundary

At the fresh scan used for this pack:

- AgentOS PR #104 is OPEN / DRAFT / UNMERGED at exact head `71c463a77b31ebeac2bfe00da13c684512daccf7`.
- Exact-head AgentOS Tests run #976 / `34808263482` completed SUCCESS.
- The continuous kernel-enforced project-file ownership boundary through publish/recovery/success-receipt remains unresolved.
- Authenticated transport identity + canonical grant lookup remain unwired at admission.
- Physical Windows acceptance has not been rerun on the current runtime-changing head.
- No exact-head independent Green PASS exists for the required Level 2 mutation path and no downstream independent PRS PASS exists.

Therefore Wave 0 remains HOLD.

## Safe beta promise

Primary line:

> **Give AgentOS a real job.**

Supporting line:

> **Stay in control. See what it did.**

Evidence-safe explanation:

> AgentOS is being built around governed execution: giving AI useful work while keeping authority, evidence and verification visible instead of simply giving an AI unrestricted computer access.

Do not use beta recruitment language that implies end-to-end autonomous Windows control, guaranteed recovery, guaranteed verification, perfect duplicate prevention or fully proven stop/revoke until those exact claims have passed their own gates.

## Wave 0 size and composition

Target **5–8 controlled testers**.

Preferred geography for the first cohort: Sunshine Coast / Brisbane where practical, because close support and direct observation are more valuable than reach at this stage.

Recommended mix:

- 2 everyday AI users who are not developers;
- 1–2 professionals / small-business users with repeatable real work;
- 1 creator/power user who currently juggles multiple AI tools;
- 1–2 developers/technical users who can deliberately challenge the boundaries;
- optional 1 operational/admin user who has clear repetitive computer tasks but limited technical interest.

Do not let developers dominate the cohort. Wave 0 is testing whether governed execution is understandable and useful to normal users, not only whether technical users can operate it.

## Recruitment sources

Use warm or high-trust channels first once GO is issued:

- owner's personal/professional network;
- local Sunshine Coast / Brisbane small-business contacts;
- trusted creator/AI-user contacts;
- developer contacts for adversarial slots only;
- existing project/community contacts who already understand that this is a controlled founding beta.

Avoid broad public recruitment, paid ads or influencer promotion for Wave 0. Those create support load before the product and evidence model have been proven with a small cohort.

## Tester screening rubric

A Wave 0 tester should ideally satisfy at least four of the following:

1. already uses AI at least weekly;
2. can bring one real, bounded job rather than a contrived demo;
3. can describe what success looks like for that job;
4. is comfortable with an early beta that may stop rather than continue when authority/evidence is insufficient;
5. will report confusion honestly;
6. can attempt a second independent job if the first experience earns enough trust;
7. is willing to test stop/revoke/denial behavior rather than only happy-path output;
8. does not require production-critical reliability in Wave 0.

Exclude or defer users whose first use case requires high-stakes financial, legal, medical, safety-critical, irreversible production or confidential-client actions that exceed the current evidence boundary.

## Wave 0 mission menu

Each tester should bring a real job. Marketing/product should map it to the current permitted capability envelope rather than forcing every tester through an identical demo.

Mission families once technically eligible:

### 1. Inspect and explain
- inspect a project/repository state;
- identify a bounded issue;
- explain what changed and what remains uncertain.

### 2. Controlled edit + verify
- make a bounded file/config/document change inside an approved root;
- run the relevant check/test;
- present exact files touched and evidence.

Only activate after the mutation ownership/recovery gate clears.

### 3. Permission denial
- ask for something outside the granted scope;
- confirm the action is denied rather than silently attempted.

### 4. Stop/revoke
- begin a bounded task;
- revoke/stop at an allowed checkpoint;
- inspect what completed, what did not, and what evidence remains.

Only use this as a proof mission once the product has independently demonstrated the required semantics.

### 5. Failure / interruption recovery
- interrupt a safe fixture task;
- restart/resume;
- verify whether the product recovers or fails closed without duplicate side effects.

### 6. Evidence comprehension
- give tester the result/evidence surface;
- ask them to explain in their own words what AgentOS did, what it did not do, and how sure they are.

### 7. Free/local/paid model routing experience
- compare a bounded job where AgentOS coordinates available intelligence while keeping the job/authority model consistent.

This tests the broader promise of making AI easier to use without relying on “more models” as the differentiator.

## Session structure

### Before the first job
Ask:
- What job do you want done?
- What would count as success?
- What is AgentOS allowed to touch?
- What would make you uncomfortable?
- What do you expect “verified” to mean?

Record the user's natural language before teaching product terminology. This exposes whether the product's trust model matches normal expectations.

### During the job
Observe:
- whether permissions are understood;
- whether the user knows when AgentOS is acting vs planning;
- whether denied actions are understandable;
- whether the user can tell local/cloud/mixed execution if relevant;
- whether evidence is visible at the right moment;
- whether the user knows how to stop/revoke;
- whether interruptions create uncertainty.

### Immediately after
Ask:
- What did AgentOS actually do?
- What evidence convinced you?
- What are you unsure about?
- Did it touch anything you did not expect?
- Would you trust it with a slightly harder version of this job?
- What would you change before using it again?

### Independent second-use test
Do not automatically assign a second task.

Observe whether the tester attempts or proposes a **second real job without prompting**. This is the strongest early adoption signal because it reflects both usefulness and enough trust to continue.

## Core measurement set

Per tester capture:

- time to first useful job definition;
- time to first successful bounded execution;
- permission comprehension: PASS / PARTIAL / FAIL;
- scope containment: PASS / FAIL;
- denied-action comprehension: PASS / PARTIAL / FAIL;
- stop/revoke comprehension: PASS / PARTIAL / FAIL;
- evidence comprehension: PASS / PARTIAL / FAIL;
- recovery/restart result where tested;
- duplicate/replay result where tested;
- perceived control before/after;
- perceived evidence clarity before/after;
- support interventions required;
- tester attempts second real job without prompting: YES / NO;
- second real job succeeds inside permitted scope: YES / NO / NOT ATTEMPTED.

### North-star early signal

> **% of Wave 0 testers who attempt a second real job without prompting.**

A high first-task completion rate with a low second-job rate should be treated as a warning that the experience is impressive but not habit-forming or trusted enough.

## Qualitative failure taxonomy

Tag each issue into one primary category:

- VALUE — job not useful enough;
- COMPREHENSION — user does not understand state/authority/evidence;
- CONTROL — user cannot confidently bound or stop the work;
- TRUST — user distrusts result/evidence/recovery;
- FRICTION — setup/permissions/UI are too hard;
- CAPABILITY — required action is not supported;
- RELIABILITY — task behaves inconsistently;
- RECOVERY — interruption/failure state is unclear or unsafe;
- COST — user does not understand or accept model/tool cost;
- POSITIONING — product promise creates the wrong expectation.

Do not collapse all failures into “UX feedback”; several categories can expose product-control defects.

## Wave 0 GO gate

Marketing may activate recruitment only after a fresh scan shows the intended Wave 0 build has, at minimum:

1. the required Level 2 mutation ownership boundary proven at the exact intended head;
2. adversarial stale-owner/success-receipt and recovery cases fail closed;
3. canonical authenticated identity + grant evidence bound into runtime admission for the tested path;
4. exact task/mission/worker/result correlation through the real tested runtime;
5. relevant mutation/interruption/restart/replay tests passing exact head;
6. physical Windows acceptance rerun on the exact runtime-changing build intended for Wave 0;
7. full relevant CI/test/audit pass exact head;
8. independent Green PASS for the tested scope;
9. independent PRS assurance after Green where required;
10. Marketing claim review of the exact build and tester-facing language.

If any mandatory gate becomes UNKNOWN because the head moves, Wave 0 returns to HOLD until rechecked.

## Stop conditions during Wave 0

Pause recruitment and return to HOLD if any of the following occur:

- unexpected mutation outside approved scope;
- success shown without required evidence;
- stale/duplicate execution causing an unintended side effect;
- stop/revoke semantics materially differ from tester-facing explanation;
- recovery cannot determine whether a mutation occurred;
- a head/build changes without revalidation;
- credential/secret visibility exceeds the explained boundary;
- a repeated user misunderstanding indicates the trust model itself is unclear.

## Expansion gate to ~30–35 testers

Do not expand because 5–8 people liked the idea. Expand only when Wave 0 shows:

- no material containment or false-success failure;
- evidence is understandable to non-developers;
- support burden is manageable;
- real jobs complete at a useful rate;
- failures are explainable and recoverable/fail-closed;
- second-real-job behavior is strong enough to justify broader testing;
- product/positioning changes from Wave 0 are incorporated into the next pinned build.

## Channel messaging after GO

### Everyday
“You already use AI. Give the job to AgentOS instead of figuring out which AI to use.”

### Professional / small business
“Bring a real piece of work. See whether AgentOS makes it easier while keeping the job bounded and visible.”

### Creator / power user
“Stop juggling AI tools. Give AgentOS the workflow and keep the execution visible.”

### Developer
“Try to break the governed AI worker before everyone else gets it.”

These are recruitment concepts, not present-tense capability guarantees.

## Publication status

**Prepared:** yes.  
**Recruitment activated:** no.  
**Paid campaign:** no.  
**Founding Beta:** HOLD pending exact build gate.  
**Overall AgentOS GREEN:** not claimed.