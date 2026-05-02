# Codex Workflows for Home Assistant + ha-mcp

## Workflow types

### 1. Read-only discovery

Use when the user asks questions like:

- what entities do I have in the garage?
- what helpers exist?
- what dashboards/resources/custom cards are installed?
- why might this automation not be working?

Allowed without approval:

- read entities, states, helpers, automations, scripts, dashboards, resources, logs/traces when relevant
- summarize findings
- propose changes

Not allowed without approval:

- write Home Assistant objects
- call services
- reload/restart
- delete or enable/disable anything

### 2. Proposed change

Use when the user wants a helper, automation, script, dashboard, label, or area change.

Flow:

1. Discover with ha-mcp.
2. Draft the exact change.
3. Identify safety-sensitive effects.
4. Ask for approval.
5. Apply only approved changes.
6. Read back and verify.
7. Export/snapshot to the repo when useful.

### 3. Repo-only edit

Use when changing:

- docs
- skills
- prompts
- exported YAML
- optional package YAML
- helper scripts

Flow:

1. Read only relevant files.
2. Edit focused files.
3. Run local validation when available.
4. Summarize changed files.

### 4. Dashboard design

Flow:

1. Inspect live dashboard and resources through ha-mcp.
2. Confirm custom cards.
3. Propose layout and cards.
4. Identify safety-sensitive controls.
5. Ask approval before changing dashboard.
6. Apply through ha-mcp/UI-supported tools.
7. Verify and store plan/snapshot.

### 5. Review/debug

Flow:

1. Read target automation/script/dashboard/helper.
2. Inspect related entities and state.
3. Inspect traces/logs only when relevant.
4. Identify concrete causes.
5. Propose minimal fix.
6. Ask approval before changes.

## Approval language

Before a write/control action, Codex should show:

```text
Proposed change:
- Tool/action:
- Target:
- Data/change summary:
- Safety-sensitive impact:
- Verification:

Approval needed before I apply this.
```

## Export naming

Suggested file naming:

```text
home-assistant/automations/exports/YYYY-MM-DD-feature-name.yaml
home-assistant/helpers/exports/YYYY-MM-DD-feature-name.yaml
home-assistant/scripts/exports/YYYY-MM-DD-feature-name.yaml
home-assistant/dashboards/plans/YYYY-MM-DD-dashboard-name.md
```
