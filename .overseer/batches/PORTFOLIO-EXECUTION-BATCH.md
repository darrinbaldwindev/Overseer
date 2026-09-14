# Portfolio Execution Batch Manifest

**Purpose:** deep bounded execution queue for the existing scheduled portfolio lanes. Exact repository/issue/CI/runtime evidence is authoritative. Scheduler firing and worker claims are never completion evidence.

**Fixed lanes:** A = AgentOS Level 2 P0 + PRS/Green assurance-adjacent; B = GlobalShopCo/Headless/eBay/Amazon/MyPrimeDelivery; C = Affiliate-Websites/GhostKitchen/Franchise/GemVerse/Content360/Commercial Frontend/Marketing.

**States:** `PENDING | ACTIVE | VERIFIED | BLOCKED | STALE | SPLIT_REQUIRED`.

**Hard boundary:** no merge/approve/ready/rebase/deploy/credentials/production writes/purchases/supplier contact/live publication/production autonomy. Core invariant: **NO MODEL DECIDES ITS OWN AUTHORITY.**

**Security:** functional status and security disposition are independent. Applicable gates come from `.overseer/security/AGENTOS-SECURITY-GATE-MATRIX.md`. Missing material evidence remains UNKNOWN/BLOCKED.

## Historical evidence registry — retained

- Previous deep checkpoint: Overseer #49 comment `5660616820`; prior manifest commit `023cdaf6dd56b43255cef333d48bc6073dee70ac`.
- AgentOS predecessor cross-platform run `34816222109` on `9f53df16ae37ee6a86e66d2a808ca7f62f203d76` ultimately succeeded on attempt 2; this PASS does not transfer to later heads.
- PRS predecessor defect baseline: PR #17 `8479ae148694af24ae5a492036f3b5cd56fd8c5c` / `34810516744`, `DEFECT_REPRODUCED`.
- Headless verified M3 baseline: `9799e6fe5a9c72e42e1554949697a64acce14bd4` / `34798624627` SUCCESS.
- eBay synthetic baseline: `b57e0a47bdff4b699d8b6b346fe5e9e1a0bbacc3` / `34805527804` SUCCESS.
- MyPrimeDelivery research baseline: `1820dfe1b5b8fe938c5fcd58e28858dc79b66e16` / `34811798266` SUCCESS, 40 research-only candidates across 12 categories, `QUALIFIED=0`.
- Affiliate master verified baseline: `d901b3e2c0c772cdc43019dd96cf2b19bdded0a6` / `34798980244` SUCCESS.
- GhostKitchen economics baseline: `ddfb2d872ca116b2cf18d3a98d53670b0c228237` / `34799531732` SUCCESS.
- Franchise tenancy/territory baselines: main `29fa0546f0d7abe03fcc1af3d0770e7e50925c31` / `34799016286` SUCCESS; draft PR #22 `7b8b07562f69ce7988f82e1f3ec71a225fb23709` / `34800298175`, `34800338862` SUCCESS.
- GemVerse PR #10 baseline: `b1f09c3a9300a24782f5f3e4ab01619a64477319` / `34803885504` SUCCESS.
- Content360 mock baseline: `8dd031bb1efaf7d0909bdc411365faf3da497f84` / `34791442838` SUCCESS.
- Commercial Frontend evidence baseline: `55b189f99025038a2c9bf9fd15a757225a7ab3be`; issue #21 comment `5659574435`.

# LANE A — AGENTOS LEVEL 2 P0

## AgentOS Overseer subqueue

### A-AG-01 — continuous project-file ownership primitive
- status: BLOCKED
- owner/workstream: AgentOS Level 2 / project-file writer
- anchor: PR #104 exact `83a58b8bd230550b5781a0fee700cca250819a75`; PRS exact retarget evidence `0defebe26f71e1cf5df1168fa5454bfd8de30091`, run `34821646371`, artifact `10338681051`, disposition `DEFECT_REPRODUCED` with 2 current-head cases.
- objective: replace the check/release gap with one kernel-enforced, crash-releasing ownership boundary held continuously through final verify -> publish/prepared recovery -> durable success receipt -> release.
- acceptance: successor/replacement writer cannot cause stale-owner publish; success cannot persist before ownership-loss detection; prepared recovery uses the identical fence; crash release is bounded.
- dependencies: real production writer design change; no policy-only or synthetic substitute.
- safe action boundary: branch code/tests only; no production mutation or merge.
- verification method: targeted ownership adversarial suite + Windows/Node26 + Ubuntu/Node22 CI + exact-head Green, then independent exact-head PRS.
- next handoff: AgentOS implementation worker; Green after exact CI; PRS only after Green PASS on unchanged head.
- security_gates: `SG-03,SG-08,SG-09,SG-10,SG-11,SG-14,SG-18,SG-19`; risk_class: `S2`; authority_required: scoped non-production AgentOS branch/test writes; negative_tests: replacement-after-verification, successor-writer, stale identity, TOCTOU, crash/replay, duplicate result/mutation, prepared-recovery stale owner; receipt_evidence: exact actor/task/file/preimage/postimage/ownership/result lineage; green_required: yes; prs_required: yes; owner_boundary: merge/deploy/physical production action; security_disposition: BLOCKED.

### A-AG-02 — exact-current-head CI baseline after cancelled docs-only run
- status: PENDING
- owner/workstream: AgentOS Level 2 / CI evidence
- anchor: PR #104 `83a58b8bd230550b5781a0fee700cca250819a75`; exact-head AgentOS Tests #1037 / `34821388860` = CANCELLED; latest commit is documentation-only; predecessor `9f53df16...` run `34816222109` succeeded on attempt 2.
- objective: obtain a complete exact-current-head cross-platform CI result without interpreting cancellation as PASS or FAIL.
- acceptance: both Ubuntu/Node22 and Windows/Node26 jobs complete deterministically on `83a58b8...` or a successor exact head; no skipped/weakened security assertions.
- dependencies: current branch remains unmerged/draft.
- safe action boundary: rerun/test-only or smallest deterministic CI fixture correction; no runtime authority widening.
- verification method: exact workflow/run/job IDs plus head SHA.
- next handoff: if runtime/security defect appears, route smallest remediation to A-AG-01/A-AG-04; otherwise preserve CI evidence only.
- security_gates: `SG-08,SG-09,SG-10,SG-18`; risk_class: `S2`; authority_required: scoped branch/test/CI writes; negative_tests: existing fail-closed suites must remain enabled; receipt_evidence: exact head/workflow/job conclusions; green_required: yes before promotion; prs_required: only if runtime semantics materially change; owner_boundary: merge/deploy; security_disposition: PENDING.

### A-AG-03 — canonical authenticated authority-admission producer
- status: BLOCKED
- owner/workstream: AgentOS Level 2 / authority admission
- anchor: PR #104 `83a58b8...`; PR body still states authenticated transport and canonical grant lookup are unwired composition seams; current emitted task is not yet canonical end-to-end admission proof.
- objective: bind admission to an existing canonical authenticated actor identity and canonical grant source without creating a second authority registry or accepting self-grant request fields.
- acceptance: payload cannot supply/override actor; grant provenance binds actor/project/scope; missing/mismatch lookup produces zero task/wake/result/mutation artifacts.
- dependencies: real existing authenticator/grant source must be identified as bindable.
- safe action boundary: architecture/code/tests only; no new authority service/registry/scheduler/memory/persistence.
- verification method: exact-head missing actor/spoof actor/no grant/grant mismatch/cross-project/replay tests and durable provenance.
- next handoff: AgentOS architecture when canonical source is evidenced; otherwise remain BLOCKED.
- security_gates: `SG-01,SG-02,SG-03,SG-04,SG-09,SG-10,SG-11,SG-18,SG-19`; risk_class: `S2`; authority_required: existing canonical identity/grant read plus scoped admission code change; negative_tests: spoofed actor, absent grant, actor/project/scope mismatch, replay, stale correlation; receipt_evidence: canonical issuer/source/version plus exact task/mission/request; green_required: yes; prs_required: yes; owner_boundary: credential/security-policy change; security_disposition: BLOCKED.

