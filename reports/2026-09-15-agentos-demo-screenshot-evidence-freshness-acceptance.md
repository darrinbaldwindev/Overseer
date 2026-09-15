# AgentOS — Demo / Screenshot Evidence-Freshness Acceptance

**Date:** 2026-09-15 AEST  
**Task:** M-A046  
**Status:** COMPLETE / CREATIVE-EVIDENCE CONTRACT

## Principle
A screenshot or demo is not decoration when it is used to prove a capability. It becomes evidence-bearing creative and must carry the same freshness discipline as the product state it depicts.

## Asset classes
### A. Concept / mockup
Must be labelled concept, prototype or illustrative when a reasonable viewer could mistake it for shipped functionality. It cannot prove implementation.

### B. Historical implementation capture
May demonstrate that a feature existed on a named historical lineage. It cannot prove current readiness without revalidation.

### C. Current bounded implementation capture
May support a bounded current claim only when tied to current exact lineage and the relevant canonical evidence.

### D. Production capture
Requires separately verified production availability, current entitlement/access and no misleading staging/test data.

## Required metadata for evidence-bearing creative
Where materially applicable, Marketing's asset register should retain:
- capture date/time;
- exact commit/build/version;
- environment (`mock`, `test`, `staging`, `production`);
- host/device class where relevant;
- capability demonstrated;
- canonical evidence pointer;
- claim classification;
- known limitations;
- expiry/revalidation trigger.

This metadata need not all be shown publicly, but it must exist upstream of Content360/publication decisions.

## Revalidation triggers
An asset falls back to `REVIEW_REQUIRED` when:
- relevant implementation head changes;
- assurance status changes;
- dependency head changes materially;
- UI copy changes the meaning of a state;
- a previously positive state becomes UNKNOWN/BLOCKED;
- product pricing/tier mapping changes;
- the capture contains stale product names/claims;
- production availability differs from test/staging.

## AgentOS-specific examples
- A Basic Chat screenshot showing `Passed for this job` cannot be captioned as Henry/PRS assurance.
- A Windows-capability screen cannot prove physical Windows acceptance.
- A physical-acceptance PASS from a predecessor exact head cannot prove current mutation readiness.
- `Stop requested` cannot be edited/captioned as `Stopped immediately`.
- A conceptual 17-agent roster cannot prove all 17 are implemented or active on every request.
- Voice mockups remain PRODUCT DIRECTION until implementation evidence exists.
- A pricing screen must use the current canonical product direction, not superseded $29 assumptions.

## Content360 status mapping
- `CREATIVE_CONCEPT_ONLY` — usable for explicitly conceptual education, never implementation proof.
- `CREATIVE_CURRENT_BOUNDED` — current exact evidence supports the narrow depicted claim.
- `CREATIVE_REVIEW_REQUIRED` — stale/moved dependency or missing evidence.
- `CREATIVE_DO_NOT_PUBLISH` — misleading, contradictory or unsupported.

These are Marketing asset states; they do not grant publication/spend authority.

## Rule for generated AI visuals
Generated scenes may illustrate concepts, but must not manufacture screenshots, testimonials, usage evidence, security proof, customer outcomes or integrations that viewers could reasonably interpret as real.

## Disposition
**Content360 and landing-page creative must inherit evidence freshness. Historical or conceptual visuals cannot silently become current product proof.**