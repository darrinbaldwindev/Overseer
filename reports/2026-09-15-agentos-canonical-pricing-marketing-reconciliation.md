# AgentOS — Canonical Pricing Marketing Reconciliation

**Date:** 2026-09-15 AEST  
**Task:** M-A045  
**Status:** COMPLETE / CANONICAL PRODUCT DIRECTION RECONCILED / NOT A SHIPPED BILLING CLAIM

## Decision
Fresh exact-main evidence resolves the Marketing conflict. `docs/COMMERCIAL_PRODUCT_MODEL_2026-09-02.md` at main `962cb3820b83506f9e6d90f50e003690dd85a8a1` explicitly states that the pricing was supplied by the owner and **updated on 2026-09-15**, and that historical pricing assumptions must not silently override it.

Therefore the current canonical product direction is:

| Product | Current target price | Marketing role |
|---|---:|---|
| AgentOS Free | $0/year | fully useful entry level |
| AgentOS Standard | $49/year | serious entry tier |
| AgentOS Advanced / Pro | $99/year | recommended full personal AgentOS tier |
| Commercial / Business | TBD | customer-hosted/private-server, multi-seat organisational path |
| AI Plus | $22/month | separate optional intelligence subscription |

## Superseded Marketing assumption
The older `Free → $29 → $99` assumption is **historical/superseded for current product-direction work**. Do not use `$29` in new pricing copy unless the owner deliberately changes the canonical model again.

This reconciliation does not delete historical artifacts; it prevents them from controlling current claims.

## Critical distinction
The $49/$99 annual amounts are **AgentOS product entitlements**. `$22/month AI Plus` is a separate intelligence resource. Marketing must not present AI Plus as the AgentOS operating-system tier itself.

Possible user combinations include AgentOS entitlements with free intelligence, local models, BYOK/provider resources and/or AI Plus where appropriate.

## Safe current language
Because the canonical document is a product target, not proof of implemented commerce:

> **Product direction:** AgentOS is planned with a useful Free tier, $49/year Standard and $99/year Advanced/Pro, plus an optional $22/month AI Plus intelligence subscription. Commercial/Business pricing is still TBD.

For internal commercial planning, the prices may be treated as owner-current targets.

## Do not yet claim
Until separately proven:
- `Buy now` / `Subscribe now` availability;
- billing infrastructure is live;
- entitlements are production-enforced;
- refunds/trials/tax treatment;
- Commercial seat pricing;
- all tier features are shipped;
- AI Plus guarantees a particular model/provider;
- savings versus purchasing individual AI subscriptions;
- upgrade recommendation automatically works in production.

## Marketing architecture
### Free
Promise: useful AgentOS, not a crippled demo.

### Standard — $49/year
Role: serious entry tier. Campaign should explain the concrete additional value rather than treating price alone as the reason to upgrade.

### Advanced / Pro — $99/year
Role: recommended full personal AgentOS experience / advanced orchestration tier.

### AI Plus — $22/month
Role: optional additional intelligence capacity/capability. Keep visibly separate from the control-plane entitlement.

### Commercial / Business
Do not invent price. Lead with governance, customer-controlled infrastructure, multi-seat administration, organisational identity/audit/isolation and approved intelligence options once those claims are implementation-supported.

## 30-day value loop
The canonical direction explicitly supports evidence-based upgrade recommendations and a legitimate `stay Free` outcome. Marketing should treat this as a trust principle: upgrades should be justified by user value, not manufactured scarcity.

## Content360 rule
All current Content360 pricing templates must use this canonical model only after claim-state metadata identifies it as **PRODUCT DIRECTION / pricing target**, unless production commerce evidence later promotes it.

## Disposition
**M-A045 COMPLETE. Current Marketing price truth is Free $0/year → Standard $49/year → Advanced/Pro $99/year, with separate AI Plus $22/month; Business TBD. Older $29 assumptions are superseded.**