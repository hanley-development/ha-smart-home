# Tools

These scripts are safe, repo-local helpers for Codex and humans working in this Home Assistant + ha-mcp workspace.

They do **not** connect to Home Assistant, call ha-mcp, manage Supervisor or add-ons, reload Home Assistant, restart Home Assistant, or control devices.

## Recommended Codex check

Run all safe local checks:

```bash
python tools/run_codex_checks.py
```

On Windows PowerShell:

```powershell
./tools/Invoke-CodexChecks.ps1
```

## Scripts

| Script | Purpose |
| --- | --- |
| `ha_workspace_audit.py` | Checks required repo files, skill paths, ignore patterns, and recommended folders. |
| `validate_ha_yaml.py` | Validates YAML syntax for source-controlled Home Assistant, ESPHome, and skill artifacts. Requires PyYAML. |
| `build_export_index.py` | Rebuilds `home-assistant/EXPORT_INDEX.md` from repo export folders and dashboard plans. |
| `run_codex_checks.py` | Runs the audit, YAML validation, and export index generation in one command. |
| `Test-HaWorkspace.ps1` | PowerShell workspace audit equivalent. |
| `New-HaWorkspaceFolders.ps1` | Creates the recommended folder skeleton. |
| `Invoke-CodexChecks.ps1` | PowerShell wrapper around `run_codex_checks.py`. |

## When Codex should use these

Use these scripts after changing:

- `AGENTS.md`
- `.agents/skills/**`
- `.codex/**`
- `home-assistant/**`
- `esphome/**`
- repo ignore files
- helper scripts

Use Home Assistant's own checks for live configuration validation. These scripts only validate repo hygiene and syntax.
