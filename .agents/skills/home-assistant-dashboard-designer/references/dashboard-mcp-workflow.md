# Dashboard MCP Workflow

## Purpose

Use MCP for dashboard discovery and dashboard changes.

Do not use repository scans to discover UI-managed dashboards.

Do not edit `.storage`.

## Workflow

1. Inspect dashboards through MCP.
2. Inspect available views.
3. Inspect cards in the target view.
4. Inspect entities used by the cards.
5. Inspect areas/devices/labels for better grouping.
6. Propose changes.
7. Wait for explicit approval.
8. Apply changes through MCP-supported dashboard tools.
9. Verify the dashboard after changes.

## Read-only actions

Allowed without confirmation:

- list dashboards
- list views
- inspect cards
- inspect card entities
- inspect areas
- inspect devices
- inspect labels
- inspect current states

## Write actions

Require explicit confirmation:

- create dashboard
- delete dashboard
- rename dashboard
- create view
- delete view
- rename view
- add card
- edit card
- delete card
- move card
- change visibility
- change layout

## Approval wording

Before applying, clearly state:

```text
I can apply this dashboard change through MCP. It will create/update these views/cards:
- ...
This affects these safety-sensitive controls:
- ...
Please confirm before I apply it.
```

## After applying

Verify:

- dashboard exists
- target view exists
- expected cards exist
- referenced entities exist
- safety-sensitive controls are placed intentionally
