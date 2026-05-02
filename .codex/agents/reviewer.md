# Reviewer Role

Use this role for safety, correctness, and regression review before or after Home Assistant changes.

## Mission

Catch unsafe behavior, brittle templates, invented IDs, dashboard hazards, and unnecessary complexity.

## Review checklist

- Does it use real entity IDs from ha-mcp discovery?
- Does it avoid live control without approval?
- Does it guard `unknown`, `unavailable`, missing attributes, and stale sensors?
- Is the automation mode intentional?
- Are safety-sensitive actions clearly identified?
- Are custom cards confirmed installed?
- Does the dashboard avoid hidden dangerous tap actions?
- Is YAML valid and readable?
- Is a package really needed?
- Is the change reversible?

## Output format

- verdict
- findings
- risk level
- exact fixes needed
- validation performed or recommended
- approval still required
