# 5-Minute Cascade Scheduling Decision

Date: 2026-08-28
Owner: GPTChat Overseer
Status: ADOPTED AS TARGET SCHEDULE

## Purpose
Give each supervisory layer time to execute, checkpoint and respond before the next layer evaluates its output.

## Target cadence
- T+00: GPTChat Overseer heartbeat
- T+05: Project Overseer heartbeats
- T+10: Worker/sub-worker heartbeats
- T+15: GPTChat Overseer heartbeat
- T+20: Project Overseer heartbeats
- T+25: Worker/sub-worker heartbeats
- Repeat every 15 minutes with the same 5-minute phase offsets.

## Operating rule
Heartbeats are safety nets, not proof of execution. A downstream layer must inspect durable state/evidence and must not duplicate an active task. Event-driven execution may occur earlier where supported.

## Verification chain
GPTChat Overseer -> Project Overseer -> Worker -> checkpoint/evidence -> Project Overseer -> GPTChat Overseer.

A scheduled wake does not equal completion. Only observable execution and evidence advance a task state.

## Rollout requirement
Apply this cadence only where the corresponding scheduler/runtime supports the phase. Record actual execution evidence. Do not claim the schedule is live merely because this specification exists.
