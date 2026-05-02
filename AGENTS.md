# AGENTS.md

## Project purpose

This repository supports a Home Assistant + ha-mcp smart home project.

The goal is to improve Home Assistant automations, helpers, scripts, templates, optional packages, ESPHome devices, entity organization, areas, labels, dashboards, and MCP-assisted workflows while keeping the live home safe.

This project uses Home Assistant MCP / ha-mcp for live Home Assistant discovery and, after explicit approval, for creating or modifying Home Assistant objects.

## Primary operating model

Use this workflow:

1. Use ha-mcp for live Home Assistant discovery.
2. Identify the smallest safe change.
3. Propose the change before applying it.
4. Ask for explicit approval before any write, delete, reload, restart, live service call, live control action, firmware compile/upload, or dashboard modification.
5. Apply only the approved change.
6. Verify the result through ha-mcp or a targeted validation command.
7. Store an export, snapshot, rollback note, or plan in this repo when useful.

Read-only discovery is allowed. Live writes and control require approval.

Do not perform broad repo-wide discovery unless explicitly asked.

## Tool and action router

Choose the narrowest path:

| User asks for | Preferred path |
|---|---|
| Find entities, devices, states, areas, labels | Read-only ha-mcp discovery |
| Build or modify UI-managed helper | ha-mcp helper tools after approval |
| Build or modify UI-managed automation | ha-mcp automation tools after approval |
| Build or modify UI-managed script | ha-mcp script tools after approval |
| Build or modify UI-managed dashboard | ha-mcp dashboard tools after approval |
| Plan dashboards/custom cards | Repo docs plus read-only ha-mcp discovery |
| Review/debug automation | ha-mcp config + trace/log tools, no writes without approval |
| Optional source-controlled package YAML | Repo file edit after user asks for YAML/package workflow |
| ESPHome review | Repo file edit/review and `esphome config` only; compile/upload requires approval |
| Live control/device action | ha-mcp service tools only after explicit approval |

## Home Assistant object management

Home Assistant is the source of truth for normal UI-managed objects.

Prefer ha-mcp for creating and modifying:

- helpers
- automations
- dashboards
- areas
- labels
- categories
- scenes
- scripts, when UI-managed

The repo should store:

- documentation
- proposed changes
- exported snapshots
- rollback references
- dashboard plans
- helper/automation/script exports
- optional source-controlled YAML only when explicitly needed

Do not create YAML packages by default.

Use packages only when:

- the user explicitly asks for package-based YAML
- a YAML-only integration requires it
- an existing package is being updated
- a feature is better maintained as source-controlled YAML
- multiple related YAML domains should intentionally live together

## ha-mcp-first discovery

Use ha-mcp for live discovery whenever possible.

Use ha-mcp for:

- entity lookup
- device lookup
- area/floor lookup
- label/category lookup
- state inspection
- helper inspection
- automation inspection
- script inspection
- scene inspection
- dashboard inspection
- dashboard resource/custom-card inspection
- service capability lookup
- HACS/custom card checks when available
- history, statistics, traces, logs, health, and update checks when debugging

Do not scan the repository just to discover live Home Assistant entities, areas, labels, devices, services, helpers, dashboards, or current states.

## ha-mcp write/control approval

Never use ha-mcp write/control tools without explicit user approval.

Write/control actions include:

- turning devices on or off
- opening or closing garage doors
- locking or unlocking locks
- arming or disarming alarms
- changing HVAC modes or setpoints
- creating, modifying, enabling, disabling, deleting, or renaming automations
- creating, modifying, or deleting helpers
- creating, modifying, or deleting scripts
- creating, modifying, or deleting scenes
- modifying dashboards or dashboard resources
- changing helpers, labels, categories, areas, floors, entities, groups, or zones
- calling Home Assistant services
- importing blueprints
- reloading or restarting Home Assistant
- backup/restore actions
- add-on management

Safety-sensitive actions require extra confirmation.

Safety-sensitive domains and objects include:

- locks
- garage doors and covers
- alarm systems
- HVAC and climate
- cameras
- water valves
- sirens
- security modes
- bulk service calls
- scripts with unknown behavior
- reloads and restarts
- backups and restores
- add-on management

## ha-mcp beta/file/YAML tools

Treat ha-mcp filesystem and YAML-editing tools as exceptional.

Do not use these unless the user explicitly asks for file/YAML editing and the target path is clear:

