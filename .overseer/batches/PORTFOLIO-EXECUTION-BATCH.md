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
- current seam still lacks trusted transport identity + canonical grant lookup wired end-to-end.
- next: bind existing trusted transport actor context + canonical grant source into the existing producer/pickup lineage; no self-granting request fields or duplicate authority layer.

### A-004 — Authority-source binding regression set
- status: PENDING
- next batch: missing authenticated actor; actor/grant mismatch; missing canonical grant evidence; delivery/request/task/mission/wake correlation preservation.

---

# LANE B — COMMERCE PRIORITY (:15)

### B-001 — GlobalShopCo Home Organisation economics closure
- status: PENDING / HOLD-PRESERVING
- fresh issue state: GlobalShopCo #9 remains OPEN and Home Organisation remains the active gate.
- verified example: United Living / Boxsweden SKU `15510`, EAN `9340957115510`.
- still UNKNOWN/HOLD: wholesale cost, candidate-level outbound freight, dropship/blind-shipping permission, sellable stock assurance, positive free-delivery contribution.
- next: continue non-duplicate exact-SKU evidence closure. Do not infer missing economics.

### B-002 — GlobalShopCo-Headless M3 checkout
- status: VERIFIED
- fresh exact head: `9799e6fe5a9c72e42e1554949697a64acce14bd4`
- CI: M3 checkout validation `34798624627` SUCCESS.
- fresh diff inspected this cycle: current batch already covers unexpected host, suffix-confusable host, HTTP downgrade, userinfo credential-host confusion, unexpected explicit port, malformed URL, missing checkoutUrl, unavailable variant and exact non-production host override.
- replenished batch: PENDING
  1. inspect production plugin host-normalization code, not just test fixture, before adding more cases;
  2. test trailing-dot / case-normalized exact-host handling only if plugin semantics leave ambiguity;
  3. preserve exact-host HTTPS fail-closed semantics and no-purchase rendering on invalid destinations.
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
- fresh exact head: `d901b3e2c0c772cdc43019dd96cf2b19bdded0a6`
- CI: Commercial CTA fixture validation `34798980244` SUCCESS.
- consumed this cycle: explicit conflicting publisher evidence blocks VERIFIED_PUBLISHER; country eligibility evidence is independently required; disclosure must be present; deterministic synthetic commercial-resolution audit events record ALLOWED/BLOCKED reason with `tracking_url: null`.
- replenished batch: PENDING
  1. validate publisher verification timestamp shape/future-dated evidence fail-closed in fixture contract;
  2. reject country/eligibility evidence mismatch that claims another country;
  3. ensure blocked audit events cannot contain destination/tracking data even if malformed input attempts it;
  4. make audit event ordering deterministic by program identity independent of input order.

### C-002 — GhostKitchen economics batch
- status: VERIFIED
- fresh exact head remains `10a519c59ad63e2c71b0c0d96e9c4a09da8c9c93`
- CI: Economics validation `34798678519` SUCCESS.
- replenished batch: PENDING
  1. define/fail-close negative net-customer-revenue policy explicitly;
  2. reject unknown required-input keys where they could create ambiguous economics evidence;
  3. empty scenario batch must remain explicit and non-commercial;
  4. batch evaluation deterministic when input object key order changes.

### C-003 — Franchise territory/tenancy validation
- status: VERIFIED
- fresh exact head: `29fa0546f0d7abe03fcc1af3d0770e7e50925c31`
- CI: Territory fixture validation `34799016286` SUCCESS.
- consumed this cycle: duplicate/missing franchise IDs fail closed; duplicate/missing routing case IDs fail closed; active areas and routing cases reject empty postcode tokens; correlation canonicalizes matched areas/owners so harmless list ordering does not change identity while material version changes still do.
- replenished batch: PENDING
  1. reject duplicate inactive area IDs as identity ambiguity too, not only active duplicates;
  2. validate franchise status enum rather than treating arbitrary non-ACTIVE text as inactive;
  3. validate delivery-area status enum explicitly;
  4. deterministic output case ordering by case_id independent of routing_cases input order.

### C-004 — GemVerse Level 2 fixture assurance
- status: VERIFIED
- fresh exact head: `0033b66de8e138c199207e33c505db6d8df5345b`
- CI: Level 2 fixture validation `34799040874` SUCCESS.
- consumed this cycle: extra/missing prepared metadata fields fail closed explicitly; recovery denial reasons distinguish invalid current state, prepared identity, payload mismatch and candidate ambiguity; successful results carry synthetic evidence distinguishing PROMOTE_PREPARED from ALREADY_COMPLETE; repeated recovery remains byte-stable and canonical fixture unchanged.
- replenished batch: PENDING
  1. bind recovery evidence to exact current-state hash as well as preimage/target metadata;
  2. reject recovery evidence replay if action/current-state combination disagrees;
  3. deterministic denial record for competing candidates without leaking arbitrary candidate payload;
  4. recovery result schema validation for required evidence fields and no unrecognised fields.

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

# MANUAL RECONCILIATION — 2026-09-14 OWNER-TRIGGERED CYCLE
- Fresh pre-action repository scan completed before consuming work.
- Manual execution advanced Affiliate-Websites, Franchise and GemVerse.
- Affiliate exact head `d901b3e...` / CI `34798980244` SUCCESS.
- Franchise exact head `29fa054...` / CI `34799016286` SUCCESS.
- GemVerse exact head `0033b66...` / CI `34799040874` SUCCESS.
- Fresh pre-replenishment scan completed across active scheduled-priority repos: AgentOS PR #104 remains `083b7dec...` OPEN/DRAFT/BLOCKED; GlobalShopCo #9 remains OPEN/HOLD; Headless remains `9799e6f...`; MyPrimeDelivery remains `528b5aa...`; GhostKitchen remains `10a519c...`.
- Headless current diff was inspected before replenishment; no already-covered checkout ambiguity case was recreated.
- No scheduler firing or worker claim was treated as completion. No overall GREEN.

# NEXT PASS ORDER
1. Fresh-scan every target before action.
2. LANE A: A-001 only on new ownership-primitive evidence; otherwise A-003/A-004 without bypassing A-001.
3. LANE B: B-001 first; B-002 plugin-code inspection; B-005 next synthetic identity/evidence batch; B-003/B-004 remain useful bounded readiness work.
4. LANE C: consume new C-001/C-003/C-004 homogeneous batches; C-002 remains ready; C-005/C-006/C-007 remain useful PENDING work.
5. Fresh-scan again before replenishment and preserve all HOLD/BLOCKED/UNKNOWN states.
