# Entity Naming Guide

## Purpose

This guide defines preferred naming patterns for Home Assistant entities, helpers, groups, scripts, automations, and templates.

The goal is to make entities predictable, searchable, and easy to maintain.

## General principles

Use names that are:

- clear
- stable
- area-aware
- function-aware
- easy to search
- not overly clever

Prefer real-world room and device names.

Avoid names based only on hardware model numbers unless the model is the meaningful device identity.

## Entity ID pattern

Preferred pattern:

```text
<domain>.<area>_<device_or_function>_<measurement_or_action>
```

Examples:

```text
sensor.garage_freezer_temperature
binary_sensor.garage_entry_door_contact
switch.living_room_lamp
light.kitchen_sink_lights
automation.garage_door_left_open_notification
script.security_arm_night
input_boolean.guest_mode
```

## Areas

Use consistent area names:

```text
garage
kitchen
living_room
master_bedroom
office
basement
front_porch
back_patio
utility_room
network_closet
```

Avoid switching between similar names. Pick one and use it consistently.

## Helpers

Helper names should explain their purpose.

Examples:

```text
input_boolean.guest_mode
input_boolean.vacation_mode
input_boolean.quiet_hours
input_number.garage_door_alert_delay_minutes
timer.garage_door_left_open
counter.garage_door_alert_count
```

## Automations

Automation IDs should describe the event and outcome.

Preferred:

```text
automation.garage_door_left_open_notification
automation.front_door_lock_at_night
automation.kitchen_lights_motion_on
automation.laundry_done_notification
```

## Do not invent entity IDs

When writing automations or scripts, use MCP to discover real entity IDs.

If an entity is unknown, write:

```yaml
# TODO: Replace with real entity ID discovered from Home Assistant.
entity_id: binary_sensor.todo_replace_me
```
