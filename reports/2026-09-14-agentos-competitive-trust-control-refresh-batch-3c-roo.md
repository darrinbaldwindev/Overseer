# AgentOS Competitive Trust/Control Refresh — Batch 3C: Roo Code

**Date:** 2026-09-14 AEST  
**Status:** CURRENT-EVIDENCE REVIEW / PRODUCT INPUT

## Evidence base
Reviewed Roo Code's current public documentation repository and update notes.

Current evidence shows:
- custom modes can carry tailored prompts and tool permissions;
- checkpoints can revert file changes, and newer checkpoint behavior saves before file modification;
- Roo's CLI moved toward automatic approval by default, with `--require-approval` used to opt into manual approval prompts;
- historical/current docs include command permission settings and auto-approval behavior.

## Competitive implication
Roo reinforces the same market direction already visible in Cursor, Claude Code, OpenHands, Raycast and others:

**tool permissions, checkpoints/undo and approval modes are not sufficient differentiation on their own.**

In some surfaces, competitors are moving toward *less friction* by making automatic approval the default and manual approval an explicit opt-in. That raises the importance of AgentOS making governance useful rather than merely adding confirmation dialogs.

## Copy
Useful patterns AgentOS should copy at the product-pattern level:
- clear permission/tool boundaries;
- fast recovery/checkpoint concepts;
- mode-specific capability exposure;
- explicit manual-vs-auto approval posture;
- easy-to-understand rollback affordances where runtime guarantees support them.

## Adapt
AgentOS should adapt these into its stronger governance model:
- tool permissions → Jack authority contract;
- checkpoints → evidence-backed recovery state, not a generic undo promise;
- auto approval → bounded standing authority with explicit scope/expiry/cost/risk where proven;
- custom modes → Simple / Essentials / Tech Head plus task profiles without changing canonical truth.

## Differentiate
AgentOS should differentiate on the integrated lifecycle:

`intent → explicit authority → bounded execution → durable evidence → recovery/replay discipline → Green → independent PRS → understandable result`

Key user-visible differentiation candidates remain:
- exact authority and consequence visibility;
- truth-preserving Stop/Revoke states;
- replay/duplicate protection made understandable;
- evidence timeline tied to canonical mission/result identity;
- provider-neutral governance;
- independent Green then PRS assurance;
- UNKNOWN/failure/recovery states that do not get cosmetically converted into success.

## Do not claim
Do not claim AgentOS is unique because it has:
- tool permissions;
- modes;
- checkpoints;
- approval controls;
- terminal/file access;
- MCP support.

These are increasingly category expectations.

## Current conclusion
Roo closes the remaining Batch-3 competitor UNKNOWN at the level needed for Marketing positioning. Approval/permission/checkpoint UX is now conclusively baseline-class rather than differentiating-class. AgentOS's marketing should continue concentrating on the complete trust contract rather than the existence of controls.
