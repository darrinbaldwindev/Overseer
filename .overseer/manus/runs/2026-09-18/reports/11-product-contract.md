# Cross-commerce Product Evidence Contract

**Batch:** Overseer repository batch dated 2026-09-18  
**Lane:** Cross-commerce Product Evidence contract  
**Observed-date convention:** All observations below were made on **2026-09-18** (UTC+10 sandbox date). A source's own publication or update date is reported when the source exposes one.

## Executive conclusion

A defensible cross-commerce product-evidence contract can standardize **what was observed, where, when, and with what access scope**, but it cannot turn a public listing into a purchase guarantee or an authenticated seller fact. The minimum portable record is an item or product identifier, marketplace and locale, seller/offer context when exposed, condition, displayed price and currency, displayed availability signal, shipping/fulfilment statements, source URL or API operation, access mode, observation timestamp, and evidence freshness. Each value must retain its provenance and uncertainty.

The strongest public evidence in this review is the eBay Browse API's documented item response, which explicitly covers description, price, condition, shipping, estimated delivery, and seller information, and provides a compact change-check group containing price, estimated availability, GTIN, shipping options, and seller revision fields [1]. eBay's separate Inventory API documentation shows why seller-authorized inventory evidence is a different class: quantity, offer price, location, policies, and publication state belong to a seller's authenticated inventory/offer workflow [2]. Walmart likewise describes its Marketplace APIs as access for sellers and approved solution providers, with OAuth credentials and access tokens required [3]. Amazon's public Conditions of Use expressly warns that it cannot confirm a price until order and that product content may not be current or error-free [4]. Amazon's official notice also says PA-API 5 is deprecated, returns 403 for continued calls, and directs integrations to the Creators API [5].

Therefore, the contract should report a displayed offer as **observed evidence at a timestamp**, not as authenticated wholesale cost, permission to sell, Prime status, earnings, legal certainty, security, or guaranteed availability.

## Evidence matrix

| Contract field / assertion | Portable representation | Evidence class | What the reviewed sources support | Explicit non-claims and caveats |
|---|---|---|---|---|
| Marketplace and locale | `marketplace`, `country`, `locale`, `observed_at` | **VERIFIED FACT** when returned or recorded from the source | eBay requires/uses marketplace context; outside the US, `X-EBAY-C-MARKETPLACE-ID` is required, with `EBAY_US` as default if absent [1]. | Locale does not establish shipping eligibility, tax treatment, or legal availability in a buyer's jurisdiction. |
| Product identity | `gtin`, marketplace product ID, item ID, SKU if authenticated | **VERIFIED FACT** only for the exact returned identifier | eBay documents a unique RESTful item ID and exposes GTIN in its compact response; product identifiers may be returned when a seller associated an ePID and the product field group is requested [1]. | A matching GTIN or title is not proof that two offers are the same condition, pack size, bundle, or seller offer. |
| Title and description | `title`, `description`, normalized text plus raw source | **VERIFIED FACT** as displayed/returned content | eBay's item method retrieves description and product/item details [1]. Amazon says it attempts accuracy but does not warrant descriptions or other content as accurate, complete, reliable, current, or error-free [4]. | Text is evidence of a listing representation, not proof of authenticity, specifications, safety, or legal compliance. |
| Offer price | `amount`, `currency`, `price_type`, `seller/offer_id`, `observed_at` | **VERIFIED FACT** as displayed at observation time | eBay's item response and compact field group include price [1]. | Do not infer wholesale price, net cost, fees, margin, sale eligibility, or final checkout total. Amazon explicitly says it cannot confirm price until order and permits correction/cancellation of mispriced orders [4]. |
| Availability / quantity | `availability_signal`, optional `quantity`, `availability_text` | **VERIFIED FACT** only for returned signal | eBay documents estimated availabilities and says buyers need to know when availability or quantity changes; its seller Inventory API contains quantity available and can perform a real-time checkout inventory check [1] [2]. | A public signal is not a guarantee at checkout. Do not infer inventory ownership, replenishment, delivery certainty, or future availability. |
| Condition | `condition_id`, `condition_name`, `raw_condition` | **VERIFIED FACT** when source returns it | eBay item details include condition [1]; seller Inventory records also include item condition [2]. | Condition does not establish authenticity, warranty, completeness, or equivalence across marketplaces. |
| Shipping and delivery | `shipping_options`, `shipping_cost`, `estimated_delivery`, destination context | **VERIFIED FACT** for the returned estimate/context | eBay documents shipping options, costs, and estimated delivery; accuracy can depend on destination context supplied in the end-user header [1]. | Estimate is not a delivery promise. Do not infer free shipping, eligibility for a particular buyer, or fulfilment program status such as Prime. |
| Seller / offer provenance | `seller_id` or seller name when exposed, `offer_id`, `source_url` | **VERIFIED FACT** only when explicitly returned | eBay can return seller user ID through `ADDITIONAL_SELLER_DETAILS`; its Inventory API defines an offer as a seller-associated live listing [1] [2]. | Do not infer marketplace permission, seller authorization, ownership, reputation beyond explicitly returned fields, or wholesale relationship. |
| Authenticated inventory and publishing state | `access_mode=authenticated_seller`, `inventory_record`, `offer_state`, `quantity` | **VERIFIED FACT** only with valid account authorization | eBay's Inventory API requires a developer account, seller business-policy opt-in, inventory locations, and policies to publish offers [2]. Walmart requires onboarding, client credentials, OAuth 2.0, and access tokens for Marketplace APIs; access is for sellers and approved solution providers [3]. | Never synthesize this class from public pages. It is **UNKNOWN/BLOCKED** without authorized credentials, and this research did not use or request them. |
| API freshness / change detection | `observed_at`, `source_revision`, `recheck_at`, `freshness_status` | **REASONABLE INFERENCE/ESTIMATE** for operational freshness | eBay documents `sellerItemRevision` and compact fields as a way to check whether stored item details changed [1]. | A revision check reduces stale-data risk but does not guarantee price, inventory, or checkout outcome after the check. |
| Access and policy status | `access_mode`, `api_auth_scope`, `terms_reviewed_at` | **VERIFIED FACT** for documented requirements; otherwise **UNKNOWN** | eBay REST operations require an Authorization header [1]. Walmart requires OAuth 2.0 [3]. Amazon PA-API 5 is deprecated and returns 403, with migration directed to Creators API [5]. | Public visibility is not permission for automated collection or redistribution. Legal certainty and security are out of scope and must remain unclaimed. |

