---
name: home-assistant-dashboard-designer
description: Use when designing, reviewing, creating, or modifying Home Assistant dashboards through ha-mcp or the Home Assistant UI. This project uses UI-managed dashboards, not YAML dashboard files.
---

# Home Assistant Dashboard Designer Skill

## Purpose

Use this skill for Home Assistant dashboard work.

This includes:

- designing dashboards
- reviewing dashboard structure
- improving views
- improving cards
- organizing controls
- creating mobile-friendly layouts
- recommending card types
- preparing dashboard changes for ha-mcp/UI application
- safely using built-in and custom dashboard cards

## Important project rule

This project uses UI-managed dashboards.

Do not:

- create YAML dashboard source files
- edit YAML dashboard source files
- edit `.storage`
- convert UI-managed dashboards to YAML
- assume dashboard files exist in the repo

Dashboard changes should happen through:

- Home Assistant UI
- ha-mcp-supported dashboard tools
- user-approved ha-mcp dashboard modification actions

## MCP-first dashboard workflow

Use this workflow:

1. Use ha-mcp to inspect existing dashboards, views, cards, areas, devices, labels, and entities.
2. Use ha-mcp, HACS, dashboard resource inspection, or existing dashboard inspection to confirm which custom cards are installed.
3. Identify the current dashboard structure.
4. Propose a dashboard change plan.
5. Identify any safety-sensitive controls affected.
6. Ask for explicit approval before applying changes.
7. Apply only the approved changes through ha-mcp-supported tools.
8. Verify the result through ha-mcp.
9. Summarize what changed.

Do not modify dashboards without explicit approval.

## Custom card behavior

Before using a custom card:

- confirm the custom card exists
- prefer built-in cards when they solve the problem cleanly
- use custom cards when they provide a clear dashboard benefit
- do not invent card syntax
- do not use stale or unmaintained cards for critical controls unless explicitly approved

## Preferred card priority

1. Built-in Home Assistant cards.
2. Installed, maintained, widely used custom cards.
3. Advanced custom cards only when they clearly solve a problem.
4. New custom card dependencies only after explicit approval.

## Safety-sensitive controls

Be extra careful with cards that control:

- garage doors
- locks
- alarm systems
- cameras
- HVAC
- water valves
- sirens
- security devices

For these, prefer status-first layouts, clear labels, separated controls, and confirmation where supported.
