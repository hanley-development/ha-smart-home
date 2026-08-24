# Server Room

> Read-only Home Assistant inventory captured 2026-08-24. No devices or configuration were changed.

- Floor classification: Basement
- Area: Server Room
- Devices: 20
- Entities: 172
- Inclusion rule: assigned to this Basement-floor area.

## Devices

| Device | Manufacturer | Model | Integration | Device ID |
|---|---|---|---|---|
| Cyberpower | CPS | PR1500LCD | nut | `7b2947b7e2bdea579e81a133f2a0cbac` |
| mediastorage | Synology | DS416j | synology_dsm | `303b4e1356990477e9629fe42ab0d5d5` |
| mediastorage | Synology | DS416j | synology_dsm | `fb64de4b87f2e1a3b0b4085531f967f0` |
| mediastorage (Drive 1) | WDC | WD60EFZX-68B3FN0 | synology_dsm | `fc9d7b18ebe7497631ba77e2dbfd487e` |
| mediastorage (Drive 2) | WDC | WD30EFRX-68EUZN0 | synology_dsm | `7882121eb78ac272a0d56c7b49ea8c43` |
| mediastorage (Drive 3) | WDC | WD30EFRX-68EUZN0 | synology_dsm | `e1a0aeb562db916c30acea4c106b4e6d` |
| mediastorage (Drive 4) | WDC | WD30EFRX-68EUZN0 | synology_dsm | `318072f6b2f2b1d4f50f947779ee484d` |
| mediastorage (Volume 1) | Synology | DS416j | synology_dsm | `f31fa6fb26606514c4b5f322e3617a0a` |
| NVR | Reolink | RLN16-410 | reolink | `221a711ea30cf81b7f603b9551ff6cc9` |
| R2D2 | Synology | DS1522+ | synology_dsm | `5935f1990114849f680d208c3558c3e6` |
| R2D2 (Drive 1) | WDC | WD240KFGX-68CJNN0 | synology_dsm | `842abc2a5ec289793c854cd657496761` |
| R2D2 (Drive 2) | WDC | WD142KFGX-68AFPN0 | synology_dsm | `f50dc6734781d34a7a1c77464ce3f803` |
| R2D2 (Drive 3) | Seagate | ST16000NT001-3MC101 | synology_dsm | `a2c6df6b63ee2422ef42a2848f945a0b` |
| R2D2 (M.2 Drive 1) | Samsung | Samsung SSD 980 PRO 1TB | synology_dsm | `9d7bec907ab54a8470dacd7398bd9dc7` |
| R2D2 (M.2 Drive 2) | Samsung | Samsung SSD 980 PRO 1TB | synology_dsm | `37116532b30a38e9205b3b1653c1812d` |
| R2D2 (Volume 1) | Synology | DS1522+ | synology_dsm | `e52a8a48167aeee1040378ebd649a07b` |
| r2d2.home.localdomain | Synology Incorporated | DS1522+ | unknown | `77da42cfc2d219f9f26e1016190dd82b` |
| Server Rack AirGuard TH | SONOFF | Temperature and humidity sensor with display and relay control | zigbee2mqtt | `bc59fb8bfe88bfc158436706bd5d3af3` |
| SpeedTest | — | — | speedtestdotnet | `dc5050416d7cb09b8b7a89db9fc7cbef` |
| Tripp_Lite_Ups | Tripp Lite | Tripp Lite UPS | nut | `77283e4628a3bd218e8dbe22f6b8401b` |

## Entities

