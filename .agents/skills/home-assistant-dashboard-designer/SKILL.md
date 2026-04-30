---
name: home-assistant-dashboard-designer
description: Use when designing, reviewing, creating, or modifying Home Assistant dashboards through MCP or the Home Assistant UI. This project uses UI-managed dashboards, not YAML dashboard files.
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
- preparing dashboard changes for MCP/UI application
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
- MCP-supported dashboard tools
- user-approved MCP dashboard modification actions

## MCP-first dashboard workflow

Use this workflow:

1. Use MCP to inspect existing dashboards, views, cards, areas, devices, labels, and entities.
2. Use MCP, HACS, dashboard resource inspection, or existing dashboard inspection to confirm which custom cards are installed.
3. Identify the current dashboard structure.
4. Propose a dashboard change plan.
5. Identify any safety-sensitive controls affected.
6. Ask for explicit approval before applying changes.
7. Apply only the approved changes through MCP-supported tools.
8. Verify the result through MCP.
9. Summarize what changed.

Do not modify dashboards without explicit approval.

## Allowed without confirmation

Read-only actions are allowed:

- inspect dashboards
- inspect views
- inspect cards
- inspect dashboard resources
- inspect installed/custom cards if available
- inspect entities used by cards
- inspect areas/devices/labels
- inspect entity states
- identify missing or unavailable entities
- recommend improvements

## Requires confirmation

Explicit approval is required before:

- creating dashboards
- deleting dashboards
- renaming dashboards
- creating views
- deleting views
- renaming views
- adding cards
- deleting cards
- moving cards
- modifying cards
- changing dashboard visibility
- changing dashboard layout
- changing controls for safety-sensitive devices
- adding a new custom card dependency
- using a stale/unmaintained custom card for critical controls

## Custom card behavior

This project may use custom dashboard cards.

Before using a custom card:

- Use MCP, HACS, dashboard resource inspection, or existing dashboard inspection to confirm the custom card exists.
- Prefer built-in cards when they solve the problem cleanly.
- Use custom cards when they provide a clear dashboard benefit.
- Do not invent card syntax.
- Do not use stale or unmaintained cards for critical controls unless explicitly approved.

Use custom cards only when they improve:

- mobile usability
- status visibility
- safe control grouping
- conditional display
- diagnostics
- device-specific control
- visual clarity

Avoid custom cards when:

- a built-in Home Assistant card works well
- the card is only decorative
- the card is stale or unmaintained
- the card syntax is complex and fragile
- the card would hide safety-sensitive controls in unclear UI

## Preferred card priority

When designing dashboards, prefer cards in this order:

1. Built-in Home Assistant cards.
2. Installed, maintained, widely used custom cards.
3. Advanced custom cards only when they clearly solve a problem.
4. New custom card dependencies only after explicit approval.

Useful built-in cards include:

- Tile
- Entities
- Button
- Conditional
- Gauge
- History graph
- Markdown
- Thermostat
- Alarm panel
- Picture glance

Useful custom cards may include:

- Mushroom
- Bubble Card
- auto-entities
- card-mod
- Battery State Card / Entity Row
- Navbar Card
- Vertical Stack In Card
- Stack In Card
- Config Template Card
- state-switch
- Custom Features for Home Assistant Cards
- status-card
- Gauge Card Pro
- Entity Progress Card
- area-card-plus
- Device Card
- Light Entity Card
- Simple Thermostat
- Weather Chart Card
- Horizon Card
- Firemote Card
- TV Remote Card
- Xiaomi Vacuum Map Card
- Purifier Card
- surveillance-card
- Custom Brand Icons
- Text Divider Row
- Entity Attributes Card
- Mail and Packages Custom Card
- Roomba Vacuum Card

Do not assume any of these are installed. Confirm first.

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

For these, prefer:

- status-first layout
- confirmation where possible
- separation from common tap controls
- clear labels
- no hidden tap actions
- no accidental tap zones
- no stale/unmaintained cards unless explicitly approved

## Dashboard design principles

Dashboards should be:

- mobile-friendly
- area-based where useful
- function-based where useful
- clean
- readable
- useful at a glance
- safe to operate
- not overloaded
- not dependent on fragile entity names
- not dependent on unnecessary custom card complexity

## Preferred dashboard structure

Good high-level views:

- Home
- Security
- Garage
- Climate
- Lighting
- Cameras
- Network
- Maintenance
- Automations

## Card design principles

Cards should:

- answer a clear question
- group related entities
- avoid duplicate controls
- avoid dangerous controls near common controls
- show alerts prominently
- keep diagnostics lower on the page
- use friendly names without hiding the real entity IDs from review
- use custom styling sparingly
- keep family-facing dashboards simple

## Dashboard change proposal format

Before applying a dashboard change, provide a proposal with:

- dashboard name
- views affected
- cards to add/change/remove
- entities involved
- custom cards required
- whether each custom card is confirmed installed
- safety-sensitive controls affected
- fallback built-in card option if a custom card is unavailable

Example:

```text
Dashboard: Home
View: Garage

Proposed changes:
- Add a garage status section.
- Add a status-first garage door card.
- Add garage temperature and freezer temperature cards.
- Add conditional alert card for garage door left open.

Custom cards:
- Mushroom: confirmed installed / not confirmed
- auto-entities: confirmed installed / not confirmed

Safety-sensitive controls:
- Garage door cover entity.
- Proposed as status-first. Control card requires approval.

Fallback:
- Use built-in Tile and Entities cards if Mushroom is unavailable.
```

## Reference files

When relevant, consult:

- `references/dashboard-layouts.md`
- `references/dashboard-card-patterns.md`
- `references/dashboard-safety.md`
- `references/dashboard-mcp-workflow.md`
- `references/custom-cards.md`
- `references/custom-card-repos.md`

Do not load every reference unless needed.

## Response style

When working on dashboards, summarize:

- dashboard inspected
- views inspected
- proposed changes
- custom cards needed
- custom cards confirmed installed
- fallback options
- safety-sensitive controls affected
- approval needed before applying
- validation after applying
