# AgentOS Authority Source Discovery Follow-up

**Marketing task:** M-A034  
**Date:** 2026-09-15 AEST  
**Status:** COMPLETE / BOUNDED AUTHORITY EVIDENCE / JACK CARD STILL INCOMPLETE

## Current exact evidence
AgentOS PR #104 current exact head observed in this cycle is `bbfee5221652c9bf0551ce5b31eb0b1cf6e78af1`, OPEN / DRAFT / UNMERGED. Exact-head workflow `34857161932` is SUCCESS.

The current tested admission path is materially stronger than the previous Marketing checkpoint. Tests now demonstrate source-backed authority admission with locally bound grant evidence, authenticated actor/issuer/project provenance, capability and project allowlisting, request freshness, duplicate-admission protection, and exact request/delivery/task/mission/wake/authority correlation. Remote callers cannot self-grant authority, consent or autonomy in the tested path.

## Jack permission-card field review
| Field | Current Marketing classification |
|---|---|
| actor/requester | SOURCE-BACKED / TESTED |
| issuer/grant provenance | SOURCE-BACKED / TESTED |
| requested capability | BOUNDED / TESTED |
| granted capability | SOURCE-BACKED / BOUNDED |
| project/scope | BOUNDED / TESTED |
| request freshness/expiry | TESTED |
| purpose/reason | INCOMPLETE |
| grant lifetime/expiry | NOT PROVEN — request freshness is not grant lifetime |
| next approval boundary | INCOMPLETE/PARTIAL |
| already-running-work behavior after authority change | NOT PROVEN |
| durable revoke operation | NOT PROVEN |
| durable revoke receipt | NOT PROVEN |
| reversibility | NOT PROVEN |
| credential consequence | INCOMPLETE |
| data/network egress consequence | INCOMPLETE |
| external communication consequence | INCOMPLETE |
| cost/capacity consequence | PARTIAL — budgets exist, user-facing authority consequence incomplete |
| evidence/correlation pointer | STRONG / TESTED |

## Claim boundary
Marketing may now say, narrowly:

> AgentOS has a tested bounded admission path that derives authority-bearing task fields from source-backed grant evidence and fails closed on actor, issuer, project and policy mismatches.

Marketing must not turn that into:
- `Jack permissions are complete`;
- `permissions can always be revoked`;
- `revoke instantly stops running work`;
- `permission automatically expires`;
- `all credential/network/data consequences are shown`;
- `authority is production-ready`.

## Jack UI promotion state
**BOUNDED / HOLD FOR COMPLETE ACTION CARD.**

A complete interactive Jack permission card still requires canonical evidence for grant lifetime/expiry, durable revoke + receipt, in-flight behavior, reversibility, secret/data-egress/external-action consequences, bounded cost/capacity consequences and the next approval boundary.

## Architectural guard
Frontend and Marketing must not invent missing authority sources. A display control is not a revoke operation, and conversational identity is not authority identity. User interaction continues through the Overseer; Jack's role is presented from canonical authority evidence rather than becoming a second authority system.

**Decision:** source-backed admission is a meaningful current implementation advance. It does not yet justify a complete Jack permission/revoke claim or Founding Beta activation.