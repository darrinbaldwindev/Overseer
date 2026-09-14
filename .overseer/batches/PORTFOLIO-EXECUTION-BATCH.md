# Portfolio Execution Batch Manifest

**Purpose:** queue state only. Canonical procedure: `.overseer/doctrine/PORTFOLIO-BATCH-ENGINE.md`; project shaping: `.overseer/profiles/PROJECT-BATCH-PROFILES.md`; security: `.overseer/security/AGENTOS-SECURITY-GATE-MATRIX.md`. Current repository/runtime/CI evidence always outranks this file.

**Fixed lanes:** A = AgentOS Level 2 P0 + PRS/Green assurance-adjacent work; B = GlobalShopCo/Headless/eBay/Amazon/MyPrimeDelivery; C = Affiliate-Websites AU/UK/US/Master, GhostKitchen, Franchise, GemVerse, Content360, Commercial Frontend, Marketing.

**States:** `PENDING | ACTIVE | VERIFIED | BLOCKED | STALE | SPLIT_REQUIRED`.

**Core invariant:** **NO MODEL DECIDES ITS OWN AUTHORITY.** Functional, security and PRS state remain separate. No merge/approve/ready/rebase/deploy/credentials/security-policy changes/production writes/purchases/spend/supplier contact/live publication/physical owner-host action/production autonomy.

## Checkpoint reconciliation — 2026-09-15 05:30 Brisbane
- Previous durable checkpoint: Overseer #49 `5668798421`; previous manifest commit `f6e8d62471cdb2cdc22f3443ea4a3ac5178b7bcf` / blob `c896fb582604a7d4599378e5eb1389557cbb96eb`.
- Canonical engine, project profiles, security matrix, shared manifest, and material #49 evidence after the previous checkpoint were read before reconciliation.
- **AgentOS:** PR #104 is OPEN/DRAFT at current head `d46d67414228231611cd6a34999163055315de57`. Substantive predecessor `a24270b5d1e90d946c6d0ecc52c9aa66736d02bb` has exact-head AgentOS Tests `34884462139` SUCCESS for expected delivery/mission/task/wake mismatch denial. Current docs successor has mixed current-head checks: run `34884690804` succeeded on Ubuntu+Windows, but later run `34884807154` has Ubuntu success and Windows failure. Therefore current-head promotion is **ACTIVE/CI_BLOCKED**, not VERIFIED. SG-08 and SG-01/02 remain controlling blockers; A-AG-05B remains split.
- **Independent assurance:** A-AG-06 predecessor exact `2c52de5820f1dfb0dc2536ec1a6887443b5a063d` / CI `34882077547` is bounded PASS only. It does not transfer to `d46d674...`.
- **shopify_ebay:** exact `23b263ecd4e04667e6c95977f694c66cce4734e2` / Fixture validation `34885862149` SUCCESS. Non-canonical whitespace in `event_id` now fails closed as `NON_CANONICAL_EVENT_ID`; bounded synthetic SG-09/10 reliability is VERIFIED. The repo has no durable replay persistence; upstream durability remains UNKNOWN and no local persistence plane may be invented.
- **Lane C:** GemVerse PR #10 exact `b6b4bb4def2eb6a244671afe17a7670075249205` / `34883530631` SUCCESS is VERIFIED_BOUNDED fixture-only. GhostKitchen PR #32 exact `316ade476804a5e3dcdef8e8f986a2ca3de431cb` has no exact-head checks and remains ACTIVE/CI_PENDING. Content360 PR #4 exact `b2c3b222ef06f98951b20312591b7af65c7ac952` has no exact-head checks/workflow runs and remains ACTIVE/CI_PENDING.
- **Commerce truth remains fail-closed:** GlobalShopCo still has `0 eBay-ready SKUs`; authenticated trade cost, freight, permission, stock identity and economics remain required. MyPrimeDelivery bounded synthetic identity conflict denial remains at `61feceb46de539948374deec86b3fe7578cf8014` / `34879834476` SUCCESS; live qualified count remains `0` and live Prime/rank/rights/publication authority remains UNKNOWN/HOLD.

# LANE A — AgentOS Level 2 P0

## AgentOS Overseer

### A-AG-01 — continuous project-file ownership fence
- status: BLOCKED; anchor: `AgentOS#104@d46d67414228231611cd6a34999163055315de57`, historical PRS stale-owner baseline `0defebe26f71e1cf5df1168fa5454bfd8de30091/34821646371`; objective: one kernel-enforced crash-releasing fence held continuously final verification -> publish/prepared recovery -> durable success receipt -> release; acceptance: replacement-after-verify, successor/three-writer, stale identity, TOCTOU, crash/replay, duplicate mutation/result and prepared-recovery stale-owner all fail closed; dependencies: real writer seam; safe boundary: draft non-production code/tests; verification: exact-head Ubuntu+Windows CI + adversarial ownership matrix; next handoff: unchanged head -> Green -> PRS after Green PASS.
- security_gates: `SG-03,SG-08,SG-09,SG-10,SG-11,SG-14,SG-18,SG-19`; risk_class: S2; authority_required: scoped branch/test write; negative_tests: full ownership matrix; receipt_evidence: actor/task/file/pre-postimage/ownership/result lineage; green_required: yes; prs_required: yes; owner_boundary: merge/deploy/physical production; security_disposition: BLOCKED.

