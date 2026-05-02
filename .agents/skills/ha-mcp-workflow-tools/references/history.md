# History Workflow

## Scope

Use for time-based investigation and debugging.

## Preferred tools

Use:

- `ha_get_history`
- `ha_get_automation_traces`
- `ha_get_logs`
- `ha_get_state`
- `ha_get_camera_image` only when the user asks for camera/image context

## Flow

1. Define the exact time window.
2. Inspect current state.
3. Pull history/traces/logs only for relevant entities or automations.
4. Avoid broad history pulls unless necessary.
5. Summarize findings with timestamps.
6. Recommend next action.

## Use cases

- why an automation did or did not run
- when a door/motion/device changed state
- whether a sensor is stale/flapping
- whether a notification fired repeatedly
- whether an update or integration produced errors

## Safety

Do not use camera snapshots unless the user explicitly asks or the task requires camera context.
