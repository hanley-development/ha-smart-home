# Dashboard Card Patterns

## General card rules

Cards should be readable, grouped logically, useful on mobile, safe to tap, and not duplicated unnecessarily.

## Status-first pattern

Use for safety-sensitive devices.

Pattern:

1. Show state clearly.
2. Show last changed/recent activity if useful.
3. Put controls below or separate from status.
4. Use confirmation where supported.

Good for locks, garage doors, alarms, HVAC, and water valves.

## Alert summary pattern

Use for home overview.

Shows open doors, unlocked locks, garage open, alarm problems, low batteries, and unavailable critical devices.

## Area control pattern

Use for lighting and common rooms.

## Diagnostic pattern

Use for maintenance/network views.

## Card types

Use available card types based on installed frontend/custom cards.

Common safe choices:

- Tile card
- Entities card
- Button card
- Conditional card
- Gauge card
- History graph
- Thermostat card
- Alarm panel card
- Picture glance
- Markdown card

If Mushroom cards are installed, they can be useful for clean mobile layouts.

If custom button-card is installed, use it carefully and avoid overly complex templates.

## Dangerous card placement

Avoid putting unlock, open garage, disarm alarm, turn off critical switches, or change HVAC mode next to frequent taps.
