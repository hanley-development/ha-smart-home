# Core ha-mcp Rules

## Mission

Operate Home Assistant through ha-mcp with a safety-first, MCP-first workflow.

Use Home Assistant as the source of truth for normal UI-managed objects:

- helpers
- automations
- dashboards
- areas
- labels
- scenes
- scripts when UI-managed

Use the repo for:

- agent rules
- skills
- proposed changes
- exported snapshots
- rollback notes
- optional source-controlled YAML only when explicitly wanted

## Preferred workflow

1. Discover through MCP.
2. Propose a compact plan.
3. Ask for explicit approval before writes/control.
4. Apply only the approved change.
5. Verify through MCP.
6. Store/export a concise snapshot in the repo when useful.

## Tool families

Use these ha-mcp tool families when available:

- Discovery: `ha_search_entities`, `ha_get_overview`, `ha_get_state`, `ha_deep_search`
- Automations: `ha_config_get_automation`, `ha_config_set_automation`, `ha_config_remove_automation`
- Helpers: `ha_config_list_helpers`, `ha_get_helper_schema`, `ha_config_set_helper`, `ha_delete_helpers_integrations`
- Scripts: `ha_config_get_script`, `ha_config_set_script`, `ha_config_remove_script`
- Dashboards: `ha_config_get_dashboard`, `ha_config_set_dashboard`, `ha_config_delete_dashboard`, `ha_config_list_dashboard_resources`, `ha_config_set_dashboard_resource`, `ha_config_delete_dashboard_resource`
- Areas/floors: `ha_config_list_areas`, `ha_config_set_area`, `ha_config_remove_area`, `ha_config_list_floors`, `ha_config_set_floor`, `ha_config_remove_floor`
- Labels/categories: `ha_config_get_label`, `ha_config_set_label`, `ha_config_remove_label`, `ha_config_get_category`, `ha_config_set_category`, `ha_config_remove_category`
- Services/control: `ha_list_services`, `ha_call_service`, `ha_bulk_control`, `ha_get_operation_status`
- History/debug: `ha_get_history`, `ha_get_automation_traces`, `ha_get_logs`
- System: `ha_check_config`, `ha_get_system_health`, `ha_get_updates`
- HACS: `ha_hacs_search`, `ha_hacs_repository_info`, `ha_hacs_download`, `ha_hacs_add_repository`

## Filesystem/YAML editing

Treat filesystem and YAML-editing tools as advanced operations.

Do not use `ha_config_set_yaml`, `ha_read_file`, `ha_write_file`, `ha_delete_file`, or `ha_list_files` unless:

- the user explicitly asks for YAML/file editing
- the target path is clear
- the user understands it is not the normal UI-managed object flow
- validation/check configuration is performed when possible

## Global safety rules

Do not invent entity IDs, helper IDs, dashboard IDs, area IDs, label IDs, services, or script IDs.

Read-only MCP discovery is allowed.

Any create, update, delete, enable, disable, service call, reload, restart, or live device control requires explicit user approval.

Do not hand-edit `.storage`.

Do not create YAML packages by default.

Safety-sensitive domains require extra confirmation:

- `alarm_control_panel`
- `lock`
- `cover`
- `climate`
- `camera`
- `siren`
- `valve`
- `water_heater`
- security-related switches/scripts