### A-AG-04 — correlation/idempotency preservation mini-batch
- status: PENDING
- owner/workstream: AgentOS Level 2 / remote-bridge lineage
- anchor: PR #104 `83a58b8...`; predecessor authority/correlation regressions passed on earlier exact heads but cannot transfer.
- objective: preserve exact delivery/request/task/mission/wake/actor/grant/result correlation and zero-artifact fail-closed behavior while ownership/admission work moves.
- acceptance: malformed/mismatched/stale IDs fail closed; rejected admission leaves no durable execution artifacts; duplicate delivery cannot create duplicate mutation/result.
- dependencies: A-AG-02 current-head CI evidence; do not invent nonce/expiry semantics absent canonical contract.
- safe action boundary: homogeneous regression tests and smallest adjacent fixes only.
- verification method: targeted replay/correlation tests + full exact-head CI.
- next handoff: Green sample; PRS only if authority semantics materially change.
- security_gates: `SG-01,SG-02,SG-09,SG-10,SG-11,SG-18`; risk_class: `S2`; authority_required: scoped branch tests; negative_tests: duplicate pickup, stale delivery, correlation mismatch, missing authority evidence, crash-after-side-effect; receipt_evidence: zero-artifact denial and exact accepted lineage; green_required: yes; prs_required: conditional; owner_boundary: merge/deploy; security_disposition: PENDING.

## PRS / Green assurance-adjacent subqueue

### A-PRS-01 — current-head continuous-ownership defect baseline
- status: VERIFIED
- owner/workstream: PRS independent assurance
- anchor: PRS exact `0defebe26f71e1cf5df1168fa5454bfd8de30091`; AgentOS exact `83a58b8...`; source tree `be291054df911b487dfbf1c0e7d409fb54a61789`; writer SHA256 `bf36ef114c6db43e3b79be5d28a5850ead70f10156de390f249ec536e63cb12c`; run `34821646371` SUCCESS as assurance execution; disposition `DEFECT_REPRODUCED`; artifact SHA256 `ceb5ef0d4cdb9d7a4747f662215788169b33186a8cf0dc55d5ce332eb17b349c`.
- objective: preserve immutable exact-head baseline; do not transfer it to future heads without rerun.
- acceptance: baseline remains evidence of two false-GREEN ownership cases only.
- dependencies: none.
- safe action boundary: read-only retention.
- verification method: exact target/source/artifact identity.
- next handoff: feed A-AG-01; rerun only after a real writer change and Green exact-head PASS.
- security_gates: `SG-08,SG-10,SG-11,SG-19`; risk_class: `S0`; authority_required: read-only exact-object assurance; negative_tests: stale-owner normal publish + prepared recovery already executed; receipt_evidence: immutable target/artifact hashes; green_required: no; prs_required: this is PRS evidence; owner_boundary: none; security_disposition: VERIFIED.

### A-PRS-02 — replacement primitive exact-head challenge
- status: BLOCKED
- owner/workstream: PRS independent assurance
- anchor: A-PRS-01 current defect baseline; no replacement ownership primitive evidenced yet.
- objective: rerun immutable ownership suite only after A-AG-01 changes the real target writer and Agent Green passes the same exact head.
- acceptance: normal publish + prepared recovery + successor-writer + crash/replay all independently classified with immutable exact target.
- dependencies: A-AG-01 implemented; current-head CI complete; Green exact-head PASS.
- safe action boundary: PRS fixtures/harness only; no target implementation.
- verification method: PRS workflow/artifact exact target SHA/tree/file hashes.
- next handoff: Overseer reconciliation; defect -> AgentOS remediation, PASS -> next bounded gate only.
- security_gates: `SG-08,SG-09,SG-10,SG-11,SG-19`; risk_class: `S2`; authority_required: read target + bounded assurance writes; negative_tests: full ownership matrix; receipt_evidence: immutable target/tree/file/artifact hashes; green_required: yes prerequisite; prs_required: yes; owner_boundary: merge/deploy; security_disposition: BLOCKED.

### A-PRS-03 — admission false-GREEN challenge
- status: BLOCKED
- owner/workstream: PRS independent assurance
- anchor: A-AG-03 remains unwired on AgentOS PR #104 `83a58b8...`.
- objective: once canonical identity/grant admission exists, prove payload cannot self-authorize and mismatched provenance cannot reach task/wake/mutation artifacts.
- acceptance: missing/spoofed actor, absent/mismatched/cross-project grant, stale/replayed request all deny with zero false success.
- dependencies: A-AG-03 implementation + Green exact-head PASS.
- safe action boundary: independent assurance only.
- verification method: exact target hashes + deterministic adversarial outputs.
- next handoff: Overseer promotion only after independent PASS.
- security_gates: `SG-01,SG-02,SG-03,SG-09,SG-10,SG-11,SG-19`; risk_class: `S2`; authority_required: read target + bounded PRS harness writes; negative_tests: actor/grant provenance attacks; receipt_evidence: exact target and denial receipts; green_required: yes prerequisite; prs_required: yes; owner_boundary: credentials/security policy; security_disposition: BLOCKED.

# LANE B — COMMERCE PRIORITY

## GlobalShopCo Overseer subqueue

### B-GSC-01 — free-delivery economics calculator gate
- status: VERIFIED
- owner/workstream: GlobalShopCo / Home Organisation economics
- anchor: branch `agent/chatgpt/m4-home-organisation` exact `f4e5de0e0e946a5c6844dea84d99527d0c9f8474`; Free-delivery economics `34822003322` SUCCESS; Home Organisation launch gate `34822003312` SUCCESS; PR #10 OPEN/UNMERGED; durable GlobalShopCo #17 comment `5661069884`.
- objective: preserve deterministic fail-closed calculator for supplier cost, freight, channel/payment fees, returns/warranty, selling price, target margin and UNKNOWN propagation.
- acceptance: critical UNKNOWN => HOLD; zero/negative contribution cannot pass; `publicationAuthority=false`, `productionMutation=false` remain explicit.
- dependencies: none for fixture reuse.
- safe action boundary: synthetic/non-production only.
- verification method: exact-head CI and receipt assertions.
- next handoff: B-GSC-02 applies calculator to exact-SKU evidence; no pricing/publication authority implied.
- security_gates: `SG-10,SG-12,SG-13,SG-14,SG-20`; risk_class: `S2`; authority_required: non-production fixture/test writes only; negative_tests: missing freight/fees, duplicate fee, negative price, UNKNOWN cost; receipt_evidence: exact inputs/calculation/disposition; green_required: no for research fixture; prs_required: no; owner_boundary: production pricing/purchase/listing; security_disposition: VERIFIED.

