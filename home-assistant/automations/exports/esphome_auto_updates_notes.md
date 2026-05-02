# ESPHome Auto Updates

Live Home Assistant source of truth:

- `automation.esphome_auto_updates`

Enrollment model:

- Uses label `esphome_auto_update` on `update.*` entities.
- New ESPHome firmware update entities join the automation when this label is added.
- Uses `binary_sensor.esphome_auto_updates_pending` as the helper-backed
  yes/no condition for whether any labeled firmware updates are pending.

Current labeled entities as of 2026-04-30:

- `update.basement_bluetooth_proxy_firmware`
- `update.garage_bluetooth_proxy_firmware`
- `update.living_room_bluetooth_proxy_firmware`
- `update.ratgdov2_5i_11d5dc_firmware`
- `update.ratgdov2_5i_0cd4e2_firmware`

Explicitly excluded:

- `update.esphome_update` because it is the ESPHome Device Builder update entity, not a device firmware entity.
