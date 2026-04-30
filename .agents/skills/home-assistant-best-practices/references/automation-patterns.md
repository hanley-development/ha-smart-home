# Automation Patterns Reference

## Preferred automation design

Good automations are readable, explicit, safe to reload, resilient to unavailable entities, easy to disable, and easy to troubleshoot.

## Basic notification automation

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

## State guard

```yaml
condition:
  - condition: template
    value_template: >
      {{ states('sensor.example') not in ['unknown', 'unavailable', 'none'] }}
```

## Numeric guard

```yaml
condition:
  - condition: template
    value_template: >
      {{ states('sensor.temperature') | float(default=0) > 80 }}
```

## Anti-spam pattern

Use timers, input booleans, or repeat delays to prevent notification spam.

## Mode guidance

- `single`: simple actions
- `restart`: state-machine behavior
- `queued`: ordered notifications/actions
- `parallel`: only when safe
