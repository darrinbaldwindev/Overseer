# Portfolio Execution Batch Manifest

**Purpose:** canonical deep bounded queue for the fixed scheduled portfolio lanes. Exact repo/issue/CI/runtime evidence outranks scheduler firing and worker claims.

**Fixed lanes:** A = AgentOS Level 2 P0 + PRS/Green; B = GlobalShopCo/Headless/eBay/Amazon/MyPrimeDelivery; C = Affiliate-Websites AU/UK/US/Master, GhostKitchen, Franchise, GemVerse, Content360, Commercial Frontend, Marketing.

**States:** `PENDING | ACTIVE | VERIFIED | BLOCKED | STALE | SPLIT_REQUIRED`.

**Hard boundary:** no merge/approve/ready/rebase/deploy/credentials/production writes/purchases/supplier contact/live publication/production autonomy. **NO MODEL DECIDES ITS OWN AUTHORITY.** Functional and security status remain independent.

## Historical evidence registry — retained
- Prior deep checkpoint: Overseer #49 comment `5661238167`; prior manifest blob `56b9160270a766d436c901105ebc6eb6dd44592a`.
- AgentOS PR #104 exact `83a58b8bd230550b5781a0fee700cca250819a75`; push Tests `34821384346` SUCCESS Ubuntu/Windows+audit; PR-triggered `34821388860` CANCELLED and is not CI authority.
- PRS current defect baseline: PRS `0defebe26f71e1cf5df1168fa5454bfd8de30091` targeting AgentOS `83a58b8...`; run `34821646371`; `DEFECT_REPRODUCED` for both continuous-ownership false-success cases.
- Headless M3 baseline `9799e6fe5a9c72e42e1554949697a64acce14bd4` / `34798624627` SUCCESS.
- GlobalShopCo free-delivery gate `f4e5de0e0e946a5c6844dea84d99527d0c9f8474`; `34822003322`,`34822003312` SUCCESS.
- eBay prior baseline `b57e0a47...` / `34805527804`; current synthetic commercial-ingest head `86d71436534a42a742cf6f9ce723fe1b90895e12` / `34827082183` SUCCESS.
- Amazon prior baseline `95191c...` / `34821710314`; current zero-authority receipt head `25f77d9b0c21a1fc306c05807e869b6dc72beac0` / `34827128200` SUCCESS.
- MyPrime prior baseline `1820dfe1...` / `34811798266`; current source-rights head `ba9d61ddd4d10a894e02a94d789d8bf26d232a5c` / `34827189247` SUCCESS; authorised live Prime/rank/deal provider UNKNOWN.
- Affiliate master `d901b3e2c0c772cdc43019dd96cf2b19bdded0a6` / `34798980244` SUCCESS.
- GhostKitchen economics `ddfb2d872ca116b2cf18d3a98d53670b0c228237` / `34799531732` SUCCESS.
- Franchise main `29fa0546f0d7abe03fcc1af3d0770e7e50925c31` / `34799016286`; PR #22 `7b8b07562f69ce7988f82e1f3ec71a225fb23709` / `34800298175`,`34800338862` SUCCESS.
- GemVerse PR #10 `b1f09c3a9300a24782f5f3e4ab01619a64477319` / `34803885504` SUCCESS.
- Content360 `8dd031bb1efaf7d0909bdc411365faf3da497f84` / `34791442838` SUCCESS.
- Commercial Frontend evidence `55b189f99025038a2c9bf9fd15a757225a7ab3be`; issue #21 comment `5659574435`.
- AgentOS frontend PR #111 exact `b14c5d81f1295ba434d6a6fd9bf5e38e4aa8ffae`; Tests `34827244536` SUCCESS for bounded read-only evidence projection only.

