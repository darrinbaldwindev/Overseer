# PROJECT BATCH PROFILES

These profiles customize the canonical `PORTFOLIO-BATCH-ENGINE.md` without forking its procedure. Every Project Overseer reads the engine first, then only its matching profile, then its live project batch.

## AgentOS
- repo: `darrinbaldwindev/AgentOS`
- lane: A / :00
- priorities: Level 2 P0, remote/local bridge, project-file ownership, authenticated authority admission, scheduler/local-wake correlation, recovery, Basic/Everyday frontend, physical Windows acceptance, capability/model routing, observability.
- required evidence: exact-head tests/CI; physical Windows evidence where claimed; Green and PRS on identical lineage where required.
- protected boundaries: no duplicate control plane, unrestricted PowerShell, production autonomy, merge/deploy/credentials.
- special rule: blocked ownership/admission gates remain blocked while adjacent safe work continues.

## PRS
- repo: `darrinbaldwindev/PRS`
- lane: A / assurance
- priorities: independent false-GREEN challenge, evaluator integrity, immutable exact-target probes, duplicate/crash/replay/result-write/identity/approval evidence, physical Windows acceptance contract.
- required evidence: exact target hash/head, independent probe outcome, artifact/provenance hashes where available.
- protected boundaries: PRS does not inherit worker/Green claims and does not certify from execution-produced evidence alone.

## Overseer
- repo: `darrinbaldwindev/Overseer`
- lane: horizontal coordination / :30 reconciliation
- priorities: shared manifest, cross-project dependencies, queue replenishment, stale evidence correction, schedule ownership, control-plane consistency, durable #49 state.
- required evidence: fresh repository/issue/CI state from owning projects.
- protected boundaries: horizontal coordination must not replace Project Overseers or their local batch files.

## GlobalShopCo
- repo: `darrinbaldwindev/GlobalShopCo`
- lane: B / :15
- priorities: exact SKU/supplier qualification, wholesale/landed cost, AU comps, freight/free-delivery economics, permission, stock, returns/warranty, channel readiness.
- fail-closed fields: missing freight, trade cost, permission, stock identity, seller identity or fees => HOLD/UNKNOWN.
- protected boundaries: no supplier contact, purchase, app install, Shopify production mutation, listing publication or spend.

## GlobalShopCo-Headless
- repo: `darrinbaldwindev/GlobalShopCo-Headless`
- lane: B / :15
- priorities: deterministic Shopify->WordPress storefront contract, exact product identity, availability, cart/checkout host integrity, malformed destination denial, safe server-side credentials boundary.
- protected boundaries: Shopify remains canonical commerce/checkout authority; no deployment/secrets/live purchase.

## Shopify to eBay
- repo: `darrinbaldwindev/shopify_ebay`
- lane: B / :15
- priorities: variant/SKU identity, supplier/marketplace permission, inventory evidence, landed economics, fees, fulfilment/seller identity, replay/idempotency, mapping receipts.
- evidence rule: synthetic mapper/gate PASS is not live eBay readiness; exact-head CI required for changed branch claims.
- protected boundaries: network/publication authority remains false until separately authorized.

## Shopify to Amazon
- owning workstream: GlobalShopCo / channel fixtures
- lane: B / :15
- priorities: seller-of-record, permission, Shopify variant/stock identity, category/GTIN, fulfilment, fees/economics, contradiction/freshness handling.
- protected boundaries: no seller setup, live listing, credentials or production mutation.

## MyPrimeDelivery
- repo: `darrinbaldwindev/MyPrimeDelivery`
- lane: B / :15
- established batch path: `docs/overseer/batches/` unless migrated deliberately.
- priorities: authoritative source/right-to-use evidence, Prime/rank/deal freshness, product/category identity, outbound destination, category depth, WordPress presentation readiness.
- evidence rule: public/editorial pages never become Prime/rank/deal authority.
- protected boundaries: provider signup/credentials/live publication remain owner-gated.

## Affiliate-Websites Master
- repo: `darrinbaldwindev/Affiliate-Websites`
- lane: C / :45
- priorities: reusable WordPress architecture, program model, CTA resolution, publication state, disclosure, SEO/AEO, country config, referral-vs-publisher separation.
- evidence rule: UNKNOWN/non-affiliate relationships must not generate monetized CTA.
- protected boundaries: no signup/contact/live publication.

