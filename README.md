# Home Assistant Smart Home Workspace

This repository is a Codex-friendly workspace for improving a Home Assistant setup with ha-mcp.

The repository is **not** intended to be a blind mirror of the Home Assistant `/config` directory. Home Assistant
remains the source of truth for normal UI-managed objects, and ha-mcp is used for live discovery and safe,
approval-gated writes.

## Goals

Use this workspace to improve:

- areas, labels, floors, categories, and entity naming
- helper selection and helper cleanup
- automations, scripts, scenes, blueprints, and templates
- dashboard planning and UI-managed dashboard changes
- ESPHome configuration review and validation
- custom card planning and dashboard resource review
- Home Assistant health, update, energy, network, and maintenance views
- durable exports, snapshots, rollback notes, and design docs

## Operating model

```text
Codex reads repo rules and skills
→ Codex uses ha-mcp for live Home Assistant discovery
→ Codex proposes the smallest safe change
→ user approves write/control actions
→ Codex applies approved changes through ha-mcp or edits repo files
→ Codex verifies through ha-mcp or targeted validation
→ repo stores plans/exports/snapshots when useful
```

Read-only ha-mcp discovery is allowed. Writes, live device control, reloads, restarts, deletions, and safety-sensitive changes require explicit approval.

## Repository structure

```text
.
├─ AGENTS.md
├─ README.md
├─ USER.md
├─ MEMORY.md
├─ SOUL.md
├─ skills-lock.json
├─ .codexignore
├─ .gitignore
├─ .codex/
│  ├─ README.md
│  ├─ config.toml.example
│  ├─ agents/
│  │  ├─ automation-builder.md
│  │  ├─ dashboard-designer.md
│  │  ├─ entity-organizer.md
│  │  ├─ ha-mcp-operator.md
│  │  └─ reviewer.md
│  └─ prompts/
│     ├─ 01-inventory-overview.md
│     ├─ 02-dashboard-master-plan.md
│     ├─ 03-area-dashboard.md
│     ├─ 04-helper-design.md
│     ├─ 05-automation-build.md
│     ├─ 06-script-build.md
│     ├─ 07-custom-card-visuals.md
│     ├─ 08-energy-weather-network.md
│     ├─ 09-ha-health-maintenance.md
│     └─ 10-safe-refactor-review.md
├─ .agents/
│  └─ skills/
│     ├─ home-assistant-best-practices/
│     ├─ home-assistant-dashboard-designer/
│     └─ ha-mcp-workflow-tools/
├─ docs/
│  ├─ codex-workflows.md
│  ├─ ha-mcp-connection.md
│  └─ starter-prompts.md
├─ tools/
│  ├─ build_export_index.py
│  ├─ ha_workspace_audit.py
│  ├─ validate_ha_yaml.py
│  ├─ New-HaWorkspaceFolders.ps1
│  └─ Test-HaWorkspace.ps1
├─ home-assistant/
│  ├─ AGENTS.md
│  ├─ automations/
│  │  └─ exports/
│  ├─ helpers/
│  │  └─ exports/
│  ├─ scripts/
│  │  └─ exports/
│  ├─ dashboards/
│  │  └─ plans/
│  └─ packages/
└─ esphome/
   ├─ AGENTS.md
   ├─ devices/
   ├─ packages/
   └─ common/
```

## Important files

- `AGENTS.md` — root rules Codex should follow in this repo.
- `USER.md` — durable user preferences and environment notes.
- `MEMORY.md` — stable project constraints and memory.
- `SOUL.md` — short project principles.
- `skills-lock.json` — enabled skills.
- `.codexignore` — files Codex should avoid reading.
- `.codex/config.toml.example` — safe reference for Codex MCP configuration. Keep real config and private URLs out of the repo.
- `.codex/prompts/` — starter prompts for common Home Assistant + ha-mcp tasks.
- `.codex/agents/` — reusable role prompts for subagent-style Codex workflows.
- `tools/` — local repo hygiene and validation helpers. These do not connect to Home Assistant.

## Skills

Skills live under `.agents/skills/` and are enabled by `skills-lock.json`.

Current skills:

```text
home-assistant-best-practices
home-assistant-dashboard-designer
ha-mcp-workflow-tools
```

Use them this way:

