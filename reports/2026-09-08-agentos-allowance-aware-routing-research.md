# AgentOS Research Packet: Allowance-Aware Capability Routing

**Prepared:** 2026-09-08  
**Scope:** Provider-neutral control-plane routing across free, trial-limited, daily-reset, subscription-capped, rate-limited, local, and paid capabilities.

## Executive recommendation

AgentOS should implement allowance awareness as a **resource-selection concern after authority and eligibility, never as an authority source**. The control-plane order should be:

> task requirements → authority and policy → capability eligibility → quality floor → verification requirements → allowance and reset horizon → cost and latency → deterministic tie-break → execution → independent verification.

The smallest useful architecture is a provider-neutral **Capability Registry**, an **Allowance Ledger**, a **Health/Telemetry Collector**, a deterministic **Route Evaluator**, and a **Verification Planner**. Each provider adapter should expose normalized metadata and should retain raw provider evidence for auditability.

The router should reject a capability before scoring it if any hard requirement fails: missing authority, incompatible data policy, inadequate quality, unsupported modality, insufficient verification independence, known outage, or insufficient allowance for the estimated request. Only then should it maximize a value function that rewards utility and expiring capacity while penalizing cost, latency, uncertainty, and operational risk.

This follows established gateway patterns. LiteLLM documents routing, retries, cooldowns, fallbacks, health-check-driven routing, and budget routing across deployments and providers.[1] OpenRouter exposes provider ordering, fallback controls, parameter compatibility, data-retention restrictions, price/latency/throughput sorting, and maximum-price constraints.[2] Rate-limit APIs commonly expose remaining capacity and reset horizons directly in response headers; OpenAI documents request, token, project-token, retry, and reset fields.[3] Google documents simultaneous RPM, TPM, RPD, spend, model, project, and reset constraints.[4]

**Critical safety conclusion:** an expiring allowance can increase the priority of an already-authorized useful task, but it must never create a task, expand permissions, lower a quality floor, bypass a verifier, or convert a human-confirmation requirement into an automatic action.

## Evidence boundary

### Research-backed findings

The following are patterns documented by current primary or first-party sources:

| Finding | Evidence |
|---|---|
| Provider-neutral gateways commonly combine routing, retries, cooldowns, health checks, fallbacks, and budgets. | LiteLLM documents these as router capabilities.[1] |
| Provider selection can be constrained by provider order, fallback permission, required parameters, data-collection policy, zero-data-retention requirements, allowed/ignored providers, quantization, price, throughput, latency, and maximum price. | OpenRouter documents these request-level controls.[2] |
| Rate limits are multi-dimensional rather than a single remaining counter. | OpenAI documents request, token, project-token, remaining, reset, and retry fields.[3] Google documents RPM, TPM, RPD, spend-based limits, model-specific limits, and project-scoped limits.[4] |
| Retry handling must distinguish temporary throttling or overload from quota, billing, and user-action errors. | OpenAI explicitly advises not retrying quota, billing, or other errors requiring action, and recommends honoring `Retry-After`, bounded retries, and jitter.[3] |
| Local runtimes can be treated as adapters rather than special cases. | Ollama exposes a local API at `localhost:11434/api`, provides model interaction APIs, and offers OpenAI-compatible access.[5] |
| Local health and saturation should be observable. | vLLM exposes `/metrics` with request, token, cache, preemption, and running-request metrics.[6] |
| Trustworthiness requires governance, measurement, and management throughout the lifecycle. | NIST AI RMF organizes risk management around Govern, Map, Measure, and Manage and emphasizes evaluation.[7] |
| Model availability does not justify broad action authority. | OWASP identifies excessive functionality, permissions, and autonomy as causes of excessive agency and recommends least privilege, granular tools, independent verification, and user approval for high-impact actions.[8] |
| Web-research providers can expose structured search, extraction, project tracking, session tracking, budgets, and citations. | Tavily documents search, extraction, crawl, map, research, project IDs, and session IDs.[9] Perplexity documents ranked results, domain filters, extracted content, and explicit content/token budgets.[10] |

### Repository facts versus recommendations

**Repository facts:** none are available in this task. No AgentOS repository, schemas, logs, adapters, or existing implementation files were supplied or inspected. References to “allowance-aware delegation,” “Green Agent,” “PRS,” Manus credits, local Ollama, and web/research tools are treated as architectural context supplied by the request, not verified repository facts.

