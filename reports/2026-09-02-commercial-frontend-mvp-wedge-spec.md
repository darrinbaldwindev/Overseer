# Commercial Frontend MVP Wedge Specification — 2026-09-02

## Candidate
Tradie AI Operations — Post-Payment Administrative Closure

## Purpose
Define the smallest testable workflow before any production frontend implementation.

## Trigger
A payment originating in Xero is reflected against a ServiceM8 invoice/job.

## Proposed agent workflow
1. Detect payment/status change.
2. Verify the corresponding ServiceM8 invoice/job and customer identity.
3. Determine whether a paid receipt/paid-invoice communication is required.
4. Prepare the customer communication and closure recommendation.
5. Present the action for human approval where required.
6. Execute only the permitted bounded action through the appropriate connector.
7. Re-read both systems to verify the expected state.
8. Record evidence, action, approval and outcome in the AgentOS audit trail.
9. Escalate mismatches, duplicate identities, partial payments or ambiguous records rather than guessing.

## Explicit non-goals
- Replace ServiceM8.
- Replace Xero.
- Build a generic AI receptionist.
- Build a generic CRM.
- Autonomously make financial/accounting decisions.
- Send customer communications without an explicit policy/approval boundary.

## Required integration evidence
- Xero event/read access.
- ServiceM8 invoice/job/customer read access.
- Exact permitted write action for receipt/communication/closure, if any.
- Identity matching rules.
- Idempotency strategy.
- Failure/retry behaviour.
- Audit evidence requirements.

## Success metrics for discovery
- Minutes of administrative work removed per qualifying payment.
- Percentage of cases resolved without manual system switching.
- Exception rate.
- Human approval rate.
- Verification success rate.
- Customer willingness to pay.

## Safety / authority
The system may recommend and prepare actions autonomously within configured policy. Financial commitments, ambiguous customer identity, accounting corrections, refunds, destructive changes and policy changes remain gated for human approval.

## Build gate
This is an MVP DISCOVERY SPECIFICATION, not production authorization. Do not connect to or mutate live customer systems until integration permissions, representative test data, authority policy and verification tests are established.

## Parallel candidate
Ecommerce supplier-exception workforce remains the second validation track because of GlobalShopCo leverage.
