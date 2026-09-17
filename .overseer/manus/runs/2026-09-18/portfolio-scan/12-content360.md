# Content360 Fresh Scan

**Scan date:** 2026-09-18 (fresh GitHub read-only scan)  
**Repository:** `darrinbaldwindev/content360`  
**Default branch/head:** `main@80b7ad1f815421157ae98043074c2195ffc23892`  
**Repository URL:** https://github.com/darrinbaldwindev/content360

## Current state

The default branch is `main`; the exact head is verified from the GitHub refs API. The branch is not protected according to the available branch metadata. One open pull request is present: [PR #4](https://github.com/darrinbaldwindev/content360/pull/4), titled “test: harden mock Content360 request integrity,” targeting `main` from `work/c005-request-integrity-batch`, marked **DRAFT**, with current head `d9782da613d407156d5e2a196d5d16f67bfc6fb2`. Three open issues are present: [#1](https://github.com/darrinbaldwindev/content360/issues/1) “Integration readiness: define safe AgentOS/Marketing Overseer boundary before API work”; [#2](https://github.com/darrinbaldwindev/content360/issues/2) “P0 bootstrap — governed AgentOS ↔ Content360 integration contract”; and [#3](https://github.com/darrinbaldwindev/content360/issues/3) “C-005 mock adapter request-integrity batch.”

Recent GitHub Actions evidence includes successful `Test` runs on `main@80b7ad1f815421157ae98043074c2195ffc23892` and predecessor main head `24a33b127fbf3b9e6f183379b5acc9ee36e872e2`. The repository’s recent run history also contains both successful and failed predecessor-branch runs on `work/c005-request-integrity-batch`; predecessor success must not be borrowed as exact-head evidence. Issue #3 contains a later owner/project update claiming exact-head run `34906007364` succeeded for PR head `d9782da...`; this claim is recorded as repository text and was not independently re-run or promoted beyond the current fresh metadata. No live provider/API/auth/publication authority was established.

## Governance and ownership

The controlling batch explicitly says Content360 is downstream of Marketing strategy and that provider-neutral dry-run contracts, validation, idempotency/correlation, freshness/error handling, and evidence capture may be improved without live publish/schedule/network action. The Overseer ledger independently marks `C-C360-01` as **ACTIVE**, owned through `PROJECT-CHAT:Content360 / WORK-PORTFOLIO`, with “Do not compete while ACTIVE; no live PUBLISH/SCHEDULE/network authority.” The owner-start batch repeats the same bounded lane. Marketing is separately marked **ACTIVE**. Therefore there is an active ChatGPT/manual ownership collision for the requested Content360 lane; the open draft PR is the concrete active lineage.

## Findings and classifications

| Finding | Classification |
|---|---|
| `main@80b7ad1f815421157ae98043074c2195ffc23892` is the fresh default-branch head. | **VERIFIED FACT** |
| PR #4 is open, draft, unmerged, and changes the active C-005 request-integrity lineage. | **VERIFIED FACT** |
| Content360 is actively owned in the coordination ledger and owner-start batch; Marketing is also active. | **VERIFIED FACT** |
| Recent historical branch runs include failures and successes; exact-head CI status should be tied only to the exact SHA, not predecessor runs. | **VERIFIED FACT** |
| Issue #3’s statement that run `34906007364` succeeded for `d9782da...` is a repository claim; it is reasonable to treat it as supporting evidence, but not as independent verification of all gates. | **REASONABLE INFERENCE** |
| Official provider/API/auth capability, credentials, publication, scheduling, and network authority are not established by the mock PR or CI metadata. | **UNKNOWN** |
| Any new implementation or documentation slice in the active C-005/Content360 lane would compete with current ChatGPT/manual ownership. | **BLOCKED_STABLE** |

## Safe independent Lite slice

**None identified. `BLOCKED_STABLE`.** The only clearly relevant work is the active C-005 mock request-integrity lineage represented by PR #4 and issue #3, and the coordination records explicitly prohibit competing work while it is active. Do not create a second adapter contract, scheduler, provider authority, publication path, or parallel handoff. Re-scan only after the active lineage materially changes or ownership is explicitly released.

This report was produced read-only; no repository, branch, PR, issue, CI, credential, deployment, merge, approval, rebase, publication, or external communication was modified or performed.
