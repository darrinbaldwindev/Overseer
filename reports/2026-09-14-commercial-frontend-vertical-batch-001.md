# Commercial Frontend Vertical Batch 001 — Evidence & Permission Matrix

**Date:** 2026-09-14  
**Role:** Commercial Frontend Overseer  
**Parent:** `.overseer/batches/PORTFOLIO-EXECUTION-BATCH.md` C-006  
**Vertical batch:** `.overseer/batches/COMMERCIAL-FRONTEND-VERTICAL-BATCH.md`  
**Decision:** CONTINUE DISCOVERY / NO PRODUCTION FRONTEND BUILD

## Evidence classification

- **VERIFIED PLATFORM EVIDENCE** = authoritative product/API documentation.
- **PUBLIC OPERATOR SIGNAL** = public self-reported workflow/friction; useful for hypothesis prioritisation but not a substitute for direct interview/observed-customer evidence.
- **PORTFOLIO EVIDENCE** = current repository evidence from owned projects.
- **INFERENCE** = reasoned interpretation.
- **UNKNOWN** = not evidenced.

No public post in this report is promoted to VERIFIED CUSTOMER EVIDENCE.

---

# 1. Tradie AI Operations — post-payment administrative closure

## Verified platform evidence

### Native gap remains current
ServiceM8 documents that when a payment is received in Xero against a ServiceM8-exported invoice, the payment syncs back and marks the invoice paid once fully paid, but ServiceM8 does **not** provide a native automation to automatically send a receipt or paid invoice for that Xero-originated payment.

Source: https://support.servicem8.com/questions/invoices/can-servicem8-automatically-send-receipt-xero-payment-syncs-back

ServiceM8 also documents the Xero sync behavior:
- invoices are sent to Xero when approved;
- Xero payments against ServiceM8-exported invoices sync back within about 30 minutes;
- once full payment is received in Xero, the invoice is marked paid in ServiceM8.

Source: https://support.servicem8.com/help-center/servicem8-add-ons/xero/how-the-sync-with-xero-works

### Read primitives are concrete
ServiceM8 API:
- retrieve/list jobs: `read_jobs`;
- retrieve/list Job Payments: `read_job_payments`;
- Job Payment records are tied to `job_uuid`.

Sources:
- https://developer.servicem8.com/reference/getjobs
- https://developer.servicem8.com/reference/listjobs
- https://developer.servicem8.com/reference/getjobpayments
- https://developer.servicem8.com/reference/listjobpayments

Xero API:
- granular scopes introduced for Accounting API;
- `accounting.invoices.read` provides invoice read access;
- `accounting.payments.read` provides payment read access;
- broad `accounting.transactions*` scopes are being replaced and should not be the preferred new design.

Sources:
- https://developer.xero.com/documentation/guides/oauth2/scopes/
- https://developer.xero.com/documentation/api/accounting/payments
- https://developer.xero.com/documentation/api/accounting/invoices

### Communication primitive exists
ServiceM8 exposes a Messaging API email endpoint. It can link a sent email to a job using `regardingJobUUID`, and can include existing attachment UUIDs. This establishes a bounded communication primitive, but exact authentication/permission behavior and document-generation path must be verified before any implementation recommendation.

Source: https://developer.servicem8.com/reference/send_email

## Public operator signal

A May 2026 Australian small-business discussion described the combination of Xero plus several admin apps as a costly mess with too much admin and too little time on the tools. Replies specifically cited Xero + ServiceM8 as a common stack and noted that growing businesses may still need someone to set up and maintain invoicing/scheduling.

Source: https://www.reddit.com/r/ausbusiness/comments/1tm5bx8/tradie_admin_tools/

**Classification:** PUBLIC OPERATOR SIGNAL only. It supports the broad admin-friction hypothesis but does not prove that post-payment closure itself occurs frequently enough or is valuable enough to buy.

## Exact read/write/approval matrix — candidate MVP

| Step | System | Candidate action | Evidence / scope | Default authority |
|---|---|---|---|---|
| Detect relevant payment | Xero | Read payment | `accounting.payments.read` | automatic read allowed after consent |
| Resolve invoice | Xero | Read invoice / status | `accounting.invoices.read` | automatic read allowed after consent |
| Resolve job | ServiceM8 | Read job | `read_jobs` | automatic read allowed after consent |
| Cross-check payment | ServiceM8 | Read Job Payment | `read_job_payments` | automatic read allowed after consent |
| Resolve recipient | ServiceM8 | Read job/contact identity | read path requires exact endpoint/scope confirmation for chosen identity source | automatic read only after exact identity match |
| Prepare receipt/paid-invoice message | AgentOS | Draft recommendation/message | no external mutation | automatic preparation |
| Send message | ServiceM8 | Messaging API email linked to job | endpoint confirmed; exact auth/attachment contract requires test | **human approval by default** |
| Update job/closure state | ServiceM8 | Potential bounded write | exact endpoint/field not yet locked | **BLOCKED/approval required** until exact contract proven |
| Verify outcome | ServiceM8/Xero | Re-read job/payment/invoice + message evidence | read primitives above | mandatory before VERIFIED |