# LANE A — AGENTOS LEVEL 2 P0
## AgentOS Overseer subqueue
### A-AG-01 — continuous project-file ownership primitive
- status: BLOCKED; owner/workstream: AgentOS / writer ownership; anchor: PR #104 `83a58b8...`, PRS `0defebe...` / `34821646371` DEFECT_REPRODUCED.
- objective: one kernel-enforced crash-releasing fence held verify→publish/prepared recovery→durable success receipt→release; acceptance: successor/stale owner cannot publish or persist success; dependencies: real writer change; safe action boundary: branch code/tests only; verification: targeted adversarial suite + exact-head Ubuntu/Windows CI + Jess Green then PRS; next handoff: AgentOS implementation worker.
- security_gates: `SG-03,SG-08,SG-09,SG-10,SG-11,SG-14,SG-18,SG-19`; risk_class: S2; authority_required: scoped non-prod branch/test writes; negative_tests: replacement-after-verify, successor writer, TOCTOU, crash/replay, duplicate result, prepared-recovery stale owner; receipt_evidence: actor/task/file/pre/postimage/ownership/result lineage; green_required: yes; prs_required: yes; owner_boundary: merge/deploy/physical production; security_disposition: BLOCKED.
### A-AG-02 — exact-current-head CI accounting
- status: VERIFIED; owner/workstream: AgentOS / CI evidence; anchor: `83a58b8...`, push `34821384346` SUCCESS Ubuntu+Windows+audit; cancelled `34821388860` retained separately.
- objective: preserve exact-head CI truth without transferring PASS to successor heads; acceptance: run/head/job identity explicit; dependencies: none; safe boundary: evidence only; verification: workflow/job SHA; next handoff: successor head must rerun.
- security_gates: `SG-18`; risk_class: S0; authority_required: read-only CI; negative_tests: cancelled-run-not-PASS; receipt_evidence: exact head/run/jobs; green_required: no for CI accounting; prs_required: no; owner_boundary: merge/deploy; security_disposition: VERIFIED.
### A-AG-03 — canonical authenticated authority-admission producer
- status: BLOCKED; owner/workstream: AgentOS / authority admission; anchor: PR #104 `83a58b8...`, authenticated transport + canonical grant lookup still unwired.
- objective: bind existing authenticated actor + canonical grant source without duplicate authority; acceptance: payload cannot self-supply actor/grant and mismatch yields zero artifacts; dependencies: real bindable canonical sources; safe boundary: architecture/code/tests, no new registry; verification: spoof/missing/mismatch/cross-project/replay tests; next handoff: architecture/implementation only when source evidenced.
- security_gates: `SG-01,SG-02,SG-03,SG-04,SG-09,SG-10,SG-11,SG-18,SG-19`; risk_class: S2; authority_required: canonical identity/grant read + scoped branch change; negative_tests: spoof actor, absent/mismatch grant, cross-project, replay; receipt_evidence: issuer/source/version + request/task/mission; green_required: yes; prs_required: yes; owner_boundary: credentials/security policy; security_disposition: BLOCKED.
### A-AG-04 — correlation/idempotency preservation
- status: VERIFIED; owner/workstream: AgentOS / remote-bridge lineage; anchor: `83a58b8...` + `34821384346`.
- objective: preserve exact delivery/request/task/mission/wake/actor/grant/result lineage and zero-artifact denial; acceptance: malformed/mismatch/replay fail closed; dependencies: no authority widening; safe boundary: tests/small adjacent fixes; verification: targeted suite + exact-head CI; next handoff: rerun on any runtime change.
- security_gates: `SG-01,SG-02,SG-09,SG-10,SG-11,SG-18`; risk_class: S2; authority_required: branch tests; negative_tests: duplicate pickup, stale delivery, mismatch, missing authority evidence; receipt_evidence: denial + accepted lineage; green_required: yes before promotion; prs_required: conditional; owner_boundary: merge/deploy; security_disposition: BLOCKED while SG-01/02/08 unresolved.
### A-AG-05 — bounded evidence-projection integration seam
- status: PENDING; owner/workstream: AgentOS / Basic Chat evidence read path; anchor: frontend PR #111 `b14c5d81...` / `34827244536` SUCCESS.
- objective: wire existing local persistence artifact/event lists through `projectBasicChatEvidence(lastTaskId, records)` into existing Basic Chat snapshot/What happened without new persistence/run identity/recovery state; acceptance: read-only, task-correlated, private/raw fields excluded, missing evidence fails closed, no Henry/PRS inference; dependencies: current canonical records only; safe boundary: draft branch code/tests; verification: exact-head projection tests + full CI; next handoff: frontend Overseer.
- security_gates: `SG-03,SG-05,SG-10,SG-11,SG-14,SG-18`; risk_class: S2; authority_required: non-prod branch code/tests; negative_tests: cross-task record, private/raw leakage, missing evidence, fabricated PRS/recovery; receipt_evidence: exact task/mission/wake/completion/Green projection; green_required: conditional; prs_required: no unless authority semantics change; owner_boundary: merge/deploy; security_disposition: PENDING.

## PRS / Jess Green assurance subqueue
### A-PRS-01 — immutable ownership defect baseline
- status: VERIFIED; owner/workstream: PRS; anchor: `0defebe...` / `34821646371` targeting `83a58b8...`; objective: retain exact false-GREEN baseline; acceptance: evidence applies only to exact target; dependencies: none; safe boundary: read-only; verification: target/tree/artifact hashes; next handoff: A-AG-01.
- security_gates: `SG-08,SG-10,SG-11,SG-19`; risk_class: S0; authority_required: read-only; negative_tests: normal publish + prepared recovery stale-owner cases; receipt_evidence: immutable hashes; green_required: no; prs_required: this is PRS evidence; owner_boundary: none; security_disposition: VERIFIED.
### A-PRS-02 — replacement ownership exact-head challenge
- status: BLOCKED; owner/workstream: PRS; anchor: A-PRS-01; objective: rerun only after real writer change and Jess exact-head PASS; acceptance: normal/prepared/successor/crash/replay independently classified; dependencies: A-AG-01 + exact CI + Jess PASS; safe boundary: harness only; verification: immutable target hashes; next handoff: Overseer.
- security_gates: `SG-08,SG-09,SG-10,SG-11,SG-19`; risk_class: S2; authority_required: read target + bounded harness writes; negative_tests: full ownership matrix; receipt_evidence: exact target/artifact; green_required: yes prerequisite; prs_required: yes; owner_boundary: merge/deploy; security_disposition: BLOCKED.
### A-PRS-03 — admission false-GREEN challenge
- status: BLOCKED; owner/workstream: PRS; anchor: A-AG-03 unwired; objective: prove no self-authorization or provenance mismatch can reach artifacts; acceptance: missing/spoof/mismatch/replay all zero false success; dependencies: A-AG-03 + Jess PASS; safe boundary: assurance only; verification: exact hashes/adversarial outputs; next handoff: Overseer.
- security_gates: `SG-01,SG-02,SG-03,SG-09,SG-10,SG-11,SG-19`; risk_class: S2; authority_required: read target + harness; negative_tests: actor/grant attacks; receipt_evidence: exact target/denials; green_required: yes prerequisite; prs_required: yes; owner_boundary: credentials/security policy; security_disposition: BLOCKED.

