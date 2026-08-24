# Lower Level Dashboard Design

**Status:** Approved design

**Date:** 2026-08-24

## Purpose

Modernize the Lower Level section of the existing `Georgetown-HAAS` dashboard while preserving the established `Home → Areas` navigation model.
The `Areas` view will provide direct access to seven Lower Level area subviews with concise, useful status and no unnecessary intermediate Basement or Lower Level view.

This dashboard is UI-managed. The implementation must use supported Home Assistant dashboard operations and must not create dashboard YAML or edit `.storage`.

## Current Context

The current dashboard inspection established the following relevant state:

- The default dashboard is `Georgetown-HAAS` and uses storage mode.
- The `Home` view navigates to the `Areas` view at `living-areas`.
- `Areas` contains Main Level, Lower Level, and Upper Level sections.
- Main Level already uses paired area cards and is the structural model for Lower Level.
- Lower Level currently includes Utility Room, Basement, and Mike's Office cards.
- The generic Basement Home Assistant area has been removed and must not return.
- Existing reusable views include Utility Room at `utility_room`, Server Room at `server-room`, and Office of Mike at `office-of-mike`.
- Installed dashboard resources include Mushroom and other existing custom cards. The design requires no new dependency.

## Goals

- Keep `Home → Areas` as the navigation entry point.
- Replace the Lower Level section with seven direct area cards.
- Use a modern, status-first card design modeled on the current Main Level structure.
- Reuse and modernize the three existing relevant views.
- Create four missing area subviews.
- Provide a consistent subview hierarchy with area-specific modules.
- Preserve unrelated dashboard views and behavior.
- Apply the work incrementally with a complete rollback path.

## Non-Goals

- Do not create a generic Basement area or parent view.
- Do not create an intermediate Lower Level view.
- Do not redesign Main Level or Upper Level.
- Do not install a custom card or other dependency.
- Do not create helpers solely for presentation unless later live inspection proves an existing entity cannot provide a required summary cleanly.
- Do not add restart, shutdown, dangerous power, or other safety-sensitive system controls.
- Do not exercise physical devices, automations, scripts, or safety-sensitive controls as part of dashboard verification.

## Selected Approach

Use incremental in-place modernization. Capture the complete live dashboard first, create or update one destination view at a time, verify each write, and update the Lower Level navigation cards only after every destination exists.

This approach preserves working content, minimizes the scope of each live change, and provides a clear stopping and rollback point after every stage.

## Information Architecture

The `Areas` view remains the single area directory. Its Lower Level section contains these cards in order:

1. Basement Entertainment
2. Basement Bathroom
3. Mike's Office
4. Utility Room
5. Server Room
6. Network
7. Home-Assistant

Cards use paired rows. Home-Assistant spans the final row. At widths too narrow for safe touch targets, Home Assistant may stack the pair rather than shrink the controls below a usable size.

All seven destinations are subviews. Existing view paths remain stable where possible:

| Display title | Path | Treatment |
| --- | --- | --- |
| Basement Entertainment | `basement-entertainment` | Create subview |
| Basement Bathroom | `basement-bathroom` | Create subview |
| Mike's Office | `office-of-mike` | Reuse, retitle, and modernize existing subview |
| Utility Room | `utility_room` | Reuse, modernize, and mark as a subview |
| Server Room | `server-room` | Reuse, modernize, and mark as a subview |
| Network | `network` | Create subview |
| Home-Assistant | `home-assistant` | Create subview |

Before creating a path, live inspection must confirm that it is not already occupied by a different view. A collision is a hard blocker; the implementation must stop and propose a revised path rather than overwrite an unrelated view.

## Lower Level Area Cards

Each area card uses the approved modern status-first structure:

- Area icon and display name
- Clear navigation affordance
- No more than two essential, area-specific status chips
- Alert styling that replaces routine status when attention is needed
- Main card tap navigates to the area subview
- Status-chip tap opens that entity's More Info dialog
- No hidden hold or double-tap action
- No direct state-changing action on the Areas screen

Chip content follows this priority:

1. Active alert or abnormal condition
2. Area-defining operational status
3. Temperature or humidity
4. Number of lights currently on
5. Primary device status

The first two applicable items are shown. An alert displaces a lower-priority routine chip rather than creating a third chip.
An `unknown` or `unavailable` state is displayed honestly with muted warning styling and is never interpreted as healthy or off.

## Area Subview Pattern

Every area subview uses the same hierarchy:

1. Area heading and concise status summary
2. Primary everyday controls
3. Environmental information
4. Area-specific systems and devices
5. Diagnostics or low-frequency information

The shared hierarchy provides consistency without forcing every area to contain identical modules. Existing useful content is retained, deduplicated where necessary, and moved into the appropriate hierarchy.

### Basement Entertainment

Prioritize lighting, media, environmental status, and meaningful entertainment controls. Raw outlet controls should not dominate the view when a higher-level device or activity control is available.

### Basement Bathroom

Prioritize lighting, ventilation, humidity, and moisture-related status.

### Mike's Office

Retain useful content from the existing Office of Mike view, then organize lighting, occupancy or environmental information, and office-specific equipment under the shared hierarchy.

### Utility Room

