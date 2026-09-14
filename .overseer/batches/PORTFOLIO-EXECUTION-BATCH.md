# Portfolio Execution Batch Manifest

**Purpose:** bounded execution manifest consumed by existing ChatGPT schedules and manual `cont` / `continue autonomously vertically` cycles. This is not a scheduler, authority source, mission ledger, registry, Green system, PRS system, or project source of truth. Live repository/issues/runtime evidence remains authoritative.

**Manual rule:** `cont` / `continue autonomously vertically` means: (1) fresh thorough repository scan before action, (2) consume as much safe useful work as possible, (3) fresh thorough scan again before reconciliation/replenishment, (4) replenish this same file before returning control.

**Schedule rule:** :00 LANE A, :15 LANE B, :30 reconcile/replenish, :37 independent assurance guard, :45 LANE C.

## Mandatory fresh-scan doctrine
Before acting, refresh branch/head, recent commits, relevant issues/comments/PRs, CI/workflows, and implicated files/tests/contracts. Before replenishing, scan the relevant repositories again for moved heads, concurrent work, duplicate completion, new CI, stale assumptions and changed blockers. Manifest text never overrides fresh evidence.

## Batch lifecycle
1. Fresh-scan target state.
2. Execute multiple safe items; blocked work must not terminate a pass while other eligible work exists.
3. Reconcile as `PENDING`, `ACTIVE`, `VERIFIED`, `BLOCKED`, `STALE`, or `SPLIT_REQUIRED` with exact evidence.
4. VERIFIED GREEN gates may expand into 2–5 homogeneous adjacent items.
5. Mixed-confidence/failed work splits and fails closed.
6. Fresh-scan again before replenishment.
7. No entry grants merge/deploy/credentials/production writes/purchases/supplier contact/listing publication/campaign activation/production autonomy.

---

# LANE A — AGENTOS LEVEL 2 P0 (:00)

### A-001 — Continuous ownership fence
- status: BLOCKED
- fresh exact head: `083b7decf48038764ec846a988a5cd30d2a4fa56`
- PR #104: OPEN / DRAFT / UNMERGED.
- blocker: unresolved check-to-publish ownership race; no kernel-enforced ownership primitive held continuously through publish/recovery/success receipt.
- no exact-head full CI PASS, new independent Green PASS or PRS PASS is claimed.
- next: only act if a real ownership primitive appears; then exact-head Windows+Ubuntu CI -> independent Green -> PRS on unchanged head.

### A-002 — Ownership adversarial regressions
- status: BLOCKED
- dependency: A-001 primitive must change first.
- next eligible homogeneous batch: replacement-after-verification; three-writer successor; stale/replaced identity; crash/replay; duplicate-result/false-success.

### A-003 — Authority/admission continuation
- status: ACTIVE
- implementation requires authenticated actor context and canonical grant evidence at the admission seam, but trusted transport identity/grant lookup are not yet wired end-to-end.
- next: bind existing trusted transport actor context + canonical grant source into the existing producer/pickup lineage; no self-granting request fields or duplicate authority layer.

### A-004 — Authority-source binding regression set
- status: PENDING
- next batch: missing authenticated actor; actor/grant mismatch; missing canonical grant evidence; delivery/request/task/mission/wake correlation preservation.

---

# LANE B — COMMERCE PRIORITY (:15)

### B-001 — GlobalShopCo Home Organisation economics closure
- status: PENDING / HOLD-PRESERVING
- GlobalShopCo #9 remains the active Home Organisation gate.
- verified example: United Living / Boxsweden SKU `15510`, EAN `9340957115510`.
- still UNKNOWN/HOLD: wholesale cost, candidate-level outbound freight, dropship/blind-shipping permission, sellable stock assurance, positive free-delivery contribution.
- next: continue non-duplicate exact-SKU evidence closure. Do not infer missing economics.

### B-002 — GlobalShopCo-Headless M3 checkout
- status: VERIFIED
- fresh exact head after pre-replenishment scan: `9799e6fe5a9c72e42e1554949697a64acce14bd4`
- CI: M3 checkout validation `34798624627` SUCCESS.
- concurrent scheduled work advanced the branch with `test(m3): cover checkout authority ambiguity batch`; do not duplicate it.
- replenished batch: PENDING
  1. inspect exact `9799e6f...` diff before further expansion;
  2. add only non-duplicate malformed/authority-boundary cases still absent after that inspection;
  3. preserve exact-host HTTPS fail-closed semantics and no-purchase rendering on invalid checkout destinations.
- external dev-store/browser checkout proof remains UNKNOWN.

### B-003 — Shopify -> eBay readiness
- status: PENDING
- next: deterministic candidate mapper/readiness with marketplace permission, fulfilment identity, stock method and landed economics. No publication authority.

### B-004 — Shopify -> Amazon readiness
- status: PENDING
- next: seller-of-record/category/GTIN/fulfilment/economics evidence model; no seller setup or publication.

### B-005 — MyPrimeDelivery synthetic WordPress slice
- status: VERIFIED
- exact head: `528b5aabb778e490e603abf6463e6eff658c4e53`
- CI: Fixture validation `34798642173` SUCCESS.
- consumed this pass: duplicate product_id/ASIN fail closed; product category_id mismatch fails closed; ranking_method_id mismatch fails closed; non-current/non-verified product evidence cannot create positive Prime/ranking/outbound presentation.
- replenished batch: PENDING
  1. missing/empty category_id or ranking_method_id must fail closed;
  2. empty product batch must remain explicit and non-positive rather than implying ranked inventory;
  3. product marketplace/category marketplace mismatch must fail closed or suppress positive presentation;
  4. ranking evidence source/method identity disagreement must fail closed before ranking presentation.
