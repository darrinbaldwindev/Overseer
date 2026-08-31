# Overseer Transaction Ledger

Status: DESIGN + INITIAL INTAKE CONTRACT

## Purpose

Provide a durable, provider-neutral record for every delegated worker transaction so scheduler activity, receipt, execution, evidence, and verification cannot be conflated.

## Lifecycle

`CREATED → DISPATCHED → RECEIVED → ACKNOWLEDGED → EXECUTING → COMPLETED|FAILED|BLOCKED → EVIDENCED → VERIFIED`

A transaction may also enter `MISSED` when an expected acknowledgement or result window expires without evidence. `VERIFIED` is terminal success only after independent verification evidence exists.

## Required identity

Each transaction must record where applicable:

- transaction/task ID;
- assigning Overseer;
- worker/provider;
- project/repository;
- canonical branch;
- base commit;
- creation/dispatch/acknowledgement/execution/completion timestamps;
- requested capabilities;
- authority/policy context;
- result commit;
- evidence references;
- verifier and verification evidence;
- final state;
- failure/blocker reason;
- checkpoint/resume information.

## State rules

- `SCHEDULED` or a heartbeat event is scheduler evidence only; it is not a worker transaction success.
- `RECEIVED` requires evidence that the assigned transaction reached its intended worker intake path.
- `ACKNOWLEDGED` requires a worker-specific acknowledgement tied to the transaction ID.
- `EXECUTING` requires evidence that the worker started the assigned action.
- `COMPLETED` requires result evidence; code tasks should include the result commit where applicable.
- `EVIDENCED` requires persisted, auditable evidence sufficient for independent review.
- `VERIFIED` requires an independent verification step against current canonical state.
- Missing acknowledgement/result must remain `MISSED` or `BLOCKED`, not `COMPLETED`.

## Idempotency

A transaction ID is unique. Retries must reference the original transaction or an explicitly linked retry transaction. Duplicate scheduler delivery must not inflate successful transaction counts.

## Fresh-state requirement

The transaction's base commit must be recorded before execution. If canonical repository state changes before completion/verification, the Overseer must re-evaluate validity against a fresh snapshot before accepting the result.

## Hourly reporting

Reports should calculate independently:

- successful verified transactions;
- completed but unverified transactions;
- failed transactions;
- blocked transactions;
- missed/no-acknowledgement transactions;
- scheduler/receiver events that are not worker transactions.

No category may silently absorb another.

## Provider neutrality

The ledger records worker/provider identity and capability evidence but does not depend on Manus, Gemini, ChatGPT/Codex, or any provider-specific plugin model.

## Security

Do not store credentials, access tokens, secrets, or sensitive authentication material in this ledger. Record references to secure mechanisms rather than secret values.

## Acceptance target

A complete end-to-end test must demonstrate one transaction moving from creation through worker acknowledgement, execution, result/evidence persistence, and independent verification, with every transition auditable by transaction ID.
