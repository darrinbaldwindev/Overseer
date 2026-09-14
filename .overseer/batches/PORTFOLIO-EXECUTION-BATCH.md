# Portfolio Execution Batch Manifest

**Purpose:** deep bounded execution queue for the existing scheduled portfolio lanes. Live repo/issue/CI/runtime evidence is authoritative. Scheduler firing and worker claims are never completion evidence.

**Fixed lanes:** A = AgentOS Level 2 P0 + PRS/Green assurance-adjacent; B = GlobalShopCo/Headless/eBay/Amazon/MyPrimeDelivery; C = Affiliate-Websites/GhostKitchen/Franchise/GemVerse/Content360/Commercial Frontend/Marketing.

**States:** `PENDING | ACTIVE | VERIFIED | BLOCKED | STALE | SPLIT_REQUIRED`.

**Hard boundary:** no merge/approve/ready/rebase/deploy/credentials/production writes/purchases/supplier contact/live publication/production autonomy. Core invariant: **NO MODEL DECIDES ITS OWN AUTHORITY.**

**Security:** functional and security disposition remain independent. Applicable SG gates come from `.overseer/security/AGENTOS-SECURITY-GATE-MATRIX.md`.

# LANE A — AGENTOS LEVEL 2 P0

## AgentOS Overseer subqueue

### A-AG-01 — continuous project-file ownership primitive
- status: BLOCKED
- anchor: `darrinbaldwindev/AgentOS` PR #104 exact head `9f53df16ae37ee6a86e66d2a808ca7f62f203d76`; PRS defect reproduction PR #17 head `8479ae148694af24ae5a492036f3b5cd56fd8c5c`, run `34810516744` against AgentOS `71c463a77b31ebeac2bfe00da13c684512daccf7`.
- objective: replace the known check/release gap with one kernel-enforced/crash-releasing ownership boundary held through final verify -> publish/prepared recovery -> durable success receipt -> release.
- acceptance: replacement/successor writer cannot publish under stale ownership; success cannot persist before ownership-loss detection; crash releases safely; prepared recovery obeys same fence.
- dependencies: real production writer design change; no synthetic policy-only substitute.
- safe boundary: branch/code/tests only; no production mutation or merge.
- verification: exact-head Windows suite + cross-platform CI + SG-08 adversarial matrix + Green exact-head, then PRS exact-head.
- next handoff: AgentOS worker implements smallest primitive; Green challenges; PRS only after Green PASS on unchanged head.
- security_gates: `SG-03,SG-08,SG-09,SG-10,SG-11,SG-14,SG-18,SG-19`; risk_class: `S2`; authority_required: scoped non-production AgentOS branch/test writes; negative_tests: replacement-after-verification, successor-writer, stale identity, TOCTOU, crash/replay, duplicate result/mutation, prepared-recovery stale owner; receipt_evidence: exact actor/task/file/preimage/postimage/ownership/result lineage; green_required: yes; prs_required: yes; owner_boundary: merge/deploy/physical production action; security_disposition: BLOCKED.

### A-AG-02 — exact-head Windows CI failure closure
- status: ACTIVE
- anchor: PR #104 `9f53df16ae37ee6a86e66d2a808ca7f62f203d76`; AgentOS Tests run `34816222109` = FAILURE; Ubuntu/Node22 job `103887346619` PASS, Windows/Node26 job `103887346695` FAIL in test suite.
- objective: identify the exact failing Windows test(s), determine regression vs fixture/flakiness, make the smallest bounded fix, rerun exact-head CI.
- acceptance: Windows/Node26 and Ubuntu/Node22 both complete SUCCESS on the new exact head; no weakening/skipping of security assertions merely to green CI.
- dependencies: inspect failing job/log/test evidence first.
- safe boundary: tests/fixture/runtime correction only; no merge/deploy.
- verification: exact new head + workflow/job IDs + changed-test rationale.
- next handoff: if failure touches ownership, route to A-AG-01; otherwise close CI regression then resume A-AG-04.
- security_gates: `SG-08,SG-09,SG-10,SG-18`; risk_class: `S2`; authority_required: scoped branch/test changes; negative_tests: preserve fail-closed ownership/correlation assertions; receipt_evidence: exact failing/passing job IDs and commit; green_required: yes for promoted Level-2 scope; prs_required: only if security-relevant runtime semantics change; owner_boundary: merge/deploy; security_disposition: ACTIVE.

### A-AG-03 — canonical authenticated authority-admission producer
- status: BLOCKED
- anchor: PR #104 current exact `9f53df16ae37ee6a86e66d2a808ca7f62f203d76`; PR body still states authenticated transport + canonical grant lookup are unwired composition seams.
- objective: bind admission to an existing canonical authenticated actor identity and canonical grant source without adding a second authority registry or accepting self-grant request fields.
- acceptance: actor cannot be supplied/overridden by payload; grant provenance binds actor/project/scope; missing/mismatch lookup produces zero task/wake/result artifacts.
- dependencies: real existing authenticator/grant source must be evidenced as bindable.
- safe boundary: no new authority service, registry, scheduler, memory or persistence layer.
- verification: exact-head missing actor/spoof actor/no grant/grant mismatch/replay tests and durable provenance.
- next handoff: AgentOS architecture only when canonical source is identified; otherwise remain BLOCKED.
- security_gates: `SG-01,SG-02,SG-03,SG-04,SG-09,SG-10,SG-11,SG-18,SG-19`; risk_class: `S2`; authority_required: existing canonical identity/grant read plus scoped admission code change; negative_tests: spoofed actor, no grant, actor/project/scope mismatch, replay, stale correlation; receipt_evidence: grant issuer/source/version plus exact task/mission/request; green_required: yes; prs_required: yes; owner_boundary: credential/security-policy change; security_disposition: BLOCKED.

### A-AG-04 — authority/correlation preservation mini-batch
- status: PENDING
- anchor: PR #104 exact `9f53df16ae37ee6a86e66d2a808ca7f62f203d76`; predecessor authority regressions were green at `a4d1a1baa104d76ae7667d5e079df4ffe87688a0` / run `34811602354`, but current head CI is red.
- objective: after A-AG-02 restores CI, preserve exact delivery/request/task/mission/wake/actor/grant correlation and zero-artifact fail-closed behavior across adjacent code movement.
- acceptance: malformed/mismatched/stale IDs fail closed; rejected admission leaves no durable execution artifacts; no invented expiry/nonce semantics absent canonical contract.
- dependencies: A-AG-02 exact-head CI green.
- safe boundary: homogeneous regression tests only.
- verification: exact-head targeted tests + full CI.
- next handoff: Green sample; PRS only if authority semantics materially change.
- security_gates: `SG-01,SG-02,SG-09,SG-10,SG-11,SG-18`; risk_class: `S2`; authority_required: scoped test/code branch writes; negative_tests: correlation mismatch, stale delivery, replay, missing authority evidence; receipt_evidence: zero-artifact denial plus exact successful lineage; green_required: yes; prs_required: conditional; owner_boundary: merge/deploy; security_disposition: PENDING.

## PRS / Green assurance-adjacent subqueue

