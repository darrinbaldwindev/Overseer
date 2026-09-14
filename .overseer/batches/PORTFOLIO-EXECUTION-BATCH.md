# Portfolio Execution Batch Manifest

**Purpose:** queue state only for the fixed scheduled portfolio lanes. Canonical procedure: `.overseer/doctrine/PORTFOLIO-BATCH-ENGINE.md`. Project shaping: `.overseer/profiles/PROJECT-BATCH-PROFILES.md`. Security: `.overseer/security/AGENTOS-SECURITY-GATE-MATRIX.md`. Repository/runtime/CI evidence outranks this file.

**Fixed lanes:** A = AgentOS Level 2 P0 + PRS/Green assurance-adjacent work; B = GlobalShopCo/Headless/eBay/Amazon/MyPrimeDelivery; C = Affiliate-Websites AU/UK/US/Master, GhostKitchen, Franchise, GemVerse, Content360, Commercial Frontend, Marketing.

**States:** `PENDING | ACTIVE | VERIFIED | BLOCKED | STALE | SPLIT_REQUIRED`.

**Core invariant:** **NO MODEL DECIDES ITS OWN AUTHORITY.** Functional state, security state and PRS state remain separate. No merge/approve/ready/rebase/deploy/credentials/security-policy changes/production writes/purchases/spend/supplier contact/live publication/physical owner-host action/production autonomy.

## Checkpoint reconciliation — 2026-09-15 04:30 Brisbane
- Previous durable checkpoint: Overseer #49 `5668096534`; previous manifest commit `793c48293f7ccd45e552e1da396cd0106f630428` / blob `2fe71ef60234f9d21fedc08a3af51f8e42d09c14`.
- Canonical engine, central profiles, current manifest, security matrix and post-checkpoint #49 evidence were re-read first. Queue text remained hypothesis only.
- **AgentOS PR #104:** exact OPEN/DRAFT head advanced to `86b08c400de2a551c3473f443e389bb0adf53546`; exact-head AgentOS Tests `34878041375` completed SUCCESS. A-AG-06 bounded read-only receipt-provenance projection is functionally VERIFIED on that exact head only. SG-08 continuous ownership and SG-01/02 authenticated actor/canonical grant remain BLOCKED; exact-head CI does not promote them.
- **Independent Green/security correction:** prior A-AG-05 wording was too broad. Current exact evidence supports required canonical mission/task/wake IDs plus duplicate durable receipt-ID first-write provenance. Cross-task/cross-mission/cross-wake mismatch, stale/replay semantics and direct-adapter malformed-receipt bypass are not fully evidenced and are split back to PENDING/SPLIT_REQUIRED below. SG-09/10/11 are therefore only bounded, not complete.
- **Basic Chat PR #111:** exact `352c83fdbcff65dd9dc592fb3b8d65d4aa130969` / Tests `34863648579` SUCCESS remains bounded read-only lifecycle/readiness evidence. Physical Windows and mutation safety remain separate.
- **GlobalShopCo:** exact `agent/overseer/initial-project-timeline@79d50227fe19826d42c43e7dec15ce245ad58e40`; PR #29/#30 remain active data/source qualification; `0 eBay-ready SKUs` remains controlling. Missing authenticated trade cost/freight/permission/stock/economics remains HOLD/UNKNOWN.
- **MyPrimeDelivery:** exact head advanced to `61feceb46de539948374deec86b3fe7578cf8014`; Fixture Validation `34879834476` SUCCESS. Multiple distinct known ASINs under one normalized-title concept now fail closed even when one observation is otherwise complete. This is VERIFIED synthetic/non-production only. Live qualified count remains `0`; live Prime/rank/rights/outbound/publication authority remains UNKNOWN/HOLD.
- **GlobalShopCo-Headless:** deterministic contract work remains bounded; real non-production dev-store/browser Shopify checkout handoff remains the meaningful proof gap.
- **shopify_ebay:** existing synthetic gate/replay lineage remains non-production only. Real SKU/network/publication authority remains HOLD. Next work is inspection of existing durable replay/idempotency/correlation state before any persistence change.
- **Shopify→Amazon:** existing channel-fixture success remains synthetic only; seller identity, permission, exact Shopify variant/stock, category/GTIN, fulfilment, fees/economics and freshness remain independently fail-closed.
- **Content360:** PR #4 remains exact `dd9bb49f09d4f67bf055e5418afb4a6bc55eff09`; no newer exact-head CI evidence was established in this reconciliation, so provider/provenance work remains ACTIVE/CI-PENDING and live network/PUBLISH/SCHEDULE/account actions remain owner-gated.
- **Lane C active ownership preserved:** Affiliate main `d3cf400aabe631dc6c2e37193eca8b192856eaba` with active PR #17/#19 and US PR #6; GhostKitchen `main@dbd64153ca3f2b0e7e9152955692f62f6c9fa59a` with PR #32; Franchise `main@0ea3b26de71f78f7eafc38cf50079805b43a7d93` with PR #24/#22; GemVerse `gemverse@b36750f01f62184e2f563ff8f8030682ba10033e` with PR #10. No duplicate implementation is assigned.

# LANE A — AgentOS Level 2 P0

## AgentOS Overseer subqueue

### A-AG-01 — continuous project-file ownership fence
- status: BLOCKED; owner/workstream: AgentOS / writer ownership; anchor: `darrinbaldwindev/AgentOS` PR #104 `86b08c400de2a551c3473f443e389bb0adf53546`, CI `34878041375` SUCCESS, historical PRS stale-owner baseline `0defebe26f71e1cf5df1168fa5454bfd8de30091` / `34821646371`; objective: one crash-releasing kernel-enforced fence held continuously final verification -> publish/prepared recovery -> durable success receipt -> release; acceptance: replacement-after-verify, successor/three-writer, stale identity, TOCTOU, crash/replay, duplicate mutation/result, prepared-recovery stale-owner all fail closed; dependencies: real writer implementation; safe boundary: draft non-production code/tests; verification: adversarial ownership matrix + exact Ubuntu/Windows CI; next handoff: identical head to Green, then PRS only after Green PASS.
- security_gates: `SG-03,SG-08,SG-09,SG-10,SG-11,SG-14,SG-18,SG-19`; risk_class: S2; authority_required: scoped branch/test write; negative_tests: full ownership matrix; receipt_evidence: actor/task/file/pre-postimage/ownership/result lineage; green_required: yes; prs_required: yes; owner_boundary: merge/deploy/physical production; security_disposition: BLOCKED.

