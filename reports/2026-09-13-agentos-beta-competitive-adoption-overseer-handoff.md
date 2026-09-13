# AgentOS Beta / Competitive Adoption — Overseer Handoff

**Date:** 2026-09-13  
**Owner:** Marketing Overseer / ChatGPT Overseer  
**Purpose:** Consolidate all current Founding Beta, competitive, migration, trust, security, positioning and adoption conclusions for Overseer review and action.

---

## 1. Executive conclusion

AgentOS should not position itself around capabilities that are already becoming table stakes across current AI tools, including multi-model chat, local models, BYOK, terminal access, Git/repo work, MCP, scheduled agents, local file access or generic “AI that works on your computer.”

The current strategic opportunity is the governed execution layer around that work:

- explicit authority and bounded scope;
- understandable permissions;
- stop / kill / revoke that actually halts work;
- durable mission state;
- recovery after interruption;
- duplicate / replay protection;
- evidence and receipts;
- independent assurance that distinguishes “agent says done” from “verified done”;
- budget / capability boundaries;
- local + cloud + free / paid model coordination without forcing the user to manage every provider manually.

The working product thesis for beta is therefore:

> **Can AgentOS perform useful real work on a user’s computer while staying inside explicit authority, showing what happened, detecting when work is not actually complete, stopping when told, and recovering without silently duplicating or losing work?**

This is a target to prove, not yet a marketing claim.

---

## 2. Founding Beta programme state

Canonical playbook:

`reports/2026-09-13-agentos-founding-beta-readiness-playbook.md`

Competitive-proof supplement:

`reports/2026-09-13-agentos-beta-competitive-proof-and-adoption-gaps.md`

Working identity:

> **AgentOS Founding Beta**  
> **Give AgentOS a real job.**

Recommended supporting line:

> **Stay in control. See what it did.**

Possible later proof-based line, only once validated:

> **AgentOS should prove the job is done — not just say it is.**

---

## 3. Tester timing and wave model

Do not recruit broadly before the Founding Beta entry gate passes.

### Internal readiness

Require:

- pinned beta build;
- exact shipped-feature matrix;
- known-limitations document;
- clean install / first-launch path;
- stop / pause / revoke path;
- permission boundaries;
- no unresolved S0 safety / trust issue;
- false-success prevention on applicable paths;
- data / privacy behaviour documented;
- security-report route;
- beta terms / NDA decision;
- internal Day 0 dry run with 2–3 people.

### Wave 0

5–8 external testers, Sunshine Coast / Brisbane preferred.

Purpose:

- installer;
- first-job flow;
- Windows behaviour;
- permission comprehension;
- stop behaviour;
- evidence / assurance comprehension;
- trust / recovery failures.

### Wave 1

~10–12 additional mixed Australian testers after Wave 0 gate passes.

### Wave 2

~12–15 additional AU / US / UK / global English specialist testers.

### Wave 3

Public waitlist / broader beta only after stop/go gates pass.

---

## 4. Recommended cohort mix

Approximate 30-person mix:

- 10 everyday / non-technical;
- 8 professional / small business;
- 7 creator / power user;
- 5 developer / technical.

Reserve at least 8 seats for low-confidence / non-technical users.

Do not let the beta become an AI-enthusiast-only or developer-only exercise.

Most important screening question:

> **What is one real task you would like AgentOS to help you get done?**

A real task matters more than enthusiasm.

---

## 5. Recruitment research conclusion

Current best sourcing direction:

1. Sunshine Coast / Peregian / local AI-business communities;
2. Brisbane AI / startup / builder communities;
3. explicit Reddit beta-testing communities;
4. AI-agent / local-AI / Claude / ChatGPT / Ollama / MCP communities;
5. Indie Hackers / maker communities;
6. Product Hunt / BetaList later;
7. carefully selected small-business / creator communities;
8. paid acquisition only after organic evidence is insufficient.

Grok’s beta-recruitment research strongly supports an Australian-first controlled cohort while preserving international expansion.

Do not spam competitor communities. Check community rules immediately before outreach.

---

## 6. Beta programme mechanics adopted from Claude

Use a 14-day operating programme.

Core checkpoints:

- Day 0: install + first real job;
- Day 1: onboarding / trust comprehension check;
- Day 3: repeat-use check;
- Day 7: midpoint review;
- Day 14: exit survey / interview.

Preferred early north-star:

> **Percentage of testers who attempt a second real job without being prompted by the beta schedule.**

Completion criteria:

- install complete;
- at least two real jobs attempted;
- Day 7 checkpoint;
- final feedback submitted.

