# Commercial Frontend — Supplier Evidence Fixture-to-Harness Mapping

Date: 2026-09-16 (Brisbane)
Status: VERIFIED AS NON-PRODUCTION MAPPING / NO RUNTIME ENABLEMENT

## Purpose
Map the existing supplier-evidence fixtures `SF-001..SF-016` into the existing Ecommerce synthetic harness semantics without creating a new runtime, queue, state authority, connector, evidence authority or provider truth source.

## Invariants
- Reuse the existing Ecommerce outcomes: `ALLOW_PREPARE`, `REQUIRE_APPROVAL`, `BLOCK`, `VERIFY_FAILED`.
- Reuse shared cockpit truth states including `READY_TO_PREPARE`, `APPROVAL_REQUIRED`, `BLOCKED_NO_ACTION`, `VERIFICATION_FAILED`, `EVIDENCE_STALE`, `EVIDENCE_SUPERSEDED`, `EVIDENCE_CONFLICT`, `CHANGED_AFTER_APPROVAL`, `REPLAY_DENIED`, `EXECUTION_PENDING_VERIFICATION`, `EXECUTION_CONFIRMED`.
- `DIRECT_SUPPLIER_EVIDENCE` may describe supplier truth only for its exact evidenced scope.
- `SYNCHRONIZED_SUPPLIER_EVIDENCE` is Shopify/app-observed synchronized state and never silently becomes direct supplier truth.
- `SHOPIFY_NATIVE_EVIDENCE` is authoritative only for the exact Shopify state represented.
- local arrival/observation time is not provider event-order authority.
- missing identity/provenance/freshness remains explicit UNKNOWN and fails closed where material.
- no fixture creates production authority.

## Mapping
| Fixture | Condition | Harness outcome | Cockpit truth state | Required assertion |
|---|---|---|---|---|
| SF-001 | direct supplier + synchronized Shopify agree, exact identity, fresh | ALLOW_PREPARE | READY_TO_PREPARE | preserve both provenance chains; no authority widening |
| SF-002 | Shopify-native state only; no supplier assertion needed | ALLOW_PREPARE | READY_TO_PREPARE | label as Shopify-native only |
| SF-003 | synchronized supplier state present; direct supplier absent | REQUIRE_APPROVAL | APPROVAL_REQUIRED | supplier-direct truth remains UNKNOWN; reread before material action |
| SF-004 | provider provenance missing | BLOCK | BLOCKED_NO_ACTION | do not infer supplier/provider source |
| SF-005 | Shopify product/variant identity mismatches supplier SKU identity | BLOCK | EVIDENCE_CONFLICT | zero mutation; exact identity mismatch surfaced |
| SF-006 | direct supplier and synchronized Shopify stock conflict | BLOCK | EVIDENCE_CONFLICT | do not choose reassuring source implicitly |
| SF-007 | synchronized stock beyond documented cadence/tolerance | BLOCK | EVIDENCE_STALE | refresh required; local observation cannot refresh provider truth |
| SF-008 | newer direct supplier evidence supersedes older synchronized evidence | BLOCK | EVIDENCE_SUPERSEDED | old evidence cannot authorize action |
| SF-009 | approval bound to old evidence; reread materially changed | BLOCK | CHANGED_AFTER_APPROVAL | invalidate prior approval |
| SF-010 | duplicate evidence/event identity replay | BLOCK | REPLAY_DENIED | no second action/intent |
| SF-011 | same provider version/revision with contradictory payload | BLOCK | EVIDENCE_CONFLICT | fail closed; no arrival-time tie break |
| SF-012 | order/package/tracking scope mismatch | BLOCK | EVIDENCE_CONFLICT | tracking cannot transfer across package/order identity |
| SF-013 | supplier source timestamp absent; Shopify update time present | REQUIRE_APPROVAL | APPROVAL_REQUIRED | Shopify chronology cannot become supplier chronology; freshness unproven |
| SF-014 | provider direct reread fails before consequential action | BLOCK | VERIFICATION_FAILED | no action from cached state |
| SF-015 | prepared action executes synthetically but post-action reread conflicts | VERIFY_FAILED | VERIFICATION_FAILED | execution success cannot become confirmed outcome |
| SF-016 | exact fresh evidence + approval + simulated action + matching reread | REQUIRE_APPROVAL then synthetic execute | EXECUTION_CONFIRMED | confirmation requires matching post-action evidence; assurance remains separate |

## Harness envelope
Each case should use the existing provider-neutral evidence envelope where fields exist:
- provider/supplier identity;
- Shopify shop/order/product/variant/fulfilment/package identity;
- supplier/provider SKU identity;
- evidence source class;
- provider source timestamp/version/sequence only when actually supplied by the provider contract;
- Shopify update timestamp only as Shopify chronology;
- local observed-at;
- evidence hash/version and request/fetch correlation;
- freshness disposition;
- approval evidence fingerprint where applicable.

## Negative assertions shared by every fixture
1. no live Shopify/provider call;
2. no customer communication;
3. no hold/release/refund/fulfilment mutation;
4. no missing field is synthesized;
5. no worker result creates Green/PRS assurance;
6. receipt/evidence presence does not imply independent assurance;
7. Simple/Essentials/Tech Head may reduce detail but cannot change the truth state.

## Build disposition
This mapping is suitable for deterministic non-production fixture implementation on an explicitly assigned branch, but it does not itself authorize implementation, connector activation or production use. Commercial demand remains UNKNOWN.