### A-AG-02 — authenticated actor + canonical grant binding
- status: BLOCKED; owner/workstream: AgentOS / authority admission; anchor: PR #104 `86b08c400...` + existing caller-supplied authority seam; objective: bind a real existing authenticated actor source and canonical grant resolver without a second authority registry; acceptance: payload/host cannot self-supply identity/grant; absent/spoofed/mismatched/cross-project/replayed grant yields no admitted artifact/success receipt; dependencies: real bindable canonical source; safe boundary: architecture discovery + bounded tests; verification: spoof/mismatch/replay matrix; next handoff: implementation only when existing source is evidenced.
- security_gates: `SG-01,SG-02,SG-03,SG-04,SG-09,SG-10,SG-11,SG-18,SG-19`; risk_class: S2; authority_required: canonical identity/grant read + scoped tests; negative_tests: host-as-auth, spoof actor, payload self-grant, absent/mismatch/cross-project/replay; receipt_evidence: issuer/source/version/request/task/mission; green_required: yes; prs_required: yes; owner_boundary: credentials/security policy; security_disposition: BLOCKED.

### A-AG-03 — Basic Chat lifecycle/readiness projection
- status: VERIFIED; owner/workstream: AgentOS / Basic Chat; anchor: PR #111 `352c83fdbcff65dd9dc592fb3b8d65d4aa130969`, Tests `34863648579` SUCCESS; objective: preserve truthful read-only lifecycle/readiness projection; acceptance: no fabricated mutation readiness, raw/secret/PRS/recovery leakage, or stale physical head promotion; dependencies: none; safe boundary: tests/small projection fixes; verification: exact-head CI + read-only negative sample; next handoff: A-PRS-03 bounded Green sample.
- security_gates: `SG-03,SG-05,SG-10,SG-14,SG-18`; risk_class: S1; authority_required: scoped branch tests; negative_tests: fabricated readiness, stale physical head, mission/wake conflict, evidence leakage; receipt_evidence: exact head/run/test names; green_required: yes before promotion; prs_required: conditional; owner_boundary: merge/deploy/runtime enablement; security_disposition: PASS_BOUNDED.

### A-AG-04 — authority-evidence receipt persistence/reload
- status: VERIFIED; owner/workstream: AgentOS / receipt provenance; anchor: PR #104 current `86b08c400...` with prior source-backed authority-evidence lineage; objective: preserve exact `authority_evidence_id` through receipt persistence/reload without broadening authority; acceptance: admitted receipt cannot silently lose/null/replace its source-backed ID; dependencies: existing receipt schema; safe boundary: tests/small compatible fix; verification: reload/recovery fixtures + exact-head CI; next handoff: regression dependency for A-AG-05/A-AG-06.
- security_gates: `SG-02,SG-09,SG-10,SG-11,SG-14,SG-18`; risk_class: S2; authority_required: scoped branch tests; negative_tests: missing/null/empty/cross-task authority evidence; receipt_evidence: authority evidence ID + request/task/result/receipt lineage; green_required: yes for promotion; prs_required: conditional; owner_boundary: merge/deploy; security_disposition: PENDING_SG18.

### A-AG-05A — canonical required correlation + duplicate provenance
- status: VERIFIED; owner/workstream: AgentOS / receipt correlation; anchor: PR #104 substantive receipt-correlation lineage carried to exact `86b08c400...`, CI `34878041375` SUCCESS; objective: retain only the exact evidence actually proved; acceptance: missing/blank canonical mission/task/wake is rejected before persistence, complete canonical receipt persists, duplicate durable receipt ID cannot replace first provenance; dependencies: existing constructor; safe boundary: tests/minimal compatible fix; verification: exact committed negatives + exact-head CI; next handoff: preserve as regression baseline.
- security_gates: `SG-10,SG-11,SG-14,SG-18`; risk_class: S1; authority_required: scoped tests; negative_tests: blank required IDs, duplicate durable receipt ID; receipt_evidence: immutable IDs/provenance/disposition; green_required: yes if promoted; prs_required: conditional; owner_boundary: merge/deploy; security_disposition: PASS_BOUNDED.

### A-AG-05B — mismatch/replay/direct-adapter correlation closure
- status: SPLIT_REQUIRED; owner/workstream: AgentOS / receipt correlation; anchor: Green/security checkpoint `Overseer#49/5668150671` against PR #104 current lineage; objective: close the scope previously overstated by A-AG-05 without creating new persistence/authority layers; acceptance: every production-path caller reaches canonical construction or equivalent existing boundary validation; direct malformed receipt attempts and cross-task/cross-mission/cross-wake mismatch cannot persist success; stale/freshness semantics are implemented only if a canonical source exists, otherwise explicitly UNKNOWN/N/A; restart/reload preserves duplicate-ID first-write provenance; dependencies: A-AG-05A + existing persistence seam; safe boundary: tests/minimal validator at existing boundary; verification: exact-head CI + direct-adapter/mismatch/restart negatives; next handoff: Green SG-09/10/11 sample.
- security_gates: `SG-09,SG-10,SG-11,SG-14,SG-18`; risk_class: S2; authority_required: scoped branch/test write; negative_tests: direct malformed receipt, cross-task/mission/wake mismatch, replay, stale only if canonical freshness exists, restart/reload duplicate; receipt_evidence: authoritative task/mission/wake + receipt IDs + first-write provenance; green_required: yes; prs_required: conditional; owner_boundary: no new persistence/authority plane, merge/deploy; security_disposition: SPLIT_REQUIRED.

### A-AG-06 — bounded receipt provenance evidence projection
- status: VERIFIED; owner/workstream: AgentOS / evidence closure; anchor: PR #104 `86b08c400de2a551c3473f443e389bb0adf53546`, AgentOS Tests `34878041375` SUCCESS; objective: expose existing receipt provenance through a bounded read-only projection; acceptance: exact tuple limited to receipt/delivery/request/mission/task/wake/host/worker/status/code-identity/authority-evidence identity; non-whitelisted secret-shaped fields excluded; missing receipt and malformed durable mission correlation fail closed; dependencies: existing persistence adapter only; safe boundary: read-only projection/tests; verification: exact-head CI + projection negatives; next handoff: Green/SABLE evidence consumer, not authority promotion.
- security_gates: `SG-05,SG-09,SG-10,SG-11,SG-14,SG-18`; risk_class: S1; authority_required: scoped branch/test write; negative_tests: missing receipt, malformed mission correlation, secret-shaped field, unknown field; receipt_evidence: exact head/run/projection tuple; green_required: yes if used for promotion; prs_required: conditional; owner_boundary: no new evidence authority, merge/deploy; security_disposition: PENDING_SG18.

### A-AG-07 — physical Windows acceptance packet
- status: BLOCKED; owner/workstream: AgentOS / physical host; anchor: PR #104 `86b08c400...` with A-AG-01/A-AG-02 unresolved; objective: retain owner-run physical acceptance packet for later; acceptance: exact SHA/root/mutation/recovery/correlation/no-production boundary; dependencies: SG-08 + SG-01/02 + explicit owner physical authority; safe boundary: checklist only; verification: future physical-host evidence; next handoff: owner after software/security closure.
- security_gates: `SG-03,SG-08,SG-10,SG-11,SG-14,SG-18,SG-20`; risk_class: S2; authority_required: owner-authorized physical Windows action; negative_tests: wrong head, production root, missing receipt; receipt_evidence: head/host/root/test/result; green_required: yes; prs_required: yes if promoted; owner_boundary: physical Windows execution; security_disposition: BLOCKED.

