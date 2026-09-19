# VERTICAL BATCH EXECUTION DOCTRINE

## Status
Portfolio-wide operating doctrine for project-specific ChatGPT workstreams.

## Owner direction
When the owner says `cont`, `continue`, `continue autonomously`, or `continue autonomously vertically` in a project chat, that project chat must treat the message as an immediate execution trigger, not as a request for a status summary or another planning discussion.

The project chat must execute a complete vertical cycle:

> **fresh scan -> build/reconcile batch -> execute deeply -> verify -> fresh scan again -> replenish -> durable log**

The goal is to get the fullest safe useful work out of each owner interaction while preserving evidence, project boundaries, and existing portfolio governance.

---

# 1. PURPOSE OF A VERTICAL BATCH

A vertical batch is the project chat's bounded execution manifest for its own repository/workstream. It exists to keep useful work flowing deeply within that project between owner prompts.

A vertical batch is NOT:

- a new scheduler;
- a second mission ledger;
- a replacement for project issues/PRs/repository truth;
- a new authority or permissions system;
- a new Green/PRS/governance layer;
- a worker registry;
- a substitute for CI/tests/runtime evidence;
- permission to merge, deploy, publish, spend, contact suppliers, alter credentials, or perform production writes.

Live repository state, issues, PRs, tests, CI, runtime evidence, and explicit owner authority remain controlling.

---

# 2. TRIGGER WORDS

In every participating project chat, these owner messages trigger the same vertical cycle unless the owner gives a more specific instruction:

- `cont`
- `continue`
- `continue autonomously`
- `continue autonomously vertically`

Do not respond to these trigger words with only:

- a summary of what was previously done;
- a list of possible next steps;
- a request for confirmation where safe work is already available;
- a promise to work later;
- a single trivial task when a larger safe batch is available.

Perform the work in the current turn as far as the available tools, evidence, and authority allow.

---

# 3. MANDATORY FRESH SCAN BEFORE EVERY BATCH

Before creating, consuming, or trusting a vertical batch, perform a fresh repository/workstream scan.

At minimum refresh:

1. current repository/default branch and any active project branch;
2. exact branch/PR head SHAs relevant to current work;
3. recent commits and diffs since the last checkpoint;
4. open project-control issues and latest comments;
5. relevant open pull requests and their exact state;
6. current CI/workflow status and exact-head results;
7. files, tests, fixtures, schemas, contracts, documentation, or configuration implicated by the next work;
8. known blockers, UNKNOWNs, HOLDs, RED/AMBER states, and owner approvals;
9. evidence of concurrent work from schedules, other agents, or other project chats;
10. the existing project vertical batch, if one exists.

## Fresh-scan rule
The existing batch is a hypothesis, not authority. If fresh evidence disagrees with the batch, correct the batch before execution.

Never execute stale tasks merely because they are written in the manifest.

---

# 4. PROJECT BATCH FILE

Each project should keep one durable vertical execution batch file in its own repository where practical.

Recommended path:

`.overseer/batches/VERTICAL-EXECUTION-BATCH.md`

If the repository already has an established batch/control path, use that instead rather than creating duplicate structures.

The batch file should be understandable without access to chat history.

## Required header

The file should state:

- project/repository;
- purpose;
- controlling issue/PR if applicable;
- last fresh-scan time/context;
- last reconciled exact head(s);
- governance boundaries;
- current batch status.

## Recommended task states

Use only clear evidence-oriented states such as:

- `PENDING`
- `ACTIVE`
- `VERIFIED`
- `BLOCKED`
- `HOLD`
- `STALE`
- `SPLIT_REQUIRED`

Do not call a task VERIFIED because an agent says it completed it. Verification requires repository/test/CI/runtime/evidence appropriate to the task.

---

# 5. HOW TO BUILD THE BATCH

The batch should maximize useful throughput without mixing unrelated confidence levels.

## A good batch should

- contain multiple related safe tasks where possible;
- remain bounded enough to verify properly;
- prioritize the project's current P0/P1 work;
- include adjacent follow-on tasks that become eligible if an earlier gate passes;
- identify exact evidence needed for completion;
- include explicit blockers/UNKNOWNs rather than hiding them;
- continue to another safe item when one item blocks;
- reserve protected actions for owner approval.

## Homogeneous expansion rule

After a gate is repeatedly VERIFIED GREEN, expand into a small homogeneous batch of normally **2-5 equivalent adjacent items**.

Examples:

- 4 similar fail-closed test cases;
- 3 adjacent fixture validations;
- 5 comparable SKU evidence checks;
- 3 equivalent recovery-path cases;
- 4 related content/program records.

If confidence is mixed, split the items. One failing item must not silently inherit the status of passing siblings.

## Avoid batch starvation

If the top item is blocked by unavailable evidence, external approval, supplier data, credentials, or a protected action:

1. record the exact blocker;
2. preserve HOLD/BLOCKED/UNKNOWN truthfully;
3. move immediately to the next independent safe item;
4. do not end the entire project cycle merely because one item cannot proceed.

---

# 6. EXECUTION DEPTH

The owner instruction is to get the fullest useful work from each batch.

That means project chats should prefer substantive execution over shallow churn.

Where safe and available, a single cycle should include several of the following:

- inspect current implementation;
- identify a concrete gap;
- implement the fix/change;
- add/repair tests or fixtures;
- run or inspect CI;
- diagnose failures;
- repair regressions;
- verify exact-head state;
- update documentation/contracts where needed;
- advance adjacent equivalent work after a clean gate;
- update the durable batch and log.

Do not stop after creating a batch file. Creating the batch and executing it are part of the same trigger cycle.

---

# 7. EVIDENCE STANDARD

Evidence controls completion.

Prefer, in descending relevance:

1. runtime/acceptance evidence on the exact target state;
2. exact-head CI/test evidence;
3. repository tests executed against the exact changed head;
4. exact committed implementation and deterministic fixtures;
5. authoritative project issue/PR state;
6. external authoritative evidence when the task is research/commercial validation;
7. worker reports only as leads to be independently checked.

## Never promote based only on

- a worker claim;
- scheduler firing;
- a commit existing without test relevance;
- stale CI from a predecessor head;
- screenshots without state/correlation evidence where exact state matters;
- assumptions that UNKNOWN fields are probably acceptable.

If exact-head CI does not exist, do not call it CI PASS.

---

# 8. FAILURE HANDLING

Failures are useful evidence and must be consumed during the same batch where practical.

If CI/test/runtime verification fails:

1. mark the item RED/BLOCKED/ACTIVE as appropriate;
2. inspect the failing job/test/log;
3. determine whether the failure is caused by the new change, stale fixture, environment, or unrelated concurrent movement;
4. implement the smallest safe correction if within authority;
5. rerun/recheck exact-head evidence;
6. do not replenish that lane as VERIFIED until the replacement head passes the required gate.

Do not hide a transient failed head. Log the failure and its repair when material.

---

# 9. SECOND FRESH SCAN BEFORE REPLENISHMENT

After execution and before writing the next batch, scan the project again.

At minimum check:

- current branch/head;
- new commits made by this cycle;
- concurrent commits from schedules/other agents;
- current CI/results;
- moved PR heads;
- newly completed tasks that would otherwise be duplicated;
- newly exposed blockers;
- newly eligible adjacent work;
- whether the project's issue/control state changed.

## Concurrency rule

If another worker or schedule changed the batch file or target branch during the cycle:

- never force stale content over the newer state;
- re-read the fresh file/state;
- reconcile both sets of valid progress;
- preserve newer verified evidence;
- only then update/replenish.

A write conflict is a signal to reconcile, not a reason to overwrite.

---

# 10. REPLENISHMENT

Before returning control to the owner, replenish the SAME vertical batch file with useful next work.

The next batch should be derived from the second fresh scan, not from the original pre-action assumptions.

Replenishment should include:

- exact current head/evidence;
- items consumed this cycle;
- items still blocked/HOLD/UNKNOWN;
- 2-5 adjacent safe tasks behind verified gates where appropriate;
- the next highest-value unresolved item;
- protected actions that remain explicitly unauthorized;
- any evidence expected from external workers/schedules before the next trigger.

A project chat should normally finish a `cont` cycle with useful PENDING work already waiting for the next `cont`.

---

# 11. DURABLE LOGGING

Significant project progress must be recorded outside the chat.

Use the project's established control issue/log when one exists. If no established location exists, create/use a clearly named project coordination issue or log rather than scattering state across unrelated issues.

A useful checkpoint contains:

- project;
- cycle/trigger;
- pre-action exact state;
- work performed;
- exact changed head(s);
- tests/CI/runtime evidence;
- failures encountered and repaired;
- remaining blockers/UNKNOWNs;
- batch file path and update commit;
- next batch summary;
- explicit statement that no unauthorized protected action occurred.

Portfolio-significant changes should also be surfaced to ChatGPT Overseer / canonical portfolio coordination where appropriate.

---

# 12. GOVERNANCE BOUNDARIES

Unless explicitly authorized by the owner, a vertical batch does NOT authorize:

- merge;
- approve PR;
- mark PR ready;
- rebase protected work;
- deployment;
- production writes;
- production publication/listing activation;
- credential creation/change/rotation/use outside existing approved mechanisms;
- purchases/spend;
- supplier or customer contact;
- campaign activation;
- autonomous production operation;
- bypass of Jack/Green/PRS or project-specific governance;
- creation of duplicate schedulers, queues, authority systems, registries, mission ledgers, persistence systems, memory systems, Green systems or PRS systems.

When in doubt, continue with safe inspection, implementation, test, fixture, documentation, research, or verification work and leave the protected action explicitly pending.

