# Commercial Frontend Cross-System Wedge Validation — 2026-09-02

## Scope
Focused incumbent-gap validation following Issues #20 and #21. Goal: identify whether a commercially defensible wedge remains after current incumbent automation is accounted for.

## Verified external evidence

### Tradie / ServiceM8
ServiceM8's current Office Agent already performs scheduled AI review tasks, identifies work needing attention, drafts customer emails, and prepares status/booking/allocation actions for approval. ServiceM8 also provides payment follow-up automation and Xero integration. Therefore a generic AI office assistant, payment chaser, quoting helper, scheduler, or ServiceM8-only automation layer is not a differentiated wedge.

ServiceM8 documentation also confirms a remaining cross-system edge case: when a payment is received in Xero against a ServiceM8 invoice, the payment syncs back and marks the invoice paid, but ServiceM8 does not natively automate sending the paid receipt/invoice PDF in that scenario. This is evidence of a specific cross-system workflow gap, but not yet evidence of sufficient customer demand or willingness to pay.

### Ecommerce / Shopify
Shopify Flow already automates store and external-app workflows using triggers, conditions and actions, including HTTP requests on eligible plans. Shopify's App Store contains hundreds of workflow/order-fulfilment applications. Therefore a generic workflow builder, order tagging automation, fulfilment automation or AI order assistant is not differentiated.

## Cross-system wedge candidates

### Tradie candidate A — exception-to-resolution workforce
Potential flow: ServiceM8 job/invoice state → Xero/payment state → customer communication → exception classification → approval → bounded action → verification/audit.

Differentiation: coordinates the exception across systems rather than adding another ServiceM8 feature.

Status: PROMISING HYPOTHESIS; demand, volume, economics and write-boundaries still require direct validation.

### Tradie candidate B — post-payment administrative closure
Potential flow: Xero payment event → ServiceM8 status verification → receipt/paid-invoice communication → job closure checklist → exception escalation.

Evidence: a native receipt automation gap exists for Xero-originated payments. This is a concrete workflow gap, but commercial value remains UNKNOWN.

Status: BEST CURRENT MICRO-WEDGE FOR TESTING.

### Ecommerce candidate A — supplier exception workforce
Potential flow: Shopify order → supplier/fulfilment status → tracking/ETA exception → customer communication → approval/escalation → Shopify fulfilment update → verification.

Differentiation: cross-system exception handling, not ordinary Shopify automation.

Status: PROMISING HYPOTHESIS; supplier-system access and customer pain need validation.

### Ecommerce candidate B — margin-risk exception workforce
Potential flow: order/product/supplier cost → freight/discount/refund signal → contribution-margin risk → human approval → pricing/fulfilment/customer action → audit.

Differentiation: governed decision support and action across commerce operations rather than a single Shopify optimisation feature.

Status: PROMISING HYPOTHESIS; actual data availability and customer willingness to pay UNKNOWN.

## Build-gate assessment

**Tradie:** CONDITIONAL PASS TO MVP DISCOVERY, not production build. The strongest testable wedge is cross-system exception closure, with post-payment administrative closure as the smallest concrete experiment.

**Ecommerce:** CONDITIONAL PASS TO MVP DISCOVERY, not production build. Supplier exception handling is the strongest initial workflow hypothesis; margin-risk orchestration is a secondary hypothesis.

**Property:** remains BLOCKED pending authoritative integration evidence.

## Commercial evidence still missing

1. Direct customer interviews or equivalent evidence from approximately 10 target businesses.
2. Workflow frequency and time/cost impact.
3. Actual integration permissions and write actions for each proposed system.
4. Representative workflow reliability test.
5. Willingness-to-pay signal.
6. Acquisition/distribution path.

## Decision
Do not build the general Commercial Frontend yet. Proceed to MVP discovery around the smallest cross-system exception workflow. The frontend should remain an approval/visibility cockpit; AgentOS owns governance, orchestration, verification and audit; customer platforms remain systems of record.

## Next autonomous action
Develop the minimum testable workflow specification and evidence checklist for the Tradie post-payment administrative closure micro-wedge, while maintaining Ecommerce supplier-exception validation as the parallel portfolio-leverage candidate.
