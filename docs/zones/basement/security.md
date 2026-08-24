# Security

> Read-only Home Assistant inventory captured 2026-08-24. No devices or configuration were changed.

- Floor classification: Outside Basement floor
- Area: Security
- Devices: 1
- Entities: 20
- Inclusion rule: `basement` appears in the device name, entity ID, or friendly name.

## Devices

| Device | Manufacturer | Model | Integration | Device ID |
|---|---|---|---|---|
| Basement Utility Room Camera | Reolink | RLC-820A | reolink | `2be0306e4723b9956469ae9ed6fb8f99` |

## Entities

| Entity ID | Friendly name | Domain |
|---|---|---|
| `binary_sensor.basement_motion` | Basement Utility Room Camera Motion | binary_sensor |
| `binary_sensor.basement_person` | Basement Utility Room Camera Person | binary_sensor |
| `binary_sensor.basement_pet` | Basement Utility Room Camera Pet | binary_sensor |
| `binary_sensor.basement_vehicle` | Basement Utility Room Camera Vehicle | binary_sensor |
| `camera.basement_fluent` | Basement Utility Room Camera Fluent | camera |
| `number.basement_ai_person_sensitivity` | Basement Utility Room Camera AI person sensitivity | number |
| `number.basement_ai_pet_sensitivity` | Basement Utility Room Camera AI pet sensitivity | number |
| `number.basement_ai_vehicle_sensitivity` | Basement Utility Room Camera AI vehicle sensitivity | number |
| `number.basement_motion_sensitivity` | Basement Utility Room Camera Motion sensitivity | number |
| `select.basement_day_night_mode` | Basement Utility Room Camera Day night mode | select |
| `sensor.basement_day_night_state` | Basement Utility Room Camera Day night state | sensor |
| `switch.basement_email_on_event` | Basement Utility Room Camera Email on event | switch |
| `switch.basement_ftp_upload` | Basement Utility Room Camera FTP upload | switch |
| `switch.basement_hub_ringtone_on_event` | Basement Utility Room Camera Hub ringtone on event | switch |
| `switch.basement_infrared_lights_in_night_mode` | Basement Utility Room Camera Infrared lights in night mode | switch |
| `switch.basement_manual_record` | Basement Utility Room Camera Manual record | switch |
| `switch.basement_push_notifications` | Basement Utility Room Camera Push notifications | switch |
| `switch.basement_record` | Basement Utility Room Camera Record | switch |
| `switch.basement_record_audio` | Basement Utility Room Camera Record audio | switch |
| `update.basement_firmware` | Basement Utility Room Camera Firmware | update |