**Recommendations:** the schema, scoring function, decision matrix, pseudocode, examples, implementation slice, and acceptance tests below are design recommendations derived from the evidence and the stated AgentOS direction. They are not claims about existing AgentOS behavior.

## Conceptual model

AgentOS should keep six states separate:

1. **Availability:** can the adapter be reached and does it advertise the requested capability?
2. **Authority:** is this capability permitted for this task, principal, data class, and action scope?
3. **Health:** is it currently likely to succeed within deadline and reliability objectives?
4. **Allowance:** how much use remains, under which dimensions, until which reset or expiry?
5. **Economics:** what monetary, credit, opportunity, and latency cost is expected?
6. **Verification:** can the result be independently checked to the required confidence?

These states must not be collapsed into one `available=true` bit. A provider can be reachable but unauthorized, authorized but unhealthy, healthy but allowance-exhausted, or cheap but unverifiable.

## Capability and allowance state schema

The following is a normative recommendation for a versioned internal representation. Raw provider responses should be retained alongside normalized fields.

```yaml
CapabilityState:
  capability_id: string
  provider_id: string
  adapter_version: string
  kind: llm | web_research | embedding | code_execution | human_review | other
  model_or_tool: string
  locality: local | remote | hybrid
  endpoint_ref: opaque-reference
  observed_at: timestamp
  expires_at: timestamp|null

  supports:
    modalities: [text, image, audio, video, code]
    operations: [generate, classify, extract, search, execute, verify]
    max_context_tokens: integer|null
    structured_output: boolean
    streaming: boolean
    tool_use: boolean
    citations: boolean

  policy:
    allowed_principals: [string]
    allowed_data_classes: [public, internal, confidential, restricted]
    allowed_actions: [string]
    requires_human_confirmation: boolean
    provider_independence_group: string
    verifier_independence_group: string|null
    data_retention: unknown | none | limited | provider-defined
    residency: string|null

  health:
    status: healthy | degraded | unavailable | unknown
    success_rate: number|null
    p50_latency_ms: number|null
    p95_latency_ms: number|null
    queue_depth: number|null
    saturation: number|null
    consecutive_failures: integer
    cooldown_until: timestamp|null
    source: probe | provider | inferred

  allowance_dimensions:
    - dimension_id: string
      unit: requests | input_tokens | output_tokens | credits | dollars | gpu_seconds | searches | unknown
      scope: key | user | project | subscription | provider | machine
      limit: number|null
      remaining: number|null
      reserved: number|null
      reset_at: timestamp|null
      expires_at: timestamp|null
      rollover: true | false | unknown
      confidence: exact | estimated | stale | unknown
      observed_at: timestamp|null
      source: header | dashboard_api | provider_api | local_meter | configured | inferred
      hard_or_soft: hard | soft | unknown
      error_on_exhaustion: retryable | non_retryable | unknown

  economics:
    fixed_cost_usd: number|null
    input_cost_per_million_tokens: number|null
    output_cost_per_million_tokens: number|null
    allowance_shadow_cost: number|null
    latency_cost_weight: number|null
    currency: string

  quality:
    capability_score: number
    task_fit_score: number
    historical_success_score: number|null
    citation_or_grounding_score: number|null
    minimum_supported_quality: number
    quality_evidence_timestamp: timestamp|null

  verification:
    supported_verifiers: [string]
    independent_verifier_available: boolean
    expected_confidence: number
    provenance_available: boolean
    replayable: boolean

  provenance:
    raw_observation_ref: opaque-reference|null
    source_urls: [string]
    source_hash: string|null
```

A separate **TaskRequirement** object should contain the requested operation, data classification, principal, deadline, quality floor, maximum cost, maximum latency, required modalities, required citation level, allowed provider classes, verifier independence requirement, human-confirmation requirement, and whether the task is user-requested or system-scheduled.

## Allowance semantics

Allowance should be modeled as a vector of constraints, not a scalar balance. A request is allowance-feasible only if it satisfies every relevant dimension:

```text
estimated_requests <= remaining_requests
estimated_input_tokens <= remaining_input_tokens
estimated_output_tokens <= remaining_output_tokens
estimated_dollars <= remaining_dollars
estimated_searches <= remaining_searches
estimated_gpu_seconds <= remaining_gpu_seconds
```

If any dimension is unknown, the router should apply a configurable uncertainty reserve. For example, if `remaining=unknown`, the capability may be eligible for low-risk probing only when a bounded probe is allowed; it should not be selected for an expensive or irreversible task merely because the balance is unknown.

Use `reserved` to prevent concurrent decisions from oversubscribing the same allowance. Reservation should be atomic, have a lease, and be released or reconciled after execution.

