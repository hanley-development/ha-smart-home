# Basement Entertainment

> Read-only Home Assistant inventory captured 2026-08-24. No devices or configuration were changed.

- Floor classification: Basement
- Area: Basement Entertainment
- Devices: 22
- Entities: 174
- Inclusion rule: assigned to this Basement-floor area.

## Devices

| Device | Manufacturer | Model | Integration | Device ID |
|---|---|---|---|---|
| Basement Echo | Amazon | Echo | alexa_devices | `089d3309ad2bb79d4244a72a7259aa04` |
| Basement Ecobee Sensor | ecobee | ecobee Room Sensor | ecobee | `a39d95fb25729226aaf8d3de386c184e` |
| Basement Entertainment Surge Protector | TP-Link | HS300 | tplink | `801569ea0c8ded6246ebaa0eeb6aeca4` |
| Basement FireTV | Amazon | Amazon Fire TV stick | alexa_devices | `9df983ce066f839099f015b18b7f4dee` |
| Basement FireTV | Amazon | Fire TV Stick 4K (Gen3) | alexa_media | `066dddd8ad94bfd7aaccbf047a4dfb79` |
| Basement Mini-Fridge Door | SONOFF | Contact sensor | zigbee2mqtt | `333a5728c4368d232bb79d59f242775e` |
| Basement Onkyo Receiver | Onkyo | Onkyo TX-NR7100 | cast | `faa690e549fb70030c951db1d21f90bb` |
| Basement Receiver | Onkyo Sound & Vision Corporation | Onkyo 9-Channel Network A/V Receiver | alexa_devices | `814893658386057cbf43d91faa541109` |
| Basement Receiver | Amazon | UNKNOWN A5MSGHEC5FTLM | alexa_media | `ba6fb15e237bb4ba230e5d38f1d794e5` |
| Sofa Surge Protector | TP-Link | HS300 | tplink | `978e64633c277bb884997aed96b620a2` |
| TP-LINK_Power Strip_4AA0 Basement Amazon Fire Outlet | TP-Link | Socket for HS300(US) | tplink | `2e6d80cdd642c2148bb6a736a4ab10d5` |
| TP-LINK_Power Strip_4AA0 Basement Entertainment Outlet 5 | TP-Link | Socket for HS300(US) | tplink | `b0374f07a1341241b17a6ce8937ea4a1` |
| TP-LINK_Power Strip_4AA0 Basement Entertainment Outlet 6 | TP-Link | Socket for HS300(US) | tplink | `8b88de44f4bbde51e5188d6082c75d54` |
| TP-LINK_Power Strip_4AA0 Left Subwoofer Outlet | TP-Link | Socket for HS300(US) | tplink | `b5cba540ca945e81765b2caf5818ecd7` |
| TP-LINK_Power Strip_4AA0 Onkyo Receiver Outlet | TP-Link | Socket for HS300(US) | tplink | `90da941f5c230ac0e6adc5cd38ece14b` |
| TP-LINK_Power Strip_4AA0 Right Subwoofer Outlet | TP-Link | Socket for HS300(US) | tplink | `9c5092bc9654682e0bc6e29aeaee9451` |
| TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 1 | TP-Link | Socket for HS300(US) | tplink | `d4b5f585ea369426f9706042610f8926` |
| TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 2 | TP-Link | Socket for HS300(US) | tplink | `f48cd3ace7103f0ff543905ac7f5de5f` |
| TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 3 | TP-Link | Socket for HS300(US) | tplink | `799d7fd57d9470c653a179a249d297e2` |
| TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 4 | TP-Link | Socket for HS300(US) | tplink | `48edcb6728ea82618a29fd69b4434a04` |
| TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 5 | TP-Link | Socket for HS300(US) | tplink | `20da3fb27b1eb0fc4fc68b63ed0fc1b3` |
| TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 6 | TP-Link | Socket for HS300(US) | tplink | `a012ebfcdb176563cceffe4d96d2a109` |

## Entities

