# AGENTS.md

## Project purpose

This repository supports a Home Assistant + ha-mcp smart home project.

The goal is to improve Home Assistant automations, helpers, scripts, templates, optional packages, ESPHome devices, entity organization, areas, labels, dashboards, and MCP-assisted smart home workflows.

This project uses the Home Assistant MCP server for live Home Assistant discovery and, after explicit approval, for creating or modifying UI-managed Home Assistant objects.

## Operating model

Use this workflow:

1. Use MCP for live Home Assistant discovery.
2. Identify the smallest safe change.
3. Propose the change before applying it.
4. Ask for explicit approval before creating, modifying, deleting, enabling, disabling, triggering, reloading, restarting, or controlling anything in Home Assistant.
5. Apply only the approved change.
6. Verify the result through MCP.
7. Store an export, snapshot, rollback reference, or note in this repo when useful.

Do not perform repo-wide discovery unless explicitly asked.

## Home Assistant object management

Home Assistant is the source of truth for normal UI-managed objects.

Prefer MCP for creating and modifying:

- helpers
- automations
- dashboards
- areas
- labels
- scenes
- scripts, when UI-managed

The repo should store:

- documentation
- proposed changes
- exported snapshots
- rollback references
- dashboard plans
- helper/automation exports
- optional source-controlled YAML only when explicitly needed

Do not create YAML packages by default.

Use packages only when:

- the user explicitly asks for package-based YAML
- a YAML-only integration requires it
- an existing package is being updated
- a feature is better maintained as source-controlled YAML
- multiple related YAML domains should intentionally live together

## MCP-first discovery

To reduce unnecessary repo scanning and avoid stale assumptions, use the Home Assistant MCP server for live discovery whenever possible.

Use MCP for:

- entity lookup
- device lookup
- area lookup
- label lookup
- state inspection
- helper inspection
- automation inspection
- script inspection
- scene inspection
- dashboard inspection, if available
- service capability lookup
- installed/custom card discovery, if available
- history/traces/logs when debugging

Do not scan the repository just to discover entities, areas, labels, devices, services, helpers, dashboards, or current states.

Read-only MCP actions are allowed without confirmation.

## MCP write/control approval

Never use MCP to perform write/control actions without explicit user approval.

Write/control actions include, but are not limited to:

- turning devices on or off
- opening or closing garage doors
- locking or unlocking locks
- arming or disarming alarms
- changing HVAC modes or setpoints
- creating, modifying, enabling, disabling, deleting, or renaming automations
- creating, modifying, or deleting helpers
- creating, modifying, or deleting scripts
- creating, modifying, or deleting scenes
- modifying dashboards
- changing helpers, labels, areas, entities, or groups
- calling arbitrary Home Assistant services
- reloading Home Assistant
- restarting Home Assistant

Safety-sensitive actions require extra confirmation.

Safety-sensitive domains and objects include:

- locks
- garage doors / covers
- alarm systems
- HVAC / climate
- cameras
- water valves
- sirens
- security modes
- bulk service calls
- scripts with unknown behavior
- reloads/restarts

## Skill usage

Use `home-assistant-best-practices` for Home Assistant design and implementation patterns.

Use `home-assistant-dashboard-designer` for dashboard layout, card selection, custom cards, and dashboard safety.

Use `ha-mcp-workflow-tools` for safe ha-mcp tool workflows, including:

- MCP discovery
- helper creation
- automation creation
- dashboard modification
- service calls
- read-only inspection
- review/debugging
- history/traces/logs
- areas/labels/organization
- onboarding
- fallback/error handling

Do not load every skill/reference unless needed.

## Dashboard agent behavior

This project uses UI-managed dashboards and may use MCP to create or modify dashboards.

Dashboard source files are not expected in the repo.

Do not:

- create YAML dashboard files
- edit YAML dashboard files
- edit `.storage`
- convert UI-managed dashboards to YAML
- assume dashboard files exist in the repo
- make dashboard changes without explicit approval

Use MCP for dashboard discovery and MCP-supported dashboard changes.

For dashboard tasks:

1. Inspect the live dashboard structure through MCP.
2. Confirm custom cards/resources are installed before using them.
3. Propose a layout/card plan.
4. Identify safety-sensitive controls.
5. Ask for approval.
6. Apply only the approved changes through MCP.
7. Verify the result.
8. Store a dashboard plan or snapshot under `home-assistant/dashboards/plans/` when useful.

## Helper behavior

Helpers should normally be created and managed through MCP/Home Assistant UI.

Use MCP to inspect existing helpers before proposing new ones.

Use helpers for:

- feature enable/disable toggles
- thresholds
- delays/durations
- modes
- counters
- timers
- manual buttons
- reusable automation state

Do not create helper YAML packages unless explicitly asked.

After creating or modifying helpers through MCP, store snapshots/exports under:

```text
home-assistant/helpers/exports/
```

## Automation behavior

Automations should normally be created and managed through MCP/Home Assistant UI.

Before creating or modifying an automation:

1. Use MCP to discover real entities, services, helpers, and related automations.
2. Prefer native triggers/conditions/actions over unnecessary templates.
3. Propose the automation behavior.
4. Identify safety-sensitive actions.
5. Ask for approval.
6. Create or modify through MCP only after approval.
7. Verify the result through MCP.
8. Store snapshots/exports under `home-assistant/automations/exports/` when useful.

Automations should be:

- readable
- idempotent where possible
- safe to reload
- resilient to `unknown` and `unavailable`
- explicit about triggers, conditions, and actions
- careful with delays, repeats, and mode behavior
- designed to fail safely

