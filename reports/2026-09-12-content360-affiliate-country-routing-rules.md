# Content360 Affiliate Country Routing Rules — 2026-09-12

**Owner:** Marketing Overseer  
**Status:** ACTIVE CONTROL SPEC

## Purpose

Prevent country-mismatched programme claims, stale referral offers and incorrect monetised links from being distributed through Content360.

## Required metadata per affiliate content item

Every named-programme content package must carry:
- `program_name`
- `program_type`: publisher_affiliate | member_referral | editorial_only
- `country_scope`: AU | UK | US | GLOBAL | explicit list
- `affiliate_status`: not_applied | pending | approved | rejected | editorial_only
- `source_verified_at`
- `terms_recheck_at`
- `monetised_link_allowed`: yes/no
- `content360_group`
- `campaign_id`
- `disclosure_required`: yes/no

## Routing rule

A content item may be scheduled into a country group only when that country is explicitly included in `country_scope` and the factual claims remain within their current evidence window.

## Monetised routing

A monetised affiliate link may only be scheduled when:
1. `program_type = publisher_affiliate` or an explicitly permitted publisher-use hybrid;
2. `affiliate_status = approved`;
3. the destination/tracking link belongs to the approved publisher account;
4. the promoted country is allowed by programme terms;
5. disclosure is present where required;
6. the campaign does not use prohibited traffic methods;
7. the offer terms have not expired or materially changed.

Member-referral links must never be silently substituted for publisher-affiliate links.

## Country groups

### Affiliate Websites AU

Allowed now:
- country-level education about paid surveys/research/reward platforms;
- current editorial facts for Australian availability;
- Ipsos iSay AU member-referral explanation as a consumer/member programme, with dated verification;
- PrizeRebel editorial coverage if AU availability remains current.

Blocked until approved:
- monetised Awin programme links not explicitly available to AU traffic;
- claims that Ipsos iSay AU is a publisher-affiliate programme;
- LifePoints AU referral CTA while first-party evidence says no referral programme.

### Affiliate Websites UK

Allowed now:
- educational comparison content;
- verified non-referral reviews;
- PrizeRebel editorial coverage where UK availability remains current;
- Awin publisher/network education.

Blocked:
- Ipsos iSay UK referral CTA while first-party evidence says Refer a Friend is unavailable;
- stale screenshots/posts containing former UK referral wording;
- financial/reward claims without current programme terms.

### Affiliate Websites US

Allowed now:
- editorial content on SurveyRewards US and QuickRewards using current public programme facts;
- Awin publisher-network education;
- PrizeRebel editorial/referral explanation subject to current terms.

Monetised links remain blocked until the relevant publisher application is approved and the approved tracking links are available.

## Content360 automation guardrails

RSS and bulk-import automation must not bypass programme-level metadata checks. If an article mentions multiple programmes, the social excerpt must not convert an editorial comparison into an unsupported earnings claim.

If `terms_recheck_at` has passed, Content360 scheduling status becomes `HOLD_REVERIFY` for any post containing dynamic payout, referral, country-availability or promotion-right claims.

## Disclosure pattern

For monetised posts, use a clear nearby disclosure such as:

> We may earn a commission if you join through an affiliate link. This does not change the reward you receive unless the programme terms explicitly say otherwise.

Do not imply that the affiliate relationship determines editorial ranking.

## Traffic-quality rule

Never use Content360 automation to generate spam, misleading urgency, fake scarcity, bulk unsolicited DMs, incentivised traffic where prohibited, or repeated posts intended to evade platform/programme controls.

## Change handling

When programme terms change:
1. mark affected content `HOLD_REVERIFY`;
2. remove/disable stale scheduled posts;
3. update the programme register;
4. update country-safe post copy;
5. create a fresh source timestamp;
6. only then resume distribution.