### A-AG-02 — authenticated actor + canonical grant binding
- status: BLOCKED; anchor: `AgentOS#104@d46d674...` + existing caller-supplied authority seam; objective: bind an existing authenticated actor source and canonical grant resolver without a second authority registry; acceptance: payload/host cannot self-supply identity/grant; absent/spoofed/mismatched/cross-project/replayed grant yields no admitted artifact/success receipt; dependencies: real bindable canonical source; safe boundary: discovery + bounded tests; verification: spoof/mismatch/replay matrix; next handoff: implement only when the existing source is evidenced.
- security_gates: `SG-01,SG-02,SG-03,SG-04,SG-09,SG-10,SG-11,SG-18,SG-19`; risk_class: S2; authority_required: canonical identity/grant read + scoped tests; negative_tests: host-as-auth, spoof actor, self-grant, absent/mismatch/cross-project/replay; receipt_evidence: issuer/source/version/request/task/mission; green_required: yes; prs_required: yes; owner_boundary: credentials/security policy; security_disposition: BLOCKED.

### A-AG-03 — current-head CI repair without weakening lineage checks
- status: ACTIVE; anchor: `AgentOS#104@d46d674...`; current checks include `34884690804` SUCCESS and later `34884807154` Windows FAILURE; objective: identify/fix the exact Windows failure while preserving predecessor `a24270b5.../34884462139` correlation denial semantics; acceptance: unchanged production fail-closed behavior and current exact head green on Ubuntu+Windows; dependencies: current failure annotations/logs; safe boundary: minimal tests/code repair on existing seam; verification: exact-head CI only; next handoff: Green sample after clean exact-head result.
- security_gates: `SG-10,SG-11,SG-14,SG-18`; risk_class: S2; authority_required: scoped branch/test write; negative_tests: cross-mission/task/wake, forged durable evidence identity, regression of canonical correlation; receipt_evidence: head/run/test names + failure/repair lineage; green_required: yes; prs_required: conditional; owner_boundary: merge/deploy; security_disposition: ACTIVE.

### A-AG-04 — A-AG-05B replay/restart/direct-adapter closure
- status: SPLIT_REQUIRED; anchor: substantive `a24270b5.../34884462139` + current `d46d674...`; objective: close conflicting replay, restart/reload duplicate behavior, remaining direct-adapter malformed-receipt paths and freshness only if a canonical freshness source exists; acceptance: malformed or mismatched durable receipt cannot persist/return success; restart preserves first-write provenance; dependencies: clean A-AG-03 current head; safe boundary: tests/minimal validation on existing persistence boundary; verification: exact-head restart/replay/direct-adapter negatives; next handoff: Green SG-09/10/11.
- security_gates: `SG-09,SG-10,SG-11,SG-14,SG-18`; risk_class: S2; authority_required: scoped tests/write; negative_tests: replay, restart duplicate, direct malformed adapter, cross-lineage mismatch; receipt_evidence: authoritative IDs + first-write provenance; green_required: yes; prs_required: conditional; owner_boundary: no new persistence/authority plane; security_disposition: SPLIT_REQUIRED.

### A-AG-05 — physical Windows acceptance packet
- status: BLOCKED; anchor: `AgentOS#104@d46d674...`; objective: preserve owner-run physical acceptance packet; acceptance: exact SHA/root/mutation/recovery/correlation/no-production boundary; dependencies: SG-08 + SG-01/02 + clean exact-head software/Green + explicit owner physical authority; safe boundary: checklist only; verification: future physical-host evidence; next handoff: owner after software/security closure.
- security_gates: `SG-03,SG-08,SG-10,SG-11,SG-14,SG-18,SG-20`; risk_class: S2; authority_required: owner-authorized physical Windows action; negative_tests: wrong head, production root, missing receipt; receipt_evidence: head/host/root/test/result; green_required: yes; prs_required: yes if promoted; owner_boundary: physical Windows execution; security_disposition: BLOCKED.

## PRS / Green

### A-PRS-01 — immutable stale-owner baseline
- status: VERIFIED; anchor: `PRS baseline 0defebe26f71e1cf5df1168fa5454bfd8de30091/34821646371`; objective: preserve immutable false-GREEN target; acceptance: target/artifact identity immutable; dependencies: none; safe boundary: read-only; verification: hashes; next handoff: A-AG-01.
- security_gates: `SG-08,SG-10,SG-11,SG-19`; risk_class: S0; authority_required: read-only; negative_tests: normal + prepared-recovery stale-owner; receipt_evidence: exact target/artifact hashes; green_required: no; prs_required: baseline; owner_boundary: none; security_disposition: VERIFIED.

### A-PRS-02 — current-head bounded Green sample
- status: PENDING; anchor: `AgentOS#104@d46d674...`; objective: after A-AG-03 clean exact-head CI, challenge correlation/evidence projection without entering blocked ownership/admission scope; acceptance: no forged evidence identity, stale lineage, malformed projection or secret/raw evidence leak; dependencies: A-AG-03 VERIFIED; safe boundary: independent read/test; verification: exact-head negatives; next handoff: AgentOS Overseer.
- security_gates: `SG-05,SG-10,SG-11,SG-18`; risk_class: S1; authority_required: read/test; negative_tests: forged identity, stale lineage, malformed projection, leakage; receipt_evidence: exact target/run/outcome; green_required: yes; prs_required: conditional; owner_boundary: merge/deploy; security_disposition: PENDING.

