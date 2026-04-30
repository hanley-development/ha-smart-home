---
name: home-assistant-best-practices
description: Use when editing or reviewing Home Assistant YAML, automations, scripts, templates, helpers, packages, ESPHome YAML, Zigbee2MQTT-related configuration, dashboard recommendations, or ha-mcp smart home workflows.
---

# Home Assistant Best Practices Skill

## Purpose

Use this skill for Home Assistant and ESPHome work.

This skill helps with:

- automation design
- safe device control
- entity organization
- helper selection
- template sensors
- dashboard recommendations
- ESPHome config review
- MCP-safe workflows
- safe refactoring

## Read relevant references

When relevant, consult:

- `references/automation-patterns.md`
- `references/dashboard-cards.md`
- `references/dashboard-guide.md`
- `references/device-control.md`
- `references/domain-docs.md`
- `references/examples.yaml`
- `references/helper-selection.md`
- `references/safe-refactoring.md`
- `references/template-guidelines.md`
- `references/yaml-only-integrations.md`

Do not load every reference unless needed.

## Core rules

- Use MCP for live Home Assistant discovery.
- Do not invent entity IDs.
- Do not hand-edit `.storage`.
- Do not create YAML dashboards unless explicitly asked.
- Do not control live devices without explicit user approval.
- Prefer safe, reversible changes.
- Prefer small diffs.
- Validate YAML when possible.
- Preserve existing behavior unless explicitly changing it.

## Dashboard rule

Dashboards are UI-managed in this project.

For dashboards:

- inspect with MCP if available
- recommend layout/card changes
- generate snippets for manual UI use if requested
- do not edit dashboard YAML
- do not edit `.storage`

## Automation rule

Automations should handle:

- `unknown`
- `unavailable`
- stale sensors
- missing attributes
- notification spam
- unsafe automatic control
- reload safety

## ESPHome rule

Do not compile or upload firmware unless explicitly approved.

Use `esphome config` first when validating ESPHome YAML.
