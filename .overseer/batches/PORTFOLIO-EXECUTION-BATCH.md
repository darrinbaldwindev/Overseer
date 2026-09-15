# Portfolio Execution Batch Manifest

Canonical engine: `.overseer/doctrine/PORTFOLIO-BATCH-ENGINE.md`; profiles: `.overseer/profiles/PROJECT-BATCH-PROFILES.md`; security: `.overseer/security/AGENTOS-SECURITY-GATE-MATRIX.md`. Repository/runtime/CI evidence outranks this queue.

**Scheduled scope only:** AgentOS, PRS, GlobalShopCo, GlobalShopCo-Headless, shopify_ebay, MyPrimeDelivery. All other portfolio workstreams remain owner-manual and are not scheduled or consumed here.

**Invariant:** **NO MODEL DECIDES ITS OWN AUTHORITY.** No merge/approve/ready/rebase/deploy/credentials/security-policy changes/production writes/purchases/spend/supplier contact/live publication/physical owner-host action/production autonomy. Functional, security, Green and PRS status remain independent.

## Checkpoint reconciliation — 2026-09-15 12:30 Brisbane
- **AgentOS:** #104 unchanged exact `4c8bcc3bc2ad2041b0a1871d3004c1db23f3c091`, OPEN/DRAFT/UNMERGED; SG-08 and SG-01/02 remain BLOCKED_STABLE. #112 unchanged exact `d1645450a06d00c49a7a78f176e97b44b9eaa225`, independently ACTIVE and outside #104 mutation ownership.
- **PRS:** #24 remains exact `3039c886bdcff911f7c6dcc3e086368058e57fb6`; completion-grade assurance remains BLOCKED_STABLE pending repaired AgentOS head plus identical-head Jess functional PASS, Michael security PASS, then PRS. Historical #17 is baseline only.
- **GlobalShopCo:** #29 `15fa99eb4c4b1f96127f6f51c412cbffc94e45e2` / #30 `80c82475b98663d677885e8b4d222ae2cedb8555` unchanged; authenticated cost+freight+permission+stock evidence remains absent and `0 eBay-ready SKUs` remains controlling.
- **GlobalShopCo-Headless — CHANGED / VERIFIED USEFUL MOVEMENT:** PR #1 advanced from `9107ca283cf20b4bb79a4c25eaf1d4340b269e04` to exact `c3f4939f1b7de8ef6e7fe6547400343dbb076348`; commit `test: reject malformed configured checkout authorities`; exact-head Actions run `34920523147`, job `104227407074`, `validate` SUCCESS. Malformed configured checkout authority values (userinfo, path, port, host-confusion and leading-space forms) now fail closed in bounded non-production tests. No live checkout/deploy authority.
- **shopify_ebay:** default remains `c68883f24fb3711fce567a35b1a80db74933b82a`; canonical durable replay owner remains BLOCKED_STABLE. No local persistence plane is authorized.
- **MyPrimeDelivery:** research `61feceb46de539948374deec86b3fe7578cf8014` and WordPress fixture `a38684c10541115f55f1d5612b72d669dced99f0` remain deliberately divergent from merge base `3635c903214b06464e28674d5a6403f8539b8c1e`; compatibility mapping remains prerequisite; live `QUALIFIED=0`.

# AgentOS — Level 2 P0

### A-AG-01 continuous ownership fence — BLOCKED_STABLE
Anchor `AgentOS#104@4c8bcc3bc2ad2041b0a1871d3004c1db23f3c091`. Objective: one crash-releasing ownership fence held continuously through final verification -> side effect/prepared recovery -> durable success receipt -> release. Acceptance: replacement/successor/three-writer/TOCTOU/crash/replay/prepared-recovery negatives deny false success with exact-head Ubuntu+Windows CI. Next: only existing #104 owner may implement the smallest repair on the existing writer seam; no competing lock/ledger. Security `SG-03,08,09,10,11,14,18,19`; S2; Green=yes; PRS=yes after identical-head Green; merge/deploy/physical/production owner-only.

### A-AG-02 authenticated actor + canonical grant — BLOCKED_STABLE
Anchor `#104@4c8bcc3...`. Dependency: real existing authenticated identity source and canonical grant resolver not evidenced. Acceptance: absent/spoofed/mismatch/cross-project/replay denies with exact issuer/source/version/request/task/mission provenance. Next: none until source evidence changes; fall through. Security `SG-01,02,03,04,09,10,11,18,19`; S2; credentials/security-policy owner-only; Green/PRS required for promotion.

### A-AG-03 runtime-shell eligibility consolidation — ACTIVE
Anchor `AgentOS#112@d1645450a06d00c49a7a78f176e97b44b9eaa225`. Objective: one canonical normalization/evaluation path without authority widening. Acceptance: deterministic aliases, compatibility adapter reuse, asserted eligibility without canonical result denied, adjacent unauthorized capability denied; exact-head CI. Next: inventory uncovered evaluator/alias negatives and implement only 2–5 homogeneous gaps. Security `SG-02,03,04,10,18`; S2; branch/tests only; Green for promotion; no merge/deploy/production.

