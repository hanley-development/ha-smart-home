# Dashboard Safety

## Safety goal

Dashboards should reduce accidental actions.

## High-risk controls

Treat these as high risk:

- garage door open/close
- lock/unlock
- alarm arm/disarm
- HVAC mode/setpoint changes
- camera privacy controls
- water valve controls
- siren controls
- security mode changes

## Safer design

Prefer:

- status cards above control cards
- separated control sections
- clear labels
- icons that match function
- confirmation where supported
- conditional visibility for advanced controls
- disabling or hiding risky controls from casual views

## Avoid

Avoid:

- tiny buttons for dangerous actions
- placing dangerous controls near lights/scenes
- unlabeled icons
- duplicate controls across many views
- controls that look like status indicators
- exposing admin/maintenance controls on main family dashboards

## Suggested approval check

Before adding a dangerous control, ask:

```text
This dashboard change adds a control for a safety-sensitive device. Do you want this as a control card, or should it be status-only?
```
