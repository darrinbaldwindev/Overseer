# Windows / PowerShell Overseer Priority

Date: 2026-09-11
Owner direction: Treat the always-on Windows laptop as a first-class AgentOS worker. Governed PowerShell autonomy is the immediate Windows-control priority because it can help build, test and maintain AgentOS itself.

## Shared architectural boundary

All work must extend existing AgentOS scheduler, worker, authority, budget, persistence, remote-bridge, Green and PRS systems. Do not create a duplicate scheduler, queue, worker runtime, shell authority, registry, memory system, governance engine, or audit source of truth.

Target execution chain:

`Overseer -> AgentOS task -> Windows laptop worker -> governed PowerShell/process execution -> durable stdout/stderr/exit-code receipt -> verification -> Green/PRS -> Overseer reconciliation`

Current bounded implementation direction:
- Level-1 PowerShell only at first.
- Non-elevated and non-interactive.
- Approved project roots only.
- Fixed operation catalogue before arbitrary command execution.
- Time/output bounded.
- Authority/consent/capability/policy/risk/budget/approval before execution.
- Durable execution receipt and verification after execution.
- Green/PRS required before final completion.
- No unrestricted administrator PowerShell.
- No production autonomy, credentials, deployment, merge, approval, ready transition or rebase from these missions.

## CLAUDE OVERSEER — WINDOWS/POWERSHELL MISSION C-001

Role: implementation-design and adversarial code review worker Overseer.

Mission:
1. Review the AgentOS Windows PowerShell adapter, governed-execution boundary and the remote-bridge/Green/ledger lineage.
2. Identify concrete implementation defects, unsafe command-surface assumptions, Windows quoting/encoding/timeout/process-tree problems, working-directory escape risks, output truncation risks, child-process cleanup problems, and privilege-boundary mistakes.
3. Propose the smallest implementation-ready fixes that preserve the existing architecture.
4. Pay special attention to how the PowerShell adapter should be wired into the existing worker registry and remote pickup path without bypassing Green/PRS or creating another runtime.
5. Define the safest path from the fixed Level-1 operation catalogue toward later governed write operations.

Required output:
- Evidence reviewed, including exact AgentOS commit/PR heads.
- VERIFIED findings vs hypotheses.
- Concrete code-level recommendations.
- Failure-injection cases.
- Explicit blockers and next mission.

## GEMINI OVERSEER — WINDOWS/POWERSHELL MISSION G-001

Role: architecture, ecosystem and Windows-platform research worker Overseer.

Mission:
1. Independently review current official Windows/PowerShell automation mechanisms relevant to AgentOS: Windows PowerShell/PowerShell 7, process execution, Task Scheduler/service constraints, Windows UI Automation/WinApp tooling, session/lock boundaries, UAC/elevation, Constrained Language/JEA/AppLocker/WDAC where relevant, and secure unattended-worker patterns.
2. Recommend which mechanisms belong in AgentOS V1/V2.3 and which should remain optional/later.
3. Compare using the user's existing always-on Windows laptop directly versus paid external Windows-control products/cloud PCs.
4. Define capability boundaries for `shell.powershell.repo.read`, `shell.powershell.dev.execute`, `shell.powershell.system.read` and future write/elevated capabilities.
5. Identify licensing, deployment, security, reliability and Windows-version constraints that could affect shipping AgentOS commercially.

Required output:
- Current official-source evidence with dates/links where available.
- Architecture recommendations mapped to existing AgentOS adapter families.
- Risks, unknowns, commercial implications and acceptance tests.
- Do not treat product marketing claims as implementation proof.

## GROK OVERSEER — WINDOWS/POWERSHELL MISSION X-001

Role: independent adversarial intelligence/review worker Overseer.

Mission:
1. Challenge the entire Windows-worker design for false-GREEN conditions.
2. Threat-model autonomous PowerShell on the always-on laptop: command injection, path/symlink/junction escape, environment poisoning, inherited credentials, subprocess escape, encoded commands, profile loading, registry/service/system changes, persistence abuse, stale task replay, duplicate execution, malicious repository content, output spoofing, and privilege escalation.
3. Attack the remote task -> claim -> worker -> PowerShell -> receipt -> Green/PRS chain for correlation failures and replay/recovery bugs.
4. Produce a failure-injection matrix for both Level-1 read/dev operations and later write/elevated stages.
5. State what evidence would be required before calling bounded PowerShell autonomy GREEN on a real physical Windows laptop.

Required output:
- GROK OVERSEER REPORT format.
- Exact evidence reviewed.
- Verified state, adversarial findings, severity, recommendations and explicit withheld claims.
- No merges, approvals, deployments, credential changes or production autonomy.

## Hourly coordination rule

On each hourly Overseer coordination cycle:
1. Fresh-scan AgentOS and relevant assurance/coordination repositories before assigning or accepting work.
2. Treat Windows/PowerShell laptop-worker readiness as a current AgentOS priority until superseded by owner direction or objectively blocked.
3. Check for new Claude/Gemini/Grok Windows/PowerShell findings and reconcile them against exact repository heads.
4. Assign the next bounded mission to whichever Overseer has the best-fit unresolved question; avoid duplicated research.
5. Convert verified findings into implementation-ready AgentOS/PRS work where safe.
6. Preserve physical-Windows acceptance as a separate evidence gate; never infer hardware success from CI.
7. Record evidence, blockers and next actions durably.

## Current priority state

Priority: P0 / active.
Objective: make the always-on Windows laptop a governed AgentOS worker, beginning with bounded PowerShell autonomy that can run repository inspection, tests, audits and safe development diagnostics.
Overall status: AMBER until the PowerShell slice is reconciled onto the stronger bridge/Green/ledger lineage and passes physical Windows acceptance plus independent assurance.
