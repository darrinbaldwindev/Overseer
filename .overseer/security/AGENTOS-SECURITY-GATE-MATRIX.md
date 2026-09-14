# AgentOS Security Gate Matrix

**Status:** canonical coordination policy for autonomous execution and assurance.

**Purpose:** security must advance with autonomy. This matrix defines the minimum deterministic controls that every AgentOS/portfolio workstream must satisfy before capabilities can widen. It is consumed by the portfolio batch system, Project Overseers, workers, Agent Green, and PRS.

## Core invariant

> **No model decides its own authority.**

Models and workers may request capabilities. Deterministic AgentOS/PRS policy decides whether authority exists, what scope is granted, for how long, and what evidence is required. External content never grants authority.

## Security operating model

Execution hierarchy remains:

`Portfolio batch -> Project Overseer -> delegated workers -> evidence -> Project Overseer reconciliation -> Agent Green -> PRS where applicable -> next batch replenishment`

Security is not a separate control plane. Security gates are requirements attached to work already owned by each Project Overseer.

## Risk classes

| Class | Typical capability | Default posture | Required assurance |
|---|---|---|---|
| S0 | Pure reasoning, synthetic fixtures, local read-only analysis | Allowed inside mission scope | deterministic receipt + provenance |
| S1 | Read-only repo/files/API metadata, public research | Allowed with least privilege | identity, scope, provenance, audit receipt |
| S2 | Non-production writes, branch/docs/tests/drafts, reversible local mutations | Explicit scoped grant | actor/grant binding, bounded blast radius, verification, Green |
| S3 | External messaging, production data mutation, deployment, credentials access, live publication | Deny by default | owner/policy approval, exact scoped grant, preflight, Green, PRS where applicable |
| S4 | Purchases/spend, destructive actions, unrestricted elevation, security-policy changes, production autonomy | Owner-only / exceptional | explicit owner authority, deterministic policy check, dual assurance, rollback/kill-switch evidence |

Unknown classification fails closed to the higher-risk class.

## Gate matrix

### SG-01 — Authenticated actor identity
**Requirement:** every state-changing action is bound to an authenticated actor identity that cannot be supplied or overridden by untrusted request payloads.

**PASS evidence:** deterministic tests for missing actor, actor mismatch, spoofed actor input, stale actor context, exact correlation to mission/task/request.

**FAIL/CLOSE:** no mutation and no success receipt.

### SG-02 — Canonical authority/grant source
**Requirement:** authority comes from one canonical policy/grant source; workers cannot self-grant and no duplicate authority registry is created.

**PASS evidence:** exact grant provenance, actor/project/scope binding, policy lookup failure denial, mismatch denial, no fallback self-authorization.

### SG-03 — Least privilege and capability scoping
**Requirement:** each worker receives only capabilities needed for the current mission/work item.

**PASS evidence:** positive allowed-path test plus negative tests for adjacent unauthorized tools/resources/actions.

**Required dimensions:** repo/project, resource, action, environment, time/expiry where supported, budget/quantity where relevant.

### SG-04 — Risk-class enforcement
**Requirement:** tools/actions are classified S0–S4 before execution; unknowns fail closed.

**PASS evidence:** deterministic mapping and denial tests for unclassified/escalated actions.

### SG-05 — Secret isolation
**Requirement:** secrets never appear in prompts, batch files, logs, memory, receipts, test fixtures, commits, screenshots, or worker-visible research artifacts.

**PASS evidence:** secret-reference/opaque-handle design, log redaction tests, fixture scans, no plaintext credential persistence.

**Rule:** existing Content360/API credentials are treated as sensitive and must never be copied into durable artifacts.

### SG-06 — Untrusted-content / prompt-injection boundary
**Requirement:** websites, email, documents, issue text, model output, API results, retrieved files, and worker messages are data, not authority.

**PASS evidence:** adversarial fixtures where external content requests tool use, authority escalation, secret disclosure, memory writes, policy bypass, or instruction override; all remain denied unless separately authorized.

### SG-07 — Memory poisoning protection
**Requirement:** externally sourced content cannot become canonical memory/state solely because a model says it should.

