# projectmem - ha-smart-home

_Last updated: 2026-06-20_

## Project purpose
This repository is a Codex-friendly workspace for improving Mike Hanley's Home Assistant setup with ha-mcp. It stores safety rules, workflow docs, skills, prompts, validation helpers, exports, snapshots, rollback notes, dashboard plans, and optional source-controlled YAML. Home Assistant remains the source of truth for normal UI-managed helpers, automations, scripts, scenes, dashboards, areas, labels, categories, and live entity state.

## Recent issues
- [DONE] #legacy_f0ac Legacy issue: Fix datetime import and usage in build_export_index.py -> Fix datetime import and usage in build_export_index.py (fixed)
- [DONE] #legacy_eebf Legacy issue: fix: resolve markdown linting errors -> fix: resolve markdown linting errors (fixed)
- [DONE] #legacy_50f2 Legacy issue: fix: resolve Markdown linting errors (line length, table formatting, blank lines) -> fix: resolve Markdown linting errors (line length, table formatting, blank lines) (fixed)
- [DONE] #0002 Git staging failed because sandbox cannot create .git/index.lock [.git/index.lock] -> Resolved staging blocker by running Git index writes with approved elevated permissions and command-scoped safe.directory. [.git/index.lock] (fixed)
- [DONE] #0001 summary.md Project purpose stayed placeholder after Setup Mode population pass [.projectmem/summary.md] -> Fixed Setup Mode placeholder by giving PROJECT_MAP.md an exact '## Project purpose' section and regenerating summary.md through projectmem events. [.projectmem/PROJECT_MAP.md] (fixed)
  - Partial attempt: Changed PROJECT_MAP.md heading from '## Project Purpose' to exact '## Project purpose' expected by projectmem regeneration. [.projectmem/PROJECT_MAP.md]

## Decisions
- This repo is a Codex-friendly Home Assistant + ha-mcp workspace for docs, prompts, skills, exports, snapshots, rollback notes, and optional YAML; it is not a blind mirror of Home Assistant /config. [README.md]
- Home Assistant remains the source of truth for normal UI-managed objects; use ha-mcp for live discovery and approval-gated writes to helpers, automations, scripts, dashboards, and organization objects. [AGENTS.md]
- Dashboard work is UI-managed by default: do not create YAML dashboard files, edit .storage, or convert dashboards to YAML; store plans and snapshots under home-assistant/dashboards/plans/. [home-assistant/dashboards/]
- Repo validation is Python 3.11 oriented with Ruff, yamllint, markdownlint, pytest config, and tools/run_codex_checks.py as the combined safe local check runner. [pyproject.toml]
- Repo-local helper scripts must not connect to Home Assistant, call ha-mcp, read credentials, reload/restart Home Assistant, manage add-ons, or control devices. [tools/README.md]
- Source-controlled Home Assistant artifacts are stored as review/rollback exports under home-assistant/automations/exports, helpers/exports, scripts/exports, dashboards/plans, and optional packages; these files are not automatically live-loaded unless explicitly documented. [home-assistant/]

## Notes
- Ignore Obsidian workspace metadata
- Stop tracking Obsidian workspace metadata
- Add humidity fan control blueprint
- Add template helper migration export note
- Remove repository MCP config example
- gotcha: validate_ha_yaml.py requires PyYAML and supports Home Assistant custom tags such as !input by adding a permissive multi-constructor. [tools/validate_ha_yaml.py]
- gotcha: Home Assistant MCP connection details, private URLs, tokens, and credentials must stay in user-level config or HA add-on config, not in this repository. [docs/ha-mcp-connection.md]
- Setup pass populated PROJECT_MAP.md with the Home Assistant + ha-mcp workspace purpose, stack, folder roles, important files, storage locations, first reads, and safety boundaries. [.projectmem/PROJECT_MAP.md]
- gotcha: PROJECT_MAP.md must use exact heading '## Project purpose' for projectmem summary regeneration to copy the purpose text. [.projectmem/PROJECT_MAP.md]
- gotcha: Git commands may fail in the Codex sandbox with dubious ownership because the repo is owned by MARVIN/hanle but commands run as MARVIN/CodexSandboxOffline; do not add global safe.directory without user approval. [C:/scripts/ha-smart-home]

## Key files
- `.editorconfig`
- `pyproject.toml`
- `.yamllint.yaml`
- `.markdownlint.yaml`
- `.pre-commit-config.yaml`
- `.github/workflows/codex-checks.yml`
- `AGENTS.md`
- `build_export_index.py`
- `tools/build_export_index.py`
- `README.md`
- `docs/automation-patterns.md`
- `docs/mcp-safety.md`
- `tools/README.md`
- `.gitignore`
- `.obsidian/app.json`
- `.obsidian/appearance.json`
- `.obsidian/community-plugins.json`
- `.obsidian/core-plugins.json`
- `.obsidian/plugins/obsidian-git/main.js`
- `.obsidian/plugins/obsidian-git/manifest.json`

## Open questions
- None logged yet.