### B-GSC-02 — next exact-SKU economics application
- status: PENDING
- owner/workstream: GlobalShopCo / supplier-product qualification
- anchor: GlobalShopCo #17; current truth still `0 eBay-ready SKUs`; Southern Pet GiGwi family remains permission-required with authenticated trade prices UNKNOWN.
- objective: apply verified calculator to one exact compact SKU using exact supplier/SKU, public/authorised acquisition evidence, AU delivered retail comps, freight and returns/warranty evidence.
- acceptance: every cost is sourced or UNKNOWN; no candidate passes if margin depends on unknown freight/permission/trade cost.
- dependencies: public/repo evidence only; no supplier contact.
- safe action boundary: research/docs/fixtures.
- verification method: dated sources + reproducible calculation receipt.
- next handoff: positive research result -> channel-specific evidence gate; negative -> record rejection and advance next SKU.
- security_gates: `SG-06,SG-10,SG-12,SG-13,SG-14,SG-20`; risk_class: `S1`; authority_required: public/read-only research + repo docs; negative_tests: retail-vs-wholesale confusion, stale price, freight missing, marketplace permission absent; receipt_evidence: exact SKU/source/date/cost table; green_required: no; prs_required: no; owner_boundary: supplier contact/purchase/production change; security_disposition: PENDING.

### B-GSC-03 — supplier permission / blind-shipping evidence matrix
- status: PENDING
- owner/workstream: GlobalShopCo / supplier governance
- anchor: Southern Pet/GiGwi `PERMISSION-REQUIRED/HOLD`; authenticated trade cost UNKNOWN; current marketing evidence also records actual GlobalShopCo eBay plan/category fee UNKNOWN.
- objective: normalize public supplier/channel terms for eBay/Amazon permission, seller identity/packing, stock, returns/warranty, buyer-data compatibility and evidence freshness.
- acceptance: ordinary dropship support never becomes marketplace permission; unknown stays UNKNOWN.
- dependencies: public/read-only evidence only.
- safe action boundary: no supplier/account contact and no connector mutation.
- verification method: dated source/status matrix and contradiction scan.
- next handoff: eBay/Amazon consume only exact supplier/SKU rows.
- security_gates: `SG-06,SG-10,SG-14,SG-15,SG-20`; risk_class: `S1`; authority_required: public/read-only research; negative_tests: ambiguous permission, stale terms, marketing prose treated as authority; receipt_evidence: supplier/status/source/date; green_required: no; prs_required: no; owner_boundary: supplier contact/agreements/account changes; security_disposition: PENDING.

### B-GSC-04 — Southern Pet owner-decision packet
- status: PENDING
- owner/workstream: GlobalShopCo / eBay commercial readiness
- anchor: Marketing report `e15743373332bde4d97f6677f9cd55fe7322d41c`; current quote-screen trade-cost ceilings: GDAG2600 A$4.57, GDAG2522 A$10.09, GDAG2515 A$8.58, GDAG2505 A$10.58, GDAG2610 A$8.47; these are ceilings only, not actual costs/profitability.
- objective: assemble a read-only decision packet stating exact evidence required before any supplier contact/permission request or stock pilot can be considered.
- acceptance: clearly separates published fee assumptions, UNKNOWN actual plan/category fee, UNKNOWN authenticated trade cost and marketplace permission requirement.
- dependencies: current reports and public evidence.
- safe action boundary: docs only; no contact/purchase/spend.
- verification method: source-to-claim mapping and explicit UNKNOWNs.
- next handoff: owner only if a future decision is required; otherwise continue safe research.
- security_gates: `SG-06,SG-10,SG-13,SG-14,SG-15,SG-20`; risk_class: `S1`; authority_required: read-only synthesis; negative_tests: quote ceiling misrepresented as cost/profit, plan fee guessed, permission inferred; receipt_evidence: SKU/evidence/UNKNOWN/decision-needed table; green_required: no; prs_required: no; owner_boundary: supplier contact/purchase/spend; security_disposition: PENDING.

## GlobalShopCo-Headless Overseer subqueue

### B-HDL-01 — checkout host parser/normalizer inspection
- status: PENDING
- owner/workstream: GlobalShopCo-Headless / Shopify checkout handoff
- anchor: issue #3; verified M3 head `9799e6fe5a9c72e42e1554949697a64acce14bd4`; CI `34798624627` SUCCESS.
- objective: inspect production-code host parsing/normalization for case, trailing dot, encoding and whitespace confusion before adding tests.
- acceptance: exact HTTPS Shopify host rule and parser behavior are documented from code; ambiguities remain explicit.
- dependencies: fresh exact-head scan before edit.
- safe action boundary: read-only first.
- verification method: file/path/code citations.
- next handoff: B-HDL-02 only for applicable parser cases.
- security_gates: `SG-03,SG-06,SG-10,SG-14`; risk_class: `S1`; authority_required: repo read; negative_tests: derived after parser inspection; receipt_evidence: exact head/file/path findings; green_required: no; prs_required: no; owner_boundary: deploy/production config; security_disposition: PENDING.

### B-HDL-02 — host-confusion fail-closed fixtures
- status: PENDING
- owner/workstream: GlobalShopCo-Headless / Shopify checkout handoff
- anchor: B-HDL-01 + `9799e6fe...` baseline.
- objective: add only parser-relevant trailing-dot/case/encoded/whitespace/domain-confusion fixtures.
- acceptance: canonical allowed Shopify HTTPS destination passes; confusion inputs fail closed with no purchase action.
- dependencies: B-HDL-01 applicability.
- safe action boundary: tests/non-production code only.
- verification method: exact-head CI.
- next handoff: Green sample only if runtime boundary changes.
- security_gates: `SG-03,SG-10,SG-14,SG-18`; risk_class: `S2`; authority_required: scoped branch tests/code; negative_tests: applicable host confusion; receipt_evidence: exact URL input/disposition; green_required: conditional; prs_required: no by default; owner_boundary: deploy/production Shopify; security_disposition: PENDING.

### B-HDL-03 — external dev-store evidence packet
- status: BLOCKED
- owner/workstream: GlobalShopCo-Headless / browser acceptance
- anchor: issue #3; code gate verified, external browser/dev-store proof UNKNOWN.
- objective: define exact evidence packet for future owner-authorized non-production cart/checkout proof.
- acceptance: test product/variant identity, environment, host, cart/redirect result, no secret leakage, timestamp/screenshots/logs; explicitly non-production.
- dependencies: owner-authorized dev/test access if required.
- safe action boundary: preparation only now.
- verification method: checklist review; live browser proof separate.
- next handoff: owner only when account/physical access is unavoidable.
- security_gates: `SG-05,SG-10,SG-14,SG-20`; risk_class: `S2`; authority_required: non-production dev-store access; negative_tests: prod host/token denial; receipt_evidence: environment-bound packet; green_required: yes for promotion; prs_required: no; owner_boundary: credentials/production access; security_disposition: BLOCKED.

## Shopify -> eBay Overseer subqueue

### B-EBY-01 — synthetic mapper/idempotency baseline
- status: VERIFIED
- owner/workstream: Shopify -> eBay
- anchor: `darrinbaldwindev/shopify_ebay` branch `agent/chatgpt/ebay-mapper-receipts` exact `b57e0a47bdff4b699d8b6b346fe5e9e1a0bbacc3`; run `34805527804` SUCCESS; prior stale/order/tracking/correlation follow-ons already implemented and must not be duplicated.
- objective: preserve current synthetic mapping/receipt/idempotency behavior with `network_io=false` and `publication_authority=false`.
- acceptance: no synthetic test grants marketplace authority.
- dependencies: none.
- safe action boundary: read-only baseline.
- verification method: exact head/run.
- next handoff: adjacent evidence-only items below.
- security_gates: `SG-02,SG-03,SG-09,SG-10,SG-11,SG-14,SG-15,SG-20`; risk_class: `S0`; authority_required: read-only baseline; negative_tests: existing replay/correlation denials retained; receipt_evidence: exact head/run; green_required: no; prs_required: no; owner_boundary: connector/account/publication; security_disposition: VERIFIED.