# LANE B — COMMERCE
## GlobalShopCo subqueue
### B-GSC-01 — free-delivery calculator
- status: VERIFIED; owner/workstream: GlobalShopCo economics; anchor: `f4e5de0...` / `34822003322`,`34822003312`; objective: retain fail-closed landed economics; acceptance: critical UNKNOWN=>HOLD; dependencies: none; safe boundary: synthetic; verification: CI/receipts; next handoff: B-GSC-02.
- security_gates: `SG-10,SG-12,SG-13,SG-14,SG-20`; risk_class: S2; authority_required: fixture writes; negative_tests: missing freight/fees/negative price; receipt_evidence: exact inputs/calculation; green_required: no; prs_required: no; owner_boundary: pricing/purchase/listing; security_disposition: VERIFIED.
### B-GSC-02 — compact Home Organisation exact-SKU economics
- status: PENDING; owner/workstream: GlobalShopCo qualification; anchor: #17, 0 eBay-ready SKUs, Dropshipzone/New Aim permission-first RESEARCH LEAD only; objective: qualify/reject one compact exact SKU with acquisition, freight, AU delivered comps, returns/warranty; acceptance: every cost sourced or UNKNOWN and missing trade/freight/permission=>HOLD; dependencies: public/read-only evidence; safe boundary: research/docs; verification: dated sources + calculator receipt; next handoff: channel gates.
- security_gates: `SG-06,SG-10,SG-12,SG-13,SG-14,SG-20`; risk_class: S1; authority_required: public research; negative_tests: retail-as-wholesale, stale price, freight missing; receipt_evidence: SKU/source/date/cost; green_required: no; prs_required: no; owner_boundary: contact/purchase/listing; security_disposition: PENDING.
### B-GSC-03 — supplier permission/blind-shipping identity matrix
- status: PENDING; owner/workstream: GlobalShopCo supplier governance; anchor: #17; objective: separate public resale-language lead from exact marketplace permission, fulfilment/packing identity and trade-account evidence; acceptance: UNKNOWN stays HOLD; dependencies: public terms only; safe boundary: no supplier contact; verification: source/date matrix; next handoff: B-GSC-02/eBay/Amazon.
- security_gates: `SG-06,SG-10,SG-14,SG-20`; risk_class: S1; authority_required: public research; negative_tests: generic resale mistaken for marketplace/blind-shipping approval; receipt_evidence: supplier/source/date/status; green_required: no; prs_required: no; owner_boundary: supplier contact/account; security_disposition: PENDING.

## Headless subqueue
### B-HDL-01 — checkout parser boundary review
- status: PENDING; owner/workstream: Headless; anchor: M3 `9799e6fe...` / `34798624627`; objective: enumerate actual parser normalization before adding tests; acceptance: no invented cases; dependencies: repo read; safe boundary: read-only; verification: exact path/head; next handoff: B-HDL-02.
- security_gates: `SG-03,SG-06,SG-10,SG-14`; risk_class: S1; authority_required: repo read; negative_tests: derived from parser; receipt_evidence: head/path findings; green_required: no; prs_required: no; owner_boundary: deploy/prod config; security_disposition: PENDING.
### B-HDL-02 — applicable host-confusion fixtures
- status: PENDING; owner/workstream: Headless; anchor: B-HDL-01/M3; objective: add only parser-relevant confusion tests; acceptance: canonical Shopify HTTPS allowed, confusion denied; dependencies: B-HDL-01; safe boundary: tests; verification: CI; next handoff: Jess only if runtime boundary changes.
- security_gates: `SG-03,SG-10,SG-14,SG-18`; risk_class: S2; authority_required: branch tests; negative_tests: parser-applicable host confusion; receipt_evidence: URL/disposition; green_required: conditional; prs_required: no; owner_boundary: deploy/Shopify prod; security_disposition: PENDING.
### B-HDL-03 — dev-store/browser packet
- status: BLOCKED; owner/workstream: Headless browser acceptance; anchor: issue #3; objective: future owner-authorized non-prod proof packet; acceptance: environment/product/redirect/no-secret evidence; dependencies: owner dev access; safe boundary: preparation only; verification: checklist/live proof later; next handoff: owner.
- security_gates: `SG-05,SG-10,SG-14,SG-20`; risk_class: S2; authority_required: dev-store access; negative_tests: prod host/token denial; receipt_evidence: environment-bound packet; green_required: yes for promotion; prs_required: no; owner_boundary: credentials/prod access; security_disposition: BLOCKED.

