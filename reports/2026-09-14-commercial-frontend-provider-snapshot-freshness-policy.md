# Commercial Frontend — Provider Snapshot Freshness Policy

Date: 2026-09-14

## Mission

Define CF-C011: provider-neutral freshness handling for supplier/order/inventory/tracking evidence without inventing event authority.

## Core rule

**Arrival time is not authority.**

A later-observed payload may be older source evidence. A locally later fetch cannot by itself prove supersession. Ordering must come from a provider-defined authoritative sequence/version/source timestamp when one is actually documented for that endpoint or record class.

If freshness cannot be proven strongly enough for the proposed action, the cockpit must fail closed to `EVIDENCE_STALE`, `EVIDENCE_CONFLICT`, or `BLOCKED_NO_ACTION`.

## Evidence envelope

Every provider snapshot used for a recommendation should carry, where available:

- provider;
- account/shop identity;
- provider order/product/variant/SKU/package identity;
- source method (`api`, `webhook`, `app_sync`, `portal`, `email`, `csv`, `manual`);
- source timestamp exactly as supplied by the provider, if any;
- provider sequence/revision/version exactly as supplied, if any;
- local observed-at timestamp;
- fetch/request correlation;
- evidence hash/version inside AgentOS/commercial layer;
- documented provider cadence relevant to that evidence class;
- freshness disposition.

Local observed-at time records when AgentOS saw evidence. It does not rewrite provider chronology.

## Freshness dispositions

### `FRESH_ENOUGH_FOR_READ`
Evidence is sufficiently current for display/context, but not necessarily for mutation.

### `FRESH_ENOUGH_FOR_PREPARE`
Evidence is sufficiently current to prepare a recommendation or approval card. No external action follows automatically.

### `REFRESH_REQUIRED_BEFORE_ACTION`
Evidence may be shown, but any approval/action requires a fresh provider/system-of-record read first.

### `EVIDENCE_STALE`
Provider-documented cadence, source timestamp, or policy maximum age has been exceeded. Mutation is blocked.

### `FRESHNESS_UNPROVEN`
The evidence lacks enough provider semantics to establish age/currentness. Mutation is blocked.

### `EVIDENCE_SUPERSEDED`
A later authoritative provider version/sequence/source-time record for the exact same identity is known.

### `EVIDENCE_CONFLICT`
Two records that cannot both be current claim incompatible state and provider ordering/version semantics cannot resolve them.

## CJdropshipping policy

Current public API evidence supports strong identity for products, variants, shops/connections, storage/warehouse and real-time inventory queries.

Policy:

1. Prefer a fresh endpoint re-read immediately before any future consequential recommendation/action involving stock or order state.
2. Use endpoint-specific source timestamps only when the response contract actually defines them.
3. Do **not** assume CJ has a universal event sequence or version field across product, inventory, shop, order and logistics APIs.
4. A newer local fetch may replace an older local snapshot for display only if it addresses the exact same provider/entity scope; it still does not establish historical event ordering when the provider does not expose that ordering.
5. Contradictory same-scope evidence with no authoritative ordering -> `EVIDENCE_CONFLICT`.
6. Any stock-dependent mutation requires refresh/re-read rather than relying on cached snapshot age alone.

## Dropshipzone / New Aim policy

Current first-party retailer documentation supports portal/Shopify integration behavior, including automatic inventory synchronization and documented inventory/API/SKU-list refresh cadence from prior evidence. Exact retailer API event/version schema remains UNKNOWN.

Policy:

1. Documented cadence can define a **maximum tolerance for cached display/preparation**, but cannot create event sequence authority.
2. If a snapshot is older than the documented update cadence plus an explicitly recorded tolerance, classify `EVIDENCE_STALE` for stock-sensitive action.
3. Even within the cadence window, retailer stock evidence should be re-read through the authorized system-of-record/integration seam before a material Shopify/customer-promise mutation.
4. Portal/email tracking evidence may support exception preparation, but tracking mutation/action requires exact order/package correlation and re-read.
5. Supplier-side API fields must not be used as retailer freshness/version authority.
6. If exact retailer source timestamp/version is unavailable, use `FRESHNESS_UNPROVEN` rather than pretending local arrival time is the source timestamp.

## Conservative action rule

For any future mutation-capable flow, approval is bound to an evidence fingerprint containing at least:

- exact business identity tuple;
- source evidence version/hash;
- source timestamp/version when available;
- observed-at;
- recommendation/action class;
- policy version.

Immediately before execution, AgentOS must re-read the relevant systems of record. If the resulting fingerprint or material state differs from the approved evidence, the approval is stale and the cockpit transitions to `CHANGED_AFTER_APPROVAL`; no action is executed under the old approval.

## Time thresholds

This policy intentionally does **not** invent universal minute/hour thresholds.

Thresholds may come only from:

- provider-documented update cadence;
- endpoint semantics;
- business/customer promise constraints captured in the governed task;
- a later explicit policy approved for that vertical.

Where none exists, currentness for consequential action is established by a just-in-time re-read, not by a guessed cache TTL.

## Acceptance fixtures

1. old snapshot beyond documented cadence -> `EVIDENCE_STALE`.
2. recent local arrival but old provider source timestamp -> stale according to source time.
3. two contradictory snapshots with same provider version -> `EVIDENCE_CONFLICT`.
4. lower provider sequence arriving later -> older evidence cannot supersede.
5. higher authoritative sequence arriving earlier in local time -> provider sequence wins.
6. no provider source time/version and no safe just-in-time read -> `FRESHNESS_UNPROVEN`.
7. approval made on evidence A; pre-execution re-read B differs materially -> `CHANGED_AFTER_APPROVAL`.
8. duplicate evidence hash/event -> no second executable intent.

## Decision

CF-C011 is **VERIFIED AS POLICY CONTRACT / NO CONNECTOR ENABLEMENT**.

No live provider call, customer-system mutation, credential use, provider write or production authorization occurred.
