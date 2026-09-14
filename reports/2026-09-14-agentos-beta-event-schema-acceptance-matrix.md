# AgentOS Founding Beta — Event Schema Acceptance Matrix

**Date:** 2026-09-14 Brisbane
**Owner:** Marketing Overseer
**Status:** PREPARED / TELEMETRY NOT ACTIVATED / BETA HOLD

## Purpose
Translate the existing Founding Beta measurement contract into an implementation-ready, privacy-minimal acceptance matrix that reuses AgentOS's canonical telemetry/privacy boundary. This document does **not** create a second analytics authority and does not enable transmission.

## Existing canonical telemetry boundary
Current AgentOS evidence shows:
- telemetry defaults to `none` / disabled;
- explicit levels are `none`, `performance`, `improvement`;
- transmission is consent-gated;
- the existing sanitiser emits a fixed performance-oriented allowlist;
- existing tests explicitly exclude arbitrary `prompt` and `conversation` content.

Any Founding Beta extension must preserve these properties and observe canonical runtime/frontend state rather than inventing parallel truth.

## Acceptance rules
A beta event is admissible only when all are true:
1. exact canonical source state is named;
2. event can be represented without raw prompt, conversation, file, clipboard, secret, credential, unrestricted stdout/stderr or arbitrary metadata;
3. consent level is explicit;
4. user-facing consent language is available before transmission;
5. local-only collection remains possible where product/privacy policy requires it;
6. retention/deletion treatment is defined before activation;
7. negative tests prove forbidden content is dropped rather than merely hidden;
8. telemetry cannot promote runtime, Green, PRS or completion state;
9. event absence is never interpreted as task failure or user disengagement without corroborating evidence.

## Proposed event matrix

| Event | Product question | Canonical source required | Minimal fields | Consent | Privacy class | Current disposition |
|---|---|---|---|---|---|---|
| `beta.real_job_attempted` | Did tester try a real job? | canonical mission/task creation receipt | pseudonymous session/tester cohort, task category, timestamp bucket, source surface | improvement | low if content-blind | PREPARED / source binding required |
| `beta.permission_prompt_viewed` | Was authority shown? | canonical authority-request projection + frontend render receipt | permission class, scope class, risk tier, timestamp bucket | improvement | low | HOLD until canonical user-facing permission projection exists |
| `beta.permission_comprehension_recorded` | Did tester understand scope? | explicit tester response, not inferred behavior | question id, response code, attempt number | improvement | moderate research data | PREPARED / consent+retention required |
| `beta.stop_requested` | Did tester attempt Stop? | canonical control request receipt | mission/task correlation, control=`stop`, timestamp bucket | improvement | low | PREPARED if canonical receipt exists |
| `beta.stop_effect_observed` | What actually happened after Stop? | canonical runtime control/result projection | effect class only: new-work-blocked / in-flight-finished / termination-confirmed / unknown | improvement | low | HOLD until canonical projection exists |
| `beta.revoke_requested` | Did tester attempt Revoke? | canonical authority-revoke operation | authority id class, timestamp bucket | improvement | low | BLOCKED — no durable canonical Revoke surfaced in current Basic Chat |
| `beta.evidence_summary_viewed` | Did tester inspect evidence? | frontend interaction with canonical evidence projection | evidence surface id, state class, timestamp bucket | improvement | low | HOLD until generic canonical Evidence Timeline projection exists |
| `beta.evidence_comprehension_recorded` | Could tester tell what happened? | explicit tester response | question id, response code | improvement | moderate research data | PREPARED / consent+retention required |
| `beta.recovery_observed` | Was interrupted work recovered safely? | canonical recovery event chain | recovery class, final state class, replay class | improvement | low | HOLD on exact runtime projection |
| `beta.duplicate_prevented_or_replayed` | Was replay/duplicate behavior safe? | canonical idempotency/replay receipt | duplicate class, disposition class | improvement | low | HOLD on exact runtime projection |
| `beta.second_real_job_attempted` | Did tester voluntarily return? | second independent canonical mission/task creation | pseudonymous cohort id, elapsed-time bucket, task category | improvement | low | PREPARED / source binding required |
| `beta.session_incident_severity` | Was there an S0–S4 incident? | facilitator/reviewer classification linked to evidence packet | severity code, evidence pointer id only | improvement | moderate | PREPARED / manual review + retention required |

## Explicitly forbidden fields
Never transmit through these beta events:
- raw user prompt or chat transcript;
- file names or contents unless separately authorised for a narrowly defined research study;
- clipboard contents;
- credentials, API keys, tokens or secret values;
- unrestricted command lines or stdout/stderr;
- full filesystem paths;
- arbitrary model-generated text;
- customer/user third-party personal data;
- hidden inference of comprehension from clicks alone.

## Negative-test contract
Before activation, add deterministic tests proving:
1. telemetry is disabled by default;
2. `none` transmits nothing;
3. performance consent does not transmit improvement/beta-research events;
4. prompt/conversation/file/secret/arbitrary fields are stripped;
5. unknown event fields fail closed or are dropped through an explicit allowlist;
6. canonical state labels cannot be overwritten by telemetry payloads;
7. absence/failure of telemetry cannot alter runtime execution;
8. Revoke events cannot exist until a real canonical revoke source exists;
9. Stop telemetry distinguishes request from confirmed effect;
10. deletion/retention policy can locate beta research records without conversation content.

## Frontend consent requirements
The Frontend Overseer should eventually present plain-language consent that distinguishes:
- performance telemetry;
- optional Founding Beta product-research measurement;
- what is **not** collected;
- whether data leaves the device;
- retention/deletion treatment;
- how consent can be changed later.

Do not use broad wording such as `Help improve AgentOS by sharing usage data` without showing the meaningful categories.

## Activation gate
**NO BETA EVENT TRANSMISSION** until:
- Founding Beta technical entry gate clears;
- product/privacy owner approves the schema and retention/deletion treatment;
- canonical source bindings exist for each activated event;
- Frontend consent surface is implemented and tested;
- negative tests pass exact head;
- activation is independently reviewed.

## Marketing interpretation
This matrix makes measurement implementation-ready without turning telemetry into proof. Beta success remains evidence from real governed jobs plus explicit user research, not an analytics dashboard claim.