# AgentOS Autonomy Hours / Night Shift — Product & Marketing Assessment

**Date:** 2026-09-07  
**Owner:** Marketing Overseer  
**Scope:** AgentOS product/UX/commercial hypothesis  
**Status:** RECOMMENDATION / HYPOTHESIS / VALIDATION REQUIRED

## Decision context

The user introduced a requirement that AgentOS autonomy must not assume 24/7 operation. Some users may prefer AgentOS to operate autonomously only overnight, during business hours, during selected windows, while a device is idle, or only when manually started.

Gemini independently assessed this requirement and strongly supported **Autonomy Hours** and the mainstream **Night Shift** concept. Marketing Overseer then critically reviewed the Gemini assessment and retained the core architecture while modifying several product/commercial details.

## Core governance principle

**WHEN AgentOS may work and WHAT AgentOS may do are separate controls.**

A permitted autonomy window grants execution time only. It does not grant broader authority.

Working control sequence:

**TIME WINDOW → USER AUTHORITY → POLICY → RISK → BUDGET → APPROVAL REQUIREMENTS → EXECUTION → EVIDENCE → HENRY ASSURANCE**

Time-based permission must never imply action-based permission.

## Night Shift concept

**RECOMMENDATION:** Use **Night Shift** as the mainstream, human-friendly preset for scheduled autonomy, while **Autonomy Hours** remains the underlying system capability.

Working consumer proposition:

> **Let AgentOS work while you sleep.**

Night Shift is considered strategically strong because it:

- gives non-technical users an understandable mental model for autonomy;
- provides explicit temporal boundaries that may increase trust;
- makes overnight/batch/local workloads intuitive;
- creates a tangible morning-value moment;
- avoids requiring users to understand background workers, cron, daemons or asynchronous pipelines.

## Character workflow during autonomy

The four AgentOS roles remain universal and are not reserved for the $99 tier:

- **Willow — Plans:** prepares and prioritises queued work.
- **Isla — Executes:** performs authorised work.
- **Jack — Protects:** enforces authority, policy, risk and budgets; holds blocked actions.
- **Henry — Checks:** verifies completed work and prepares evidence/results.

Working Night Shift flow:

**Willow plans the queue → Isla works → Jack guards the boundaries → Henry checks → Morning Brief**

## Morning Brief

**RECOMMENDATION:** Treat the Morning Brief as a major Night Shift UX feature.

Suggested structure:

### While you were away

- Jobs completed
- Documents/files processed
- Reports/drafts prepared
- Actions waiting for approval
- Tasks safely halted or requiring attention
- Henry assurance status

The Morning Brief should tell the user what happened, what failed, what needs approval, and what remains.

## Tonight's Queue

**RECOMMENDATION:** Add a pre-autonomy review surface such as **Tonight's Shift / Tonight's Queue**.

Before a Night Shift begins, Willow can show:

- planned jobs;
- expected order/dependencies;
- estimated completion window where supportable;
- premium-AI budget limit;
- authority profile;
- whether external writes/sends are allowed;
- any known blockers.

This allows the user to understand what AgentOS intends to do before unattended work begins.

## Approval handling during unattended work

Default behaviour should favour:

**Continue safe work and queue blocked actions for later approval.**

Working principles:

- A blocked branch must not freeze unrelated safe work.
- Ordinary approvals should wait for the user rather than waking them overnight.
- Emergency/high-priority notifications require explicit user configuration.
- Safe fallbacks may be used when pre-authorised, e.g. create an email draft rather than send it.
- Workflow state should be preserved so the user can approve in the morning and allow Isla to continue rather than restart the job.

This establishes a key future capability:

**Pause → preserve state → approve → resume**

## Autonomy window end

For mainstream users, the preferred simple default is:

> **Finish the current safe step, save progress, then stop.**

No new work should begin after the permitted window ends.

Essentials/Tech Head may expose deeper controls for immediate stop, checkpoint/resume, workflow completion thresholds, long-running compute, browser sessions and other technical behaviour.

## Autonomy settings by view

### Everyday

Simple controls:

- Anytime
- Night Shift
- During selected hours
- Only when I start it
- Never work without me

**Default recommendation:** manual/interactive autonomy unless the user explicitly opts into unattended work.

### Essentials

Expose:

- start/end times;
- selected days;
- multiple autonomy windows;
- per-project / Context Space schedules;
- autonomy budget;
- notification behaviour;
- approval-queue behaviour;
- window-end behaviour.

### Tech Head

Expose advanced controls such as:

- timezone;
- execution concurrency;
- maximum runtime;
- permitted workers;
- provider/model preferences;
- free/local/premium routing preferences;
- maximum cost per task/window;
- external-write permissions;
- network/domain restrictions;
- local-only windows;
- retries and escalation rules;
- queue priorities;
- failure behaviour;
- maintenance windows;
- idle-state conditions;
- hardware/GPU scheduling and resource thresholds.

## Autonomy Authority Profiles

**RECOMMENDATION:** Introduce reusable authority profiles so users do not need to rebuild permission rules for each shift.

Example profile: **Night Shift — Safe**

Allowed:

- research;
- read files;
- analyse data;
- create reports;
- draft communications;
- monitor approved websites.

Requires approval:

- send external communications;
- modify external systems;
- publish;
- spend money.

Never unattended by default:

- permanent destructive actions;
- security/credential changes;
- unapproved financial commitments;
- other explicitly high-risk actions.

Exact policy remains implementation/governance-dependent.

## Autonomy Budget

The autonomy budget should cover more than AI tokens alone.

Possible limits:

- premium AI spend;
- maximum jobs;
- browser/action count;
- maximum runtime;
- concurrency;
- local GPU permission;
- external-write authority;
- financial authority.

Example:

**Night Shift AI budget: $2.00**  
**Prefer free/local AI where suitable**  
**Ask before premium AI exceeds a user threshold**

Jack is the user-facing enforcement role.

## AI routing during autonomy

Gemini recommended a Local-First default. Marketing Overseer modifies this.

**RECOMMENDATION:** Do not blindly default to local AI. Route according to:

- task suitability/capability;
- required quality;
- privacy/policy;
- availability;
- reliability;
- user preference;
- budget/cost;
- hardware suitability.

Possible user-facing preferences:

- **Prefer free/local**
- **Balanced**
- **Prefer best available**

This better supports the existing **Make the most of AI** positioning.

## Free/local overnight compute

**HYPOTHESIS:** Night Shift may make free/local capability more useful because non-urgent work can be scheduled when user hardware is idle.

Candidate technologies include:

- Ollama;
- LocalAI;
- llama.cpp;
- vLLM;
- local embeddings;
- DuckDB;
- document parsing/OCR;
- local speech processing;
- local coding workers;
- Playwright/browser automation;
- batch inference.

Marketing must not claim night-time cloud APIs are cheaper unless a provider explicitly offers time-dependent pricing.

Avoid consumer-facing language such as **quota harvesting**. Preferred internal framing is **free allowance optimisation** or simply using available included/free capacity where permitted.

## Safety / failure considerations

Important scheduled-autonomy risks include:

- stale context/state drift;
- cascading dependent-task failures;
- retry/token/cost loops;
- hardware/resource exhaustion;
- provider outages;
- session expiry/authentication failures;
- browser state drift;
- unauthorized actions caused by confusing time permission with action permission;
- incomplete workflows at window end.

Mitigations should include:

- pre-execution state revalidation;
- assurance gates between dependent steps where appropriate;
- retry ceilings;
- budget ceilings;
- checkpoint/resume;
- hardware/resource limits;
- safe-halt behaviour;
- explicit authority checks independent of schedule.

## Commercial tier implications

Gemini proposed making Night Shift itself a $29 feature and reserving complex Willow/Isla/Jack/Henry orchestration for $99. Marketing Overseer rejects that latter distinction because the four roles are AgentOS itself and are introduced during the Free user's 30-day journey.

Working commercial progression:

### FREE — Taste / Assistant

> **AgentOS helps you while you're there.**

- limited but genuinely useful AgentOS;
- Willow/Isla/Jack/Henry all exist;
- manual/on-demand operation;
- limited jobs/capability;
- no meaningful unattended autonomy.

### $29/year — Co-worker

> **AgentOS works with you.**

- more capability and jobs;
- more memory/context;
- more free/premium AI options;
- more integrations;
- multi-step delegation;
- basic scheduled delegation / Night Shift;
- Morning Brief;
- conservative autonomy limits.

### $99/year — Operator

> **AgentOS works for you, on your schedule.**

- substantially greater autonomy and scheduling;
- multiple autonomy windows;
- recurring jobs;
- Context Space schedules;
- more parallel/complex work;
- stronger recovery;
- broader integrations;
- higher capacity;
- advanced monitoring/routing/control.

### Additional subscriptions / serious users

Reserved for extra/specialist capability such as premium providers, larger quotas, teams, business integrations, specialist workers, higher-volume automation and future enterprise controls.

Do not market $99/year as **enterprise-grade** unless SLA, SSO, team administration, compliance, support and related enterprise expectations are actually implemented and evidenced.

## Language / claim corrections from Gemini assessment

### KEEP

- Autonomy Hours.
- Night Shift mainstream concept.
- Morning Brief.
- Separate time authority from action authority.
- Manual/opt-in default.
- Continue safe branches while approvals wait.
- Budget/retry/resource ceilings.
- Free/local compute as an overnight opportunity.
- State revalidation and checkpointing.

### CHANGE

- Do not reserve Willow/Isla/Jack/Henry orchestration for $99.
- Do not call $99 enterprise-grade without evidence.
- Do not blindly make local-first routing the universal default.
- Avoid **quota harvesting** language.
- Do not claim **cryptographic verification proofs** unless cryptographic evidence mechanisms are actually implemented.
- Henry assurance should initially be described as evidence records/checking/verification, with hashes/signatures/immutable proofs added only when implemented.
- Simplify window-end behaviour for Everyday users.

### ADD

- Tonight's Queue.
- Autonomy Authority Profiles.
- Pause → preserve state → approve → resume.
- Autonomy Budget broader than AI spend.
- Night Shift as a preset within the larger Autonomy Hours engine.
- Named shifts/windows such as Work Shift, Weekend Shift, Idle Mode and Manual Shift.

## Product/marketing conclusion

**RECOMMENDATION:** The strongest current autonomy loop is:

> **Before bed:** Willow shows what AgentOS intends to do.  
> **Overnight:** Isla works; Jack guards the boundaries; Henry verifies results.  
> **Morning:** AgentOS shows exactly what was completed, what failed and what needs the user.

This makes the commercial phrase:

> **AgentOS works for you, on your schedule.**

more tangible than generic wording such as **background agents**.

## Evidence status

All Night Shift/Autonomy Hours UX, entitlement, technical behaviour, routing, budget and pricing implications in this document remain **RECOMMENDATION / HYPOTHESIS / VALIDATION REQUIRED** unless separately backed by implementation and verification evidence.

This report does not assert that Night Shift, Autonomy Hours, pause/resume, authority profiles, budget enforcement, local routing, Morning Brief or scheduled unattended execution are currently implemented in AgentOS.
