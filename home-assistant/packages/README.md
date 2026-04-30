# Packages

Packages are optional in this project.

Do not create packages by default.

Use packages only when:

- the user explicitly asks for package-based YAML
- a YAML-only integration requires it
- the feature is better maintained as source-controlled YAML
- an existing package is being updated
- multiple related YAML domains should intentionally live together

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
