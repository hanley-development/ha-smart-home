# home-assistant/AGENTS.md

## Scope

This directory contains documentation, exports, snapshots, and optional source-controlled YAML for Home Assistant.

Home Assistant itself is the source of truth for most UI-managed objects.

Prefer MCP for creating and modifying:

- helpers
- automations
- dashboards
- areas
- labels
- scenes
- scripts, when UI-managed

Do not assume new Home Assistant objects must be created as YAML packages.

## Preferred operating model

Use MCP-first object management.

For new helpers and automations:

1. Use MCP to inspect existing entities, helpers, automations, areas, labels, and services.
2. Propose the helper or automation design.
3. Ask for explicit approval before creating or modifying anything.
4. Use MCP to create or modify the approved Home Assistant object.
5. Verify the object exists through MCP.
6. Export or document the resulting YAML/config snapshot in this repo.

## Repo storage model

Use this repo to store:

- proposed automation YAML
- exported automation YAML
- helper design notes
- helper export snapshots
- dashboard plans
- dashboard card plans
- MCP change logs
- package YAML only when source-controlled YAML is intentionally needed

Do not use this repo as the primary source of truth for UI-managed Home Assistant objects unless explicitly stated.

## Automations

Automations are normally created and managed through Home Assistant/MCP.

Store automation snapshots under:

```text
home-assistant/automations/exports/
```

Automation export files are for review, documentation, and rollback reference unless the user explicitly says they are source-controlled live config.

## Helpers

Helpers are normally created and managed through Home Assistant/MCP.

Store helper snapshots or notes under:

```text
home-assistant/helpers/exports/
```

Do not create helper YAML packages unless explicitly asked.

## Packages

Packages are optional.

Use packages only when a feature truly benefits from being source-controlled as YAML.

Good package use cases:

- complex YAML-only integrations
- bundled feature logic that should be version-controlled
- reusable feature systems with helpers, templates, scripts, and automations together
- configurations that are easier to review as code than through the UI
- legacy YAML packages already in use

Do not create new packages by default.

Ask first before converting UI-managed automations or helpers into packages.

## Dashboards

Dashboards are UI-managed.

Do not:

- create YAML dashboard files
- edit `.storage`
- convert UI dashboards to YAML

Use MCP/UI-supported dashboard tools.

Store dashboard plans under:

```text
home-assistant/dashboards/plans/
```
This project does not use YAML-managed dashboards.

## Safety

Creating, modifying, enabling, disabling, deleting, or triggering automations through MCP requires explicit approval.

Creating or modifying helpers through MCP requires approval.

Automations that control safety-sensitive devices require extra confirmation.

Safety-sensitive devices include locks, garage doors, alarm systems, HVAC, cameras, water valves, sirens, and security devices.

Notification-only automations are lower risk, but still require approval before creation.

## Automation rules

Automations should be:

- readable
- safe
- reloadable
- resilient to `unknown` and `unavailable`
- explicit about triggers, conditions, and actions
- careful with delays, repeats, and modes

Preferred modes:

- `single` for simple one-shot automations
- `restart` for state-machine automations
- `queued` for ordered actions or notifications
- `parallel` only when clearly safe

## Safety-sensitive devices

Require explicit approval before creating automations that control:

- locks
- garage doors
- alarm systems
- HVAC
- cameras
- water valves
- sirens
- security devices

Notification-only automations are preferred first.

## Validation

After MCP creates or modifies an object:

- verify it exists
- verify key entities are correct
- verify it is enabled/disabled as expected
- export or document the final configuration when possible

Prefer Home Assistant config validation before reload.
Do not reload or restart Home Assistant unless explicitly approved.
