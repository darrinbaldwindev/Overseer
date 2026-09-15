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
- Lane-C and other non-core projects are owner-manual unless the owner explicitly re-enables scheduled execution. Their durable state is retained here for coordination only.

## Reconciliation checkpoint — 2026-09-15 18:32 Brisbane
Live evidence changed in coordination, not in AgentOS code lineage. AgentOS PR #104 remains OPEN/DRAFT/UNMERGED at exact `4c8bcc3bc2ad2041b0a1871d3004c1db23f3c091`; exact-head Ubuntu/Node22 and Windows/Node26 checks remain SUCCESS. Independent Jess/Michael handoff remains `BLOCKED_STABLE_SG08` / `BLOCKED_STABLE_CONTROLLING_GATES`, with SG-01/02 unresolved and PRS completion assurance NOT_ELIGIBLE. New durable assurance specifications add two implementation-ready cross-gate negatives: (1) recovery-state / authority-generation cross-bind and (2) authority revocation at the success-linearization boundary. These are queued behind the existing single-threaded SG-08 ownership repair and do not authorize a second lock/authority/recovery subsystem.

## Current ledger

| Task | Project | Priority | State | Owner | Exact anchor / dependency | Acceptance boundary / next transition |
|---|---|---:|---|---|---|---|
| A-AG-01 | AgentOS | P0 | BLOCKED_STABLE | SCHED-00-AGENTOS / WORK-PORTFOLIO, first exact claimant wins | `AgentOS#104@4c8bcc3bc2ad2041b0a1871d3004c1db23f3c091`; SG-08 | Existing single ownership primitive must hold continuously through verify -> side effect/prepared recovery -> durable success receipt -> release; no parallel ownership plane. Reopen only on changed candidate/evidence. |
| A-AG-02 | AgentOS | P0 | BLOCKED_STABLE | SCHED-00-AGENTOS | `#104@4c8bcc3...`; SG-01/02 | Authenticated actor + canonical grant source not wired end-to-end. No invented identity/grant registry. Reopen only when real existing source evidence changes. |
| A-AG-03 | AgentOS | P0 | PENDING | SCHED-00-AGENTOS | changed A-AG-01 candidate | 2–5 homogeneous ownership/crash/replay/result-write/correlation negatives with exact-head Ubuntu+Windows CI; no persistence/control-plane addition. |
| A-AG-04 | AgentOS | P0 | BLOCKED_STABLE | SCHED-00-AGENTOS | repaired #104 + admission + Jess/Michael + PRS + owner physical authority | Physical Windows install/5-minute scheduler acceptance is owner-gated; no simulated evidence. |
| A-AG-05 | AgentOS | P0 | ACTIVE | SCHED-00-AGENTOS | existing #104 authority-receipt lineage | Preserve exact source-backed authority evidence/correlation; do not duplicate A-AG-01/02. VERIFYING only on a changed exact head. |
| A-AG-06 | AgentOS | P0 | PENDING | SCHED-00-AGENTOS | after A-AG-01 repair; durable #49 assurance handoff `5676439889` | Add recovery-state/authority-generation cross-bind: stale G1/O1 prepared recovery must not inherit G2/O2 authority, publish, persist success or retire successor ownership. Exact-head Ubuntu+Windows CI required. SG-01/02/08/09/10/11/18/19; S2; Green+PRS required for promotion. |
| A-AG-07 | AgentOS | P0 | PENDING | SCHED-00-AGENTOS | after A-AG-01 repair; latest Jess/Michael handoff | Add authority-revocation-at-success-linearization negative: revocation/replacement immediately before durable success must fail closed with zero premature success and exact authority/ownership generation correlation. SG-01/02/08/10/11/18/19; S2. |
| A-AG-08 | AgentOS | P0 | ACTIVE | SCHED-00-AGENTOS | `AgentOS#112@d1645450a06d00c49a7a78f176e97b44b9eaa225` | Canonical runtime-shell eligibility consolidation; add only uncovered alias/evaluator denial cases, preserve #104 hot path; exact-head CI. |
| A-PRS-01 | PRS | P0 | VERIFIED | SCHED-40-ASSURANCE | historical `PRS#17@49fe1f8bca3ddae271d85e0f4767173060267222` | Historical false-GREEN baseline only; never certifies successor AgentOS heads. |
| A-PRS-02 | PRS | P0 | BLOCKED_STABLE | SCHED-40-ASSURANCE | unchanged `AgentOS#104@4c8bcc3...` | Do not recertify unchanged head. Reopen automatically on changed AgentOS candidate. |
| A-PRS-03 | PRS | P0 | BLOCKED_STABLE | SCHED-40-ASSURANCE | `PRS#24@3039c886bdcff911f7c6dcc3e086368058e57fb6` + future repaired AgentOS head | Completion-grade PRS requires identical-head Jess functional PASS + Michael security PASS + required owner/runtime gates. |
| A-PRS-04 | PRS | P0 | PENDING | SCHED-40-ASSURANCE | `PRS#24@3039c886...` | Independent fixture work only: stale/missing/mismatched AgentOS head, host/root, mutation/recovery/correlation/artifact identity. No physical execution. |
| B-GSC-01 | GlobalShopCo | P1 | ACTIVE | SCHED-15-COMMERCE | `#29@15fa99eb4c4b1f96127f6f51c412cbffc94e45e2`; `#30@80c82475b98663d677885e8b4d222ae2cedb8555` | Process only authenticated trade cost/freight/permission/stock/returns evidence. Any missing material field => HOLD/UNKNOWN. |
| B-GSC-02 | GlobalShopCo | P1 | PENDING | SCHED-15-COMMERCE | evidence-complete B-GSC-01 row | Delivered-margin calculation only after evidence completeness; stale/unknown/negative => HOLD. |
| B-GSC-03 | GlobalShopCo | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | current truth `0 eBay-ready SKUs` | Reopen only on exact evidence-complete variant; no synthetic commercial readiness. |
| B-GSC-04 | GlobalShopCo | P1 | PENDING | SCHED-15-COMMERCE | authenticated source routes only | 2–5 compact/light AU-stock candidates; capture identity/provenance/freight/permission/stock/returns or HOLD; stop at public/syndicated-only evidence. |
| B-HDL-01 | GlobalShopCo-Headless | P1 | VERIFIED | SCHED-15-COMMERCE | `#1@c3f4939f1b7de8ef6e7fe6547400343dbb076348` | Configured Shopify store authority + malformed authority negatives, bounded non-production only. |
| B-HDL-02 | GlobalShopCo-Headless | P1 | PENDING | SCHED-15-COMMERCE | same #1 lineage | Add 2–5 uncovered canonical-checkout/local-order/alternate-host denial cases; exact-head CI; Shopify remains commerce authority. |
| B-HDL-03 | GlobalShopCo-Headless | P1 | PENDING | SCHED-15-COMMERCE | same #1 lineage | Add homogeneous variant mismatch/stale availability/duplicate-cart identity contradictions; exact-head CI. |
| B-HDL-04 | GlobalShopCo-Headless | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | owner-authorized dev-store/browser environment | No dev-store/browser acceptance without genuine credentials/environment; remains non-production. |
| B-EBAY-01 | shopify_ebay | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | main `c68883f24fb3711fce567a35b1a80db74933b82a` | No evidenced canonical upstream replay persistence owner; never create a new persistence plane. |
| B-EBAY-02 | shopify_ebay | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | B-EBAY-01 | Restart replay durability waits for canonical upstream owner. |
| B-EBAY-03 | shopify_ebay | P1 | BLOCKED_STABLE | SCHED-15-COMMERCE | GlobalShopCo evidence-complete SKU | Current truth zero eligible SKUs; no live listing/publication. |
| B-EBAY-04 | shopify_ebay | P1 | PENDING | SCHED-15-COMMERCE | existing mapper lineage | 2–5 synthetic variant mismatch/malformed ID/conflicting hash/duplicate-event regressions; fixtures only; no network/publication/persistence. |
| B-MPD-01 | MyPrimeDelivery | P1 | ACTIVE | SCHED-15-COMMERCE | research `61feceb46de539948374deec86b3fe7578cf8014`; WordPress fixture `a38684c10541115f55f1d5612b72d669dced99f0`; merge base `3635c903214b06464e28674d5a6403f8539b8c1e` | Path-by-path compatibility map before presentation integration; no merge/rebase/stale overwrite. |
| B-MPD-02 | MyPrimeDelivery | P1 | PENDING | SCHED-15-COMMERCE | authorized coherent observations only | Current live `QUALIFIED=0`; public/editorial pages never become Prime/rank/deal authority. |
| B-MPD-03 | MyPrimeDelivery | P1 | VERIFIED | SCHED-15-COMMERCE | research `61feceb...` | One-observation coherence/conflicting-known-ASIN denial only; synthetic/non-production. |
| B-MPD-04 | MyPrimeDelivery | P1 | PENDING | SCHED-15-COMMERCE | B-MPD-01 | Port only compatible non-production presentation contract; HOLD/UNKNOWN cannot emit monetized/live CTA. |
| B-MPD-05 | MyPrimeDelivery | P1 | PENDING | SCHED-15-COMMERCE | existing validator lineage | 2–5 stale Prime/rank/deal or identity/outbound contradictions; exact-head fixture CI. |
| C-AFF-01 | Affiliate-Websites Master/AU/UK/US | P1 | ACTIVE | PROJECT-CHAT:Affiliate-Websites / WORK-PORTFOLIO | current Master/AU/UK/US seams | OWNER-MANUAL coordination only. Preserve country compliance, disclosure and UNKNOWN/non-affiliate CTA HOLD; no scheduled claim. |
| C-GK-01 | GhostKitchen | P1 | CLAIMED | SCHED-45-VENTURES | `GhostKitchen#32@eab5b290c93e111a0275308bee39945d9076c956`; exact-head economics CI verification | Owner re-enabled Lane-C scheduled execution. Verify current exact-head CI and reconcile GK-V1/GK-V3; do not widen economics or publication authority while CI is absent. |
| C-FR-01 | Franchise | P1 | PENDING | PROJECT-CHAT:Franchise / WORK-PORTFOLIO | GhostKitchen template evidence | OWNER-MANUAL. Gate-3 reusable franchise acceptance; synthetic/non-production. |
| C-GEM-01 | GemVerse | P2 | PENDING | PROJECT-CHAT:GemVerse / WORK-PORTFOLIO | current canon/recovery lineage | OWNER-MANUAL. Exact recovery identity; competing/ambiguous state fails closed. |
| C-C360-01 | content360 | P1 | ACTIVE | PROJECT-CHAT:Content360 / WORK-PORTFOLIO | current PR lineage + Marketing provenance | OWNER-MANUAL. Provenance/claim-strength/secret boundary; no live PUBLISH/SCHEDULE/network authority. |
| C-CF-01 | Commercial Frontend | P2 | PENDING | PROJECT-CHAT:Commercial Frontend / WORK-PORTFOLIO | Overseer commercial-frontend evidence | OWNER-MANUAL. Evidence packets/bounded correction only; demand/WTP remain hypotheses until externally evidenced. |
| C-MKT-01 | Marketing | P2 | ACTIVE | PROJECT-CHAT:Marketing / WORK-PORTFOLIO | canonical capability/pricing evidence | OWNER-MANUAL. Draft/research only; no unsupported readiness/security/autonomy claims or campaign activation. |
| C-CAR-01 | Car Rental | P2 | BLOCKED_STABLE | PROJECT-CHAT:Car Rental / WORK-PORTFOLIO | no canonical repo visible | Manual research lane only; reopen repo-backed implementation only when a real repo is visible. No purchase/contact/finance/listing. |
| OVR-01 | Overseer | P0 | ACTIVE | SCHED-30-REPLENISH | this ledger + project batches + #49 | Fresh-fetch before every shared write; reconcile exact handoffs; never become runtime scheduler/authority. |

