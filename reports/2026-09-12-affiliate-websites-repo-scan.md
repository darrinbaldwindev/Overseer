# Affiliate Websites Repository Scan — 2026-09-12

**Role:** Marketing Overseer  
**Repository:** `darrinbaldwindev/Affiliate-Websites`  
**Scanned main:** `f736f68c526f8d47705043cf1952b566b42de97a`  
**Status:** GOOD ARCHITECTURAL FOUNDATION / NOT PRODUCTION-READY

## Executive assessment

The repository is materially more mature than its older `IMPLEMENTATION-STATUS.md` wording suggests. It is no longer only a minimal theme scaffold. Current main includes reusable WordPress patterns for country pages, category/detail/comparison/buying-guide flows, trust/methodology, affiliate disclosure, commercial CTA, legal-page shell, country selector, and global homepage. It also contains a canonical rewards data contract, commercial CTA/API contract, country configuration contract, legal/trust page register, AU vertical-slice contracts, plugin governance and CI validation.

However, the system remains pre-production. The contracts explicitly state that the Rewards API, database migrations, authentication, live commercial-resolution backend, live tracking, browser acceptance, accessibility/performance verification and production WordPress deployment are not yet proven.

## Current source-of-truth architecture

Visitor → Cloudflare CDN/WAF → WordPress Block Theme → Rewards API → PostgreSQL/Supabase.

AgentOS is intended to research, verify, monitor and orchestrate. WordPress remains presentation/editorial, while structured volatile commercial intelligence belongs behind the Rewards API/PostgreSQL boundary.

This separation is sound and should be preserved.

## Theme / UX implementation present

Current theme tree includes:
- `theme.json`
- `functions.php`
- header/footer parts
- front-page, index, page, category, single, legal and 404 templates
- global homepage
- country selector
- country homepage
- Earn/Save/Compare
- category page
- buying guide
- comparison page/table
- detail page
- opportunity card
- commercial CTA
- trust/methodology
- affiliate disclosure
- legal page shell

This is enough to prove a fixture-based reusable funnel without introducing live affiliate data.

## Data and commercial governance

`CANONICAL-REWARDS-DATA-CONTRACT.md` correctly separates:
1. consumer opportunity/program data;
2. consumer/member referral relationships;
3. publisher affiliate relationships;
4. commercial offers/destinations;
5. evidence/freshness metadata;
6. append-only material change history;
7. commercial resolution/audit events.

This directly supports the Marketing Overseer requirement not to confuse member referrals with publisher affiliate rights.

Publication lifecycle is defined as:
`CONCEPT → RESEARCHED → VERIFIED → PUBLISHABLE → PUBLISHED → MONITORED`.

A commercial record must not become publishable merely because an affiliate programme exists.

## Commercial CTA boundary

The intended CTA sends semantic context (`country`, `entity_type`, `entity_id`, `action`) to a governed resolver rather than embedding raw tracking URLs in editorial templates.

The resolver is expected to validate:
- country eligibility;
- active opportunity;
- publisher affiliate relationship;
- destination;
- attribution parameters;
- commercial status;
- freshness/verification state.

This is the correct architecture for Content360 as well: social posts should link to controlled site content/resolvers, not carry uncontrolled programme URLs as source-of-truth data.

## Country model

AU, GB and US are defined as `active-design`; production country URLs are explicitly deployment configuration rather than hard-coded example domains.

Country selection must remain manual/accessibility-safe; geolocation may assist but cannot become the only route.

Country implementations retain local content, commercial relationships, SEO priorities and compliance rules while sharing the master theme.

## Legal / trust readiness

The repo already has the right page register:
- Affiliate Disclosure
- Privacy Policy
- Cookies & Tracking
- Terms
- Editorial Policy
- Corrections
- Methodology
- Contact

The footer already exposes these routes and contains a baseline affiliate disclosure.

Important production gate: the legal register explicitly prohibits invented legal identity, addresses, processors, cookies, retention periods and contact details. Country/site wording needs actual review/configuration before publication.

## AU vertical slice

The intended acceptance route is:
`Global → AU → Category → Guide/Comparison → Detail → Commercial CTA`.

The AU fixture layer is marked ready for country content but **NO LIVE COMMERCIAL CLAIMS**.

Production acceptance still requires:
- routes rendered through shared theme;
- AU isolated via config/content rather than duplicated theme code;
- defined commercial CTA API boundary;
- destination verification before click;
- affiliate disclosure at commercial decision point;
- no fabricated commercial facts;
- real WordPress browser/accessibility/performance/end-to-end tracking tests.

## CI / repository health

A GitHub Actions `Theme Validation` workflow exists and validates:
- PHP syntax;
- governed `theme.json` properties;
- expected design tokens/palette;
- required theme files;
- category/detail template pattern wiring.

The most recent surfaced Theme Validation run on commit `6f930df739d4aedd5a7020f871df5a1289582c5a` completed successfully. Current main is later (`f736f68...`) and the later commits are research/docs changes, not theme-code changes, so the workflow was not necessarily triggered for those commits.

## Marketing / Content360 assessment

### GREEN now
- brand/trust/editorial educational content;
- non-commercial category education;
- programme research summaries when accurately qualified;
- country-specific editorial Content360 posts;
- affiliate-disclosure messaging;
- methodology/transparency content;
- RSS/content repurposing once the country WordPress site is live.

### AMBER
- named programme profiles where consumer facts are current but publisher approval is absent;
- member-referral content, with clear distinction from publisher affiliate relationship;
- Awin application preparation;
- country-specific commercial CTAs using fixtures/non-production resolver.

### RED / NOT YET PROVEN
- live publisher affiliate monetisation;
- end-to-end tracking/attribution;
- production Rewards API;
- live PostgreSQL/Supabase canonical commercial database;
- raw tracking link automation through Content360;
- automated commercial substitution;
- live legal/compliance readiness;
- browser/CWV/accessibility acceptance;
- production country deployment.

## Awin readiness after repo scan

Architecture readiness is stronger than previously assumed. The repo already has disclosure/trust components, legal-route definitions, country separation, affiliate-resolution design and editorial standards.

Remaining blocker is mostly deployment evidence:
1. live public country property;
2. working trust/legal/contact pages;
3. representative published editorial pages;
4. real publisher/promotional-space identity;
5. owner-controlled identity/payment/terms onboarding;
6. later publisher/program approval evidence.

Therefore: **AWIN = PRE-APPLICATION READY / DEPLOYMENT-GATED**, not architecture-gated.

## Stale-document risk

`IMPLEMENTATION-STATUS.md` and `STATUS.md` are dated 2026-09-03 and describe an earlier implementation point. Some statements are now stale relative to current main, because later theme patterns, contracts, legal/trust definitions and AU fixture/vertical-slice material exist.

Recommendation: create a fresh canonical status document rather than rely on those older status files for current readiness.

## Highest-value next implementation work

1. Create a current `STATUS-2026-09-12.md` reconciled against main.
2. Deploy the first non-production WordPress instance with the current theme.
3. Prove Global → AU → category → comparison/guide → detail → CTA using fixture-safe records.
4. Add/verify trust/legal pages in the live instance.
5. Run browser, accessibility and performance acceptance.
6. Implement the controlled Rewards API/commercial resolver boundary.
7. Connect canonical structured data/storage only after contracts are accepted.
8. Apply to Awin only after a real publisher property and representative content are live.
9. After network approval, store exact programme approvals/terms in the canonical commercial model before any Content360 monetised promotion.

## Governance

No production deployment, affiliate application, account creation, credentials, live programme links, legal publication or commercial writes were performed by this scan.