---
name: ha-mcp-workflow-tools
description: Use when operating Home Assistant through ha-mcp tools, including MCP discovery, helper creation, automation creation, dashboard changes, service calls, labels, areas, scripts, history, reviews, onboarding, and fallback/error handling. Complements home-assistant-best-practices by defining how agents should safely use MCP tools.
---

# ha-mcp Workflow Tools

## Purpose

Use this skill when working with Home Assistant through ha-mcp.

This skill defines safe MCP tool workflows for:

- discovery
- read-only inspection
- helper creation
- automation creation
- dashboard changes
- service calls
- reviews/debugging
- history/traces/logs
- areas, labels, floors, groups, and organization
- onboarding/inventory
- fallback/error handling

## Core rule

Use MCP for live Home Assistant discovery.

Use MCP for creating or modifying UI-managed Home Assistant objects only after explicit user approval.

Home Assistant is the source of truth for normal UI-managed objects.

The repo stores:

- plans
- exports
- snapshots
- rollback references
- optional source-controlled YAML only when explicitly needed

Do not create YAML packages by default.

Do not edit `.storage`.

Do not invent entity IDs.

Do not perform live device control without explicit approval.

## Safety-sensitive actions

Extra confirmation is required for anything involving:

- locks
- garage doors
- alarm systems
- HVAC
- cameras
- water valves
- sirens
- security devices
- bulk service calls
- reloads/restarts
- enabling/disabling automations
- deleting objects

## Workflow router

Use the relevant reference file for the task:

| Task | Reference |
|---|---|
| General ha-mcp rules | `references/core.md` |
| Entity/device/state discovery | `references/entity-discovery.md` |
| Helper creation/review | `references/helper.md` |
| Creating/updating objects | `references/write.md` |
| Read-only inspection | `references/read.md` |
| Review/debug/audit | `references/review.md` |
| Service calls/live control | `references/service-call.md` |
| Dashboards/resources/custom cards | `references/dashboard.md` |
| History/traces/logs | `references/history.md` |
| Areas/labels/floors/groups | `references/organize.md` |
| First-time inventory/onboarding | `references/onboarding.md` |
| Tool failure/ambiguity/unsafe fallback | `references/fallback.md` |

Do not load every reference unless needed.

## Default workflow

1. Use MCP for discovery.
2. Propose a concise plan.
3. Identify safety-sensitive objects.
4. Ask for approval before writes/control.
5. Apply only the approved change.
6. Verify through MCP.
7. Store/export a snapshot in the repo when useful.

## Repo export locations

Use these locations for snapshots or documentation:

```text
home-assistant/automations/exports/
home-assistant/helpers/exports/
home-assistant/scripts/exports/
home-assistant/dashboards/plans/
```

## Response style

When using ha-mcp, summarize:

- what was inspected
- what will change
- whether approval is needed
- what was verified
- where any export/snapshot should go