## Fail-closed requirements

Do not send or close when:
- invoice/job/customer identity is ambiguous;
- payment is partial, reversed, duplicated or disputed;
- ServiceM8 and Xero disagree materially;
- receipt/paid-invoice attachment or content cannot be generated/verified;
- a previous execution with the same idempotency key is unresolved;
- approval is missing where required;
- verification re-read cannot establish the expected state.

## Current Tradie decision

- Platform feasibility: **PARTIAL PASS** for read + communication proof.
- Exact closure-write path: **UNKNOWN/BLOCKED**.
- Public pain signal: **PRESENT but broad**.
- Frequency/minutes-per-case/WTP: **UNKNOWN**.
- Read-only/non-production prototype gate: **NOT YET PASSED** because the protocol still requires materially similar evidence from at least 3 independent relevant participants.

---

# 2. Ecommerce AI Operations — supplier / fulfilment exception handling

## Verified Shopify platform evidence

Shopify's Admin GraphQL API provides concrete bounded primitives:

### Read fulfilment state
`fulfillmentOrders` requires one or more fulfillment-order read scopes, such as `read_merchant_managed_fulfillment_orders` or `read_third_party_fulfillment_orders` depending on the relationship.

Source: https://shopify.dev/docs/api/admin-graphql/2026-01/queries/fulfillmentorders

### Place fulfilment hold
`fulfillmentOrderHold` can place an order fulfilment on hold, including an `INVENTORY_OUT_OF_STOCK` reason. It requires the relevant write fulfilment-order scope and `fulfill_and_ship_orders` permission.

Source: https://shopify.dev/docs/api/admin-graphql/2026-04/mutations/fulfillmentOrderHold

Shopify Flow also exposes a native Hold fulfillment order action, reinforcing that a basic hold workflow by itself is not differentiated.

Source: https://help.shopify.com/en/manual/shopify-flow/reference/actions/hold-fulfillment

### Update tracking
`fulfillmentTrackingInfoUpdate` can update carrier/tracking number/URL and optionally notify the customer. It requires the relevant fulfillment-order write scope and `fulfill_and_ship_orders` permission.

Source: https://shopify.dev/docs/api/admin-graphql/2026-04/mutations/fulfillmentTrackingInfoUpdate

### Release hold
Shopify exposes `fulfillmentOrderReleaseHold`; apps should identify the specific holds they intend to release rather than broad release where possible.

Source: https://shopify.dev/docs/api/admin-graphql/2025-10/mutations/fulfillmentOrderReleaseHold

## Public operator signals

### Multi-supplier tracking administration
A 2026 dropshipping merchant described receiving dispatch emails from multiple suppliers with different couriers and email formats, forwarding them to a VA who manually uploads tracking numbers into Shopify. The merchant reported paying the VA $15/hour and sometimes seeing 12+ hour delays before customers receive tracking. A respondent described supplier-format drift and scaling pain when the number of suppliers increases.

Source: https://www.reddit.com/r/dropshipping/comments/1slemiy/uploading_supplier_tracking_details_to_shopify/

**Classification:** PUBLIC OPERATOR SIGNAL. Strongly relevant to the candidate wedge, but still not direct validation of this product.

### Supplier inventory / SKU mismatch
A merchant described items appearing out of stock despite supplier inventory. Discussion pointed to fulfillment-location configuration and supplier-SKU/variant mapping as possible causes.

Source: https://www.reddit.com/r/dropship/comments/1nopfdm

**Classification:** PUBLIC OPERATOR SIGNAL. Useful exception taxonomy evidence; not proof of prevalence.

### Supplier delay consequence
A September 2026 dropshipping discussion describes a past delivery taking more than a month, missing a customer's intended birthday and contributing to the operator closing the store. The post asks specifically about supplier/delivery options and operational automation.

Source: https://www.reddit.com/r/dropship/comments/1w6l2um/how_to_deal_with_chinese_suppliers_delivery_delay/

**Classification:** PUBLIC OPERATOR SIGNAL. Illustrates potential consequence severity, not frequency.

## Exact read/write/approval matrix — candidate MVP