## Shopify→eBay subqueue
### B-EBY-01 — commercial evidence ingest
- status: VERIFIED; owner/workstream: Shopify→eBay; anchor: `86d71436534a42a742cf6f9ce723fe1b90895e12` / `34827082183`; objective: retain fail-closed UNKNOWN permission/cost/freight/fee/identity/freshness gate; acceptance: denied evidence yields no candidate and publication/network authority false; dependencies: none; safe boundary: synthetic; verification: CI; next handoff: B-EBY-02.
- security_gates: `SG-02,SG-03,SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: branch fixtures; negative_tests: missing commercial fields; receipt_evidence: evidence flags/disposition; green_required: no for synthetic; prs_required: no; owner_boundary: connector/listing; security_disposition: VERIFIED synthetic only.
### B-EBY-02 — zero-network/publication guard
- status: PENDING; owner/workstream: Shopify→eBay; anchor: B-EBY-01; objective: prove fixture path cannot invoke HTTP/SDK/listing/account mutation; acceptance: forbidden interfaces zero calls; dependencies: current branch; safe boundary: tests/static assertions; verification: CI/spies; next handoff: stop at owner boundary.
- security_gates: `SG-03,SG-05,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: tests; negative_tests: network/publish/credential attempts; receipt_evidence: zero-invocation audit; green_required: conditional; prs_required: no; owner_boundary: connector/account/listing; security_disposition: PENDING.
### B-EBY-03 — stale inventory/economics precedence
- status: PENDING; owner/workstream: Shopify→eBay; anchor: `86d714...`; objective: add stale/contradictory cases only where canonical schema supports freshness/version; acceptance: stale non-authoritative prose cannot override canonical Shopify/commercial evidence; dependencies: schema inspection; safe boundary: tests; verification: deterministic fixtures; next handoff: GlobalShopCo.
- security_gates: `SG-06,SG-07,SG-09,SG-10,SG-14`; risk_class: S2; authority_required: tests; negative_tests: stale inventory/fee/economics contradiction; receipt_evidence: source/version/time/disposition; green_required: conditional; prs_required: no; owner_boundary: listing; security_disposition: PENDING.