### A-PRS-01 — continuous-ownership defect baseline
- status: VERIFIED
- anchor: `darrinbaldwindev/PRS` PR #17 exact `8479ae148694af24ae5a492036f3b5cd56fd8c5c`; workflow `34810516744`; AgentOS target `71c463a77b31ebeac2bfe00da13c684512daccf7`; result `DEFECT_REPRODUCED` in normal publish + prepared recovery.
- objective: preserve immutable baseline evidence for comparison only.
- acceptance: no transfer of PASS/FAIL to later heads without rerun.
- dependencies: none.
- safe boundary: read-only evidence retention.
- verification: exact Git object + artifact identity already recorded.
- next handoff: feed A-AG-01 design and later exact-head rerun.
- security_gates: `SG-08,SG-10,SG-11,SG-19`; risk_class: `S0`; authority_required: read-only exact-object assurance; negative_tests: already executed stale-owner false-success cases; receipt_evidence: artifact ID/hash recorded in PR #17; green_required: no; prs_required: this is PRS evidence; owner_boundary: none; security_disposition: VERIFIED.

### A-PRS-02 — replacement primitive exact-head challenge
- status: BLOCKED
- anchor: PRS PR #17 `8479ae148694af24ae5a492036f3b5cd56fd8c5c`; AgentOS current PR #104 `9f53df16ae37ee6a86e66d2a808ca7f62f203d76` has no evidenced ownership primitive replacement and current CI is red.
- objective: rerun immutable ownership adversarial suite only after a real target writer change and Green PASS.
- acceptance: unchanged exact target from Green; normal and prepared recovery; no stale success; independent result classification.
- dependencies: A-AG-01 implemented, A-AG-02 CI green, Green exact-head PASS.
- safe boundary: PRS fixtures/harness only, no target implementation.
- verification: PRS run/artifact exact target SHA and source hashes.
- next handoff: Overseer reconciliation; if defect remains, route smallest target remediation to AgentOS.
- security_gates: `SG-08,SG-09,SG-10,SG-11,SG-19`; risk_class: `S2`; authority_required: read exact target + write bounded assurance fixtures/results; negative_tests: full ownership matrix; receipt_evidence: immutable target/tree/file hashes + artifact hash; green_required: yes prerequisite; prs_required: yes; owner_boundary: merge/deploy; security_disposition: BLOCKED.

### A-PRS-03 — admission false-GREEN challenge
- status: BLOCKED
- anchor: AgentOS PR #104 `9f53df16ae37ee6a86e66d2a808ca7f62f203d76`; admission canonical source remains unwired.
- objective: once A-AG-03 binds canonical identity/grant, independently prove payload cannot self-authorize and mismatched provenance cannot reach task/wake/mutation artifacts.
- acceptance: missing/spoofed actor, absent/mismatched grant, stale/replayed request and cross-project grant all deny with zero false success.
- dependencies: A-AG-03 implementation + Green exact-head PASS.
- safe boundary: assurance only.
- verification: exact target hashes + deterministic adversarial output.
- next handoff: Overseer state promotion only on independent PASS.
- security_gates: `SG-01,SG-02,SG-03,SG-09,SG-10,SG-11,SG-19`; risk_class: `S2`; authority_required: read target + bounded PRS harness writes; negative_tests: actor/grant provenance attacks; receipt_evidence: immutable exact target and denial receipts; green_required: yes prerequisite; prs_required: yes; owner_boundary: credentials/security policy; security_disposition: BLOCKED.

# LANE B — COMMERCE PRIORITY

## GlobalShopCo Overseer subqueue

### B-GSC-01 — next Home Organisation exact-SKU economics candidate
- status: PENDING
- anchor: `darrinbaldwindev/GlobalShopCo` issue #17 plus prior negative closure `V178-36336`: A$37.99 delivered supplier/public path vs A$34.95 exact free-shipping retail offer.
- objective: select a different compact Home Organisation candidate already evidenced in repo/public supplier material and build exact supplier/SKU, authorised acquisition evidence, AU retail comps, freight and free-delivery contribution.
- acceptance: every cost field sourced or explicit UNKNOWN; candidate is rejected if margin depends on unknown freight/permission.
- dependencies: public/repo evidence only; no supplier contact.
- safe boundary: research/docs/fixtures; no Shopify production write.
- verification: source URLs/dates + arithmetic + explicit confidence.
- next handoff: if positive, channel-specific eBay/Amazon gates separately; if negative, record reason and advance next candidate.
- security_gates: `SG-06,SG-10,SG-12,SG-13,SG-14,SG-20`; risk_class: `S1`; authority_required: public/read-only research + repo docs; negative_tests: missing freight, stale price, retail-vs-wholesale confusion, marketplace permission absent; receipt_evidence: exact SKU/source/date/cost table; green_required: no; prs_required: no; owner_boundary: supplier contact/purchase/production changes; security_disposition: PENDING.

