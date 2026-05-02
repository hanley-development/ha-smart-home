# Core ha-mcp Rules

## Mission

Operate Home Assistant through ha-mcp with a safety-first, MCP-first workflow.

Use Home Assistant as the source of truth for normal UI-managed objects:

- helpers
- automations
- scripts
- scenes
- dashboards
- areas
- labels
- floors
- categories
- groups
- zones

Use the repo for:

- agent rules
- skills
- proposed changes
- exported snapshots
- rollback notes
- optional source-controlled YAML only when explicitly wanted

## Preferred workflow

1. Discover through ha-mcp.
2. Propose a compact plan.
3. Ask for explicit approval before writes/control.
4. Apply only the approved change.
5. Verify through ha-mcp.
6. Store/export a concise snapshot in the repo when useful.

## Tool families

Use these ha-mcp tool families when available:

- Discovery: `ha_search_entities`, `ha_get_overview`, `ha_get_state`, `ha_get_entity`, `ha_get_device`, `ha_deep_search`
- Automations: `ha_config_get_automation`, `ha_config_set_automation`, `ha_config_remove_automation`, `ha_get_automation_traces`
- Helpers: `ha_config_list_helpers`, `ha_get_helper_schema`, `ha_config_set_helper`, `ha_delete_helpers_integrations`
- Scripts: `ha_config_get_script`, `ha_config_set_script`, `ha_config_remove_script`
- Dashboards: `ha_config_get_dashboard`, `ha_config_set_dashboard`, `ha_config_delete_dashboard`, `ha_config_list_dashboard_resources`, `ha_config_set_dashboard_resource`, `ha_config_delete_dashboard_resource`
- Areas/floors: `ha_config_list_areas`, `ha_config_set_area`, `ha_config_remove_area`, `ha_config_list_floors`, `ha_config_set_floor`, `ha_config_remove_floor`, `ha_list_floors_areas`
- Labels/categories: `ha_config_get_label`, `ha_config_set_label`, `ha_config_remove_label`, `ha_config_get_category`, `ha_config_set_category`, `ha_config_remove_category`
- Services/control: `ha_list_services`, `ha_call_service`, `ha_bulk_control`, `ha_get_operation_status`
- History/debug: `ha_get_history`, `ha_get_automation_traces`, `ha_get_logs`
- System: `ha_check_config`, `ha_get_system_health`, `ha_get_updates`
- HACS: `ha_hacs_search`, `ha_hacs_repository_info`, `ha_hacs_download`, `ha_hacs_add_repository`
- Blueprints: `ha_get_blueprint`, `ha_import_blueprint`
- Add-ons/system operations: `ha_get_addon`, `ha_manage_addon`, `ha_backup_create`, `ha_backup_restore`, `ha_reload_core`, `ha_restart`

## Filesystem/YAML editing

Treat filesystem and YAML-editing tools as advanced operations.

Do not use `ha_config_set_yaml`, `ha_read_file`, `ha_write_file`, `ha_delete_file`, `ha_list_files`, or `ha_install_mcp_tools` unless:

- the user explicitly asks for YAML/file editing
- the target path is clear
- the user understands it is not the normal UI-managed object flow
- validation/check configuration is performed when possible

Prefer object-specific tools first:

- `ha_config_set_helper`
- `ha_config_set_automation`
- `ha_config_set_script`
- `ha_config_set_dashboard`
- `ha_config_set_label`
- `ha_config_set_area`

## Global safety rules

Do not invent entity IDs, helper IDs, dashboard IDs, area IDs, label IDs, services, scripts, URLs, secrets, or file paths.

Read-only ha-mcp discovery is allowed.

Any create, update, delete, enable, disable, service call, reload, restart, backup/restore, add-on management, or live device control requires explicit user approval.

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

## Failure behavior

When a tool fails:

1. Report the failure plainly.
2. Do not guess the result.
3. Try a narrower read-only tool if useful.
4. If the capability is missing, explain which capability is missing.
5. Provide a safe manual/UI path only when useful.
6. Do not retry destructive/write actions by guessing.
