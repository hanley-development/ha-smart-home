# Utility Room

> Read-only Home Assistant inventory captured 2026-08-24. No devices or configuration were changed.

- Floor classification: Basement
- Area: Utility Room
- Devices: 12
- Entities: 225
- Inclusion rule: assigned to this Basement-floor area.

## Devices

| Device | Manufacturer | Model | Integration | Device ID |
|---|---|---|---|---|
| Basement Deep Freezer Door | SONOFF | Contact sensor | zigbee2mqtt | `9d8635354fcaafebf89fe1be4ea26079` |
| Dehumidifier | TP-Link | KP115 | tplink | `7b15d1eb6d0eb1c39f6a6ed0fee4fdee` |
| dehumidifier-kp115-plug | TP-Link | KP115 | unknown | `b0890243ecce1e4f921c51082b562e1f` |
| flo-48701e066fc4 | Flo by Moen | flo_device_100_v2 | unknown | `628bef8b6952ca3267b56e7fe37618b5` |
| Furnace | Emporia | VUE002 | emporia_vue | `0e9fda61fb030e53010822080b60aa89` |
| Intelis Gas Meter | Itron | Itron ERG-7100-005 | mqtt | `0f01bf81728d2cda81da542b0a40c542` |
| Sense 252685 | Sense Labs, Inc. | Sense | sense | `ebbfd38db77ec510cc3291af264a8f71` |
| Sub Panel | Emporia | VUE002 | emporia_vue | `45e9afcb29def01e5e176930d455cacb` |
| Sump Pump | Zooz | ZEN15 | zwave_js | `9c3f19bf654166ffee6b6511ed219f06` |
| Utility Room Light | Inovelli | VZW31-SN | zwave_js | `830d32d6b600e5cdec05df0f42105bc2` |
| Water ERT Module | Itron | 100W+ Water ERT Module | mqtt | `c07684711ee9c32fdad3554f1c41fbb9` |
| Water monitor | Flo by Moen | flo_device_100_v2 | flo | `7547f115fcbfff2876dc417ed49feeb9` |

## Entities