### B-EBY-02 — commercial evidence ingest fail-closed fixture
- status: PENDING
- owner/workstream: Shopify -> eBay
- anchor: B-EBY-01 baseline; GlobalShopCo #17 still has zero eBay-ready SKUs.
- objective: add a synthetic input contract that consumes supplier/SKU channel-readiness fields without converting UNKNOWN permission/freight/trade cost into listing eligibility.
- acceptance: any missing permission, seller identity, stock freshness, landed economics or plan/category fee evidence yields HOLD; no network path.
- dependencies: exact schema from GlobalShopCo B-GSC-02/03.
- safe action boundary: fixtures/tests only.
- verification method: deterministic HOLD/PASS fixture matrix; PASS remains candidate-only, not publication authority.
- next handoff: GlobalShopCo/eBay Overseer reconciliation.
- security_gates: `SG-02,SG-06,SG-10,SG-12,SG-13,SG-14,SG-15,SG-20`; risk_class: `S2`; authority_required: branch test writes; negative_tests: missing permission/freight/fee/stock/seller identity; receipt_evidence: exact evidence flags and disposition; green_required: conditional; prs_required: no until production-capable path exists; owner_boundary: live connector/listing; security_disposition: PENDING.

### B-EBY-03 — zero-network/publication regression guard
- status: PENDING
- owner/workstream: Shopify -> eBay
- anchor: B-EBY-01 exact synthetic baseline.
- objective: prove adjacent fixture work cannot introduce HTTP calls, marketplace SDK invocation, listing publish, account mutation or hidden send path.
- acceptance: mocked forbidden interfaces remain zero-invocation; explicit non-production flags remain false for authority.
- dependencies: B-EBY-02 if changed.
- safe action boundary: tests only.
- verification method: zero-invocation spies + exact-head CI.
- next handoff: stop at owner/live-account boundary.
- security_gates: `SG-03,SG-05,SG-10,SG-14,SG-15,SG-20`; risk_class: `S2`; authority_required: branch tests; negative_tests: attempted network/publish/credential use; receipt_evidence: zero-invocation audit; green_required: conditional; prs_required: no; owner_boundary: connector install/credentials/listing; security_disposition: PENDING.

## Shopify -> Amazon Overseer subqueue

### B-AMZ-01 — granular synthetic preflight gate
- status: VERIFIED
- owner/workstream: Shopify -> Amazon
- anchor: branch `agent/chatgpt/amazon-au-preflight` exact `95191c639d2deccd85ed494550e12731fb8ed00e`; Amazon channel gate `34821710314` SUCCESS; 27 deterministic cases; GlobalShopCo #23 comment `5661067590`.
- objective: preserve seller-of-record, category/GTIN-exemption, supplier marketplace-fulfilment, Shopify stock freshness and exact variant-identity gates.
- acceptance: unresolved or mismatched evidence remains HOLD/DENY; no listing/network authority.
- dependencies: none for baseline.
- safe action boundary: synthetic only.
- verification method: exact head/run and fixture count.
- next handoff: adjacent stale/replay evidence items below.
- security_gates: `SG-02,SG-03,SG-06,SG-09,SG-10,SG-14,SG-20`; risk_class: `S0`; authority_required: read-only baseline; negative_tests: existing 27-case gate retained; receipt_evidence: exact evidence flags/status; green_required: no; prs_required: no; owner_boundary: Amazon account/credentials/listing; security_disposition: VERIFIED.

### B-AMZ-02 — stale seller/category/GTIN evidence precedence
- status: PENDING
- owner/workstream: Shopify -> Amazon
- anchor: B-AMZ-01 exact `95191c...`.
- objective: add homogeneous stale/future/contradictory evidence cases only where schema supports evidence timestamps/versions.
- acceptance: stale or contradictory authoritative fields cannot be overridden by fresher non-authoritative prose; unsupported freshness fields are not invented.
- dependencies: schema inspection.
- safe action boundary: fixtures/tests only.
- verification method: deterministic exact-head CI.
- next handoff: B-AMZ-03.
- security_gates: `SG-06,SG-07,SG-09,SG-10,SG-14`; risk_class: `S2`; authority_required: branch tests; negative_tests: stale/future seller identity, GTIN contradiction, category mismatch; receipt_evidence: source/version/time/disposition; green_required: conditional; prs_required: no; owner_boundary: listing/account; security_disposition: PENDING.

### B-AMZ-03 — zero-listing/network authority regression
- status: PENDING
- owner/workstream: Shopify -> Amazon
- anchor: B-AMZ-01 verified synthetic gate.
- objective: prove preflight cannot call Amazon/Shopify live mutation interfaces or infer publication authority from all-green synthetic inputs.
- acceptance: zero live adapter invocation; final synthetic PASS remains advisory only.
- dependencies: none.
- safe action boundary: tests/mocks.
- verification method: forbidden-interface spies + receipt assertions.
- next handoff: stop at commercial evidence/account boundary.
- security_gates: `SG-03,SG-05,SG-10,SG-14,SG-15,SG-20`; risk_class: `S2`; authority_required: branch tests; negative_tests: attempted API/listing/credential path; receipt_evidence: zero-invocation + advisory disposition; green_required: conditional; prs_required: no; owner_boundary: seller account/credentials/listing; security_disposition: PENDING.

## MyPrimeDelivery Overseer subqueue

### B-MPD-01 — research baseline / qualification ceiling
- status: VERIFIED
- owner/workstream: MyPrimeDelivery
- anchor: exact `1820dfe1b5b8fe938c5fcd58e28858dc79b66e16`; run `34811798266` SUCCESS; 40 research-only candidates / 12 categories / `QUALIFIED=0`.
- objective: preserve explicit research-only ceiling and no inferred Prime/rank/deal truth.
- acceptance: fixture count/category coverage cannot upgrade qualification.
- dependencies: none.
- safe action boundary: read-only baseline.
- verification method: exact head/run.
- next handoff: evidence-rights/freshness work below.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: `S0`; authority_required: read-only baseline; negative_tests: unsupported rank/Prime inference already prohibited; receipt_evidence: candidate IDs/category counts/status; green_required: no; prs_required: no; owner_boundary: Amazon/Associates credentials/publication; security_disposition: VERIFIED.

