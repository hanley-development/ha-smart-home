# Codex Workspace Notes

This folder contains Codex-facing helper material for this Home Assistant + ha-mcp workspace.

## Files

- `config.toml.example` — reference MCP configuration. Keep real private URLs and credentials out of the repo.
- `prompts/` — copy/paste starter prompts for common Home Assistant tasks.
- `agents/` — subagent-style role prompts. Use these as scoped task instructions when the Codex app supports agent/task delegation, or paste them into a normal prompt when it does not.

## How Codex should use this repo

1. Read `AGENTS.md` first.
2. Use `skills-lock.json` to understand enabled skills.
3. Use ha-mcp read-only tools for live Home Assistant discovery.
4. Propose changes before writes/control.
5. Use the local `tools/` scripts only for repo validation and hygiene.
6. Store durable exports, snapshots, and plans in `home-assistant/`.

## What not to store here

Do not commit:

- real Home Assistant MCP URLs if they expose private access
- tokens or credentials
- Home Assistant `.storage`
- secrets, backups, databases, logs, or generated build output