### B-GSC-02 — supplier permission / blind-shipping evidence matrix
- status: PENDING
- anchor: GlobalShopCo issue #17 current classifications: Southern Pet/GiGwi `PERMISSION-REQUIRED`, Eleganter `NOT-ELIGIBLE` under recorded owned-site-only terms, NewDeals/Dropshipzone `UNKNOWN/HOLD`.
- objective: normalize existing public terms into per-supplier fields for eBay/Amazon permission, seller identity/packing, stock model, returns/warranty and buyer-data compatibility.
- acceptance: no ordinary dropship support is promoted to marketplace permission; unknown stays UNKNOWN.
- dependencies: public terms/repo evidence only.
- safe boundary: no supplier contact.
- verification: dated citations and deterministic status rules.
- next handoff: eBay/Amazon subqueues consume only exact supplier/SKU rows.
- security_gates: `SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: `S1`; authority_required: public research; negative_tests: ambiguous permission, stale terms, marketing prose as authority; receipt_evidence: supplier/status/source/date matrix; green_required: no; prs_required: no; owner_boundary: supplier contact/agreements; security_disposition: PENDING.

### B-GSC-03 — free-delivery contribution calculator fixture
- status: PENDING
- anchor: GlobalShopCo issue #17 and `V178-36336` negative economics baseline.
- objective: encode a non-production deterministic calculation fixture for landed cost + channel fee allowance + free delivery + target margin, with UNKNOWN propagation.
- acceptance: any unknown critical cost returns HOLD, never a positive margin; arithmetic is reproducible.
- dependencies: no production price write.
- safe boundary: fixtures/tests/docs only.
- verification: boundary cases around zero/negative contribution and missing freight.
- next handoff: use on future exact-SKU evidence rows.
- security_gates: `SG-10,SG-12,SG-13,SG-14`; risk_class: `S0`; authority_required: local fixture/test writes; negative_tests: missing freight, zero/negative price, omitted fees, duplicate fee; receipt_evidence: input hash/calculation/result; green_required: no; prs_required: no; owner_boundary: production pricing/purchase; security_disposition: PENDING.

## GlobalShopCo-Headless Overseer subqueue

### B-HDL-01 — production-code host normalization inspection
- status: PENDING
- anchor: `darrinbaldwindev/GlobalShopCo-Headless` M3 verified head `9799e6fe5a9c72e42e1554949697a64acce14bd4`; CI `34798624627` SUCCESS; issue #3.
- objective: inspect actual plugin checkout host parser/normalizer for case, trailing-dot, encoded/whitespace confusion before adding tests.
- acceptance: exact-host HTTPS rule is unambiguous; no parser ambiguity left undocumented.
- dependencies: stable exact head fresh-scan.
- safe boundary: read-only inspection first.
- verification: code-path citation + decision whether follow-on tests are applicable.
- next handoff: B-HDL-02/03 only for parser-supported cases.
- security_gates: `SG-03,SG-06,SG-10,SG-14`; risk_class: `S1`; authority_required: repo read; negative_tests: planned based on parser; receipt_evidence: exact file/head/path notes; green_required: no; prs_required: no; owner_boundary: production deploy/config; security_disposition: PENDING.

### B-HDL-02 — host-confusion negative fixtures
- status: PENDING
- anchor: same M3 head `9799e6fe5a9c72e42e1554949697a64acce14bd4` / run `34798624627`, dependent on B-HDL-01 applicability.
- objective: add homogeneous trailing-dot/case/encoded/whitespace negative fixtures only where parser semantics make them meaningful.
- acceptance: only canonical allowed Shopify host over HTTPS passes; confusion inputs fail closed without purchase action.
- dependencies: B-HDL-01.
- safe boundary: tests/non-production code only.
- verification: exact-head CI.
- next handoff: Green sample if checkout boundary code changes.
- security_gates: `SG-03,SG-10,SG-14,SG-18`; risk_class: `S2`; authority_required: scoped branch test/code change; negative_tests: applicable host-confusion cases; receipt_evidence: exact URL input/disposition; green_required: conditional yes if runtime boundary changes; prs_required: no unless higher-risk production boundary semantics change; owner_boundary: deploy/production Shopify; security_disposition: PENDING.

### B-HDL-03 — external dev-store/browser evidence packet
- status: BLOCKED
- anchor: issue #3; repo M3 code gate verified but external dev-store/browser proof remains UNKNOWN.
- objective: define exact evidence packet for owner-authorized future non-production browser proof without executing production writes.
- acceptance: test product identity, host, redirect/cart result, no secret leakage, timestamp/screenshots/logs and environment clearly marked non-production.
- dependencies: owner-authorized accessible dev/test environment if required.
- safe boundary: preparation only now.
- verification: checklist review; later browser evidence separate.
- next handoff: owner action only when physical/account access is necessary.
- security_gates: `SG-05,SG-10,SG-14,SG-20`; risk_class: `S2`; authority_required: non-production dev-store access; negative_tests: prod host/token denial; receipt_evidence: environment-bound evidence packet; green_required: yes for promotion; prs_required: no by default; owner_boundary: credentials/production access; security_disposition: BLOCKED.

## Shopify -> eBay Overseer subqueue

### B-EBY-01 — stale inventory event denial
- status: PENDING
- anchor: `darrinbaldwindev/shopify_ebay` branch `agent/chatgpt/ebay-mapper-receipts` head `b57e0a47bdff4b699d8b6b346fe5e9e1a0bbacc3`; fixture run `34805527804` SUCCESS; canonical commercial gate GlobalShopCo #17.
- objective: reject stale Shopify inventory events relative to newer canonical fixture evidence.
- acceptance: no eBay candidate side effect/network/publication; deterministic denial receipt.
- dependencies: synthetic only.
- safe boundary: no live connector/network/credentials.
- verification: unit fixture + exact-head CI.
- next handoff: same mini-batch B-EBY-02..04.
- security_gates: `SG-02,SG-03,SG-09,SG-10,SG-14,SG-15,SG-20`; risk_class: `S2`; authority_required: test branch writes only; negative_tests: stale event/newer source, replay; receipt_evidence: Shopify source IDs/event timestamp/input hash/denial; green_required: yes if adapter semantics widen; prs_required: no until production-capable path exists; owner_boundary: app connection/publication; security_disposition: PENDING.

### B-EBY-02 — out-of-order tracking event denial
- status: PENDING
- anchor: same `b57e0a47...` / `34805527804`.
- objective: prevent older tracking/fulfilment state from superseding newer canonical order state.
- acceptance: mismatch/out-of-order event denied deterministically; no alternate order state persisted.
- dependencies: synthetic fixtures.
- safe boundary: test only.
- verification: exact-head CI and deterministic receipts.
- next handoff: B-EBY-03.
- security_gates: `SG-09,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: branch tests; negative_tests: out-of-order/stale tracking, wrong order correlation; receipt_evidence: exact order/tracking lineage; green_required: conditional; prs_required: no; owner_boundary: live marketplace updates; security_disposition: PENDING.

### B-EBY-03 — duplicate order-import idempotency
- status: PENDING
- anchor: same `b57e0a47...` / `34805527804`.
- objective: repeated synthetic eBay order event yields one Shopify handoff candidate and duplicate-denial receipt.
- acceptance: no duplicate durable side-effect candidate.
- dependencies: synthetic only.
- safe boundary: no network.
- verification: duplicate/replay test.
- next handoff: B-EBY-04.
- security_gates: `SG-09,SG-10,SG-11,SG-14`; risk_class: `S2`; authority_required: branch tests; negative_tests: exact duplicate and semantically same event with reused correlation; receipt_evidence: idempotency key/source IDs/disposition; green_required: conditional; prs_required: no; owner_boundary: live Shopify/eBay write; security_disposition: PENDING.

### B-EBY-04 — correlation mismatch fail-closed
- status: PENDING
- anchor: same `b57e0a47...`; GlobalShopCo #17 still reports zero eBay-ready SKUs.
- objective: deny product/variant/order/tracking cross-correlation mismatches and preserve `publication_authority=false`, `network_io=false`.
- acceptance: all mismatches deny with zero publish/network path.
- dependencies: none beyond fixture branch.
- safe boundary: synthetic.
- verification: CI plus receipt assertions.
- next handoff: stop at commercial upstream gate; do not widen integration.
- security_gates: `SG-10,SG-14,SG-15,SG-20`; risk_class: `S2`; authority_required: test branch; negative_tests: variant/SKU/order/tracking mismatch; receipt_evidence: exact correlation values; green_required: conditional; prs_required: no; owner_boundary: publication/credentials; security_disposition: PENDING.

## Shopify -> Amazon Overseer subqueue

### B-AMZ-01 — seller-of-record evidence field
- status: PENDING
- anchor: `agent/chatgpt/amazon-au-preflight` head `84ab928ba1b95d0d763b69508bfa189cbf9e8a8d`; Amazon channel gate run `34813625619` SUCCESS.
- objective: add explicit seller-of-record evidence requirement to synthetic advisory fixture.
- acceptance: missing/ambiguous seller identity returns HOLD/DENY.
- dependencies: no live API.
- safe boundary: fixtures/docs/tests.
- verification: exact-head channel-gate CI.
- next handoff: B-AMZ-02..04.
- security_gates: `SG-02,SG-03,SG-10,SG-14,SG-20`; risk_class: `S2`; authority_required: branch fixture/test write; negative_tests: missing/ambiguous seller; receipt_evidence: evidence source/status; green_required: conditional; prs_required: no; owner_boundary: seller account/credentials/listing; security_disposition: PENDING.

