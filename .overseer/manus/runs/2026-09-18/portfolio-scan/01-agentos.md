# AgentOS fresh governance scan

- **Repository:** [darrinbaldwindev/AgentOS](https://github.com/darrinbaldwindev/AgentOS)
- **Default branch:** `main` (**VERIFIED FACT**)
- **Exact default-branch head:** `962cb3820b83506f9e6d90f50e003690dd85a8a1` (**VERIFIED FACT**, read from GitHub API)
- **Method:** GitHub CLI/API read-only scan. No checkout, code execution, mutation, merge, approval, rebase, deployment, or contact was performed.

## Open work

GitHub reported active open pull requests and open issues during the scan (**VERIFIED FACT**). The observed open PR set included active branches named `agent/overseer/windows-worker-bridge`, `frontend-overseer/vertical-batch-2026-09-14`, and `frontend-overseer/basic-chat-plain-language`; exact PR metadata was queried read-only. The open issue set was non-empty and included issue numbers in the 100-range (exact titles/records were not safely preserved because transient CLI output was contaminated by the sandbox wrapper).

## Recent checks / CI

Recent GitHub Actions runs for workflow **AgentOS Tests** were observed (**VERIFIED FACT**), including successful runs on `work/powershell-receipt-proof` at `a0b13feafdfc85a81ba5656c188118f7cf5effc9`, `frontend-overseer/vertical-batch-2026-09-14` at `8ad509cfb4c898a57ca4b50796cf7be7cff58b00`, `frontend-overseer/basic-chat-plain-language` at `aa274b837f454b8268a5e658f11916a70c66d1f6` and `bc70ab24132b3e6b1fd871c4b141bdc24c6384fa`, and `agent/overseer/windows-worker-bridge` at `f01021301255ebde0f9b3c6baf2b1d55bea05420`. These are branch-run facts, not ownership or release clearance.

## Governance / ownership findings

- **VERIFIED FACT:** active PRs/issues and concurrent governance/Overseer-named branches exist.
- **REASONABLE INFERENCE:** this creates a material collision risk for any new Lite slice, especially in Overseer, frontend, worker, or batch/handoff scope.
- **UNKNOWN:** no authoritative ChatGPT/manual ownership ledger was independently available in the GitHub metadata queried; repository claims were not treated as proof.
- **UNKNOWN:** final recursive default-branch tree retrieval was not safely preserved, so relevant governance/batch/handoff paths cannot be asserted from this scan.
- **BLOCKED_STABLE:** no safe independent Lite slice can be identified without authoritative ownership and scope reconciliation.

## Safe slice

**BLOCKED_STABLE — none identified.**

The report intentionally does not claim that green CI, an open branch, or an issue title establishes authority, ownership, or merge readiness.

## Scan limitation

Some large CLI/API captures were contaminated by the shared sandbox command wrapper during later reads. The exact head and representative CI observations above were independently visible; open-work presence and collision risk are retained conservatively, while unrecoverable exact PR/issue lists and governance paths are marked unknown rather than inferred.
