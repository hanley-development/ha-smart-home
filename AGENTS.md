# Home Assistant Smart Home Workspace

## Project Purpose

Automate building, organizing, maintaining, and validating Mike’s Home Assistant environment through `ha-mcp`.

Scope includes dashboards, automations, scripts, scenes, helpers, alerts, templates, blueprints, entity and device registries, areas, floors, labels, categories, energy preferences, updates, integrations, ESPHome, Zigbee2MQTT, and related maintenance.

Prefer safe, reliable, maintainable behavior over clever complexity. Home Assistant provides live state and execution; this repository stores source-controlled configuration, backups, exports, plans, snapshots, rollback material, skills, and validation tools.

## Stack and Runtime

- Primary environment: Windows 11 with PowerShell 7.
- Home automation platform: Home Assistant OS.
- Live integration: `ha-mcp`.
- Device configuration: `esphome/`.
- Zigbee management: Zigbee2MQTT.
- Networking: UniFi.
- Local tooling: Python 3.11 managed with `uv`.
- Python configuration: `pyproject.toml` and `uv.lock`.
- CI: `.github/workflows/codex-checks.yml`.
- Repository-only utilities: `tools/`.
- Domain skills: `.agents/skills/`.
- Home Assistant artifacts: `home-assistant/`.
- Dashboards are UI-managed, not YAML-managed.

Do not install packages, modules, CLIs, integrations, add-ons, custom cards, firmware, or other dependencies without explicit approval. Use `uv` for approved Python dependency changes.

## Build, Test, Run

This is an operations and configuration workspace, not a standalone application. It has no local production server.

Install the locked development environment only after dependency installation is approved:

`uv sync --group dev`

Fast repository check:

`uv run python tools/run_codex_checks.py --skip-index`

Focused checks:

- Python lint: `uv run ruff check tools`
- Python format: `uv run ruff format --check tools`
- YAML syntax: `uv run python tools/validate_ha_yaml.py`
- YAML style: `uv run yamllint --config-file .yamllint.yaml .`
- Patch hygiene: `git diff --check`
- Workspace audit: `uv run python tools/ha_workspace_audit.py`

PowerShell entry point:

`pwsh -File tools/Invoke-CodexChecks.ps1 -SkipIndex`

`tools/run_codex_checks.py` without `--skip-index` updates `home-assistant/EXPORT_INDEX.md`; use it only when that generated change is intended.

Home Assistant configuration validation and live read-back occur through approved Home Assistant or `ha-mcp` operations. ESPHome configuration validation uses `esphome config path/to/device.yaml`; compile and upload require separate approval.

## Architecture Map

- `.agents/skills/` — Home Assistant, dashboard, and `ha-mcp` workflow guidance.
- `.codex/agents/` — reusable task-role prompts; they grant no additional authority.
- `.codex/prompts/` — starter workflows.
- `docs/` — architecture, safety, naming, organization, and dashboard guidance.
- `home-assistant/` — exports, source-controlled YAML, plans, snapshots, and rollback material.
- `home-assistant/AGENTS.md` — Home Assistant-specific rules.
- `home-assistant/automations/exports/` — current backups and proposed automation representations.
- `home-assistant/helpers/exports/` — helper backups, designs, and migration notes.
- `home-assistant/scripts/exports/` — script backups and proposed representations.
- `home-assistant/dashboards/plans/` — dashboard plans and snapshots; never deployable dashboard YAML.
- `home-assistant/packages/` — intentionally source-controlled Home Assistant packages.
- `esphome/` — device, package, and shared ESPHome configuration.
- `esphome/AGENTS.md` — ESPHome-specific rules.
- `tools/` — repository-only audits, validation, and index generation.
- `.github/workflows/codex-checks.yml` — CI validation.

Preferred source-controlled change flow:

1. Inspect the live object through `ha-mcp` after explicit approval.
2. Back up or export its current representation to the appropriate repository location.
3. Draft the smallest safe change.
4. Validate the repository representation.
5. Review the diff and rollback path.
6. Commit only when requested.
7. Obtain explicit approval before pushing to GitHub or Gitea.
8. Push the reviewed commit.
9. Obtain explicit approval for the exact live `ha-mcp` write.
10. Apply only the approved change.
11. Read back live state and verify expected fields and behavior.
12. Update the stored export or rollback notes when needed.