### B-AMZ-02 — category/GTIN mismatch denials
- status: PENDING
- anchor: same `84ab928b...` / `34813625619`.
- objective: separate category ineligibility from unresolved GTIN/exemption status.
- acceptance: either unresolved field fails closed; no inference from product title/category guess.
- dependencies: synthetic data only.
- safe boundary: no marketplace calls.
- verification: deterministic fixtures.
- next handoff: B-AMZ-03.
- security_gates: `SG-06,SG-10,SG-14`; risk_class: `S2`; authority_required: test branch; negative_tests: category mismatch, GTIN missing, exemption claimed without evidence; receipt_evidence: exact evidence flags; green_required: conditional; prs_required: no; owner_boundary: Amazon account/listing; security_disposition: PENDING.

### B-AMZ-03 — fulfilment-model conflict
- status: PENDING
- anchor: same Amazon preflight gate; current supplier classifications remain PERMISSION-REQUIRED/UNKNOWN.
- objective: deny incompatible supplier fulfilment/marketplace model even when product identity/GTIN fields otherwise pass.
- acceptance: ordinary dropship evidence cannot authorize Amazon marketplace fulfilment.
- dependencies: existing supplier evidence only.
- safe boundary: synthetic/read-only.
- verification: fixture CI.
- next handoff: B-AMZ-04.
- security_gates: `SG-02,SG-06,SG-10,SG-14,SG-20`; risk_class: `S2`; authority_required: fixture tests; negative_tests: owned-site permission presented as Amazon permission; receipt_evidence: supplier/status source; green_required: conditional; prs_required: no; owner_boundary: supplier contact/listing; security_disposition: PENDING.

### B-AMZ-04 — stale/unsafe stock-sync evidence
- status: PENDING
- anchor: same `84ab928b...` / run `34813625619`.
- objective: fail closed on stale or insufficient Shopify-canonical stock-sync evidence.
- acceptance: no Amazon-ready classification without freshness/safety proof.
- dependencies: synthetic fixtures.
- safe boundary: no live channel adapter.
- verification: stale timestamp/version tests.
- next handoff: remain advisory-only until real commercial evidence exists.
- security_gates: `SG-09,SG-10,SG-14`; risk_class: `S2`; authority_required: test branch; negative_tests: stale stock evidence, mismatched variant; receipt_evidence: source identity/freshness/disposition; green_required: conditional; prs_required: no; owner_boundary: production stock/channel write; security_disposition: PENDING.

## MyPrimeDelivery Overseer subqueue

### B-MPD-01 — cross-tranche duplicate denial
- status: PENDING
- anchor: `darrinbaldwindev/MyPrimeDelivery` exact verified head `1820dfe1b5b8fe938c5fcd58e28858dc79b66e16`; fixture run `34811798266` SUCCESS; 40 research-only candidates/12 categories, `QUALIFIED=0`.
- objective: prevent duplicate ASIN/product candidate identity across research tranches.
- acceptance: deterministic duplicate rejection without upgrading qualification.
- dependencies: fixture data only.
- safe boundary: research/tests; no Amazon live API/publication.
- verification: fixture CI.
- next handoff: B-MPD-02.
- security_gates: `SG-06,SG-09,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: repo fixture/test writes; negative_tests: duplicate ID, conflicting duplicate metadata; receipt_evidence: candidate IDs/source/tranche/disposition; green_required: conditional; prs_required: no; owner_boundary: Associates credentials/publication; security_disposition: PENDING.

### B-MPD-02 — cumulative category-coverage verification
- status: PENDING
- anchor: same `1820dfe1...` / `34811798266`.
- objective: deterministically verify all 12 launch categories are represented while preserving research-only semantics.
- acceptance: missing/thin category identified explicitly; count alone never implies top/Prime/deal qualification.
- dependencies: current fixture set.
- safe boundary: local tests.
- verification: category coverage assertion.
- next handoff: B-MPD-03.
- security_gates: `SG-06,SG-10,SG-14`; risk_class: `S0`; authority_required: fixture tests; negative_tests: category alias/duplicate/missing category; receipt_evidence: category counts + candidate IDs; green_required: no; prs_required: no; owner_boundary: live publication; security_disposition: PENDING.

### B-MPD-03 — deterministic candidate ordering
- status: PENDING
- anchor: same exact verified head/run.
- objective: define deterministic research ordering based only on explicit fixture fields, never inferred sales rank/Prime status.
- acceptance: stable order for identical inputs; unsupported rank fields cannot influence qualification.
- dependencies: schema-supported fields only.
- safe boundary: tests/fixtures.
- verification: reorder/replay tests.
- next handoff: B-MPD-04.
- security_gates: `SG-06,SG-10,SG-14`; risk_class: `S0`; authority_required: local fixture changes; negative_tests: missing rank, stale public signal, conflicting source quality; receipt_evidence: sort inputs/order hash; green_required: no; prs_required: no; owner_boundary: live Amazon claims; security_disposition: PENDING.

### B-MPD-04 — thin-category research expansion
- status: PENDING
- anchor: same `1820dfe1...`; authorised live product/Prime/ranking/deal provider remains UNKNOWN.
- objective: add a small research-only tranche to the thinnest categories using allowed public discovery signals, clearly non-authoritative.
- acceptance: all new entries retain research-only status and cannot become `QUALIFIED` without canonical provider evidence.
- dependencies: public research only.
- safe boundary: no credentials/live API/affiliate publication.
- verification: source-quality hierarchy + fixture validator.
- next handoff: stop at provider/rights owner boundary.
- security_gates: `SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: `S1`; authority_required: public research + repo fixture docs; negative_tests: public editorial signal misrepresented as Prime/rank truth; receipt_evidence: URL/date/source-quality/candidate identity; green_required: no; prs_required: no; owner_boundary: provider subscription/credentials/publication; security_disposition: PENDING.

# LANE C — PRODUCT / CONTENT / VENTURES

## Affiliate-Websites Master subqueue

### C-AFF-M1 — publisher timestamp/future-evidence denial
- status: PENDING
- anchor: `darrinbaldwindev/Affiliate-Websites` previously verified CTA/program gate head `d901b3e2c0c772cdc43019dd96cf2b19bdded0a6`; CI `34798980244` SUCCESS.
- objective: reject publisher/program evidence dated in the future or outside accepted freshness semantics already supported by schema.
- acceptance: no CTA-ready result from impossible/future evidence.
- dependencies: fresh-scan country movement before touching shared surface.
- safe boundary: tests/fixtures only.
- verification: exact-head CI.
- next handoff: Master Overseer then country consumers.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: scoped branch test writes; negative_tests: future timestamp/stale evidence; receipt_evidence: program/publisher/source/time/disposition; green_required: conditional; prs_required: no; owner_boundary: live publication; security_disposition: PENDING.