| Entity ID | Friendly name | Domain |
|---|---|---|
| `automation.dehumidifier` | Dehumidifier | automation |
| `binary_sensor.basement_deep_freezer_door_battery_low` | Basement Deep Freezer Door Battery | binary_sensor |
| `binary_sensor.basement_deep_freezer_door_contact` | Basement Deep Freezer Door Door | binary_sensor |
| `binary_sensor.basement_deep_freezer_door_tamper` | Basement Deep Freezer Door Tamper | binary_sensor |
| `binary_sensor.dehumidifier_cloud_connection` | Dehumidifier Cloud connection | binary_sensor |
| `binary_sensor.sump_pump` | Sump pump Power | binary_sensor |
| `binary_sensor.water_monitor_pending_system_alerts` | Water monitor Pending system alerts | binary_sensor |
| `button.dehumidifier_restart` | button.dehumidifier_restart | button |
| `button.sump_pump_ping` | Sump Pump Ping | button |
| `button.sump_pump_reset_accumulated_values` | Sump Pump Reset accumulated values | button |
| `button.utility_room_light_identify` | Utility Room Light Identify | button |
| `button.utility_room_light_ping` | Utility Room Light Ping | button |
| `button.utility_room_light_reset_accumulated_values` | Utility Room Light Reset accumulated values | button |
| `device_tracker.dehumidifier_plug` | dehumidifier-kp115-plug Dehumidifier KP115 Plug | device_tracker |
| `device_tracker.flo` | flo-48701e066fc4 flo-48701e066fc4 | device_tracker |
| `event.sump_pump_scene_id` | Sump Pump Scene ID | event |
| `event.utility_room_light_scene_001` | Utility Room Light Scene 001 | event |
| `event.utility_room_light_scene_002` | Utility Room Light Scene 002 | event |
| `event.utility_room_light_scene_003` | Utility Room Light Scene 003 | event |
| `input_number.desired_humidity` | Desired Humidity | input_number |
| `light.utility_room_light` | Utility Room Light | light |
| `number.sump_pump_auto_off_timer` | number.sump_pump_auto_off_timer | number |
| `number.sump_pump_auto_on_timer` | number.sump_pump_auto_on_timer | number |
| `number.sump_pump_electricity_report_frequency` | number.sump_pump_electricity_report_frequency | number |
| `number.sump_pump_energy_report_frequency` | number.sump_pump_energy_report_frequency | number |
| `number.sump_pump_power_report_frequency` | number.sump_pump_power_report_frequency | number |
| `number.sump_pump_power_report_percentage_threshold` | number.sump_pump_power_report_percentage_threshold | number |
| `number.sump_pump_power_report_value_threshold` | number.sump_pump_power_report_value_threshold | number |
| `number.sump_pump_voltage_report_frequency` | number.sump_pump_voltage_report_frequency | number |
| `number.utility_room_light_all_led_strip_effect_color` | number.utility_room_light_all_led_strip_effect_color | number |
| `number.utility_room_light_all_led_strip_effect_duration` | number.utility_room_light_all_led_strip_effect_duration | number |
| `number.utility_room_light_all_led_strip_effect_level` | number.utility_room_light_all_led_strip_effect_level | number |
| `number.utility_room_light_auto_off_timer` | number.utility_room_light_auto_off_timer | number |
| `number.utility_room_light_default_all_led_strip_brightness_when_off` | number.utility_room_light_default_all_led_strip_brightness_when_off | number |
| `number.utility_room_light_default_all_led_strip_brightness_when_on` | number.utility_room_light_default_all_led_strip_brightness_when_on | number |
| `number.utility_room_light_default_all_led_strip_color_when_off` | number.utility_room_light_default_all_led_strip_color_when_off | number |
| `number.utility_room_light_default_all_led_strip_color_when_on` | number.utility_room_light_default_all_led_strip_color_when_on | number |
| `number.utility_room_light_default_level_local` | number.utility_room_light_default_level_local | number |
| `number.utility_room_light_default_level_remote` | number.utility_room_light_default_level_remote | number |
| `number.utility_room_light_dimming_speed_down_local` | number.utility_room_light_dimming_speed_down_local | number |
| `number.utility_room_light_dimming_speed_down_remote` | number.utility_room_light_dimming_speed_down_remote | number |
| `number.utility_room_light_dimming_speed_up_local` | number.utility_room_light_dimming_speed_up_local | number |
| `number.utility_room_light_dimming_speed_up_remote` | number.utility_room_light_dimming_speed_up_remote | number |
| `number.utility_room_light_double_down_level` | number.utility_room_light_double_down_level | number |
| `number.utility_room_light_double_up_level` | number.utility_room_light_double_up_level | number |
| `number.utility_room_light_energy_change_report_threshold` | number.utility_room_light_energy_change_report_threshold | number |
| `number.utility_room_light_indicator_value` | number.utility_room_light_indicator_value | number |
| `number.utility_room_light_led1_strip_effect_color` | number.utility_room_light_led1_strip_effect_color | number |
| `number.utility_room_light_led1_strip_effect_duration` | number.utility_room_light_led1_strip_effect_duration | number |
| `number.utility_room_light_led1_strip_effect_level` | number.utility_room_light_led1_strip_effect_level | number |
| `number.utility_room_light_led2_strip_effect_color` | number.utility_room_light_led2_strip_effect_color | number |
| `number.utility_room_light_led2_strip_effect_duration` | number.utility_room_light_led2_strip_effect_duration | number |
| `number.utility_room_light_led2_strip_effect_level` | number.utility_room_light_led2_strip_effect_level | number |
| `number.utility_room_light_led3_strip_effect_color` | number.utility_room_light_led3_strip_effect_color | number |
| `number.utility_room_light_led3_strip_effect_duration` | number.utility_room_light_led3_strip_effect_duration | number |
| `number.utility_room_light_led3_strip_effect_level` | number.utility_room_light_led3_strip_effect_level | number |
| `number.utility_room_light_led4_strip_effect_color` | number.utility_room_light_led4_strip_effect_color | number |
| `number.utility_room_light_led4_strip_effect_duration` | number.utility_room_light_led4_strip_effect_duration | number |
| `number.utility_room_light_led4_strip_effect_level` | number.utility_room_light_led4_strip_effect_level | number |
| `number.utility_room_light_led5_strip_effect_color` | number.utility_room_light_led5_strip_effect_color | number |
| `number.utility_room_light_led5_strip_effect_duration` | number.utility_room_light_led5_strip_effect_duration | number |
| `number.utility_room_light_led5_strip_effect_level` | number.utility_room_light_led5_strip_effect_level | number |
| `number.utility_room_light_led6_strip_effect_color` | number.utility_room_light_led6_strip_effect_color | number |
| `number.utility_room_light_led6_strip_effect_duration` | number.utility_room_light_led6_strip_effect_duration | number |
| `number.utility_room_light_led6_strip_effect_level` | number.utility_room_light_led6_strip_effect_level | number |
| `number.utility_room_light_led7_strip_effect_color` | number.utility_room_light_led7_strip_effect_color | number |
| `number.utility_room_light_led7_strip_effect_duration` | number.utility_room_light_led7_strip_effect_duration | number |
| `number.utility_room_light_led7_strip_effect_level` | number.utility_room_light_led7_strip_effect_level | number |
| `number.utility_room_light_level_after_power_restored` | number.utility_room_light_level_after_power_restored | number |
| `number.utility_room_light_load_level_indicator_timeout` | number.utility_room_light_load_level_indicator_timeout | number |
| `number.utility_room_light_maximum_level` | number.utility_room_light_maximum_level | number |
| `number.utility_room_light_minimum_level` | number.utility_room_light_minimum_level | number |
| `number.utility_room_light_power_change_report_threshold` | number.utility_room_light_power_change_report_threshold | number |
| `number.utility_room_light_power_energy_report_interval` | number.utility_room_light_power_energy_report_interval | number |
| `number.utility_room_light_ramp_rate_off_to_on_local` | number.utility_room_light_ramp_rate_off_to_on_local | number |
| `number.utility_room_light_ramp_rate_off_to_on_remote` | number.utility_room_light_ramp_rate_off_to_on_remote | number |
| `number.utility_room_light_ramp_rate_on_to_off_local` | number.utility_room_light_ramp_rate_on_to_off_local | number |
| `number.utility_room_light_ramp_rate_on_to_off_remote` | number.utility_room_light_ramp_rate_on_to_off_remote | number |
| `select.sump_pump_led_power_consumption_indicator` | select.sump_pump_led_power_consumption_indicator | select |
| `select.sump_pump_manual_control` | select.sump_pump_manual_control | select |
| `select.sump_pump_on_off_status_change_notifications` | select.sump_pump_on_off_status_change_notifications | select |
| `select.sump_pump_overload_protection` | select.sump_pump_overload_protection | select |
| `select.sump_pump_state_after_power_failure` | select.sump_pump_state_after_power_failure | select |
| `select.sump_pump_z_wave_off_control` | select.sump_pump_z_wave_off_control | select |
| `select.sump_pump_z_wave_on_control` | select.sump_pump_z_wave_on_control | select |
| `select.utility_room_light_all_led_strip_effect_effect` | select.utility_room_light_all_led_strip_effect_effect | select |
| `select.utility_room_light_aux_switch_scenes` | select.utility_room_light_aux_switch_scenes | select |
| `select.utility_room_light_button_delay_time` | select.utility_room_light_button_delay_time | select |
| `select.utility_room_light_dimmer_mode` | select.utility_room_light_dimmer_mode | select |
| `select.utility_room_light_double_down_level_enable` | select.utility_room_light_double_down_level_enable | select |
| `select.utility_room_light_double_tap_config_to_clear_notification` | select.utility_room_light_double_tap_config_to_clear_notification | select |
| `select.utility_room_light_double_up_level_enable` | select.utility_room_light_double_up_level_enable | select |
| `select.utility_room_light_exclusion_behavior` | select.utility_room_light_exclusion_behavior | select |
| `select.utility_room_light_firmware_progress_led` | select.utility_room_light_firmware_progress_led | select |
| `select.utility_room_light_forward_z_wave_commands_to_associated_devices` | select.utility_room_light_forward_z_wave_commands_to_associated_devices | select |
| `select.utility_room_light_increase_output_power_non_neutral` | select.utility_room_light_increase_output_power_non_neutral | select |
| `select.utility_room_light_invert_switch` | select.utility_room_light_invert_switch | select |
| `select.utility_room_light_led_bar_in_on_off_mode` | select.utility_room_light_led_bar_in_on_off_mode | select |
| `select.utility_room_light_led_brightness_scaling` | select.utility_room_light_led_brightness_scaling | select |
| `select.utility_room_light_led1_strip_effect_effect` | select.utility_room_light_led1_strip_effect_effect | select |
| `select.utility_room_light_led2_strip_effect_effect` | select.utility_room_light_led2_strip_effect_effect | select |
| `select.utility_room_light_led3_strip_effect_effect` | select.utility_room_light_led3_strip_effect_effect | select |
| `select.utility_room_light_led4_strip_effect_effect` | select.utility_room_light_led4_strip_effect_effect | select |
| `select.utility_room_light_led5_strip_effect_effect` | select.utility_room_light_led5_strip_effect_effect | select |
| `select.utility_room_light_led6_strip_effect_effect` | select.utility_room_light_led6_strip_effect_effect | select |
| `select.utility_room_light_led7_strip_effect_effect` | select.utility_room_light_led7_strip_effect_effect | select |
| `select.utility_room_light_local_protection_state` | Utility Room Light Local protection state | select |
| `select.utility_room_light_relay_click_in_on_off_mode` | select.utility_room_light_relay_click_in_on_off_mode | select |
| `select.utility_room_light_rf_protection_state` | Utility Room Light RF protection state | select |
| `select.utility_room_light_send_local_commands_to_associated_devices` | select.utility_room_light_send_local_commands_to_associated_devices | select |
| `select.utility_room_light_smart_bulb_mode` | select.utility_room_light_smart_bulb_mode | select |
| `select.utility_room_light_switch_type` | select.utility_room_light_switch_type | select |
| `sensor.0xa4c138121e6bffff_last_seen` | sensor.0xa4c138121e6bffff_last_seen | sensor |
| `sensor.0xa4c138121e6bffff_linkquality` | sensor.0xa4c138121e6bffff_linkquality | sensor |
| `sensor.basement_deep_freezer_door_battery` | Basement Deep Freezer Door Battery | sensor |
| `sensor.basement_deep_freezer_door_voltage` | Basement Deep Freezer Door Voltage | sensor |
| `sensor.city_of_lees_ummit_water_gal_mqtt_rtlamr` | Water ERT Module city_of_lees_ummit_water_gal_mqtt_rtlamr | sensor |
| `sensor.daily_from_grid` | Sense 252685 Daily From Grid | sensor |
| `sensor.daily_net_production` | Sense 252685 Daily Net Production | sensor |
| `sensor.daily_net_production_percentage` | Sense 252685 Daily Net Production Percentage | sensor |
| `sensor.daily_production` | Sense 252685 Daily Production | sensor |
| `sensor.daily_solar_powered_percentage` | Sense 252685 Daily Solar Powered Percentage | sensor |
| `sensor.daily_to_grid` | Sense 252685 Daily To Grid | sensor |
| `sensor.daily_usage` | Sense 252685 Daily Energy | sensor |
| `sensor.dehumidifier_current` | Dehumidifier Current | sensor |
| `sensor.dehumidifier_current_consumption` | Dehumidifier Current consumption | sensor |
| `sensor.dehumidifier_on_since` | sensor.dehumidifier_on_since | sensor |
| `sensor.dehumidifier_signal_strength` | sensor.dehumidifier_signal_strength | sensor |
| `sensor.dehumidifier_this_month_s_consumption` | Dehumidifier This month's consumption | sensor |
| `sensor.dehumidifier_today_s_consumption` | Dehumidifier Today's consumption | sensor |
| `sensor.dehumidifier_total_consumption` | Dehumidifier Total consumption | sensor |
| `sensor.dehumidifier_voltage` | Dehumidifier Voltage | sensor |
| `sensor.energy_production` | Sense 252685 Production | sensor |
| `sensor.energy_usage` | Sense 252685 Energy | sensor |
| `sensor.furnace_3_1d` | Furnace 3 1D | sensor |
| `sensor.furnace_3_1min` | Furnace Power Minute Average | sensor |
| `sensor.furnace_3_1mon` | Furnace 3 1MON | sensor |
| `sensor.gas_utility_daily` | Intelis Gas Meter Gas Utility Daily | sensor |
| `sensor.gas_utility_hourly` | Intelis Gas Meter Gas Utility Hourly | sensor |
| `sensor.gas_utility_montly` | Intelis Gas Meter Gas Utility Montly | sensor |
| `sensor.gas_utility_weekly` | Intelis Gas Meter Gas Utility Weekly | sensor |
| `sensor.l1_voltage` | Sense 252685 L1 Voltage | sensor |
| `sensor.l2_voltage` | Sense 252685 L2 Voltage | sensor |
| `sensor.monthly_from_grid` | Sense 252685 Monthly From Grid | sensor |
| `sensor.monthly_net_production` | Sense 252685 Monthly Net Production | sensor |
| `sensor.monthly_net_production_percentage` | Sense 252685 Monthly Net Production Percentage | sensor |
| `sensor.monthly_production` | Sense 252685 Monthly Production | sensor |
| `sensor.monthly_solar_powered_percentage` | Sense 252685 Monthly Solar Powered Percentage | sensor |
| `sensor.monthly_to_grid` | Sense 252685 Monthly To Grid | sensor |
| `sensor.monthly_usage` | Sense 252685 Monthly Energy | sensor |
| `sensor.sense_252685_bill_energy` | Sense 252685 Bill Energy | sensor |
| `sensor.sense_252685_bill_from_grid` | Sense 252685 Bill From Grid | sensor |
| `sensor.sense_252685_bill_net_production` | Sense 252685 Bill Net Production | sensor |
| `sensor.sense_252685_bill_net_production_percentage` | sensor.sense_252685_bill_net_production_percentage | sensor |
| `sensor.sense_252685_bill_production` | Sense 252685 Bill Production | sensor |
| `sensor.sense_252685_bill_solar_powered_percentage` | sensor.sense_252685_bill_solar_powered_percentage | sensor |
| `sensor.sense_252685_bill_to_grid` | Sense 252685 Bill To Grid | sensor |
| `sensor.spire_gas` | Intelis Gas Meter Spire Gas | sensor |
| `sensor.spire_gas_ft3_mqtt_rtlamr` | Intelis Gas Meter spire_gas_ft3_mqtt_rtlamr | sensor |
| `sensor.sub_panel_123_1d` | Sub Panel Energy Today | sensor |
| `sensor.sub_panel_123_1min` | Sub Panel Power Minute Average | sensor |
| `sensor.sub_panel_123_1mon` | Sub Panel Energy This Month | sensor |
| `sensor.sump_pump_basic` | Sump Pump Basic | sensor |
| `sensor.sump_pump_commands_dropped_rx` | sensor.sump_pump_commands_dropped_rx | sensor |
| `sensor.sump_pump_commands_dropped_tx` | sensor.sump_pump_commands_dropped_tx | sensor |
| `sensor.sump_pump_electric_a` | Sump Pump Electric [A] | sensor |
| `sensor.sump_pump_electric_consumption_a` | Sump Pump Electric Consumption [A] | sensor |
| `sensor.sump_pump_electric_consumption_kwh` | Sump Pump Electric Consumption [kWh] | sensor |
| `sensor.sump_pump_electric_consumption_v` | Sump Pump Electric Consumption [V] | sensor |
| `sensor.sump_pump_electric_consumption_w` | Sump Pump Electric Consumption [W] | sensor |
| `sensor.sump_pump_electric_w` | Sump Pump Electric [W] | sensor |
| `sensor.sump_pump_electric_w_2` | Sump Pump Electric [W] | sensor |
| `sensor.sump_pump_last_seen` | Sump Pump Last seen | sensor |
| `sensor.sump_pump_node_status` | Sump Pump Node status | sensor |
| `sensor.sump_pump_round_trip_time` | sensor.sump_pump_round_trip_time | sensor |
| `sensor.sump_pump_rssi` | sensor.sump_pump_rssi | sensor |
| `sensor.sump_pump_successful_commands_rx` | sensor.sump_pump_successful_commands_rx | sensor |
| `sensor.sump_pump_successful_commands_tx` | sensor.sump_pump_successful_commands_tx | sensor |
| `sensor.sump_pump_timed_out_responses` | sensor.sump_pump_timed_out_responses | sensor |
| `sensor.sump_pump_usage` | Sump pump Power | sensor |
| `sensor.utility_room_light_commands_dropped_rx` | sensor.utility_room_light_commands_dropped_rx | sensor |
| `sensor.utility_room_light_commands_dropped_tx` | sensor.utility_room_light_commands_dropped_tx | sensor |
| `sensor.utility_room_light_dimming_mode` | sensor.utility_room_light_dimming_mode | sensor |
| `sensor.utility_room_light_electric_consumption_kwh` | Utility Room Light Electric Consumption [kWh] | sensor |
| `sensor.utility_room_light_electric_consumption_w` | Utility Room Light Electric Consumption [W] | sensor |
| `sensor.utility_room_light_internal_temperature` | sensor.utility_room_light_internal_temperature | sensor |
| `sensor.utility_room_light_last_seen` | sensor.utility_room_light_last_seen | sensor |
| `sensor.utility_room_light_node_status` | Utility Room Light Node status | sensor |
| `sensor.utility_room_light_overheat_detected` | sensor.utility_room_light_overheat_detected | sensor |
| `sensor.utility_room_light_power_type` | sensor.utility_room_light_power_type | sensor |
| `sensor.utility_room_light_round_trip_time` | sensor.utility_room_light_round_trip_time | sensor |
| `sensor.utility_room_light_signal_strength` | sensor.utility_room_light_signal_strength | sensor |
| `sensor.utility_room_light_successful_commands_rx` | sensor.utility_room_light_successful_commands_rx | sensor |
| `sensor.utility_room_light_successful_commands_tx` | sensor.utility_room_light_successful_commands_tx | sensor |
| `sensor.utility_room_light_timed_out_responses` | sensor.utility_room_light_timed_out_responses | sensor |
| `sensor.water_monitor_current_system_mode` | Water monitor Current system mode | sensor |
| `sensor.water_monitor_today_s_water_usage` | Water monitor Today's water usage | sensor |
| `sensor.water_monitor_water_flow_rate` | Water monitor Water flow rate | sensor |
| `sensor.water_monitor_water_pressure` | Water monitor Water pressure | sensor |
| `sensor.water_monitor_water_temperature` | Water monitor Water temperature | sensor |
| `sensor.water_utility_meter_daily` | Water monitor Water Utility Meter Daily | sensor |
| `sensor.water_utility_meter_hourly` | Water monitor Water Utility Meter Hourly | sensor |
| `sensor.water_utility_meter_monthly` | Water monitor Water Utility Meter Monthly | sensor |
| `sensor.water_utility_meter_weekly` | Water monitor Water Utility Meter Weekly | sensor |
| `sensor.weekly_from_grid` | Sense 252685 Weekly From Grid | sensor |
| `sensor.weekly_net_production` | Sense 252685 Weekly Net Production | sensor |
| `sensor.weekly_net_production_percentage` | Sense 252685 Weekly Net Production Percentage | sensor |
| `sensor.weekly_production` | Sense 252685 Weekly Production | sensor |
| `sensor.weekly_solar_powered_percentage` | Sense 252685 Weekly Solar Powered Percentage | sensor |
| `sensor.weekly_to_grid` | Sense 252685 Weekly To Grid | sensor |
| `sensor.weekly_usage` | Sense 252685 Weekly Energy | sensor |
| `sensor.yearly_from_grid` | Sense 252685 Yearly From Grid | sensor |
| `sensor.yearly_net_production` | Sense 252685 Yearly Net Production | sensor |
| `sensor.yearly_net_production_percentage` | Sense 252685 Yearly Net Production Percentage | sensor |
| `sensor.yearly_production` | Sense 252685 Yearly Production | sensor |
| `sensor.yearly_solar_powered_percentage` | Sense 252685 Yearly Solar Powered Percentage | sensor |
| `sensor.yearly_to_grid` | Sense 252685 Yearly To Grid | sensor |
| `sensor.yearly_usage` | Sense 252685 Yearly Energy | sensor |
| `switch.dehumidifier` | Dehumidifier | switch |
| `switch.dehumidifier_led` | Dehumidifier LED | switch |
| `switch.sump_pump` | Sump Pump | switch |
| `switch.water_monitor_shutoff_valve` | Water monitor Shutoff valve | switch |
| `update.basement_deep_freezer_door` | Basement Deep Freezer Door | update |
| `update.sump_pump_firmware` | Sump Pump Firmware | update |
| `update.utility_room_light_firmware` | Utility Room Light Firmware | update |