| Entity ID | Friendly name | Domain |
|---|---|---|
| `binary_sensor.basement_echo_connectivity` | Basement Echo Connectivity | binary_sensor |
| `binary_sensor.basement_ecobee_sensor_occupancy` | Basement Ecobee Sensor Occupancy | binary_sensor |
| `binary_sensor.basement_entertainment_surge_protector_cloud_connection` | Basement Entertainment Surge Protector Cloud connection | binary_sensor |
| `binary_sensor.basement_firetv_connectivity` | Basement FireTV Connectivity | binary_sensor |
| `binary_sensor.basement_mini_fridge_door_battery_low` | Basement Mini-Fridge Door Battery | binary_sensor |
| `binary_sensor.basement_mini_fridge_door_contact` | Basement Mini-Fridge Door Door | binary_sensor |
| `binary_sensor.basement_mini_fridge_door_tamper` | Basement Mini-Fridge Door Tamper | binary_sensor |
| `binary_sensor.basement_receiver_connectivity` | Basement Receiver Connectivity | binary_sensor |
| `binary_sensor.basement_sofa_surge_protector_cloud_connection` | Sofa Surge Protector Cloud connection | binary_sensor |
| `button.basement_echo_restart` | Basement Echo Restart | button |
| `button.basement_entertainment_surge_protector_restart` | button.basement_entertainment_surge_protector_restart | button |
| `button.basement_sofa_surge_protector_restart` | Sofa Surge Protector Restart | button |
| `event.basement_echo_voice_event` | Basement Echo Voice event | event |
| `event.basement_firetv_voice_event` | Basement FireTV Voice event | event |
| `event.basement_receiver_voice_event` | Basement Receiver Voice event | event |
| `media_player.basement_echo_2` | Basement Echo | media_player |
| `media_player.basement_firetv` | Basement FireTV | media_player |
| `media_player.basement_receiver` | Basement Receiver | media_player |
| `media_player.basement_receiver_2` | Basement Receiver | media_player |
| `media_player.onkyo` | Basement Onkyo Receiver | media_player |
| `notify.basement_echo_announce` | Basement Echo Announce | notify |
| `notify.basement_echo_speak` | Basement Echo Speak | notify |
| `notify.basement_receiver_announce` | Basement Receiver Announce | notify |
| `notify.basement_receiver_speak` | Basement Receiver Speak | notify |
| `select.basement_echo_drop_in` | Basement Echo Drop In | select |
| `sensor.0xa4c138127aaaffff_last_seen` | sensor.0xa4c138127aaaffff_last_seen | sensor |
| `sensor.0xa4c138127aaaffff_linkquality` | sensor.0xa4c138127aaaffff_linkquality | sensor |
| `sensor.basement_amazon_fire_outlet_current` | TP-LINK_Power Strip_4AA0 Basement Amazon Fire Outlet Current | sensor |
| `sensor.basement_amazon_fire_outlet_current_consumption` | TP-LINK_Power Strip_4AA0 Basement Amazon Fire Outlet Current consumption | sensor |
| `sensor.basement_amazon_fire_outlet_today_s_consumption` | TP-LINK_Power Strip_4AA0 Basement Amazon Fire Outlet Today's consumption | sensor |
| `sensor.basement_amazon_fire_outlet_total_consumption` | TP-LINK_Power Strip_4AA0 Basement Amazon Fire Outlet Total consumption | sensor |
| `sensor.basement_amazon_fire_outlet_voltage` | TP-LINK_Power Strip_4AA0 Basement Amazon Fire Outlet Voltage | sensor |
| `sensor.basement_echo_illuminance` | Basement Echo Illuminance | sensor |
| `sensor.basement_echo_next_alarm_2` | Basement Echo Next alarm | sensor |
| `sensor.basement_echo_next_reminder_2` | Basement Echo Next reminder | sensor |
| `sensor.basement_echo_next_timer_2` | Basement Echo Next timer | sensor |
| `sensor.basement_ecobee_sensor_temperature` | Basement Ecobee Sensor Temperature | sensor |
| `sensor.basement_entertainment_outlet_5_current` | TP-LINK_Power Strip_4AA0 Basement Entertainment Outlet 5 Current | sensor |
| `sensor.basement_entertainment_outlet_5_current_consumption` | TP-LINK_Power Strip_4AA0 Basement Entertainment Outlet 5 Current consumption | sensor |
| `sensor.basement_entertainment_outlet_5_today_s_consumption` | TP-LINK_Power Strip_4AA0 Basement Entertainment Outlet 5 Today's consumption | sensor |
| `sensor.basement_entertainment_outlet_5_total_consumption` | TP-LINK_Power Strip_4AA0 Basement Entertainment Outlet 5 Total consumption | sensor |
| `sensor.basement_entertainment_outlet_5_voltage` | TP-LINK_Power Strip_4AA0 Basement Entertainment Outlet 5 Voltage | sensor |
| `sensor.basement_entertainment_outlet_6_current` | TP-LINK_Power Strip_4AA0 Basement Entertainment Outlet 6 Current | sensor |
| `sensor.basement_entertainment_outlet_6_current_consumption` | TP-LINK_Power Strip_4AA0 Basement Entertainment Outlet 6 Current consumption | sensor |
| `sensor.basement_entertainment_outlet_6_today_s_consumption` | TP-LINK_Power Strip_4AA0 Basement Entertainment Outlet 6 Today's consumption | sensor |
| `sensor.basement_entertainment_outlet_6_total_consumption` | TP-LINK_Power Strip_4AA0 Basement Entertainment Outlet 6 Total consumption | sensor |
| `sensor.basement_entertainment_outlet_6_voltage` | TP-LINK_Power Strip_4AA0 Basement Entertainment Outlet 6 Voltage | sensor |
| `sensor.basement_entertainment_surge_protector_current` | Basement Entertainment Surge Protector Current | sensor |
| `sensor.basement_entertainment_surge_protector_current_consumption` | Basement Entertainment Surge Protector Current consumption | sensor |
| `sensor.basement_entertainment_surge_protector_on_since` | sensor.basement_entertainment_surge_protector_on_since | sensor |
| `sensor.basement_entertainment_surge_protector_signal_strength` | sensor.basement_entertainment_surge_protector_signal_strength | sensor |
| `sensor.basement_entertainment_surge_protector_this_month_s_consumption` | Basement Entertainment Surge Protector This month's consumption | sensor |
| `sensor.basement_entertainment_surge_protector_today_s_consumption` | Basement Entertainment Surge Protector Today's consumption | sensor |
| `sensor.basement_entertainment_surge_protector_total_consumption` | Basement Entertainment Surge Protector Total consumption | sensor |
| `sensor.basement_entertainment_surge_protector_voltage` | Basement Entertainment Surge Protector Voltage | sensor |
| `sensor.basement_firetv_next_alarm` | Basement FireTV Next alarm | sensor |
| `sensor.basement_firetv_next_alarm_2` | Basement FireTV Next alarm | sensor |
| `sensor.basement_firetv_next_reminder` | Basement FireTV Next reminder | sensor |
| `sensor.basement_firetv_next_reminder_2` | Basement FireTV Next reminder | sensor |
| `sensor.basement_firetv_next_timer` | Basement FireTV Next timer | sensor |
| `sensor.basement_firetv_next_timer_2` | Basement FireTV Next timer | sensor |
| `sensor.basement_mini_fridge_door_battery` | Basement Mini-Fridge Door Battery | sensor |
| `sensor.basement_mini_fridge_door_voltage` | Basement Mini-Fridge Door Voltage | sensor |
| `sensor.basement_receiver_next_alarm` | Basement Receiver Next alarm | sensor |
| `sensor.basement_receiver_next_alarm_2` | Basement Receiver Next alarm | sensor |
| `sensor.basement_receiver_next_reminder` | Basement Receiver Next reminder | sensor |
| `sensor.basement_receiver_next_reminder_2` | Basement Receiver Next reminder | sensor |
| `sensor.basement_receiver_next_timer` | Basement Receiver Next timer | sensor |
| `sensor.basement_receiver_next_timer_2` | Basement Receiver Next timer | sensor |
| `sensor.basement_sofa_surge_protector_current` | Sofa Surge Protector Current | sensor |
| `sensor.basement_sofa_surge_protector_current_consumption` | Sofa Surge Protector Current consumption | sensor |
| `sensor.basement_sofa_surge_protector_on_since` | Sofa Surge Protector On since | sensor |
| `sensor.basement_sofa_surge_protector_signal_strength` | Sofa Surge Protector Signal strength | sensor |
| `sensor.basement_sofa_surge_protector_this_month_s_consumption` | Sofa Surge Protector This month's consumption | sensor |
| `sensor.basement_sofa_surge_protector_today_s_consumption` | Sofa Surge Protector Today's consumption | sensor |
| `sensor.basement_sofa_surge_protector_total_consumption` | Sofa Surge Protector Total consumption | sensor |
| `sensor.basement_sofa_surge_protector_voltage` | Sofa Surge Protector Voltage | sensor |
| `sensor.left_subwoofer_outlet_current` | TP-LINK_Power Strip_4AA0 Left Subwoofer Outlet Current | sensor |
| `sensor.left_subwoofer_outlet_current_consumption` | TP-LINK_Power Strip_4AA0 Left Subwoofer Outlet Current consumption | sensor |
| `sensor.left_subwoofer_outlet_today_s_consumption` | TP-LINK_Power Strip_4AA0 Left Subwoofer Outlet Today's consumption | sensor |
| `sensor.left_subwoofer_outlet_total_consumption` | TP-LINK_Power Strip_4AA0 Left Subwoofer Outlet Total consumption | sensor |
| `sensor.left_subwoofer_outlet_voltage` | TP-LINK_Power Strip_4AA0 Left Subwoofer Outlet Voltage | sensor |
| `sensor.onkyo_receiver_outlet_current` | TP-LINK_Power Strip_4AA0 Onkyo Receiver Outlet Current | sensor |
| `sensor.onkyo_receiver_outlet_current_consumption` | TP-LINK_Power Strip_4AA0 Onkyo Receiver Outlet Current consumption | sensor |
| `sensor.onkyo_receiver_outlet_today_s_consumption` | TP-LINK_Power Strip_4AA0 Onkyo Receiver Outlet Today's consumption | sensor |
| `sensor.onkyo_receiver_outlet_total_consumption` | TP-LINK_Power Strip_4AA0 Onkyo Receiver Outlet Total consumption | sensor |
| `sensor.onkyo_receiver_outlet_voltage` | TP-LINK_Power Strip_4AA0 Onkyo Receiver Outlet Voltage | sensor |
| `sensor.right_subwoofer_outlet_current` | TP-LINK_Power Strip_4AA0 Right Subwoofer Outlet Current | sensor |
| `sensor.right_subwoofer_outlet_current_consumption` | TP-LINK_Power Strip_4AA0 Right Subwoofer Outlet Current consumption | sensor |
| `sensor.right_subwoofer_outlet_today_s_consumption` | TP-LINK_Power Strip_4AA0 Right Subwoofer Outlet Today's consumption | sensor |
| `sensor.right_subwoofer_outlet_total_consumption` | TP-LINK_Power Strip_4AA0 Right Subwoofer Outlet Total consumption | sensor |
| `sensor.right_subwoofer_outlet_voltage` | TP-LINK_Power Strip_4AA0 Right Subwoofer Outlet Voltage | sensor |
| `sensor.sr_basement_camera_current` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 5 Current | sensor |
| `sensor.sr_basement_camera_current_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 5 Current consumption | sensor |
| `sensor.sr_basement_camera_today_s_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 5 Today's consumption | sensor |
| `sensor.sr_basement_camera_total_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 5 Total consumption | sensor |
| `sensor.sr_basement_camera_voltage` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 5 Voltage | sensor |
| `sensor.sr_plug_4_current` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 4 Current | sensor |
| `sensor.sr_plug_4_current_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 4 Current consumption | sensor |
| `sensor.sr_plug_4_today_s_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 4 Today's consumption | sensor |
| `sensor.sr_plug_4_total_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 4 Total consumption | sensor |
| `sensor.sr_plug_4_voltage` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 4 Voltage | sensor |
| `sensor.sr_plug_6_current` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 6 Current | sensor |
| `sensor.sr_plug_6_current_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 6 Current consumption | sensor |
| `sensor.sr_plug_6_today_s_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 6 Today's consumption | sensor |
| `sensor.sr_plug_6_total_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 6 Total consumption | sensor |
| `sensor.sr_plug_6_voltage` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 6 Voltage | sensor |
| `sensor.sr_plug_open_current` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 3 Current | sensor |
| `sensor.sr_plug_open_current_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 3 Current consumption | sensor |
| `sensor.sr_plug_open_today_s_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 3 Today's consumption | sensor |
| `sensor.sr_plug_open_total_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 3 Total consumption | sensor |
| `sensor.sr_plug_open_voltage` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 3 Voltage | sensor |
| `sensor.sr_unifi_150_switch_current` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 2 Current | sensor |
| `sensor.sr_unifi_150_switch_current_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 2 Current consumption | sensor |
| `sensor.sr_unifi_150_switch_today_s_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 2 Today's consumption | sensor |
| `sensor.sr_unifi_150_switch_total_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 2 Total consumption | sensor |
| `sensor.sr_unifi_150_switch_voltage` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 2 Voltage | sensor |
| `sensor.sr_unifi_dream_machine_current` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 1 Current | sensor |
| `sensor.sr_unifi_dream_machine_current_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 1 Current consumption | sensor |
| `sensor.sr_unifi_dream_machine_today_s_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 1 Today's consumption | sensor |
| `sensor.sr_unifi_dream_machine_total_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 1 Total consumption | sensor |
| `sensor.sr_unifi_dream_machine_voltage` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 1 Voltage | sensor |
| `sensor.tp_link_power_strip_4aa0_basement_amazon_fire_outlet_on_since` | sensor.tp_link_power_strip_4aa0_basement_amazon_fire_outlet_on_since | sensor |
| `sensor.tp_link_power_strip_4aa0_basement_amazon_fire_outlet_this_month_s_consumption` | TP-LINK_Power Strip_4AA0 Basement Amazon Fire Outlet This month's consumption | sensor |
| `sensor.tp_link_power_strip_4aa0_basement_entertainment_outlet_5_on_since` | sensor.tp_link_power_strip_4aa0_basement_entertainment_outlet_5_on_since | sensor |
| `sensor.tp_link_power_strip_4aa0_basement_entertainment_outlet_5_this_month_s_consumption` | TP-LINK_Power Strip_4AA0 Basement Entertainment Outlet 5 This month's consumption | sensor |
| `sensor.tp_link_power_strip_4aa0_basement_entertainment_outlet_6_on_since` | sensor.tp_link_power_strip_4aa0_basement_entertainment_outlet_6_on_since | sensor |
| `sensor.tp_link_power_strip_4aa0_basement_entertainment_outlet_6_this_month_s_consumption` | TP-LINK_Power Strip_4AA0 Basement Entertainment Outlet 6 This month's consumption | sensor |
| `sensor.tp_link_power_strip_4aa0_left_subwoofer_outlet_on_since` | sensor.tp_link_power_strip_4aa0_left_subwoofer_outlet_on_since | sensor |
| `sensor.tp_link_power_strip_4aa0_left_subwoofer_outlet_this_month_s_consumption` | TP-LINK_Power Strip_4AA0 Left Subwoofer Outlet This month's consumption | sensor |
| `sensor.tp_link_power_strip_4aa0_onkyo_receiver_outlet_on_since` | sensor.tp_link_power_strip_4aa0_onkyo_receiver_outlet_on_since | sensor |
| `sensor.tp_link_power_strip_4aa0_onkyo_receiver_outlet_this_month_s_consumption` | TP-LINK_Power Strip_4AA0 Onkyo Receiver Outlet This month's consumption | sensor |
| `sensor.tp_link_power_strip_4aa0_right_subwoofer_outlet_on_since` | sensor.tp_link_power_strip_4aa0_right_subwoofer_outlet_on_since | sensor |
| `sensor.tp_link_power_strip_4aa0_right_subwoofer_outlet_this_month_s_consumption` | TP-LINK_Power Strip_4AA0 Right Subwoofer Outlet This month's consumption | sensor |
| `sensor.tp_link_power_strip_d348_sr_open_on_since` | sensor.tp_link_power_strip_d348_sr_open_on_since | sensor |
| `sensor.tp_link_power_strip_d348_sr_open_this_month_s_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 1 This month's consumption | sensor |
| `sensor.tp_link_power_strip_d348_sr_reolink_nvr_on_since` | sensor.tp_link_power_strip_d348_sr_reolink_nvr_on_since | sensor |
| `sensor.tp_link_power_strip_d348_sr_reolink_nvr_this_month_s_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 6 This month's consumption | sensor |
| `sensor.tp_link_power_strip_d348_sr_smartthings_on_since` | sensor.tp_link_power_strip_d348_sr_smartthings_on_since | sensor |
| `sensor.tp_link_power_strip_d348_sr_smartthings_this_month_s_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 4 This month's consumption | sensor |
| `sensor.tp_link_power_strip_d348_sr_synology_nas_on_since` | sensor.tp_link_power_strip_d348_sr_synology_nas_on_since | sensor |
| `sensor.tp_link_power_strip_d348_sr_synology_nas_this_month_s_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 2 This month's consumption | sensor |
| `sensor.tp_link_power_strip_d348_sr_unifi_dream_machine_se_on_since` | sensor.tp_link_power_strip_d348_sr_unifi_dream_machine_se_on_since | sensor |
| `sensor.tp_link_power_strip_d348_sr_unifi_dream_machine_se_this_month_s_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 5 This month's consumption | sensor |
| `sensor.tp_link_power_strip_d348_sr_unifi_switch_150_on_since` | sensor.tp_link_power_strip_d348_sr_unifi_switch_150_on_since | sensor |
| `sensor.tp_link_power_strip_d348_sr_unifi_switch_150_this_month_s_consumption` | TP-LINK_Power Strip_D348 BSMT Living Room - Outlet 3 This month's consumption | sensor |
| `switch.basement_amazon_fire_outlet` | Basement Entertainment Surge Protector Basement Amazon Fire Outlet | switch |
| `switch.basement_echo_announcements` | Basement Echo Announcements | switch |
| `switch.basement_echo_communications` | Basement Echo Communications | switch |
| `switch.basement_echo_do_not_disturb` | Basement Echo Do not disturb | switch |
| `switch.basement_entertainment_outlet_5` | Basement Entertainment Surge Protector Basement Entertainment Outlet 5 | switch |
| `switch.basement_entertainment_outlet_6` | Basement Entertainment Surge Protector Basement Entertainment Outlet 6 | switch |
| `switch.basement_entertainment_surge_protector` | Basement Entertainment Surge Protector | switch |
| `switch.basement_entertainment_surge_protector_led` | Basement Entertainment Surge Protector LED | switch |
| `switch.basement_firetv_announcements` | Basement FireTV Announcements | switch |
| `switch.basement_firetv_communications` | Basement FireTV Communications | switch |
| `switch.basement_firetv_do_not_disturb` | Basement FireTV Do not disturb | switch |
| `switch.basement_firetv_do_not_disturb_switch` | Basement FireTV Do not disturb | switch |
| `switch.basement_receiver_do_not_disturb` | Basement Receiver Do not disturb | switch |
| `switch.basement_receiver_do_not_disturb_switch` | Basement Receiver Do not disturb | switch |
| `switch.basement_receiver_repeat_switch` | Basement Receiver Repeat | switch |
| `switch.basement_receiver_shuffle_switch` | Basement Receiver Shuffle | switch |
| `switch.basement_sofa_surge_protector` | Sofa Surge Protector | switch |
| `switch.basement_sofa_surge_protector_bsmt_living_room_outlet_1` | Sofa Surge Protector BSMT Living Room - Outlet 1 | switch |
| `switch.basement_sofa_surge_protector_bsmt_living_room_outlet_2` | Sofa Surge Protector BSMT Living Room - Outlet 2 | switch |
| `switch.basement_sofa_surge_protector_bsmt_living_room_outlet_3` | Sofa Surge Protector BSMT Living Room - Outlet 3 | switch |
| `switch.basement_sofa_surge_protector_bsmt_living_room_outlet_4` | Sofa Surge Protector BSMT Living Room - Outlet 4 | switch |
| `switch.basement_sofa_surge_protector_bsmt_living_room_outlet_5` | Sofa Surge Protector BSMT Living Room - Outlet 5 | switch |
| `switch.basement_sofa_surge_protector_bsmt_living_room_outlet_6` | Sofa Surge Protector BSMT Living Room - Outlet 6 | switch |
| `switch.basement_sofa_surge_protector_led` | Sofa Surge Protector LED | switch |
| `switch.left_subwoofer_outlet` | Basement Entertainment Surge Protector Left Subwoofer Outlet | switch |
| `switch.onkyo_receiver_outlet` | Basement Entertainment Surge Protector Onkyo Receiver Outlet | switch |
| `switch.right_subwoofer_outlet` | Basement Entertainment Surge Protector Right Subwoofer Outlet | switch |
| `update.basement_mini_fridge_door` | Basement Mini-Fridge Door | update |