### B-MPD-02 — source-rights/provider-authority contract
- status: PENDING
- owner/workstream: MyPrimeDelivery
- anchor: B-MPD-01; authorised live product/Prime/ranking/deal provider remains UNKNOWN.
- objective: define deterministic source-quality/right-to-use fields separating public discovery, official provider evidence and prohibited/unknown reuse.
- acceptance: public/editorial source cannot become canonical Prime/rank/deal truth; missing rights/provider authority yields HOLD.
- dependencies: current fixture schema.
- safe action boundary: docs/fixtures/tests only; no provider signup or credentials.
- verification method: source-class fixtures and validator.
- next handoff: B-MPD-03.
- security_gates: `SG-05,SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: `S2`; authority_required: repo docs/tests; negative_tests: public blog as ranking authority, unknown reuse rights, hidden tracking source; receipt_evidence: source/type/date/rights/disposition; green_required: conditional; prs_required: no; owner_boundary: provider subscription/credentials/publication; security_disposition: PENDING.

### B-MPD-03 — time-sensitive sale freshness fixture
- status: PENDING
- owner/workstream: MyPrimeDelivery
- anchor: B-MPD-01; time-sensitive sale/Prime evidence remains unresolved.
- objective: encode freshness/expiry semantics only from evidenced provider fields; stale/undated sale signals must not be promoted.
- acceptance: stale/undated/contradictory sale evidence remains research-only/HOLD.
- dependencies: B-MPD-02 provider/source contract.
- safe action boundary: synthetic fixtures/tests.
- verification method: stale/future/undated fixture matrix.
- next handoff: thin-category research expansion only after source rules are explicit.
- security_gates: `SG-06,SG-07,SG-09,SG-10,SG-14`; risk_class: `S2`; authority_required: test branch; negative_tests: stale sale, future timestamp, unsupported Prime flag; receipt_evidence: source/time/status; green_required: conditional; prs_required: no; owner_boundary: live provider/publication; security_disposition: PENDING.

# LANE C — PRODUCT / CONTENT / VENTURES

## Affiliate-Websites Master subqueue

### C-AFF-M1 — future/stale publisher evidence denial
- status: PENDING
- owner/workstream: Affiliate-Websites Master
- anchor: verified gate `d901b3e2c0c772cdc43019dd96cf2b19bdded0a6` / `34798980244` SUCCESS.
- objective: reject impossible future evidence and stale evidence only according to existing schema semantics.
- acceptance: no CTA-ready result from invalid freshness evidence.
- dependencies: fresh-scan before edit.
- safe action boundary: fixtures/tests.
- verification method: exact-head CI.
- next handoff: country consumers.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: scoped tests; negative_tests: future/stale evidence; receipt_evidence: program/publisher/source/time/disposition; green_required: conditional; prs_required: no; owner_boundary: live publication; security_disposition: PENDING.

### C-AFF-M2 — deterministic program identity/destination resolution
- status: PENDING
- owner/workstream: Affiliate-Websites Master
- anchor: same verified gate.
- objective: reject or deterministically resolve duplicate/ambiguous program identities without silently swapping destination/tracking metadata.
- acceptance: ambiguity fails closed or existing canonical ID wins; blocked entries are non-clickable.
- dependencies: stable schema.
- safe action boundary: tests/fixtures.
- verification method: permutation/replay and render assertions.
- next handoff: AU/UK/US use master contract.
- security_gates: `SG-05,SG-06,SG-07,SG-09,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: test branch; negative_tests: duplicate IDs, conflicting destination/tracking, malicious query; receipt_evidence: program IDs/input hash/disposition; green_required: conditional; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