| Task | Skill |
| --- | --- |
| Automation, helper, template, package, ESPHome review | `home-assistant-best-practices` |
| Dashboard layout, custom cards, Lovelace safety | `home-assistant-dashboard-designer` |
| Safe ha-mcp tool selection and workflow | `ha-mcp-workflow-tools` |

Do not load every reference file by default. Load only the references needed for the current task.

## How actions are called

There are three distinct action paths:

1. **Repo edits** — Codex edits Markdown, YAML exports, helper scripts, skills, prompt files, and optional package YAML in this repository.
2. **ha-mcp read-only tools** — Codex discovers live Home Assistant state, entities, helpers, automations, dashboards, resources, logs, traces, updates, and health.
3. **ha-mcp write/control tools** — Codex creates, updates, deletes, reloads, restarts, or controls Home Assistant objects only after explicit user approval.

Preferred ha-mcp tool families:

| Need | Preferred tool family |
| --- | --- |
| Find entities/devices/states | `ha_search_entities`, `ha_get_state`, `ha_get_entity`, `ha_get_device`, `ha_get_overview` |
| Helpers | `ha_config_list_helpers`, `ha_get_helper_schema`, `ha_config_set_helper` |
| Automations | `ha_config_get_automation`, `ha_config_set_automation`, `ha_get_automation_traces` |
| Scripts | `ha_config_get_script`, `ha_config_set_script` |
| Dashboards/resources | `ha_config_get_dashboard`, `ha_config_set_dashboard`, `ha_config_list_dashboard_resources` |
| Areas/floors/labels/categories | `ha_config_list_areas`, `ha_list_floors_areas`, `ha_config_get_label`, `ha_config_set_label` |
| Services/live control | `ha_list_services`, `ha_call_service`, `ha_bulk_control`, `ha_get_operation_status` |
| Health/updates | `ha_get_system_health`, `ha_get_updates`, `ha_check_config` |
| HACS/custom cards | `ha_hacs_search`, `ha_hacs_repository_info`, `ha_config_list_dashboard_resources` |

## Home Assistant OS connection model

A repo does not directly connect to Home Assistant OS. Codex connects to ha-mcp, and ha-mcp connects to Home Assistant.

For Home Assistant OS, the safest pattern is:

```text
Home Assistant OS add-on runs ha-mcp
→ add-on exposes an MCP URL
→ Codex config points at that MCP URL
→ repo rules tell Codex how to use the tools safely
```

Keep private URLs, tokens, and credentials outside this repository.

See `docs/ha-mcp-connection.md`.

## Dashboard policy

Dashboards are UI-managed in this project.

Do not:

- create dashboard YAML files by default
- edit `.storage`
- convert UI dashboards to YAML
- assume dashboard source files exist in the repo

Dashboard work should use ha-mcp/UI-supported dashboard tools, with plans and snapshots stored under:

```text
home-assistant/dashboards/plans/
```

## Export locations

Use these folders for durable review and rollback references:

```text
home-assistant/automations/exports/
home-assistant/helpers/exports/
home-assistant/scripts/exports/
home-assistant/dashboards/plans/
home-assistant/packages/
```

Files under `home-assistant/` are not automatically live-loaded by Home Assistant unless explicitly documented.

## Local helper scripts

These scripts operate on the repository only. They do not connect to Home Assistant and do not handle tokens.

```bash
python tools/ha_workspace_audit.py
python tools/validate_ha_yaml.py
python tools/build_export_index.py
```

PowerShell alternatives:

```powershell
./tools/Test-HaWorkspace.ps1
./tools/New-HaWorkspaceFolders.ps1
```

## Recommended validation

Use the narrowest validation available:

- repo structure: `python tools/ha_workspace_audit.py`
- repo YAML syntax: `python tools/validate_ha_yaml.py`
- helper/automation/script/dashboard created by MCP: read back through ha-mcp and verify IDs/fields
- Home Assistant YAML/packages: Home Assistant config check before reload
- ESPHome YAML: `esphome config path/to/device.yaml` before compile/upload

Do not reload, restart, upload firmware, or control devices unless explicitly approved.

## Safety rules

Do not expose, print, modify, or commit secrets.

Sensitive items include passwords, API keys, long-lived access tokens, webhook URLs, private keys,
certificates, MQTT credentials, Wi-Fi credentials, and Home Assistant credentials.

If a file appears to contain secrets, stop and warn before displaying or modifying it.

## Starter prompts

See `docs/starter-prompts.md` and `.codex/prompts/` for copy/paste Codex prompts.