### C-AFF-M2 — deterministic program identity ordering
- status: PENDING
- anchor: same `d901b3e...` / `34798980244`.
- objective: ensure duplicate/ambiguous program identities sort and resolve deterministically without silently swapping destination/tracking metadata.
- acceptance: ambiguity fails closed or deterministic canonical ID wins per existing contract.
- dependencies: stable head.
- safe boundary: fixtures/tests.
- verification: permutation/replay cases.
- next handoff: AU/UK/US use same master contract.
- security_gates: `SG-06,SG-07,SG-09,SG-10`; risk_class: `S2`; authority_required: test branch; negative_tests: duplicate IDs, conflicting destination/tracking; receipt_evidence: program IDs/input hash/order; green_required: conditional; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

### C-AFF-M3 — blocked destination/tracking stripping
- status: PENDING
- anchor: same verified CTA gate.
- objective: prove blocked/invalid programs cannot leak destination or tracking parameters into rendered/audit output.
- acceptance: blocked result is non-clickable and strips active outbound tracking surface.
- dependencies: existing renderer/audit contract.
- safe boundary: test-only.
- verification: rendered fixture assertions.
- next handoff: country-specific negative tests.
- security_gates: `SG-05,SG-06,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: test branch; negative_tests: blocked destination, malicious tracking query, mismatched country; receipt_evidence: sanitized output + reason; green_required: conditional; prs_required: no; owner_boundary: live site publication; security_disposition: PENDING.

## Affiliate-Websites AU subqueue

### C-AFF-AU1 — AU program-country mismatch fixture
- status: PENDING
- anchor: Master gate `d901b3e...` / `34798980244`; AU remains a country workstream under same repo contract.
- objective: deny CTA when evidence is UK/US-only or worldwide status is not proven for AU.
- acceptance: AU eligibility requires explicit AU/worldwide evidence.
- dependencies: fresh-scan AU paths.
- safe boundary: fixture/test only.
- verification: country mismatch cases.
- next handoff: AU Overseer records exact program evidence.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: AU fixture tests; negative_tests: UK-only/US-only/unknown-worldwide; receipt_evidence: program/country/source/disposition; green_required: conditional; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

### C-AFF-AU2 — AU rewards/referral evidence normalization
- status: PENDING
- anchor: same repo/master verified gate; user direction requires programs rewarding the user and having a referral affiliate path.
- objective: normalize existing AU research into `user_reward`, `referral_affiliate`, `country_scope`, `evidence_date`, `source_quality` without inventing payout claims.
- acceptance: missing one required dimension remains HOLD.
- dependencies: public official terms preferred.
- safe boundary: research/docs only.
- verification: source citations and schema validation.
- next handoff: Master program data model.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: `S1`; authority_required: public research; negative_tests: marketing page without terms, stale payout claim; receipt_evidence: source/date/fields; green_required: no; prs_required: no; owner_boundary: affiliate signup/publication; security_disposition: PENDING.

### C-AFF-AU3 — AU CTA audit receipt fixture
- status: PENDING
- anchor: same master gate.
- objective: add deterministic audit record for AU program identity, country decision, destination and blocked reason.
- acceptance: receipt cannot upgrade HOLD to publishable.
- dependencies: C-AFF-AU1/2 data shape.
- safe boundary: fixtures/tests.
- verification: deterministic hash/order.
- next handoff: AU->Master integration review.
- security_gates: `SG-10,SG-11,SG-14,SG-15`; risk_class: `S2`; authority_required: test branch; negative_tests: missing program ID/country mismatch; receipt_evidence: exact audit record; green_required: conditional; prs_required: no; owner_boundary: live CTA; security_disposition: PENDING.

## Affiliate-Websites UK subqueue

### C-AFF-UK1 — UK network/program evidence refresh
- status: PENDING
- anchor: Affiliate-Websites master gate `d901b3e...`; established UK research names Awin/CJ/Impact/Tradedoubler/Webgains as discovery context only.
- objective: verify currently relevant official publisher/referral terms for user-reward programs; separate network availability from program eligibility.
- acceptance: official evidence/date or UNKNOWN; no inference from network presence.
- dependencies: public research.
- safe boundary: no signup/contact.
- verification: source/date matrix.
- next handoff: UK program fixtures.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: `S1`; authority_required: public research; negative_tests: network membership mistaken for program acceptance; receipt_evidence: official source/date/status; green_required: no; prs_required: no; owner_boundary: account signup/publication; security_disposition: PENDING.

### C-AFF-UK2 — UK regulatory claim boundary fixture
- status: PENDING
- anchor: same repo; prior direction flags FCA/ASA sensitivity and initial non-financial focus.
- objective: encode non-production content fixture that rejects unsupported financial/reward guarantees and marks regulated/uncertain categories HOLD.
- acceptance: no guaranteed earnings/payout claim without evidence; ambiguous financial program stays blocked.
- dependencies: existing content schema.
- safe boundary: fixture/content tests only.
- verification: prohibited/unsupported claim cases.
- next handoff: Marketing/content use safe claims only.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: repo tests/docs; negative_tests: guaranteed income, stale rate, regulated offer without evidence; receipt_evidence: claim/source/disposition; green_required: conditional; prs_required: no; owner_boundary: live publication/legal decision; security_disposition: PENDING.

### C-AFF-UK3 — UK voucher/code tracking-abuse denial
- status: PENDING
- anchor: same master gate; coupon abuse suppression is an existing UK constraint.
- objective: test deterministic stripping/blocking of unapproved voucher/code attribution paths.
- acceptance: no affiliate destination emitted when tracking integrity is ambiguous or prohibited by current contract.
- dependencies: renderer/audit path.
- safe boundary: tests only.
- verification: malicious/ambiguous code fixtures.
- next handoff: Master audit model.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: test branch; negative_tests: unapproved code override/tracking injection; receipt_evidence: blocked attribution audit; green_required: conditional; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## Affiliate-Websites US subqueue

### C-AFF-US1 — US reward/referral evidence normalization
- status: PENDING
- anchor: Affiliate-Websites master gate `d901b3e...` / `34798980244`.
- objective: normalize official US user-reward + referral-affiliate evidence into master schema.
- acceptance: exact country scope, user reward, referral path, terms source/date; UNKNOWN preserved.
- dependencies: public official research.
- safe boundary: no signup/contact.
- verification: schema + citations.
- next handoff: US CTA fixtures.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: `S1`; authority_required: public research; negative_tests: unsupported payout/worldwide claim; receipt_evidence: program/source/date/status; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: PENDING.

### C-AFF-US2 — US country/identity mismatch denial
- status: PENDING
- anchor: same master gate.
- objective: deny CTA when US program evidence and publisher identity/country scope disagree.
- acceptance: mismatch leaves non-clickable HOLD with audit reason.
- dependencies: normalized fixture data.
- safe boundary: tests only.
- verification: deterministic mismatch tests.
- next handoff: US Overseer.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: repo tests; negative_tests: publisher/program/country mismatch; receipt_evidence: exact identities/reason; green_required: conditional; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

### C-AFF-US3 — US outbound destination safety fixture
- status: PENDING
- anchor: same verified CTA gate.
- objective: reject non-approved/redirect-confused outbound destinations in synthetic program fixtures.
- acceptance: only exact contract-approved destination survives; no hidden tracking redirect.
- dependencies: existing destination parser.
- safe boundary: fixture tests.
- verification: redirect/domain confusion cases.
- next handoff: Master renderer.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: test branch; negative_tests: lookalike domain, redirect chain metadata, tracking override; receipt_evidence: normalized destination/disposition; green_required: conditional; prs_required: no; owner_boundary: live CTA; security_disposition: PENDING.

## GhostKitchen Overseer subqueue

### C-GK-01 — batch status enum validation
- status: PENDING
- anchor: `darrinbaldwindev/GhostKitchen` issue #31; exact pre-scan base `4b217247b73eefcf96f2bfb0140c9150ab4d28a1`; prior economics gate `ddfb2d872ca116b2cf18d3a98d53670b0c228237` / `34799531732` SUCCESS.
- objective: enforce declared batch status against current non-authoritative `DECISION_SUPPORT_ONLY` contract.
- acceptance: unknown/promotional status denied; no eligibility upgrade.
- dependencies: issue #31 bounded batch.
- safe boundary: tests/tool code only.
- verification: economics validation CI.
- next handoff: C-GK-02..04.
- security_gates: `SG-06,SG-10,SG-12,SG-14`; risk_class: `S2`; authority_required: branch code/tests; negative_tests: unknown status/eligibility-like status; receipt_evidence: batch input/status/result; green_required: conditional; prs_required: no; owner_boundary: commercial selection/deploy; security_disposition: PENDING.

### C-GK-02 — source_note validation
- status: PENDING
- anchor: same issue #31/base.
- objective: require supplied `source_note` to be a non-empty string while keeping prose non-authoritative.
- acceptance: empty/non-string rejected; valid prose never upgrades evidence class.
- dependencies: same homogeneous batch.
- safe boundary: tests only/code validation.
- verification: unit/economics CI.
- next handoff: C-GK-03.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: `S2`; authority_required: branch tests; negative_tests: malicious/instructional prose, empty/non-string; receipt_evidence: validated metadata/result; green_required: conditional; prs_required: no; owner_boundary: production/commercial decision; security_disposition: PENDING.

### C-GK-03 — unknown economics evidence key denial
- status: PENDING
- anchor: same issue #31/base.
- objective: reject unknown keys in economics input evidence objects.
- acceptance: schema cannot silently absorb invented authority fields.
- dependencies: same batch.
- safe boundary: tests/code validation.
- verification: unknown-key fixture.
- next handoff: C-GK-04.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: `S2`; authority_required: branch tests; negative_tests: injected eligibility/authority field; receipt_evidence: schema error path; green_required: conditional; prs_required: no; owner_boundary: deployment; security_disposition: PENDING.

### C-GK-04 — non-promoting batch evidence summary
- status: PENDING
- anchor: same issue #31/base.
- objective: emit deterministic summary derived only from scenario results.
- acceptance: summary cannot change scenario/batch commercial eligibility.
- dependencies: C-GK-01..03.
- safe boundary: local artifact/tests.
- verification: replay/order determinism + no-promotion assertions.
- next handoff: GhostKitchen Overseer durable report.
- security_gates: `SG-07,SG-10,SG-11,SG-14`; risk_class: `S2`; authority_required: branch code/tests; negative_tests: all-fail/all-unknown summary must remain non-authoritative; receipt_evidence: input/result hash/summary; green_required: conditional; prs_required: no; owner_boundary: commercial decision; security_disposition: PENDING.

## Franchise Overseer subqueue

### C-FR-01 — tenancy-first evidence fixture
- status: PENDING
- anchor: `darrinbaldwindev/Franchise` main gate `29fa0546f0d7abe03fcc1af3d0770e7e50925c31`, CI `34799016286` SUCCESS; draft PR #22 head `7b8b07562f69ce7988f82e1f3ec71a225fb23709`, runs `34800298175` and `34800338862` SUCCESS.
- objective: require exact tenant/franchise identity before territory decision evidence can be consumed.
- acceptance: missing/mismatched tenant denies; synthetic success never implies production territory.
- dependencies: stable PR #22 head or fresh-scan successor.
- safe boundary: tests/fixtures.
- verification: exact-head CI.
- next handoff: C-FR-02.
- security_gates: `SG-03,SG-06,SG-10,SG-12,SG-14`; risk_class: `S2`; authority_required: branch tests; negative_tests: tenant mismatch/cross-tenant evidence; receipt_evidence: tenant/territory/result correlation; green_required: conditional; prs_required: no; owner_boundary: production tenancy/deploy; security_disposition: PENDING.

### C-FR-02 — territory evidence freshness/mismatch
- status: PENDING
- anchor: same exact gate/PR #22.
- objective: deny stale territory evidence and cross-territory substitution where schema supports timestamp/version.
- acceptance: stale/mismatched inputs fail closed.
- dependencies: existing schema support only; do not invent version semantics.
- safe boundary: tests.
- verification: deterministic negative cases.
- next handoff: C-FR-03.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: `S2`; authority_required: tests; negative_tests: stale/mismatched territory; receipt_evidence: evidence identity/version/time; green_required: conditional; prs_required: no; owner_boundary: production territory change; security_disposition: PENDING.

### C-FR-03 — audit handoff non-promotion
- status: PENDING
- anchor: same PR #22 exact `7b8b0756...`.
- objective: produce deterministic audit handoff that records synthetic tenancy/territory result without granting commercial/production authority.
- acceptance: receipt explicitly `non_production=true` and cannot mark territory live.
- dependencies: C-FR-01/02.
- safe boundary: fixture/audit code.
- verification: receipt schema/replay.
- next handoff: Franchise Overseer durable evidence.
- security_gates: `SG-10,SG-11,SG-14,SG-20`; risk_class: `S2`; authority_required: branch tests; negative_tests: attempted production/live flag from fixture; receipt_evidence: tenant/territory/source/result/disposition; green_required: conditional; prs_required: no; owner_boundary: live franchise/territory action; security_disposition: PENDING.

## GemVerse Overseer subqueue

### C-GV-01 — recovery action/result correlation
- status: PENDING
- anchor: `darrinbaldwindev/GemVerse` default `0033b66de8e138c199207e33c505db6d8df5345b`; issue #9; OPEN DRAFT PR #10 exact `b1f09c3a9300a24782f5f3e4ab01619a64477319`; Level 2 fixture run `34803885504` SUCCESS.
- objective: bind recovery decision to exact synthetic action/result identifiers.
- acceptance: mismatch denies recovery success.
- dependencies: fixture schema only.
- safe boundary: no canonical AgentOS execution.
- verification: exact-head fixture CI.
- next handoff: C-GV-02.
- security_gates: `SG-09,SG-10,SG-11,SG-14`; risk_class: `S2`; authority_required: branch fixture/test writes; negative_tests: action/result mismatch/replay; receipt_evidence: exact recovery/action/result lineage; green_required: conditional; prs_required: no; owner_boundary: production execution; security_disposition: PENDING.

### C-GV-02 — stale recovery evidence denial
- status: PENDING
- anchor: same PR #10 exact `b1f09c3a...`.
- objective: reject stale recovery timestamp/version only where existing schema supports it.
- acceptance: no invented version fields; supported stale evidence fails closed.
- dependencies: schema inspection.
- safe boundary: fixtures/tests.
- verification: deterministic stale/current cases.
- next handoff: C-GV-03.
- security_gates: `SG-07,SG-09,SG-10,SG-14`; risk_class: `S2`; authority_required: branch tests; negative_tests: stale/older recovery evidence; receipt_evidence: version/time/result; green_required: conditional; prs_required: no; owner_boundary: canonical runtime; security_disposition: PENDING.

### C-GV-03 — duplicate recovery-result idempotency
- status: PENDING
- anchor: same PR #10/run.
- objective: prove replayed recovery result cannot create duplicate synthetic completion/receipt.
- acceptance: one result accepted, duplicate denied/audited.
- dependencies: current fixture contract.
- safe boundary: tests only.
- verification: duplicate/replay CI.
- next handoff: C-GV-04 if capacity.
- security_gates: `SG-09,SG-10,SG-11`; risk_class: `S2`; authority_required: tests; negative_tests: exact replay/correlation reuse; receipt_evidence: idempotency key/result count; green_required: conditional; prs_required: no; owner_boundary: production runtime; security_disposition: PENDING.

### C-GV-04 — malformed evidence deterministic denial
- status: PENDING
- anchor: same exact PR #10.
- objective: reject malformed/missing fixture evidence deterministically rather than defaulting success.
- acceptance: malformed fields always explicit FAIL/HOLD.
- dependencies: none.
- safe boundary: tests.
- verification: malformed fixture matrix.
- next handoff: GemVerse Overseer report; do not claim AgentOS Level 2 readiness.
- security_gates: `SG-06,SG-10,SG-14`; risk_class: `S2`; authority_required: test branch; negative_tests: malformed/missing/unexpected keys; receipt_evidence: validation error/result; green_required: conditional; prs_required: no; owner_boundary: production; security_disposition: PENDING.

## Content360 Overseer subqueue

### C-C360-01 — current mock-adapter baseline
- status: VERIFIED
- anchor: `darrinbaldwindev/content360` main exact `8dd031bb1efaf7d0909bdc411365faf3da497f84`; Test run `34791442838` SUCCESS.
- objective: preserve current provider-neutral mocked adapter baseline; no credential persistence.
- acceptance: exact baseline remains non-production/mock only.
- dependencies: none.
- safe boundary: read-only baseline.
- verification: exact head/run.
- next handoff: adjacent homogeneous failure cases below.
- security_gates: `SG-05,SG-06,SG-10,SG-14,SG-15`; risk_class: `S0`; authority_required: none beyond read; negative_tests: baseline already mocked/no-live; receipt_evidence: exact head/run; green_required: no; prs_required: no; owner_boundary: credentials/live publish; security_disposition: VERIFIED.

### C-C360-02 — provider timeout/rate-limit mocked failures
- status: PENDING
- anchor: content360 `8dd031bb1efaf7d0909bdc411365faf3da497f84` / `34791442838`.
- objective: add deterministic timeout/rate-limit/error responses without exposing or requiring API credentials.
- acceptance: errors remain explicit, retry behavior bounded, no publish side effect.
- dependencies: existing mock adapter contract.
- safe boundary: mocks/tests only.
- verification: Test workflow exact head.
- next handoff: C-C360-03.
- security_gates: `SG-05,SG-06,SG-09,SG-10,SG-12,SG-14`; risk_class: `S2`; authority_required: branch/local test writes; negative_tests: timeout, 429, malformed provider response, retry ceiling; receipt_evidence: request ID/mock response/retry/disposition; green_required: conditional; prs_required: no; owner_boundary: API credential/live publishing; security_disposition: PENDING.

### C-C360-03 — prompt-injection/provider-output boundary
- status: PENDING
- anchor: same content360 exact head/run.
- objective: treat provider/content output as data only; deny embedded instructions requesting tool use, secret disclosure, policy bypass or publication.
- acceptance: malicious output cannot alter authority/state or trigger publish path.
- dependencies: mock adapter.
- safe boundary: adversarial fixtures only.
- verification: injection fixture tests.
- next handoff: C-C360-04.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: test branch; negative_tests: tool-use/policy-bypass/secret/publish instructions in content; receipt_evidence: input/output provenance + denial; green_required: yes if adapter used by autonomous AgentOS path; prs_required: conditional for promoted autonomous path; owner_boundary: credentials/publication; security_disposition: PENDING.

### C-C360-04 — request/result schema and provenance receipt
- status: PENDING
- anchor: same baseline `8dd031bb...`.
- objective: ensure mocked request/result records carry provider-neutral request ID, content hash, model/provider label where available, result status and no plaintext secret.
- acceptance: exact correlation survives retries; secret scan clean.
- dependencies: C-C360-02/03.
- safe boundary: tests/schema only.
- verification: deterministic receipts + fixture secret scan.
- next handoff: Marketing consumes only non-production output artifacts.
- security_gates: `SG-05,SG-09,SG-10,SG-11,SG-14`; risk_class: `S2`; authority_required: repo tests; negative_tests: mismatched result ID, secret-like fixture value redaction, replay; receipt_evidence: request/result hash/correlation; green_required: conditional; prs_required: conditional; owner_boundary: live provider credentials/publish; security_disposition: PENDING.

## Commercial Frontend Overseer subqueue

### C-CF-01 — ecommerce exception direct-evidence extraction
- status: PENDING
- anchor: isolated branch `work/commercial-frontend-ecommerce-exception-batch` head `55b189f99025038a2c9bf9fd15a757225a7ab3be`; report `reports/2026-09-14-commercial-frontend-ecommerce-exception-batch.md`; issue #21 comment `5659574435`.
- objective: apply existing validation protocol to any already-available real operator evidence for frequency, pain, minutes/case, trial intent and WTP.
- acceptance: evidence is quoted/sourced and classified; no invented demand.
- dependencies: existing internal/public operator evidence only.
- safe boundary: no outreach unless separately owner-authorized.
- verification: source-to-record trace.
- next handoff: C-CF-02 or explicit BLOCKED on external evidence.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-20`; risk_class: `S1`; authority_required: read-only evidence research; negative_tests: anecdote/general platform docs misclassified as operator demand; receipt_evidence: source/persona/problem metric/status; green_required: no; prs_required: no; owner_boundary: outreach/contact; security_disposition: PENDING.

