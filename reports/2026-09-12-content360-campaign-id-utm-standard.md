# Content360 Campaign ID + UTM Standard — 2026-09-12

**Owner:** Marketing Overseer  
**Status:** ACTIVE STANDARD

## Purpose

Create one portfolio-wide naming and attribution convention so Content360, social posts, landing pages, ecommerce listings and affiliate content can be reconciled without inventing a second analytics/source-of-truth system.

## Campaign ID format

`C360-{PROJECT}-{COUNTRY}-{FUNNEL}-{THEME}-{YYYYMM}-{NN}`

Examples:
- `C360-AGENTOS-GLOBAL-TOF-FREEAI-202609-01`
- `C360-GSC-AU-MOF-HOMEORG-202609-01`
- `C360-GSC-EBAY-AU-BOF-HOMESTORAGE-202609-01`
- `C360-AFF-AU-MOF-SURVEYS-202609-01`

## Project codes

- AGENTOS = AgentOS
- GSC = GlobalShopCo
- GSC-EBAY = Shopify→eBay
- AFF-AU = Affiliate Websites Australia
- AFF-UK = Affiliate Websites United Kingdom
- AFF-US = Affiliate Websites United States
- GK = GhostKitchen
- FR = Franchise

## Funnel codes

- TOF = awareness / education
- MOF = consideration / comparison / proof
- BOF = conversion / direct CTA
- RET = retention / re-engagement / referral
- PRE = pre-launch / waitlist / interest

## UTM standard

Use lowercase values:

- `utm_source` = facebook | instagram | tiktok | youtube | x | linkedin | pinterest | content360
- `utm_medium` = social | paid_social | video | rss | affiliate | referral
- `utm_campaign` = exact campaign ID lowercased
- `utm_content` = asset ID or creative variant
- `utm_term` = optional category/audience keyword; never sensitive-personal-category targeting

Example:
`?utm_source=instagram&utm_medium=social&utm_campaign=c360-agentos-global-tof-freeai-202609-01&utm_content=freeai-carousel-a`

## Asset ID format

`{CAMPAIGN-ID}-{FORMAT}-{VARIANT}`

Formats:
- IMG
- CAR
- VID
- TXT
- STORY
- SHORT
- ARTICLE
- EMAIL

Example:
`C360-AGENTOS-GLOBAL-TOF-FREEAI-202609-01-CAR-A`

## Destination rule

Every campaign record must identify one canonical destination type:
- product/category page
- eBay listing/category
- country affiliate article
- AgentOS landing page
- waitlist/interest page
- no-link engagement content

The destination itself remains authoritative for live price, stock, offer, eligibility and programme terms.

## Change-control rule

Do not recycle campaign IDs for materially different messages, offers, audiences or landing destinations. Create a new sequence number so historical analytics stay interpretable.
