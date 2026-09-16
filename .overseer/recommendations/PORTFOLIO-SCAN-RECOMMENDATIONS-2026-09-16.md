# PORTFOLIO SCAN — GAPS & RECOMMENDATIONS

Date: 2026-09-16
Owner: Portfolio Overseer
Status: RECOMMENDATIONS / NOT AUTHORITY / NOT GREEN

This record captures findings from a fresh portfolio repository and open-work scan. Repository, exact-head runtime, CI, security, Green and PRS evidence outrank this document. This document does not authorize implementation, merging, deployment, credentials, production writes, purchases, publication, contact or physical-host actions.

## Portfolio inventory observed

Connected portfolio inventory reviewed:
- AgentOS
- Overseer
- PRS
- Franchise
- GhostKitchen
- GlobalShopCo
- GlobalShopCo-Headless
- shopify_ebay
- MyPrimeDelivery
- Affiliate-Websites
- GemVerse
- content360

Structural item to reconcile: MyPrimeDelivery and GlobalShopCo were observed using `agent/overseer/initial-project-timeline` as default branch rather than `main`; GemVerse uses `gemverse`. Confirm these are intentional and document canonical branch rules so automation cannot silently inspect or mutate the wrong lineage.

## Priority recommendations

### R-01 — Portfolio lineage consolidation gate
AgentOS has accumulated many concurrent/open draft lineages. Establish a non-destructive lineage classification pass using:
`CANONICAL | ABSORBED | SUPERSEDED | HISTORICAL | ABANDONED`.

Before any close/merge action, map unique evidence and implementation content and establish one canonical implementation lineage per capability. Do not auto-close or auto-merge.

### R-02 — AgentOS admission -> local-wake compatibility
Treat admission-to-wake contract compatibility as a P0 integration concern. PRS evidence has identified a possible contract mismatch in which canonical non-PowerShell remote admission output does not carry fields required downstream by local wake (`consent_mode`, `acceptance_criteria`, `target`). Re-fetch the exact current candidate and PRS evidence before implementation. If still present, repair through the existing canonical contract rather than adding a second adapter/control plane.

Suggested task label: `S-SRV-02B / A-AG-P0 — Admission-to-Wake Contract Compatibility`.

Acceptance should include exact correlation preservation, deterministic fail-closed negatives, exact-head Ubuntu/Windows CI where applicable, and independent Jess/Michael/PRS evidence before completion claims.

### R-03 — Server identity and tenancy ADR
Before implementing a new identity provider or grant registry, define an evidence-controlled Server Identity & Tenancy architecture decision record:

`Organization -> User -> Membership -> Role -> Session -> authenticated actor -> AgentOS grant -> Project -> Mission -> Worker/Host`

Explicitly separate authentication, organization membership, commercial seat entitlement and execution authority. No model or transport may manufacture authority.

### R-04 — Strong worker identity/provenance
For Server worker projection, design for host identity, worker identity, build/code identity, capability evidence, boot/session identity and freshness/heartbeat. None of these confer authority. Evaluate signed worker/build attestations as a future hardening layer for remote/multi-customer operation.

### R-05 — Canonical evidence envelope
Define a reusable portfolio evidence schema rather than duplicating evidence vocabulary in each project. Candidate core fields:
- source
- observed_at
- fresh_until
- subject
- claim
- classification
- evidence_ref
- collector
- code/version identity
- explicit UNKNOWN state

Projects may extend this schema. It must not become a competing authority, ledger, scheduler, Green or PRS system.

### R-06 — Franchise persistence tenancy gate
Prioritize two-franchise persistence-isolation acceptance before expanding territory/application breadth. Existing application/runtime and membership work is useful, but database-backed membership/context, tenant-scoped repository behavior and cross-tenant persistence isolation remain the security-relevant closure target. Do not infer storage isolation from UI/domain isolation.

### R-07 — Shared commerce product-evidence contract
GlobalShopCo, shopify_ebay, MyPrimeDelivery, Affiliate-Websites and Marketing repeatedly require overlapping product facts. Define a shared evidence contract/library for product identity, source, price, shipping, availability, region, compliance, affiliate eligibility, marketplace eligibility, observation time and freshness.

This should be a shared schema/library only, not a shared authority or new persistence control plane. Missing material fields remain HOLD/UNKNOWN.

### R-08 — Affiliate program lifecycle
Extend Affiliate-Websites beyond discovery/presentation with an explicit lifecycle:

`discovered -> application -> approval -> tracking identity -> destination verification -> disclosure requirements -> commission terms -> freshness/recheck -> suspended/terminated`

Stale or unverifiable programs must degrade to STALE/UNKNOWN and must not continue to appear verified merely because they were historically valid.

### R-09 — GhostKitchen <-> Franchise versioned evidence seam
Keep GhostKitchen and Franchise separate products while defining a versioned handoff:

`Concept/Economics Evidence -> Franchise Offering Candidate`

GhostKitchen owns concept/economics evidence; Franchise owns tenancy, territory and operator mechanics. Avoid copying business logic between repositories.

### R-10 — Overseer coordination cleanup
Reconcile older Overseer reconciliation lineages against the newer canonical portfolio task ledger and maximum vertical batches. Preserve unique evidence before classifying older work as superseded. No automatic closure.

## Cross-cutting architecture additions

### Canonical Correlation Passport
Define one portfolio correlation vocabulary. Each project declares the subset required for its governed operations. AgentOS should continue to preserve at least the relevant delivery/request/project/mission/task/wake/host/worker/code/actor/authority correlation. Other projects can use smaller domain-specific subsets.

This is a vocabulary/contract, not a new mission ledger or authority source.

### Portfolio Dependency Graph
Add a dependency/unlock view to Overseer so replenishment can select work that unlocks the most downstream verified progress rather than selecting only by static priority.

Example AgentOS/Server chain:
`admission-to-wake compatibility -> continuous ownership -> authenticated identity/grant provenance -> physical Windows Level-2 acceptance -> Server authenticated adapter -> Server worker identity/health -> Server non-production E2E`.

Example commerce chain:
`evidence-complete GlobalShopCo SKU -> eBay mapper -> synthetic listing -> governed pilot -> marketing evidence`.

The graph is coordination metadata only and must not become a scheduler, queue runtime, mission ledger or authority source.

## Recommended portfolio operating balance

Current constraint is increasingly integration, canonicalization and evidence closure rather than feature scarcity. Recommended planning bias: approximately 70% integration/closure and 30% new capability work until the main execution paths are demonstrably connected.

Suggested immediate technical chain:
1. AgentOS admission-to-wake compatibility.
2. SG-08 continuous ownership/crash safety.
3. Authenticated identity and canonical grant provenance.
4. Physical Windows Level-2 acceptance when owner-authorized.
5. Server authenticated adapter.
6. Server worker identity/health projection.
7. Server non-production end-to-end acceptance.

## Governance

These are recommendations, not completion claims. No overall GREEN is implied. Before executing any item, fresh-fetch the canonical task ledger, relevant repository branch/PR exact head, CI/runtime evidence and latest assurance handoff; avoid competing with ACTIVE/CLAIMED lineages.

NO MODEL DECIDES ITS OWN AUTHORITY.
