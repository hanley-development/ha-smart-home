# Dashboard Style Guide

## Important

This project uses UI-managed Home Assistant dashboards.

Do not create YAML dashboard files.

Do not edit `.storage`.

Do not convert UI-managed dashboards to YAML.

Dashboard work should be done through:

- Home Assistant UI
- MCP-supported dashboard tools, if available
- proposed card snippets for manual paste into the UI

## Goals

Dashboards should be:

- clean
- mobile-friendly
- useful at a glance
- grouped by area or function
- fast to understand
- safe to operate
- not overloaded with rarely used controls

## Preferred dashboard sections

Useful dashboard sections include:

- Home overview
- Security
- Garage
- Climate
- Lighting
- Cameras
- Network
- Batteries
- Maintenance
- Automations
- Alerts

## Mobile-first layout

Prioritize mobile usability.

Recommended pattern:

1. Status summary
2. Critical alerts
3. Area controls
4. Frequently used actions
5. Detailed diagnostics lower down

## Safety-sensitive controls

Require extra care for:

- locks
- garage doors
- alarm systems
- HVAC
- cameras
- security modes
- water shutoff
- appliances

Prefer confirmation patterns where possible.