Recommended reward:

> **12 months AgentOS Operator**

Reward must be for participation, not positive sentiment.

Negative / critical feedback must receive equal eligibility.

---

## 7. NDA / confidentiality / legal model

Do not automatically require a full NDA.

Three models are acceptable depending on product state:

- no NDA + beta terms / privacy / responsible disclosure;
- light confidentiality agreement for unreleased screenshots, pricing experiments, roadmaps or security-sensitive details;
- formal NDA only where genuinely justified by sensitive IP, partner obligations or significant unreleased security architecture.

An NDA must not substitute for:

- security controls;
- privacy notice;
- beta terms;
- vulnerability reporting;
- credential handling;
- consumer / statutory rights.

Final legal language should receive qualified legal review for applicable jurisdictions.

---

## 8. Security / privacy operating requirements

Before Wave 0, document:

- what AgentOS can access;
- what it cannot access;
- local vs cloud behaviour;
- telemetry / diagnostics;
- data retention;
- log collection;
- who can access reports;
- uninstall / revoke / cleanup;
- emergency kill path;
- credential handling;
- incident route.

Testers should not use production customer secrets, banking credentials, passwords, private keys, highly sensitive health data or unauthorised employer / client data.

BYO API credentials must use secure entry, masking, revocation guidance and log redaction.

---

## 9. Critical new security gap — secret visibility model

AgentOS needs an explicit credential visibility / reachability model.

For every credential class, answer:

- which component can access it;
- whether the model can see it;
- whether a worker can see it;
- whether an MCP/tool can see it;
- whether it can appear in logs;
- where it is stored;
- how it is scoped;
- how it is rotated / revoked;
- whether a job can run without exposing raw secret material to the model.

Credential examples:

- OpenAI API keys;
- Anthropic keys;
- OpenRouter keys;
- GitHub tokens;
- OAuth tokens;
- MCP credentials;
- browser session credentials.

This should become part of Jack’s authority / capability model.

---

## 10. Critical new security gap — untrusted content / prompt injection

AgentOS must explicitly distinguish:

- owner instruction;
- approved plan;
- model reasoning;
- external / untrusted content encountered during execution;
- tool / MCP metadata.

Untrusted sources include:

- web pages;
- READMEs;
- repository files;
- documents;
- emails;
- MCP tool descriptions;
- external API text.

These sources must never silently become authority.

A Level 2 governed worker should treat them as data unless explicit policy says otherwise.

This threat model should be considered a prerequisite before broad computer autonomy.

---

## 11. Competitive reality — Open WebUI Computer and adjacent tools

Open WebUI Computer materially overlaps AgentOS Level 2 ambitions.

Current evidence indicates real host / mounted-folder work, local files, editor / terminal, Git, Windows / macOS / Linux, shell / PowerShell on Windows, scheduled work, bots / gateway operation, local models via Ollama, MCP support and unattended pathways.

Its security model appears comparatively explicit:

- bare-metal host access should be treated like SSH;
- Docker reduces blast radius to mounts;
- bare-metal path sandboxing is not assumed;
- unattended paths may run with broad approval;
- persistence survives browser disconnect, but host and process must remain alive;
- server restart interrupts in-flight work.

Implication:

AgentOS must not market generic computer control as unique.

---

## 12. Capabilities likely commoditised / weak differentiators

Treat the following as baseline unless current evidence later proves otherwise:

- multi-model chat;
- local model support;
- Ollama;
- BYOK;
- terminal access;
- Git / repo editing;
- local file access;
- MCP support;
- browser/tool use;
- scheduled agents;
- agent workflows;
- local RAG / document indexing.

These may remain valuable product features, but should not carry uniqueness claims.

---

## 13. Potential AgentOS moats to prove

Possible differentiators:

### Jack

- explicit authority;
- bounded scope;
- risk / budget control;
- user intent protection;
- stop / deny / revoke;
- secret / capability governance.

### Henry / PRS / Green

- independent challenge of executor claims;
- evidence validation;
- false-success prevention;
- explicit partial / failed / blocked states;
- exact-head assurance.

### Durable mission / execution model

- restart-safe state;
- crash recovery;
- replay / duplicate protection;
- side-effect correlation;
- resumable missions.

### Provider-neutral orchestration

- local / free / paid / cloud provider coordination;
- user cost / performance policy;
- no single-vendor lock-in.

These are only moats once independently proven.

---

## 14. Patterns worth adopting

### A. Understandable execution modes

Competitor patterns such as ask / auto / full show a real user need for clear modes.

