# Write Workflow

## Scope

Use for ha-mcp write operations after discovery and approval.

Normal write targets:

- automations
- helpers
- scripts
- scenes
- dashboards
- dashboard resources
- labels
- categories
- areas
- floors
- groups
- zones
- calendar events
- blueprints

## Preferred tools

Use object-specific tools first:

- Automations: `ha_config_set_automation`, `ha_config_get_automation`, `ha_config_remove_automation`
- Scripts: `ha_config_set_script`, `ha_config_get_script`, `ha_config_remove_script`
- Helpers: `ha_config_set_helper`, `ha_config_list_helpers`, `ha_get_helper_schema`
- Dashboards: `ha_config_set_dashboard`, `ha_config_get_dashboard`, `ha_config_list_dashboard_resources`
- Labels/categories: `ha_config_set_label`, `ha_config_get_label`, `ha_config_set_category`, `ha_config_get_category`
- Areas/floors: `ha_config_set_area`, `ha_config_list_areas`, `ha_config_set_floor`, `ha_config_list_floors`
- Groups: `ha_config_set_group`, `ha_config_list_groups`
- Blueprints: `ha_get_blueprint`, `ha_import_blueprint`
- Validation: `ha_check_config` when YAML/config validation is relevant

## Write workflow

1. Read/discover the current state/config first.
2. Draft the exact change.
3. Preview the change to the user.
4. Identify safety-sensitive devices/domains.
5. Ask for explicit approval.
6. Apply only the approved change.
7. Read back with ha-mcp.
8. Verify the intended result.
9. Store/export a concise snapshot in the repo when useful.

## Approval preview format

```text
Proposed ha-mcp write:
- Tool:
- Target:
- Change summary:
- Safety-sensitive impact:
- Validation/read-back:
- Export/snapshot path:

Approval needed before I apply this.
```

## Automation rules

For automations:

- prefer clear state/time/event triggers
- use real entity IDs from ha-mcp discovery
- avoid overusing templates
- guard `unknown` and `unavailable`
- set `mode` intentionally
- prefer notification-only before control
- do not control locks, covers, alarms, HVAC, cameras, sirens, valves, or security systems without extra confirmation

## Script rules

For scripts:

- define fields clearly when reusable
- avoid hidden safety-sensitive actions
- do not run the script unless explicitly approved
- read back the script after writing

## Dashboard write rules

For dashboards:

- read the current dashboard first
- confirm custom cards/resources before use
- preserve existing views/cards unless the user approved replacing them
- avoid hidden tap actions on safety-sensitive controls
- read back the dashboard after writing

## Package rule

Do not create YAML packages by default.

Use packages only when explicitly requested, required by YAML-only integrations, or better as source-controlled feature bundles.