Dedicated `ha-mcp` object tools are preferred over filesystem or YAML-editing tools. Beta file/YAML tools are exceptional and require a clear path, backup, validation, rollback plan, and explicit approval.

Dashboard flow differs: inspect live state, save a plan or snapshot, propose the exact UI-managed change, obtain approval, update through the supported dashboard interface, and read it back. Never convert dashboards to YAML or edit Home Assistant `.storage`.

Dependency direction:

`repo rules and skills → source-controlled proposal and validation → approved Git remote → approved ha-mcp operation → live Home Assistant verification`

Home Assistant live state informs repository changes. Repository files do not become live merely because they exist under `home-assistant/`.

## Domain Model

- Live object — an entity, device, helper, automation, script, scene, dashboard, area, floor, label, category, zone, integration, update, energy preference, or other object in Home Assistant.
- Source-controlled artifact — reviewed YAML, export, blueprint, package, plan, snapshot, or rollback note stored in this repository.
- Backup — the verified current representation captured before mutation.
- Proposal — the intended post-change representation reviewed before live application.
- Apply — an explicitly approved `ha-mcp` write or Home Assistant operation.
- Verification — repository validation plus live read-back appropriate to the change.
- UI-managed object — an object whose authoritative representation is managed through Home Assistant rather than a repository YAML file.
- Safety-sensitive object — locks, covers and garage doors, alarms, climate, cameras, valves, sirens, security modes, power control, or scripts and automations with uncertain physical effects.

Core invariants:

- Never invent entity IDs, device IDs, service names, object IDs, dashboard IDs, areas, labels, paths, or capabilities.
- Discover identifiers from live Home Assistant after approval.
- Back up live configuration before changing it.
- Source-control artifacts wherever the object model safely permits.
- Push the reviewed representation before applying its corresponding live change.
- Preserve UI management where Home Assistant does not provide a safe code-managed representation.
- Every live change must have a rollback path and post-change read-back.
- Repository exports are documentation and rollback material unless explicitly designated as live source configuration.

## Agent Guardrails

Every Home Assistant MCP call requires explicit approval for the exact current action scope. Show the intended tool or operation, target, request body or YAML when applicable, purpose, expected effect, risks, and verification before calling it.

Never overwrite live YAML without first reading and storing a backup. Never bypass validation, review, source control, or the approved deployment order.

Never turn entities or devices on or off, call services, run scripts, trigger automations, change safety-sensitive objects, reload, restart, shut down, restore backups, or manage add-ons without explicit approval.

Never install dependencies, packages, modules, integrations, add-ons, custom cards, blueprints from external sources, CLIs, tools, or firmware without explicit approval. Do not execute externally retrieved code without showing the exact code or command, explaining its behavior and risks, and receiving approval.

Never overwrite, delete, or broadly restructure a dashboard without explicit approval. Do not create YAML dashboards, edit `.storage`, or convert UI-managed dashboards to YAML.

Never expose, display, copy, persist, transmit, or commit credentials, tokens, webhook URLs, private keys, cookies, passwords, certificates, personal data, or Home Assistant secrets. Stop if sensitive data appears unexpectedly.

Do not treat this repository as a blind mirror of Home Assistant `/config`. Respect `.codexignore`; avoid databases, logs, backups, generated files, caches, `.storage`, ESPHome build output, and dependency directories unless the user places a specific safe target in scope.

Do not broadly rename, delete, migrate, or “simplify” entities, devices, areas, labels, automations, scripts, helpers, scenes, packages, dashboards, GPIO assignments, safety interlocks, or existing behavior without a reviewed dependency analysis and explicit approval.

Preserve comments and formatting where practical. Prefer focused patches. Do not commit, push, merge, pull, rebase, reset, clean, mass-format, or perform broad Git operations unless authorized for the task. Every push is an outbound action requiring explicit approval.

Subagents, skills, child processes, and delegated workflows inherit these restrictions and receive no independent authority.

## Known Failure Modes