## PRS / Green assurance subqueue

### A-PRS-01 — immutable stale-owner false-GREEN baseline
- status: VERIFIED; owner/workstream: PRS; anchor: historical `0defebe26f71e1cf5df1168fa5454bfd8de30091` / `34821646371`; objective: preserve exact stale-owner defect baseline without inheritance; acceptance: target/artifact identity immutable; dependencies: none; safe boundary: read-only; verification: hashes; next handoff: A-AG-01.
- security_gates: `SG-08,SG-10,SG-11,SG-19`; risk_class: S0; authority_required: read-only; negative_tests: normal + prepared recovery stale-owner; receipt_evidence: exact target/artifact hashes; green_required: no; prs_required: baseline; owner_boundary: none; security_disposition: VERIFIED.

### A-PRS-02 — exact-head ownership challenge
- status: BLOCKED; owner/workstream: PRS; anchor: AgentOS PR #104 `86b08c400...` + A-PRS-01; objective: rerun ownership matrix only after real A-AG-01 repair and identical-head Green PASS; acceptance: normal/prepared/successor/crash/replay independently classified; dependencies: A-AG-01 + exact CI + Green; safe boundary: assurance harness; verification: immutable target/artifact hashes; next handoff: Overseer.
- security_gates: `SG-08,SG-09,SG-10,SG-11,SG-19`; risk_class: S2; authority_required: bounded harness; negative_tests: full ownership matrix; receipt_evidence: exact target/artifact hash; green_required: yes prerequisite; prs_required: yes; owner_boundary: merge/deploy; security_disposition: BLOCKED.

### A-PRS-03 — frontend + receipt false-GREEN sample
- status: PENDING; owner/workstream: Green first / PRS conditional; anchor: PR #111 `352c83fd...` / `34863648579` plus PR #104 `86b08c400...`; objective: independently sample fabricated readiness/leakage and A-AG-05A/A-AG-06 wrong-lineage success without entering blocked ownership/admission scope; acceptance: no false readiness, wrong-lineage success, or secret/raw evidence leak; dependencies: immutable exact heads; safe boundary: read/test only; verification: independent negatives; next handoff: AgentOS Overseer.
- security_gates: `SG-05,SG-10,SG-11,SG-18,SG-19`; risk_class: S1; authority_required: read/test only; negative_tests: fabricated readiness, stale lineage, malformed projection, leakage; receipt_evidence: exact target/run/test outcome; green_required: yes; prs_required: conditional; owner_boundary: merge/deploy; security_disposition: PENDING.

# LANE B — Commerce

## GlobalShopCo subqueue

### B-GSC-01 — exact product evidence consumption
- status: ACTIVE; owner/workstream: GlobalShopCo qualification; anchor: `darrinbaldwindev/GlobalShopCo` `agent/overseer/initial-project-timeline@79d50227fe19826d42c43e7dec15ce245ad58e40`, active PR #29/#30, `0 eBay-ready SKUs`; objective: reconcile exact SKU/GTIN, buy-cost class, freight, permission, stock/fulfilment, AU/eBay comps, returns/warranty; acceptance: each row PROMOTE/REJECT/HOLD with every material missing field explicit; dependencies: active PR ownership; safe boundary: research/docs/calculation; verification: source/date/identity/economics table; next handoff: channel gates.
- security_gates: `SG-02,SG-03,SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public/read-only evidence; negative_tests: missing freight/permission/stock/seller/fee => HOLD; receipt_evidence: exact source/date/SKU/cost/freight/fee table; green_required: no for research; prs_required: no; owner_boundary: supplier contact/purchase/Shopify mutation/publication/spend; security_disposition: ACTIVE.

### B-GSC-02 — delivered-cost/free-delivery sensitivity mini-batch
- status: PENDING; owner/workstream: GlobalShopCo economics; anchor: same PR #29/#30 evidence set + current free-delivery policy; objective: compute landed/free-delivery sensitivity only for rows with evidence-complete inputs; acceptance: low/base/high freight and fee allowance shown; any margin dependent on UNKNOWN freight rejected/HOLD; dependencies: B-GSC-01 source completeness; safe boundary: offline calculations; verification: reproducible worksheet/formula; next handoff: eBay/Amazon readiness comparison.
- security_gates: `SG-06,SG-10,SG-12,SG-13,SG-14,SG-20`; risk_class: S0; authority_required: read/calculation only; negative_tests: missing freight, stale comp, unknown fee => no PROMOTE; receipt_evidence: source/date/formula/result; green_required: no; prs_required: no; owner_boundary: spend/contact; security_disposition: PENDING.

### B-GSC-03 — replacement candidate evidence tranche
- status: PENDING; owner/workstream: GlobalShopCo sourcing research; anchor: current GSC source table at `79d50227...`; objective: add 2–5 homogeneous compact AU-stock candidates only where exact identity and delivered-cost evidence can be captured without contact; acceptance: every candidate has exact supplier SKU/model, public price or explicit UNKNOWN, freight evidence or HOLD, realistic delivered market comp, permission status and returns/warranty status; dependencies: none; safe boundary: public research only; verification: primary/public source citations + date; next handoff: B-GSC-01.
- security_gates: `SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research; negative_tests: inferred wholesale/permission/stock forbidden; receipt_evidence: exact URLs/date/identity table; green_required: no; prs_required: no; owner_boundary: supplier contact/purchase; security_disposition: PENDING.

## GlobalShopCo-Headless subqueue

### B-HDL-01 — deterministic product identity contract regression
- status: PENDING; owner/workstream: Headless / Shopify projection; anchor: current Headless documented/hardening lineage under `darrinbaldwindev/GlobalShopCo-Headless`; objective: preserve exact Shopify product/variant identity and canonical checkout host; acceptance: malformed/missing/stale IDs fail closed and no alternate catalogue authority is created; dependencies: existing fixtures; safe boundary: tests/docs; verification: exact fixture tests; next handoff: B-HDL-02.
- security_gates: `SG-03,SG-05,SG-06,SG-09,SG-10,SG-14,SG-20`; risk_class: S1; authority_required: scoped tests; negative_tests: wrong variant, stale availability, malformed checkout destination; receipt_evidence: exact fixture/input/output; green_required: conditional; prs_required: no; owner_boundary: deployment/secrets/live purchase; security_disposition: PENDING.

### B-HDL-02 — non-production checkout handoff packet
- status: BLOCKED; owner/workstream: Headless / browser handoff; anchor: current Headless lineage + Commerce checkpoint `Overseer#49/5668603831`; objective: prove one dev/non-production product retrieval -> render -> Shopify checkout handoff with Shopify authoritative; acceptance: browser-visible destination is approved Shopify host, identity conserved, no live purchase; dependencies: safe dev-store/browser evidence and qualified fixture; safe boundary: non-production browser/read-only; verification: captured request/destination/variant evidence; next handoff: Headless Overseer.
- security_gates: `SG-03,SG-05,SG-06,SG-10,SG-14,SG-20`; risk_class: S1; authority_required: non-production browser/read; negative_tests: hostile destination, missing variant, live purchase path; receipt_evidence: exact environment/product/URL/result; green_required: conditional; prs_required: no; owner_boundary: deployment/secrets/live purchase; security_disposition: BLOCKED_EXTERNAL_EVIDENCE.

