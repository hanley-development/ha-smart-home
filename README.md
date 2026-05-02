# Home Assistant Smart Home Workspace

This repository documents and improves my Home Assistant setup.

The focus is on building a cleaner, safer, more maintainable smart home using:

- Home Assistant
- Home Assistant MCP / ha-mcp
- ESPHome
- Zigbee2MQTT
- Codex/agent-assisted development
- dashboard design guidance
- automation/helper/template organization
- entity, area, and label cleanup

The goal is not just to store config files. The goal is to create a structured workspace that helps agents and humans safely improve the smart home over time.

---

## Project Goals

This workspace is used to improve:

- areas
- labels
- entity naming consistency
- helper organization
- automations
- scripts
- templates
- optional packages
- ESPHome device configuration
- dashboard design
- custom card usage
- MCP-assisted Home Assistant discovery
- future cleanup and refactoring work

The setup should be:

- reliable
- safe
- easy to maintain
- mobile-friendly
- organized by real-world areas and functions
- clear enough for Codex/agents to work on safely
- protected from accidental live device control

---

## Current Inventory

The current Home Assistant inventory notes are stored here:

- [Areas](docs/areas.md)
- [Labels](docs/labels.md)
- [Known Issues](docs/known-issues.md)

Inventory currently reflects Home Assistant data queried on **2026-04-23**.

Current naming issues:

- none currently recorded

---

## Operating Model

Home Assistant is the source of truth for normal UI-managed objects.

Use MCP to discover and, after approval, create or modify:

- helpers
- automations
- dashboards
- areas
- labels
- scenes
- UI-managed scripts

Use this repo to store:

- agent rules
- skills
- documentation
- proposed changes
- exports/snapshots
- rollback references
- dashboard plans
- optional source-controlled YAML packages

Do not create packages by default.

Packages are only used when:

- explicitly requested
- a YAML-only integration requires them
- an existing package is being updated
- a feature is better maintained as source-controlled YAML
- multiple related YAML domains intentionally need to live together

---

## Agent and Codex Structure

This repo includes agent instructions and skills so Codex can work safely and consistently.

Important files:

- [`AGENTS.md`](AGENTS.md) — root agent rules and safety boundaries
- [`USER.md`](USER.md) — user preferences and project context
- [`MEMORY.md`](MEMORY.md) — stable project memory and constraints
- [`SOUL.md`](SOUL.md) — short project principles
- [`skills-lock.json`](skills-lock.json) — enabled skills
- [`.codexignore`](.codexignore) — files Codex should avoid reading
- [`.gitignore`](.gitignore) — files Git should ignore

The root `AGENTS.md` defines the main operating model:

1. Use MCP for live Home Assistant discovery.
2. Avoid repo-wide scans unless explicitly requested.
3. Do not invent entity IDs.
4. Do not hand-edit `.storage`.
5. Do not control live devices without explicit approval.
6. Prefer MCP for UI-managed Home Assistant objects.
7. Store exports/snapshots/plans in the repo when useful.
8. Validate changes when possible.

---

## MCP-First Workflow

This project is designed to use the Home Assistant MCP server for discovery and approved Home Assistant object changes.

MCP should be used for:

- entity lookup
- device lookup
- area lookup
- label lookup
- state inspection
- automation inspection
- helper inspection
- script inspection
- scene inspection
- dashboard inspection, if available
- service capability lookup
- installed/custom card discovery, if available

The repo should not be scanned just to discover live Home Assistant state.

Preferred workflow:

```text
MCP discovers live Home Assistant state
→ agent proposes a safe change
→ user approves if needed
→ MCP applies approved Home Assistant object changes
→ MCP verifies the result
→ repo stores exports/snapshots/plans when useful
```

For source-controlled YAML or docs:

```text
MCP discovers live Home Assistant state
→ agent drafts the change
→ user approves
→ Codex edits only the needed repo files
→ change is validated
```

Read-only MCP actions are allowed.

Live control or write actions require explicit approval.

Examples of live/write actions:

- turning devices on/off
- opening or closing garage doors
- locking or unlocking doors
- arming or disarming alarms
- changing HVAC modes or setpoints
- creating/modifying/enabling/disabling automations
- creating/modifying helpers
- modifying dashboards
- changing labels/areas/entities
- reloading or restarting Home Assistant

---

## Skills

Agent skills live under:

```text
.agents/skills/
```

Current skills:

```text
.agents/skills/
├─ home-assistant-best-practices/
├─ home-assistant-dashboard-designer/
└─ ha-mcp-workflow-tools/
```

### Home Assistant Best Practices Skill

Path:

```text
.agents/skills/home-assistant-best-practices/
```

Used for Home Assistant design and implementation patterns.

This skill answers:

```text
What is the right Home Assistant pattern?
```

Used for:

- automation design
- helper selection
- templates
- scripts
- optional packages
- entity organization
- safe refactoring
- ESPHome review
- device-control safety
- YAML-only integration guidance

### Home Assistant Dashboard Designer Skill

Path:

```text
.agents/skills/home-assistant-dashboard-designer/
```