### C-AFF-M3 — blocked destination/tracking stripping
- status: PENDING
- owner/workstream: Affiliate-Websites Master
- anchor: same verified CTA gate.
- objective: prove HOLD/BLOCKED programs cannot leak active outbound destinations or tracking parameters into rendered/audit output.
- acceptance: blocked output contains no active CTA/tracking surface.
- dependencies: renderer/audit contract.
- safe action boundary: tests only.
- verification method: rendered fixture assertions.
- next handoff: country-specific negative cases.
- security_gates: `SG-05,SG-06,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: tests; negative_tests: blocked destination, tracking injection, country mismatch; receipt_evidence: sanitized output + reason; green_required: conditional; prs_required: no; owner_boundary: live site publication; security_disposition: PENDING.

## Affiliate-Websites AU subqueue

### C-AFF-AU1 — AU rewards/referral evidence normalization
- status: PENDING
- owner/workstream: Affiliate AU
- anchor: master `d901b3e...` / `34798980244`; AU user-reward + referral-affiliate requirement remains authoritative.
- objective: normalize official/public AU evidence into `user_reward`, `referral_affiliate`, `country_scope`, `evidence_date`, `source_quality`.
- acceptance: missing required dimension remains HOLD; no payout claim invented.
- dependencies: official terms preferred.
- safe action boundary: public research/docs only.
- verification method: source citations + schema validation.
- next handoff: master program model.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: `S1`; authority_required: public research; negative_tests: marketing page without terms, stale payout claim; receipt_evidence: source/date/fields; green_required: no; prs_required: no; owner_boundary: affiliate signup/publication; security_disposition: PENDING.

### C-AFF-AU2 — country mismatch / worldwide unknown denial
- status: PENDING
- owner/workstream: Affiliate AU
- anchor: same master gate.
- objective: deny CTA when evidence is UK/US-only or worldwide status is unproven for AU.
- acceptance: explicit AU/worldwide evidence required.
- dependencies: C-AFF-AU1 normalized fixtures.
- safe action boundary: fixture tests.
- verification method: country mismatch cases.
- next handoff: AU audit receipt.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: AU fixture tests; negative_tests: UK-only/US-only/unknown-worldwide; receipt_evidence: program/country/source/disposition; green_required: conditional; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

### C-AFF-AU3 — AU CTA audit receipt
- status: PENDING
- owner/workstream: Affiliate AU
- anchor: master gate + C-AFF-AU1/2.
- objective: emit deterministic audit record for program identity, country decision, destination and blocked reason without upgrading HOLD.
- acceptance: receipt is descriptive only; no publish authority.
- dependencies: C-AFF-AU1/2.
- safe action boundary: fixtures/tests.
- verification method: deterministic hash/order.
- next handoff: AU -> Master reconciliation.
- security_gates: `SG-10,SG-11,SG-14,SG-15`; risk_class: `S2`; authority_required: tests; negative_tests: missing program ID/country mismatch; receipt_evidence: exact audit record; green_required: conditional; prs_required: no; owner_boundary: live CTA; security_disposition: PENDING.

## Affiliate-Websites UK subqueue

### C-AFF-UK1 — official network/program evidence refresh
- status: PENDING
- owner/workstream: Affiliate UK
- anchor: master `d901b3e...`; Awin/CJ/Impact/Tradedoubler/Webgains remain discovery context only.
- objective: verify official publisher/referral terms for actual user-reward programs and separate network availability from program eligibility.
- acceptance: official source/date or UNKNOWN; no inference from network presence.
- dependencies: public research.
- safe action boundary: no signup/contact.
- verification method: source/date matrix.
- next handoff: UK fixtures.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: `S1`; authority_required: public research; negative_tests: network membership mistaken for program acceptance; receipt_evidence: official source/date/status; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: PENDING.

### C-AFF-UK2 — regulatory claim boundary fixture
- status: PENDING
- owner/workstream: Affiliate UK
- anchor: existing FCA/ASA sensitivity and initial non-financial focus.
- objective: reject unsupported guaranteed income/reward claims and keep regulated/uncertain offers HOLD.
- acceptance: no guaranteed earnings/payout claim without current evidence.
- dependencies: existing content schema.
- safe action boundary: fixture/content tests.
- verification method: prohibited/unsupported claim matrix.
- next handoff: Marketing safe-claim surface.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: repo tests/docs; negative_tests: guaranteed income, stale rate, regulated offer without evidence; receipt_evidence: claim/source/disposition; green_required: conditional; prs_required: no; owner_boundary: live publication/legal decision; security_disposition: PENDING.

### C-AFF-UK3 — voucher/code attribution abuse denial
- status: PENDING
- owner/workstream: Affiliate UK
- anchor: master verified CTA gate; coupon-abuse suppression remains existing UK constraint.
- objective: block unapproved voucher/code override and ambiguous tracking attribution.
- acceptance: no affiliate destination emitted when attribution integrity is ambiguous/prohibited.
- dependencies: renderer/audit path.
- safe action boundary: tests only.
- verification method: malicious/ambiguous code fixtures.
- next handoff: Master audit model.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: tests; negative_tests: unapproved code override/tracking injection; receipt_evidence: blocked attribution audit; green_required: conditional; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

## Affiliate-Websites US subqueue

### C-AFF-US1 — US reward/referral evidence normalization
- status: PENDING
- owner/workstream: Affiliate US
- anchor: master `d901b3e...` / `34798980244`.
- objective: normalize official US user-reward + referral-affiliate evidence into master schema.
- acceptance: exact country scope, reward, referral path, terms source/date; UNKNOWN preserved.
- dependencies: public official research.
- safe action boundary: no signup/contact.
- verification method: schema + citations.
- next handoff: US CTA fixtures.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: `S1`; authority_required: public research; negative_tests: unsupported payout/worldwide claim; receipt_evidence: program/source/date/status; green_required: no; prs_required: no; owner_boundary: signup/publication; security_disposition: PENDING.

### C-AFF-US2 — publisher/country identity mismatch denial
- status: PENDING
- owner/workstream: Affiliate US
- anchor: same master gate.
- objective: deny CTA when publisher identity/program/country scope disagree.
- acceptance: mismatch yields non-clickable HOLD with audit reason.
- dependencies: normalized US fixtures.
- safe action boundary: tests only.
- verification method: deterministic mismatch tests.
- next handoff: US Overseer reconciliation.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: tests; negative_tests: publisher/program/country mismatch; receipt_evidence: exact identities/reason; green_required: conditional; prs_required: no; owner_boundary: publication; security_disposition: PENDING.

### C-AFF-US3 — outbound destination safety fixture
- status: PENDING
- owner/workstream: Affiliate US
- anchor: same verified CTA gate.
- objective: reject lookalike/non-approved/redirect-confused outbound destinations.
- acceptance: only exact contract-approved destination survives; hidden tracking redirects fail closed.
- dependencies: existing destination parser.
- safe action boundary: fixture tests.
- verification method: redirect/domain confusion cases.
- next handoff: Master renderer.
- security_gates: `SG-06,SG-10,SG-14,SG-15`; risk_class: `S2`; authority_required: test branch; negative_tests: lookalike domain, redirect metadata, tracking override; receipt_evidence: normalized destination/disposition; green_required: conditional; prs_required: no; owner_boundary: live CTA; security_disposition: PENDING.

## GhostKitchen Overseer subqueue

### C-GK-01 — batch status/source metadata validation
- status: PENDING
- owner/workstream: GhostKitchen / economics evidence
- anchor: issue #31; exact pre-scan base `4b217247b73eefcf96f2bfb0140c9150ab4d28a1`; verified economics baseline `ddfb2d872ca116b2cf18d3a98d53670b0c228237` / `34799531732`.
- objective: enforce declared non-authoritative status and non-empty source metadata without allowing prose to upgrade evidence class.
- acceptance: unknown/promotional status and empty/non-string source note denied.
- dependencies: issue #31 bounded batch.
- safe action boundary: tests/tool code only.
- verification method: economics validation CI.
- next handoff: C-GK-02.
- security_gates: `SG-06,SG-07,SG-10,SG-12,SG-14`; risk_class: `S2`; authority_required: branch code/tests; negative_tests: eligibility-like status, malicious/instructional source prose; receipt_evidence: batch metadata/result; green_required: conditional; prs_required: no; owner_boundary: commercial selection/deploy; security_disposition: PENDING.

### C-GK-02 — unknown economics evidence-key denial
- status: PENDING
- owner/workstream: GhostKitchen / economics evidence
- anchor: issue #31/base above.
- objective: reject unknown keys so synthetic economics cannot absorb invented authority/eligibility fields.
- acceptance: schema errors are explicit; no silent field acceptance.
- dependencies: C-GK-01.
- safe action boundary: tests/code validation.
- verification method: unknown-key fixtures.
- next handoff: C-GK-03.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: `S2`; authority_required: branch tests; negative_tests: injected authority/eligibility field; receipt_evidence: schema error path; green_required: conditional; prs_required: no; owner_boundary: deployment; security_disposition: PENDING.

### C-GK-03 — non-promoting economics summary
- status: PENDING
- owner/workstream: GhostKitchen / economics evidence
- anchor: issue #31/base above.
- objective: emit deterministic summary derived only from scenario results.
- acceptance: summary never upgrades commercial eligibility or fills missing supplier/packaging/labour/delivery inputs.
- dependencies: C-GK-01/02.
- safe action boundary: local artifacts/tests.
- verification method: replay/order determinism + no-promotion assertions.
- next handoff: GhostKitchen durable report.
- security_gates: `SG-07,SG-10,SG-11,SG-14`; risk_class: `S2`; authority_required: branch tests; negative_tests: all-fail/all-unknown summary remains non-authoritative; receipt_evidence: input/result hash/summary; green_required: conditional; prs_required: no; owner_boundary: commercial decision; security_disposition: PENDING.

## Franchise Overseer subqueue

### C-FR-01 — tenancy-first evidence fixture
- status: PENDING
- owner/workstream: Franchise / membership-tenancy
- anchor: main `29fa0546f0d7abe03fcc1af3d0770e7e50925c31` / `34799016286` SUCCESS; draft PR #22 `7b8b07562f69ce7988f82e1f3ec71a225fb23709` / `34800298175`, `34800338862` SUCCESS.
- objective: require exact tenant/franchise identity before territory evidence can be consumed.
- acceptance: missing/mismatched tenant denies; synthetic success cannot imply production territory.
- dependencies: fresh exact-head scan.
- safe action boundary: tests/fixtures.
- verification method: exact-head CI.
- next handoff: C-FR-02.
- security_gates: `SG-03,SG-06,SG-10,SG-12,SG-14`; risk_class: `S2`; authority_required: branch tests; negative_tests: tenant mismatch/cross-tenant evidence; receipt_evidence: tenant/territory/result correlation; green_required: conditional; prs_required: no; owner_boundary: production tenancy/deploy; security_disposition: PENDING.

### C-FR-02 — territory freshness/mismatch denial
- status: PENDING
- owner/workstream: Franchise / territory evidence
- anchor: same PR #22 baseline.
- objective: deny stale territory evidence and cross-territory substitution only where current schema supports time/version.
- acceptance: stale/mismatched inputs fail closed; no invented version semantics.
- dependencies: schema inspection.
- safe action boundary: tests.
- verification method: deterministic negative cases.
- next handoff: C-FR-03.
- security_gates: `SG-06,SG-07,SG-10,SG-14`; risk_class: `S2`; authority_required: tests; negative_tests: stale/mismatched territory; receipt_evidence: evidence identity/version/time; green_required: conditional; prs_required: no; owner_boundary: production territory change; security_disposition: PENDING.

### C-FR-03 — audit handoff non-promotion
- status: PENDING
- owner/workstream: Franchise / audit handoff
- anchor: same PR #22 exact baseline.
- objective: record synthetic tenancy/territory result without granting commercial/production authority.
- acceptance: receipt explicitly non-production and cannot mark territory live.
- dependencies: C-FR-01/02.
- safe action boundary: fixture/audit code.
- verification method: receipt schema/replay.
- next handoff: Franchise durable evidence.
- security_gates: `SG-10,SG-11,SG-14,SG-20`; risk_class: `S2`; authority_required: branch tests; negative_tests: attempted live/production flag; receipt_evidence: tenant/territory/source/result/disposition; green_required: conditional; prs_required: no; owner_boundary: live franchise/territory action; security_disposition: PENDING.

## GemVerse Overseer subqueue

### C-GV-01 — recovery action/result correlation
- status: PENDING
- owner/workstream: GemVerse / Level-2 fixture
- anchor: default `0033b66de8e138c199207e33c505db6d8df5345b`; issue #9; draft PR #10 `b1f09c3a9300a24782f5f3e4ab01619a64477319`; run `34803885504` SUCCESS.
- objective: bind recovery decision to exact synthetic action/result identifiers.
- acceptance: mismatch/replay denies recovery success.
- dependencies: fixture schema only.
- safe action boundary: no canonical AgentOS execution.
- verification method: exact-head fixture CI.
- next handoff: C-GV-02.
- security_gates: `SG-09,SG-10,SG-11,SG-14`; risk_class: `S2`; authority_required: branch fixture/tests; negative_tests: action/result mismatch/replay; receipt_evidence: recovery/action/result lineage; green_required: conditional; prs_required: no; owner_boundary: production execution; security_disposition: PENDING.

### C-GV-02 — stale/malformed recovery evidence denial
- status: PENDING
- owner/workstream: GemVerse / Level-2 fixture
- anchor: PR #10 `b1f09c3...`.
- objective: reject malformed/missing evidence and stale evidence only where schema supports time/version.
- acceptance: malformed fields always explicit FAIL/HOLD; no invented version semantics.
- dependencies: schema inspection.
- safe action boundary: fixtures/tests.
- verification method: malformed + supported stale/current matrix.
- next handoff: C-GV-03.
- security_gates: `SG-06,SG-07,SG-09,SG-10,SG-14`; risk_class: `S2`; authority_required: tests; negative_tests: malformed/missing/unexpected keys, stale evidence; receipt_evidence: validation error/version/result; green_required: conditional; prs_required: no; owner_boundary: canonical runtime; security_disposition: PENDING.

### C-GV-03 — duplicate recovery-result idempotency
- status: PENDING
- owner/workstream: GemVerse / Level-2 fixture
- anchor: same PR #10/run.
- objective: replayed recovery result cannot create duplicate synthetic completion/receipt.
- acceptance: one accepted result; duplicate denied/audited.
- dependencies: current fixture contract.
- safe action boundary: tests only.
- verification method: replay CI.
- next handoff: GemVerse durable report; do not claim AgentOS readiness.
- security_gates: `SG-09,SG-10,SG-11`; risk_class: `S2`; authority_required: tests; negative_tests: exact replay/correlation reuse; receipt_evidence: idempotency key/result count; green_required: conditional; prs_required: no; owner_boundary: production runtime; security_disposition: PENDING.

## Content360 Overseer subqueue

### C-C360-01 — current mock-adapter baseline
- status: VERIFIED
- owner/workstream: Content360
- anchor: main `8dd031bb1efaf7d0909bdc411365faf3da497f84`; Test `34791442838` SUCCESS.
- objective: preserve provider-neutral mocked adapter baseline and no credential persistence.
- acceptance: baseline remains non-production/mock only.
- dependencies: none.
- safe action boundary: read-only baseline.
- verification method: exact head/run.
- next handoff: adjacent failure/injection items below.
- security_gates: `SG-05,SG-06,SG-10,SG-14,SG-15`; risk_class: `S0`; authority_required: read-only; negative_tests: no-live baseline; receipt_evidence: exact head/run; green_required: no; prs_required: no; owner_boundary: credentials/live publish; security_disposition: VERIFIED.

### C-C360-02 — provider timeout/rate-limit/malformed-response batch
- status: PENDING
- owner/workstream: Content360
- anchor: C-C360-01 exact baseline.
- objective: deterministic timeout, 429 and malformed-provider failures with bounded retries and zero publish side effect.
- acceptance: explicit failure disposition; retry ceiling enforced; no credential requirement.
- dependencies: mock adapter.
- safe action boundary: mocks/tests only.
- verification method: exact-head Test workflow.
- next handoff: C-C360-03.
- security_gates: `SG-05,SG-06,SG-09,SG-10,SG-12,SG-14`; risk_class: `S2`; authority_required: branch test writes; negative_tests: timeout, 429, malformed response, retry ceiling; receipt_evidence: request ID/mock response/retry/disposition; green_required: conditional; prs_required: no; owner_boundary: API credentials/live publishing; security_disposition: PENDING.

### C-C360-03 — prompt-injection + provenance receipt batch
- status: PENDING
- owner/workstream: Content360
- anchor: C-C360-01 baseline.
- objective: treat provider/content output as data only and correlate request/result provenance without plaintext secrets.
- acceptance: embedded tool-use, secret-disclosure, policy-bypass or publication instructions cannot alter authority/state; result IDs survive retries; secret scan clean.
- dependencies: mock adapter.
- safe action boundary: adversarial fixtures/schema tests.
- verification method: injection tests + deterministic receipts + fixture secret scan.
- next handoff: Marketing consumes only non-production output artifacts.
- security_gates: `SG-05,SG-06,SG-07,SG-09,SG-10,SG-11,SG-14,SG-15`; risk_class: `S2`; authority_required: test branch; negative_tests: tool/policy/secret/publish injection, mismatched result ID, replay; receipt_evidence: request/content/result hashes and denial; green_required: yes if later autonomous path promotes; prs_required: conditional for promoted path; owner_boundary: credentials/publication; security_disposition: PENDING.

## Commercial Frontend Overseer subqueue

### C-CF-01 — direct operator-evidence extraction
- status: PENDING
- owner/workstream: Commercial Frontend
- anchor: `work/commercial-frontend-ecommerce-exception-batch` exact `55b189f99025038a2c9bf9fd15a757225a7ab3be`; report `reports/2026-09-14-commercial-frontend-ecommerce-exception-batch.md`; issue #21 comment `5659574435`.
- objective: classify already-available real operator evidence for frequency, pain, minutes/case, trial intent and WTP.
- acceptance: every record has source and evidence class; no invented demand.
- dependencies: existing internal/public evidence only.
- safe action boundary: no outreach/contact.
- verification method: source-to-record trace.
- next handoff: C-CF-02 or explicit outreach-required BLOCKED classification.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-20`; risk_class: `S1`; authority_required: read-only research; negative_tests: platform docs/anecdote misclassified as operator demand; receipt_evidence: source/persona/problem metric/status; green_required: no; prs_required: no; owner_boundary: outreach/contact; security_disposition: PENDING.

