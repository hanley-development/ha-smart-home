# MEMORY.md

## Stable project memory

This repository supports a Home Assistant + ha-mcp smart home ecosystem.

Core goals:

- Improve automations.
- Improve scripts.
- Improve templates.
- Improve helper usage.
- Improve entity organization.
- Improve areas and labels.
- Improve dashboard planning through MCP/UI-supported workflows.
- Improve ESPHome device consistency.
- Make the smart home easier to maintain.

## Important constraints

- Dashboards are UI-managed.
- Do not edit `.storage`.
- Do not create YAML dashboards unless explicitly instructed.
- Use ha-mcp for live entity/device/area/label/state discovery.
- Do not use repo-wide scans just to discover live Home Assistant state.
- Do not perform live control actions without explicit user approval.
- Prefer small, targeted diffs.
- Preserve existing working behavior.

## Cap-saving behavior

To reduce Codex usage:

- Read only files needed for the task.
- Use `.codexignore`.
- Avoid generated folders.
- Avoid Home Assistant database/log/cache files.
- Avoid ESPHome build artifacts.
- Avoid broad Git operations.
- Prefer ha-mcp discovery over repo search.