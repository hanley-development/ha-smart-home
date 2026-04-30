# AGENTS.md

## Project purpose

This repository supports a Home Assistant + ha-mcp smart home project.

The goal is to improve Home Assistant automations, scripts, helpers, templates, packages, ESPHome devices, entity organization, areas, labels, dashboards, and MCP-assisted smart home workflows.

This project uses the Home Assistant MCP server for live discovery whenever possible.

## Operating model

Use this workflow:

1. Use MCP for live Home Assistant discovery.
2. Identify the smallest file set needed.
3. Edit only files explicitly named by the user, unless a directly referenced include/package must also be read.
4. Validate the change when possible.
5. Summarize changed files, validation performed, risks, and next steps.

Do not perform repo-wide discovery unless explicitly asked.

## MCP-first discovery

To reduce unnecessary repo scanning and avoid stale assumptions, use the Home Assistant MCP server for live discovery whenever possible.

Use MCP for:

- entity lookup
- device lookup
- area lookup
- label lookup
- state inspection
- automation inspection
- script inspection
- scene inspection
- dashboard inspection, if available
- service capability lookup

Do not scan the repository just to discover entities, areas, labels, devices, services, or current states.

Never use MCP to perform live control actions without explicit user approval.

Live control actions include, but are not limited to:

- turning devices on or off
- opening or closing garage doors
- locking or unlocking locks
- arming or disarming alarms
- changing HVAC modes or setpoints
- enabling, disabling, deleting, or renaming automations
- modifying dashboards
- changing helpers, labels, areas, or entities
- reloading Home Assistant
- restarting Home Assistant

Read-only MCP actions are allowed without confirmation.

## Dashboard agent behavior

This project uses UI-managed dashboards and may use MCP to create or modify dashboards.

Use the `home-assistant-dashboard-designer` skill for dashboard-related tasks.

Dashboard source files are not expected in the repo.

Do not:

- create YAML dashboard files
- edit `.storage`
- convert UI dashboards to YAML
- make dashboard changes without explicit approval

Use MCP for dashboard discovery and MCP-supported dashboard changes.

For dashboard tasks:

1. Inspect the live dashboard structure through MCP.
2. Propose a layout/card plan.
3. Identify safety-sensitive controls.
4. Ask for approval.
5. Apply only the approved changes through MCP.
6. Verify the result.

## Context discipline

Codex should minimize context usage.

- Respect `.codexignore`.
- Do not scan the whole repository unless explicitly asked.
- Do not inspect `.storage`.
- Do not inspect logs, databases, backups, cache folders, generated files, dependency folders, or build output unless directly relevant.
- Prefer targeted edits to named files.
- Prefer small patches over full rewrites.
- Preserve existing comments and formatting where possible.
- Ask before broad refactors.
- Keep summaries concise.
- Do not invent entity IDs, device names, areas, labels, secrets, tokens, IPs, service calls, or file paths.

## Home Assistant rules

This project uses Home Assistant OS and UI-managed dashboards.

Dashboards are not YAML-managed.

Codex must not:

- create YAML dashboard files
- edit YAML dashboard files
- edit `.storage`
- convert UI-managed dashboards to YAML
- assume dashboard files exist in the repo

Codex may:

- inspect dashboards through MCP when available
- recommend dashboard layout improvements
- generate card snippets for manual use in the UI
- apply dashboard changes only through approved MCP/UI-supported tools and only after explicit confirmation

For Home Assistant YAML files, prefer safe, readable, maintainable changes.

Relevant YAML may include:

- automations
- scripts
- scenes
- packages
- template sensors
- binary sensors
- helpers, if represented in YAML
- groups
- input booleans
- input numbers
- input selects
- timers
- counters
- notification logic

Do not modify `secrets.yaml` unless explicitly instructed.

Do not delete automations, scripts, helpers, scenes, entities, labels, areas, or dashboard content without explicit confirmation.

## Automation standards

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

- Home Assistant YAML automations/packages/templates/scripts: run a Home Assistant config check if available.
- ESPHome YAML: run `esphome config <file>` before suggesting compile/upload.
- Python files: run targeted tests or syntax checks.
- Markdown/rules files: check for clarity and consistency.

Do not run long deployment, compile, upload, restart, or live-service commands unless explicitly asked.

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

- files changed
- what changed
- validation performed
- risks or follow-up actions

Avoid long explanations unless the user asks for them.
