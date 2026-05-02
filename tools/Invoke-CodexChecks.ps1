<#
.SYNOPSIS
Runs safe local Codex workspace checks.

.DESCRIPTION
This script is a PowerShell wrapper for the repo-local helper scripts. It does
not connect to Home Assistant, call ha-mcp, manage add-ons, reload Home
Assistant, or control devices.
#>

[CmdletBinding()]
param(
  [string]$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path,
  [switch]$SkipYaml,
  [switch]$SkipIndex,
  [string]$Python = 'python'
)

$ErrorActionPreference = 'Stop'

Push-Location $Root
try {
  $arguments = @('tools/run_codex_checks.py')

  if ($SkipYaml) {
    $arguments += '--skip-yaml'
  }

  if ($SkipIndex) {
    $arguments += '--skip-index'
  }

  & $Python @arguments
  exit $LASTEXITCODE
}
finally {
  Pop-Location
}
