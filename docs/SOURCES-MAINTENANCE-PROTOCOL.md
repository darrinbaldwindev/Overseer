# ChatGPT Sources Maintenance Protocol

## Objective

Keep the ChatGPT Project Sources layer useful, current, compact, and aligned with the GitHub Overseer control plane without turning Sources into a duplicate of the operational logs.

## What belongs in Sources

- Stable mission and scope.
- Agent roles and authority boundaries.
- Stable governance and safety principles.
- Portfolio/project registry when it is intended as durable reference.
- Durable architectural decisions.
- Stable terminology and evidence standards.
- High-value reusable operating principles.

## What does not normally belong in Sources

- Daily scan logs.
- Transient GitHub issues.
- Commit-by-commit history.
- Temporary debugging notes.
- Unverified findings.
- Secrets or credentials.
- Information that changes too frequently to maintain reliably.

## Review triggers

Review the Sources layer when:

1. A governing policy changes.
2. Agent responsibilities change.
3. The portfolio architecture changes materially.
4. A repeated contradiction is found between Sources and GitHub.
5. A better continuity or knowledge-management mechanism is identified.
6. A durable project decision is made in conversation.
7. The Overseer itself gains a material new capability.

## Conflict rule

If Sources and GitHub disagree:

- Do not silently merge the two versions.
- Determine which is intended to be authoritative for the specific fact.
- Treat GitHub as authoritative for current implementation/state.
- Treat Sources as authoritative for stable ChatGPT project guidance unless a newer approved decision supersedes it.
- Record material contradictions for resolution.

## Continuous improvement

During normal supervision, evaluate whether the Sources/GitHub/conversation separation is still the best architecture. Prefer improvements that increase reliability and reduce duplicated maintenance without unnecessarily expanding autonomous authority.

## Update discipline

A Source update should be deliberate and relatively infrequent. Every Source document should have a clear purpose and should avoid duplicating operational state that already has a better home in GitHub.