## Shopify→Amazon subqueue
### B-AMZ-01 — zero-listing/network receipt
- status: VERIFIED; owner/workstream: Shopify→Amazon; anchor: `25f77d9b0c21a1fc306c05807e869b6dc72beac0` / `34827128200`; objective: preserve all-green synthetic receipt with publicationAuthority=false, productionMutation=false, networkIo=false, Shopify canonical inventory; acceptance: no synthetic PASS grants listing authority; dependencies: none; safe boundary: synthetic; verification: CI; next handoff: B-AMZ-02.
- security_gates: `SG-03,SG-05,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: fixtures; negative_tests: attempted API/listing/credential path; receipt_evidence: decision receipt; green_required: no; prs_required: no; owner_boundary: seller account/listing; security_disposition: VERIFIED synthetic only.
### B-AMZ-02 — stale seller/category/GTIN evidence
- status: PENDING; owner/workstream: Shopify→Amazon; anchor: B-AMZ-01; objective: inspect schema then add freshness/version contradictions only where supported; acceptance: no invented timestamp authority; dependencies: schema; safe boundary: tests; verification: CI; next handoff: channel reconciliation.
- security_gates: `SG-06,SG-07,SG-09,SG-10,SG-14`; risk_class: S2; authority_required: tests; negative_tests: stale/future seller, GTIN contradiction, category mismatch; receipt_evidence: source/version/time; green_required: conditional; prs_required: no; owner_boundary: listing/account; security_disposition: PENDING.
### B-AMZ-03 — permission/stock identity cross-check
- status: PENDING; owner/workstream: Shopify→Amazon; anchor: GlobalShopCo #23; objective: consume exact supplier permission + Shopify variant/stock identity without upgrading UNKNOWN; acceptance: mismatch/permission-required/unknown stock=>HOLD; dependencies: B-GSC-03; safe boundary: fixtures; verification: deterministic gate; next handoff: GlobalShopCo.
- security_gates: `SG-02,SG-06,SG-10,SG-14,SG-20`; risk_class: S2; authority_required: tests; negative_tests: supplier/variant/stock mismatch; receipt_evidence: exact identities/status; green_required: conditional; prs_required: no; owner_boundary: seller/listing; security_disposition: PENDING.

## MyPrimeDelivery subqueue
### B-MPD-01 — source-rights/provider contract
- status: VERIFIED; owner/workstream: MyPrimeDelivery; anchor: `ba9d61ddd4d10a894e02a94d789d8bf26d232a5c` / `34827189247`; objective: preserve official-provider/right-to-use/provider-authority requirements; acceptance: public/editorial discovery never becomes Prime/rank/deal truth; dependencies: none; safe boundary: synthetic; verification: CI; next handoff: B-MPD-02.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: fixtures; negative_tests: public blog as ranking authority, unknown rights; receipt_evidence: source/type/date/rights; green_required: no; prs_required: no; owner_boundary: provider signup/credentials/publication; security_disposition: VERIFIED synthetic only.
### B-MPD-02 — sale freshness/expiry fixture
- status: PENDING; owner/workstream: MyPrimeDelivery; anchor: B-MPD-01; objective: encode freshness only from supported provider/deal fields; acceptance: stale/future/undated=>HOLD; dependencies: current contract; safe boundary: tests; verification: fixture matrix; next handoff: research expansion.
- security_gates: `SG-06,SG-07,SG-09,SG-10,SG-14`; risk_class: S2; authority_required: tests; negative_tests: stale/future/undated sale, unsupported Prime flag; receipt_evidence: source/time/status; green_required: conditional; prs_required: no; owner_boundary: live provider/publication; security_disposition: PENDING.
### B-MPD-03 — thin-category evidence expansion
- status: PENDING; owner/workstream: MyPrimeDelivery; anchor: 40 candidates/12 categories, QUALIFIED=0; objective: add research-only candidates in weakest categories under B-MPD-01 source classes; acceptance: no Prime/rank/deal qualification without official evidence; dependencies: source contract; safe boundary: public research/docs; verification: source/date/category receipts; next handoff: evidence validator.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: public research; negative_tests: unsupported Prime/rank/deal claim; receipt_evidence: candidate/source/date/class; green_required: no; prs_required: no; owner_boundary: provider/account/publication; security_disposition: PENDING.

# LANE C — PRODUCT / CONTENT / VENTURES
## Affiliate-Websites Master subqueue
### C-AFF-M1 — freshness denial
- status: PENDING; owner/workstream: Affiliate Master; anchor: `d901b3e...` / `34798980244`; objective: reject impossible future/stale evidence per schema; acceptance: no CTA-ready invalid evidence; dependencies: fresh scan; safe boundary: fixtures; verification: CI; next handoff: countries.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: tests; negative_tests: future/stale evidence; receipt_evidence: program/source/time; green_required: conditional; prs_required: no; owner_boundary: publication; security_disposition: PENDING.
### C-AFF-M2 — deterministic program identity/destination
- status: PENDING; owner/workstream: Affiliate Master; anchor: same baseline; objective: fail closed on duplicate/ambiguous identity/tracking; acceptance: blocked non-clickable; dependencies: schema; safe boundary: tests; verification: permutation/replay; next handoff: countries.
- security_gates: `SG-05,SG-06,SG-07,SG-09,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: tests; negative_tests: duplicate IDs/conflicting destination; receipt_evidence: IDs/hash/disposition; green_required: conditional; prs_required: no; owner_boundary: publication; security_disposition: PENDING.
### C-AFF-M3 — blocked tracking stripping
- status: PENDING; owner/workstream: Affiliate Master; anchor: same baseline; objective: ensure HOLD/BLOCKED emits no active destination/tracking; acceptance: zero active CTA; dependencies: renderer; safe boundary: tests; verification: rendered assertions; next handoff: country cases.
- security_gates: `SG-05,SG-06,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: tests; negative_tests: tracking injection/country mismatch; receipt_evidence: sanitized output; green_required: conditional; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## Affiliate AU subqueue
### C-AFF-AU1 — AU reward/referral normalization
- status: PENDING; owner/workstream: Affiliate AU; anchor: master baseline; objective: official/public AU evidence into reward/referral/country/date/quality; acceptance: missing dimension=>HOLD; dependencies: official terms; safe boundary: research/docs; verification: citations/schema; next handoff: master.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: S1; authority_required: public research; negative_tests: marketing page without terms/stale payout; receipt_evidence: source/date/fields; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: PENDING.
### C-AFF-AU2 — country/worldwide mismatch
- status: PENDING; owner/workstream: Affiliate AU; anchor: AU1; objective: deny UK/US-only or unproven worldwide CTA; acceptance: explicit AU/worldwide evidence; dependencies: AU1; safe boundary: fixtures; verification: mismatch tests; next handoff: AU3.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: tests; negative_tests: country mismatch; receipt_evidence: program/country/source; green_required: conditional; prs_required: no; owner_boundary: publication; security_disposition: PENDING.
### C-AFF-AU3 — CTA audit receipt
- status: PENDING; owner/workstream: Affiliate AU; anchor: AU1/2; objective: deterministic descriptive audit; acceptance: no publish authority; dependencies: AU1/2; safe boundary: tests; verification: deterministic hash/order; next handoff: master.
- security_gates: `SG-10,SG-11,SG-14,SG-15`; risk_class: S2; authority_required: tests; negative_tests: missing ID/country mismatch; receipt_evidence: audit record; green_required: conditional; prs_required: no; owner_boundary: live CTA; security_disposition: PENDING.

## Affiliate UK subqueue
### C-AFF-UK1 — official program/network refresh
- status: PENDING; owner/workstream: Affiliate UK; anchor: master baseline; objective: separate network availability from actual user-reward/referral eligibility; acceptance: official source/date or UNKNOWN; dependencies: public research; safe boundary: no signup/contact; verification: source matrix; next handoff: fixtures.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: S1; authority_required: public research; negative_tests: network presence=>eligibility; receipt_evidence: source/date/status; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: PENDING.
### C-AFF-UK2 — regulatory claim boundary
- status: PENDING; owner/workstream: Affiliate UK; anchor: FCA/ASA sensitivity; objective: reject unsupported guaranteed income/reward claims; acceptance: uncertain/regulated=>HOLD; dependencies: content schema; safe boundary: tests; verification: claim matrix; next handoff: Marketing.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: tests/docs; negative_tests: guaranteed income/stale rate; receipt_evidence: claim/source/disposition; green_required: conditional; prs_required: no; owner_boundary: publication/legal decision; security_disposition: PENDING.
### C-AFF-UK3 — voucher attribution abuse denial
- status: PENDING; owner/workstream: Affiliate UK; anchor: master CTA gate; objective: block unapproved voucher/tracking override; acceptance: ambiguous attribution=>no destination; dependencies: renderer; safe boundary: tests; verification: malicious fixtures; next handoff: master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: tests; negative_tests: code override/tracking injection; receipt_evidence: blocked attribution; green_required: conditional; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## Affiliate US subqueue
### C-AFF-US1 — US reward/referral normalization
- status: PENDING; owner/workstream: Affiliate US; anchor: master baseline; objective: normalize official US reward/referral evidence; acceptance: country/reward/referral/source/date exact; dependencies: official research; safe boundary: no signup; verification: schema/citations; next handoff: US2.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: S1; authority_required: public research; negative_tests: unsupported payout/worldwide; receipt_evidence: program/source/date; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: PENDING.
### C-AFF-US2 — publisher/country mismatch
- status: PENDING; owner/workstream: Affiliate US; anchor: US1; objective: deny publisher/program/country disagreement; acceptance: non-clickable HOLD; dependencies: fixtures; safe boundary: tests; verification: mismatch tests; next handoff: US3.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: tests; negative_tests: identity mismatch; receipt_evidence: identities/reason; green_required: conditional; prs_required: no; owner_boundary: publication; security_disposition: PENDING.
### C-AFF-US3 — outbound destination safety
- status: PENDING; owner/workstream: Affiliate US; anchor: master gate; objective: reject lookalike/redirect-confused destination; acceptance: only contract-approved destination survives; dependencies: parser; safe boundary: tests; verification: domain/redirect fixtures; next handoff: master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: tests; negative_tests: lookalike/redirect/tracking override; receipt_evidence: normalized destination; green_required: conditional; prs_required: no; owner_boundary: live CTA; security_disposition: PENDING.

## GhostKitchen subqueue
### C-GK-01 — batch status/source validation
- status: PENDING; owner/workstream: GhostKitchen; anchor: issue #31, baseline `ddfb2d...` / `34799531732`; objective: enforce non-authoritative status/source metadata; acceptance: promotional/empty source denied; dependencies: issue #31; safe boundary: tests/tool code; verification: CI; next handoff: GK2.
- security_gates: `SG-06,SG-07,SG-10,SG-12,SG-14`; risk_class: S2; authority_required: branch tests; negative_tests: eligibility-like status/instructional source prose; receipt_evidence: metadata/result; green_required: conditional; prs_required: no; owner_boundary: commercial selection/deploy; security_disposition: PENDING.
### C-GK-02 — unknown economics key denial
- status: PENDING; owner/workstream: GhostKitchen; anchor: GK1; objective: reject invented authority/eligibility fields; acceptance: explicit schema errors; dependencies: GK1; safe boundary: tests; verification: unknown-key fixtures; next handoff: GK3.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: S2; authority_required: tests; negative_tests: injected authority fields; receipt_evidence: schema error; green_required: conditional; prs_required: no; owner_boundary: deploy; security_disposition: PENDING.
### C-GK-03 — non-promoting economics summary
- status: PENDING; owner/workstream: GhostKitchen; anchor: GK1/2; objective: deterministic summary only from scenarios; acceptance: no commercial eligibility or filled UNKNOWNs; dependencies: GK1/2; safe boundary: artifacts/tests; verification: replay/order; next handoff: durable report.
- security_gates: `SG-07,SG-10,SG-11,SG-14`; risk_class: S2; authority_required: tests; negative_tests: all-fail/all-unknown; receipt_evidence: input/result hash; green_required: conditional; prs_required: no; owner_boundary: commercial decision; security_disposition: PENDING.

## Franchise subqueue
### C-FR-01 — tenancy-first fixture
- status: PENDING; owner/workstream: Franchise; anchor: main `29fa0546...`, PR #22 `7b8b0756...`; objective: require tenant identity before territory evidence; acceptance: missing/mismatch denies; dependencies: fresh scan; safe boundary: tests; verification: CI; next handoff: FR2.
- security_gates: `SG-03,SG-06,SG-10,SG-12,SG-14`; risk_class: S2; authority_required: tests; negative_tests: tenant/cross-tenant mismatch; receipt_evidence: tenant/territory/result; green_required: conditional; prs_required: no; owner_boundary: prod tenancy/deploy; security_disposition: PENDING.
### C-FR-02 — territory freshness/mismatch
- status: PENDING; owner/workstream: Franchise; anchor: PR #22; objective: deny stale/cross-territory only where schema supports version/time; acceptance: no invented semantics; dependencies: schema; safe boundary: tests; verification: deterministic negatives; next handoff: FR3.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: S2; authority_required: tests; negative_tests: stale/mismatch; receipt_evidence: evidence identity/version; green_required: conditional; prs_required: no; owner_boundary: territory change; security_disposition: PENDING.
### C-FR-03 — audit non-promotion
- status: PENDING; owner/workstream: Franchise; anchor: PR #22; objective: record synthetic result without live authority; acceptance: receipt explicitly non-prod; dependencies: FR1/2; safe boundary: fixtures; verification: schema/replay; next handoff: durable evidence.
- security_gates: `SG-10,SG-11,SG-14,SG-20`; risk_class: S2; authority_required: tests; negative_tests: attempted live flag; receipt_evidence: tenant/territory/source/result; green_required: conditional; prs_required: no; owner_boundary: live franchise action; security_disposition: PENDING.

## GemVerse subqueue
### C-GV-01 — recovery action/result correlation
- status: PENDING; owner/workstream: GemVerse; anchor: PR #10 `b1f09c3...` / `34803885504`; objective: exact synthetic recovery/action/result IDs; acceptance: mismatch/replay denied; dependencies: fixture schema; safe boundary: fixtures; verification: CI; next handoff: GV2.
- security_gates: `SG-09,SG-10,SG-11,SG-14`; risk_class: S2; authority_required: tests; negative_tests: mismatch/replay; receipt_evidence: lineage; green_required: conditional; prs_required: no; owner_boundary: production execution; security_disposition: PENDING.
### C-GV-02 — malformed/stale recovery denial
- status: PENDING; owner/workstream: GemVerse; anchor: PR #10; objective: reject malformed/missing and schema-supported stale evidence; acceptance: explicit FAIL/HOLD; dependencies: schema; safe boundary: tests; verification: matrix; next handoff: GV3.
- security_gates: `SG-06,SG-07,SG-09,SG-10,SG-14`; risk_class: S2; authority_required: tests; negative_tests: malformed/missing/unexpected/stale; receipt_evidence: validation/version; green_required: conditional; prs_required: no; owner_boundary: canonical runtime; security_disposition: PENDING.
### C-GV-03 — duplicate recovery idempotency
- status: PENDING; owner/workstream: GemVerse; anchor: PR #10; objective: replay cannot duplicate synthetic completion/receipt; acceptance: one accepted result; dependencies: contract; safe boundary: tests; verification: replay CI; next handoff: durable report.
- security_gates: `SG-09,SG-10,SG-11`; risk_class: S2; authority_required: tests; negative_tests: exact replay; receipt_evidence: idempotency/result count; green_required: conditional; prs_required: no; owner_boundary: production runtime; security_disposition: PENDING.

## Content360 subqueue
### C-C360-01 — mock baseline
- status: VERIFIED; owner/workstream: Content360; anchor: `8dd031bb...` / `34791442838`; objective: preserve provider-neutral mock/no-credential baseline; acceptance: non-prod only; dependencies: none; safe boundary: read-only; verification: exact run; next handoff: C360-02.
- security_gates: `SG-05,SG-06,SG-10,SG-14,SG-15`; risk_class: S0; authority_required: read-only; negative_tests: no-live baseline; receipt_evidence: head/run; green_required: no; prs_required: no; owner_boundary: credentials/live publish; security_disposition: VERIFIED.
### C-C360-02 — timeout/429/malformed provider
- status: PENDING; owner/workstream: Content360; anchor: C360-01; objective: bounded retry and zero publish on timeout/429/malformed; acceptance: explicit failure/retry ceiling; dependencies: mock; safe boundary: tests; verification: workflow; next handoff: C360-03.
- security_gates: `SG-05,SG-06,SG-09,SG-10,SG-12,SG-14`; risk_class: S2; authority_required: tests; negative_tests: timeout/429/malformed/retry ceiling; receipt_evidence: request/retry/disposition; green_required: conditional; prs_required: no; owner_boundary: credentials/publish; security_disposition: PENDING.
### C-C360-03 — prompt-injection/provenance receipt
- status: PENDING; owner/workstream: Content360; anchor: C360-01; objective: provider/content output remains data; acceptance: tool/secret/policy/publish injection cannot alter authority and secrets absent; dependencies: mock; safe boundary: fixtures; verification: adversarial tests + secret scan; next handoff: Marketing.
- security_gates: `SG-05,SG-06,SG-07,SG-09,SG-10,SG-11,SG-14,SG-15`; risk_class: S2; authority_required: tests; negative_tests: tool/policy/secret/publish injection, replay; receipt_evidence: request/content/result hashes; green_required: yes if promoted; prs_required: conditional; owner_boundary: credentials/publication; security_disposition: PENDING.

## Commercial Frontend subqueue
### C-CF-01 — direct operator-evidence extraction
- status: PENDING; owner/workstream: Commercial Frontend; anchor: `55b189f...`, issue #21 comment `5659574435`; objective: classify available operator evidence for pain/frequency/time/trial/WTP; acceptance: source/evidence class per row; dependencies: existing evidence; safe boundary: no outreach; verification: trace; next handoff: CF2 or OWNER_REQUIRED.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-20`; risk_class: S1; authority_required: read-only; negative_tests: platform docs=>demand; receipt_evidence: source/persona/metric; green_required: no; prs_required: no; owner_boundary: outreach; security_disposition: PENDING.
### C-CF-02 — ecommerce exception fixtures
- status: PENDING; owner/workstream: Commercial Frontend; anchor: same report; objective: supplier-stock/ETA/order-change exceptions with approval boundaries; acceptance: source/stale/request/approval/audit fields; dependencies: taxonomy; safe boundary: fixtures; verification: schema/replay; next handoff: prototype.
- security_gates: `SG-06,SG-10,SG-12,SG-14,SG-15`; risk_class: S2; authority_required: tests; negative_tests: stale/cross-order/unauthorized approval; receipt_evidence: exception/source/decision; green_required: conditional; prs_required: no; owner_boundary: production order mutation; security_disposition: PENDING.
### C-CF-03 — demand-boundary disposition
- status: PENDING; owner/workstream: Commercial Frontend; anchor: feasibility VERIFIED, WTP UNKNOWN; objective: classify AVAILABLE_EVIDENCE vs OUTREACH_REQUIRED; acceptance: no fabricated intent/WTP; dependencies: CF1; safe boundary: report; verification: source/blocker each row; next handoff: owner if outreach needed.
- security_gates: `SG-06,SG-10,SG-15,SG-20`; risk_class: S1; authority_required: synthesis; negative_tests: inferred WTP; receipt_evidence: row/source/blocker; green_required: no; prs_required: no; owner_boundary: outreach; security_disposition: PENDING.

