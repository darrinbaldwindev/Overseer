# AgentOS UI Mode Specification

## Status
Marketing/product UX specification. Production implementation remains evidence-gated.

## Principle
AgentOS has one capability and governance model presented through three density modes. UI mode changes visibility and interaction complexity; it never changes authority, permissions, assurance requirements, routing policy, or security controls.

## SIMPLE
Audience: new users, casual users, personal users, accessibility-first users.

- Large, obvious buttons.
- Minimal navigation.
- Large first-class AgentOS chat window.
- Primary actions: Ask AgentOS, New Mission, Tasks, AI Team.
- Minimal status information: current mission and system health.
- Technical telemetry hidden by default.
- Plain-language labels and progressive disclosure.
- Mobile-friendly as a first-class requirement.

## ESSENTIALS
Audience: normal daily users.

- Focused dashboard with only high-value widgets.
- Large central chat remains a primary interaction surface.
- Current mission and progress.
- AI Team status.
- Recent activity.
- Essential system status.
- Quick actions.
- No unnecessary telemetry or configuration noise.

## TECH HEAD
Audience: developers, operators, administrators, power users.

- All available widgets can be surfaced.
- Configurable dense panels.
- Full model/provider routing visibility.
- Mission/task telemetry.
- Security, quality, cost, speed and governance indicators.
- Logs, evidence and diagnostics where authorised.
- Advanced controls and configuration.
- Large/persistent AgentOS chat remains available rather than being sacrificed for telemetry.

## Chat is first-class
Chat is not a sidebar accessory in any mode. It can initiate and manage missions, answer questions, plan work, show status, present results, request approvals, navigate the application and explain system decisions. All chat-originated actions pass through the same permissions, policy, execution, evidence and assurance controls as equivalent UI actions.

## Progressive disclosure
Simple hides complexity without removing capability. Essentials exposes what is normally needed. Tech Head exposes deeper controls and telemetry. Users should be able to drill from Simple into detail without losing context.

## Character canon
- Willow: dark brown hair, brown eyes, glasses.
- Isla: light brown hair, blue eyes.
- Jack: very light brown hair, thin build, no glasses.
- Henry: blonde hair.

## Accessibility and responsiveness
All modes should support readable typography, keyboard navigation where applicable, sufficient contrast, clear status semantics, responsive layouts and touch-friendly controls. Simple is the accessibility baseline; advanced density must not compromise core usability.

## Product rule
Do not build three separate products. Implement a shared capability model and permission layer with presentation profiles. Mode switching must be reversible, predictable and safe.
