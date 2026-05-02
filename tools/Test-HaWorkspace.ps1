<#
.SYNOPSIS
Checks the Home Assistant Codex workspace structure.

.DESCRIPTION
This script checks local repo files only. It does not connect to Home Assistant,
call ha-mcp, manage Supervisor/add-ons, or handle credentials.
#>

[CmdletBinding()]
param(
  [string]$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
)

$ErrorActionPreference = 'Stop'

$requiredPaths = @(
  'AGENTS.md',
  'README.md',
  'USER.md',
  'MEMORY.md',
  'SOUL.md',
  'skills-lock.json',
  '.codexignore',
  '.gitignore',
  '.agents/skills/home-assistant-best-practices/SKILL.md',
  '.agents/skills/home-assistant-dashboard-designer/SKILL.md',
  '.agents/skills/ha-mcp-workflow-tools/SKILL.md',
  'home-assistant/AGENTS.md',
  'esphome/AGENTS.md'
)

$recommendedDirs = @(
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

$findings = New-Object System.Collections.Generic.List[string]

foreach ($path in $requiredPaths) {
  $fullPath = Join-Path $Root $path
  if (-not (Test-Path $fullPath)) {
    $findings.Add("MISSING required path: $path")
  }
}

foreach ($path in $recommendedDirs) {
  $fullPath = Join-Path $Root $path
  if (-not (Test-Path $fullPath -PathType Container)) {
    $findings.Add("MISSING recommended directory: $path")
  }
}

$skillsLockPath = Join-Path $Root 'skills-lock.json'
if (Test-Path $skillsLockPath) {
  try {
    $skillsLock = Get-Content $skillsLockPath -Raw | ConvertFrom-Json
    foreach ($skillName in $skillsLock.skills.PSObject.Properties.Name) {
      $skill = $skillsLock.skills.$skillName
      $skillPath = Join-Path $Root $skill.path
      if (-not (Test-Path $skillPath -PathType Container)) {
        $findings.Add("Skill path missing for $skillName: $($skill.path)")
      }
      elseif (-not (Test-Path (Join-Path $skillPath 'SKILL.md'))) {
        $findings.Add("Skill missing SKILL.md: $skillName")
      }
    }
  }
  catch {
    $findings.Add("skills-lock.json is invalid JSON: $($_.Exception.Message)")
  }
}

if ($findings.Count -gt 0) {
  Write-Host 'Workspace audit findings:'
  foreach ($finding in $findings) {
    Write-Host "- $finding"
  }
  exit 1
}

Write-Host 'Workspace audit passed.'
exit 0
