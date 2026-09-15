# PORTFOLIO TASK LEDGER

Status: ACTIVE coordination index
Created: 2026-09-15
Owner: Portfolio Overseer

## Purpose

This file is the canonical human-readable coordination ledger above the portfolio batch files. It prevents scheduled Overseers, manual Work windows and project chats from unknowingly duplicating the same task.

It is **not** a scheduler, queue implementation, authority source, mission ledger, persistence service, Green system or PRS system. AgentOS remains authoritative for runtime execution/governance. Repository/runtime/CI evidence outranks this ledger.

## State machine

`PENDING -> CLAIMED -> ACTIVE -> VERIFYING -> VERIFIED`

Alternative terminal/holding states:
- `BLOCKED` — currently blocked but dependency may change soon.
- `BLOCKED_STABLE` — same external dependency unchanged for two relevant cycles; do not repeatedly burn execution capacity.
- `SUPERSEDED` — replaced by a newer exact task/lineage.
- `REJECTED` — evidence proves the proposed work should not proceed.

Rules:
1. CLAIMED requires an owning Overseer/context and exact project/task identity.
2. ACTIVE requires evidence that substantive work started.
3. VERIFYING requires an exact candidate lineage/artifact.
4. VERIFIED requires the task's stated acceptance evidence; worker self-report alone is insufficient.
5. A changed code head invalidates predecessor verification unless the evidence explicitly covers the successor.
6. No task may self-promote authority, Green, security or PRS status.
7. Before claiming, reconcile this ledger + project batch + live repo/PR/CI evidence.
8. If another executor owns the exact mutation lineage, do not create a competing implementation.

## Executor identities

- `SCHED-00-AGENTOS` — hourly :00 AgentOS Level-2 executor.
- `SCHED-15-COMMERCE` — hourly :15 GlobalShopCo / Headless / Shopify-eBay / MyPrime executor.
- `SCHED-30-REPLENISH` — hourly :30 queue/batch replenisher; normally does not compete with active mutation owners.
- `SCHED-40-ASSURANCE` — hourly :40 Jess + Michael independent functional/security assurance; AgentOS/PRS scope.
- `SCHED-45-VENTURES` — hourly :45 Lane-C / full-portfolio visibility executor.
- `WORK-PORTFOLIO` — owner-started ChatGPT Work window using OWNER-START-WORK-BATCH.
- `PROJECT-CHAT:<name>` — project-specific Overseer chat.

## Current ledger

