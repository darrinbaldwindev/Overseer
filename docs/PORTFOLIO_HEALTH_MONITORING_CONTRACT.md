# Portfolio Health Monitoring Contract v1

## Purpose

Provide one repeatable, evidence-first health contract for every canonical portfolio repository. Green Agent may consume these records; Project Overseers may produce them; PRS independently assures applicable results.

## Required cycle

1. Resolve canonical repository and branch from the portfolio registry.
2. Capture the exact commit under inspection.
3. Check repository accessibility and control-plane files.
4. Run the project's canonical deterministic tests when available.
5. Check security/health signals and unresolved critical findings.
6. Confirm Project Overseer mission/heartbeat freshness.
7. Confirm evidence freshness and provenance.
8. Record PRS disposition where applicable.
9. Record Green Agent observation/disposition.
10. Produce a health result using `schemas/PORTFOLIO_HEALTH_CONTRACT.v1.json`.
11. On AMBER/RED/BLOCKED, create or update a durable finding and wake/escalate the responsible Project Overseer.
12. Re-scan after remediation before promoting health.

## GREEN rule

A repository is not GREEN because it is accessible, has recent commits, or reports success. GREEN requires sufficient current evidence for all applicable checks and no unresolved blocking finding. If evidence is missing, health cannot be promoted merely by inference.

## Equal portfolio treatment

Every canonical repository receives the same baseline checks. Project-specific checks may extend the baseline but may not weaken it.

## Wake/response contract

A finding must carry repository, commit, check, severity, evidence reference, owner/authority, and next action. A Project Overseer response must state what it inspected, what it changed, evidence produced, remaining risk, and requested upstream disposition.

## Failure behaviour

- Missing repository: BLOCKED; do not substitute another repository.
- Missing branch/path: BLOCKED pending reconciliation.
- Missing tests: AMBER unless the project explicitly records why tests are not applicable.
- Failed critical test/security check: RED.
- Stale/missing evidence for a required assurance gate: AMBER or BLOCKED according to the gate.
- Stale Project Overseer heartbeat: AMBER; escalate if it exceeds the configured freshness window.
- Conflicting project and independent assurance results: lower health to the safer disposition until reconciled.

## Non-goals

This contract does not create a second runtime, scheduler, router, worker registry, or assurance engine. It is a shared evidence contract for the existing Overseer, Green Agent, Project Overseer and PRS architecture.