### A-PRS-03 — completion-grade ownership challenge
- status: BLOCKED; anchor: `AgentOS#104@d46d674...` + A-PRS-01; objective: rerun ownership matrix only after real SG-08 repair and identical-head Green PASS; acceptance: normal/prepared/successor/crash/replay independently classified; dependencies: A-AG-01 + clean exact CI + Green; safe boundary: assurance harness; verification: immutable target/artifact hashes; next handoff: Overseer.
- security_gates: `SG-08,SG-09,SG-10,SG-11,SG-19`; risk_class: S2; authority_required: bounded harness; negative_tests: full ownership matrix; receipt_evidence: exact target/artifact hash; green_required: yes prerequisite; prs_required: yes; owner_boundary: merge/deploy; security_disposition: BLOCKED.

# LANE B — Commerce

## GlobalShopCo

### B-GSC-01 — PR #29/#30 exact supplier evidence rows
- status: ACTIVE; anchor: `darrinbaldwindev/GlobalShopCo` PR #29/#30; portfolio evidence `Overseer#49/5669389060`; objective: close exact SKU rows only where authenticated trade cost, packaged freight, permission, stock identity and returns/warranty evidence exists; acceptance: every promoted field source/date/identity traceable; dependencies: current PR evidence; safe boundary: research/data/docs only; verification: row-by-row provenance review; next handoff: free-delivery economics gate.
- security_gates: `SG-02,SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read-only public/internal evidence; negative_tests: missing freight, retail-as-wholesale, permission inference, stale stock; receipt_evidence: source/date/SKU/cost/freight/status; green_required: no; prs_required: no; owner_boundary: supplier contact/purchase/production Shopify; security_disposition: ACTIVE.

### B-GSC-02 — free-delivery conservative margin gate
- status: PENDING; anchor: same PR #29/#30 evidence; objective: compute delivered margin only for evidence-complete candidates; acceptance: fees/freight/returns allowance explicit and UNKNOWN inputs force HOLD; dependencies: B-GSC-01; safe boundary: deterministic calculator/data; verification: contradiction + missing-field fixtures; next handoff: channel readiness.
- security_gates: `SG-10,SG-12,SG-13,SG-14,SG-20`; risk_class: S1; authority_required: non-production calculation; negative_tests: zero/unknown freight, missing fee, stale cost, negative margin; receipt_evidence: input sources + calculation version + disposition; green_required: no; prs_required: no; owner_boundary: spend/listing; security_disposition: PENDING.

### B-GSC-03 — channel-ready shortlist
- status: PENDING; anchor: `Overseer#49/5669389060` truth `0 eBay-ready SKUs`; objective: produce 2–5 homogeneous evidence-complete candidates only if upstream evidence clears; acceptance: exact variant/SKU + permission + stock + delivered economics + returns/warranty; dependencies: B-GSC-01/02; safe boundary: shortlist only; verification: fail-closed readiness schema; next handoff: eBay/Amazon fixture lanes.
- security_gates: `SG-02,SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: read-only; negative_tests: any missing readiness field => HOLD; receipt_evidence: candidate packet; green_required: no; prs_required: no; owner_boundary: publication/contact/spend; security_disposition: PENDING.

## GlobalShopCo-Headless

### B-HDL-01 — dev-store/browser checkout handoff proof
- status: BLOCKED; anchor: `Overseer#49/5669389060`; objective: prove one non-production product retrieval -> render -> Shopify checkout handoff with Shopify authoritative; acceptance: exact identity/availability preserved and checkout host allow-listed; dependencies: usable dev-store/browser evidence + one parent candidate; safe boundary: non-production only; verification: browser trace + deterministic contract assertions; next handoff: Headless Overseer.
- security_gates: `SG-03,SG-05,SG-06,SG-10,SG-14,SG-20`; risk_class: S2; authority_required: dev-only browser/store access; negative_tests: malformed checkout host, stale variant, unavailable product, secret leak; receipt_evidence: request/product/checkout destination trace; green_required: yes; prs_required: no; owner_boundary: deployment/secrets/live purchase; security_disposition: BLOCKED.

### B-HDL-02 — checkout destination/host negative pack
- status: PENDING; anchor: current deterministic Headless contract + blocker above; objective: widen only adjacent malformed destination cases; acceptance: 2–5 encoded/alternate-host/path-confusion cases deny deterministically; dependencies: existing parser contract; safe boundary: tests only; verification: exact-head CI; next handoff: B-HDL-01.
- security_gates: `SG-05,SG-06,SG-10,SG-14`; risk_class: S2; authority_required: branch/test write; negative_tests: encoded host, scheme confusion, userinfo, redirect-like path; receipt_evidence: exact head/run/test list; green_required: yes; prs_required: no; owner_boundary: deploy/live checkout; security_disposition: PENDING.

### B-HDL-03 — server-side secret boundary regression
- status: PENDING; anchor: current Headless server contract; objective: prove browser-facing payload cannot expose server credentials or opaque handles; acceptance: secret-shaped fields absent/redacted; dependencies: existing adapter; safe boundary: tests only; verification: fixture scan + exact-head CI; next handoff: Headless Overseer.
- security_gates: `SG-05,SG-06,SG-14`; risk_class: S2; authority_required: branch/test write; negative_tests: env leak, error serialization, debug payload; receipt_evidence: scan/run; green_required: yes; prs_required: no; owner_boundary: credentials/deploy; security_disposition: PENDING.

## Shopify to eBay

