# Starter Prompts for Codex + Home Assistant + ha-mcp

## 1. Inventory overview

```text
Use ha-mcp read-only discovery only. Do not scan the whole repo. Do not change Home Assistant.

Build a concise inventory overview with areas, labels, helper types, automation/script counts, dashboards/resources, health/update summary, and cleanup opportunities.
```

## 2. Main dashboard master plan

```text
Use the dashboard designer and ha-mcp workflow skills. Inspect dashboards/resources through ha-mcp. Do not modify dashboards yet.

Design a feature-rich main dashboard with navigation buttons to subviews for Home, Security, Garage, Climate, Lighting, Cameras, Energy, Weather, Network, HA Health, and Automations/Scripts.
```

## 3. Area dashboard

```text
Use ha-mcp to inspect area REPLACE_ME_AREA. Do not modify dashboards yet.

Plan a mobile-friendly area dashboard with lights, fans, climate, humidity, air quality, cameras, locks/doors/covers, scripts/scenes, and power graphs when available.
```

## 4. Helper design

```text
Use ha-mcp to inspect existing helpers and related automations. Do not create helpers yet.

Design helpers for REPLACE_ME_FEATURE. Include helper types, entity IDs, min/max/step/unit, default behavior, reuse options, and exact approval needed.
```

## 5. Automation build

```text
Use ha-mcp discovery first. Do not create or modify automations until I approve.

Build an automation for REPLACE_ME_GOAL. Use real entity IDs, reuse helpers, guard unknown/unavailable, set mode intentionally, identify safety-sensitive actions, and propose final behavior first.
```

## 6. Script build

```text
Use ha-mcp to inspect existing scripts and services. Do not create, modify, or run scripts until I approve.

Design a reusable script for REPLACE_ME_SCRIPT_GOAL with fields, sequence, targets, safety-sensitive actions, validation, and export location.
```

## 7. Custom card visuals

```text
Use ha-mcp to inspect dashboard resources and HACS/custom cards if available. Do not modify dashboards or add resources yet.

Create a visual card plan for REPLACE_ME_VIEW with built-in, Mushroom/button-card, and advanced custom card options plus mobile layout and safe tap behavior.
```

## 8. Energy, weather, appliances, and network dashboards

```text
Use read-only ha-mcp discovery. Do not modify Home Assistant yet.

Plan dashboards for weather, appliances, energy, and network. Include entities, graph candidates, alert cards, thresholds, custom cards, and built-in fallbacks.
```

## 9. Home Assistant health and maintenance

```text
Use ha-mcp read-only tools only. Do not update, restart, reload, manage add-ons, or change Home Assistant.

Review system health, pending updates, relevant logs, automation failures/traces, and propose a health dashboard plan.
```

## 10. Safe refactor review

```text
Use ha-mcp read-only discovery first. Do not change Home Assistant until I approve.

Review this proposed refactor: REPLACE_ME_REFACTOR. Check affected entities, helpers, automations, scripts, dashboards, safety-sensitive actions, rollback plan, and validation steps.
```
