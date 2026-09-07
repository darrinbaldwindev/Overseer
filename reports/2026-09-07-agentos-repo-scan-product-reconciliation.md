# AgentOS Repo Scan & Product Reconciliation — 2026-09-07

**Owner:** Marketing Overseer  
**Status:** EXECUTED / EVIDENCE-GATED  
**Scope:** Repository scan, product/commercial reconciliation and free-capability registry design. No runtime, scheduler, credential, permission, production or merge actions.

## Scan findings

AgentOS main contained recent product/governance documentation establishing:

- `docs/AUTONOMY_SCALE.md` — graduated autonomy levels 0–5 with the invariant that autonomy does not itself grant permission.
- `docs/AUTONOMY_RUNTIME.md` — autonomous continuation semantics remain independent of scheduler implementation.
- `docs/AUTONOMY_MILESTONES.md` — scheduled execution is a measurable autonomy milestone rather than a marketing claim.
- `docs/COMMERCIAL-ACCESS-MODEL.md` — Free as a limited taste; $29/year and $99/year share the same AgentOS control plane and differ primarily by AI resources/capacity.
- Existing provider/catalog evidence is historical/synthetic rather than live: `catalog/PROVIDER_CATALOG_RECONCILIATION.md` has an August 2026 evidence cutoff and `catalog/CAPABILITY_COMPARISON_MATRIX.md` explicitly uses fixtures rather than live provider claims.
- `contracts/agentos-core-types.ts` already defines canonical ProviderRecord, ModelRecord, ToolRecord, health, capability, pricing and secret-reference structures suitable for reuse.

Open draft PR scan found:

- **PR #78** — first deterministic graduated-autonomy policy primitive; supports time-bounded autonomy with fail-closed expiry, but explicitly does not enable scheduling/providers/credentials/production autonomy.
- **PR #80** — governed local Basic Chat vertical slice; preserves DRY_RUN, disabled autonomy and fail-closed safeguards.
- Other governance/assurance drafts remain open/unmerged; no merge/approval/ready action was taken.

## Product tension identified

The latest commercial document says both paid tiers have full governed autonomy and differentiates them mainly by AI resources/capacity. Newer product research now treats **scope, persistence and scheduled autonomy** as important upgrade drivers, especially for the $99 Operator proposition.

The commercial document also still uses **Basic** for the simple view while current marketing work prefers **Everyday** as the leading customer-facing candidate. This is a naming/product mismatch, not a reason to disrupt current implementation branches.

## Action executed 1 — product/commercial reconciliation

Created:

`AgentOS/docs/PRODUCT-COMMERCIAL-RECONCILIATION-2026-09-07.md`

Commit:

`857503274d964688daecec98ceed0ca0c9acc475`

The artifact reconciles:

- One AgentOS / same control plane across plans.
- Views vs commercial entitlements.
- Free / $29 / $99 autonomy scope as a validation-gated entitlement hypothesis.
- Autonomy Hours / Night Shift.
- WHEN vs WHAT as separate control dimensions.
- Tonight's Queue.
- Morning Brief.
- Autonomy Authority Profiles.
- pause → preserve → approve → resume.
- Autonomy Budget.
- free/local routing without blind local-first assumptions.
- Basic as current internal/implementation language vs Everyday as validation-gated marketing candidate.
- safe defaults and explicit implementation gates.

No existing PR was modified.

## Action executed 2 — dynamic free capability registry specification

Created:

`AgentOS/catalog/FREE_CAPABILITY_REGISTRY_SPEC.md`

Commit:

`1fb6ad79842335494c258612a728625dcd63f7e0`

This specification deliberately extends rather than duplicates existing AgentOS provider/model/tool records.

Key rules:

- Consumer free access is not automatically callable AgentOS capacity.
- Open-source is not free hosted compute.
- Open weights are not automatically commercially unrestricted.
- Free allowances are dynamic and must not be hard-coded into product logic.
- Affiliate economics do not influence routing.
- Unknown remains unknown.
- Capabilities are grouped by outcome/fallback groups so providers can be replaced without changing the user-facing product.
- Current free-tier/API/terms evidence must be reverified and dated.
- Australia availability and commercial-use status are explicit evidence fields.
- High integration score does not authorize activation.

The registry specification reuses:

- canonical AgentOS core types;
- capability comparison semantics;
- provider health/fallback principles;
- existing evidence boundaries.

## Initial verification queue captured

The registry design identifies an initial research queue including:

- Gemini Developer API
- OpenRouter Free Router
- Groq
- Cloudflare Workers AI
- Mistral developer/free routes
- NVIDIA NIM development routes
- Ollama
- LocalAI
- llama.cpp
- vLLM
- Tavily
- Firecrawl
- Exa
- Jina Reader/Search
- Brave Search
- Playwright
- Composio
- Activepieces
- n8n
- Node-RED
- OpenHands
- Cline
- Aider
- Qwen Code
- SQLite
- DuckDB
- PostgreSQL/pgvector
- Qdrant
- Supabase
- Langfuse
- OpenTelemetry

This is a **research/verification queue, not an activation list**.

## Recommended next step

The highest-value next evidence task is now to populate the new registry design with a **small P0 verification tranche** from current official sources rather than attempting to catalogue hundreds of names immediately.

Suggested first tranche:

1. Gemini Developer API
2. OpenRouter Free Router
3. Groq
4. Cloudflare Workers AI
5. Ollama / LocalAI local inference path
6. Tavily / Firecrawl / Jina research path
7. Playwright execution path
8. one automation/integration layer (Composio or Activepieces)

For each, capture current official free status, limits, Australia availability, commercial-use constraints, privacy/data treatment, interface compatibility, capability tags, fallback group and AgentOS integration score.

## Evidence classification

- **FACT:** repository states, files and draft PR descriptions observed during this scan.
- **IMPLEMENTED:** the two new documentation/specification artifacts and durable handoff report.
- **RECOMMENDATION:** Night Shift/product reconciliation and dynamic registry structure.
- **HYPOTHESIS:** Free/$29/$99 autonomy packaging and customer conversion effect.
- **UNKNOWN:** final pricing/entitlements, live provider suitability, economic sustainability and runtime implementation until independently verified.

## Status

**AMBER — meaningful product/catalog reconciliation completed; runtime and commercial claims remain evidence-gated.**