## Ready queue ordering
1. AgentOS: A-AG-08 independent runtime-shell slice while A-AG-01/02 are BLOCKED_STABLE; A-AG-03/06/07 become executable only after changed ownership candidate.
2. PRS: A-PRS-04 independent fixture gaps; A-PRS-02/03 remain closed until changed AgentOS lineage and required identical-head assurance.
3. Commerce: B-HDL-02/03; B-EBAY-04; B-MPD-01 then B-MPD-04, with B-MPD-05 independent; B-GSC-04 only where authenticated evidence routes exist.
4. Lane C: SCHED-45-VENTURES may consume only exact tasks it first claims after fresh scan; skip C-AFF-01/C-C360-01/C-MKT-01 while already ACTIVE under another executor. GhostKitchen C-GK-01 is the current claimed verification slice.

## Security / authority boundary
Security is cross-cutting. Material AgentOS Level-2 work uses the applicable SG-01/02/03/08/09/10/11/14/18/19/20 gates; commerce applies applicable SG-02/05/06/09/10/12/13/14/15/20. Risk is S0/S1 for read-only/synthetic work and S2 for non-production branch/test mutations; unknown classification fails closed upward. Production/publication/contact/spend/credentials/security-policy/physical-host actions remain owner-only. Functional success never upgrades security, Green or PRS status.

## Claim / verification protocol
Fresh-scan ledger + project batch + live repo/PR/CI before claiming. PENDING -> CLAIMED only with exact identity; CLAIMED -> ACTIVE only when substantive work begins; ACTIVE -> VERIFYING only on exact candidate artifact/head; VERIFYING -> VERIFIED only with acceptance evidence. Changed head invalidates predecessor verification unless explicitly covered. Research tasks require exact source/date/provenance and VERIFIED FACT / REASONABLE INFERENCE / UNKNOWN separation.

## Relationship to batch files
`.overseer/batches/PORTFOLIO-EXECUTION-BATCH.md` remains the detailed scheduled-core execution queue. Project-local/manual batches retain their own detailed work. This ledger coordinates ownership across all visible portfolio work and does not override either.

**NO MODEL DECIDES ITS OWN AUTHORITY.** No merge/approve/ready/rebase/deploy, credentials/security-policy mutation, production writes/autonomy, purchases/spend, supplier/seller contact, live listing/publication/campaign activation, unrestricted elevation or invented physical Windows evidence without explicit owner authorization. No overall GREEN is implied.