- `ha_config_set_yaml`
- `ha_list_files`
- `ha_read_file`
- `ha_write_file`
- `ha_delete_file`
- `ha_install_mcp_tools`

Prefer dedicated object tools first, such as:

- `ha_config_set_helper`
- `ha_config_set_automation`
- `ha_config_set_script`
- `ha_config_set_dashboard`
- `ha_config_set_label`
- `ha_config_set_area`

If YAML/file tools are unavailable, do not guess. Explain the missing capability and provide a safe UI or repo-based fallback.

## Skill usage

Use `home-assistant-best-practices` for Home Assistant design and implementation patterns.

Use `home-assistant-dashboard-designer` for dashboard layout, card selection, custom cards, and dashboard safety.

Use `ha-mcp-workflow-tools` for safe ha-mcp tool workflows, including:

- discovery
- helper creation
- automation creation
- script creation
- dashboard modification
- service calls
- read-only inspection
- review/debugging
- history/traces/logs
- areas/labels/floors/categories organization
- onboarding/inventory
- fallback/error handling

Do not load every skill/reference unless needed.

## Codex subagent-style workflow

Codex may use role prompts under `.codex/agents/` as subagent-style task scopes.

Use these roles when helpful:

- `ha-mcp-operator` — safe live discovery and tool routing
- `automation-builder` — automation/helper/script design
- `dashboard-designer` — dashboards, custom cards, and visual layout
- `entity-organizer` — areas, labels, names, categories, grouping
- `reviewer` — safety, validation, and regression review

Subagent prompts are not independent authority. This `AGENTS.md` remains the top-level policy.

## Dashboard behavior

This project uses UI-managed dashboards and may use ha-mcp to create or modify dashboards.

Dashboard source files are not expected in the repo.

Do not:

- create YAML dashboard files by default
- edit YAML dashboard files by default
- edit `.storage`
- convert UI-managed dashboards to YAML
- assume dashboard files exist in the repo
- make dashboard changes without explicit approval

For dashboard tasks:

1. Inspect the live dashboard structure through ha-mcp.
2. Confirm custom cards/resources are installed before using them.
3. Propose a layout/card plan.
4. Identify safety-sensitive controls.
5. Ask for approval.
6. Apply only approved changes through ha-mcp/UI-supported tools.
7. Verify the result.
8. Store a dashboard plan or snapshot under `home-assistant/dashboards/plans/` when useful.

## Helper behavior

Helpers should normally be created and managed through ha-mcp/Home Assistant UI.

Use ha-mcp to inspect existing helpers before proposing new ones.

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

After creating or modifying helpers through ha-mcp, store snapshots/exports under:

```text
home-assistant/helpers/exports/
```

## Automation behavior

Automations should normally be created and managed through ha-mcp/Home Assistant UI.

Before creating or modifying an automation:

1. Use ha-mcp to discover real entities, services, helpers, and related automations.
2. Prefer native triggers/conditions/actions over unnecessary templates.
3. Propose the automation behavior.
4. Identify safety-sensitive actions.
5. Ask for approval.
6. Create or modify through ha-mcp only after approval.
7. Verify the result through ha-mcp.
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

## Script behavior

Scripts should be reusable, explicit, and safe.

Before creating or modifying scripts:

1. Inspect existing scripts and services through ha-mcp.
2. Identify safety-sensitive actions.
3. Propose the script sequence and fields.
4. Ask for approval.
5. Apply through ha-mcp after approval.
6. Verify by reading back the script config.
7. Store exports under `home-assistant/scripts/exports/` when useful.

Do not run scripts unless explicitly approved.

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
- group

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

Do not delete automations, scripts, helpers, scenes, entities, labels, areas, dashboards, or dashboard resources without explicit confirmation.

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

Do not compile or upload firmware unless explicitly approved.

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

- MCP-created helpers/automations/scripts/dashboards: read back through ha-mcp and verify expected fields/entities/actions.
- Home Assistant YAML/packages/templates/scripts: run Home Assistant config check if available and approved.
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
- Home Assistant credentials

If a file appears to contain secrets, stop and warn before displaying or modifying that content.

## Response style

Be practical and concise.

When making changes, summarize:

- what was inspected
- files changed, if any
- Home Assistant objects created/modified, if any
- what changed
- validation or ha-mcp verification performed
- risks or follow-up actions
- where exports/snapshots were stored, if applicable

Avoid long explanations unless the user asks for them.
