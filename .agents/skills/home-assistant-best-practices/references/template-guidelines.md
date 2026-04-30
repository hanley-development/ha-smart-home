# Template Guidelines

## General rules

Templates should be readable and safe.

Always consider `unknown`, `unavailable`, missing attributes, empty lists, and invalid numeric values.

## Safe state checks

```jinja2
{{ states('sensor.example') not in ['unknown', 'unavailable', 'none'] }}
```

## Safe numeric conversion

```jinja2
{{ states('sensor.temperature') | float(default=0) }}
```

## Safe integer conversion

```jinja2
{{ states('sensor.count') | int(default=0) }}
```

## Attribute access

```jinja2
{{ state_attr('climate.thermostat', 'current_temperature') | float(default=0) }}
```

## Avoid

Avoid deeply nested unreadable templates, relying on friendly names, assuming attributes always exist, hardcoding entity IDs without verification, and creating templates that fail on startup.
