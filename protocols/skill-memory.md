# Overseer Reusable Skill Memory

## Purpose

Overseer must retain validated ways of doing work, not only observations about repositories. A **skill** is a reusable procedure that can be selected for a future task when its trigger, prerequisites, scope and validation criteria match.

Skill memory is distinct from findings, decisions and repository history:

- **Finding** = something observed about a project.
- **Decision** = what Overseer or the owner decided to do.
- **Skill** = how to perform a repeatable task effectively.
- **Memory** = the persistent record that makes the skill available across sessions.

## Skill record

Every reusable skill should contain:

- stable `skill_id`;
- canonical name and short description;
- trigger conditions and applicable task types;
- prerequisites and required capabilities;
- ordered procedure steps;
- expected inputs and outputs;
- validation checks and success criteria;
- safety constraints and forbidden actions;
- scope (`portfolio`, `repository`, `component`, or `task`);
- provenance: where and when the skill was learned;
- evidence references supporting the skill;
- confidence;
- version;
- usage count and successful-use count;
- last-used timestamp;
- status (`candidate`, `validated`, `deprecated`, `blocked`).

## Learning policy

Overseer must not convert every successful action into a skill. A procedure becomes a **candidate** when it appears repeatable and has evidence of useful execution. It becomes **validated** only after the validation criteria have been satisfied and the procedure has sufficient supporting evidence.

A skill should normally be promoted when:

1. the procedure has produced the intended result;
2. its preconditions are understood;
3. its steps can be expressed independently of the original session;
4. safety boundaries are explicit;
5. evidence is retained so the skill can be audited or revised.

## Retrieval policy

Before inventing a procedure, Overseer should search reusable skill memory. Candidate skills may be reused when their scope and prerequisites match, but must remain clearly marked as unvalidated. Validated skills are preferred over candidates when otherwise equivalent.

Skill selection should consider, in order:

1. exact task/trigger match;
2. scope compatibility;
3. prerequisite satisfaction;
4. validation status;
5. confidence;
6. historical success rate;
7. recency and version compatibility.

## Safety and isolation

A remembered skill never grants authority that the active policy does not grant. Skills describe procedure; policy controls permission.

A skill must never silently inherit credentials, secrets, production authority, or mutation rights from the session in which it was learned.

Skills must be versioned and invalidated or revalidated when their dependencies, interfaces, policies, or assumptions materially change.

## Feedback loop

Each reuse records an outcome. Repeated success increases confidence; failure creates a review signal and may downgrade or block the skill. Overseer should prefer improving an existing skill over creating near-duplicate skills.

## Cross-repository reuse

Skills should be portable where their procedure is genuinely general. Repository-specific assumptions belong in the skill's scope or prerequisites rather than being silently generalized.

## Success condition

Overseer should eventually be able to answer:

> "Have I solved this kind of problem before, and what validated procedure should I reuse?"

with an evidence-backed skill rather than relying only on conversational recall.
