# TEST-002

## Assigned by
GPTChat Overseer

## Executor
Manus (worker)

## Project
GlobalShopCo

## Objective
Perform an evidence-backed read-only baseline/architecture audit of GlobalShopCo to establish the real repository state for the first usable Shopify + WordPress headless vertical slice.

## Required work
1. Inventory the complete repository structure relevant to the application.
2. Identify application entry points, configuration, dependencies and build/test surfaces.
3. Inspect and document Shopify backend/product/checkout assumptions and WordPress headless integration assumptions.
4. Identify what is implemented, partially implemented, missing, or contradictory for the first usable vertical slice.
5. Identify the smallest highest-value next implementation tasks.
6. Return evidence references for material findings; distinguish evidence from inference/recommendation.

## Constraints
- READ ONLY against GlobalShopCo.
- No production mutation.
- No secrets/credentials.
- No dependency changes, deployments, or external-system changes.
- Do not claim GitHub/workspace access unless observable.
- Do not mark anything VERIFIED; GPTChat Overseer independently verifies the result.

## Acceptance
Return a structured result containing: task_id, status (COMPLETED/PARTIALLY_COMPLETED/BLOCKED), executor, files/paths inspected, work performed, findings, evidence, assumptions/uncertainties, blockers, recommended next task, and checkpoint/resume information.

## Parent evidence
GlobalShopCo Project Overseer TEST-001 completed without human intervention and explicitly recommended this audit as TEST-002.

## Next transition
GPTChat Overseer consumes the Manus result, independently verifies evidence, then either marks TEST-002 VERIFIED, assigns rework, or derives the next milestone task.