A reset horizon is the earliest applicable future replenishment or expiry boundary. For a daily allowance, `reset_at` is the next daily reset. For non-rollover credits, `expires_at` is the hard deadline. For rolling windows, the adapter should report the provider’s reset estimate or a conservative upper bound.

## Routing decision matrix

| Stage | Question | Reject or action | Safety meaning |
|---|---|---|---|
| 1. Task parse | What operation, data, deadline, quality, and authority are required? | Fail closed on missing material requirements. | Prevents optimization from defining the task. |
| 2. Authority | Is the principal authorized to use this capability for this data and action? | Exclude if false or unknown for protected data/actions. | Availability never grants authority. |
| 3. Capability fit | Does the adapter support the modality, operation, context, and output contract? | Exclude incompatible capabilities. | Avoids silent degradation. |
| 4. Data policy | Does retention, residency, privacy, and provider policy satisfy task constraints? | Exclude non-compliant providers. | Prevents cheap routing from leaking data. |
| 5. Quality floor | Is predicted quality at or above the task minimum? | Exclude below-floor candidates. | Expiring capacity cannot justify low-quality work. |
| 6. Verification | Is a verifier available at the required confidence and independence? | Exclude or require human review. | Prevents verifier weakening under quota pressure. |
| 7. Health | Is the capability healthy enough for the deadline? | Exclude unavailable or cooled-down providers. | Avoids predictable failure. |
| 8. Allowance feasibility | Can all quota dimensions cover the estimated request plus reserve? | Exclude hard-infeasible candidates; defer unknowns if needed. | Prevents wasteful retries and oversubscription. |
| 9. Expiry value | Does selecting this candidate for a useful queued task avoid loss of valid capacity? | Add bounded priority bonus only to existing useful work. | No filler work is created. |
| 10. Cost and latency | Which eligible candidate meets budget and deadline at lowest total cost? | Score or apply lexicographic tie-breaks. | Makes trade-offs explicit. |
| 11. Determinism | Are ties resolved reproducibly? | Sort by stable score, provider ID, capability ID. | Enables audit and testing. |
| 12. Post-execution | Did actual usage, outcome, and verification match estimates? | Reconcile ledger; update health and quality estimates. | Closes the control loop. |

## Deterministic selection algorithm

The recommended implementation uses hard gates followed by a bounded score. A score must never rescue a candidate that fails a hard gate.

```text
select(task, capability_states, now):
    requirements = normalize_task(task)
    assert requirements.authority_decision is already evaluated

    candidates = []
    for c in capability_states:
        if not authority_allows(requirements, c.policy):
            continue
        if not supports(c, requirements):
            continue
        if not data_policy_allows(requirements, c.policy):
            continue
        if c.quality.capability_score < requirements.quality_floor:
            continue
        if not verification_compatible(requirements, c.verification, c.policy):
            continue
        if c.health.status == unavailable:
            continue
        if c.health.cooldown_until != null and c.health.cooldown_until > now:
            continue

        estimate = estimate_usage(requirements, c)
        feasibility = allowance_feasibility(c.allowance_dimensions, estimate)
        if feasibility == HARD_INFEASIBLE:
            continue
        if feasibility == UNKNOWN and not requirements.allow_bounded_probe:
            continue
        if expected_latency(c) > requirements.max_latency_ms:
            continue
        if expected_cost(c, estimate) > requirements.max_cost_usd:
            continue

        quality = conservative_quality(c, requirements)
        verify = conservative_verification(c, requirements)
        health = conservative_health(c)
        cost = normalized_cost(c, estimate)
        latency = normalized_latency(c, requirements)
        uncertainty = allowance_uncertainty(c, estimate)
        expiry_value = useful_expiry_value(task, c, now)

        score = (
            WQ * quality
          + WV * verify
          + WH * health
          + WE * expiry_value
          - WC * cost
          - WL * latency
          - WU * uncertainty
        )

        candidates.append({capability:c, estimate, score, tie_key:(c.provider_id,c.capability_id)})

    if candidates is empty:
        return NO_ROUTE_WITH_REASONED_FAILURE

    sort candidates by descending score, then ascending provider_id, then ascending capability_id
    winner = candidates[0]

    reserve = atomic_reserve(winner.capability, winner.estimate, requirements.reservation_ttl)
    if reserve.failed:
        mark_stale_and_retry_selection_once()
        return select(task, refreshed_states, now)

    return RoutePlan(
        capability=winner.capability,
        reservation=reserve,
        fallback_candidates=top_k_nonconflicting(candidates, requirements),
        verifier=select_independent_verifier(requirements, winner.capability),
        reason=explain_score_and_gates(winner)
    )
```

