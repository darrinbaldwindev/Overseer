# Content360 Overseer — Repo Scan Reconciliation — 2026-09-13

**Owner:** Content360 Overseer  
**Status:** ACTIVE / DISTRIBUTION-READY-IN-PRINCIPLE / NOT PUBLISHED  
**Scope:** Reconcile current Overseer/Marketing Content360 artefacts into one current execution state without changing Marketing Overseer strategy or product facts.

## Repo scan result

The current Overseer repository already contains a substantially mature Content360 operating layer. Content360 should no longer be treated as a blank calendar/scheduling task.

Current durable controls found and reconciled:

- portfolio marketing matrix and seven-group architecture;
- initial campaign register with campaign IDs and funnel/destination mapping;
- campaign ID + UTM standard;
- evidence-expiry/recheck rules;
- performance-receipt schema;
- portfolio learning loop;
- release-readiness packets;
- first safe release manifest;
- unblock queue;
- current unblock evidence status;
- Affiliate AU/UK/US country-routing rules and country-safe post pack;
- GlobalShopCo, Shopify→eBay, Affiliate and GhostKitchen/Franchise Content360 plans/libraries.

The current repo head inspected during this pass was `afa93be7518fa736930237896b780f058ff146e1` (2026-09-13), with newer non-Content360 portfolio work including AgentOS Founding Beta and commercial-frontend validation. No newer Content360 control document was found that supersedes the 2026-09-12 Content360 standards during this scan.

## Current role boundary

Marketing Overseer owns:
- campaign strategy;
- approved master content;
- offer/product truth;
- audience/commercial positioning;
- claim state/evidence decisions.

Content360 Overseer owns:
- channel-native adaptation;
- account/group routing;
- formatting/cropping/short-form transformation;
- cadence/scheduling preparation;
- UTM/campaign attribution implementation;
- evidence-expiry enforcement before schedule/repost;
- publication verification records;
- performance receipts and distribution analytics feedback.

Content360 does not become the canonical scheduler, campaign authority, product source of truth, mission ledger, governance layer or approval authority.

## First safe release state

### AgentOS
Ready in principle for Content360 optimisation:
- `AOS-FREEAI-01` — “You already have AI. AgentOS helps you make the most of it.”
- `AOS-PUTAI-01` — “Put AI to work.”
- `AOS-TEAM-01` — Willow / Isla / Jack / Henry roles.
- `AOS-OPERATOR-01` — `$99/year — less than $2/week`.

Hold:
- benchmark-result claims;
- quantified savings/ROI;
- broad Night Shift claims;
- broad Windows-worker/remote execution proof;
- shipped Ollama/Libra claims without implementation evidence.

### GlobalShopCo
Ready in principle:
- selection/brand philosophy;
- product-vetting transparency;
- Home Organisation education;
- shortlist/reject behind-the-scenes content.

Hold:
- named SKU conversion;
- price/stock/delivery/free-delivery claims without current evidence;
- margin/value claims dependent on missing freight.

### Shopify → eBay
Ready in principle:
- category montage/education;
- Home Storage, Pet, Kitchen/Pantry and other established category content;
- trust/evidence-process content.

Hold:
- exact live listing/price/shipping/returns CTA until listing evidence is current.

### Affiliate AU
Ready in principle:
- evergreen trust/scam/opportunity-type/disclosure content;
- dated Ipsos iSay AU member-referral editorial, subject to freshness recheck.

Important boundary: member referral is not automatically a publisher affiliate programme.

### Affiliate UK
Ready in principle:
- generic rewards/research education;
- scam/red-flag content;
- current correction that legacy Ipsos iSay Refer a Friend is unavailable, subject to current first-party recheck before publication.

Hold named referral/affiliate promotion unless separately verified.

### Affiliate US
Ready in principle:
- generic paid-participation education;
- affiliate-vs-referral explainer;
- dated editorial profiles of SurveyRewards/QuickRewards as network-level publisher candidates.

Hold monetised outbound affiliate deployment until actual publisher/network approval and traffic/country eligibility are verified.

### GhostKitchen / Franchise
Ready in principle:
- delivery-first education;
- operating-system explainers;
- build-in-public progress;
- unit-economics education without earnings promises.

Hold earnings, payback, profitability, demand, compliance-complete and sensitive legal/tax/Centrelink claims.

### HOLD
- GemVerse public Content360 activation;
- MyPrimeDelivery public Content360 activation;
- consumer PRS/Overseer feeds.

## Attribution standard now controlling

Campaign IDs use:

`C360-{PROJECT}-{COUNTRY}-{FUNNEL}-{THEME}-{YYYYMM}-{NN}`

Asset IDs use:

`{CAMPAIGN-ID}-{FORMAT}-{VARIANT}`

UTM source/medium/campaign/content values must follow the existing active standard. Campaign IDs must never be recycled for materially different messages, offers, audiences or destinations.

## Evidence-expiry behaviour now controlling

- Class A fast-changing commercial facts: recheck before publication and before any repost older than 72 hours.
- Class B programme/offer facts: recheck before publication and every 30 days while actively promoted, or immediately after known policy change.
- Class C product specs: recheck against the exact canonical listing/source before first promotion and when identity changes.
- Class D stable educational/brand statements: recheck on source-of-truth/product-direction change.

If evidence expires, Content360 action is fail-closed:
- hold direct conversion CTA;
- hold scheduled repost;
- remove/qualify dynamic claim only within Marketing-approved bounds;
- mark `REVERIFY-EVIDENCE`;
- request bounded recheck from the owning project workstream.

## Publication verification / analytics contract

Content360 queue acceptance is not publication proof.

For each published asset retain where available:
- campaign ID;
- asset ID;
- Content360 group/post/source ID;
- social platform post ID/URL;
- publish timestamp;
- destination/reference;
- evidence verified/expiry state;
- creative/caption variant;
- T+24h, T+7d and (when relevant) T+30d performance receipts.

Missing telemetry remains `UNKNOWN`, never silently zero.

Analytics can drive creative/audience/research priorities but cannot promote an unverified product, programme, feature or claim into an approved state.

## New cross-portfolio observation from 2026-09-13 scan

The AgentOS Founding Beta readiness playbook is now present and explicitly held until product readiness. This creates a future Content360 recruitment/distribution use case, but no Content360 beta-recruitment campaign should be activated yet. When the product gate clears, Marketing Overseer should own the recruitment proposition/content and Content360 Overseer should adapt it into approved local/Australian and later international recruitment channel variants.

## Current autonomous next actions

1. Treat the Marketing Overseer first-safe-release manifest as the controlling starter batch.
2. Build Content360-ready release packets from those approved assets rather than inventing new content.
3. Prioritise AgentOS Batch A, then GlobalShopCo category/trust content, then eBay category/trust content, then Affiliate country-safe evergreen/editorial packs, then GhostKitchen/Franchise pre-launch education.
4. Keep all blocked conversion/proof campaigns out of the scheduler until their evidence gates clear.
5. Apply active campaign-ID/UTM and evidence-expiry standards to every future optimisation packet.
6. When platform accounts are connected and publication authority is explicitly granted, verify actual publication separately from Content360 queue state and create performance receipts.
7. Preserve Content360 as a replaceable downstream distribution worker under AgentOS/portfolio governance.

## Boundaries preserved

This scan/reconciliation does not authorise production publishing, paid spend, account connection changes, credential changes, affiliate applications, supplier contact, direct customer messaging, auto-DM sales flows, merges, deployments or production autonomy.
