# Commercial Frontend — Ecommerce Exception Evidence Batch

**Date:** 2026-09-14
**Scope:** C-006 bounded platform-evidence batch for `Overseer#21`.
**Status:** platform evidence only; commercial demand remains UNKNOWN.

## Architecture boundary

Preserve:

`Vertical cockpit -> shared commercial layer -> AgentOS governance/execution/verification -> Shopify/external supplier systems of record`

This batch does not authorize a production frontend, provider write, customer communication, fulfilment mutation, refund, order edit, deployment, credential use, or campaign.

## Evidence classes

- **VERIFIED PLATFORM EVIDENCE** — current first-party Shopify documentation checked 2026-09-14.
- **HYPOTHESIS** — proposed cross-system workflow requiring customer validation.
- **UNKNOWN** — no evidence available in this batch.

No platform evidence is promoted to customer-pain or willingness-to-pay evidence.

## Homogeneous batch: three supplier/fulfilment exception records

### ECOM-EX-01 — Supplier stock becomes unavailable after order creation

**Systems involved**
- Shopify order / fulfilment order
- external supplier or fulfilment service stock signal
- customer communication path

**Verified incumbent capability**
- Shopify can place fulfilment orders on hold manually or through Flow.
- Shopify documents insufficient inventory as a valid reason to hold fulfilment.
- A hold blocks fulfilment until released; inventory may remain reserved.

**Residual cross-system handoff hypothesis**
An external supplier reports that stock is unavailable after Shopify accepted the order. The merchant must reconcile supplier evidence against Shopify state, decide whether to wait/substitute/cancel/refund, and communicate the resulting promise.

**Approval boundary**
- reading supplier + Shopify state may be automated;
- placing/releasing a hold, substitution, cancellation, refund, or customer promise change should remain approval-gated until exact customer policy and write scopes are evidenced;
- ambiguous supplier identity/SKU/order correlation must fail closed.

**Smallest testable non-production surface**
External synthetic `OUT_OF_STOCK` event -> exact order/line correlation -> proposed hold + decision options -> human approval card -> dry-run action intent + verification receipt.

**Measurable prototype outcome**
One supplier exception produces at most one correlated case and no action when order/SKU/supplier evidence is incomplete or replayed.

**Commercial evidence**
- frequency: UNKNOWN
- minutes/case: UNKNOWN
- loss/refund/complaint impact: UNKNOWN
- trial intent: UNKNOWN
- willingness-to-pay: UNKNOWN

### ECOM-EX-02 — Supplier dispatch delay / unknown ETA before fulfilment

**Systems involved**
- Shopify fulfilment order
- supplier/fulfilment service status
- customer promise/notification path

**Verified incumbent capability**
- Shopify supports fulfilment holds and releases.
- Shopify Flow can hold fulfilment orders from supported triggers.
- Customer notifications are event-driven for fulfilment, tracking, cancellation and refund events.

**Residual cross-system handoff hypothesis**
A supplier provides a late-dispatch or unknown-ETA signal that does not itself determine the merchant's customer promise. The merchant must decide whether to continue waiting, hold, reroute, cancel, refund, or notify the customer.

**Approval boundary**
- exception detection and evidence assembly may be automated;
- any customer-facing promise, cancellation/refund, reroute or release remains approval-gated until policy is evidenced;
- absence of an ETA must remain `UNKNOWN`, never inferred as a safe delivery promise.

**Smallest testable non-production surface**
Synthetic supplier `DELAYED/ETA_UNKNOWN` event -> exact Shopify order/fulfilment correlation -> evidence card showing current Shopify state + supplier status -> proposed bounded options -> no-send/no-write default -> dry-run receipt on simulated approval.

**Measurable prototype outcome**
A delayed supplier event becomes one reviewable exception with preserved source/timestamp and zero invented ETA.

**Commercial evidence**
- frequency: UNKNOWN
- minutes/case: UNKNOWN
- customer-impact rate: UNKNOWN
- trial intent: UNKNOWN
- willingness-to-pay: UNKNOWN

### ECOM-EX-03 — Order change decision while external fulfilment state may be stale

**Systems involved**
- Shopify order editing
- external fulfilment/supplier app
- payment/refund and customer communication state

**Verified incumbent capability / risk**
- Shopify supports order edits before fulfilment for product, quantity, shipping-fee and discount changes.
- Shopify warns that some apps might not recognize order edits and their data may become incorrect.
- Shopify specifically warns that order editing can affect fulfilment apps and instructs merchants to verify whether a fulfilment service supports edits.
- Orders created by an app have additional edit restrictions.

**Residual cross-system handoff hypothesis**
A customer or operator wants to change an order while supplier/fulfilment state may already have progressed. The valuable workflow is not the edit itself; it is proving whether Shopify and the external fulfilment system still agree before an approved edit/refund/customer response.

**Approval boundary**
- read/reconcile both systems first;
- mismatch or unknown external state -> block action and escalate;
- financial, quantity, fulfilment or customer-facing changes remain approval-gated;
- re-read after simulated action before producing a success receipt.

**Smallest testable non-production surface**
Synthetic order-change request + external fulfilment snapshot -> correlation/reconciliation -> `SAFE_TO_PROPOSE` or `BLOCKED_STALE_STATE` -> approval card only for the safe case -> dry-run mutation intent + post-intent verification contract.

**Measurable prototype outcome**
No edit proposal is emitted when external fulfilment state is stale, unsupported or uncorrelated.

**Commercial evidence**
- frequency: UNKNOWN
- minutes/case: UNKNOWN
- failure consequence frequency: UNKNOWN
- trial intent: UNKNOWN
- willingness-to-pay: UNKNOWN

## Batch decision

All three records pass only a **platform-feasibility / authority-shaping** gate. They do **not** pass the Commercial Frontend Build Gate.

The common evidenced product shape is a governed exception cockpit, not a replacement automation engine:

`external exception -> exact cross-system correlation -> evidence assembly -> fail-closed ambiguity handling -> human decision -> bounded action intent -> verification receipt`

## Fresh sources checked 2026-09-14

1. Shopify Help — Hold fulfillment order: https://help.shopify.com/en/manual/shopify-flow/reference/actions/hold-fulfillment
2. Shopify Help — Marking your order as on hold: https://help.shopify.com/en/manual/fulfillment/fulfilling-orders/holding-fulfillments
3. Shopify Help — Setting up customer notifications: https://help.shopify.com/en/manual/fulfillment/setup/notifications/customer-notifications
4. Shopify Help — Editing orders: https://help.shopify.com/en/manual/fulfillment/managing-orders/editing-orders
5. Shopify Help — Considerations for editing orders: https://help.shopify.com/en/manual/fulfillment/managing-orders/editing-orders/considerations
6. Shopify Help — Fulfilling orders using a fulfillment service with an app: https://help.shopify.com/en/manual/fulfillment/fulfilling-orders/app-fulfillment

## Exact next validation step

Use the existing direct-validation protocol to test these three records with real ecommerce operators. Capture, per workflow: weekly frequency, systems involved, current manual handoffs, minutes/case, actual failure/refund/complaint consequence, who approves the action, existing workaround, trial intent and willingness-to-pay.

Do not rank or green-light a production build until direct customer evidence exists. If one workflow receives repeated evidence while others do not, split the batch and preserve GREEN only for the evidenced item.