# Connecting Codex to Home Assistant OS through ha-mcp

A repository does not directly connect to Home Assistant OS. The connection path is:

```text
Codex client
→ ha-mcp MCP server
→ Home Assistant OS
```

## Recommended Home Assistant OS pattern

For HAOS, use the ha-mcp add-on pattern:

1. Install/run the Home Assistant MCP Server add-on in Home Assistant OS.
2. Open the add-on logs and copy the MCP URL shown by the add-on.
3. Add that MCP URL to your user-level Codex configuration if your Codex version supports HTTP MCP servers.
4. Keep private URLs and credentials outside this repository.
5. Use this repo's `AGENTS.md`, skills, and prompts to constrain Codex behavior.

## Local workstation pattern

Alternatively, run ha-mcp locally on the workstation where Codex runs.

Use the `uvx ha-mcp@latest` style only from your local user configuration. Do not store credentials in this repo.

## What this repo should store

Store:

- safety rules
- prompts
- skills
- dashboard plans
- helper/automation/script exports
- rollback notes
- optional package YAML

Do not store:

- credentials
- tokens
- private webhook URLs
- Home Assistant `.storage`
- logs, databases, backups, or generated files

## Validation after connection

After Codex can see ha-mcp, the first safe prompt is:

```text
Use ha-mcp read-only discovery only. Can you see my Home Assistant? List available ha-mcp tool families, then get a high-level overview. Do not change anything.
```

The expected result is a read-only summary. No devices should be controlled and no Home Assistant objects should be changed.