### Expiring-capacity score

`useful_expiry_value` should be zero unless all of the following hold:

1. The task already exists in the queue or is an explicitly authorized scheduled task.
2. The task passes authority, quality, data-policy, health, and verification gates.
3. The capability’s capacity would otherwise expire or reset before the task could be served.
4. The expected utility of completing the task exceeds a minimum utility threshold.
5. The work is not duplicated, synthetic filler, or generated solely to consume capacity.

A practical bounded form is:

```text
expiry_value = min(1, urgency / horizon) * utility_surplus * confidence
```

where `horizon` is time until reset or expiry, `utility_surplus` is expected task utility above the minimum threshold, and `confidence` discounts stale or estimated allowance data. Cap the bonus so it cannot outweigh a hard safety or quality constraint and cannot make a more expensive or much slower route win without an explicit policy.

The router should **not** manufacture benchmark prompts, idle summaries, redundant retries, or speculative background tasks to consume expiring credits. If no useful queued task qualifies, capacity may expire.

## Value per expiring credit

Use a thresholded ratio only after hard gates:

```text
value_per_credit =
    (expected_utility - minimum_utility)
    / max(expected_consumption_in_credit_units, epsilon)
```

Then adjust for the reset horizon:

```text
priority = value_per_credit
         * min(1, urgency / max(time_to_reset, epsilon))
         * verification_confidence
         * allowance_confidence
```

Do not treat a free request as zero cost. Its **shadow cost** includes opportunity cost, rate-limit contention, verification work, data exposure, failure risk, and the possibility of displacing a higher-value task. Paid capacity can therefore win when free capacity is scarce, uncertain, low quality, or needed for a higher-value future task.

## Provider examples

The values below illustrate adapter behavior, not current provider entitlements.

### Manus daily credits

The Manus adapter should expose a daily-credit allowance dimension with `unit=credits`, `scope=subscription_or_account`, `reset_at=next_known_daily_reset`, and `source=provider_api_or_configured`. The adapter must not hard-code a numeric credit balance unless the provider exposes it through an authoritative telemetry source. If the balance is unknown, the router should use a conservative reserve or select another eligible capability for expensive work. A useful, authorized task can receive a bounded expiry bonus when credits would reset soon, but verification, authority, and quality floors remain unchanged.

### Free cloud-model quota

Represent a free cloud model as at least RPM, TPM, and RPD dimensions. Google’s current documentation illustrates why all dimensions matter: exceeding any one can trigger an error, and RPD resets at a stated timezone.[4] The adapter should record timezone-normalized `reset_at`, project scope, model scope, and whether the quota is guaranteed or only an observed limit. Free status should affect economics, not eligibility or safety.

### Paid API

Represent a paid provider with cost-per-token, spend cap, RPM, TPM, and retry/reset fields. If the paid provider returns `Retry-After` or remaining/reset headers, update the ledger from the response.[3] Use paid capacity as a fallback when free capacity is infeasible, but require the task’s budget policy to allow the spend. Never silently exceed a user or project spend cap.

### Local Ollama

Register Ollama as `local` with endpoint health, loaded-model inventory, context limits, GPU/CPU saturation, queue depth, observed latency, and zero external API cost. Ollama’s documented local endpoint is `http://localhost:11434/api`.[5] Local does not automatically mean high quality, available, private in every deployment, or free of opportunity cost. Route to it when its quality floor, latency, model fit, and local policy satisfy the task.

### Web research capability

Represent search and research as a capability family with operation-specific allowance units such as searches, extracted pages, crawl depth, or research jobs. Record source provenance, citation support, domain restrictions, freshness, and token/content budgets. Tavily supports project and session tracking.[9] Perplexity exposes ranked results, domain filtering, extracted content, and content budgets.[10] A web-research result should usually be verified by source inspection or an independent synthesis step; a search provider should not automatically serve as its own independent verifier for high-stakes claims.

## Top integration candidates and patterns