| Task | Project | Priority | State | Owner | Depends on | Current evidence / boundary | Next transition |
|---|---|---:|---|---|---|---|---|
| A-AG-01 | AgentOS | P0 | PENDING | SCHED-00-AGENTOS / WORK-PORTFOLIO, first exact claimant wins | existing #104 lineage | SG-08 continuous crash-releasing ownership fence not yet proven; do not create parallel ownership system | CLAIMED by first executor that binds exact #104 head and begins repair |
| A-AG-02 | AgentOS | P0 | PENDING | SCHED-00-AGENTOS | bounded PowerShell runtime + local-wake | Wire existing governed bounded PowerShell into existing local-wake; no new scheduler/queue/authority plane; project-file mutation remains disabled | CLAIMED when exact hot-path implementation begins |
| A-AG-03 | AgentOS | P0 | PENDING | SCHED-00-AGENTOS | A-AG-01 changed candidate | concurrency/crash/replay/result-write/correlation regression matrix | ACTIVE after ownership candidate exists |
| A-AG-04 | AgentOS | P0 | PENDING | SCHED-00-AGENTOS | A-AG-01/02/03 + assurance | software-side physical Windows install + real 5-minute scheduler acceptance packet; no simulated owner evidence | ACTIVE only when software prerequisites pass |
| A-AG-05 | AgentOS | P0 | ACTIVE | SCHED-00-AGENTOS | existing authority admission/receipt lineage | Authority evidence receipt provenance advanced previously; remain bounded to correlation/replay and do not duplicate A-AG-01 | VERIFYING on exact changed head |
| A-PRS-01 | PRS | P0 | BLOCKED | SCHED-40-ASSURANCE | changed AgentOS candidate + Jess/Michael identical-lineage results | Historical assurance does not certify successor | ACTIVE only after candidate changes and prerequisites exist |
| B-GSC-01 | GlobalShopCo | P1 | ACTIVE | SCHED-15-COMMERCE | authenticated supplier/commercial evidence | Close one exact SKU evidence bundle; missing cost/freight/permission/stock remains HOLD/UNKNOWN | VERIFYING when one complete candidate bundle exists |
| B-EBAY-01 | shopify_ebay | P1 | ACTIVE | SCHED-15-COMMERCE | existing mapper lineage | Deterministic replay/conflict work allowed; no invented durable replay store; no live listing | VERIFYING on exact synthetic test head |
| B-HDL-01 | GlobalShopCo-Headless | P1 | PENDING | SCHED-15-COMMERCE | existing headless checkout contract | Add only uncovered fail-closed Shopify checkout/variant/availability negatives | CLAIMED on exact current lineage |
| B-MPD-01 | MyPrimeDelivery | P1 | PENDING | SCHED-15-COMMERCE | divergent research/WordPress lineages | Reconcile compatibility before UI growth; no invented Prime/rank/deal authority | CLAIMED after fresh lineage map |
| C-AFF-01 | Affiliate-Websites | P1 | ACTIVE | SCHED-45-VENTURES / relevant PROJECT-CHAT, first exact claimant wins | current Master/AU/UK/US seams | Governed presentation/evidence contract; country compliance retained | VERIFYING per exact country/template slice |
| C-GK-01 | GhostKitchen | P1 | PENDING | SCHED-45-VENTURES | representative-order evidence | Advance deterministic economics/field evidence; UNKNOWN stays UNKNOWN | CLAIMED after fresh scan |
| C-FR-01 | Franchise | P1 | PENDING | SCHED-45-VENTURES | GhostKitchen template evidence | Advance Gate-3 reusable franchise acceptance; no deployment | CLAIMED after fresh scan |
| C-GEM-01 | GemVerse | P2 | PENDING | SCHED-45-VENTURES | current canon/recovery lineage | Recovery identity must be exact; ambiguous competing state fails closed | CLAIMED after fresh scan |
| C-C360-01 | content360 | P1 | ACTIVE | SCHED-45-VENTURES | Marketing provenance + existing PR lineage | Provenance/claim-strength/secret-boundary work active; no live publication; credentials opaque | VERIFYING only with exact-head CI |
| C-MKT-01 | Marketing | P2 | ACTIVE | SCHED-45-VENTURES / Marketing PROJECT-CHAT, first exact claimant wins | canonical AgentOS pricing/capability evidence | Draft/research only; no unsupported readiness/security/autonomy claims; no campaign activation | VERIFYING per evidence-gated asset |
| C-CAR-01 | Car Rental | P2 | PENDING | SCHED-45-VENTURES / PROJECT-CHAT:Car Rental | no canonical repo visible | Manual research lane only; no substitute repo; no purchase/contact/finance/listing | ACTIVE when next evidence research slice starts |

## Claim protocol

Before substantive execution:
1. Fresh-scan the project repo/PR/CI and this ledger.
2. If exact task is ACTIVE under another executor, do not compete. Select an independent adjacent task.
3. If task is PENDING, update its owner/state to CLAIMED with exact repo/branch/head/PR/evidence anchor where applicable.
4. Move CLAIMED -> ACTIVE only when substantive work begins.
5. Move ACTIVE -> VERIFYING only when an exact candidate artifact/head exists.
6. Move VERIFYING -> VERIFIED only with acceptance evidence.
7. On external blocker, record exact dependency. After two unchanged relevant cycles use BLOCKED_STABLE and fall through.

## Verification protocol

For code tasks record:
- repository;
- branch;
- exact head;
- PR;
- files materially changed;
- local tests;
- exact-head CI;
- independent assurance where required.

For research/commercial tasks record:
- exact source/provenance/date;
- VERIFIED FACT / REASONABLE INFERENCE / UNKNOWN;
- acceptance criteria satisfied/missing;
- prohibited action boundary.

## Relationship to existing batch files

- `.overseer/batches/OWNER-START-WORK-BATCH-2026-09-15.md` = large owner-started execution batch.
- `.overseer/batches/PORTFOLIO-EXECUTION-BATCH.md` = live detailed/replenished work queue.
- `PORTFOLIO-TASK-LEDGER.md` = coordination/claim/status index above those batches.

The detailed batch files define **what** to do. This ledger identifies **who currently owns the exact task and what evidence is required to change its state**.

## Mandatory handoff update

Any executor materially changing a listed task should update this ledger or leave a durable handoff that the next replenisher can reconcile into it. Never overwrite a newer concurrent update: fresh-fetch immediately before writing and reconcile first.

Hard boundaries remain: no merge/approve/mark-ready/rebase/deploy, credentials/security-policy mutation, production writes/autonomy, purchases/spend, supplier/seller contact, live listings/publication/campaign activation, unrestricted elevation or invented physical Windows evidence without explicit owner authorization.
