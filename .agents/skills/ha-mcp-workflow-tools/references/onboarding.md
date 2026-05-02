# Onboarding Workflow

## Scope

Use for first-pass inventory and repo documentation.

## Preferred tools

Use:

- `ha_get_overview`
- `ha_search_entities`
- `ha_config_list_areas`
- `ha_list_floors_areas`
- `ha_config_list_helpers`
- `ha_config_get_dashboard`
- `ha_config_list_dashboard_resources`
- `ha_get_updates`
- `ha_get_system_health`

## Flow

1. Verify MCP can read Home Assistant.
2. Get overview.
3. Inventory areas/floors.
4. Inventory labels/categories if needed.
5. Inventory helpers.
6. Inventory dashboards/resources.
7. Identify obvious organization gaps.
8. Do not modify anything.
9. Update repo docs only if asked.

## Output format

Return:

- MCP connectivity result
- areas/floors summary
- helper summary
- dashboard/resource summary
- custom card/resource summary
- obvious cleanup opportunities
- next suggested task