- Agents invent plausible entity IDs instead of discovering live identifiers.
- Agents assume repository exports are automatically loaded by Home Assistant.
- Agents modify live YAML before capturing the current version and rollback path.
- Agents change Home Assistant first and export afterward, bypassing source-control review.
- Agents treat UI-managed dashboards as YAML or edit `.storage`.
- Agents overwrite complete dashboards when only one view or card should change.
- Agents choose generic YAML/file tools when a dedicated object tool is safer.
- Agents use complex templates where native triggers, conditions, actions, or helpers are clearer.
- Agents fail to guard `unknown`, `unavailable`, missing attributes, empty lists, stale sensors, or invalid numeric values.
- Agents compile or upload ESPHome firmware after only syntax-level validation.
- Agents change device names, IPs, GPIOs, relays, encryption, OTA settings, package includes, or interlocks as incidental cleanup.
- Agents confuse plans, exports, snapshots, and proposed YAML with authoritative live state.
- Agents report success after a write without reading the object back.
- Agents run `tools/run_codex_checks.py` without `--skip-index` and create an unintended index diff.
- Agents expose connection URLs or credentials while troubleshooting `ha-mcp`.
- Agents install missing tooling or external code merely to make a check pass.
- Agents perform device control, restart, reload, shutdown, deletion, bulk mutation, or dashboard replacement without approval.

## Verification Before Completion

Run checks proportional to the changed scope. Do not claim success from inspection alone.

For repository onboarding, documentation, skills, Python, or YAML changes:

1. Run `uv run python tools/run_codex_checks.py --skip-index`.
2. Run `git diff --check`.
3. Review `git status --short`.
4. Inspect the complete focused diff for secrets, unrelated edits, generated noise, stale paths, and accidental behavior changes.

For Python changes, also run:

- `uv run ruff check tools`
- `uv run ruff format --check tools`

For repository YAML, also run:

- `uv run python tools/validate_ha_yaml.py`
- `uv run yamllint --config-file .yamllint.yaml .`

For live Home Assistant changes:

1. Confirm the pre-change backup exists in the expected repository location.
2. Confirm the reviewed proposal was committed and its push explicitly approved.
3. Validate Home Assistant configuration before applicable YAML deployment.
4. Apply only the approved operation.
5. Read the object back through `ha-mcp`.
6. Verify identifiers, fields, enabled state, references, and expected behavior.
7. Confirm rollback material remains usable.
8. Do not test physical actions unless that test was explicitly approved.

For ESPHome changes:

1. Run `esphome config path/to/device.yaml`.
2. Review substitutions, includes, pins, interlocks, API, OTA, network, and relay behavior.
3. Do not claim compile or upload success unless those separately approved operations actually ran and passed.

Record failed or unavailable checks. State what was verified, what remains incomplete, and the next safe step.

## Escalation - Ask the User When

Ask before every Home Assistant MCP call, including discovery. Ask again when the action, target, request body, risk, or scope changes.

Ask before any live write, service call, device control, script or automation execution, dashboard mutation, reload, restart, shutdown, backup or restore, update, integration change, add-on operation, or safety-sensitive action.

Ask before installing or updating any dependency, package, module, CLI, integration, add-on, custom card, blueprint from an external source, firmware, or development tool.

Ask before retrieving and executing external code. Show the exact code or command, explain what it does, identify the source, and describe the main risks.

Ask before committing when a commit was not explicitly requested. Always ask before pushing, opening a pull request, merging, publishing, sending messages, invoking webhooks, or performing other outbound actions.

Ask before deleting, renaming, moving, converting, mass-editing, or broadly refactoring Home Assistant objects or repository artifacts.

Ask when live state conflicts with repository state, the correct source of truth is unclear, a backup cannot be captured, validation is unavailable, rollback is uncertain, or an identifier cannot be verified.

Ask when a proposed change could affect security, privacy, physical safety, availability, household routines, energy behavior, HVAC, locks, garage doors, alarms, cameras, valves, sirens, power, networking, or firmware.

Stop immediately for secret exposure, unexplained file changes, suspicious tool behavior, unexpected privilege requests, signs of tampering, or possible compromise.