## Marketing / brand integration subqueue
### C-MKT-01 — Founding Beta truth/measurement contract
- status: PENDING; owner/workstream: Marketing; anchor: PR #104 `83a58b8...`; beta event matrix `206337090d5577be94284732fe345990c08a22e6`; frontend claim delta `3539dc59f499167b434857f0f4ccd135bea2c5a1`; objective: map claims/metrics to PROVEN/DEMO_ONLY/PLANNED/HOLD; acceptance: no Level2/PRS/recovery/privacy overclaim; dependencies: exact runtime/frontend evidence; safe boundary: docs/content; verification: contradiction scan; next handoff: frontend/marketing copy.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: non-prod docs; negative_tests: Level2/PRS/autonomy/privacy overclaim; receipt_evidence: claim/metric/source/state; green_required: no; prs_required: no; owner_boundary: public beta/campaign; security_disposition: PENDING.
### C-MKT-02 — Operator integration/brand shortlist readiness
- status: PENDING; owner/workstream: Marketing/Operator integrations; anchor: capability/MCP trust comparison `1585942475eb00d97d302941eadc8953642978e4`; objective: first-wave shortlist with official marketplace/install path, auth, free/paid boundary, evidence date, AgentOS ownership boundary and readiness; acceptance: RESEARCH_READY/MOCK_READY/OWNER_SETUP_REQUIRED/BLOCKED only; dependencies: official evidence; safe boundary: research, no install/account/credential/spend; verification: dated official sources + architecture fit; next handoff: AgentOS capability backlog after canonical gates.
- security_gates: `SG-02,SG-03,SG-05,SG-06,SG-10,SG-14,SG-20`; risk_class: S1; authority_required: public research; negative_tests: provider self-authority, credential-in-doc, marketplace=>production-ready inference; receipt_evidence: provider/source/date/readiness/boundary; green_required: no; prs_required: no; owner_boundary: install/credentials/spend; security_disposition: PENDING.
### C-MKT-03 — commerce/channel claim boundary
- status: PENDING; owner/workstream: Marketing commerce; anchor: 0 eBay-ready SKUs; eBay `86d714...`; Amazon `25f77d9...`; MyPrime `ba9d61d...`; permission-first supplier screen `12b14b162d07e22f5d52158747e73d5690d13bff`; objective: keep channel/Prime/stock/delivery claims aligned to evidence; acceptance: no readiness/income/Prime/price claim beyond evidence; dependencies: Lane B; safe boundary: content matrix only; verification: contradiction scan; next handoff: Content360 non-prod optimization.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: synthesis; negative_tests: eBay/Amazon/Prime/stock/income overclaim; receipt_evidence: claim→anchor; green_required: no; prs_required: no; owner_boundary: campaign/publication; security_disposition: PENDING.

