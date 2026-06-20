# Project Map - ha-smart-home

## Project purpose

This repository is a Codex-friendly workspace for improving Mike Hanley's Home Assistant setup with ha-mcp. It stores safety rules, workflow docs, skills, prompts, validation helpers, exports, snapshots, rollback notes, dashboard plans, and optional source-controlled YAML. Home Assistant remains the source of truth for normal UI-managed helpers, automations, scripts, scenes, dashboards, areas, labels, categories, and live entity state.

## Operating Model

- Use ha-mcp for live read-only discovery of Home Assistant entities, devices, states, areas, labels, automations, scripts, dashboards, services, traces, logs, health, and updates when those details are needed.
- Require explicit user approval before any Home Assistant write/control action, including service calls, helper/automation/script/dashboard changes, reloads, restarts, add-on actions, firmware compile/upload, and safety-sensitive controls.
- Prefer repo edits for documentation, plans, exports, snapshots, rollback notes, optional packages, skills, prompts, and local validation tools.
- Store durable project knowledge through projectmem events; never edit `.projectmem/summary.md` or `.projectmem/events.jsonl` directly.

## Stack

- Primary domain: Home Assistant plus ha-mcp workflows.
- Primary environment: Windows 11, PowerShell 7 preferred.
- Python target: Python 3.11 for local helper scripts and tests.
- Local validation: `tools/run_codex_checks.py`, Ruff, yamllint, markdownlint, and pytest configuration.
- CI: GitHub Actions on `main` and pull requests, using Python 3.11 and Node.js 24.
- Skills: `home-assistant-best-practices`, `home-assistant-dashboard-designer`, and `ha-mcp-workflow-tools`.

## Main Folders

- `.agents/skills/` - local Home Assistant and ha-mcp workflow skills used by agents.
- `.codex/agents/` - role prompts for subagent-style task scopes such as automation builder, dashboard designer, entity organizer, ha-mcp operator, and reviewer.
- `.codex/prompts/` - starter prompts for common Home Assistant + ha-mcp workflows.
- `.github/workflows/` - CI checks for repo-local linting and validation.
- `docs/` - workflow and safety documentation, including MCP safety, automation patterns, HAOS connection guidance, and starter prompts.
- `tools/` - safe repo-local audit, YAML validation, export index, and PowerShell wrapper scripts. These do not connect to Home Assistant.
- `home-assistant/` - documentation, exports, snapshots, rollback references, dashboard plans, and optional package YAML. Files here are not automatically live-loaded unless explicitly documented.
- `esphome/` - ESPHome device, package, and common config workspace; validate with `esphome config` before compile/upload, and require approval for compile/upload.

## Important Files

- `AGENTS.md` - root operating rules, security requirements, Home Assistant routing, approval policy, validation guidance, and response style.
- `README.md` - project overview, repository structure, skills, ha-mcp action paths, connection model, dashboard policy, export locations, and recommended validation.
- `USER.md` - durable user preferences and local environment notes.
- `MEMORY.md` - stable project constraints and project-level memory.
- `SOUL.md` - compact project principles.
- `skills-lock.json` - enabled local skills and paths.
- `.codexignore` and `.gitignore` - files and patterns agents and Git should avoid, including secrets/noisy Home Assistant artifacts.
- `pyproject.toml` - Ruff, pytest, and dev dependency-group configuration.
- `.markdownlint.yaml`, `.yamllint.yaml`, `.pre-commit-config.yaml`, `.editorconfig` - repo formatting and linting rules.
- `tools/run_codex_checks.py` - combined safe local check runner for workspace audit, YAML validation, and export index generation.
- `tools/ha_workspace_audit.py` - checks required paths, enabled skills, ignore patterns, and sensitive/noisy file presence.
- `tools/validate_ha_yaml.py` - validates source-controlled HA/ESPHome/skill YAML syntax with support for Home Assistant custom tags.
- `tools/build_export_index.py` - rebuilds `home-assistant/EXPORT_INDEX.md` from exports and dashboard plans.
- `docs/mcp-safety.md` - read-only vs write/control MCP safety model and dangerous domains.
- `docs/automation-patterns.md` - preferred Home Assistant automation structure, modes, guards, and safety guidance.
- `docs/ha-mcp-connection.md` - safe connection patterns for Codex to reach Home Assistant OS through ha-mcp.

## Home Assistant Storage Areas

- `home-assistant/automations/exports/` - automation exports, proposed YAML, snapshots, and rollback references.
- `home-assistant/helpers/exports/` - helper exports, helper design notes, and rollback references.
- `home-assistant/scripts/exports/` - script exports and snapshots.
- `home-assistant/dashboards/plans/` - dashboard layout plans, card plans, resource notes, and snapshots.
- `home-assistant/packages/` - optional source-controlled YAML packages only when explicitly needed.

## Suggested First Reads

- For any task: `AGENTS.md`, then projectmem summary/map.
- For Home Assistant object work: relevant local skills plus `docs/mcp-safety.md`.
- For automations: `.agents/skills/home-assistant-best-practices/SKILL.md` and `docs/automation-patterns.md`.
- For dashboards: `.agents/skills/home-assistant-dashboard-designer/SKILL.md` and dashboard plans under `home-assistant/dashboards/plans/`.
- For ha-mcp connection questions: `docs/ha-mcp-connection.md`.
- For local repo validation: `tools/README.md` and `tools/run_codex_checks.py`.

## Safety Boundaries

- Do not inspect or expose secrets, tokens, private URLs, `.storage`, Home Assistant databases, logs, backups, or credentials unless explicitly instructed and safe.
- Do not control devices, call services, modify live Home Assistant objects, reload/restart Home Assistant, or compile/upload ESPHome firmware without explicit approval.
- Do not create YAML dashboard files or edit `.storage`; dashboards are UI-managed by default.
- Do not treat files under `home-assistant/` as live configuration unless a file explicitly documents that behavior.