| Entity ID | Friendly name | Domain |
|---|---|---|
| `binary_sensor.mediastorage_drive_1_below_min_remaining_life` | mediastorage (Drive 1) Below min remaining life | binary_sensor |
| `binary_sensor.mediastorage_drive_1_exceeded_max_bad_sectors` | mediastorage (Drive 1) Exceeded max bad sectors | binary_sensor |
| `binary_sensor.mediastorage_drive_2_below_min_remaining_life` | mediastorage (Drive 2) Below min remaining life | binary_sensor |
| `binary_sensor.mediastorage_drive_2_exceeded_max_bad_sectors` | mediastorage (Drive 2) Exceeded max bad sectors | binary_sensor |
| `binary_sensor.mediastorage_drive_3_below_min_remaining_life` | mediastorage (Drive 3) Below min remaining life | binary_sensor |
| `binary_sensor.mediastorage_drive_3_exceeded_max_bad_sectors` | mediastorage (Drive 3) Exceeded max bad sectors | binary_sensor |
| `binary_sensor.mediastorage_drive_4_below_min_remaining_life` | mediastorage (Drive 4) Below min remaining life | binary_sensor |
| `binary_sensor.mediastorage_drive_4_exceeded_max_bad_sectors` | mediastorage (Drive 4) Exceeded max bad sectors | binary_sensor |
| `binary_sensor.mediastorage_security_status` | mediastorage Security status | binary_sensor |
| `binary_sensor.r2d2_drive_1_below_min_remaining_life` | R2D2 (Drive 1) Below min remaining life | binary_sensor |
| `binary_sensor.r2d2_drive_1_exceeded_max_bad_sectors` | R2D2 (Drive 1) Exceeded max bad sectors | binary_sensor |
| `binary_sensor.r2d2_drive_2_below_min_remaining_life` | R2D2 (Drive 2) Below min remaining life | binary_sensor |
| `binary_sensor.r2d2_drive_2_exceeded_max_bad_sectors` | R2D2 (Drive 2) Exceeded max bad sectors | binary_sensor |
| `binary_sensor.r2d2_drive_3_below_min_remaining_life` | R2D2 (Drive 3) Below min remaining life | binary_sensor |
| `binary_sensor.r2d2_drive_3_exceeded_max_bad_sectors` | R2D2 (Drive 3) Exceeded max bad sectors | binary_sensor |
| `binary_sensor.r2d2_m_2_drive_1_below_min_remaining_life` | R2D2 (M.2 Drive 1) Below min remaining life | binary_sensor |
| `binary_sensor.r2d2_m_2_drive_1_exceeded_max_bad_sectors` | R2D2 (M.2 Drive 1) Exceeded max bad sectors | binary_sensor |
| `binary_sensor.r2d2_m_2_drive_2_below_min_remaining_life` | R2D2 (M.2 Drive 2) Below min remaining life | binary_sensor |
| `binary_sensor.r2d2_m_2_drive_2_exceeded_max_bad_sectors` | R2D2 (M.2 Drive 2) Exceeded max bad sectors | binary_sensor |
| `binary_sensor.r2d2_security_status` | R2D2 Security status | binary_sensor |
| `button.mediastorage_reboot` | mediastorage Restart | button |
| `button.mediastorage_shutdown` | mediastorage Shut down | button |
| `button.r2d2_reboot` | R2D2 Restart | button |
| `button.r2d2_shutdown` | R2D2 Shut down | button |
| `device_tracker.r2d2_lan` | r2d2.home.localdomain r2d2.home.localdomain | device_tracker |
| `number.server_rack_airguard_th_comfort_humidity_max` | Server Rack AirGuard TH Comfort humidity max | number |
| `number.server_rack_airguard_th_comfort_humidity_min` | Server Rack AirGuard TH Comfort humidity min | number |
| `number.server_rack_airguard_th_comfort_temperature_max` | Server Rack AirGuard TH Temperature | number |
| `number.server_rack_airguard_th_comfort_temperature_min` | Server Rack AirGuard TH Temperature | number |
| `number.server_rack_airguard_th_external_humidity` | Server Rack AirGuard TH External humidity | number |
| `number.server_rack_airguard_th_external_temperature` | Server Rack AirGuard TH Temperature | number |
| `number.server_rack_airguard_th_humidity_calibration` | Server Rack AirGuard TH Humidity calibration | number |
| `number.server_rack_airguard_th_temperature_calibration` | Server Rack AirGuard TH Temperature calibration | number |
| `select.server_rack_airguard_th_temperature_sensor_select` | Server Rack AirGuard TH Temperature sensor select | select |
| `select.server_rack_airguard_th_temperature_units` | Server Rack AirGuard TH Temperature units | select |
| `select.server_room_mediastorage_fan_speed_mode` | mediastorage Fan speed mode | select |
| `select.server_room_r2d2_fan_speed_mode` | R2D2 Fan speed mode | select |
| `sensor.0xa4c13809c1dbffff_last_seen` | Server Rack AirGuard TH Last seen | sensor |
| `sensor.0xa4c13809c1dbffff_linkquality` | Server Rack AirGuard TH Linkquality | sensor |
| `sensor.cyberpower_battery_charge` | Cyberpower Battery charge | sensor |
| `sensor.cyberpower_battery_chemistry` | sensor.cyberpower_battery_chemistry | sensor |
| `sensor.cyberpower_battery_manuf_date` | Cyberpower Battery manuf. date | sensor |
| `sensor.cyberpower_battery_runtime` | Cyberpower Battery runtime | sensor |
| `sensor.cyberpower_battery_voltage` | Cyberpower Battery voltage | sensor |
| `sensor.cyberpower_beeper_status` | Cyberpower Beeper status | sensor |
| `sensor.cyberpower_input_line_frequency` | Cyberpower Input frequency | sensor |
| `sensor.cyberpower_input_voltage` | Cyberpower Input voltage | sensor |
| `sensor.cyberpower_load` | Cyberpower Load | sensor |
| `sensor.cyberpower_load_restart_delay` | Cyberpower Load restart delay | sensor |
| `sensor.cyberpower_load_shutdown_timer` | Cyberpower Load shutdown timer | sensor |
| `sensor.cyberpower_load_start_timer` | Cyberpower Load start timer | sensor |
| `sensor.cyberpower_low_battery_runtime` | Cyberpower Low battery runtime | sensor |
| `sensor.cyberpower_low_battery_setpoint` | Cyberpower Low battery setpoint | sensor |
| `sensor.cyberpower_nominal_battery_voltage` | Cyberpower Nominal battery voltage | sensor |
| `sensor.cyberpower_nominal_input_voltage` | Cyberpower Nominal input voltage | sensor |
| `sensor.cyberpower_nominal_real_power` | Cyberpower Nominal real power | sensor |
| `sensor.cyberpower_output_frequency` | Cyberpower Output frequency | sensor |
| `sensor.cyberpower_output_voltage` | Cyberpower Output voltage | sensor |
| `sensor.cyberpower_self_test_result` | Cyberpower Self-test result | sensor |
| `sensor.cyberpower_status` | Cyberpower Status | sensor |
| `sensor.cyberpower_status_data` | Cyberpower Status data | sensor |
| `sensor.cyberpower_ups_shutdown_delay` | Cyberpower UPS shutdown delay | sensor |
| `sensor.cyberpower_warning_battery_setpoint` | Cyberpower Warning battery setpoint | sensor |
| `sensor.mediastorage_cpu_load_average_1_min` | sensor.mediastorage_cpu_load_average_1_min | sensor |
| `sensor.mediastorage_cpu_load_average_15_min` | mediastorage CPU load average (15 min) | sensor |
| `sensor.mediastorage_cpu_load_average_5_min` | mediastorage CPU load average (5 min) | sensor |
| `sensor.mediastorage_cpu_utilization_other` | sensor.mediastorage_cpu_utilization_other | sensor |
| `sensor.mediastorage_cpu_utilization_system` | sensor.mediastorage_cpu_utilization_system | sensor |
| `sensor.mediastorage_cpu_utilization_total` | mediastorage CPU utilization (total) | sensor |
| `sensor.mediastorage_cpu_utilization_user` | mediastorage CPU utilization (user) | sensor |
| `sensor.mediastorage_download_throughput` | mediastorage Download throughput | sensor |
| `sensor.mediastorage_drive_1_status` | mediastorage (Drive 1) Status | sensor |
| `sensor.mediastorage_drive_1_status_smart` | sensor.mediastorage_drive_1_status_smart | sensor |
| `sensor.mediastorage_drive_1_temperature` | mediastorage (Drive 1) Temperature | sensor |
| `sensor.mediastorage_drive_2_status` | mediastorage (Drive 2) Status | sensor |
| `sensor.mediastorage_drive_2_status_smart` | sensor.mediastorage_drive_2_status_smart | sensor |
| `sensor.mediastorage_drive_2_temperature` | mediastorage (Drive 2) Temperature | sensor |
| `sensor.mediastorage_drive_3_status` | mediastorage (Drive 3) Status | sensor |
| `sensor.mediastorage_drive_3_status_smart` | sensor.mediastorage_drive_3_status_smart | sensor |
| `sensor.mediastorage_drive_3_temperature` | mediastorage (Drive 3) Temperature | sensor |
| `sensor.mediastorage_drive_4_status` | mediastorage (Drive 4) Status | sensor |
| `sensor.mediastorage_drive_4_status_smart` | sensor.mediastorage_drive_4_status_smart | sensor |
| `sensor.mediastorage_drive_4_temperature` | mediastorage (Drive 4) Temperature | sensor |
| `sensor.mediastorage_last_boot` | sensor.mediastorage_last_boot | sensor |
| `sensor.mediastorage_memory_available_real` | mediastorage Memory available (real) | sensor |
| `sensor.mediastorage_memory_available_swap` | mediastorage Memory available (swap) | sensor |
| `sensor.mediastorage_memory_cached` | sensor.mediastorage_memory_cached | sensor |
| `sensor.mediastorage_memory_size` | sensor.mediastorage_memory_size | sensor |
| `sensor.mediastorage_memory_total_real` | mediastorage Memory total (real) | sensor |
| `sensor.mediastorage_memory_total_swap` | mediastorage Memory total (swap) | sensor |
| `sensor.mediastorage_memory_usage_real` | mediastorage Memory usage (real) | sensor |
| `sensor.mediastorage_temperature` | mediastorage Temperature | sensor |
| `sensor.mediastorage_upload_throughput` | mediastorage Upload throughput | sensor |
| `sensor.mediastorage_volume_1_average_disk_temp` | mediastorage (Volume 1) Average disk temp | sensor |
| `sensor.mediastorage_volume_1_maximum_disk_temp` | sensor.mediastorage_volume_1_maximum_disk_temp | sensor |
| `sensor.mediastorage_volume_1_status` | mediastorage (Volume 1) Status | sensor |
| `sensor.mediastorage_volume_1_total_size` | sensor.mediastorage_volume_1_total_size | sensor |
| `sensor.mediastorage_volume_1_used_space` | mediastorage (Volume 1) Used space | sensor |
| `sensor.mediastorage_volume_1_volume_used` | mediastorage (Volume 1) Volume used | sensor |
| `sensor.nvr_link_speed` | sensor.nvr_link_speed | sensor |
| `sensor.r2d2_cpu_load_average_1_min` | sensor.r2d2_cpu_load_average_1_min | sensor |
| `sensor.r2d2_cpu_load_average_15_min` | R2D2 CPU load average (15 min) | sensor |
| `sensor.r2d2_cpu_load_average_5_min` | R2D2 CPU load average (5 min) | sensor |
| `sensor.r2d2_cpu_utilization_other` | sensor.r2d2_cpu_utilization_other | sensor |
| `sensor.r2d2_cpu_utilization_system` | sensor.r2d2_cpu_utilization_system | sensor |
| `sensor.r2d2_cpu_utilization_total` | R2D2 CPU utilization (total) | sensor |
| `sensor.r2d2_cpu_utilization_user` | R2D2 CPU utilization (user) | sensor |
| `sensor.r2d2_download_throughput` | R2D2 Download throughput | sensor |
| `sensor.r2d2_drive_1_status` | R2D2 (Drive 1) Status | sensor |
| `sensor.r2d2_drive_1_status_smart` | sensor.r2d2_drive_1_status_smart | sensor |
| `sensor.r2d2_drive_1_temperature` | R2D2 (Drive 1) Temperature | sensor |
| `sensor.r2d2_drive_2_status` | R2D2 (Drive 2) Status | sensor |
| `sensor.r2d2_drive_2_status_smart` | sensor.r2d2_drive_2_status_smart | sensor |
| `sensor.r2d2_drive_2_temperature` | R2D2 (Drive 2) Temperature | sensor |
| `sensor.r2d2_drive_3_status` | R2D2 (Drive 3) Status | sensor |
| `sensor.r2d2_drive_3_status_smart` | sensor.r2d2_drive_3_status_smart | sensor |
| `sensor.r2d2_drive_3_temperature` | R2D2 (Drive 3) Temperature | sensor |
| `sensor.r2d2_last_boot` | sensor.r2d2_last_boot | sensor |
| `sensor.r2d2_link_speed_2` | sensor.r2d2_link_speed_2 | sensor |
| `sensor.r2d2_m_2_drive_1_status` | R2D2 (M.2 Drive 1) Status | sensor |
| `sensor.r2d2_m_2_drive_1_status_smart` | sensor.r2d2_m_2_drive_1_status_smart | sensor |
| `sensor.r2d2_m_2_drive_1_temperature` | R2D2 (M.2 Drive 1) Temperature | sensor |
| `sensor.r2d2_m_2_drive_2_status` | R2D2 (M.2 Drive 2) Status | sensor |
| `sensor.r2d2_m_2_drive_2_status_smart` | sensor.r2d2_m_2_drive_2_status_smart | sensor |
| `sensor.r2d2_m_2_drive_2_temperature` | R2D2 (M.2 Drive 2) Temperature | sensor |
| `sensor.r2d2_memory_available_real` | R2D2 Memory available (real) | sensor |
| `sensor.r2d2_memory_available_swap` | R2D2 Memory available (swap) | sensor |
| `sensor.r2d2_memory_cached` | sensor.r2d2_memory_cached | sensor |
| `sensor.r2d2_memory_size` | sensor.r2d2_memory_size | sensor |
| `sensor.r2d2_memory_total_real` | R2D2 Memory total (real) | sensor |
| `sensor.r2d2_memory_total_swap` | R2D2 Memory total (swap) | sensor |
| `sensor.r2d2_memory_usage_real` | R2D2 Memory usage (real) | sensor |
| `sensor.r2d2_temperature` | R2D2 Temperature | sensor |
| `sensor.r2d2_upload_throughput` | R2D2 Upload throughput | sensor |
| `sensor.r2d2_volume_1_average_disk_temp` | R2D2 (Volume 1) Average disk temp | sensor |
| `sensor.r2d2_volume_1_maximum_disk_temp` | sensor.r2d2_volume_1_maximum_disk_temp | sensor |
| `sensor.r2d2_volume_1_status` | R2D2 (Volume 1) Status | sensor |
| `sensor.r2d2_volume_1_total_size` | sensor.r2d2_volume_1_total_size | sensor |
| `sensor.r2d2_volume_1_used_space` | R2D2 (Volume 1) Used space | sensor |
| `sensor.r2d2_volume_1_volume_used` | R2D2 (Volume 1) Volume used | sensor |
| `sensor.server_rack_airguard_th_battery` | Server Rack AirGuard TH Battery | sensor |
| `sensor.server_rack_airguard_th_humidity` | Server Rack AirGuard TH Humidity | sensor |
| `sensor.server_rack_airguard_th_temperature` | Server Rack AirGuard TH Temperature | sensor |
| `sensor.server_rack_airguard_th_voltage` | Server Rack AirGuard TH Voltage | sensor |
| `sensor.speedtest_download` | SpeedTest Download | sensor |
| `sensor.speedtest_ping` | SpeedTest Ping | sensor |
| `sensor.speedtest_upload` | SpeedTest Upload | sensor |
| `sensor.tripp_lite_ups_battery_charge` | Tripp_Lite_Ups Battery charge | sensor |
| `sensor.tripp_lite_ups_battery_chemistry` | Tripp_Lite_Ups Battery chemistry | sensor |
| `sensor.tripp_lite_ups_battery_runtime` | Tripp_Lite_Ups Battery runtime | sensor |
| `sensor.tripp_lite_ups_battery_voltage` | Tripp_Lite_Ups Battery voltage | sensor |
| `sensor.tripp_lite_ups_beeper_status` | Tripp_Lite_Ups Beeper status | sensor |
| `sensor.tripp_lite_ups_current_apparent_power` | Tripp_Lite_Ups Apparent power | sensor |
| `sensor.tripp_lite_ups_input_line_frequency` | Tripp_Lite_Ups Input frequency | sensor |
| `sensor.tripp_lite_ups_input_voltage` | Tripp_Lite_Ups Input voltage | sensor |
| `sensor.tripp_lite_ups_load` | Tripp_Lite_Ups Load | sensor |
| `sensor.tripp_lite_ups_load_reboot_timer` | Tripp_Lite_Ups Load reboot timer | sensor |
| `sensor.tripp_lite_ups_load_shutdown_timer` | Tripp_Lite_Ups Load shutdown timer | sensor |
| `sensor.tripp_lite_ups_nominal_battery_voltage` | Tripp_Lite_Ups Nominal battery voltage | sensor |
| `sensor.tripp_lite_ups_nominal_input_voltage` | Tripp_Lite_Ups Nominal input voltage | sensor |
| `sensor.tripp_lite_ups_nominal_output_frequency` | Tripp_Lite_Ups Nominal output frequency | sensor |
| `sensor.tripp_lite_ups_nominal_output_voltage` | Tripp_Lite_Ups Nominal output voltage | sensor |
| `sensor.tripp_lite_ups_nominal_power` | Tripp_Lite_Ups Nominal power | sensor |
| `sensor.tripp_lite_ups_output_voltage` | Tripp_Lite_Ups Output voltage | sensor |
| `sensor.tripp_lite_ups_self_test_result` | Tripp_Lite_Ups Self-test result | sensor |
| `sensor.tripp_lite_ups_status` | Tripp_Lite_Ups Status | sensor |
| `sensor.tripp_lite_ups_status_data` | Tripp_Lite_Ups Status data | sensor |
| `sensor.tripp_lite_ups_ups_shutdown_delay` | Tripp_Lite_Ups UPS shutdown delay | sensor |
| `sensor.tripp_lite_ups_watchdog_status` | Tripp_Lite_Ups Watchdog status | sensor |
| `update.mediastorage_dsm_update` | mediastorage DSM update | update |
| `update.r2d2_dsm_update` | R2D2 DSM update | update |
| `update.server_rack_airguard_th` | Server Rack AirGuard TH | update |