### A-AG-04 replay/correlation slice — SPLIT_REQUIRED
Anchor current #104 lineage. Objective: close genuinely uncovered replay/correlation cases without touching A-AG-01 ownership repair. Acceptance: first-write provenance retained; conflicting same identity, duplicate result and restart duplicate fail closed. Next: inventory coverage, select 2–5 homogeneous gaps, test exact head. Security `SG-09,10,11,14,18`; S2; no new persistence/authority plane.

### A-AG-05 physical Windows acceptance — BLOCKED_STABLE
Dependency repaired #104 + A-AG-02 + Jess/Michael + PRS + owner physical authority. Next: none; preserve owner-run evidence contract. Security `SG-03,08,10,11,14,18,20`; S2; owner-only physical action.

# PRS — independent assurance

### A-PRS-01 historical false-GREEN baseline — VERIFIED
Anchor `PRS#17@49fe1f8bca3ddae271d85e0f4767173060267222`. Immutable historical defect evidence only; never successor certification. Security `SG-01,02,08,10,11,19`; S0.

### A-PRS-02 changed-head bounded challenge — PENDING
Target only a changed AgentOS #104 lineage. Objective: independently challenge replay/correlation/receipt ordering and defect-baseline behavior. Acceptance: immutable exact target/artifact hashes plus independent outcomes. Next: skip while #104 remains unchanged; automatically reopen on changed target/evidence. Security `SG-08,09,10,11,19`; S1; read/harness only.

### A-PRS-03 completion-grade ownership challenge — BLOCKED_STABLE
Anchor `PRS#24@3039c886bdcff911f7c6dcc3e086368058e57fb6` plus future repaired AgentOS head. Acceptance: identical-head Jess functional PASS + Michael security PASS first, then independent normal/prepared/successor/crash/replay matrix. Next: none until prerequisites change. Security `SG-08,09,10,11,18,19`; S2; Green prerequisite.

### A-PRS-04 physical evidence-contract negatives — PENDING
Anchor `PRS#24@3039c886...`. Objective: reject stale/missing/mismatched AgentOS head, host/root, mutation/recovery/correlation or artifact identity. Next: add only missing contract-negative fixtures; no physical execution. Security `SG-10,11,19,20`; S1; owner physical host.

# GlobalShopCo

### B-GSC-01 authenticated supplier evidence closure — ACTIVE
Anchors `#29@15fa99eb...`, `#30@80c82475...`. Objective: close exact SKU rows only with authenticated trade cost, packaged freight/free-delivery basis, permission, stock identity, returns/warranty. Acceptance: source/date/SKU/cost/freight/status traceable; missing material field => HOLD. Next: process only newly available authenticated evidence; no repeated public rediscovery. Security `SG-02,06,10,12,13,14,15,20`; S1; read-only; contact/purchase/Shopify mutation owner-only.

### B-GSC-02 conservative delivered-margin gate — PENDING
Dependency evidence-complete B-GSC-01 row. Acceptance: fees/freight/returns allowance explicit; unknown/stale/negative economics => HOLD. Next: calculate only when a row becomes evidence-complete. Security `SG-10,12,13,14,20`; S1; non-production calculation.

### B-GSC-03 bounded eBay shortlist — BLOCKED_STABLE
Anchor `0 eBay-ready SKUs`. Dependency B-GSC-01/02. Next: none until an exact variant has permission+stock+delivered economics+returns/warranty. Security `SG-02,06,10,12,13,14,15,20`; S1; publication/contact/spend owner-only.

### B-GSC-04 compact AU-stock evidence mini-batch — PENDING
Objective: 2–5 compact/light candidates only where authenticated evidence routes exist. Acceptance: exact identity, supplier provenance, freight, permission, stock, returns captured or HOLD. Next: one homogeneous mini-batch; stop when sources remain retail/syndicated only. Security `SG-06,10,12,13,14,15,20`; S1; research only.

# GlobalShopCo-Headless

### B-HDL-01 configured Shopify store authority — VERIFIED
Anchor predecessor/current lineage through `#1@c3f4939f1b7de8ef6e7fe6547400343dbb076348`; pre-request configured store authority remains fail-closed. Current exact-head `validate` SUCCESS `34920523147` / `104227407074`. Security `SG-02,05,06,10,14,20`; S1; non-production only.

### B-HDL-02 malformed configured checkout authority — VERIFIED
Anchor `#1@c3f4939f1b7de8ef6e7fe6547400343dbb076348`, commit `test: reject malformed configured checkout authorities`, Actions `34920523147` SUCCESS. Acceptance evidenced for configured checkout userinfo/path/port/host-confusion/leading-space denial plus canonical configured host acceptance and alternate destination denial. No live checkout inference. Security `SG-02,06,10,14,20`; S1; tests only; deploy/live purchase owner-only.

### B-HDL-03 canonical checkout projection — PENDING
Anchor `#1@c3f4939...`. Objective: prove WordPress cannot become order/payment authority. Acceptance: canonical Shopify checkout destination only; no local payment/order mutation; alternate host/local-order negatives fail closed. Next: inventory current tests, then add only 2–5 uncovered authority-boundary cases. Security `SG-02,05,06,10,14,20`; S1; tests/docs only.