| Candidate or pattern | Integrate or adapt | Why it fits | Boundary |
|---|---|---|---|
| LiteLLM Router/Proxy | Adapt or integrate behind an AgentOS adapter | Provides provider-neutral routing, retries, cooldowns, fallbacks, health checks, budget routing, and observability hooks.[1] | AgentOS must retain its own authority, verification, and allowance semantics rather than delegating policy to the gateway. |
| OpenRouter provider controls | Integrate where acceptable, or mirror the pattern | Request-level provider ordering, fallback controls, parameter compatibility, data policy, price/latency/throughput sorting, and max-price constraints are directly relevant.[2] | External routing does not replace AgentOS’s data classification, verifier independence, or spend authorization. |
| Ollama | Direct adapter | Local endpoint and OpenAI compatibility make it a practical local capability source.[5] | Add local health, GPU saturation, model inventory, and privacy policy telemetry. |
| vLLM metrics | Adapt telemetry pattern | `/metrics` provides operational signals for local model serving, including running requests, cache use, tokens, preemption, and successes.[6] | Metrics indicate health and saturation, not authority or semantic quality. |
| OpenAI/Gemini-style quota headers | Normalize adapter pattern | Remaining and reset headers provide concrete allowance telemetry; Gemini demonstrates multi-dimensional quotas and reset scopes.[3][4] | Providers differ; preserve raw headers and attach confidence and timestamp. |
| Tavily or Perplexity search | Use through a web-research adapter | Structured search, extraction, budgets, project/session tracking, ranking, and citations support provenance-aware research.[9][10] | Add domain policy, freshness requirements, source independence, and claim verification. |
| NIST AI RMF and OWASP controls | Adapt as governance patterns | They provide a credible separation between risk governance, measurement, least privilege, independent verification, and human approval.[7][8] | These are control frameworks, not routing engines. |

## Failure modes and safeguards

| Failure mode | Safeguard |
|---|---|
| Multiple free tiers are all treated as unlimited. | Model each account/project/key separately; enforce per-scope limits and anti-abuse policy. |
| Unknown allowance is treated as infinite. | Use `unknown` confidence, conservative reserve, bounded probe, or exclude for costly tasks. |
| Stale quota data causes oversubscription. | Timestamp observations, apply TTLs, use atomic reservations, and reconcile actual usage. |
| Provider outage triggers a retry storm. | Honor `Retry-After`, use bounded exponential backoff with jitter, cooldown unhealthy providers, and switch only to pre-eligible fallbacks.[1][3] |
| Per-minute quota is confused with daily quota. | Keep independent dimensions; feasibility requires every dimension to pass.[3][4] |
| Daily reset timezone is wrong. | Store timezone and normalized reset instant from the provider; never assume local midnight.[4] |
| Non-rollover credits are wasted or consumed by filler. | Schedule only existing useful work; use expiry priority only above a utility threshold. |
| Prepaid credits silently incur spend. | Require explicit budget authorization and enforce hard spend caps. |
| BYOK key is rotated into a different owner or policy scope. | Treat each credential as a distinct principal/account scope; never infer authority from possession of a key. |
| Local GPU is saturated. | Incorporate queue depth, saturation, p95 latency, and cooldown into health; fall back to remote only if policy permits.[6] |
| Quota exhaustion weakens verification. | Verification is a hard gate; if no verifier is available, defer, downgrade output status, or require human review. |
| Provider verifies its own output. | Require a distinct verifier model, provider, evidence source, or human where independence is required. |
| Expiry bonus picks a poor model. | Apply expiry only after quality and verification floors; cap its contribution. |
| Fallback changes data-retention or residency properties. | Re-run data-policy eligibility for every fallback candidate. |
| Two workers spend the same remaining allowance. | Use atomic lease reservations and post-call reconciliation. |
| A retry repeats a non-idempotent action. | Separate generation/research from action execution; require idempotency keys and confirmation for consequential operations. |
| A provider reports a false or optimistic balance. | Retain raw evidence, track confidence, compare predictions to actual usage, and fail closed on repeated inconsistency. |

## Smallest AgentOS implementation slice

Implement the following slice before building adaptive learning or complex portfolio optimization:

1. Define `TaskRequirement`, `CapabilityState`, `AllowanceDimension`, `RoutePlan`, and `ExecutionReceipt` schemas.
2. Implement a registry with five adapters: Manus daily credits, one free cloud model, one paid API, local Ollama, and web research.
3. Normalize health, cost, latency, allowance, reset, provenance, and verification metadata.
4. Implement hard eligibility gates and a deterministic score with stable tie-breaking.
5. Add atomic allowance reservations with TTL and execution reconciliation.
6. Add one independent verification policy for generated outputs and one human-confirmation policy for consequential actions.
7. Emit an explainable decision record containing excluded candidates and reasons, not only the winner.
8. Add telemetry dashboards or logs for allowance freshness, reservation failures, actual-versus-estimated usage, route distribution, and verification outcomes.

