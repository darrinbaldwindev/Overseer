# Content360 Performance Receipt Schema — 2026-09-12

**Owner:** Marketing Overseer  
**Status:** ACTIVE STANDARD / ANALYTICS-NEUTRAL

## Purpose

Define the minimum durable record for each published campaign asset so marketing performance can be reconciled with source evidence and downstream project decisions.

## Receipt fields

### Identity
- campaign_id
- asset_id
- project
- country/market
- channel
- content360_group
- publish_datetime
- destination_url_or_reference

### Evidence state
- claim_set_id or source references
- evidence_verified_at
- evidence_expiry_at where dynamic
- product/programme/listing identifier where applicable
- claim_status: VERIFIED | QUALIFIED | EDUCATIONAL-NO-LIVE-CLAIM

### Creative
- format
- hook
- CTA
- audience/use-case
- creative_variant
- caption_version

### Performance
Capture only metrics actually available from the platform/analytics source:
- impressions
- reach
- video_views
- video_completion_rate
- likes/reactions
- comments
- saves
- shares
- link_clicks
- CTR
- landing sessions
- product/listing views
- add_to_cart where available
- outbound affiliate clicks
- conversions/signups/sales where attributable
- attributable_revenue where supportable
- spend where paid media is used

Unknown/unavailable metrics remain `UNKNOWN`; never convert missing telemetry into zero.

### Qualitative signal
- common questions
- objections
- sentiment/themes
- requested categories/features
- misinformation/confusion observed
- support burden generated

### Decision
- KEEP
- ITERATE
- SCALE-CANDIDATE
- PAUSE
- RETIRE
- REVERIFY-EVIDENCE

Decision must include a short rationale and must not be based on engagement alone when evidence, margin, stock, programme eligibility or compliance has changed.

## Review windows

Recommended snapshots:
- T+24h: distribution/creative sanity check
- T+7d: primary performance review
- T+30d: campaign-learning review when still relevant

Do not compare channels using raw counts alone; use rates and channel role where possible.

## Governance

Content360/platform analytics are observations, not canonical product facts. A successful post cannot promote an unverified product/programme from candidate to approved state. Marketing may create a research priority from demand signal, but the relevant project workstream must verify the underlying offer before conversion promotion.
