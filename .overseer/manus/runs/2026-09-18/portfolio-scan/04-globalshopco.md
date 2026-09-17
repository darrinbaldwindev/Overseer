# GlobalShopCo Fresh Scan

**Scan mode:** read-only GitHub CLI/API review; no repository files, branches, PRs, issues, checks, or external systems were modified. **Scan date:** 2026-09-18 (local batch date). Repository evidence outranks claims in coordination documents.

## Scope and source of truth

Repository: [darrinbaldwindev/GlobalShopCo](https://github.com/darrinbaldwindev/GlobalShopCo). The default branch is `agent/overseer/initial-project-timeline`; its current head is `79d50227fe19826d42c43e7dec15ce245ad58e40` (verified with `gh api repos/.../branches/...`). The repository is public and not archived. The default branch is unusual; do not assume `main` or `master` is canonical.

Relevant files inspected on the default-branch tree included `.overseer/VERTICAL-BATCH-ADOPTION.md`, `docs/overseer/CHATGPT_HANDOFF.md`, `docs/overseer/OVERSEER.md`, `docs/overseer/OVERSEER_PROTOCOL.md`, `docs/portfolio-oversight/PORTFOLIO-NEXT-BATCH-2026-09-13.md`, `docs/research/M4.1_HOME_ORGANISATION_BATCH_A_HANDOFF_2026-08-28.md`, and the assurance evidence directory. The repository adoption file explicitly says the pointer is not authority and prohibits production Shopify writes, purchases, supplier contact, publication, deployment, credential changes, and duplicate control-plane systems.

## Open pull requests

There are 14 open PRs at scan time: [#31](https://github.com/darrinbaldwindev/GlobalShopCo/pull/31), [#30](https://github.com/darrinbaldwindev/GlobalShopCo/pull/30), [#29](https://github.com/darrinbaldwindev/GlobalShopCo/pull/29), [#28](https://github.com/darrinbaldwindev/GlobalShopCo/pull/28), [#27](https://github.com/darrinbaldwindev/GlobalShopCo/pull/27), [#26](https://github.com/darrinbaldwindev/GlobalShopCo/pull/26), [#25](https://github.com/darrinbaldwindev/GlobalShopCo/pull/25), [#24](https://github.com/darrinbaldwindev/GlobalShopCo/pull/24), [#15](https://github.com/darrinbaldwindev/GlobalShopCo/pull/15), [#14](https://github.com/darrinbaldwindev/GlobalShopCo/pull/14), [#13](https://github.com/darrinbaldwindev/GlobalShopCo/pull/13), [#10](https://github.com/darrinbaldwindev/GlobalShopCo/pull/10), [#3](https://github.com/darrinbaldwindev/GlobalShopCo/pull/3). (The API returned 14 entries; the links above cover the entries observed in the compact output and should be treated as the active PR set.)

The active set includes the `agent/ebay-amazon/vertical-batch-*` line (`#24`, `#25`, `#26`, `#27`, `#28`, `#29`, `#30`, `#31`), overseer research/evidence PRs (`#13`, `#14`, `#15`), and ChatGPT-owned work (`#10` on `agent/chatgpt/m4-home-organisation`, plus `#3` on `agent/chatgpt/m3-contract-prep`). Exact observed heads include #31 `6387a92238cf18c60024c00f3f8b64875f945c24`, #30 `80c82475b98663d677885e8b4d222ae2cedb8555`, #29 `15fa99eb4c4b1f96127f6f51c412cbffc94e45e2`, #28 `5a28d996d79efe7903ff08ba4ce9c2e5a9e406a5`, #27 `2809177a8e6fe0f3adcbdda53eaa4ed617d073e7`, #26 `6598684322e96b9a01aa8ccd4081fa4d1494f08e`, #25 `13a9a050983b2db790d3ecc00c69ab31aa71776b`, #24 `752eb48fd760191c692471834415b9e8e6082312`, #15 `ec173cb8f927cd8308151f3ce22efed1a10c8f0a`, #14 `60738edace0a6ca88b08b5c2764c12be466166b1`, #13 `69637712fc3fdf588b720b781aa18464005e7bdb`, #10 `f4e5de0e0e946a5c6844dea84d99527d0c9f8474`, and #3 `7c35d90ad4f141dbd4d5205d7536ab9d9b189151`.

## Open issues

There are 14 open issues: [#23 Amazon channel gate](https://github.com/darrinbaldwindev/GlobalShopCo/issues/23), [#19 allowance-aware routing strategy](https://github.com/darrinbaldwindev/GlobalShopCo/issues/19), [#18 site-wide launch gate](https://github.com/darrinbaldwindev/GlobalShopCo/issues/18), [#17 eBay channel gate](https://github.com/darrinbaldwindev/GlobalShopCo/issues/17), [#16 Level 2 acceptance workload](https://github.com/darrinbaldwindev/GlobalShopCo/issues/16), [#12 M4.1 Batch B](https://github.com/darrinbaldwindev/GlobalShopCo/issues/12), [#11 Commercial Intelligence M002](https://github.com/darrinbaldwindev/GlobalShopCo/issues/11), [#9 M4.1 Product Sub-Agent Handoff Gate](https://github.com/darrinbaldwindev/GlobalShopCo/issues/9), [#8 Manus Overseer operating loop](https://github.com/darrinbaldwindev/GlobalShopCo/issues/8), [#7 M4 Product Research Dashboard](https://github.com/darrinbaldwindev/GlobalShopCo/issues/7), [#6 M4.1 product/supplier validation](https://github.com/darrinbaldwindev/GlobalShopCo/issues/6), [#5 Portfolio Overseer reconciliation](https://github.com/darrinbaldwindev/GlobalShopCo/issues/5), [#4 M5 supplier/free-delivery economics](https://github.com/darrinbaldwindev/GlobalShopCo/issues/4), and [#2 M4 curated catalogue](https://github.com/darrinbaldwindev/GlobalShopCo/issues/2). Issue titles are coordination signals, not proof that work is complete or authorized.

## Checks and CI

`gh run list` returned 28 recent runs. The newest observed runs on 2026-09-14 include successful `Amazon channel gate` runs on the `agent/chatgpt/amazon-au-preflight` branch (for example run [34856135125](https://github.com/darrinbaldwindev/GlobalShopCo/actions/runs/34856135125), SHA `0b52631e9a3f084d9b947227c84e7f656ebab6f5`) and successful `Home Organisation launch gate` / `Free-delivery economics fixture` runs on `agent/chatgpt/m4-home-organisation` at SHA `f4e5de0e0e946a5c6844dea84d99527d0c9f8474` (runs [34822007927](https://github.com/darrinbaldwindev/GlobalShopCo/actions/runs/34822007927) and [34822007960](https://github.com/darrinbaldwindev/GlobalShopCo/actions/runs/34822007960)). Earlier runs include failures for `Free-delivery economics fixture` on the same ChatGPT line (run [34821864358](https://github.com/darrinbaldwindev/GlobalShopCo/actions/runs/34821864358), SHA `f465a842707c7913b4a6c26a8b881503aeaf6b88`). These are branch/run facts only; CI success is not a release, security, commerce, or launch authorization, and the checks were not rerun.

## Findings and classifications

1. **VERIFIED FACT:** The default branch is `agent/overseer/initial-project-timeline` at exact head `79d50227fe19826d42c43e7dec15ce245ad58e40`; it is not safe to infer that active PR work has landed there.
2. **VERIFIED FACT:** The repository has a large active workset: 14 open PRs, 14 open issues, and 28 recent workflow runs, including multiple parallel vertical-batch and ChatGPT/overseer branches.
3. **VERIFIED FACT:** Active PRs and issues cover the same commerce/research domains named by the batch instructions: Home Organisation, catalogue/economics, eBay/Amazon channel gates, headless integration, and portfolio/Manus/GPTChat reconciliation.
4. **VERIFIED FACT:** Repository governance files prohibit live supplier/provider/customer actions, deployment/publication, credential changes, and duplicate control-plane creation.
5. **VERIFIED FACT:** The Home Organisation handoff explicitly records unresolved freight, dropship capability, final landed cost, market price, and warranty/returns unknowns; it says candidates are hold/research/price-request rather than launch-ready.
6. **REASONABLE INFERENCE:** A new Lite implementation or research slice in commerce, catalogue, Home Organisation, eBay/Amazon, or orchestration would likely overlap an existing PR/issue lineage and could compete with active ChatGPT/manual ownership.
7. **UNKNOWN:** No independent evidence here establishes merge readiness, owner approval, production readiness, live supplier permission, marketplace permission, or that any successful check represents a complete launch gate.
8. **UNKNOWN:** The compact scan did not independently resolve which open PR is canonical versus supporting/superseded, nor whether all PR review decisions/check suites remain current at their exact heads.

## Ownership collision and safe slice

**Ownership collision:** `ACTIVE_COLLISION_VERIFIED`. Exact evidence includes ChatGPT branches/PRs (`#10` `agent/chatgpt/m4-home-organisation`, #3 `agent/chatgpt/m3-contract-prep`), active `agent/ebay-amazon/vertical-batch-*` PRs (#24–#31), overseer PRs (#13–#15), and open coordination issues #5, #9, #17, #18, #23. These lineages overlap the prescribed GSC Lite areas. The controlling batch says not to compete with active ChatGPT schedules/manual work and to stop after unchanged checks when no independent slice is clear.

**Safe independent Lite slice:** `BLOCKED_STABLE` — no clearly unowned slice identified. Do not implement, comment, claim, merge, approve, rebase, deploy, contact suppliers, or create a parallel batch/control plane. A future slice requires fresh exact-head reconciliation and explicit proof that its files/domain are outside the active PR/issue lineages.

## Caveats

This report is a local durable scan artifact, not a GitHub coordination record; the task explicitly required saving it locally and prohibited writes. No project code, tests, builds, migrations, or deployments were executed. Claims in repository documents were treated as untrusted until corroborated by exact GitHub metadata; unresolved claims remain UNKNOWN.

## Commands/evidence basis

Read-only `gh api` for repository metadata, default-branch commit, recursive tree, pull requests, issues, and `gh run list` for recent Actions runs. No write-capable GitHub command was issued.