# RECONCILIATION — 2026-09-14 19:30 BRISBANE
- **LANE A:** PR #104 remains exact `83a58b8...`, OPEN/DRAFT/UNMERGED. Exact-head push Tests `34821384346` is SUCCESS on Ubuntu and Windows+audit; cancelled PR run remains separately CANCELLED. A-AG-02 is VERIFIED for CI accounting and A-AG-04 for regression-preservation only, but security remains BLOCKED because SG-01/02 canonical authenticated admission and SG-08 continuous ownership are unresolved. PRS `0defebe...` / `34821646371` still reproduces both stale-owner false-success cases. No current-head Jess Green→PRS promotion evidence.
- **LANE B:** eBay B-EBY-01 advanced to `86d714...` / `34827082183` SUCCESS and is VERIFIED synthetic commercial-ingest only; Amazon B-AMZ-01 advanced to `25f77d9...` / `34827128200` SUCCESS and is VERIFIED zero-authority synthetic receipt only; MyPrime B-MPD-01 advanced to `ba9d61d...` / `34827189247` SUCCESS and is VERIFIED source-rights synthetic only. Real commerce remains HOLD: 0 evidence-complete eBay-ready SKUs; authorised Prime/rank/deal provider UNKNOWN; supplier trade cost/freight/fulfilment identity/account fees/economics remain incomplete. Headless live browser/dev-store proof remains BLOCKED.
- **LANE C:** no new exact implementation evidence promotes Affiliate/GhostKitchen/Franchise/GemVerse/Content360/Commercial Frontend. Their verified baselines are retained and multiple homogeneous PENDING items remain. Marketing/frontend evidence advanced: PR #111 `b14c5d81...` / `34827244536` SUCCESS for bounded read-only evidence projection; beta/claim/supply-chain/supplier/SEO artifacts are evidence-layer only and do not change runtime readiness or public authority.
- **Security:** canonical matrix applies cross-cutting only. Missing authority, ownership, permission, credentials, external/physical-host or production evidence remains BLOCKED/UNKNOWN. Functional PASS never upgrades security and security PASS never upgrades functional status.
- Every active scheduled workstream has actionable PENDING work or an explicit blocker. Scheduler firing was not treated as completion. **No overall GREEN.**

# NEXT EXECUTION EMPHASIS
1. Lane A: real SG-08 ownership primitive remains single-threaded technical P0; separately identify canonical SG-01/02 sources; consume A-AG-05 read-only evidence seam without inventing recovery/PRS state.
2. Lane B: execute zero-network eBay guard, Amazon schema-supported freshness cases, MyPrime freshness, and one compact exact-SKU economics/permission packet; do not wait on blocked Headless live proof.
3. Lane C: consume homogeneous country affiliate evidence/negative fixtures, then GhostKitchen/Franchise/GemVerse/Content360/Commercial Frontend mini-batches; Marketing keeps Founding Beta HOLD and advances Operator shortlist only by official evidence.
