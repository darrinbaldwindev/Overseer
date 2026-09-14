# Commercial Frontend — Ecommerce Synthetic Harness Mapping

Date: 2026-09-14
Role: Commercial Frontend Overseer
Parent: `.overseer/batches/COMMERCIAL-FRONTEND-VERTICAL-BATCH.md` / CF-C006

## Decision

**IMPLEMENTATION-READY MAPPING ONLY / NO NEW RUNTIME CREATED**

A fresh scan found no existing Commercial Frontend decision engine or provider-specific supplier runtime in Overseer that could accept EC-001..EC-014 without inventing a new source of execution truth. AgentOS does have an existing deterministic local test convention that is explicitly provider-free and dry-run oriented. That convention is suitable as a future test shape, but the commercial vertical must not be inserted into AgentOS until there is an approved reusable commercial decision seam.

Relevant existing convention:
- `AgentOS/tests/README.md`: deterministic vertical/runtime tests must not require paid model/API calls; provider adapters remain outside deterministic tests.
- `AgentOS/tests/agentos-local-mock-api.test.mjs`: uses pure local fixture calls, explicit idempotency keys, deterministic equality assertions, no persistence, and source checks prohibiting network/environment/process escape.

Therefore this pass maps the Ecommerce fixtures into that **test contract style**, not into production or a new execution module.

## Proposed table-driven fixture envelope

```json
{
  "case_id": "EC-001",
  "provider": "fixture-supplier",
  "shopify": {
    "order_id": "order-001",
    "fulfillment_order_id": "fo-001",
    "line_item_id": "li-001",
    "sku": "SKU-001"
  },
  "supplier": {
    "product_id": "supplier-product-001",
    "variant_id": "supplier-variant-001",
    "sku": "SKU-001",
    "event_id": "supplier-event-001",
    "event_version": 1,
    "observed_at": "2026-09-14T00:00:00Z",
    "status": "UNKNOWN"
  },
  "prior_case": null,
  "approval": "NOT_REQUESTED",
  "verification": "NOT_RUN",
  "expected": {
    "decision": "BLOCK",
    "reason_code": "SUPPLIER_STOCK_UNKNOWN",
    "external_action_count": 0
  }
}
```

## Deterministic evaluator contract

Future reusable pure function shape, only when a canonical seam exists:

`evaluateEcommerceException(fixture) -> { decision, reason_code, action_intent, approval_required, verification_required, evidence_identity }`

Allowed decisions remain:
- `ALLOW_PREPARE`
- `REQUIRE_APPROVAL`
- `BLOCK`
- `VERIFY_FAILED`

The evaluator must not itself call Shopify, a supplier, email, browser, shell, database, scheduler, mission ledger, authority service, Green or PRS.

## Case mapping

| Case | Condition | Expected decision | Required assertion |
|---|---|---|---|
| EC-001 | supplier stock unknown | BLOCK | reason `SUPPLIER_STOCK_UNKNOWN`; zero action |
| EC-002 | supplier stock disagrees with Shopify | REQUIRE_APPROVAL or BLOCK per customer promise exposure | exact SKU/provider identity retained |
| EC-003 | SKU/variant identity mismatch | BLOCK | no fuzzy repair or inferred identity |
| EC-004 | tracking missing after evidenced dispatch | ALLOW_PREPARE | prepare request/escalation only, no mutation |
| EC-005 | conflicting tracking values | BLOCK | contradiction retained as evidence |
| EC-006 | tracking belongs to wrong order/package | BLOCK | exact order/package correlation required |
| EC-007 | late dispatch/ETA risk | REQUIRE_APPROVAL | material customer promise change never auto-sent |
| EC-008 | split fulfilment | REQUIRE_APPROVAL | action scope limited to affected fulfilment/order lines |
| EC-009 | customer promise at risk | REQUIRE_APPROVAL | no material communication without approval |
| EC-010 | hold recommended | REQUIRE_APPROVAL | only exact fulfilment-order identity may be proposed |
| EC-011 | release requested with wrong hold identity | BLOCK | exact hold ID required |
| EC-012 | supplier evidence stale/contradictory | BLOCK | stale evidence cannot authorize action |
| EC-013 | replay/duplicate event | BLOCK | same idempotency/event identity cannot repeat state-changing intent |
| EC-014 | verification re-read failure | VERIFY_FAILED | success cannot be emitted |

## Assertions borrowed from existing AgentOS test style

1. Same fixture input must produce byte-equivalent normalized decision output.
2. Replayed fixture/event identity must not generate a second state-changing intent.
3. Any fixture requiring approval returns no executable mutation instruction.
4. `BLOCK` and `VERIFY_FAILED` always imply `external_action_count = 0`.
5. Provider-facing code is absent from the evaluator source.
6. No `fetch`, HTTP URL, environment secret, child process or credential access belongs in deterministic fixture evaluation.
7. Missing required identity fields fail closed.
8. Unknown enum/status values fail closed rather than defaulting to a safe-looking business state.
9. Evidence timestamp/version ordering is evaluated explicitly; arrival order is not authority.
10. A verification result cannot set Green, PRS or overall mission completion.

## Placement recommendation

Do **not** add a new runtime to Overseer.

When an existing reusable commercial decision seam is approved, preferred structure is:

```text
<existing-product-repo>/fixtures/commercial-frontend/ecommerce/*.json
<existing-product-repo>/tests/...commercial-frontend...test.*
```

Until then, this mapping plus the EC specification is the canonical non-production contract.

## Gate result

CF-C006 = **VERIFIED AS MAPPING / IMPLEMENTATION DEFERRED**.

This does not satisfy direct customer evidence, provider integration, production reliability, AgentOS Wave/Level 2 readiness, Green or PRS assurance.
