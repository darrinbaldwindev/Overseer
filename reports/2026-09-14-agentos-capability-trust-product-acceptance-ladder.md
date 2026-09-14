# AgentOS Capability Trust — Product Acceptance Ladder

Date: 2026-09-14 Brisbane
Owner: Marketing Overseer
Status: PRODUCT/CLAIM CONTRACT / NOT IMPLEMENTATION PROOF

## Purpose
Turn current competitive supply-chain research into implementation acceptance gates without creating a second capability registry, authority system or evidence store.

## Acceptance ladder

### Gate C1 — Identity
A capability must expose a canonical name, origin/publisher identity, version and installation/source reference. UNKNOWN origin fails closed to untrusted/attention state.

### Gate C2 — Permission diff
Before first use or material update, the product must be able to show the exact requested capability scope and highlight newly added privileges. No generic `Allow` copy if the actual requested scope is unavailable.

### Gate C3 — Secret and data boundary
The user-facing contract must disclose whether secrets, local files, clipboard, external communication or customer data may be touched. Do not claim that secrets are invisible to models/tools unless exact architecture proves it.

### Gate C4 — Egress / external action
Capabilities that can call networks, send messages, publish, purchase or mutate external systems require an explicit canonical risk/action boundary. Product wording must distinguish read-only from external mutation.

### Gate C5 — Update and rollback
Version changes must be attributable. If rollback/disable exists, surface actual canonical state. Do not imply a safe rollback where only UI uninstall/disable exists.

### Gate C6 — Evidence
Execution should point to canonical task/mission/capability/version and result evidence. A frontend activity entry is not sufficient proof by itself.

### Gate C7 — Assurance
Green and PRS/Henry remain separate layers. Neither publisher verification nor installation provenance can substitute for execution verification/assurance.

## Product hierarchy
Safe future wording if implemented and evidenced:
`Known capability → known permissions → bounded authority → execution evidence → recovery/rollback evidence → Green → PRS`.

Unsafe shortcuts:
- `Verified plugin = safe`;
- `MCP compatible = trusted`;
- `Installed from marketplace = approved for all jobs`;
- `User clicked Allow once = permanently authorised`;
- `Update available = safe to auto-upgrade`.

## Competitive interpretation
Verified-extension programmes, granular tool approval, checkpoints and MCP configuration are increasingly baseline. AgentOS's product opportunity is to connect capability identity/version/origin to the same canonical authority, evidence, recovery and assurance lifecycle used by governed execution.

## Marketing gate
No public differentiation claim should move from PRODUCT DIRECTION to PROVEN until the exact repository/runtime implementation demonstrates the relevant gate and current-head tests/evidence support it.