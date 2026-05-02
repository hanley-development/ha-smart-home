# Service Call Workflow

## Scope

Use for service discovery and approved service calls.

## Preferred tools

Use:

- `ha_list_services` before unfamiliar service calls
- `ha_get_state` before and after control
- `ha_call_service` for single service calls
- `ha_bulk_control` only for approved multi-entity changes
- `ha_get_operation_status` when operation tracking is returned

## Safety model

Read-only service discovery is allowed.

Any actual service call requires explicit approval.

Extra confirmation is required for:

- locks
- garage doors/covers
- alarms
- HVAC/climate
- cameras
- sirens
- valves/water controls
- security modes
- bulk actions

## Flow

1. Discover current state.
2. List/inspect service if needed.
3. Preview exact domain, service, target, and data.
4. Identify safety-sensitive effects.
5. Ask for explicit approval.
6. Call service only after approval.
7. Verify resulting state.
8. Report result.

## Do not

- call services while "testing" without approval
- infer a destructive service target
- use `all` targets for safety-sensitive domains
- run scripts if script behavior is unknown and may control devices
