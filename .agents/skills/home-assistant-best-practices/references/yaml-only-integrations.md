# YAML-Only Integrations

## Purpose

Some Home Assistant integrations or advanced configurations may still require YAML.

Use YAML only when appropriate.

## Project dashboard rule

Dashboards are UI-managed.

Do not create YAML dashboards unless explicitly asked.

## YAML is appropriate for

- packages
- template sensors
- binary sensors
- groups
- helpers when intentionally source-controlled
- scripts
- scenes
- automations
- advanced integrations that require YAML

## Validation

After editing YAML, validate Home Assistant configuration when possible.

Do not reload or restart without explicit approval.
