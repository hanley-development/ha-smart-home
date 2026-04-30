# home-assistant/AGENTS.md

## Scope

This directory contains Home Assistant source-controlled configuration.

This may include:

- automations
- scripts
- scenes
- packages
- templates
- groups
- helpers represented in YAML
- notification logic

This project does not use YAML-managed dashboards.

## Dashboard rule

Dashboards are UI-managed.

Do not:

- create YAML dashboard files
- edit YAML dashboard files
- edit `.storage`
- convert UI dashboards to YAML

Use MCP or the Home Assistant UI for dashboard inspection and changes.

## File handling

- Prefer editing YAML files directly.
- Do not hand-edit `.storage`.
- Do not modify generated files, logs, databases, backups, or dependency folders.
- Preserve comments and formatting.
- Keep related logic together when reasonable.
- Prefer packages for grouped feature logic.

## Entity rules

- Do not invent entity IDs.
- Use MCP to discover real entities.
- Prefer stable entity IDs over friendly names.
- Do not rename entities unless explicitly asked.
- If an entity is unknown, mark it as TODO instead of guessing.

Example:

```yaml
# TODO: Replace with real entity discovered from MCP.
entity_id: binary_sensor.todo_replace_me
```

## Automation rules

Automations should be:

- readable
- safe
- reloadable
- resilient to `unknown` and `unavailable`
- explicit about triggers, conditions, and actions
- careful with delays, repeats, and modes

Preferred modes:

- `single` for simple one-shot automations
- `restart` for state-machine automations
- `queued` for ordered actions or notifications
- `parallel` only when clearly safe

## Safety-sensitive devices

Require explicit approval before creating automations that control:

- locks
- garage doors
- alarm systems
- HVAC
- cameras
- water valves
- sirens
- security devices

Notification-only automations are preferred first.

## Validation

Prefer Home Assistant config validation before reload.

Do not reload or restart Home Assistant unless explicitly asked.
