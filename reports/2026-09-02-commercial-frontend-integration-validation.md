# Commercial Frontend Integration Validation — 2026-09-02

## Scope
Focused validation of the three Tier-A commercial frontend hypotheses: Tradie AI Operations, Ecommerce AI Operations, and Property Maintenance AI.

## Verified findings

### Tradie / ServiceM8
ServiceM8 exposes a REST API intended for third-party applications and internal integrations. Its API maps core operational concepts including jobs, companies, materials, scheduled bookings, recorded time and job attachments. The public developer documentation also exposes a `POST /api_1.0/job.json` create-job endpoint requiring the `create_jobs` OAuth scope. This establishes that a governed overlay can potentially read and create operational records rather than merely display data. Sources: ServiceM8 developer REST overview and Create Job documentation.

### Ecommerce / Shopify
Shopify's current Admin API is GraphQL-first for new public apps. The GraphQL Admin API exposes orders, fulfillment orders and fulfillment objects; fulfillment supports creation, cancellation and tracking updates, while order data can be used for reporting and fulfillment automation. Access is controlled through OAuth scopes. This establishes a meaningful execution surface for a governed ecommerce operations workforce, subject to app scopes and Shopify policy. Sources: Shopify Admin GraphQL API, Order, Fulfillment and FulfillmentOrder documentation.

### Property / PropertyMe
No sufficiently authoritative current PropertyMe developer/API source was found in this validation pass. Existing research claims about API/write capabilities therefore remain **unverified** and must not be treated as implementation evidence.

## Consequences

1. Tradie AI Operations has a credible integration/execution surface and remains a strong first validation candidate.
2. Ecommerce AI Operations has a particularly clear API execution surface and strong direct portfolio leverage through GlobalShopCo.
3. Property Maintenance AI remains commercially interesting but cannot yet pass an integration build gate.

## Architecture implication

The commercial frontend should be designed as an approval-oriented operating cockpit, not as the system of record. AgentOS should own governance, permissions, orchestration, verification and audit; connectors should execute bounded actions against customer systems.

## Build-gate status

**Tradie:** integration surface = PASS for further validation; customer-gap evidence still required.

**Ecommerce:** integration surface = PASS for further validation; commercial/customer-gap evidence still required.

**Property:** integration surface = INSUFFICIENT EVIDENCE; do not build against assumed API capabilities.

## Next action

Continue customer/problem and competitive-gap validation for Tradie and Ecommerce, while independently establishing authoritative PropertyMe integration documentation before considering Property Maintenance AI for MVP build.