Preferred automation modes:

- `single` for simple one-shot automations
- `restart` for state-machine style automations
- `queued` for notification or ordered workflows
- `parallel` only when clearly safe

Use guards for:

- `unknown`
- `unavailable`
- missing attributes
- empty lists
- stale sensors
- nighttime/daytime constraints
- occupancy ambiguity
- network/device availability

Notification-only automations are preferred before automatic control.

## Package behavior

Packages are optional.

Do not create packages by default.

A package may include:

- automation
- script
- template
- sensor
- binary_sensor
- input_boolean
- input_number
- input_select
- input_datetime
- timer
- counter
- variable
- group

Use packages only when:

- explicitly requested
- a YAML-only integration requires them
- an existing package is being updated
- a feature is better maintained as source-controlled YAML
- multiple related YAML domains intentionally need to live together

Packages should represent one clear feature or system.

Examples:

```text
nws_alerts.yaml
esphome_auto_updates.yaml
battery_monitoring.yaml
network_monitoring.yaml
```

Do not use packages as random dumping grounds.

## Context discipline

Codex should minimize context usage.

- Respect `.codexignore`.
- Do not scan the whole repository unless explicitly asked.
- Do not inspect `.storage`.
- Do not inspect logs, databases, backups, cache folders, generated files, dependency folders, or build output unless directly relevant.
- Do not inspect secrets unless explicitly instructed and safe to do so.
- Prefer targeted edits to named files.
- Prefer small patches over full rewrites.
- Preserve existing comments and formatting where possible.
- Ask before broad refactors.
- Keep summaries concise.
- Do not invent entity IDs, device names, areas, labels, secrets, tokens, IPs, service calls, helper IDs, dashboard IDs, or file paths.

## Home Assistant repo storage

Repo folders under `home-assistant/` are primarily for documentation, exports, snapshots, and optional YAML.

Recommended structure:

```text
home-assistant/
├─ AGENTS.md
├─ automations/
│  └─ exports/
├─ helpers/
│  └─ exports/
├─ packages/
├─ scripts/
│  └─ exports/
└─ dashboards/
   └─ plans/
```

Files in these folders are not automatically live-loaded by Home Assistant unless explicitly documented.

Use:

- `home-assistant/automations/exports/` for automation exports, proposed YAML, snapshots, and rollback references
- `home-assistant/helpers/exports/` for helper exports, helper design notes, and rollback references
- `home-assistant/scripts/exports/` for script exports and snapshots
- `home-assistant/dashboards/plans/` for dashboard plans, card plans, and layout notes
- `home-assistant/packages/` for optional source-controlled YAML packages only when needed

Do not modify `secrets.yaml` unless explicitly instructed.

Do not delete automations, scripts, helpers, scenes, entities, labels, areas, or dashboard content without explicit confirmation.

## Template behavior

Prefer native Home Assistant triggers, conditions, helpers, and integrations before writing complex templates.

Templates should safely handle:

- `unknown`
- `unavailable`
- missing attributes
- empty lists
- invalid numeric values

Use safe conversions:

```jinja2
{{ states('sensor.temperature') | float(default=0) }}
```

Use safe state checks:

```jinja2
{{ states('sensor.example') not in ['unknown', 'unavailable', 'none'] }}
```

Avoid deeply nested templates unless necessary.

## ESPHome rules

ESPHome changes should be conservative and validated.

Do not change the following unless explicitly asked:

- device name
- friendly name
- static IP
- Wi-Fi settings
- API encryption
- OTA settings
- board type
- substitutions
- package include structure
- GPIO pins
- relay behavior
- garage door behavior
- safety interlocks

Do not compile or upload firmware unless explicitly asked.

Prefer validation first:

```bash
esphome config path/to/device.yaml
```

Only compile with explicit approval:

```bash
esphome compile path/to/device.yaml
```

Only upload with explicit approval:

```bash
esphome upload path/to/device.yaml
```

## Git behavior

Do not commit unless explicitly asked.

Do not run the following unless explicitly asked:

- `git pull`
- `git push`
- `git reset`
- `git rebase`
- `git clean`
- broad repo-wide formatting
- mass renames

Because this project may be accessed over Samba, avoid unnecessary repo-wide Git operations.

Prefer focused diffs on named files.

## Validation

Use the most specific validation available.

Preferred checks:

- MCP-created helpers/automations/scripts/dashboards: read back through MCP and verify the expected fields/entities/actions.
- Home Assistant YAML/packages/templates/scripts: run Home Assistant config check if available.
- ESPHome YAML: run `esphome config <file>` before suggesting compile/upload.
- Python files: run targeted tests or syntax checks.
- Markdown/rules files: check for clarity and consistency.

Do not run long deployment, compile, upload, reload, restart, or live-service commands unless explicitly asked.

## Safety and privacy

Do not expose, print, modify, or commit secrets.

Sensitive items include:

- passwords
- API keys
- long-lived access tokens
- webhook URLs
- private keys
- certificates
- Duo/Auth secrets
- Cloudflare tokens
- MQTT credentials
- Wi-Fi credentials
- Home Assistant tokens

If a file appears to contain secrets, stop and warn the user before displaying or modifying that content.

## Response style

Be practical and concise.

When making changes, summarize:

- what was inspected
- files changed, if any
- Home Assistant objects created/modified, if any
- what changed
- validation or MCP verification performed
- risks or follow-up actions
- where exports/snapshots were stored, if applicable

Avoid long explanations unless the user asks for them.