### C-CF-02 — ecommerce exception acceptance fixtures
- status: PENDING
- owner/workstream: Commercial Frontend
- anchor: same `55b189f...` feasibility report.
- objective: encode supplier-stock unavailable, dispatch/ETA uncertainty and order-change exception classes with explicit approval boundaries.
- acceptance: each fixture has source system, stale-state flag, requested decision, approval boundary and audit outcome; no production action.
- dependencies: report taxonomy.
- safe action boundary: docs/fixtures/tests only.
- verification method: schema/replay checks.
- next handoff: prototype only after evidence-safe model.
- security_gates: `SG-06,SG-10,SG-12,SG-14,SG-15`; risk_class: `S2`; authority_required: branch fixtures/tests; negative_tests: stale state, cross-order mismatch, unauthorized approval; receipt_evidence: exception/source/decision/audit; green_required: conditional; prs_required: no; owner_boundary: production order mutation; security_disposition: PENDING.

### C-CF-03 — demand-boundary disposition
- status: PENDING
- owner/workstream: Commercial Frontend
- anchor: same report; platform feasibility VERIFIED, operator demand/WTP UNKNOWN.
- objective: classify validation rows as `AVAILABLE_EVIDENCE` vs `OUTREACH_REQUIRED` and stop at owner boundary.
- acceptance: no fabricated interview/intent/WTP.
- dependencies: C-CF-01.
- safe action boundary: report/classification only.
- verification method: every row has source or explicit blocker.
- next handoff: owner/external research lane only if outreach is required.
- security_gates: `SG-06,SG-10,SG-15,SG-20`; risk_class: `S1`; authority_required: read-only synthesis; negative_tests: inferred WTP from feasibility docs; receipt_evidence: row/source/blocker; green_required: no; prs_required: no; owner_boundary: external outreach/contact; security_disposition: PENDING.

