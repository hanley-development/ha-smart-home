# Write Workflow

## Scope

Use for MCP write operations after discovery and approval.

Normal write targets:

- automations
- helpers
- scripts
- dashboards
- labels
- areas
- scenes
- dashboard resources

## Preferred tools

Use:

- Automations: `ha_config_set_automation`, `ha_config_get_automation`, `ha_config_remove_automation`
- Scripts: `ha_config_set_script`, `ha_config_get_script`, `ha_config_remove_script`
- Helpers: `ha_config_set_helper`, `ha_config_list_helpers`, `ha_get_helper_schema`
- Dashboards: `ha_config_set_dashboard`, `ha_config_get_dashboard`
- Labels/areas: `ha_config_set_label`, `ha_config_set_area`
- Validation: `ha_check_config` when YAML/config validation is relevant

## Write workflow

1. Read/discover the current state/config first.
2. Draft the exact change.
3. Preview the change to the user.
4. Identify safety-sensitive devices/domains.
5. Ask for explicit approval.
6. Apply only the approved change.
7. Read back with MCP.
8. Verify the intended result.
9. Store/export a concise snapshot in the repo when useful.

## Automation rules

For automations:

- prefer clear state/time/event triggers
- use real entity IDs from MCP discovery
- avoid overusing templates
- guard `unknown` and `unavailable`
- set `mode` intentionally
- prefer notification-only before control
- do not control locks, covers, alarms, HVAC, cameras, sirens, valves, or security systems without extra confirmation

## Package rule

Do not create YAML packages by default.

Use packages only when explicitly requested, required by YAML-only integrations, or better as source-controlled feature bundles.
