# Internal Sub-Worker Pool

Purpose: maintain a small provider-agnostic pool of ready-to-use internal worker roles. These are workers, not Overseers, and do not require separate user-facing chat windows.

## Core pool

### REPO-CODE
Repository structure, implementation, GitHub changes, code review and repository scans.

### QA-TEST
Test design, test execution where available, regression checks and evidence verification.

### RESEARCH
Web/repository research, evidence gathering, comparisons and requirements analysis.

### ARCHITECTURE
System architecture, integration boundaries, interfaces, trade-offs and AgentOS design.

### SKILLS
Reusable skill discovery, skill registry, capability routing, skill lifecycle and skill-memory integration.

### SECURITY-HEALTH
Security review, dependency/risk review, repository health, recovery and control-plane consistency.

## Operating model

GPTChat Overseer / Project Overseer -> worker role -> task -> execution -> evidence -> checkpoint -> response -> verification.

Workers are instantiated/selected as needed; this registry does not imply six continuously running processes. Provider workers such as Manus, Amazon Q and Gemini can be selected as execution providers for these roles when their capabilities and permissions match the task.

## Rules

- Workers do not supersede Project Overseers.
- Do not create a parallel task router.
- Use the canonical task/log/control-plane mechanisms.
- Missing evidence means UNKNOWN/PARTIALLY_VERIFIED, never VERIFIED.
- Keep provider choice separate from capability/skill identity.
- Prefer reuse of existing repository primitives, including skill memory and scan infrastructure.
- Only create a dedicated persistent worker process when there is a demonstrated need; otherwise treat these as ready-to-dispatch internal roles.
- Every autonomous portfolio cycle must reconcile useful outputs from all available workers/providers, including Gemini, Manus and other model workers, against current repository state.
- Worker/provider outputs are intelligence or candidate evidence until independently verified; they must never self-certify consequential implementation or GREEN status.
- Preserve source-agent/provider provenance on useful handoffs so downstream Overseers can distinguish origin from independent verification.
- Before creating new work from a worker/provider recommendation, reconcile it with the canonical portfolio registry, existing backlog/issues and current implementation to prevent duplicate runtimes, routers or assurance engines.

## Initial readiness

All six roles are defined and ready for dispatch. Implementation/runtime spawning is a separate capability question and must not be claimed merely from this registry.
