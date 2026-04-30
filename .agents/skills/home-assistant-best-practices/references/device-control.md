# Device Control Safety

## Read-only is usually safe

Allowed without explicit confirmation: read states, inspect attributes, list services, inspect areas/devices/entities, inspect automations/scripts/scenes.

## Control requires approval

Require explicit approval before controlling locks, garage doors, alarm systems, HVAC, cameras, sirens, switches, water valves, and security devices.

## Dangerous domains

```text
alarm_control_panel
lock
cover
climate
camera
siren
switch
fan
valve
water_heater
```

## Safer pattern

1. Read state.
2. Report current state.
3. Recommend action.
4. Ask for approval.
5. Execute only approved action.
6. Verify result.
