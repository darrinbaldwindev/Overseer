# PORTFOLIO TASK LEDGER

Status: ACTIVE coordination index
Created: 2026-09-15
Owner: Portfolio Overseer

## Purpose

Canonical human-readable coordination ledger above portfolio batch files. It prevents scheduled executors, owner-started Work and project chats from duplicating the same exact task. It is **not** a scheduler, queue runtime, authority source, mission ledger, persistence service, Green system or PRS system. Repository/runtime/CI evidence outranks this ledger.

## State machine
`PENDING -> CLAIMED -> ACTIVE -> VERIFYING -> VERIFIED`
Holding/terminal: `BLOCKED | BLOCKED_STABLE | SUPERSEDED | REJECTED`.

Rules: CLAIMED requires an owner and exact task identity; ACTIVE requires substantive work evidence; VERIFYING requires an exact candidate lineage/artifact; VERIFIED requires stated acceptance evidence and never worker self-report alone. A changed code head invalidates predecessor verification unless evidence explicitly covers the successor. No task self-promotes authority, Green, security or PRS. If another executor owns an exact mutation lineage, select independent work.

## Executor identities / ownership
- `SCHED-00-AGENTOS` — AgentOS Level-2 executor.
- `SCHED-15-COMMERCE` — GlobalShopCo / Headless / Shopify-eBay / MyPrime executor.
- `SCHED-30-REPLENISH` — portfolio coordination/replenishment; does not compete with mutation owners.
- `SCHED-40-ASSURANCE` — Jess + Michael AgentOS/PRS assurance.
- `SCHED-45-VENTURES` — owner-re-enabled Lane C / Ventures executor; claims only exact Lane-C tasks not already ACTIVE/VERIFYING elsewhere.
- `WORK-PORTFOLIO` — owner-started Work.
- `PROJECT-CHAT:<name>` — project-specific manual executor.
- Lane-C and other non-core projects retain durable coordination state here. Their execution ownership is governed by the latest owner instruction and exact claims; this ledger never grants authority.

## Reconciliation checkpoint — 2026-09-15 19:32 Brisbane
Changed evidence only: GlobalShopCo-Headless PR #1 advanced from `c3f4939f1b7de8ef6e7fe6547400343dbb076348` to exact `708d32207e1e01bcbf8f9052698ffb29e98a8270`. Commit `708d322...` adds canonical checkout projection denials for HTTP downgrade, localhost/local-order target, hostname-suffix confusion, userinfo confusion and non-TLS port, while asserting zero network calls on denied inputs and retaining explicit TLS/443 acceptance. Exact-head `M3 checkout validation` run `34951837218` completed SUCCESS. Therefore the bounded non-production checkout-projection slice is VERIFIED on this exact successor lineage. Product identity/availability contradictions remain independently PENDING; real dev-store/browser acceptance remains BLOCKED_STABLE. AgentOS #104/#112 and PRS #24 exact heads are unchanged; no unchanged-head assurance was repeated. Lane-C/manual durable state is preserved unchanged.

## Current ledger