### B-HDL-03 — server credential boundary negative tranche
- status: PENDING; owner/workstream: Headless / credential isolation; anchor: current headless server boundary; objective: prove storefront/client cannot expose or override server-side secret handles; acceptance: client bundle/log fixture contains no plaintext secret and malformed external content cannot request secret disclosure; dependencies: existing testable server boundary; safe boundary: static/tests only; verification: bundle/log/fixture scan; next handoff: Headless security sample.
- security_gates: `SG-05,SG-06,SG-14`; risk_class: S1; authority_required: read/test only; negative_tests: secret-shaped fixture, prompt-injection request, client override; receipt_evidence: scan/test outputs; green_required: conditional; prs_required: no; owner_boundary: credentials/deploy; security_disposition: PENDING.

## Shopify to eBay subqueue

### B-EBY-01 — existing replay/idempotency state inspection
- status: PENDING; owner/workstream: Shopify→eBay; anchor: `darrinbaldwindev/shopify_ebay` existing synthetic gate/replay lineage referenced by Commerce checkpoint `5668603831`; objective: map existing durable state/correlation before any persistence change; acceptance: exact state keys, first-write semantics, restart behavior and network/publication=false boundary documented from code/tests; dependencies: none; safe boundary: read/test only; verification: source paths + exact fixture outcomes; next handoff: B-EBY-02 only if a gap is evidenced.
- security_gates: `SG-03,SG-05,SG-09,SG-10,SG-11,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: repo read/test; negative_tests: replay, duplicate mapping, stale correlation, network/publication assertion; receipt_evidence: exact code/test/state-key map; green_required: conditional; prs_required: no; owner_boundary: credentials/network/listing publication; security_disposition: PENDING.

### B-EBY-02 — bounded durable replay negatives
- status: PENDING; owner/workstream: Shopify→eBay; anchor: B-EBY-01 identified existing seam only; objective: add 2–5 homogeneous negatives for duplicate event/mapping/result, stale correlation and restart without adding a second state plane; acceptance: duplicate/replayed input cannot produce second durable side effect/success mapping; dependencies: B-EBY-01; safe boundary: synthetic tests/minimal compatible fix; verification: exact-head CI; next handoff: channel gate.
- security_gates: `SG-09,SG-10,SG-11,SG-14,SG-15`; risk_class: S2; authority_required: scoped branch/tests; negative_tests: duplicate event/mapping/result, stale correlation, restart; receipt_evidence: idempotency key/mapping/receipt lineage; green_required: yes if implementation changes; prs_required: conditional; owner_boundary: network/publication/merge/deploy; security_disposition: PENDING.

### B-EBY-03 — real SKU readiness remains hold
- status: BLOCKED; owner/workstream: Shopify→eBay commercial readiness; anchor: GlobalShopCo `79d50227...`, `0 eBay-ready SKUs`; objective: consume only evidence-cleared Shopify/supplier facts; acceptance: exact variant/SKU, permission, stock, landed economics, fees, fulfilment/seller identity all evidenced on same candidate; dependencies: B-GSC-01/02; safe boundary: read/research; verification: complete readiness row; next handoff: owner decision only after evidence complete.
- security_gates: `SG-02,SG-03,SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read-only; negative_tests: any missing material field => HOLD; receipt_evidence: exact source/date/readiness row; green_required: no; prs_required: no; owner_boundary: listing/app/install/production write/spend; security_disposition: BLOCKED_EVIDENCE.

## Shopify to Amazon subqueue

### B-AMZ-01 — contradiction/freshness negatives
- status: PENDING; owner/workstream: GlobalShopCo / Amazon fixtures; anchor: existing GlobalShopCo Amazon channel-fixture success referenced in `5668603831`; objective: challenge contradictory seller/permission/variant/stock/category/GTIN/fulfilment/fee evidence and stale source timestamps; acceptance: contradiction or stale mandatory evidence cannot promote readiness; dependencies: existing schema; safe boundary: synthetic tests only; verification: exact fixture output; next handoff: B-AMZ-02.
- security_gates: `SG-02,SG-03,SG-06,SG-10,SG-12,SG-14,SG-15,SG-20`; risk_class: S0; authority_required: test only; negative_tests: conflict/stale/missing mandatory evidence; receipt_evidence: fixture/input/outcome; green_required: no; prs_required: no; owner_boundary: seller setup/listing/network; security_disposition: PENDING.

### B-AMZ-02 — cross-record evidence composition denial
- status: PENDING; owner/workstream: Amazon fixtures; anchor: MyPrime coherent-observation/identity-conflict lessons + existing Amazon schema; objective: ensure evidence from distinct variants/sellers/observations cannot compose into one stronger readiness claim; acceptance: one coherent admissible evidence unit is required for promoted claim; dependencies: schema supports identity correlation; safe boundary: synthetic tests; verification: mixed-record negative fixture; next handoff: channel gate.
- security_gates: `SG-06,SG-10,SG-11,SG-14`; risk_class: S0; authority_required: test only; negative_tests: cross-variant, cross-seller, cross-observation composition; receipt_evidence: evidence-unit IDs/outcome; green_required: no; prs_required: no; owner_boundary: production/listing; security_disposition: PENDING.

### B-AMZ-03 — live seller/readiness hold
- status: BLOCKED; owner/workstream: Amazon live readiness; anchor: Commerce checkpoint `5668603831`; objective: keep seller identity, permission, exact Shopify stock/variant, GTIN/category, fulfilment and fees/economics explicit until real evidence exists; acceptance: no synthetic fixture treated as live readiness; dependencies: external owner/account evidence; safe boundary: documentation only; verification: evidence checklist; next handoff: owner if/when seller/account evidence is authorized.
- security_gates: `SG-02,SG-03,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S3; authority_required: owner/account evidence; negative_tests: synthetic-to-live promotion; receipt_evidence: authoritative account/evidence IDs; green_required: yes before production; prs_required: conditional; owner_boundary: seller setup/credentials/listing; security_disposition: BLOCKED_OWNER_REQUIRED.

## MyPrimeDelivery subqueue

### B-MPD-01 — coherent-observation qualification invariant
- status: VERIFIED; owner/workstream: MyPrimeDelivery; anchor: predecessor `ae69e8da54e00b0af1d6ca042360b8003016d2d9`, Fixture Validation `34873679401` SUCCESS; objective: require one observation to satisfy identity + Prime + freshness + rank + source-rights + outbound gates; acceptance: partial evidence across observations cannot compose QUALIFIED; dependencies: none; safe boundary: synthetic; verification: exact fixture run; next handoff: regression baseline.
- security_gates: `SG-02,SG-03,SG-06,SG-10,SG-12,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: scoped test branch; negative_tests: cross-observation composition; receipt_evidence: exact head/run/fixture counts; green_required: conditional; prs_required: no; owner_boundary: provider signup/credentials/publication; security_disposition: PASS_BOUNDED.

