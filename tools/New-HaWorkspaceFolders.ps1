<#
.SYNOPSIS
Creates the recommended repository folder skeleton.

.DESCRIPTION
This script modifies local repository folders only. It does not connect to Home
Assistant, call ha-mcp, manage Supervisor/add-ons, or handle credentials.
#>

[CmdletBinding(SupportsShouldProcess)]
param(
  [string]$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
)

$ErrorActionPreference = 'Stop'

$directories = @(
  '.codex/prompts',
  '.codex/agents',
  'docs',
  'tools',
  'home-assistant/automations/exports',
  'home-assistant/helpers/exports',
  'home-assistant/scripts/exports',
  'home-assistant/dashboards/plans',
  'home-assistant/packages',
  'esphome/devices',
  'esphome/packages',
  'esphome/common'
)

foreach ($directory in $directories) {
  $path = Join-Path $Root $directory
  if ($PSCmdlet.ShouldProcess($path, 'Create directory')) {
    New-Item -ItemType Directory -Path $path -Force | Out-Null
  }
}

Write-Host 'Recommended workspace folders are present.'