| Task | Project | Priority | State | Owner | Exact anchor / dependency | Acceptance boundary / next transition |
|---|---|---:|---|---|---|---|
| A-AG-01 | AgentOS | P0 | BLOCKED_STABLE | SCHED-00-AGENTOS / WORK-PORTFOLIO, first exact claimant wins | `AgentOS#104@4c8bcc3bc2ad2041b0a1871d3004c1db23f3c091`; SG-08 | Existing single ownership primitive must hold continuously through verify -> side effect/prepared recovery -> durable success receipt -> release; no parallel ownership plane. Reopen only on changed candidate/evidence. |
| A-AG-02 | AgentOS | P0 | BLOCKED_STABLE | SCHED-00-AGENTOS | `#104@4c8bcc3...`; SG-01/02 | Authenticated actor + canonical grant source not wired end-to-end. No invented identity/grant registry. Reopen only when real existing source evidence changes. |
| A-AG-03 | AgentOS | P0 | PENDING | SCHED-00-AGENTOS | changed A-AG-01 candidate | 2–5 homogeneous ownership/crash/replay/result-write/correlation negatives with exact-head Ubuntu+Windows CI; no persistence/control-plane addition. |
| A-AG-04 | AgentOS | P0 | BLOCKED_STABLE | SCHED-00-AGENTOS | repaired #104 + admission + Jess/Michael + PRS + owner physical authority | Physical Windows install/5-minute scheduler acceptance is owner-gated; no simulated evidence. |
| A-AG-05 | AgentOS | P0 | ACTIVE | SCHED-00-AGENTOS | existing #104 authority-receipt lineage | Preserve exact source-backed authority evidence/correlation; do not duplicate A-AG-01/02. VERIFYING only on a changed exact head. |
| A-AG-06 | AgentOS | P0 | PENDING | SCHED-00-AGENTOS | after A-AG-01 repair; durable #49 assurance handoff `5676439889` | Add recovery-state/authority-generation cross-bind after ownership repair; exact-head Ubuntu+Windows CI required. |
| A-AG-07 | AgentOS | P0 | PENDING | SCHED-00-AGENTOS | after A-AG-01 repair | Add authority-revocation-at-success-linearization negative after ownership repair. |
| A-AG-08 | AgentOS | P0 | ACTIVE | SCHED-00-AGENTOS | `AgentOS#112@d1645450a06d00c49a7a78f176e97b44b9eaa225` | Canonical runtime-shell eligibility consolidation; preserve #104 hot path; exact-head CI. |
| A-PRS-01 | PRS | P0 | VERIFIED | SCHED-40-ASSURANCE | historical `PRS#17@49fe1f8bca3ddae271d85e0f4767173060267222` | Historical false-GREEN baseline only. |
| A-PRS-02 | PRS | P0 | BLOCKED_STABLE | SCHED-40-ASSURANCE | unchanged `AgentOS#104@4c8bcc3...` | Reopen on changed AgentOS candidate. |
| A-PRS-03 | PRS | P0 | BLOCKED_STABLE | SCHED-40-ASSURANCE | `PRS#24@3039c886bdcff911f7c6dcc3e086368058e57fb6` + future repaired AgentOS head | Completion-grade PRS requires identical-head assurance. |
| A-PRS-04 | PRS | P0 | PENDING | SCHED-40-ASSURANCE | `PRS#24@3039c886...`; #49 handoff `5677299519` | Implement evidence-bundle mix-and-match/substitution and whole-bundle replay negatives; fixtures only, no physical execution. |
| B-GSC-01 | GlobalShopCo | P1 | ACTIVE | SCHED-15-COMMERCE | `#29@15fa99eb4c4b1f96127f6f51c412cbffc94e45e2`; `#30@80c82475b98663d677885e8b4d222ae2cedb8555` | Authenticated trade evidence only; missing material field => HOLD/UNKNOWN. |
| B-GSC-02 | GlobalShopCo | P1 | PENDING | SCHED-15-COMMERCE | evidence-complete B-GSC-01 row | Delivered-margin calculation only after evidence completeness. |
| B-GSC-03 | GlobalShopCo | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | current truth `0 eBay-ready SKUs` | Reopen only on exact evidence-complete variant. |
| B-GSC-04 | GlobalShopCo | P1 | PENDING | SCHED-15-COMMERCE | authenticated source routes only | Compact/light AU-stock evidence batch. |
| B-HDL-01 | GlobalShopCo-Headless | P1 | VERIFIED | SCHED-15-COMMERCE | `#1@708d32207e1e01bcbf8f9052698ffb29e98a8270`; run `34951837218` SUCCESS | Configured Shopify authority + malformed-authority predecessor tests remain passing on exact successor; bounded non-production only. |
| B-HDL-02 | GlobalShopCo-Headless | P1 | VERIFIED | SCHED-15-COMMERCE | `#1@708d32207e1e01bcbf8f9052698ffb29e98a8270`; run `34951837218` SUCCESS | Canonical checkout projection denials verified: downgrade/local-order/suffix/userinfo/non-TLS port fail closed with zero network calls. |
| B-HDL-03 | GlobalShopCo-Headless | P1 | PENDING | SCHED-15-COMMERCE | `#1@708d32207e1e01bcbf8f9052698ffb29e98a8270` | Variant mismatch/stale availability/duplicate-cart contradictions; keep homogeneous and non-production. |
| B-HDL-04 | GlobalShopCo-Headless | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | owner-authorized dev-store/browser environment | Real browser acceptance owner-gated. |
| B-EBAY-01 | shopify_ebay | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | main `c68883f24fb3711fce567a35b1a80db74933b82a` | No evidenced canonical upstream replay persistence owner. |
| B-EBAY-02 | shopify_ebay | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | B-EBAY-01 | Restart replay durability waits for canonical upstream owner. |
| B-EBAY-03 | shopify_ebay | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | GlobalShopCo evidence-complete SKU | Current truth zero eligible SKUs. |
| B-EBAY-04 | shopify_ebay | P1 | PENDING | SCHED-15-COMMERCE | existing mapper lineage | Synthetic identity regression fixtures only. |
| B-MPD-01 | MyPrimeDelivery | P1 | ACTIVE | SCHED-15-COMMERCE | research `61feceb46de539948374deec86b3fe7578cf8014`; fixture `a38684c10541115f55f1d5612b72d669dced99f0` | Compatibility map before presentation integration. |
| B-MPD-02 | MyPrimeDelivery | P1 | PENDING | SCHED-15-COMMERCE | authorized coherent observations only | Current live `QUALIFIED=0`. |
| B-MPD-03 | MyPrimeDelivery | P1 | VERIFIED | SCHED-15-COMMERCE | research `61feceb...` | Synthetic coherence baseline only. |
| B-MPD-04 | MyPrimeDelivery | P1 | PENDING | SCHED-15-COMMERCE | B-MPD-01 | Compatible non-production presentation contract only. |
| B-MPD-05 | MyPrimeDelivery | P1 | PENDING | SCHED-15-COMMERCE | existing validator lineage | Freshness/identity contradiction fixtures. |
| C-AFF-01 | Affiliate-Websites Master/AU/UK/US | P1 | ACTIVE | PROJECT-CHAT:Affiliate-Websites / WORK-PORTFOLIO | current Master/AU/UK/US seams | Preserve country compliance, disclosure and UNKNOWN/non-affiliate CTA HOLD; do not compete while ACTIVE. |
| C-GK-01 | GhostKitchen | P1 | BLOCKED_STABLE | SCHED-45-VENTURES | `GhostKitchen#32@766f69b92fe3ea5a98aca0cd611727cdf61c879d`; project handoff `GhostKitchen#31 comment 5677347199` | Repeated exact-head CI absence. Reopen only on a real workflow run, workflow/evidence-path repair, or materially changed implementation lineage. GK-V2 remains independently evidence-gated. |
| C-FR-01 | Franchise | P1 | PENDING | PROJECT-CHAT:Franchise / WORK-PORTFOLIO | GhostKitchen template evidence | Gate-3 reusable franchise acceptance; synthetic/non-production. |
| C-GEM-01 | GemVerse | P2 | PENDING | PROJECT-CHAT:GemVerse / WORK-PORTFOLIO | current canon/recovery lineage | Exact recovery identity; competing/ambiguous state fails closed. |
| C-C360-01 | content360 | P1 | ACTIVE | PROJECT-CHAT:Content360 / WORK-PORTFOLIO | current PR lineage + Marketing provenance | Do not compete while ACTIVE; no live PUBLISH/SCHEDULE/network authority. |
| C-CF-01 | Commercial Frontend | P2 | PENDING | PROJECT-CHAT:Commercial Frontend / WORK-PORTFOLIO | Overseer commercial-frontend evidence | Evidence packets/bounded correction only; demand/WTP remain hypotheses. |
| C-MKT-01 | Marketing | P2 | ACTIVE | PROJECT-CHAT:Marketing / WORK-PORTFOLIO | canonical capability/pricing evidence | Do not compete while ACTIVE; draft/research only. |
| C-CAR-01 | Car Rental | P2 | BLOCKED_STABLE | PROJECT-CHAT:Car Rental / WORK-PORTFOLIO | no canonical repo visible | Research-only; no substitute repo/purchase/contact/finance/listing. |
| OVR-01 | Overseer | P0 | ACTIVE | SCHED-30-REPLENISH | this ledger + project batches + #49 | Fresh-fetch before every shared write; coordination only. |