### C-CF-02 — exception fixture acceptance model
- status: PENDING
- anchor: same `55b189f...` feasibility report.
- objective: encode non-production acceptance fixture for supplier stock unavailable, dispatch/ETA uncertainty and order change exception classes.
- acceptance: each fixture has source system, stale-state flag, requested decision, approval boundary and audit outcome; no production action.
- dependencies: existing report taxonomy.
- safe boundary: docs/fixtures/tests only.
- verification: schema/replay checks.
- next handoff: frontend prototype only after evidence-safe model.
- security_gates: `SG-06,SG-10,SG-12,SG-14,SG-15`; risk_class: `S2`; authority_required: branch fixture/test writes; negative_tests: stale external state, cross-order mismatch, unauthorized approval; receipt_evidence: exception/source/decision/audit; green_required: conditional; prs_required: no; owner_boundary: production order mutation; security_disposition: PENDING.

### C-CF-03 — external-demand boundary disposition
- status: PENDING
- anchor: same report/issue #21 evidence says platform feasibility is VERIFIED while real operator demand/WTP is UNKNOWN.
- objective: deterministically classify remaining validation rows as `AVAILABLE_EVIDENCE` vs `OUTREACH_REQUIRED` and stop at owner boundary.
- acceptance: no fabricated interviews, intent or WTP.
- dependencies: C-CF-01.
- safe boundary: classification/report only.
- verification: each row has source or explicit blocker.
- next handoff: owner/external research lane only if outreach is required.
- security_gates: `SG-06,SG-10,SG-15,SG-20`; risk_class: `S1`; authority_required: read-only synthesis; negative_tests: inferred WTP from platform docs; receipt_evidence: row/source/blocker; green_required: no; prs_required: no; owner_boundary: external outreach/contact; security_disposition: PENDING.

