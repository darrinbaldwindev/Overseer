# Two-Tier AI Architecture

## Canonical Model

The portfolio uses two distinct supervisory roles.

```text
                         OWNER
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       MANUS OVERSEER            AGENTOS OVERSEER
       Portfolio AI                Project AI
              │                         │
       all projects                 AgentOS
              │                         │
       project-level             AgentOS agents,
       overseers/agents           services and state
```

## AgentOS Overseer

AgentOS Overseer is the **primary AI agent inside the AgentOS project**.

Its responsibility is deep project-level operation and development, including:

- AgentOS architecture and runtime;
- AgentOS agents and their coordination;
- AgentOS state, memory and continuity;
- AgentOS tools and integrations;
- correctness, reliability and security of AgentOS;
- project-level autonomous operation;
- project-specific development and recovery.

AgentOS Overseer should be capable of operating as the primary intelligence of AgentOS without requiring Manus Overseer to be continuously active.

## Manus Overseer

Manus Overseer is the owner's **personal portfolio-level Overseer** running with the Manus Desktop environment.

Its responsibility is breadth across the owner's projects, including:

- repository and project inventory;
- cross-project health;
- dependencies and architectural relationships;
- duplicated capabilities;
- project-level progress and regressions;
- strategic priorities;
- portfolio recommendations;
- communication with project-level agents/overseers.

Manus Overseer should not replace the project-level intelligence of AgentOS Overseer.

## Depth vs Breadth

AgentOS Overseer optimizes for **depth**. Manus Overseer optimizes for **breadth**.

Similarity of responsibility does not imply identical scope.

## Communication

The two Overseers may exchange evidence, findings, capabilities and recommendations.

Examples:

- AgentOS Overseer may publish a reusable capability that Manus Overseer can identify as useful to another project.
- Manus Overseer may identify portfolio-level duplication or a cross-project dependency and recommend that AgentOS Overseer evaluate it.

Manus Overseer does not silently assume authority over AgentOS implementation.

AgentOS Overseer does not silently assume authority over unrelated projects.

## Authority

The owner remains the final authority.

Changing either Overseer's authority boundary requires an explicit policy change outside autonomous reasoning.

## Design Rule

Capabilities built for AgentOS Overseer should be designed for reuse by Manus Overseer where that reuse is beneficial, but AgentOS implementation should not be weakened or redirected merely to satisfy portfolio-level symmetry.