## Marketing / brand integration subqueue

### C-MKT-01 — Founding Beta trust/measurement contract
- status: PENDING
- owner/workstream: Marketing / AgentOS brand integration
- anchor: AgentOS PR #104 exact `83a58b8...` remains blocked; Frontend PR #111 exact `72693c68eedbf4fff7c6a1f4ed573780eed0161c` with AgentOS Tests #1041 / `34821420543` SUCCESS; trust traceability report `2e3c5b13566e4c423db643b3812fa395a8159ca7`.
- objective: define privacy-minimal non-production measurement criteria for Wave-0/Founding-Beta trust objections without implying runtime readiness.
- acceptance: each metric/claim maps to `PROVEN`, `DEMO_ONLY`, `PLANNED`, or `HOLD`; no synthetic Revoke/Henry/PRS/full-Evidence-Timeline claim.
- dependencies: truthful frontend/runtime evidence.
- safe action boundary: docs/content/tests only; no invitations/public beta/campaign.
- verification method: claim-evidence matrix + contradiction scan.
- next handoff: frontend/marketing copy only after evidence check.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15`; risk_class: `S1`; authority_required: non-production content/docs; negative_tests: Level-2 overclaim, Green/PRS implied, production autonomy claim, privacy-overcollection; receipt_evidence: claim/metric/source/state; green_required: no; prs_required: no; owner_boundary: public beta/campaign/publication; security_disposition: PENDING.

### C-MKT-02 — Operator integration/brand shortlist implementation-readiness
- status: PENDING
- owner/workstream: Marketing / Operator integration strategy
- anchor: current portfolio strategy keeps first-wave integrations complementary to AgentOS; latest competitive report `0525c7e6355853aa74c90cd92bb12876e0efbf8d`; n8n/Cline/Roo remain `TO VERIFY`; AgentOS PR #104 is not Level-2 ready.
- objective: maintain a first-wave shortlist with integration surface, official marketplace/install path, auth model, free/paid boundary, evidence date, AgentOS ownership boundary and readiness state.
- acceptance: each candidate is exactly `RESEARCH_READY`, `MOCK_READY`, `OWNER_SETUP_REQUIRED`, or `BLOCKED`; provider never becomes authority source; no credential copied into artifacts.
- dependencies: official/public provider evidence only.
- safe action boundary: research/synthesis; no install/account/credential/spend.
- verification method: dated official sources + architecture-fit check + current-control verification for n8n/Cline/Roo.
- next handoff: AgentOS capability backlog only after canonical runtime gates; Marketing may use evidence-safe positioning.
- security_gates: `SG-02,SG-03,SG-05,SG-06,SG-10,SG-14,SG-20`; risk_class: `S1`; authority_required: public research; negative_tests: provider self-authorization, credential-in-doc, production-ready inference from marketplace listing; receipt_evidence: provider/source/date/readiness/boundary; green_required: no; prs_required: no; owner_boundary: install/credentials/spend; security_disposition: PENDING.

### C-MKT-03 — marketplace/channel claim boundary
- status: PENDING
- owner/workstream: Marketing / commerce brand integration
- anchor: GlobalShopCo still `0 eBay-ready SKUs`; Amazon exact synthetic gate `95191c...` is VERIFIED synthetic only; MyPrime `1820dfe1...` remains `QUALIFIED=0`; eBay actual plan/category fee for GlobalShopCo remains UNKNOWN.
- objective: keep Shopify/eBay/Amazon/Affiliate/Operator claims exactly aligned to verified, synthetic, research-only or blocked evidence states.
- acceptance: no channel-readiness, income, Prime, stock, price, delivery or shop-now claim exceeds evidence.
- dependencies: current Lane B/C states.
- safe action boundary: content matrix and organic non-product-specific assets only.
- verification method: cross-lane contradiction scan.
- next handoff: WordPress/Content360 optimization only in non-production; public publication remains owner boundary.
- security_gates: `SG-06,SG-07,SG-10,SG-14,SG-15,SG-20`; risk_class: `S1`; authority_required: non-production content synthesis; negative_tests: eBay-ready/Amazon-ready/Prime-qualified/guaranteed-income/stock-price claims without evidence; receipt_evidence: claim -> exact evidence anchor; green_required: no; prs_required: no; owner_boundary: campaign/publication; security_disposition: PENDING.

# RECONCILIATION — 2026-09-14 18:30 BRISBANE

- **LANE A:** PR #104 is exact `83a58b8bd230550b5781a0fee700cca250819a75`, OPEN/DRAFT/UNMERGED. Exact-head AgentOS Tests `34821388860` is CANCELLED, so current-head full CI is not inferred PASS/FAIL. PRS independently retargeted current head at `0defebe26f71e1cf5df1168fa5454bfd8de30091` / `34821646371` and reproduced both continuous-ownership false-GREEN cases (`defect_count=2`). Canonical authenticated transport/grant admission remains unwired. A-AG-01/A-AG-03 remain BLOCKED; A-AG-02/A-AG-04 are safe PENDING evidence/test closure. No exact-head Green PASS, therefore no promotion or completion-grade PRS PASS.
- **LANE B:** Amazon granular synthetic preflight is narrowly VERIFIED at `95191c639d2deccd85ed494550e12731fb8ed00e` / `34821710314` SUCCESS (27 deterministic cases). GlobalShopCo free-delivery calculator is narrowly VERIFIED at `f4e5de0e0e946a5c6844dea84d99527d0c9f8474` with `34822003322` and `34822003312` SUCCESS. Current truth remains 0 eBay-ready SKUs; Southern Pet permission and authenticated trade costs are UNKNOWN; actual GlobalShopCo eBay plan/category fee is UNKNOWN; Headless external browser proof is UNKNOWN; MyPrime remains research-only `QUALIFIED=0`.
- **LANE C:** no new exact implementation evidence justifies broad promotion of Affiliate/GhostKitchen/Franchise/GemVerse/Content360/Commercial Frontend. Their prior exact baselines are retained and homogeneous next work remains PENDING. Marketing advanced its evidence layer: Frontend PR #111 `72693c68eedbf4fff7c6a1f4ed573780eed0161c` / `34821420543` SUCCESS, trust traceability `2e3c5b1...`, competitive refresh `0525c7e...`, but Founding Beta remains HOLD and runtime readiness is unchanged.
- **Security:** SG fields are attached only where materially applicable. Synthetic/functional success does not widen security or production authority. Missing permission/freight/identity/stock/economics/environment/credential/physical-host evidence remains HOLD/BLOCKED. Core invariant remains **NO MODEL DECIDES ITS OWN AUTHORITY**.
- Scheduler firing was not treated as completion. No merge/deploy/credential/production mutation/purchase/supplier contact/live publication/production autonomy. **No overall GREEN.**

# NEXT EXECUTION EMPHASIS

1. **LANE A:** establish exact-current-head cross-platform CI; implement only a real continuous-ownership primitive; separately identify/bind the canonical authenticated identity/grant source; then Green and PRS on identical exact head.
2. **LANE B:** apply the verified free-delivery calculator to exact SKUs and close supplier/channel evidence; preserve zero-live-authority eBay/Amazon guards; advance MyPrime source-rights/freshness fixtures.
3. **LANE C:** consume homogeneous pending fixture/evidence batches rather than rescans; prioritize Content360 failure/injection evidence, GhostKitchen issue #31, stable Affiliate/Franchise/GemVerse batches, Commercial Frontend real-evidence classification, and Marketing Operator/claim matrices.
4. Fresh-scan exact head/issue/CI immediately before any state promotion or write. Preserve owner/credential/physical-host/external-evidence blockers and do not broaden scheduled scope.