| Step | System | Candidate action | Evidence / scope | Default authority |
|---|---|---|---|---|
| Read order/fulfilment state | Shopify | Query fulfillment orders / order state | fulfillment-order read scope(s) | automatic read after consent |
| Ingest supplier status | Supplier/email/app | Read supplier dispatch/stock/ETA evidence | supplier-specific; **UNKNOWN until connector exists** | automatic read only where bounded/consented |
| Classify exception | AgentOS | Compare supplier vs Shopify state | no mutation | automatic |
| Hold affected fulfilment | Shopify | `fulfillmentOrderHold` | write fulfilment-order scope + ship permission | human approval by default for first MVP |
| Update tracking | Shopify | `fulfillmentTrackingInfoUpdate` | write fulfilment-order scope + ship permission | approval can be policy-driven after identity proof |
| Notify customer | Shopify mutation / approved communication surface | optional tracking notification or separate message | exact surface depends on action | approval by default for material promise changes |
| Release hold | Shopify | `fulfillmentOrderReleaseHold` | relevant write scope | approval/policy gate; bind exact hold IDs |
| Verify | Shopify + supplier | Re-read fulfilment/tracking/hold/supplier state | read scopes + supplier read | mandatory before VERIFIED |

## Fail-closed requirements

Do not mutate when:
- supplier identity/SKU/order mapping is ambiguous;
- supplier evidence is stale or contradictory;
- multiple Shopify fulfilment orders make customer impact unclear;
- tracking belongs to a different order/package;
- customer-promise change would be made without required approval;
- hold/release identity cannot be bound to the exact intended fulfilment/hold;
- verification re-read fails;
- supplier connector itself has no trustworthy source/evidence timestamp.

## Current Ecommerce decision

- Shopify action feasibility: **PASS for bounded read/hold/tracking primitives**.
- Supplier-side integration: **UNKNOWN / provider-specific**.
- Relevant public operator pain: **PRESENT and specific**.
- Frequency/WTP/direct customer proof: **UNKNOWN**.
- Differentiation remains cross-system exception resolution, not Shopify automation alone.
- Read-only/non-production prototype gate: **NOT YET PASSED** pending 3 independent materially similar direct participants/observations.

---

# 3. Portfolio leverage — GlobalShopCo

Current GlobalShopCo Home Organisation research already models useful exception categories without pretending missing evidence is known. Reusable fixture concepts include:

- exact supplier/SKU identity;
- wholesale/cost evidence;
- outbound freight evidence;
- sellable stock assurance;
- dropship/blind-shipping permission;
- fulfilment identity;
- marketplace/channel permission;
- landed/free-delivery economics;
- HOLD when required evidence is absent.

Examples are present in `docs/research/M4.1_HOME_ORGANISATION_*` and the eBay pilot shortlist. These are suitable as **PORTFOLIO EVIDENCE / synthetic acceptance-fixture seeds** for Ecommerce exception handling. They are not demand evidence.

Recommended reusable exception taxonomy:
1. `SUPPLIER_STOCK_UNKNOWN`
2. `SUPPLIER_STOCK_MISMATCH`
3. `SKU_IDENTITY_MISMATCH`
4. `FREIGHT_UNKNOWN`
5. `FULFILMENT_IDENTITY_UNKNOWN`
6. `DROPSHIP_PERMISSION_UNKNOWN`
7. `CHANNEL_PERMISSION_BLOCKED`
8. `TRACKING_MISSING`
9. `TRACKING_STALE_OR_CONFLICTING`
10. `CUSTOMER_PROMISE_AT_RISK`
11. `MARGIN_AT_RISK`
12. `MANUAL_APPROVAL_REQUIRED`

This taxonomy can later drive a non-production cockpit fixture without creating a production storefront or modifying Shopify.

---

# 4. Batch conclusion

## What advanced

- Tradie candidate now has a clearer least-privilege read matrix and a bounded ServiceM8 communication primitive.
- Ecommerce candidate now has exact Shopify read/hold/tracking primitives plus a highly relevant public multi-supplier tracking-admin signal.
- GlobalShopCo provides reusable exception/evidence fixtures.

## What did not advance

No direct customer interview/observation evidence was created. Therefore no WTP/frequency claim is upgraded.

## Current priority ranking

1. **Ecommerce supplier/tracking exception cockpit** — strongest newly observed public workflow signal + strong Shopify action surface, but supplier connector and direct demand remain unproven.
2. **Tradie post-payment administrative closure** — concrete native gap + viable read/communication surface, but narrower pain and demand still unproven.
3. **Property Maintenance** — remains blocked on authoritative integration evidence.

## Next safe batch

1. Create compact 10-participant capture/scoring sheet.
2. Define read-only synthetic prototype fixtures for Ecommerce using GlobalShopCo exception taxonomy.
3. Define equivalent Tradie exception fixtures: full payment, partial payment, duplicate identity, reversed payment, sync lag, disputed payment, missing recipient, prior-send replay.
4. Re-scan Issues #20/#21 and AgentOS Wave-0 state before any prototype recommendation.
5. Keep production build HOLD until direct validation threshold is met.