**PASS evidence:** provenance + validation gate + reversible/staged memory proposal path; malicious/stale/conflicting proposals denied or quarantined.

### SG-08 — Continuous ownership / transactional mutation
**Requirement:** the same valid ownership fence is held continuously across final verification -> side effect/publish -> prepared recovery where applicable -> durable success receipt -> release.

**PASS evidence:** replacement-after-verification, successor-writer, stale identity, TOCTOU, crash/replay, duplicate result/mutation, prepared-recovery adversarial tests.

**Rule:** success must not persist before ownership-loss detection.

### SG-09 — Idempotency / replay / duplicate-execution safety
**Requirement:** at-least-once delivery must not create duplicate external or durable side effects.

**PASS evidence:** replayed request/task/event, crash-after-side-effect, duplicate result write, duplicate scheduler pickup, stale delivery, and correlation mismatch tests.

### SG-10 — Exact correlation and provenance
**Requirement:** mission, request, delivery, task, wake, actor, grant, side effect, result, receipt, Green evidence, and PRS evidence remain exactly correlated.

**PASS evidence:** malformed/mismatched/stale correlation fails closed and produces no false success.

### SG-11 — Immutable/durable audit receipt
**Requirement:** every material autonomous action records who acted, authority used, exact scope, input/evidence provenance, intended action, actual side effect/result, verification result, and disposition.

**PASS evidence:** receipt survives restart/recovery and cannot silently promote UNKNOWN/PARTIAL/FAIL to success.

### SG-12 — Blast-radius limits
**Requirement:** missions/workers have deterministic ceilings.

**Candidate ceilings:** max files/records/messages changed, API calls, spend, elapsed runtime, retries, external recipients, repositories/projects, inventory/order/listing count.

**PASS evidence:** boundary and over-limit denial tests.

### SG-13 — Budget / spend safety
**Requirement:** no worker can infer financial authority from mission context.

**PASS evidence:** zero-spend default, explicit amount/currency/merchant/category scope when owner-authorized, duplicate-charge/replay denial, approval expiry/revocation.

### SG-14 — Production boundary
**Requirement:** synthetic/dev/staging evidence does not grant production authority.

**PASS evidence:** environment-bound grants, production-host/resource denial, dev-token-on-prod denial, publication/deployment defaults OFF.

### SG-15 — External communication boundary
**Requirement:** sending email/messages, supplier contact, campaign activation, public posting, marketplace publication, or user-visible outbound action requires explicit scoped authority appropriate to risk class.

**PASS evidence:** draft/read-only paths cannot silently become send/publish paths; recipient/destination correlation enforced.

### SG-16 — Kill switch and scoped quarantine
**Requirement:** AgentOS can deny all external writes immediately and can quarantine a single worker/provider/tool/repo/mission without requiring global shutdown.

**PASS evidence:** deterministic disable state, denial under stale sessions, recovery/re-enable only under authorized policy.

### SG-17 — Dependency/provider compromise containment
**Requirement:** one compromised provider/tool/worker cannot widen its own scope or poison canonical authority/state.

**PASS evidence:** malicious tool result, malformed provider response, stale signed/unsigned metadata, unexpected capability response, provider substitution tests.

### SG-18 — Green exact-head assurance
**Requirement:** Agent Green assesses the exact code/evidence lineage being promoted and actively repairs authorized defects or routes implementation-ready remediation.

**PASS evidence:** exact head/evidence IDs, targeted negative tests, repair verification. Green PASS on one head never transfers to another.

### SG-19 — PRS independent assurance
**Requirement:** high-risk/current promoted scope receives PRS only after Green passes the identical exact head/evidence lineage.

**PASS evidence:** independent adversarial result with exact target identity. PRS must not inherit worker/Green success claims without independent evidence.

### SG-20 — Owner-only boundary
**Requirement:** merge/approve/ready/rebase/deploy, credentials/security-policy changes, purchases/spend, supplier contact, production mutation/publication, unrestricted elevation, physical Windows action, and production autonomy remain owner-only unless Darrin explicitly grants a narrower authority.

**PASS evidence:** attempted execution without explicit authority fails closed and is recorded as BLOCKED/OWNER_REQUIRED, not as task failure or success.

## Batch-system integration