### B-EBY-01 — replay identity canonicality
- status: VERIFIED; anchor: `shopify_ebay@23b263ecd4e04667e6c95977f694c66cce4734e2`, Fixture validation `34885862149`; objective: reject non-canonical event IDs rather than normalize replay identity; acceptance: whitespace variant fails `NON_CANONICAL_EVENT_ID`; dependencies: none; safe boundary: synthetic tests; verification: exact-head CI; next handoff: B-EBY-02.
- security_gates: `SG-09,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: test/branch write; negative_tests: whitespace/correlation ambiguity; receipt_evidence: head/run/error code; green_required: yes if widened; prs_required: no; owner_boundary: network/publication; security_disposition: VERIFIED_BOUNDED.

### B-EBY-02 — upstream durable replay-store discovery
- status: PENDING; anchor: `shopify_ebay@23b263ec...` code inspection + `Overseer#49/5669389060`; objective: identify whether caller/host already owns durable replay state; acceptance: existing store documented with ownership/correlation semantics or durability explicitly UNKNOWN; dependencies: none; safe boundary: read-only inspection; verification: code/host contract evidence; next handoff: if existing, add 2–5 bounded restart/replay fixtures; if absent, do not create local plane.
- security_gates: `SG-09,SG-10,SG-11,SG-14`; risk_class: S1; authority_required: read-only repo/host contract; negative_tests: restart duplicate, conflicting payload same ID, same payload different ID where contract defines; receipt_evidence: source path/interface/owner; green_required: no; prs_required: no; owner_boundary: production state/network; security_disposition: PENDING.

### B-EBY-03 — real SKU handoff readiness
- status: BLOCKED; anchor: upstream `0 eBay-ready SKUs` in `Overseer#49/5669389060`; objective: map one evidence-complete Shopify variant only after GSC readiness; acceptance: permission/inventory/economics/fees/fulfilment/seller identity all present; dependencies: B-GSC-03; safe boundary: fixture mapping only; verification: fail-closed gate; next handoff: eBay Overseer.
- security_gates: `SG-02,SG-03,SG-06,SG-09,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: non-production mapping; negative_tests: every missing commercial field; receipt_evidence: mapping receipt + upstream evidence IDs; green_required: yes; prs_required: no; owner_boundary: seller setup/network/publication; security_disposition: BLOCKED.

## Shopify to Amazon

### B-AMZ-01 — freshness/correlation contradiction pack
- status: PENDING; anchor: existing GlobalShopCo Amazon channel fixtures, portfolio evidence `Overseer#49/5669389060`; objective: add 2–5 homogeneous stale/conflicting seller/variant/stock/category/GTIN/fee cases supported by schema; acceptance: contradiction never composes to READY; dependencies: current fixture schema; safe boundary: synthetic tests; verification: exact fixture CI; next handoff: Amazon channel owner.
- security_gates: `SG-02,SG-06,SG-09,SG-10,SG-12,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: fixture write; negative_tests: stale seller, variant mismatch, stock mismatch, GTIN/category conflict, fee freshness; receipt_evidence: input identities + disposition; green_required: yes if widened; prs_required: no; owner_boundary: seller setup/listing/network; security_disposition: PENDING.

### B-AMZ-02 — seller/permission fail-closed contract
- status: PENDING; anchor: same channel fixture lineage; objective: ensure missing seller-of-record or supplier/marketplace permission cannot be inferred from product existence; acceptance: explicit HOLD reason; dependencies: existing schema; safe boundary: tests/docs; verification: deterministic negatives; next handoff: B-AMZ-03.
- security_gates: `SG-02,SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: test write; negative_tests: missing seller, inferred permission, cross-market seller; receipt_evidence: gate reason/source; green_required: yes; prs_required: no; owner_boundary: account/listing; security_disposition: PENDING.

### B-AMZ-03 — one evidence-complete candidate fixture
- status: BLOCKED; anchor: B-GSC-03; objective: instantiate one exact Shopify variant only after upstream evidence clears; acceptance: seller, permission, stock, GTIN/category, fulfilment and fees/economics all exact; dependencies: GSC candidate; safe boundary: non-production fixture; verification: full gate pass; next handoff: Amazon Overseer.
- security_gates: `SG-02,SG-03,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: fixture only; negative_tests: missing/contradictory field; receipt_evidence: source IDs + fixture result; green_required: yes; prs_required: no; owner_boundary: live listing; security_disposition: BLOCKED.

## MyPrimeDelivery

### B-MPD-01 — identity-conflict baseline
- status: VERIFIED; anchor: `MyPrimeDelivery@61feceb46de539948374deec86b3fe7578cf8014`, `34879834476` SUCCESS; objective: preserve multi-ASIN normalized-title fail-close baseline; acceptance: conflicting known ASINs => 0 qualified/publication false/network false; dependencies: none; safe boundary: synthetic fixture; verification: exact-head CI; next handoff: B-MPD-02.
- security_gates: `SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: fixture tests; negative_tests: multi-ASIN conflict; receipt_evidence: head/run/counts; green_required: yes if widened; prs_required: no; owner_boundary: provider signup/credentials/publication; security_disposition: VERIFIED_BOUNDED.