### B-MPD-02 — multi-ASIN identity ambiguity denial
- status: VERIFIED; owner/workstream: MyPrimeDelivery identity; anchor: exact `61feceb46de539948374deec86b3fe7578cf8014`, Fixture Validation `34879834476` SUCCESS, MyPrimeDelivery#2 `5668596008`; objective: fail closed when one normalized-title concept carries >1 distinct known ASIN; acceptance: `B000TEST04` + `B000TEST05` yields identity conflict, zero qualified, publication=false, network_io=false; dependencies: none; safe boundary: synthetic; verification: exact-head fixture; next handoff: preserve as anti-fail-open regression.
- security_gates: `SG-02,SG-03,SG-05,SG-06,SG-10,SG-12,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: scoped branch/tests; negative_tests: multiple ASINs same normalized concept; receipt_evidence: exact head/run/counts; green_required: conditional; prs_required: no; owner_boundary: provider/account/publication; security_disposition: PASS_BOUNDED.

### B-MPD-03 — authorised exact identity evidence intake
- status: PENDING; owner/workstream: MyPrimeDelivery evidence; anchor: exact `61feceb46...`, live qualified count `0`; objective: validate 2–5 candidate concepts only where exact identity/ASIN evidence is authorised and source-rights are explicit; acceptance: public/editorial pages never become Prime/rank authority; absent ASIN/Prime/rank/rights/outbound remains HOLD; dependencies: authorised source evidence; safe boundary: read-only evidence normalization; verification: source/date/provenance table; next handoff: qualification funnel.
- security_gates: `SG-02,SG-03,SG-05,SG-06,SG-10,SG-12,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read-only authorised source; negative_tests: editorial-as-authority, ambiguous ASIN, stale rank, missing rights; receipt_evidence: source/date/identity/rights tuple; green_required: no for research; prs_required: no; owner_boundary: provider signup/credentials/live publication; security_disposition: PENDING.

### B-MPD-04 — WordPress presentation fail-closed fixture
- status: PENDING; owner/workstream: MyPrimeDelivery presentation; anchor: exact `61feceb46...` + profile requirement; objective: render HOLD/UNKNOWN/QUALIFIED states without inventing Prime/deal/rank claims or unsafe outbound destination; acceptance: unqualified concept cannot display authoritative Prime/rank/deal badge or monetized destination; dependencies: existing normalized concept output; safe boundary: static/synthetic presentation; verification: snapshot/fixture tests; next handoff: WordPress Overseer.
- security_gates: `SG-05,SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: non-production test; negative_tests: fabricated badges, missing outbound, stale evidence, unsafe link; receipt_evidence: fixture/status/render output; green_required: conditional; prs_required: no; owner_boundary: live publication; security_disposition: PENDING.

# LANE C — Affiliate / Vertical / Content / Marketing

## Affiliate-Websites Master subqueue

### C-AFF-M-01 — reusable publishability evidence contract
- status: ACTIVE; owner/workstream: Affiliate Master; anchor: `darrinbaldwindev/Affiliate-Websites` `main@d3cf400aabe631dc6c2e37193eca8b192856eaba`, active PR #17/#19; objective: unify program identity, country eligibility, reward economics, referral-vs-publisher route, disclosure, evidence freshness and CTA state; acceptance: UNKNOWN/non-affiliate relationship never generates monetized CTA; dependencies: active PR ownership; safe boundary: code/docs/tests on existing branch owner; verification: country fixtures; next handoff: AU/UK/US rows.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: scoped branch/tests; negative_tests: unknown publisher, stale evidence, hostile destination, missing disclosure; receipt_evidence: program/country/evidence/CTA disposition; green_required: conditional; prs_required: no; owner_boundary: signup/contact/live publication; security_disposition: ACTIVE.

### C-AFF-M-02 — CTA destination resolution negatives
- status: PENDING; owner/workstream: Affiliate Master / CTA; anchor: current Master active lineage; objective: challenge malformed/redirected/country-mismatched/referral-only destinations; acceptance: unsafe or unsupported destination falls back to non-monetized informational state; dependencies: C-AFF-M-01 contract; safe boundary: tests only; verification: deterministic fixture matrix; next handoff: country overseers.
- security_gates: `SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: tests; negative_tests: hostile redirect, country mismatch, referral-only treated publisher; receipt_evidence: input/destination/disposition; green_required: conditional; prs_required: no; owner_boundary: publication/signup; security_disposition: PENDING.

### C-AFF-M-03 — disclosure/SEO-AEO state projection
- status: PENDING; owner/workstream: Affiliate Master; anchor: current Master lineage; objective: generate reusable non-production content state that separates evidence-backed facts from UNKNOWN/publisher approval; acceptance: no guaranteed reward/income claim and no hidden affiliate state; dependencies: C-AFF-M-01; safe boundary: static/docs/tests; verification: snapshot/claim scan; next handoff: Marketing.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: draft only; negative_tests: unsupported claim, missing disclosure, unknown approval; receipt_evidence: source/date/claim/disclosure map; green_required: no for draft; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## Affiliate AU subqueue

### C-AFF-AU-01 — AU candidate evidence tranche
- status: PENDING; owner/workstream: Affiliate AU; anchor: Affiliate main `d3cf400a...` + Master contract; objective: take 2–5 reputable AU user-reward/paid-participation candidates through exact country/reward/referral/publisher evidence; acceptance: AU availability and reward terms evidenced separately from publisher approval; dependencies: Master fields; safe boundary: public research; verification: primary terms/date table; next handoff: Master normalizer.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research; negative_tests: worldwide inferred as AU, referral treated publisher, stale terms; receipt_evidence: program/source/date/country/reward/route; green_required: no; prs_required: no; owner_boundary: signup/contact/publication; security_disposition: PENDING.