## Contract schema and acceptance rules

A record should contain at least:

```text
record_id
marketplace
marketplace_locale
source_kind              # official API, official page, or other explicitly labeled source
source_url
access_mode              # public-page, public-api, authenticated-seller, sandbox, unknown
observed_at              # ISO 8601 with timezone
product_identifiers      # GTIN/UPC/EAN/ePID/marketplace item ID, preserving type
raw_title
raw_description
seller_or_offer_context  # nullable; never guessed
condition                 # nullable; raw plus normalized value
price                    # amount, currency, display context, nullable
availability             # raw signal, quantity if explicitly returned, nullable
shipping                 # raw options/estimate plus destination context
source_revision           # nullable
confidence_label          # VERIFIED FACT / REASONABLE INFERENCE-ESTIMATE / UNKNOWN / BLOCKED
non_claims                # explicit exclusions for each record
```

Acceptance requires that every populated commercial value be tied to **one source URL or API operation and one observed timestamp**. Normalization must preserve the raw value, currency, locale, condition, seller/offer identity, and pack-size cues. If a field is absent, the contract uses `UNKNOWN`; if it requires credentials, it uses `BLOCKED`, rather than substituting a guess. A later observation must be a new record or an append-only revision, not an overwrite that erases historical evidence.

## Scenario table

| Scenario | Allowed conclusion | Required label | Prohibited conclusion |
|---|---|---|---|
| An eBay Browse response returns item ID, GTIN, price, condition, estimated availability, and shipping estimate at 2026-09-18 09:00 | Those values were returned for that item, marketplace, locale, and request context at that time | **VERIFIED FACT** | The item will still be available or at the same price at checkout |
| A public Amazon product page shows a price | The page displayed that price when observed, subject to Amazon's stated pricing caveat | **VERIFIED FACT** plus caveat | Final confirmed price, seller margin, or guaranteed fulfillment |
| A seller-authenticated eBay Inventory response exposes quantity and offer price | The authorized seller account reported those fields for its inventory/offer workflow | **VERIFIED FACT** | Permission to reproduce the offer on another marketplace or legal right to sell |
| A Walmart Marketplace API integration is proposed without a seller or approved-provider OAuth grant | The required evidence cannot be collected from the authorized API in this lane | **BLOCKED** | Public access, authenticated wholesale pricing, or marketplace permission |
| A product title and GTIN match across two marketplaces | The identifiers/text are potentially consistent and merit comparison | **REASONABLE INFERENCE/ESTIMATE** | Same seller, same bundle/condition, same landed cost, or interchangeable stock |
| A record is older than the operational freshness threshold | The record should be rechecked before a decision; exact threshold is a policy choice | **REASONABLE INFERENCE/ESTIMATE** | That the offer is stale, unavailable, fraudulent, or legally invalid |

