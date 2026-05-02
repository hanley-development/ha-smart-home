---
name: ha-mcp-workflow-tools
description: Use when operating Home Assistant through ha-mcp tools, including MCP discovery, helper creation, automation creation, script creation, dashboard changes, service calls, labels, areas, floors, categories, blueprints, history, reviews, onboarding, and fallback/error handling. Complements home-assistant-best-practices by defining how agents should safely use ha-mcp tools.
---

# ha-mcp Workflow Tools

## Purpose

Use this skill when working with Home Assistant through ha-mcp.

This skill defines safe ha-mcp workflows for:

- discovery
- read-only inspection
- helper creation
- automation creation
- script creation
- dashboard changes
- service calls
- reviews/debugging
- history/traces/logs
- areas, labels, floors, categories, groups, and organization
- blueprints
- HACS/custom card checks
- health/update review
- onboarding/inventory
- fallback/error handling

## Core rule

Use ha-mcp for live Home Assistant discovery.

Use ha-mcp for creating or modifying UI-managed Home Assistant objects only after explicit user approval.

Home Assistant is the source of truth for normal UI-managed objects.

The repo stores:

- plans
- exports
- snapshots
- rollback references
- optional source-controlled YAML only when explicitly needed

Do not create YAML packages by default.

Do not edit `.storage`.

Do not invent entity IDs.

Do not perform live device control without explicit approval.

## Safety-sensitive actions

Extra confirmation is required for anything involving:

- locks
- garage doors/covers
- alarm systems
- HVAC/climate
- cameras
- water valves
- sirens
- security devices
- bulk service calls
- scripts with unknown behavior
- reloads/restarts
- backups/restores
- add-on management
- enabling/disabling automations
- deleting objects

## Tool family router

Use the relevant reference file for the task:

| Task | Reference |
|---|---|
| General ha-mcp rules | `references/core.md` |
| Entity/device/state discovery | `references/entity-discovery.md` |
| Helper creation/review | `references/helper.md` |
| Creating/updating objects | `references/write.md` |
| Read-only inspection | `references/read.md` |
| Review/debug/audit | `references/review.md` |
| Service calls/live control | `references/service-call.md` |
| Dashboards/resources/custom cards | `references/dashboard.md` |
| History/traces/logs | `references/history.md` |
| Areas/labels/floors/groups/categories | `references/organize.md` |
| First-time inventory/onboarding | `references/onboarding.md` |
| Tool failure/ambiguity/unsafe fallback | `references/fallback.md` |

Do not load every reference unless needed.

## Default workflow

1. Use ha-mcp for discovery.
2. Propose a concise plan.
3. Identify safety-sensitive objects.
4. Ask for approval before writes/control.
5. Apply only the approved change.
6. Verify through ha-mcp.
7. Store/export a snapshot in the repo when useful.

## Preferred ha-mcp tools by need

| Need | Preferred tools |
|---|---|
| Entity/device discovery | `ha_search_entities`, `ha_get_state`, `ha_get_entity`, `ha_get_device`, `ha_get_overview` |
| Broad config discovery | `ha_deep_search`, only when narrow tools are insufficient |
| Helpers | `ha_config_list_helpers`, `ha_get_helper_schema`, `ha_config_set_helper`, `ha_delete_helpers_integrations` |
| Automations | `ha_config_get_automation`, `ha_config_set_automation`, `ha_config_remove_automation`, `ha_get_automation_traces` |
| Scripts | `ha_config_get_script`, `ha_config_set_script`, `ha_config_remove_script` |
| Dashboards | `ha_config_get_dashboard`, `ha_config_set_dashboard`, `ha_config_delete_dashboard`, `ha_config_list_dashboard_resources`, `ha_config_set_dashboard_resource`, `ha_config_delete_dashboard_resource` |
| Areas/floors | `ha_config_list_areas`, `ha_config_set_area`, `ha_config_remove_area`, `ha_config_list_floors`, `ha_config_set_floor`, `ha_config_remove_floor`, `ha_list_floors_areas` |
| Labels/categories | `ha_config_get_label`, `ha_config_set_label`, `ha_config_remove_label`, `ha_config_get_category`, `ha_config_set_category`, `ha_config_remove_category` |
| Services/control | `ha_list_services`, `ha_call_service`, `ha_bulk_control`, `ha_get_operation_status` |
| History/debug | `ha_get_history`, `ha_get_automation_traces`, `ha_get_logs` |
| Health/updates | `ha_get_system_health`, `ha_get_updates`, `ha_check_config` |
| HACS/custom cards | `ha_hacs_search`, `ha_hacs_repository_info`, `ha_hacs_download`, `ha_hacs_add_repository` |
| Blueprints | `ha_get_blueprint`, `ha_import_blueprint` |

## Beta filesystem/YAML tools

Treat filesystem and direct YAML tools as advanced/beta-style operations.

Use only when explicitly requested and when object-specific tools cannot do the job:

- `ha_config_set_yaml`
- `ha_list_files`
- `ha_read_file`
- `ha_write_file`
- `ha_delete_file`
- `ha_install_mcp_tools`

Prefer object tools first for helpers, automations, scripts, dashboards, labels, areas, zones, groups, and calendars.

## Repo export locations

Use these locations for snapshots or documentation:

```text
home-assistant/automations/exports/
home-assistant/helpers/exports/
home-assistant/scripts/exports/
home-assistant/dashboards/plans/
```

## Response style

When using ha-mcp, summarize:

- what was inspected
- what will change
- whether approval is needed
- what was verified
- where any export/snapshot should go
