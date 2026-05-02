# Dashboard Workflow

## Scope

Use for UI-managed dashboards through ha-mcp.

Do not edit `.storage`.

Do not create YAML dashboard source files unless explicitly requested.

## Preferred tools

Use:

- `ha_config_get_dashboard`
- `ha_config_set_dashboard`
- `ha_config_delete_dashboard`
- `ha_config_list_dashboard_resources`
- `ha_config_set_dashboard_resource`
- `ha_config_delete_dashboard_resource`
- `ha_hacs_search`
- `ha_hacs_repository_info`
- `ha_hacs_download`

## Dashboard workflow

1. Inspect dashboards/resources through ha-mcp.
2. Confirm custom cards/resources are installed before using them.
3. Read the existing dashboard before content changes.
4. Propose a targeted plan.
5. Identify safety-sensitive controls.
6. Ask for approval before applying changes.
7. Apply through `ha_config_set_dashboard` or resource tools.
8. Read back and verify the change.
9. Store a dashboard plan/snapshot under `home-assistant/dashboards/plans/` when useful.

## Dashboard planning checklist

For each dashboard/view, capture:

- purpose
- target users/devices
- entities involved
- card types
- custom card dependencies
- whether each dependency is confirmed installed
- safety-sensitive controls
- fallback built-in card option
- mobile layout notes
- navigation links/buttons

## Recommended dashboard map

A good feature-rich dashboard set usually includes:

- Home overview
- Area overview
- Security
- Garage/doors/locks
- Climate and air quality
- Lighting/fans/humidifiers/air filters
- Cameras
- Energy and appliances
- Weather
- Network
- Home Assistant health/updates
- Automations and scripts

## Custom card rules

- Prefer built-in Home Assistant cards when they solve the problem cleanly.
- Use custom cards only when they provide clear value.
- Confirm installation via dashboard resources/HACS before using a custom card.
- Do not invent custom-card schema.
- Do not use stale/unmaintained custom cards for critical controls unless approved.

## Useful card families

Confirm installation before using custom cards.

- built-in Tile, Area, Entities, Button, Conditional, Gauge, History Graph, Markdown, Thermostat, Alarm Panel, Picture Glance
- Mushroom cards
- button-card
- auto-entities
- card-mod
- Bubble Card
- ApexCharts Card
- mini-graph-card
- layout-card
- vertical-stack-in-card
- Battery State Card
- Gauge Card Pro
- Entity Progress Card
- Weather Chart Card
- Horizon Card
- Simple Thermostat
- Firemote / TV remote cards
- vacuum/purifier/device-specific cards when relevant

## Safety-sensitive cards

For locks, garage doors, alarms, HVAC, cameras, sirens, valves, and security controls:

- show status before controls
- keep controls visually separated
- avoid hidden tap actions
- use confirmation where possible
- do not bury controls inside unclear popups
- provide clear labels and icons

## Proposal format

```text
Dashboard:
View:

Proposed changes:
- ...

Entities:
- ...

Custom cards:
- card: confirmed/not confirmed

Safety-sensitive controls:
- ...

Fallback:
- ...

Approval needed before I modify the dashboard.
```