### C-AFF-AU-02 — AU publishability HOLD matrix
- status: PENDING; owner/workstream: Affiliate AU; anchor: same; objective: explicitly classify missing publisher approval, network account, destination or disclosure as HOLD/fallback; acceptance: no monetized CTA from UNKNOWN; dependencies: AU evidence rows; safe boundary: data/tests; verification: deterministic statuses; next handoff: Master CTA tests.
- security_gates: `SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S0; authority_required: test only; negative_tests: missing approval/network/destination/disclosure; receipt_evidence: row/status/reason; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: PENDING.

### C-AFF-AU-03 — claim-safe AU content packet
- status: PENDING; owner/workstream: Affiliate AU / content handoff; anchor: evidence-complete AU rows only; objective: draft factual non-production descriptions with reward variability and eligibility limits explicit; acceptance: no guaranteed-income/reward or unverified partner language; dependencies: C-AFF-AU-01; safe boundary: draft only; verification: claim-to-source mapping; next handoff: Marketing/Content360.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S0; authority_required: draft only; negative_tests: guarantee/partner/publisher implication; receipt_evidence: source/claim map; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## Affiliate UK subqueue

### C-AFF-UK-01 — UK rewards/publisher evidence tranche
- status: PENDING; owner/workstream: Affiliate UK; anchor: Affiliate main `d3cf400a...`; objective: validate 2–5 UK rewards/paid-participation candidates including Awin/CJ/Impact/Webgains/Tradedoubler evidence where relevant; acceptance: user reward, country eligibility and publisher route separately evidenced; dependencies: Master contract; safe boundary: public research; verification: primary terms/network/date table; next handoff: Master.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research; negative_tests: network presence treated approval, stale terms, country mismatch; receipt_evidence: program/network/source/date/route; green_required: no; prs_required: no; owner_boundary: signup/contact/publication; security_disposition: PENDING.

### C-AFF-UK-02 — conservative regulatory/claim HOLD matrix
- status: PENDING; owner/workstream: Affiliate UK compliance; anchor: same; objective: classify financial/regulatory ambiguity conservatively; acceptance: uncertain financial/promotional claim => HOLD and no guaranteed-income wording; dependencies: current evidence rows; safe boundary: research/docs; verification: claim/risk/status table; next handoff: Marketing.
- security_gates: `SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: research only; negative_tests: guaranteed income, unsupported reward frequency/value; receipt_evidence: source/date/claim/status; green_required: no; prs_required: no; owner_boundary: publication/legal decision; security_disposition: PENDING.

### C-AFF-UK-03 — UK CTA fallback tests
- status: PENDING; owner/workstream: Affiliate UK; anchor: Master CTA resolver + UK rows; objective: ensure referral-only/unknown publisher route never becomes monetized publisher CTA; acceptance: informational fallback is deterministic; dependencies: C-AFF-UK-01; safe boundary: tests; verification: fixture outcomes; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S0; authority_required: test only; negative_tests: referral/publisher confusion, missing account, hostile destination; receipt_evidence: route/status/CTA output; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## Affiliate US subqueue

### C-AFF-US-01 — US paid-participation evidence tranche
- status: ACTIVE; owner/workstream: Affiliate US; anchor: Affiliate repo active US PR #6 on current main `d3cf400a...`; objective: validate 2–5 US user-testing/focus-group/survey/reward candidates; acceptance: reward value and publisher/referral eligibility evidenced separately; dependencies: active PR ownership; safe boundary: existing owner branch/research only; verification: primary terms/date table; next handoff: Master.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read/research; negative_tests: reward treated guaranteed, referral treated publisher; receipt_evidence: program/source/date/reward/route; green_required: no; prs_required: no; owner_boundary: signup/contact/publication; security_disposition: ACTIVE.

### C-AFF-US-02 — destination/eligibility contradiction fixtures
- status: PENDING; owner/workstream: Affiliate US; anchor: US PR #6 schema; objective: deny country/age/participation contradiction and stale destination evidence; acceptance: contradiction => HOLD/fallback; dependencies: existing schema; safe boundary: tests; verification: deterministic fixtures; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S0; authority_required: tests; negative_tests: country mismatch, stale terms, invalid destination; receipt_evidence: fixture/status; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

### C-AFF-US-03 — claim-safe US content packet
- status: PENDING; owner/workstream: Affiliate US / content; anchor: evidence-complete US rows; objective: draft non-production copy with variability/eligibility explicit; acceptance: no guaranteed reward/value/approval; dependencies: C-AFF-US-01; safe boundary: drafts only; verification: source-to-claim map; next handoff: Marketing/Content360.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S0; authority_required: draft only; negative_tests: guarantee/approval implication; receipt_evidence: source/claim map; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## GhostKitchen subqueue

### C-GK-01 — active representative-order economics
- status: ACTIVE; owner/workstream: GhostKitchen; anchor: `darrinbaldwindev/GhostKitchen` `main@dbd64153ca3f2b0e7e9152955692f62f6c9fa59a`, PR #32 active; objective: complete one representative order/menu-item evidence packet without inventing labour/packaging/delivery/yield; acceptance: every input source-tagged and unknowns explicit; dependencies: active PR ownership; safe boundary: docs/tests/calculation on existing owner branch; verification: reproducible unit/contribution calculation; next handoff: readiness gate.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-12,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: scoped branch/research; negative_tests: missing yield/labour/packaging/delivery => NOT_TESTABLE/HOLD; receipt_evidence: source/date/input/formula/output; green_required: conditional; prs_required: no; owner_boundary: supplier/partner contact/spend/production; security_disposition: ACTIVE.

### C-GK-02 — sensitivity mini-batch
- status: PENDING; owner/workstream: GhostKitchen economics; anchor: C-GK-01 evidence-complete inputs only; objective: 2–5 homogeneous sensitivity cases for food cost/yield/labour/packaging/channel fee; acceptance: profitability claim only where all tested inputs evidenced; dependencies: C-GK-01; safe boundary: calculation only; verification: reproducible table; next handoff: Marketing claim ceiling.
- security_gates: `SG-06,SG-10,SG-12,SG-14,SG-20`; risk_class: S0; authority_required: calculation; negative_tests: UNKNOWN input cannot produce verified profit; receipt_evidence: formula/input/output; green_required: no; prs_required: no; owner_boundary: spend/contact; security_disposition: PENDING.

### C-GK-03 — fail-closed readiness fixture
- status: PENDING; owner/workstream: GhostKitchen readiness; anchor: current PR #32 contract; objective: make missing material operating input deterministically non-ready; acceptance: any missing supplier price/yield/labour/packaging/delivery evidence blocks readiness; dependencies: schema; safe boundary: tests; verification: fixture matrix; next handoff: GhostKitchen Overseer.
- security_gates: `SG-06,SG-10,SG-12,SG-14,SG-20`; risk_class: S0; authority_required: tests; negative_tests: each missing field independently; receipt_evidence: fixture/status/reason; green_required: conditional; prs_required: no; owner_boundary: production; security_disposition: PENDING.

## Franchise subqueue

### C-FR-01 — active tenancy/membership isolation owner
- status: ACTIVE; owner/workstream: Franchise; anchor: `darrinbaldwindev/Franchise` `main@0ea3b26de71f78f7eafc38cf50079805b43a7d93`, PR #24/#22 active; objective: preserve active owner for tenancy/franchise identity and territory model; acceptance: no parallel implementation by :30; dependencies: active PRs; safe boundary: inspect/reconcile only outside owner branch; verification: exact PR/head evidence; next handoff: current Franchise owner.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-12,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: current owner branch only; negative_tests: cross-tenant identity, overlap, stale version; receipt_evidence: tenant/franchise/territory/version IDs; green_required: conditional; prs_required: no; owner_boundary: real tenancy/partner activation/production; security_disposition: ACTIVE.