### B-HDL-04 product identity/availability contradictions — PENDING
Anchor current M3 contract `c3f4939...`. Objective: stale/mismatched product/variant/availability cannot form checkout payload. Next: add 2–5 homogeneous uncovered variant mismatch/stale availability/duplicate cart identity fixtures; exact-head CI. Security `SG-06,09,10,14`; S1; synthetic only.

### B-HDL-05 non-production dev-store/browser acceptance — BLOCKED_STABLE
Dependency genuine dev-store/browser evidence plus owner-authorized credentials/environment. Next: none; fall through to deterministic tests. Security `SG-05,10,14,20`; S2; credentials/deploy/live purchase owner-only.

# shopify_ebay

### B-EBAY-01 upstream durable replay owner — BLOCKED_STABLE
Anchor default `c68883f24fb3711fce567a35b1a80db74933b82a`. Acceptance requires an evidenced existing canonical upstream owner/source/schema/lifecycle; caller-supplied seen IDs are not durability. Next: none until topology/source changes. Security `SG-02,09,10,11,14`; S1; no new ledger/persistence.

### B-EBAY-02 restart replay durability negatives — BLOCKED
Dependency B-EBAY-01. Objective: restart duplicate/conflict/result-write replay preserves first-write provenance. Next: none until canonical store exists. Security `SG-09,10,11,14`; S2; synthetic only after dependency.

### B-EBAY-03 evidence-complete SKU admission — BLOCKED_STABLE
Anchor `c68883f...` + GlobalShopCo `0 eBay-ready SKUs`. Next: none until a real evidence-complete Shopify variant exists. Security `SG-02,06,10,12,13,14,15,20`; S1; network/listing/spend owner-only.

### B-EBAY-04 synthetic mapper identity regression — PENDING
Anchor `c68883f...`. Objective: exact variant/SKU/event mapping under malformed/duplicate inputs. Next: inventory existing mapper tests and implement only 2–5 uncovered homogeneous variant mismatch/malformed-ID/conflicting-hash cases; fixture CI. Security `SG-06,09,10,14`; S1; no live API/publication.

# MyPrimeDelivery

### B-MPD-01 divergent-lineage compatibility map — ACTIVE
Anchors research `61feceb46de539948374deec86b3fe7578cf8014`, fixture `a38684c10541115f55f1d5612b72d669dced99f0`, merge base `3635c903214b06464e28674d5a6403f8539b8c1e`. Objective: exact path/contract compatibility map before integration; no stale overwrite/merge/rebase. Acceptance: explicit compatible/conflicting/fixture-only classifications. Next: identify smallest presentation-contract port that does not import stale fixture assumptions. Security `SG-10,11,14,20`; S1; read/docs/tests.

### B-MPD-02 authoritative source/right-to-use evidence — PENDING
Anchor research `61feceb...`; truth `0 live QUALIFIED`. Acceptance: one coherent observation carries exact ASIN + current product-level Prime + owner-approved rank/deal freshness + source rights + outbound destination; editorial/public pages never become authority. Next: process only newly available authorized evidence. Security `SG-02,06,10,12,14,15,20`; S1; signup/credentials/publication owner-only.

### B-MPD-03 coherent qualification baseline — VERIFIED
Anchor research `61feceb...`; preserve one-observation coherence and conflicting-known-ASIN denial. Next: only genuinely uncovered contradictions. Security `SG-06,09,10,14`; S1.

### B-MPD-04 WordPress non-production presentation adapter — PENDING
Dependency B-MPD-01. Objective: render only QUALIFIED fixture data without inventing Prime/rank/deal authority. Acceptance: HOLD/UNKNOWN never emits monetized/live CTA; outbound destination exact; no secret leakage. Next: after compatibility map, port only compatible presentation contract into bounded fixture/tests. Security `SG-05,06,10,14,15,20`; S2; Green if promoted; credentials/publication owner-only.

### B-MPD-05 freshness/identity contradiction mini-batch — PENDING
Anchor research `61feceb...`. Objective: 2–5 uncovered homogeneous stale Prime/rank/deal or identity/outbound contradictions fail closed. Next: inventory validator coverage, add only genuine gaps, exact-head fixture CI. Security `SG-06,09,10,14`; S1; tests only.

## Execution order / starvation control
1. AgentOS A-AG-01 remains P0 but its stable blocker must not starve independent #112 and replay/correlation slices.
2. PRS runs only on changed AgentOS lineage; no repeated certification of unchanged #104.
3. Headless has fresh VERIFIED movement at `c3f4939...`; consume B-HDL-03/04 adjacent deterministic slices next while confidence class remains homogeneous.
4. GlobalShopCo processes new authenticated evidence only; `0 eBay-ready SKUs` remains truth.
5. shopify_ebay falls through to mapper regressions while persistence/SKU blockers remain stable; never create persistence.
6. MyPrimeDelivery completes compatibility mapping before presentation work; live qualification authority remains fail-closed.

**No overall GREEN. Scheduled work outside these six projects remains untouched.**