Recommended AgentOS adaptation:

- Preview / Plan Only;
- Approve As Needed;
- bounded **Autonomy Window**.

Avoid a generic unrestricted “full” mode.

Autonomy Window should bind:

- duration;
- folder / repo scope;
- capability list;
- external side effects;
- network destinations where practical;
- budget;
- risk ceiling;
- stop condition.

### B. Persistent tasks independent of chat/browser session

Task state should not depend on whether the user leaves the chat window.

### C. Evidence-first execution surfaces

Adopt / emphasise:

- changed-file list;
- diffs;
- commands executed;
- stdout / stderr;
- exit codes;
- test results;
- timestamps;
- screenshots / browser evidence where relevant;
- external side-effect receipts.

### D. Optional isolation

Where tasks do not require unrestricted host access, provide / investigate isolated container or sandbox execution to reduce blast radius.

### E. Explicit host-risk disclosure

If operating on the real Windows machine, say so plainly.

### F. Recovery as product UX

Recovery should be visible and understandable, not merely an internal implementation detail.

---

## 15. Patterns we should deliberately not copy

Avoid:

- unrestricted host “full access” as the mainstream path;
- unattended work automatically receiving maximum authority;
- executor self-verification as final success;
- broad persistent permissions for convenience;
- security by warning text alone;
- feature-count competition;
- claiming uniqueness for generic local AI / MCP / computer-control capabilities.

---

## 16. P0 gaps before Wave 0

The following should be treated as beta-entry proof gaps:

1. exact pinned beta build / shipped-feature matrix;
2. physical Windows acceptance on the real worker path;
3. permission-scope UX ordinary users can understand;
4. reliable Stop / Kill / Revoke behaviour;
5. false-success prevention;
6. independent Henry / PRS / Green assurance on applicable paths;
7. documented app / worker / machine restart semantics;
8. duplicate / replay protection around side effects;
9. exact known-limitations document;
10. secret / credential handling and redaction;
11. clean uninstall / revoke / data cleanup;
12. private security incident route;
13. untrusted-content / prompt-injection threat model;
14. evidence surface understandable to non-technical testers;
15. exact definition of what VERIFIED means per mission class.

A capability may remain disabled for Wave 0 if explicitly documented and not marketed / assigned in beta missions.

---

## 17. Beta missions revised by competitive research

Wave 0 should explicitly include, where the beta build supports them:

### Scope test

Give AgentOS access to one folder / repo while an adjacent location remains out of bounds.

Expected proof:

- no unauthorised access;
- denied scope visibly enforced.

### Permission-denial test

User denies one capability mid-job.

Expected proof:

- no action using denied capability;
- clear blocked / partial state rather than fabricated success.

### Stop test

User stops active work.

Expected proof:

- no further tool calls / side effects after stop boundary;
- user can understand final state.

### False-success trap

Design a task that cannot honestly become VERIFIED without specific evidence.

Expected proof:

- executor “done” is insufficient;
- Henry / assurance catches missing proof.

### Recovery test

Interrupt a controlled mission and resume.

Expected proof:

- mission resumes from safe state;
- completed side effects are not silently repeated.

### Duplicate / replay test

Re-submit / replay same mutation attempt.

Expected proof:

- duplicate side effect does not occur.

### Evidence comprehension test

Ask tester what AgentOS actually changed and compare with receipts.

Expected proof:

- ordinary user can understand result at useful level;
- Tech Head view can expose deeper receipts without changing safety policy.

### Local / free model test

Where supported, complete useful work without a paid AI subscription.

Expected proof:

- free/local path is practical, not merely technically connected.

---

## 18. Everyday / Essentials / Tech Head implications

Safety policy should remain constant across views.

Only presentation depth changes.

### Everyday

Show:

- what AgentOS wants to do;
- what it needs access to;
- what changed;
- whether result is verified / incomplete;
- stop button.

### Essentials

Add:

- affected files / tools;
- concise evidence;
- permissions and limits;
- recovery / retry status.

### Tech Head

Add:

- full tool calls;
- diffs;
- stdout / stderr;
- exit codes;
- correlation / receipt IDs;
- detailed authority / assurance state.

Do not weaken / strengthen actual governance based on UI mode.

---

## 19. Marketing claims to avoid until proven

Avoid:

- first / only AI operating system;
- the only AI that controls your computer;
- fully autonomous;
- completely private;
- always chooses the best AI;
- always chooses the cheapest AI;
- replaces all your AI subscriptions;
- guaranteed savings;
- guaranteed ROI;
- AgentOS pays for itself;
- unlimited agents / unlimited autonomy unless entitlement and runtime truth support it;
- works with every AI.