### C-FR-02 — territory duplicate/overlap denial tranche
- status: PENDING; owner/workstream: Franchise assurance; anchor: existing PR schema after C-FR-01 owner exposes stable seam; objective: 2–5 synthetic overlapping/duplicate/stale territory cases; acceptance: deterministic deny with audit reason; dependencies: no conflict with active PR owner; safe boundary: tests only after handoff; verification: exact fixture outputs; next handoff: Franchise owner.
- security_gates: `SG-06,SG-10,SG-11,SG-12,SG-14,SG-20`; risk_class: S1; authority_required: scoped tests; negative_tests: duplicate territory, overlap, stale version, wrong tenant; receipt_evidence: IDs/version/disposition; green_required: conditional; prs_required: no; owner_boundary: production partner activation; security_disposition: PENDING.

### C-FR-03 — real partner/tenancy evidence hold
- status: BLOCKED; owner/workstream: Franchise production readiness; anchor: current synthetic/non-production profile + active PRs; objective: keep production status separate from synthetic routing success; acceptance: no real franchise/tenant/partner claim without authoritative evidence; dependencies: external owner/partner evidence; safe boundary: checklist only; verification: authoritative partner/tenant evidence; next handoff: owner.
- security_gates: `SG-02,SG-10,SG-12,SG-14,SG-15,SG-20`; risk_class: S3; authority_required: owner/partner evidence; negative_tests: synthetic-to-production promotion; receipt_evidence: authoritative identity/version; green_required: yes for production; prs_required: conditional; owner_boundary: partner activation/production; security_disposition: BLOCKED_OWNER_REQUIRED.

## GemVerse subqueue

### C-GV-01 — active source-intake/recovery owner
- status: ACTIVE; owner/workstream: GemVerse; anchor: `darrinbaldwindev/GemVerse` `gemverse@b36750f01f62184e2f563ff8f8030682ba10033e`, PR #10 active; objective: preserve active owner for source-intake recovery and exact target/preimage identity; acceptance: no duplicate implementation/control plane; dependencies: active PR #10; safe boundary: reconcile/read outside owner; verification: exact PR/head; next handoff: GemVerse owner.
- security_gates: `SG-05,SG-06,SG-07,SG-09,SG-10,SG-11,SG-14,SG-20`; risk_class: S2; authority_required: current owner branch; negative_tests: stale identity, competing candidate, replay/idempotence; receipt_evidence: source/preimage/target/version IDs; green_required: conditional; prs_required: no; owner_boundary: alternate AgentOS control plane/production; security_disposition: ACTIVE.

### C-GV-02 — competing candidate/stale identity negatives
- status: PENDING; owner/workstream: GemVerse assurance; anchor: PR #10 stable seam when handed off; objective: 2–5 synthetic negatives for competing candidates, changed preimage, stale target identity and retry; acceptance: only exact expected preimage/target can proceed; dependencies: no overlap with active owner; safe boundary: tests; verification: exact fixture outcomes; next handoff: GemVerse owner.
- security_gates: `SG-06,SG-09,SG-10,SG-11,SG-14`; risk_class: S1; authority_required: scoped tests; negative_tests: candidate conflict, stale preimage, target drift, replay; receipt_evidence: source/preimage/target hashes; green_required: conditional; prs_required: no; owner_boundary: production/control-plane creation; security_disposition: PENDING.

### C-GV-03 — Level-2 fixture readiness packet
- status: PENDING; owner/workstream: GemVerse / AgentOS acceptance candidate; anchor: GemVerse current deterministic mutation fixture concept + AgentOS A-AG-01/A-AG-02 blockers; objective: keep exact bounded file-edit/idempotency/recovery workload ready without executing it through unaccepted AgentOS mutation path; acceptance: exact preimage/edit/postimage/rollback/receipt expectations documented; dependencies: AgentOS SG-08 + SG-01/02 + Green/PRS before execution; safe boundary: fixture docs/tests only; verification: deterministic fixture self-check; next handoff: AgentOS owner after gates pass.
- security_gates: `SG-03,SG-08,SG-09,SG-10,SG-11,SG-14,SG-18,SG-19,SG-20`; risk_class: S1; authority_required: fixture-only; negative_tests: wrong preimage, replay, concurrency, recovery; receipt_evidence: exact hashes/diff/expected receipt; green_required: yes before Level-2 execution; prs_required: yes before promotion; owner_boundary: physical/production mutation; security_disposition: PENDING_GATED.

## Content360 subqueue

### C-C360-01 — provider-neutral request/result integrity owner
- status: ACTIVE; owner/workstream: Content360; anchor: `darrinbaldwindev/content360` PR #4 exact `dd9bb49f09d4f67bf055e5418afb4a6bc55eff09`, no newer exact-head CI established this cycle; objective: preserve active owner for request/result provenance and Marketing-source receipt work; acceptance: no concurrent duplicate adapter/persistence work; dependencies: PR #4; safe boundary: current owner branch only; verification: exact head + later CI; next handoff: Content360 owner.
- security_gates: `SG-05,SG-06,SG-07,SG-09,SG-10,SG-11,SG-14,SG-15`; risk_class: S2; authority_required: scoped branch/tests; negative_tests: malformed provider response, prompt injection, duplicate correlation, secret leak; receipt_evidence: request/result/provider/source/correlation IDs; green_required: yes for changed implementation; prs_required: conditional; owner_boundary: credentials/live network/PUBLISH/SCHEDULE/account mutation; security_disposition: ACTIVE_CI_PENDING.

### C-C360-02 — mocked provider failure mini-batch
- status: PENDING; owner/workstream: Content360 assurance; anchor: PR #4 existing adapter seam after owner handoff; objective: 2–5 homogeneous mocked failures: timeout, malformed result, provider substitution, duplicate result, wrong correlation; acceptance: no success/publication state and provenance remains exact; dependencies: no overlap with PR owner; safe boundary: mocked tests; verification: exact-head CI; next handoff: Content360 owner.
- security_gates: `SG-05,SG-06,SG-09,SG-10,SG-11,SG-14,SG-17`; risk_class: S1; authority_required: tests; negative_tests: timeout/malformed/substitution/duplicate/wrong-correlation; receipt_evidence: request/provider/result/disposition; green_required: conditional; prs_required: no; owner_boundary: live network/account mutation; security_disposition: PENDING.

### C-C360-03 — READ/OPTIMISE boundary contract
- status: PENDING; owner/workstream: Content360 / Marketing handoff; anchor: central profile + PR #4; objective: prove approved Marketing content may be read/optimised but cannot silently become PUBLISH/SCHEDULE authority; acceptance: publish/schedule/network/account mutation always false without explicit owner grant; dependencies: existing capability model; safe boundary: tests/docs; verification: capability matrix negatives; next handoff: Marketing.
- security_gates: `SG-03,SG-05,SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: READ/OPTIMISE only; negative_tests: optimise->publish escalation, schedule, network/account write; receipt_evidence: requested/granted capability + disposition; green_required: conditional; prs_required: no; owner_boundary: credentials/publication/scheduling; security_disposition: PENDING.

### C-C360-04 — official API/auth capability evidence
- status: BLOCKED; owner/workstream: Content360 external capability research; anchor: profile + current PR #4; objective: document official supported API/auth/capabilities without exposing existing credentials; acceptance: official docs/evidence only, credentials opaque, unsupported capability remains UNKNOWN; dependencies: external authoritative docs; safe boundary: public research; verification: source/date/capability table; next handoff: owner for any connection action.
- security_gates: `SG-05,SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research only; negative_tests: copied secret, unofficial inference, network mutation; receipt_evidence: official source/date/capability; green_required: no; prs_required: no; owner_boundary: credentials/live connection/publication; security_disposition: BLOCKED_EXTERNAL_EVIDENCE.

