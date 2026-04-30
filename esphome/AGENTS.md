# esphome/AGENTS.md

## Scope

This directory contains ESPHome device configs, packages, and common reusable configuration.

## Safety

Do not upload firmware unless explicitly asked.

Do not change the following unless explicitly asked:

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

## Preferred layout

Use:

```text
esphome/devices/
esphome/packages/
esphome/common/
```

Device files should contain device-specific substitutions and hardware configuration.

Common packages should contain reusable logic.

## Validation

Before suggesting that an ESPHome config is ready, prefer:

```bash
esphome config path/to/device.yaml
```

Only compile with approval:

```bash
esphome compile path/to/device.yaml
```

Only upload with approval:

```bash
esphome upload path/to/device.yaml
```

## YAML style

- Preserve includes.
- Avoid unnecessary YAML anchors/merge keys.
- Keep device-specific logic in device files.
- Keep shared logic in packages/common files.
- Avoid broad formatting rewrites.