## Affiliate AU
- repo/workstream: `Affiliate-Websites` AU
- lane: C / :45
- priorities: reputable AU user-reward programs, surveys/paid participation, country eligibility, reward economics, referral/publisher route, evidence freshness.
- special rule: AU facts remain country-specific; missing publisher approval => fallback/HOLD.

## Affiliate UK
- repo/workstream: `Affiliate-Websites` UK
- lane: C / :45
- priorities: UK reward/paid-participation programs, Awin/CJ/Impact/Webgains/Tradedoubler evidence where relevant, country eligibility, attribution, disclosure, claim safety.
- special rule: financial/regulatory uncertainty is conservative HOLD; no guaranteed-income claims without evidence.

## Affiliate US
- repo/workstream: `Affiliate-Websites` US
- lane: C / :45
- priorities: high-value paid participation, user testing, focus groups, surveys/rewards, affiliate/referral route, country eligibility and disclosure.
- special rule: reward value and publisher eligibility need separate evidence.

## GhostKitchen
- repo: `darrinbaldwindev/GhostKitchen`
- lane: C / :45
- priorities: representative-order evidence, unit/channel economics, packaging/labour/delivery assumptions, operational fixtures, fail-closed readiness.
- evidence rule: hypothesis/reference economics are not verified profitability.
- protected boundaries: no supplier/partner contact, spend or production changes.

## Franchise
- repo: `darrinbaldwindev/Franchise`
- lane: C / :45
- priorities: tenancy/franchise identity, territory routing, duplicate/overlap denial, evidence/version correlation, deterministic auditability.
- protected boundaries: synthetic/non-production until real tenancy/partner evidence and owner authority exist.

## GemVerse
- repo: `darrinbaldwindev/GemVerse`
- lane: C / :45
- established batch path: `docs/overseer/VERTICAL_BATCH_*.md` until deliberately migrated.
- priorities: source-intake recovery, implementation-evidence reconciliation, exact preimage/target identity, idempotence, competing candidate denial, stale identity/recovery fixtures.
- protected boundaries: do not create an alternate AgentOS control plane or claim executable implementation from documentation alone.

## Content360
- repo: `darrinbaldwindev/content360`
- lane: C / :45
- priorities: governed provider-neutral adapter, request/result integrity, correlation/idempotency, mock failures, READ/OPTIMISE boundary, official API/auth/capability evidence.
- ownership rule: Marketing Overseer owns content direction; Content360 optimizes approved content.
- protected boundaries: credentials remain opaque; no live PUBLISH/SCHEDULE/network/account mutation without explicit authority.

## Commercial Frontend
- owning repo/workstream: `darrinbaldwindev/Overseer` commercial-frontend issues/PRs unless superseded
- lane: C / :45
- priorities: Tradie/service-ops/ecommerce exception workflows, evidence packets, bounded correction/receipts, integration feasibility, measurable operator value.
- evidence rule: pain, demand and willingness-to-pay remain hypothesis until externally evidenced.
- protected boundaries: no customer contact/deployment/account mutation.

## Marketing
- owning repo/workstream: `darrinbaldwindev/Overseer` marketing issues/docs unless superseded
- lane: C / :45
- priorities: AgentOS/GlobalShopCo/Affiliate positioning, claims ladder, landing/ad/content assets, objections, content calendar, influencer/affiliate evidence, Content360-ready packages.
- evidence rule: creation is not campaign validation; compatibility/partner/conversion claims require exact evidence.
- protected boundaries: no campaign activation, spend, outreach or publication without explicit authority.

## Profile maintenance rule
If a project changes materially, update this central profile rather than forking the universal engine. Local live batch files may add temporary task-specific constraints but must not silently override portfolio governance.
## Inherited Work-mode convention — all current and future profiles
Every profile above, including country-specific and non-repository workstreams, inherits owner issue #54 and the Portfolio Batch Engine's Work-mode reconciliation and carry-forward section. Maintain WORK_MODE_QUEUE as a small section in the established batch/control log referencing existing task IDs, not as a separate queue or persistence plane. Record objective, why Work is needed, chat-side preparation complete/UNKNOWN, exact source/head, blockers, acceptance/tests and protected boundary. The Portfolio Overseer reconciles these candidates against live ownership and previous-batch receipts. Current per-project adoption is not implied until that project consumes this updated profile.
