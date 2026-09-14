# AgentOS Jack Permission Card — Acceptance Matrix

**Date:** 2026-09-15 AEST  
**Role:** Marketing Overseer  
**Canonical mission:** `darrinbaldwindev/Overseer#49`

## Objective

Turn the current authority-evidence gap analysis into explicit UI/product acceptance conditions. The card is presentation over canonical authority evidence only; it must not create a second grant, consent, revoke or policy source.

## Required fields before a permission card may be called complete

| Field | User question answered | Current disposition | Acceptance condition |
|---|---|---|---|
| actor / requester | Who is asking? | PARTIAL | canonical authenticated actor identity |
| issuer / grant provenance | Who granted this authority? | PARTIAL | canonical grant source + evidence ID |
| requested capability | What does it want to do? | AVAILABLE in current admission contract | exact capability list |
| granted capability | What is actually allowed? | AVAILABLE in current admission contract | requested vs granted diff visible |
| target / scope | Where can it act? | PARTIAL | exact host/project/resource scope |
| purpose / reason | Why is it asking? | INCOMPLETE | canonical user-facing reason/objective |
| lifetime / expiry | For how long? | MISSING | canonical start + expiry or one-shot condition |
| next approval boundary | When will it ask again? | MISSING | canonical condition describing next escalation/approval |
| already-running-work behavior | What happens to work already underway if I stop/revoke? | MISSING | canonical runtime semantics, not frontend promise |
| durable revoke operation | Can I remove authority? | MISSING | canonical revoke action exists |
| revoke receipt | How do I know revoke took effect? | MISSING | durable correlated receipt/evidence |
| reversibility | Can the action be undone? | MISSING | canonical reversible/irreversible classification |
| credential consequence | Will it use a secret/account? | MISSING | canonical credential-use disclosure without exposing secret value |
| data / network egress | Will anything leave my computer/account boundary? | MISSING | canonical external destination/data-class disclosure |
| external communication | Will it send/post/message? | MISSING | canonical recipient/channel/action disclosure |
| money / capacity impact | Can it spend money or consume paid quota? | MISSING/PARTIAL | canonical bounded cost/capacity consequence |
| evidence pointer | What proves the authority state? | PARTIAL | canonical authority evidence ID/pointer |

## Allowed interim product language

Until every required field for the relevant action exists, Jack may present a **bounded authority summary**, not a complete permission contract.

Safe examples:
- `Requested: read repository status for this project.`
- `Allowed capabilities: repo.status.`
- `Target: this project.`
- `Permission duration: not available in the current authority record.`

Unsafe examples without canonical support:
- `Allowed until 5 PM`;
- `Revoke anytime`;
- `Revoked`;
- `No further actions authorised`;
- `This cannot affect your accounts`;
- `No data leaves your device`;
- `This action is reversible`;
- `Maximum cost: $0`.

## Negative acceptance tests

The permission card must fail closed if:
1. expiry is synthesized from UI/session lifetime;
2. a frontend button claims durable revoke without a canonical revoke operation;
3. revoke success is shown without a correlated durable receipt;
4. future actions are called unauthorised while already-running work semantics are unknown;
5. secret use or external egress is hidden when canonical evidence says it may occur;
6. cost is displayed as zero merely because exact cost is absent;
7. reversibility is inferred from tool type rather than canonical action semantics;
8. requested capabilities are shown as granted without a canonical grant decision;
9. one action's authority evidence is reused for another task/mission/wake identity.

## Promotion states

- **HOLD:** one or more action-material fields are absent/unknown.
- **BOUNDED:** enough canonical fields exist to explain this exact action, with explicit unknowns.
- **COMPLETE FOR ACTION:** all action-material fields above are canonical, correlated and tested fail-closed.

A complete Jack permission card does not itself imply Green, PRS, execution success or overall AgentOS readiness.