## Marketing / brand integration subqueue

### C-MKT-01 — AgentOS objection acceptance metrics
- status: PENDING
- anchor: AgentOS #109; Frontend PR #111 exact `d528f953201d299c823ffe12df1615f3396e278e` with AgentOS Tests #1000 SUCCESS for plain-language/fail-closed presentation; PR #104 runtime remains blocked/red at `9f53df16...`.
- objective: turn trust objections into measurable non-production onboarding/demo/pricing acceptance criteria without implying Level-2 runtime readiness.
- acceptance: every claim maps to evidence state (`PROVEN`, `DEMO_ONLY`, `PLANNED`, `HOLD`); Founding Beta remains HOLD on runtime gates.
- dependencies: current truthful frontend evidence.
- safe boundary: docs/content/tests; no campaign/live publication.
- verification: claim-evidence matrix and contradiction scan.
- next handoff: frontend consumes approved safe wording.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: `S1`; authority_required: non-production content/docs; negative_tests: runtime capability overclaim, Green/PRS implied, production autonomy claim; receipt_evidence: claim/source/state; green_required: no; prs_required: no; owner_boundary: campaign activation/publication; security_disposition: PENDING.

### C-MKT-02 — Operator integration/brand shortlist implementation-readiness
- status: PENDING
- anchor: current portfolio direction keeps first-wave Operator integrations complementary to AgentOS control plane; no production integration authority is granted; AgentOS PR #104 exact `9f53df16...` is not Level-2 ready.
- objective: maintain a concise shortlist record with integration surface, marketplace/install path, auth model, free/paid boundary, evidence source, AgentOS ownership boundary and current readiness.
- acceptance: shortlist distinguishes `RESEARCH_READY`, `MOCK_READY`, `OWNER_SETUP_REQUIRED`, `BLOCKED`; no tool/provider becomes authority source.
- dependencies: official/public provider evidence only.
- safe boundary: research/synthesis; no account install/credentials.
- verification: dated official links and architecture fit check.
- next handoff: AgentOS capability router/backlog only after canonical runtime gates; Marketing may use evidence-safe positioning.
- security_gates: `SG-02,SG-03,SG-05,SG-06,SG-10,SG-14,SG-20`; risk_class: `S1`; authority_required: public research; negative_tests: provider self-authorization, credential-in-doc, production-ready inference from marketplace listing; receipt_evidence: provider/source/date/readiness/boundary; green_required: no; prs_required: no; owner_boundary: install/credentials/spend; security_disposition: PENDING.