Retain useful existing content while prioritizing leak or moisture status, environmental information, lighting, and relevant mechanical or laundry equipment.

### Server Room

Prioritize temperature and equipment-health status. Omit risky power controls unless they receive a separate design and explicit approval.

### Network

Prioritize gateway, access-point, switch, and connectivity health. This view is diagnostic and status-first rather than control-oriented.

### Home-Assistant

Prioritize platform health, relevant update status, backup status, and integration or system warnings. Exclude restart, shutdown, and similar administrative controls.

## Entity and Card Selection

Only identifiers discovered from live Home Assistant may be used. Area assignment is useful for discovery but does not automatically make an entity dashboard-worthy. Each selected entity must be relevant to the area's everyday use, alerting,
environment, or diagnostics.

Use direct entity state where practical. Avoid duplicate helpers and complex templates. A new helper requires its own justification, source-controlled proposal, approval, and verification and is outside this design unless separately approved.

Prefer built-in cards first, followed by installed and verified Mushroom cards when they provide the approved interaction or layout benefit. Do not invent custom-card syntax or add a dependency.

## Data and Interaction Flow

The Home Assistant entity registry and live entity state are the data sources. Verified entity IDs feed the area cards and subview cards directly.

The interaction flow is:

1. The user opens `Home` and selects `Areas`.
2. The user scans the Lower Level cards for concise normal or alert status.
3. Selecting a card opens its area subview.
4. Selecting a chip opens the source entity's More Info dialog.
5. State-changing controls, when appropriate, are available only inside the area subview.

Read-only health and status presentation must not trigger automations, scripts, or service calls.

## Safe Rollout

The implementation order is:

1. Re-read the live dashboard, seven areas, relevant entities, and installed dashboard resources after exact MCP approval.
2. Save the complete pre-change dashboard representation to `home-assistant/dashboards/plans/2026-08-24-georgetown-haas-lower-level-pre-change.md` as a non-deployable snapshot and rollback artifact.
3. Prepare the exact proposed dashboard changes in repository documentation and validate them.
4. Commit the reviewed repository representation and obtain explicit approval before pushing it.
5. Push the reviewed representation before any corresponding live write.
6. Create Basement Entertainment, Basement Bathroom, Network, and Home-Assistant subviews one at a time.
7. Modernize Utility Room, Server Room, and Office of Mike one at a time.
8. Verify all seven subview paths and essential cards.
9. Replace the Lower Level section in `Areas` only after every destination is verified.
10. Read back the complete navigation chain and compare it with the approved design.

Every Home Assistant MCP call requires a preview of the exact operation, target, request body when applicable, expected effect, risks, and verification plan followed by explicit approval.
Each changed view is read back before the next dependent stage begins.

## Failure Handling and Rollback

Stop the rollout immediately when:

- A referenced entity or dashboard resource does not exist.
- A proposed path is occupied by an unrelated view.
- A dashboard write fails.
- Live read-back differs from the approved proposal.
- An unrelated view changes.
- A backup or usable rollback representation is unavailable.

Do not continue dependent navigation changes after a failure. Preserve the last verified state, diagnose from live read-back, and propose the smallest corrective operation.

Restoring from the captured snapshot is a separate live write. Show the exact rollback operation and obtain explicit approval before applying it.

An entity becoming `unknown` or `unavailable` does not invalidate otherwise sound dashboard configuration. The affected card must show that state honestly without reporting a false healthy state.

## Verification

### Repository Verification

- Run `uv run python tools/run_codex_checks.py --skip-index`.
- Run `git diff --check`.
- Review `git status --short`.
- Inspect the complete focused diff for secrets, unrelated edits, generated noise, stale paths, and accidental behavior changes.
- Keep `.superpowers/` visual-companion artifacts untracked and out of commits.

### Live Verification

- Confirm `Home → Areas` navigation still works.
- Confirm Main Level and Upper Level are logically unchanged.
- Confirm Lower Level contains exactly seven cards in the approved order.
- Confirm paired rows and the final full-row Home-Assistant card.
- Confirm every main card opens the correct area subview.
- Confirm every chip is configured to open the intended entity's More Info dialog and does not directly change state.
- Confirm each card contains no more than two chips.
- Confirm alert states replace routine chips.
- Confirm `unknown` and `unavailable` states are represented honestly.
- Confirm all seven subviews follow the shared hierarchy and retain useful area-specific content.
- Confirm no card references a missing entity, missing resource, or invalid navigation path.
- Confirm Server Room, Network, and Home-Assistant contain no risky power, restart, shutdown, or similar controls.
- Confirm the pre-change snapshot remains available and usable.

Visual acceptance covers standard phone and wider tablet or desktop widths. Verification must not operate physical devices or execute automations, scripts, or safety-sensitive controls without separate exact approval.

## Acceptance Criteria

The dashboard work is complete only when:

- The seven Lower Level cards and seven working subviews match this design.
- Navigation and More Info interactions are correct.
- Live entity references and installed card resources are verified.
- Unrelated dashboard areas and views remain unchanged.
- Repository and live checks pass or any unavailable check is explicitly reported.
- A verified rollback artifact remains available.
- The user completes visual review and accepts the result.