## Calculations and freshness guidance

A simple age calculation is useful for triage:

```text
age_minutes = (now - observed_at) / 60
freshness_status =
  FRESH       if age_minutes <= threshold_minutes
  RECHECK     if age_minutes > threshold_minutes
  UNKNOWN     if observed_at is missing or clock context is unclear
```

The threshold must be set by the consuming workflow and should be shorter for volatile price/availability fields than for stable identifiers. This is an **operational estimate**, not a source-backed guarantee. Even at `age_minutes = 0`, the evidence remains a timestamped observation; it does not establish checkout success. eBay's documented compact response and seller revision support change detection, not a guarantee against a race between observation and purchase [1].

## Findings by evidence class

### VERIFIED FACT

The official eBay Browse API documents item retrieval for description, price, category, aspects, condition, return policies, seller feedback/score, shipping options, shipping costs, and estimated delivery. It also documents compact fields for price, estimated availability, GTIN, shipping options, and seller revision, and requires an Authorization header [1].

The official eBay Inventory API distinguishes inventory items from offers and states that inventory records can contain condition and quantity, while published offers contain quantity, listing description, offer price, marketplace, location, category, and business policies. It requires a developer account and seller business-policy opt-in for use [2].

Walmart's official documentation says Marketplace APIs are for sellers and approved solution providers, cover items, inventory, orders, pricing, promotions, and reporting, and require onboarding, client credentials, OAuth 2.0, and access tokens [3].

Amazon's official Conditions of Use state that Amazon does not warrant product content to be accurate, complete, reliable, current, or error-free. They also state that Amazon cannot confirm an item's price until order and may contact the customer or cancel a mispriced order [4].

Amazon's official PA-API notice states that PA-API 5 is deprecated, that continued calls receive HTTP 403/AccessDeniedException, and that integrations should migrate to the Creators API [5].

### REASONABLE INFERENCE / ESTIMATE

A portable evidence contract should treat identifiers, displayed offer facts, seller context, and authenticated inventory facts as separate layers. This follows from the platform documentation's separation of buyer-facing Browse data from seller-facing Inventory/Marketplace APIs [1] [2] [3].

A same-GTIN match is useful for candidate linkage but is not sufficient to merge offers. The remaining differences can include seller, condition, bundle, quantity, destination, and fulfillment terms. This is a data-quality inference, not a marketplace fact.

Revision checks and bounded rechecks are reasonable controls for stale evidence because eBay explicitly documents revision and compact change-detection fields [1]. They reduce, but cannot eliminate, race conditions.

### UNKNOWN / BLOCKED

No authenticated wholesale price, cost of goods, seller permission, marketplace selling permission, Prime status, earnings, sales volume, legal certainty, security posture, or guaranteed availability was established. These claims require separate authorized evidence or are outside this read-only lane.

Amazon's current Creators API access scope, eligibility, rate limits, and exact offer fields were not validated here because the official PA-API page only establishes deprecation and migration direction. PA-API 5 should not be treated as an available source.

No production repository lineage was inspected or changed. No credentials, purchases, contacts, publications, deployments, or production writes were used.

## Next safe actions

1. **Adopt the schema above** as an append-only evidence record, requiring source URL, access mode, observed timestamp, raw values, and explicit non-claims.
2. **Implement one official read-only eBay Browse adapter** in a sandbox or test harness, preserving the raw response and marketplace header; do not publish or modify listings.
3. **Define freshness thresholds by field volatility** and run bounded rechecks using eBay compact/revision fields before consuming price or availability evidence.
4. **Obtain owner-approved, least-privilege sandbox or read-only authorization** before testing seller-side eBay Inventory or Walmart Marketplace evidence; do not request or reuse production credentials in this lane.
5. **Validate Amazon's Creators API documentation and terms through an owner-approved access path** before designing an adapter; do not revive PA-API 5 calls that the official notice says return 403.

## References

[1]: https://developer.ebay.com/api-docs/buy/browse/resources/item/methods/getItem "eBay Browse API getItem reference"

[2]: https://developer.ebay.com/api-docs/sell/inventory/static/overview.html "eBay Inventory API overview"

[3]: https://developer.walmart.com/us-marketplace/docs/introduction-to-marketplace-apis "Walmart Marketplace APIs introduction"

[4]: https://www.amazon.com/gp/help/customer/display.html?nodeId=GLSBYFE9MGKKQXXM "Amazon Conditions of Use"

[5]: https://webservices.amazon.com/paapi5/documentation/ "Amazon PA-API 5 deprecation notice"
