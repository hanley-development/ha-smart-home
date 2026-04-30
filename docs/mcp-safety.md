# MCP Safety Guide

## Purpose

This project uses the Home Assistant MCP server for live discovery and controlled interaction with Home Assistant.

MCP is powerful and should be treated carefully.

## Read-only MCP actions

Allowed without explicit confirmation:

- inspect entity state
- inspect device metadata
- inspect areas
- inspect labels
- inspect automations
- inspect scripts
- inspect scenes
- inspect services
- inspect dashboards, if supported
- inspect history/statistics, if supported

## Write/control MCP actions

Require explicit user confirmation:

- turn devices on/off
- open/close garage doors
- lock/unlock doors
- arm/disarm alarm
- change HVAC mode
- change thermostat setpoints
- enable/disable automations
- delete automations
- edit helpers
- rename entities
- change areas
- change labels
- reload Home Assistant
- restart Home Assistant
- modify dashboards
- run scripts that control devices
- call arbitrary services

## Dangerous domains

Be especially careful with:

```text
alarm_control_panel
lock
cover
climate
camera
switch
fan
water_heater
valve
siren
```

## Preferred workflow

Use MCP like this:

1. Query current state.
2. Query real entity IDs.
3. Query available services.
4. Draft the change.
5. Ask for approval before live writes.
6. Apply only the approved change.
7. Verify state after change.