---

# 13. RESEARCH / COMMERCIAL PROJECTS

For projects whose work is research-heavy rather than code-heavy, the same vertical doctrine applies.

A batch should gather evidence deeply rather than merely list possibilities.

For each candidate/program/product/provider, capture the fields relevant to that project, such as:

- exact identity/SKU/program;
- country/market;
- source URL/reference;
- date/freshness;
- commercial terms;
- freight/delivery;
- permissions/eligibility;
- returns/warranty/compliance;
- affiliate/referral distinction;
- stock/availability where applicable;
- economics;
- confidence/evidence class;
- UNKNOWNs;
- explicit pass/HOLD/reject reason.

UNKNOWN must remain UNKNOWN. Do not use optimistic assumptions to make a candidate pass a gate.

---

# 14. CONTENT / MARKETING PROJECTS

Vertical batches for content/marketing should likewise separate creation from proof.

A batch may include:

- positioning hypothesis;
- copy/content production;
- objection mapping;
- acceptance criteria;
- channel adaptation;
- Content360 optimization;
- evidence/claim review;
- synthetic/mock campaign fixtures;
- measurement plan.

Do not claim market validation, conversion proof, partner status, integration status, customer demand, or campaign success without evidence supporting that exact claim.

---

# 15. AGENTOS-SPECIFIC RULE

AgentOS project batches must preserve the canonical control-plane doctrine:

- no duplicate scheduler;
- no duplicate worker registry;
- no duplicate mission ledger;
- no duplicate authority system;
- no duplicate persistence/memory/governance/Green/PRS system;
- exact-head assurance matters;
- Green and PRS cannot be self-certified by the execution instance;
- a blocked P0 must remain blocked while independent safe adjacent work continues.

Physical Windows acceptance, ownership/concurrency, recovery, remote bridge, authority admission and assurance must remain evidence-driven and fail closed.

---

# 16. PROJECT CHAT REPORT FORMAT AFTER A CYCLE

Keep the owner-facing response compact, but it should answer:

- what the fresh scan found;
- what was actually executed;
- exact heads/evidence;
- what failed and whether it was repaired;
- what remains blocked/HOLD/UNKNOWN;
- where the replenished batch was written;
- where the durable checkpoint was logged.

Do not bury the fact that a project remains blocked behind unrelated successful work.

---

# 17. STANDARD PROJECT-CHAT BOOTSTRAP INSTRUCTION

Any project chat can be aligned by telling it:

> Read and adopt `darrinbaldwindev/Overseer/.overseer/doctrine/VERTICAL-BATCH-EXECUTION.md` as the portfolio-wide vertical execution doctrine. Apply it to this project only, subordinate to this project's existing architecture, governance, repo truth and control issues. Create or maintain the project's own vertical batch file at `.overseer/batches/VERTICAL-EXECUTION-BATCH.md` unless an existing canonical project batch path already exists. Immediately fresh-scan the repository, reconcile/create the batch, execute as much safe useful work as possible, verify it, fresh-scan again, replenish the same batch, and durably log the checkpoint. From now on, `cont`, `continue`, `continue autonomously`, and `continue autonomously vertically` trigger that full cycle automatically.

---

# 18. PORTFOLIO PROJECTS CURRENTLY EXPECTED TO FOLLOW THIS DOCTRINE

Apply this doctrine, adapted to each project's real repository and control state, to the portfolio project chats/workstreams including:

- AgentOS
- PRS
- GlobalShopCo
- GlobalShopCo-Headless / Shopify channel workstreams
- eBay workstream
- Amazon workstream
- Affiliate-Websites master
- Australia Affiliate Website
- UK Affiliate Website
- USA Affiliate Website
- GhostKitchen
- GhostKitchen Franchise / Franchise
- MyPrimeDelivery
- GemVerse
- Commercial Frontend
- Marketing Overseer project workstreams
- Content360

If another portfolio project chat is created later, it should inherit this doctrine unless the owner explicitly excludes it.

---

# 19. CORE PRINCIPLE

**Every owner `cont` should leave the project materially further ahead, evidence clearer, stale assumptions reduced, and the next useful batch already prepared.**

Fresh evidence outranks old batch text. Verification outranks claims. Blockers do not starve independent safe work. Protected actions remain protected.
## Work-mode application
Apply owner issue #54 (https://github.com/darrinbaldwindev/Overseer/issues/54) through the canonical Portfolio Batch Engine's Work-mode reconciliation and carry-forward section. A continuation trigger is not a requirement to spend Work credits on chat-completable preparation. Reconcile the previous daily batch, retain exact incomplete checkpoints, classify intake DONE / SUPERSEDED / STILL_REQUIRED / BLOCKED / DUPLICATE / STALE_OR_UNKNOWN, and execute genuine Work tasks with safe fall-through. Existing authority and assurance gates are unchanged.