### B-MPD-02 — authorised identity/evidence adapter negatives
- status: PENDING; anchor: B-MPD-01 + current Batch 009 lineage; objective: add 2–5 provider-neutral ASIN/marketplace/variant/freshness conflict fixtures; acceptance: no inferred ASIN/Prime/rank/deal truth; dependencies: existing adapter contract; safe boundary: fixtures/tests; verification: exact-head CI; next handoff: MyPrime Overseer.
- security_gates: `SG-05,SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: branch/test write; negative_tests: ASIN mismatch, marketplace mismatch, stale provider evidence, variant conflict; receipt_evidence: provider/source/freshness/identity result; green_required: yes; prs_required: no; owner_boundary: credentials/provider signup/publication; security_disposition: PENDING.

### B-MPD-03 — WordPress presentation readiness packet
- status: PENDING; anchor: live qualified count `0` per `Overseer#49/5669389060`; objective: define presentation contract that distinguishes PROVISIONAL/HOLD/QUALIFIED without implying Prime/rank authority; acceptance: unresolved/stale/unsupported concepts visibly non-qualified and outbound destination validated; dependencies: existing evidence model; safe boundary: docs/fixtures/UI data only; verification: rendering fixture + destination negatives; next handoff: WordPress implementation after authoritative provider evidence exists.
- security_gates: `SG-05,SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: non-production docs/tests; negative_tests: stale badge, unsupported Prime claim, malformed outbound destination; receipt_evidence: status/evidence source/destination; green_required: no; prs_required: no; owner_boundary: live publication; security_disposition: PENDING.

# LANE C — Ventures / content

## Affiliate-Websites Master

### C-AFF-M1 — publication-state/CTA ownership preservation
- status: ACTIVE; anchor: `Affiliate-Websites main@d3cf400aabe631dc6c2e37193eca8b192856eaba`, active PR #17/#19, `Overseer#49/5669064204`; objective: continue only inside existing publication-state/CTA seams; acceptance: UNKNOWN/non-affiliate relationships never yield monetized CTA; dependencies: active PR owners; safe boundary: non-production code/tests; verification: exact-head CI on owning PR; next handoff: Master Overseer.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: scoped branch/test write; negative_tests: unknown relationship, malformed destination, disclosure absent, cross-country reuse; receipt_evidence: program/country/state/destination; green_required: yes; prs_required: no; owner_boundary: signup/contact/publication; security_disposition: ACTIVE.

### C-AFF-M2 — reusable evidence contract
- status: PENDING; anchor: same main/PR lineage; objective: define common evidence fields for AU/UK/US without flattening country facts; acceptance: reward/referral route, publisher route, approval state, terms/freshness, disclosure and destination separated; dependencies: M1 schema; safe boundary: schema/tests; verification: three-country fixtures; next handoff: country queues.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: branch/test write; negative_tests: member-referral-as-publisher, stale terms, country mismatch; receipt_evidence: evidence source/date/type; green_required: yes; prs_required: no; owner_boundary: publication/signup; security_disposition: PENDING.

### C-AFF-M3 — CTA destination hardening
- status: PENDING; anchor: PR #17/#19 existing CTA seam; objective: add 2–5 malformed/unsupported destination negatives; acceptance: only evidenced approved destination renders monetized CTA; dependencies: M1; safe boundary: tests; verification: exact-head CI; next handoff: Master Overseer.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: tests; negative_tests: redirector, wrong country, unsupported network, absent approval; receipt_evidence: destination/evidence/disposition; green_required: yes; prs_required: no; owner_boundary: live CTA/publication; security_disposition: PENDING.

## Affiliate AU

### C-AU-01 — reputable AU candidate evidence packet
- status: PENDING; anchor: `Affiliate-Websites@d3cf400...`, AU workstream; objective: take 2–5 homogeneous user-reward/referral candidates through first-party terms, AU eligibility, reward economics, referral/publisher separation and freshness; acceptance: publisher approval UNKNOWN if not evidenced; dependencies: Master evidence contract; safe boundary: public research/data; verification: source/date cross-check; next handoff: AU read-model owner.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research; negative_tests: referral≠publisher, stale terms, AU unavailable; receipt_evidence: source/date/country/route/status; green_required: no; prs_required: no; owner_boundary: signup/contact/publication; security_disposition: PENDING.

### C-AU-02 — publishability fixture pack
- status: PENDING; anchor: Master/AU current gate; objective: map 2–5 AU evidence packets into CTA/no-CTA outcomes; acceptance: UNKNOWN approval => non-monetized fallback; dependencies: C-AU-01; safe boundary: fixtures/tests; verification: exact-head CI; next handoff: AU Overseer.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: test write; negative_tests: expired terms, wrong destination, missing disclosure; receipt_evidence: candidate/evidence/result; green_required: yes; prs_required: no; owner_boundary: live publication; security_disposition: PENDING.

### C-AU-03 — disclosure/claim safety
- status: PENDING; anchor: AU content model; objective: ensure reward ranges and eligibility are evidence-bound; acceptance: no guaranteed-income or unsupported approval claim; dependencies: C-AU-01; safe boundary: content tests/docs; verification: claim-source matrix; next handoff: Marketing.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: internal content; negative_tests: guaranteed earnings, stale reward, publisher claim; receipt_evidence: claim/source/date; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## Affiliate UK

### C-UK-01 — UK rewards/network evidence mini-batch
- status: PENDING; anchor: `Affiliate-Websites@d3cf400...`, UK workstream; objective: 2–5 reputable reward/paid-participation candidates with first-party UK eligibility and Awin/CJ/Impact/Webgains/Tradedoubler route where relevant; acceptance: account acceptance and attribution remain separate evidence; dependencies: Master contract; safe boundary: research; verification: first-party source/date; next handoff: UK model.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research; negative_tests: network presence≠approval, stale terms, UK unavailable; receipt_evidence: source/date/route/status; green_required: no; prs_required: no; owner_boundary: signup/contact/publication; security_disposition: PENDING.

