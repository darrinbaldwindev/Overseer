# Affiliate Websites — Editorial Acquisition & Monetisation Gate

**Date:** 2026-09-13  
**Owner:** Marketing Overseer / ChatGPT Overseer  
**Status:** EDITORIAL PREP/CONTENT SAFE IN PRINCIPLE / MONETISED OUTBOUND HOLD  
**Architecture source:** `darrinbaldwindev/Affiliate-Websites`

## Current evidence state

Repository architecture establishes:

- WordPress is the presentation/editorial layer, not the canonical rewards intelligence database.
- PostgreSQL/Supabase is intended as canonical structured commercial data store.
- Rewards API is the governed commercial resolution boundary.
- WordPress should send semantic CTA context rather than store raw affiliate tracking URLs or commercial-resolution logic.
- Country architecture and trust/evidence UI are already part of the site direction.

Marketing evidence in Overseer additionally establishes that publisher-affiliate candidates have been verified at network level, but publisher/account approval is still required before monetised outbound use.

Therefore the safe strategy is:

> Build trust, search utility and country/category authority first; activate monetised outbound resolution only after the relevant publisher relationship is approved and live.

---

## Acquisition model

### Phase A — Editorial authority now

Safe content types where facts are current and country-scoped:

- “How this rewards programme works” explainers;
- country-specific rewards directories;
- comparisons of reward mechanism, eligibility, payout/reward type and known restrictions;
- guides to survey/reward programme terminology;
- “last verified” evidence panels;
- editorial programme pages with CTA resolved to non-monetised or blocked state when no approved affiliate relationship exists.

### Phase B — Monetised CTA after approval

Only after approved publisher relationship and live commercial-resolution evidence:

- Join / Learn More CTA may resolve through Rewards API to the authorised affiliate relationship;
- country and campaign context must remain explicit;
- disclosure must be visible and appropriate;
- monetised link must not be hard-coded into editorial templates.

### Phase C — Scaled distribution

After live WordPress/browser/SEO/tracking validation:

- Content360 country-specific distribution;
- organic social snippets;
- comparison/update content;
- seasonal/intent content where programme terms remain current;
- paid acquisition only after unit economics, policy and conversion evidence justify it.

---

## SEO / AEO content structure

### Country landing page

Purpose: answer “Which reward/survey programmes are actually available in my country?”

Sections:

1. How we verify programmes.
2. Last-updated date.
3. Category navigation.
4. Comparison table using structured approved data.
5. Programme cards.
6. Editorial disclosure.
7. How rewards/referrals/affiliate relationships differ.

### Category page

Examples:

- Surveys
- Cashback / shopping rewards
- Offer walls / tasks
- Referral programmes
- Other user-reward models

Each category page should explain eligibility and risk of confusing a member referral with a publisher affiliate programme.

### Programme detail page

Minimum evidence fields:

- programme name;
- country availability;
- reward mechanism;
- user eligibility;
- payout/reward form;
- current referral/member-reward status;
- current publisher-affiliate status separately;
- verification date;
- evidence/source class;
- commercial CTA state: approved / blocked / editorial-only.

---

## Trust pattern

Every commercial/editorial page should make it easy to answer:

- When was this last checked?
- Is this programme available in my country?
- Does the programme reward the user?
- Is this a member referral or a publisher affiliate relationship?
- Are we paid if you join?
- Is the commercial link active or currently editorial-only?

This distinction is a potential brand advantage because reward-programme content is often unclear about who receives the benefit.

---

## Claim rules

Do not say:

- “best” unless comparison methodology is defined and current;
- “highest paying” without current comparable evidence;
- “guaranteed earnings”;
- “easy money”;
- “available worldwide” unless evidenced;
- “affiliate programme” when only a member-referral mechanism is verified;
- “join here” through monetised tracking before account/program approval exists.

Prefer:

- “Last verified [date]”;
- “Available in [country] based on current programme evidence”;
- “Member referral” / “Publisher affiliate” as separate labels;
- “Reward terms can change—check the programme’s current terms before joining.”

---

## Content360 handoff

Content360 receives:

- country;
- programme/category;
- verification date;
- approved claims;
- relationship type;
- CTA state;
- disclosure requirement;
- campaign ID/UTM when monetised activation is authorised;
- expiry/recheck date.

Content360 must not infer publisher approval, payout amounts, country availability or commercial relationship state.

---

## Marketing readiness gate

### GREEN for editorial publication only when

- programme identity/country/reward facts are current enough for the stated page;
- last-verified date is present;
- disclosure state is clear;
- site/browser/legal basics for publication are acceptable.

### GREEN for monetised CTA only when

- publisher/network/account approval exists;
- exact programme relationship is active;
- current destination/tracking contract is verified;
- disclosure is ready;
- Rewards API/commercial resolution path is the source of truth;
- tracking test succeeds without leaking raw commercial logic into WordPress.

---

## Current blockers / UNKNOWNs

- publisher/account acceptance for target monetised programmes;
- live WordPress/browser/accessibility/performance/E2E tracking acceptance;
- current programme-term rechecks at publication time;
- country-specific regulatory/disclosure review where required.

## Next safe Marketing action

Editorial acquisition can proceed as prepared content architecture once publication authority/site readiness exists. Monetised activation remains gated. If this lane is blocked, move to GhostKitchen/Franchise pre-launch positioning without earnings/payback claims.
