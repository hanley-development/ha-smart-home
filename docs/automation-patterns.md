# Automation Patterns

## Purpose

This guide defines preferred Home Assistant automation patterns.

Automations should be safe, readable, and resilient.

## Basic automation structure

```yaml
alias: Garage door left open notification
id: garage_door_left_open_notification
mode: restart

trigger:
  - platform: state
    entity_id: cover.garage_door
    to: open
    for:
      minutes: 10

condition:
  - condition: template
    value_template: >
      {{ states('cover.garage_door') not in ['unknown', 'unavailable'] }}

action:
  - service: notify.mobile_app_phone
    data:
      title: Garage door open
      message: The garage door has been open for 10 minutes.
```

## Recommended modes

Use `single` for simple one-shot automations.

Use `restart` for state-machine style automations where a new trigger should restart the sequence.

Use `queued` for notification or ordered workflows.

Use `parallel` only when safe.

## Guard unknown and unavailable

Use guards when entity state matters.

```yaml
condition:
  - condition: template
    value_template: >
      {{ states('sensor.example') not in ['unknown', 'unavailable', 'none'] }}
```

Use MCP for discovery. Create automations through MCP after approval. Store exports under `home-assistant/automations/exports/`.

## Avoid dangerous automatic actions

Do not automatically lock, unlock, open, close, arm, disarm, or change HVAC aggressively without explicit user approval and clear safety conditions.

Prefer notification first.
