# Helper Workflow

## Scope

Use for helper design and MCP-managed helper creation.

Helpers should normally be created through MCP/Home Assistant, not YAML packages, unless explicitly requested.

## Preferred tools

Use:

- `ha_config_list_helpers` to inspect existing helpers
- `ha_get_helper_schema` to identify required/allowed helper fields
- `ha_config_set_helper` to create or update helpers after approval
- `ha_delete_helpers_integrations` only after explicit destructive confirmation

## Helper selection

Use:

- `input_boolean` for modes, toggles, and enable/disable flags
- `input_number` for thresholds, durations, retry counts, limits
- `input_select` for named modes or finite state choices
- `input_datetime` for configurable times/dates
- `timer` for delayed/repeat workflows
- `counter` for event counts or retry attempts
- `input_button` for manual triggers

## Flow

1. Inspect existing helpers with `ha_config_list_helpers`.
2. Reuse existing helpers when appropriate.
3. If new helper is needed, propose:
   - helper type
   - entity_id/name
   - icon
   - min/max/step/unit where applicable
   - restore/default behavior where applicable
4. Ask for approval before creating/updating.
5. Use `ha_get_helper_schema` before `ha_config_set_helper`.
6. Create/update with `ha_config_set_helper`.
7. Verify with `ha_config_list_helpers` or `ha_get_state`.
8. Store/export the helper snapshot under `home-assistant/helpers/exports/` when useful.

## Do not

- create helper YAML packages by default
- invent helper entity IDs
- delete helpers without explicit confirmation
- create helpers when a native automation feature is simpler