Use narrower, evidence-backed copy.

---

## 20. Current positioning direction

Retain:

> **Put AI to work.**

Retain beta invitation:

> **Give AgentOS a real job.**

Recommended supporting trust language:

> **Stay in control. See what it did.**

Potential later proof claim:

> **AgentOS proves the job is done — not just says it is.**

Only promote the last claim after the assurance path has independent evidence.

---

## 21. Pricing / commercial conclusions to retain

Current direction remains:

- Free;
- $39/year Co-worker;
- $99/year Operator.

$99 remains expected mainstream paid tier.

$39 remains a lower-friction conversion / “second bite” tier and should not become the default product if it can reasonably be prevented through genuine capability / capacity differentiation.

Universal safety / trust / governance must not be paywalled.

Beta should test price perception only near the end, before and after revealing the proposed ladder.

Do not lead users with internal “$99 expected sale” assumptions.

---

## 22. Commercial claims from Gemini that remain hypotheses

Treat the following as hypotheses / benchmark targets, not approved public claims:

- AgentOS replaces a $20/month AI subscription;
- AgentOS produces net annual savings;
- verified savings ledger proves ROI;
- 58% savings versus a single AI subscription;
- “guaranteed net positive savings”;
- full / unlimited background execution;
- exact tier capacity assumptions not yet tied to shipped runtime.

These require real benchmark / user evidence.

---

## 23. Migration / competitor user research direction

High-value existing-user pools likely include:

- Open WebUI / Jan / Msty / Cherry / TypingMind users;
- Ollama / OpenRouter users;
- Cursor / Aider / Claude Code / Cline / Goose users;
- n8n / automation users;
- multi-subscription ChatGPT / Claude / Gemini users.

The key research question is not “Do they use AI?”

It is:

> **What pain remains after they already have these tools?**

AgentOS may be:

- replacement;
- complement;
- control layer above;
- optional add-on;
- low relevance.

Do not force replacement positioning where orchestration / integration is more valuable.

---

## 24. Partner / complement direction

Likely complements rather than direct replacement targets:

- Ollama;
- OpenRouter;
- GitHub;
- MCP ecosystem;
- Aider / coding agents where they can function as governed workers;
- n8n / automation systems where AgentOS can govern rather than duplicate;
- cloud providers / local models.

AgentOS should prefer wrapping / governing proven specialist capability over rebuilding it where appropriate.

---

## 25. Architecture / governance invariants

Do not create alternate:

- scheduler;
- queue;
- authority system;
- worker registry;
- mission ledger;
- persistence layer;
- governance layer;
- assurance source of truth.

No broad competitor response should compromise the existing AgentOS control-plane architecture.

No merge / deploy / credential / production autonomy decisions are implied by this handoff.

---

## 26. Immediate Overseer decisions requested

Overseer should consider and decide whether to elevate the following into formal AgentOS Level 2 acceptance requirements:

1. explicit secret visibility model;
2. untrusted-content / prompt-injection boundary;
3. bounded Autonomy Window UX;
4. mandatory Stop / Kill / Revoke acceptance test;
5. exact VERIFIED semantic contract;
6. duplicate / replay test at user-visible mission layer;
7. restart / recovery test across app / worker / host failure classes;
8. evidence-comprehension requirement for Everyday view;
9. isolated execution option where host access is unnecessary;
10. explicit host-risk disclosure where local worker uses real machine access.

---

## 27. Recommended smallest safe next actions

1. Reconcile current AgentOS main / active Level 2 branches against the 15 P0 beta-entry proof gaps.
2. Produce a canonical shipped / draft / planned / not-proven matrix.
3. Define `VERIFIED` for file edit, test run, repo mutation, browser action and external side-effect mission classes.
4. Design the secret visibility / credential reachability table.
5. Design the untrusted-content threat model.
6. Confirm Stop / Kill / Revoke semantics and physical Windows acceptance evidence.
7. Confirm duplicate / replay / crash recovery evidence on exact current heads.
8. Keep Founding Beta on HOLD until the entry gate can be assessed against real runtime evidence.
9. When candidate build exists, invoke the beta playbook and run internal Day 0 dry run before Wave 0 outreach.

---

## 28. Final operating principle

AgentOS should not attempt to win because it can do more things than every competitor.

It should attempt to win because it can make increasingly capable AI workers **safer to trust, easier to control, easier to recover, and harder to falsely declare successful**.

The product and beta should prove that proposition before Marketing turns it into a claim.