Used for dashboard design, layout, cards, custom cards, and dashboard safety.

Important rule:

> Dashboards are UI-managed. Do not create YAML dashboard files, edit YAML dashboard files, or hand-edit `.storage`.

Dashboard changes should be made through:

- Home Assistant UI
- MCP-supported dashboard tools
- user-approved MCP dashboard modification actions

### ha-mcp Workflow Tools Skill

Path:

```text
.agents/skills/ha-mcp-workflow-tools/
```

Used for safe Home Assistant MCP operations.

This skill answers:

```text
How should the agent safely use ha-mcp tools?
```

It adapts ha-nova-style workflow categories to the `homeassistant-ai/ha-mcp` tool model.

It includes reference workflows for:

- core MCP rules
- entity discovery
- helper creation
- read-only inspection
- writing approved Home Assistant objects
- reviews/debugging
- service calls
- dashboards
- history/traces/logs
- organization
- onboarding
- fallback/error handling

Core behavior:

- MCP-first discovery.
- Explicit approval before writes/control.
- Home Assistant remains source of truth for UI-managed helpers, automations, dashboards, areas, labels, scenes, and scripts.
- Repo stores exports/snapshots/plans.
- YAML packages are optional and not created by default.
- Dashboard changes use ha-mcp dashboard tools, not `.storage` edits.

---

## Home Assistant Repo Storage

This repo may contain Home Assistant exports, snapshots, plans, and optional YAML.

Recommended structure:

```text
home-assistant/
├─ AGENTS.md
├─ automations/
│  └─ exports/
├─ helpers/
│  └─ exports/
├─ packages/
├─ scripts/
│  └─ exports/
└─ dashboards/
   └─ plans/
```

Files under these folders are not automatically live-loaded by Home Assistant unless explicitly documented.

Use these folders as follows:

- `home-assistant/automations/exports/` — automation exports, proposed YAML, snapshots, rollback references
- `home-assistant/helpers/exports/` — helper exports, helper design notes, rollback references
- `home-assistant/scripts/exports/` — script exports and snapshots
- `home-assistant/dashboards/plans/` — dashboard plans, card plans, layout notes
- `home-assistant/packages/` — optional source-controlled YAML packages only when needed

Do not commit:

- `.storage`
- database files
- logs
- backups
- dependency folders
- secrets
- tokens
- generated ESPHome build output

---

## Dashboards

This project uses **UI-managed dashboards**, not YAML dashboards.

Do not:

- create YAML dashboard source files
- edit YAML dashboard source files
- edit `.storage`
- convert UI-managed dashboards to YAML
- assume dashboard files exist in the repo

Dashboard planning and design guidance belongs in documentation and skills, not dashboard YAML files.

Dashboard work should follow this pattern:

```text
Inspect dashboard through MCP
→ identify current views/cards/entities
→ propose layout/card changes
→ confirm custom cards are installed
→ identify safety-sensitive controls
→ ask for approval
→ apply changes only through MCP/UI-supported methods
→ verify result
```

Recommended dashboard areas:

- Home
- Security
- Garage
- Climate
- Lighting
- Cameras
- Network
- Maintenance
- Automations

---

## Custom Cards

Custom card guidance is stored in:

```text
.agents/skills/home-assistant-dashboard-designer/references/custom-cards.md
.agents/skills/home-assistant-dashboard-designer/references/custom-card-repos.md
```

Custom cards should be treated as an allowlist and design reference, not as guaranteed installed dependencies.

Before using a custom card:

- use MCP, HACS, dashboard resource inspection, or existing dashboard inspection to confirm the custom card exists
- prefer built-in cards when they solve the problem cleanly
- use custom cards when they provide a clear dashboard benefit
- do not invent card syntax
- do not use stale or unmaintained cards for critical controls unless explicitly approved

Useful custom cards may include:

- Mushroom
- Bubble Card
- auto-entities
- card-mod
- Battery State Card / Entity Row
- Custom Brand Icons
- Navbar Card
- Vertical Stack In Card
- Stack In Card
- Config Template Card
- state-switch
- Weather Chart Card
- Horizon Card
- status-card
- Gauge Card Pro
- Entity Progress Card
- area-card-plus
- Device Card
- Light Entity Card
- Simple Thermostat
- Firemote Card
- TV Remote Card
- Xiaomi Vacuum Map Card
- Purifier Card
- surveillance-card
- Entity Attributes Card

Custom cards should be chosen because they make the dashboard:

- safer
- clearer
- easier to use
- easier to maintain
- better on mobile

They should not be chosen only because they are popular.

---

## Helpers

Helpers should normally be created and managed through MCP/Home Assistant UI.

Common helper types:

- `input_boolean`
- `input_number`
- `input_select`
- `input_datetime`
- `timer`
- `counter`
- `input_button`

Examples:

```text
input_boolean.guest_mode
input_boolean.vacation_mode
input_boolean.quiet_hours
input_number.garage_door_alert_delay_minutes
timer.garage_door_left_open
counter.garage_alert_count
```

Use helpers when:

- a value should be adjustable from the UI
- multiple automations need the same value
- a workflow needs state
- notification timing should be configurable
- a manual override is useful

Do not invent helper entity IDs. Use MCP to discover existing helpers first.

After creating or modifying helpers through MCP, store snapshots/exports in:

```text
home-assistant/helpers/exports/
```

---

## Automations

Automations should normally be created and managed through MCP/Home Assistant UI.

Automations should be:

- readable
- safe
- reloadable
- resilient to `unknown` and `unavailable`
- explicit about triggers, conditions, and actions
- careful with delays, repeats, and modes
- designed to fail safely

Preferred modes:

- `single` for simple one-shot automations
- `restart` for state-machine style automations
- `queued` for notification or ordered workflows
- `parallel` only when clearly safe

Automation work should use real entity IDs discovered through MCP.

Do not create automations that control safety-sensitive devices without explicit approval.

Safety-sensitive areas include:

- locks
- garage doors
- alarm systems
- HVAC
- cameras
- water valves
- sirens
- security devices

Notification-only automations are preferred before automatic control.

After creating or modifying automations through MCP, store snapshots/exports in:

```text
home-assistant/automations/exports/
```

---

## Packages

Packages are optional.

Do not create packages by default.

Use packages only when:

- explicitly requested
- a YAML-only integration requires them
- an existing package is being updated
- a feature is better maintained as source-controlled YAML
- multiple related YAML domains intentionally need to live together

A package may include:

- automation
- script
- template
- sensor
- binary_sensor
- input_boolean
- input_number
- input_select
- input_datetime
- timer
- counter
- variable
- group

Packages should represent one clear feature or system.

Examples:

```text
nws_alerts.yaml
esphome_auto_updates.yaml
battery_monitoring.yaml
network_monitoring.yaml
```

Do not use packages as random dumping grounds.

---

## Templates

Templates should safely handle:

- `unknown`
- `unavailable`
- missing attributes
- empty lists
- invalid numeric values

Prefer safe conversion patterns:

```jinja2
{{ states('sensor.temperature') | float(default=0) }}
```

Prefer safe state checks:

```jinja2
{{ states('sensor.example') not in ['unknown', 'unavailable', 'none'] }}
```

Templates should be readable and maintainable. Avoid deeply nested templates unless necessary.

Prefer native Home Assistant triggers, conditions, and helpers before creating complex templates.

---

## ESPHome

ESPHome configuration lives under:

```text
esphome/
├─ AGENTS.md
├─ devices/
├─ packages/
└─ common/
```

ESPHome changes should be conservative.

Do not change these unless explicitly asked:

- device name
- friendly name
- static IP
- Wi-Fi settings
- API encryption
- OTA settings
- board type
- substitutions
- package include structure
- GPIO pins
- relay behavior
- garage door behavior
- safety interlocks

Preferred validation:

```bash
esphome config path/to/device.yaml
```

Do not compile or upload firmware unless explicitly approved.

---

## Safety Rules

Do not expose, print, modify, or commit secrets.

Sensitive items include:

- passwords
- API keys
- long-lived access tokens
- webhook URLs
- private keys
- certificates
- Duo/Auth secrets
- Cloudflare tokens
- MQTT credentials
- Wi-Fi credentials
- Home Assistant tokens

If a file appears to contain secrets, stop and warn before displaying or modifying that content.

---

## Git and Repo Usage

This repo may be accessed over Samba, so avoid unnecessary broad Git operations.

Agents should not run these unless explicitly asked:

- `git pull`
- `git push`
- `git reset`
- `git rebase`
- `git clean`
- broad repo-wide formatting
- mass renames

Prefer focused diffs on named files.

---

## Recommended Agent Prompt Pattern

Use targeted prompts like this:

```text
Use MCP for discovery.

Do not scan the whole repo.

Task:
Create a helper and automation for dryer notifications.

Rules:
- Do not create a package unless I explicitly approve it.
- Use MCP to inspect existing dryer entities, notification services, helpers, and related automations.
- Propose the helper and automation first.
- After I approve, create them through MCP.
- Then export or document the final automation/helper YAML into:
  - home-assistant/automations/exports/dryer_notification.yaml
  - home-assistant/helpers/exports/laundry_helpers.yaml
```

For dashboard work:

```text
Use the Home Assistant dashboard designer skill and ha-mcp-workflow-tools skill.

Use MCP to inspect the existing dashboard.

Do not edit `.storage`.
Do not create YAML dashboard files.
Confirm custom cards are installed before using them.
Propose changes first.
Do not apply dashboard changes until I approve.
```

---

## Project Principle

This repo exists to make the smart home safer, cleaner, and easier to maintain.

Prefer:

```text
MCP discovery
small changes
clear validation
safe dashboards
maintainable automations
real entity IDs
explicit approval for live control
exports/snapshots for review and rollback
```

Avoid:

```text
repo-wide scanning
invented entities
hand-edited .storage
fragile dashboard hacks
unsafe live control
broad refactors
unapproved restarts/reloads
unnecessary packages
```