# Portfolio Intelligence Protocol

## Objective

Move beyond isolated repository reviews and identify patterns across the entire project portfolio.

## Analysis Passes

### 1. Dependency Patterns

Identify shared dependencies, incompatible versions, repeated vulnerabilities and unnecessary duplication.

### 2. Component Reuse

Identify components or capabilities that appear independently in multiple repositories and may be candidates for shared implementation.

Do not recommend consolidation solely because names are similar.

### 3. Architecture

Identify common services, APIs, databases, infrastructure and architectural patterns.

Flag conflicting decisions when they create operational or maintenance risk.

### 4. Project Lifecycle

Identify projects that appear:

- active;
- stalled;
- abandoned;
- superseded;
- experimental;
- production-oriented;
- foundational/infrastructure.

Lifecycle classifications are hypotheses unless supported by evidence such as commit activity, deployment configuration, documentation or explicit project metadata.

### 5. Systemic Findings

If substantially similar findings appear across multiple repositories, create a portfolio-level observation rather than treating every occurrence as unrelated.

Example:

```text
PORTFOLIO-SECURITY-001
Repeated secret-management weakness across 3 repositories.
```

Repository-specific findings remain linked to the systemic observation.

### 6. Opportunity Detection

Overseer may identify:

- reusable internal tooling;
- shared CI templates;
- common automation;
- duplicated business logic;
- opportunities to standardize conventions;
- candidate projects for consolidation.

These are recommendations unless proven otherwise.

## Confidence

Every relationship or systemic conclusion receives a confidence level.

Low-confidence opportunities are presented as candidates for investigation, not decisions.

## Owner Decision Boundary

Portfolio intelligence can recommend consolidation, reuse or retirement. It does not autonomously delete, merge or retire projects under the default policy.
