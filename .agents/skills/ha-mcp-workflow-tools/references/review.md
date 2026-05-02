# Review Workflow

## Scope

Use for audit/review before or after changes.

## Preferred tools

Use:

- `ha_config_get_automation`
- `ha_get_automation_traces`
- `ha_get_logs`
- `ha_get_state`
- `ha_get_entity`
- `ha_get_device`
- `ha_list_services`
- `ha_check_config`
- `ha_config_get_script`
- `ha_config_get_dashboard`
- `ha_config_list_helpers`
- `ha_config_list_dashboard_resources`

## Review workflow

1. Identify the target automation/script/dashboard/helper.
2. Read its current config.
3. Inspect related entities/states.
4. For automation issues, inspect traces with `ha_get_automation_traces`.
5. Check logs only if needed.
6. Identify concrete issues.
7. Propose a minimal fix.
8. Do not apply changes until approved.

## Review checklist

Check:

- entity IDs are real
- triggers match expected states/events
- conditions are not impossible
- mode is intentional
- templates handle `unknown`/`unavailable`
- actions use correct services and targets
- notification spam is prevented
- safety-sensitive actions require confirmation
- dashboards do not hide dangerous controls
- custom cards are confirmed installed
- helpers are the right type
- YAML packages are justified if used
- rollback/export path is clear

## Risk levels

- Low: read-only, docs-only, dashboard plan, notification-only proposal
- Medium: helper/automation/script/dashboard write after approval
- High: safety-sensitive device control, deletion, bulk actions, reload/restart, backup/restore, add-on management

## Output format

Return:

- target reviewed
- evidence inspected
- findings
- risk level
- proposed fix
- validation plan
- approval needed before write/control