## Ready queue ordering
1. AgentOS/PRS/Commerce remain with their owning schedules; skip exact tasks already ACTIVE/VERIFYING elsewhere.
2. Headless B-HDL-02 is closed VERIFIED at `708d322...`; next independent Headless work is B-HDL-03 product identity/availability contradictions. Do not reopen dev-store/browser acceptance without owner environment evidence.
3. Lane C: C-GK-01 remains BLOCKED_STABLE. Eligible independent claims remain C-FR-01, C-GEM-01 or C-CF-01 only after fresh project scan and exact-lineage reconciliation; do not compete with ACTIVE Affiliate/Content360/Marketing work.

## Security / authority boundary
Security is cross-cutting. Risk is S0/S1 for read-only/synthetic work and S2 for non-production branch/test/docs mutations; unknown classification fails closed upward. Production/publication/contact/spend/credentials/security-policy/physical-host actions remain owner-only. Functional success never upgrades security, Green or PRS status.

## Claim / verification protocol
Fresh-scan ledger + project batch + live repo/PR/CI before claiming. PENDING -> CLAIMED only with exact identity; CLAIMED -> ACTIVE only when substantive work begins; ACTIVE -> VERIFYING only on exact candidate artifact/head; VERIFYING -> VERIFIED only with acceptance evidence. Changed head invalidates predecessor verification unless explicitly covered. Research tasks require exact source/date/provenance and VERIFIED FACT / REASONABLE INFERENCE / UNKNOWN separation.

## Relationship to batch files
`.overseer/batches/PORTFOLIO-EXECUTION-BATCH.md` remains the detailed scheduled-core execution queue. Project-local/manual batches retain their own detailed work. This ledger coordinates ownership across all visible portfolio work and does not override either.

**NO MODEL DECIDES ITS OWN AUTHORITY.** No merge/approve/ready/rebase/deploy, credentials/security-policy mutation, production writes/autonomy, purchases/spend, supplier/seller contact, live listing/publication/campaign activation, unrestricted elevation or invented physical Windows evidence without explicit owner authorization. No overall GREEN is implied.