### C-UK-02 — conservative compliance/claim fixtures
- status: PENDING; anchor: UK model; objective: 2–5 financial/regulatory/earning-claim negatives; acceptance: uncertainty => HOLD and no guaranteed-income claim; dependencies: C-UK-01; safe boundary: tests/content rules; verification: deterministic outcomes; next handoff: UK Overseer.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: tests; negative_tests: guaranteed income, financial promotion uncertainty, disclosure absent; receipt_evidence: claim/evidence/disposition; green_required: yes; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

### C-UK-03 — destination/attribution separation
- status: PENDING; anchor: Master CTA contract; objective: ensure programme URL, member referral and publisher tracking route cannot substitute for one another; acceptance: unsupported path => fallback/HOLD; dependencies: C-UK-01; safe boundary: fixtures; verification: route-conflict matrix; next handoff: Master.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: fixture write; negative_tests: member link as publisher, wrong country, expired attribution; receipt_evidence: route/source/result; green_required: yes; prs_required: no; owner_boundary: live CTA; security_disposition: PENDING.

## Affiliate US

### C-US-01 — US paid-participation evidence mini-batch
- status: ACTIVE; anchor: Affiliate US PR #6 + `Overseer#49/5669064204`; objective: 2–5 user-testing/focus-group/survey/reward candidates with separate reward value and publisher eligibility evidence; acceptance: country availability/terms/freshness exact; dependencies: PR #6 owner; safe boundary: research/data; verification: first-party source/date; next handoff: US PR owner.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: research; negative_tests: reward≠publisher approval, stale terms, US unavailable; receipt_evidence: source/date/reward/route; green_required: no; prs_required: no; owner_boundary: signup/contact/publication; security_disposition: ACTIVE.

### C-US-02 — eligibility/publisher conflict fixtures
- status: PENDING; anchor: PR #6 current schema; objective: 2–5 cases where user eligibility exists but publisher/referral authority is absent/expired; acceptance: no monetized CTA; dependencies: C-US-01; safe boundary: tests; verification: exact-head CI; next handoff: US Overseer.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: tests; negative_tests: user-only eligibility, expired publisher terms, wrong destination; receipt_evidence: evidence/result; green_required: yes; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

### C-US-03 — claim-safe reward presentation
- status: PENDING; anchor: US content model; objective: evidence-bound reward ranges without guaranteed earnings; acceptance: source/freshness visible and UNKNOWN values not promoted; dependencies: C-US-01; safe boundary: internal content/tests; verification: claim-source matrix; next handoff: Marketing.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: internal content; negative_tests: guaranteed earning, stale reward; receipt_evidence: claim/source/date; green_required: no; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## GhostKitchen

### C-GK-01 — exact-head CI closure
- status: ACTIVE; anchor: PR #32 `316ade476804a5e3dcdef8e8f986a2ca3de431cb`, project receipt `GhostKitchen#31/5669049666`; objective: obtain exact-head verification for five new fail-closed security negatives; acceptance: CI emitted and green without weakening HYPOTHESIS/PUBLIC_REFERENCE boundaries; dependencies: current PR workflow; safe boundary: CI trigger/repair only, no deployment; verification: exact-head checks; next handoff: C-GK-02.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-12,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: scoped branch/test write; negative_tests: source-note authority injection, public-reference promotion, scenario/batch publication authority, unknown-delivery override; receipt_evidence: head/run/test result; green_required: yes; prs_required: no; owner_boundary: supplier/partner contact/spend/production; security_disposition: ACTIVE.

### C-GK-02 — provenance-labelled economics mini-batch
- status: PENDING; anchor: PR #32 existing economics seam; objective: 2–5 homogeneous representative-order records using only traceable evidence; acceptance: cost/yield/labour/packaging/delivery fields labelled VERIFIED/HYPOTHESIS/PUBLIC_REFERENCE/UNKNOWN; dependencies: C-GK-01 clean CI; safe boundary: fixtures/data; verification: schema + arithmetic tests; next handoff: GK Overseer.
- security_gates: `SG-06,SG-07,SG-10,SG-12,SG-14,SG-20`; risk_class: S2; authority_required: non-production data write; negative_tests: unknown override, mixed provenance, profitability claim from hypothesis; receipt_evidence: inputs/source/type/result; green_required: yes; prs_required: no; owner_boundary: spend/contact; security_disposition: PENDING.

### C-GK-03 — contribution sensitivity packet
- status: PENDING; anchor: C-GK-02; objective: bounded sensitivity analysis for delivery/labour/packaging ranges without asserting profitability; acceptance: material UNKNOWNs preserved; dependencies: evidence records; safe boundary: analysis artifact; verification: deterministic recalculation; next handoff: Commercial review.
- security_gates: `SG-06,SG-10,SG-12,SG-14`; risk_class: S1; authority_required: analysis; negative_tests: missing input, optimistic default; receipt_evidence: scenario inputs/version/output; green_required: no; prs_required: no; owner_boundary: commercial activation; security_disposition: PENDING.

## Franchise

### C-FR-01 — tenancy prerequisite closure
- status: BLOCKED; anchor: `Franchise main@0ea3b26de71f78f7eafc38cf50079805b43a7d93`, PR #24 duplicate-membership seam, PR #22 territory fixtures; objective: prove persistent membership/tenant isolation before territory widening; acceptance: A/B tenant isolation + duplicate active membership fail closed; dependencies: active PR ownership; safe boundary: non-production tests/data; verification: exact-head CI; next handoff: C-FR-02.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-12,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: scoped branch/test write; negative_tests: duplicate active membership, cross-tenant request/context, stale membership; receipt_evidence: tenant/membership/request/result; green_required: yes; prs_required: no; owner_boundary: production tenancy/partner action; security_disposition: BLOCKED.