Defer reinforcement learning, opaque semantic routers, automatic filler generation, and cross-provider credential rotation until the deterministic baseline is stable and auditable.

## Acceptance tests

| ID | Test | Expected result |
|---|---|---|
| A1 | Capability is reachable but policy denies the data class. | It is excluded before scoring. |
| A2 | Free capability has expiring credits but is below the task quality floor. | It is excluded; no expiry bonus rescues it. |
| A3 | Paid provider is costlier but the free provider’s allowance is hard-infeasible. | Paid provider is selected if budget-authorized. |
| A4 | Allowance is unknown for a high-cost request. | Candidate is excluded unless bounded probing is explicitly allowed. |
| A5 | Two candidates have equal score. | Stable provider/capability tie-break produces the same winner across runs. |
| A6 | Two concurrent workers see the same remaining credits. | Only one reservation succeeds for the overlapping budget. |
| A7 | Provider returns 429 with `Retry-After`. | Router waits at least the specified delay or selects an eligible fallback; it does not hot-loop. |
| A8 | Provider returns a billing/quota error requiring user action. | Router does not retry indefinitely and records a non-retryable failure. |
| A9 | Daily reset is midnight Pacific while AgentOS runs in another timezone. | Reset is converted correctly and expiry scoring uses the absolute instant. |
| A10 | Local Ollama is healthy but GPU saturation exceeds threshold. | Local candidate is degraded or excluded based on policy. |
| A11 | Web research provider returns citations but the claim needs independent verification. | The route plan includes a separate verifier or marks the result unverified. |
| A12 | Verifier uses the same provider and same evidence path as the generator when independence is required. | Route is rejected or human verification is required. |
| A13 | No eligible capability remains. | Router returns a reasoned no-route result with remediation, not an unsafe downgrade. |
| A14 | Expiring capacity exists but no authorized useful task is queued. | No filler task is created; capacity may expire. |
| A15 | Fallback has different residency or retention policy. | Fallback is excluded unless the task policy explicitly allows it. |
| A16 | Actual tokens exceed estimate and consume the reserved allowance. | Receipt reconciles the delta, records estimation error, and updates future reserves. |
| A17 | A high-impact action is requested with a capability that requires confirmation. | Plan pauses for human confirmation; quota pressure cannot bypass it. |
| A18 | Manus credit balance is not available from an authoritative source. | Adapter reports unknown confidence and does not invent a numeric balance. |

## Final design principles

**First, optimize only over eligible capabilities.** Optimization is not policy.

**Second, represent allowances as typed, scoped, time-bounded dimensions.** A request quota, token quota, credit balance, spend cap, and GPU budget are not interchangeable.

**Third, make unknowns explicit.** Unknown allowance, stale health, and uncertain quality should reduce confidence or cause deferral rather than silently become “available.”

**Fourth, treat expiring capacity as an opportunity-cost signal.** It may reprioritize useful work. It must not create work or lower controls.

**Fifth, preserve independent verification.** The verifier is a separate control-plane decision with its own eligibility and allowance checks.

**Sixth, keep decisions deterministic and explainable.** A stable route can be optimized later, but it must be auditable now.

## References

[1]: https://docs.litellm.ai/docs/routing-load-balancing "LiteLLM Routing & Load Balancing"

[2]: https://openrouter.ai/docs/guides/routing/provider-selection "OpenRouter Provider Routing"

[3]: https://developers.openai.com/api/docs/guides/rate-limits "OpenAI API Rate Limits"

[4]: https://ai.google.dev/gemini-api/docs/rate-limits "Gemini API Rate Limits"

[5]: https://docs.ollama.com/api/introduction "Ollama API Introduction"

[6]: https://docs.vllm.ai/en/stable/usage/metrics/ "vLLM Production Metrics"

[7]: https://www.nist.gov/itl/ai-risk-management-framework "NIST AI Risk Management Framework"

[8]: https://genai.owasp.org/llmrisk/llm06-sensitive-information-disclosure/ "OWASP LLM06:2025 Excessive Agency"

[9]: https://docs.tavily.com/documentation/api-reference/introduction "Tavily API Introduction"

[10]: https://docs.perplexity.ai/docs/search/quickstart "Perplexity Search API Quickstart"

---

**Status note:** This packet is a research recommendation. It contains no production actions, credentials, purchasing, deployment, or external account changes. No AgentOS repository evidence was available in the task context.