- boundary: synthetic only; no live Prime/ranking/affiliate claims.

---

# LANE C — PRODUCT / CONTENT / VENTURES (:45)

### C-001 — Affiliate Websites governed CTA/program evidence
- status: VERIFIED
- fresh exact head: `de598e42bee2bafb9dc9b017f9dc03286d3c7600`
- CI: Commercial CTA fixture validation `34796872773` SUCCESS.
- replenished batch: PENDING
  1. explicit conflicting publisher evidence must block VERIFIED_PUBLISHER CTA;
  2. country eligibility evidence must be independent from publisher relationship evidence;
  3. disclosure-present gate must be required for publishable synthetic CTA;
  4. synthetic commercial-resolution audit event must record blocked/allowed reason without production tracking URLs.

### C-002 — GhostKitchen economics batch
- status: VERIFIED
- exact head: `10a519c59ad63e2c71b0c0d96e9c4a09da8c9c93`
- CI: Economics validation `34798678519` SUCCESS.
- consumed this pass: missing/duplicate scenario_id fail closed; non-numeric required values identify the field; negative cost inputs are rejected; batch output is deterministically sorted by scenario identity.
- replenished batch: PENDING
  1. define/fail-close negative net-customer-revenue policy explicitly;
  2. reject duplicate/unknown required-input keys where they could create ambiguous economics evidence;
  3. empty scenario batch must remain explicit and non-commercial;
  4. batch evaluation must remain deterministic when input object key order changes.
- boundary: public/hypothesis benchmarks remain decision support, not project economics proof.

### C-003 — Franchise territory/tenancy validation
- status: VERIFIED
- fresh exact head: `9d58ad13e3846a6dfaba02793a54e390f50b49e0`
- CI: Territory fixture validation `34796848783` SUCCESS.
- replenished batch: PENDING
  1. duplicate franchise IDs fail closed;
  2. duplicate routing case IDs fail closed;
  3. missing/empty postcode tokens fail closed;
  4. correlation remains deterministic under harmless input ordering while changing on material routing/version changes.

### C-004 — GemVerse Level 2 fixture assurance
- status: VERIFIED
- fresh exact head: `fd57ce4cd1a5455cc00c9d5e3e7a445710a18a36`
- CI: Level 2 fixture validation `34796879316` SUCCESS.
- replenished batch: PENDING
  1. extra/unrecognised prepared metadata fields fail closed explicitly;
  2. stale current-state + canonical prepared target recovery remains deterministic;
  3. prepared/current identity disagreement reports a specific recovery denial reason;
  4. recovery result includes enough synthetic evidence to distinguish promoted vs already-complete without mutating canonical fixture.

### C-005 — Content360 provider-neutral adapter
- status: PENDING
- next: consume official/public contract evidence when available; extend request/result schemas and mock failures; no credential/live publish.

### C-006 — Commercial Frontend workflow evidence
- status: PENDING
- next: deepen Tradie/Ecommerce cross-system exception evidence; customer pain/frequency/WTP remain UNKNOWN until evidenced.

### C-007 — AgentOS marketing/product objection acceptance
- status: PENDING
- target: AgentOS #109
- next: convert objections into testable onboarding/pricing/demo evidence; planned mitigation != proof.

---

# INDEPENDENT PRS CHECKPOINT
- status: VERIFIED for evaluator-parity cleanup only
- exact head: `a646f4033fd1b0c40135cb6f5c1286e9c7610728`
- CI: `34793554142` SUCCESS.
- does not imply AgentOS PR #104 assurance or overall GREEN.

# MANUAL RECONCILIATION — 2026-09-14 12:xx AEST
- Fresh pre-action scan completed before consuming work.
- Manual execution advanced MyPrimeDelivery and GhostKitchen.
- MyPrimeDelivery exact head `528b5aa...` / CI `34798642173` SUCCESS.
- GhostKitchen exact head `10a519c...` / CI `34798678519` SUCCESS.
- Fresh pre-replenishment scan broadened across active batch repos and caught concurrent GlobalShopCo-Headless advancement to `9799e6f...`; exact-head CI `34798624627` SUCCESS, so prior B-002 work is not duplicated.
- Affiliate-Websites remains `de598e42...`; Franchise remains `9d58ad13...`; GemVerse remains `fd57ce4c...`; AgentOS PR #104 remains OPEN/DRAFT at `083b7dec...` and A-001/A-002 remain fail-closed.
- No scheduler firing or worker claim was treated as completion. No overall GREEN.

# NEXT PASS ORDER
1. Fresh-scan every target before action.
2. LANE A: A-001 only on new primitive evidence; otherwise A-003/A-004 without bypassing A-001.
3. LANE B: B-001 first; inspect current Headless `9799e6f...` before any adjacent expansion; B-005 new identity/evidence batch is ready.
4. LANE C: C-001/C-003/C-004 remain ready homogeneous batches; C-002 has a new post-GREEN economics batch; C-005/C-006/C-007 remain useful PENDING work.
5. Fresh-scan again before replenishment and preserve all HOLD/BLOCKED/UNKNOWN states.