## Commercial Frontend subqueue

### C-CF-01 — Tradie/service-ops exception evidence packet
- status: PENDING; owner/workstream: Commercial Frontend; anchor: `darrinbaldwindev/Overseer` commercial-frontend issue/workstream current portfolio evidence; objective: define one bounded operator exception workflow with inputs, evidence, correction and receipt; acceptance: no demand/WTP claim presented as verified; dependencies: existing issue/workstream; safe boundary: docs/prototype only; verification: scenario/receipt walkthrough; next handoff: frontend owner.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-12,SG-14,SG-15,SG-20`; risk_class: S0; authority_required: docs/prototype; negative_tests: unsupported demand claim, unbounded correction, cross-customer data; receipt_evidence: scenario/input/action/result; green_required: no; prs_required: no; owner_boundary: customer contact/deployment/account mutation; security_disposition: PENDING.

### C-CF-02 — property/ecommerce exception mini-batch
- status: PENDING; owner/workstream: Commercial Frontend; anchor: same workstream; objective: add 2–5 homogeneous evidence-first exception cases with deterministic status and operator correction boundary; acceptance: each case has measurable operator outcome hypothesis but no fabricated market proof; dependencies: C-CF-01 pattern; safe boundary: docs/prototype; verification: scenario matrix; next handoff: product research.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-12,SG-14,SG-20`; risk_class: S0; authority_required: docs/prototype; negative_tests: invented evidence, cross-tenant scope, unbounded write; receipt_evidence: case/evidence/correction/result; green_required: no; prs_required: no; owner_boundary: deployment/customer contact; security_disposition: PENDING.

### C-CF-03 — demand/WTP evidence hold and research synthesis
- status: BLOCKED; owner/workstream: Commercial Frontend market validation; anchor: central profile states pain/demand/WTP remain hypothesis until externally evidenced; objective: maintain explicit evidence gap while synthesising allowed public market evidence; acceptance: no customer/willingness-to-pay claim upgraded without direct evidence; dependencies: external/public research; safe boundary: research only; verification: source/date/hypothesis matrix; next handoff: owner before any outreach.
- security_gates: `SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research; negative_tests: proxy evidence treated direct demand; receipt_evidence: source/date/hypothesis/status; green_required: no; prs_required: no; owner_boundary: customer contact/deployment; security_disposition: BLOCKED_DIRECT_EVIDENCE.

## Marketing subqueue

### C-MKT-01 — claim ladder refresh
- status: PENDING; owner/workstream: Marketing / AgentOS+GlobalShopCo+Affiliate; anchor: current product truth from AgentOS PR #104/#111, GSC `0 eBay-ready`, Affiliate active evidence gates; objective: refresh claim ladder to current evidence ceiling; acceptance: no overall GREEN, partner, conversion, eBay-ready, live-qualified or unsupported compatibility claim; dependencies: current evidence only; safe boundary: internal drafts; verification: claim-to-evidence map; next handoff: Content360 READ/OPTIMISE.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S0; authority_required: draft only; negative_tests: unsupported readiness/partner/conversion/compatibility; receipt_evidence: claim/source/date/status; green_required: no; prs_required: no; owner_boundary: publication/campaign/spend/outreach; security_disposition: PENDING.

### C-MKT-02 — internal landing/ad objection mini-batch
- status: PENDING; owner/workstream: Marketing content; anchor: C-MKT-01 evidence ceiling; objective: create 2–5 homogeneous internal content assets/objection responses that remain valid while commerce products are HOLD; acceptance: no product-readiness-dependent conversion claim and all factual statements traceable; dependencies: C-MKT-01; safe boundary: draft assets only; verification: source/claim review; next handoff: Content360 optimisation.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S0; authority_required: draft only; negative_tests: fabricated performance, unsupported product readiness, hidden affiliate relationship; receipt_evidence: asset/source/claim map; green_required: no; prs_required: no; owner_boundary: publication/campaign activation/spend; security_disposition: PENDING.

### C-MKT-03 — influencer/affiliate evidence refresh
- status: PENDING; owner/workstream: Marketing research; anchor: existing portfolio influencer/affiliate direction; objective: refresh 2–5 evidence-backed creator/program candidates with public contact route/rate evidence where available, without outreach; acceptance: no fabricated rates/relationships; dependencies: public evidence; safe boundary: research only; verification: source/date/table; next handoff: owner shortlist only.
- security_gates: `SG-05,SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research; negative_tests: guessed rate/contact/partnership; receipt_evidence: source/date/candidate/evidence status; green_required: no; prs_required: no; owner_boundary: outreach/spend/agreement; security_disposition: PENDING.

### C-MKT-04 — Content360-ready provenance package
- status: PENDING; owner/workstream: Marketing -> Content360; anchor: C-MKT-01/02 + Content360 C-C360-03; objective: package approved internal content with source/provenance and explicit `READ/OPTIMISE` scope; acceptance: no PUBLISH/SCHEDULE authority or secret material; dependencies: claim-safe assets; safe boundary: internal handoff artifact; verification: provenance/capability scan; next handoff: Content360.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: internal READ/OPTIMISE; negative_tests: publish/schedule flag, secret-shaped data, unsupported claim; receipt_evidence: content/source/scope/version; green_required: no; prs_required: no; owner_boundary: publication/campaign; security_disposition: PENDING.

# Lane health after replenishment
- **Lane A:** multiple useful PENDING/SPLIT_REQUIRED items remain (A-AG-05B, A-PRS-03) while A-AG-01, A-AG-02, A-PRS-02 and physical Windows stay explicit blockers. A-AG-06 is exact-head functionally VERIFIED only; no security/authority widening.
- **Lane B:** multiple useful PENDING items exist across GSC economics/research, Headless contract/secret negatives, eBay replay-state inspection, Amazon contradiction/composition fixtures, and MyPrime exact-identity/presentation work. Real publication/seller/provider authority remains blocked.
- **Lane C:** every fixed workstream has at least one actionable next item; active PR ownership in Affiliate/GhostKitchen/Franchise/GemVerse/Content360 is preserved rather than duplicated. External publication/contact/partner/canon/provider evidence blockers remain explicit.

**No overall GREEN.** Functional success does not upgrade security; security success does not upgrade functional state. Scheduler firing and worker claims are not completion evidence.