### C-FR-02 — request-context/persistence isolation
- status: PENDING; anchor: PR #24/#22; objective: 2–5 homogeneous A/B persistence/request-context negatives once C-FR-01 lineage stabilises; acceptance: no cross-tenant bleed; dependencies: C-FR-01; safe boundary: tests; verification: exact-head CI; next handoff: Franchise Overseer.
- security_gates: `SG-06,SG-07,SG-10,SG-12,SG-14`; risk_class: S2; authority_required: test write; negative_tests: cross-tenant read/write, stale context, replayed tenant identity; receipt_evidence: tenant/context/result; green_required: yes; prs_required: no; owner_boundary: production; security_disposition: PENDING.

### C-FR-03 — territory overlap routing fixtures
- status: PENDING; anchor: PR #22 territory model; objective: only after tenancy proof, run 2–5 duplicate/overlap/version-correlation cases; acceptance: ambiguous territory fails closed deterministically; dependencies: C-FR-01/02; safe boundary: synthetic fixtures; verification: exact-head CI; next handoff: Franchise Overseer.
- security_gates: `SG-06,SG-10,SG-12,SG-14,SG-20`; risk_class: S2; authority_required: fixture write; negative_tests: duplicate/overlap/stale version; receipt_evidence: tenant/territory/version/result; green_required: yes; prs_required: no; owner_boundary: live routing; security_disposition: PENDING.

## GemVerse

### C-GV-01 — recovery evidence tamper baseline
- status: VERIFIED; anchor: PR #10 `b6b4bb4def2eb6a244671afe17a7670075249205`, run `34883530631` SUCCESS, GemVerse #9 `5669052070`; objective: preserve chosen-state/correlation/current-hash/secret-shaped evidence denial; acceptance: exact existing fixtures remain green; dependencies: none; safe boundary: fixture-only; verification: exact-head CI; next handoff: C-GV-02.
- security_gates: `SG-05,SG-10,SG-14`; risk_class: S2; authority_required: fixture tests; negative_tests: existing four tamper cases; receipt_evidence: head/run/fixture; green_required: yes if widened; prs_required: no; owner_boundary: canon/runtime/production; security_disposition: VERIFIED_BOUNDED.

### C-GV-02 — replay/ambiguous-candidate/result mismatch pack
- status: PENDING; anchor: PR #10 current recovery schema; objective: 2–5 fixture-only negatives for replay, competing candidate identity, stale target/preimage and result mismatch; acceptance: no chosen state without exact evidence; dependencies: C-GV-01; safe boundary: fixtures/tests only; verification: exact-head CI; next handoff: GemVerse Overseer.
- security_gates: `SG-05,SG-06,SG-07,SG-09,SG-10,SG-12,SG-14`; risk_class: S2; authority_required: fixture write; negative_tests: replay, competing candidate, stale target, result mismatch; receipt_evidence: preimage/target/candidate/result IDs; green_required: yes; prs_required: no; owner_boundary: canon/runtime mutation; security_disposition: PENDING.

### C-GV-03 — canon-dependent execution gate
- status: BLOCKED; anchor: current docs/fixture lineage only; objective: prevent documentation/fixtures from being treated as executable implementation or canon; acceptance: executable work requires verified canon + implementation evidence; dependencies: external canon source; safe boundary: policy/test assertion; verification: evidence review; next handoff: owner/project when canon exists.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-20`; risk_class: S1; authority_required: read-only; negative_tests: docs-as-runtime, model-selected canon; receipt_evidence: canon source/version; green_required: no; prs_required: no; owner_boundary: canon authority; security_disposition: BLOCKED.

## Content360

### C-C360-01 — exact-head verification-system closure
- status: ACTIVE; anchor: PR #4 `b2c3b222ef06f98951b20312591b7af65c7ac952`, current exact-head check-runs/workflow-runs `0`, Content360 #3 `5669054216`; objective: diagnose/route missing PR workflow trigger before stacking new capability; acceptance: exact head receives adapter/secret/provenance/optimisation suite result; dependencies: existing workflow; safe boundary: workflow/test repair only; verification: exact-head run; next handoff: C-C360-02.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: scoped workflow/test write; negative_tests: no predecessor CI inheritance, secret leak, malformed provenance; receipt_evidence: exact head/run/suite; green_required: yes; prs_required: no; owner_boundary: credentials/network/publish/schedule; security_disposition: ACTIVE.

### C-C360-02 — provider/result integrity mini-batch
- status: PENDING; anchor: PR #4 current adapter; objective: after C-C360-01, add 2–5 homogeneous provider-neutral correlation/idempotency/malformed-result negatives; acceptance: external/provider output cannot grant authority or widen claim evidence class; dependencies: clean exact-head CI; safe boundary: mock tests; verification: exact-head CI; next handoff: Content360 Overseer.
- security_gates: `SG-05,SG-06,SG-07,SG-09,SG-10,SG-14,SG-15`; risk_class: S2; authority_required: test write; negative_tests: provider substitution, malformed response, correlation mismatch, duplicate result; receipt_evidence: request/provider/result/disposition; green_required: yes; prs_required: no; owner_boundary: credentials/live network/PUBLISH/SCHEDULE; security_disposition: PENDING.

### C-C360-03 — READ/OPTIMISE authority boundary
- status: PENDING; anchor: current adapter capability contract; objective: prove optimise cannot silently become publish/schedule/account mutation; acceptance: unsupported capability denied and opaque credentials never exposed; dependencies: C-C360-01; safe boundary: mocks/tests; verification: capability-denial suite; next handoff: Marketing handoff package.
- security_gates: `SG-03,SG-05,SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S2; authority_required: mock tests; negative_tests: optimise->publish, schedule, account mutation, secret exposure; receipt_evidence: requested/allowed capability + result; green_required: yes; prs_required: no; owner_boundary: credentials/live actions; security_disposition: PENDING.