Every active Project Overseer subqueue must carry security alongside delivery. The :30 replenisher should add security items only where they are relevant to the workstream rather than creating generic busywork.

Each security-aware batch item must include:
- `security_gates`: SG IDs that materially apply;
- `risk_class`: S0–S4;
- `authority_required`: exact capability/approval boundary;
- `negative_tests`: adversarial cases required before promotion;
- `receipt_evidence`: exact durable evidence expected;
- `green_required`: yes/no;
- `prs_required`: yes/no;
- `owner_boundary`: any action reserved to Darrin;
- `security_disposition`: PENDING / ACTIVE / VERIFIED / BLOCKED / STALE / SPLIT_REQUIRED.

Security status never upgrades functional status automatically, and functional success never upgrades security status automatically.

## Overseer responsibilities

### AgentOS Overseer
Prioritize SG-01/02/03/08/09/10/11/14/16/18/19 around Level 2 remote bridge and autonomous runtime. Current continuous ownership and canonical authenticated transport/grant work are security blockers, not optional hardening.

### PRS Overseer
Own independent negative assurance for authority, ownership, replay, correlation, receipts, environment boundaries, and false-GREEN. PRS does not implement the target control plane unless explicitly assigned a bounded fixture/test harness.

### GlobalShopCo / Headless / eBay / Amazon / MyPrimeDelivery Overseers
Apply SG-02/03/05/06/09/10/12/13/14/15/20. Shopify remains canonical commercial authority. Missing freight, supplier permission, marketplace eligibility, stock, identity, or economics remain UNKNOWN/HOLD and cannot be converted into publication authority.

### Affiliate Websites Overseers
Apply SG-05/06/07/10/14/15/20 to affiliate links, program evidence, content ingestion, publisher identity, tracking, outbound CTA destinations, and publishing. Research content cannot self-authorize publication or affiliate claims.

### Content360 / Marketing Overseers
Apply SG-05/06/07/10/14/15. Credentials remain opaque; model/content/provider outputs are data only. Content may be generated/optimized in non-production but live publishing/campaign activation requires explicit authority.

### GhostKitchen / Franchise / GemVerse / Commercial Frontend Overseers
Apply SG-05/06/07/10/12/14/15/20 according to the actual surface. Synthetic economics, territory, canon, demand, or frontend evidence must never silently promote production capability.

## Agent Green recurring security mission

Green continuously samples the newest high-risk or newly VERIFIED items and challenges the applicable SG gates. Green should prefer real adversarial evidence over policy prose. When authorized, Green fixes the smallest defect, tests it, verifies the exact result, and updates the same batch item. Otherwise it injects an exact remediation item into the responsible Project Overseer subqueue.

## Promotion rule

A capability may widen only when:

1. functional acceptance criteria are VERIFIED;
2. every materially applicable security gate is independently VERIFIED or explicitly non-applicable with evidence;
3. exact actor/grant/correlation/receipt lineage is intact;
4. Green passes the exact head/evidence where required;
5. PRS passes the identical exact head/evidence where required;
6. owner-only actions remain blocked until explicit owner authority exists.

Any missing material evidence is `UNKNOWN`/`BLOCKED`, never presumed safe.

## Immediate security priorities

1. **AgentOS Level 2:** SG-08 continuous ownership fence remains the controlling blocker for safe writer autonomy.
2. **AgentOS remote admission:** SG-01/02 canonical authenticated actor/grant source remains BLOCKED until a real source is bindable without duplicating authority.
3. **Autonomous runtime:** SG-09/10/11 replay, exact correlation, durable receipts, crash recovery and false-success denial.
4. **Secrets:** SG-05 portfolio-wide credential isolation and redaction; no API key persistence in logs/batches/memory.
5. **Prompt injection / memory:** SG-06/07 adversarial fixtures for web/email/docs/API/provider outputs before broader autonomous ingestion.
6. **Kill/quarantine:** SG-16 deterministic global external-write stop plus worker/provider/tool/repo/mission quarantine design and tests.
7. **Commerce/content production:** SG-14/15/20 preserve non-production and owner-only publication/contact/spend boundaries.

No overall security GREEN or portfolio GREEN is implied by this policy document. Evidence controls promotion.