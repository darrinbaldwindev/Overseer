# AgentOS — Overseer Front-Door Implementation Watch

**Date:** 2026-09-16 AEST  
**Task:** M-A047  
**Status:** WATCH COMPLETE / PRODUCT CONTRACT STRONG / FULL IMPLEMENTATION NOT YET PROMOTED

## Product contract
The owner-approved interaction model remains:
`User → Overseer → specialist agents/models/tools/capabilities → Overseer → User`.

The user should not need to choose a specialist agent as a competing conversational endpoint.

## Fresh implementation evidence
Frontend #111 provides meaningful supporting evidence for a single primary Chat experience:
- ordinary-user Chat copy with progressive technical disclosure;
- Simple / Essentials / Tech Head presentation modes around the same bounded experience;
- canonical read-only evidence and Recent Jobs projections;
- project-scoped Jobs fail closed rather than creating frontend-owned project truth;
- Green and PRS remain separate;
- Projects and Inbox remain explicitly unwired when canonical composition/attention sources are absent.

This supports the product direction, but does not by itself prove a complete runtime-wide Overseer router across every agent/model/tool/modality.

## Marketing promotion
Safe:
> **AgentOS is designed around one primary Overseer experience that coordinates specialist capability behind the user's request.**

Stronger bounded wording for current frontend work:
> **The current Basic Chat frontend is being implemented as the primary ordinary-user interaction surface, with technical detail progressively disclosed rather than requiring users to manage specialist endpoints.**

Not yet supportable:
- `Every AgentOS interaction already routes through the Overseer.`
- `All 17 specialist agents are wired behind Chat.`
- `Voice, browser, email and every capability share one proven production Overseer path.`
- `There are no alternate runtime entry points.`

## Evidence needed for full implementation promotion
- canonical Overseer request/router seam;
- stable specialist role/agent registry where applicable;
- authority preserved through routing;
- evidence correlation preserved through handoffs;
- no direct persona bypass;
- supported modality parity;
- end-to-end tests for representative specialist delegation;
- shipped frontend/runtime integration.

## Disposition
**Single-front-door remains a strong owner-approved product contract with meaningful frontend implementation alignment, but full end-to-end runtime implementation remains evidence-gated.**