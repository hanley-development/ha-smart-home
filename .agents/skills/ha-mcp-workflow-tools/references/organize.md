# Organization Workflow

## Scope

Use for organization and cleanup:

- areas
- floors
- labels
- categories
- groups
- entity registry metadata
- naming cleanup plans

## Preferred tools

Use:

- `ha_config_list_areas`
- `ha_config_set_area`
- `ha_config_remove_area`
- `ha_config_list_floors`
- `ha_config_set_floor`
- `ha_config_remove_floor`
- `ha_config_get_label`
- `ha_config_set_label`
- `ha_config_remove_label`
- `ha_config_get_category`
- `ha_config_set_category`
- `ha_config_remove_category`
- `ha_get_entity`
- `ha_set_entity`
- `ha_config_list_groups`
- `ha_config_set_group`
- `ha_config_remove_group`

## Flow

1. Inventory current organization.
2. Identify duplicates, unclear names, missing areas/labels.
3. Propose a cleanup plan.
4. Ask for approval before creating/removing/renaming.
5. Apply only approved changes.
6. Verify through MCP.
7. Update docs such as `docs/areas.md`, `docs/labels.md`, or `docs/known-issues.md` when useful.

## Do not

- rename entities without approval
- remove areas/labels/groups without exact confirmation
- reorganize broad sets without a reviewed plan
- invent naming conventions that conflict with user preferences