### C-MKT-03 — marketplace-path claim boundary
- status: PENDING
- anchor: GlobalShopCo #17 still has zero eBay-ready SKUs; Amazon gate `84ab928b...` is synthetic only; MyPrime `1820dfe1...` remains `QUALIFIED=0`.
- objective: align portfolio marketing language so Shopify/eBay/Amazon/Affiliate/Operator marketplace paths are described as verified, synthetic, research-only or blocked exactly as evidence supports.
- acceptance: no channel-readiness or income claim exceeds evidence.
- dependencies: Lane B/C current states.
- safe boundary: content matrix only.
- verification: cross-lane contradiction check.
- next handoff: website/brochure/ad copy only after owner publication authority.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: `S1`; authority_required: non-production content synthesis; negative_tests: eBay-ready, Amazon-ready, Prime-qualified, guaranteed income claims without evidence; receipt_evidence: claim -> exact evidence anchor; green_required: no; prs_required: no; owner_boundary: live campaign/publication; security_disposition: PENDING.

# RECONCILIATION — 2026-09-14 17:30 BRISBANE

- **LANE A:** AgentOS PR #104 advanced from prior `a4d1a1baa...` to exact `9f53df16ae37ee6a86e66d2a808ca7f62f203d76`. Exact-head AgentOS Tests run `34816222109` is **FAILURE**: Ubuntu/Node22 `103887346619` SUCCESS; Windows/Node26 `103887346695` FAIL in test suite. Therefore the current head is not promotable. Continuous ownership remains independently falsified by PRS PR #17 `8479ae...` / `34810516744` on predecessor target `71c463a...`; canonical authenticated actor/grant admission remains unwired. A-AG-02 is ACTIVE; A-AG-01/A-AG-03 and dependent PRS assurance remain BLOCKED; adjacent correlation work remains queued but cannot inherit predecessor PASS.
- **LANE B:** no fresh evidence justifies promotion beyond prior verified synthetic gates. GlobalShopCo #17 still controls eBay commercial readiness; `V178-36336` remains negative; Headless M3 code gate remains verified with external browser proof UNKNOWN; eBay/Amazon remain synthetic/non-publication; MyPrime remains research-only with `QUALIFIED=0`. Deep homogeneous queues are replenished without widening authority.
- **LANE C:** GhostKitchen issue #31 is a newly durable bounded follow-on at exact pre-scan base `4b217247...`, so its four-item metadata/evidence-summary mini-batch is PENDING rather than inferred complete. Content360 is now explicitly anchored as VERIFIED baseline main `8dd031bb1efaf7d0909bdc411365faf3da497f84`, Test `34791442838` SUCCESS, with three adjacent mocked/security-negative items replenished. Other prior verified fixture gates remain exact-head-bounded and receive only homogeneous adjacent work.
- **Security:** all materially changed/new items carry applicable SG gates, risk class, authority, negative tests, receipt evidence, Green/PRS need, owner boundary and separate security disposition. Missing material evidence remains BLOCKED/UNKNOWN. Functional success does not promote security, and security success does not promote functionality.
- No scheduler firing was treated as completion. No overall GREEN.

# NEXT EXECUTION EMPHASIS
1. **A:** close the exact-head Windows CI failure without weakening tests; separately do not touch ownership/authority blockers except with a real primitive/canonical source.
2. **B:** exact-SKU economics + supplier permission evidence; run synthetic eBay/Amazon/MyPrime negative batches in parallel where isolated.
3. **C:** consume GhostKitchen issue #31 batch; Content360 mocked failure/injection batch; stable Affiliate/Franchise/GemVerse fixture batches; Commercial Frontend real-evidence classification; Marketing claim/Operator-readiness matrices.
4. Fresh-scan exact head/issue/CI immediately before any write or state promotion. Preserve owner/external/credential/physical-host blockers and do not broaden the fixed scheduled priority sets.