## Commercial Frontend

### C-CF-01 — Tradie operator evidence packet
- status: PENDING; anchor: `Overseer` commercial-frontend workstream; portfolio state `Overseer#49/5669064204`; objective: collect 2–5 direct evidence points for invoice-closure frequency, minutes/case, consequence, authority and willingness-to-pay; acceptance: source/date/operator context and UNKNOWNs explicit; dependencies: public/available non-contact evidence; safe boundary: research synthesis; verification: source triangulation; next handoff: Commercial Frontend Overseer.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public research; negative_tests: synthetic feasibility as demand, unsupported WTP claim; receipt_evidence: source/date/metric/confidence; green_required: no; prs_required: no; owner_boundary: customer contact/deploy; security_disposition: PENDING.

### C-CF-02 — exception workflow evidence schema
- status: PENDING; anchor: same workstream; objective: encode operator-visible evidence packet + bounded correction + receipt fields without production integration; acceptance: correction authority explicit and every state transition attributable; dependencies: C-CF-01; safe boundary: docs/fixtures/prototype; verification: scenario fixtures; next handoff: prototype owner.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-12,SG-14,SG-15`; risk_class: S2; authority_required: non-production artifact write; negative_tests: unsupported correction, missing evidence, over-broad scope; receipt_evidence: case/input/evidence/action/result; green_required: yes; prs_required: no; owner_boundary: customer/account mutation; security_disposition: PENDING.

### C-CF-03 — integration feasibility boundary
- status: PENDING; anchor: existing Xero-paid-invoice feasibility evidence; objective: separate documented integration capability from production/customer authority; acceptance: no build-gate promotion from API existence alone; dependencies: C-CF-01; safe boundary: research/docs; verification: capability-vs-authority matrix; next handoff: Overseer.
- security_gates: `SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: S1; authority_required: public/read-only research; negative_tests: API availability=>customer authority, sandbox=>production; receipt_evidence: integration/source/authority status; green_required: no; prs_required: no; owner_boundary: deploy/customer access; security_disposition: PENDING.

## Marketing

### C-MKT-01 — evidence-bound claims ladder refresh
- status: ACTIVE; anchor: current AgentOS/GlobalShopCo/Affiliate evidence + `Overseer#49/5669064204`; objective: keep internal claims mapped to VERIFIED/HYPOTHESIS/HOLD classes; acceptance: no eBay-ready SKU, partner, conversion or production-readiness claim beyond evidence; dependencies: current project evidence; safe boundary: internal copy/docs; verification: claim-source table; next handoff: Content360 optimisation only.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: internal content creation; negative_tests: claim-class widening, unsupported partner/readiness claim; receipt_evidence: claim/source/evidence class; green_required: no; prs_required: no; owner_boundary: campaign activation/spend/outreach/publication; security_disposition: ACTIVE.

### C-MKT-02 — Content360-ready non-public packages
- status: PENDING; anchor: C-MKT-01 + Content360 READ/OPTIMISE boundary; objective: prepare 2–5 homogeneous internal content packages with immutable source/evidence class metadata; acceptance: optimiser may improve presentation but cannot widen evidence class; dependencies: C-C360-03 contract; safe boundary: draft content only; verification: before/after claim-class diff; next handoff: Content360.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: internal content; negative_tests: optimiser invents partner/performance claim, strips disclosure; receipt_evidence: source package/output/evidence-class diff; green_required: no; prs_required: no; owner_boundary: live publish/schedule; security_disposition: PENDING.

### C-MKT-03 — objection/proof asset mini-batch
- status: PENDING; anchor: AgentOS current bounded capability evidence; objective: 2–5 non-paid educational/proof assets using only evidenced features and explicit limitations; acceptance: no overall GREEN or unsupported compatibility/conversion claim; dependencies: claims ladder; safe boundary: internal draft; verification: evidence citation audit; next handoff: owner/content review.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: S1; authority_required: internal content; negative_tests: unsupported capability, partner, conversion, readiness claim; receipt_evidence: asset/claim/source; green_required: no; prs_required: no; owner_boundary: publication/campaign/spend; security_disposition: PENDING.

## Replenishment health
- Lane A: multiple safe PENDING items exist despite SG-08/SG-01/02/physical blockers; current-head CI repair is highest safe action.
- Lane B: GlobalShopCo evidence closure, eBay upstream durability discovery, Amazon fixture negatives and MyPrime identity/presentation work remain actionable; live commercial/publication actions remain blocked.
- Lane C: every scheduled workstream has at least one actionable item or explicit blocker; active PR ownership is preserved and no duplicate implementation is assigned.
- Repeatedly VERIFIED scopes widen only into 2–5 homogeneous adjacent items and never across confidence classes.

**No overall GREEN.**