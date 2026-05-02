# Read Workflow

## Scope

Use for read-only Home Assistant inspection.

## Preferred tools

Use:

- `ha_get_overview` for broad system summary
- `ha_search_entities` for entity lookup
- `ha_get_state` for state/attributes
- `ha_get_entity` for entity registry details
- `ha_config_get_automation` for automation config
- `ha_config_get_script` for script config
- `ha_config_list_helpers` for helpers
- `ha_config_get_dashboard` for dashboards
- `ha_config_list_dashboard_resources` for Lovelace resources
- `ha_get_system_health` for health
- `ha_get_updates` for update entities
- `ha_get_logs` only when logs are directly relevant

## Read workflow

1. Use the narrowest read tool first.
2. Avoid broad/deep reads unless required.
3. Do not dump huge raw JSON/YAML unless explicitly requested.
4. Summarize the relevant facts.
5. Include exact entity IDs/object IDs.
6. Note uncertainty or missing access.

## Output format

Return:

- what was inspected
- relevant IDs
- current state/config summary
- issues found
- recommended next action
