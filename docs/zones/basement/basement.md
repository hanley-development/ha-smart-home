# Basement

> Read-only Home Assistant inventory captured 2026-08-24. No devices or configuration were changed.

- Floor classification: Basement
- Area: Basement
- Devices: 18
- Entities: 692
- Inclusion rule: assigned to this Basement-floor area.

## Devices

| Device | Manufacturer | Model | Integration | Device ID |
|---|---|---|---|---|
| Basement Bar Light | Inovelli | VZW31-SN | zwave_js | `43dff434ef45af9c228b2e1d0be5274d` |
| Basement Core 400 | VeSync | Core400S | vesync | `8783729d922d632a7ca48785dd126195` |
| Basement Echo | Amazon | Echo (Gen2) | alexa_media | `06c6c34df5a70a7ca495b1f122fa01ae` |
| Basement Entertainment Outlet 5 | Sense Labs, Inc. | Sense | sense | `33a960e1204bd76baf7d81e5afa7dac9` |
| Basement Entertainment Outlet 6 | Sense Labs, Inc. | Sense | sense | `58040579a15e84f9f5ca0f7d8fe01497` |
| Basement Entertainment Surge Protector | TP-Link | HS300 | unknown | `83c0f9e8ee312f47d027e6a0438bb821` |
| Basement Hallway Light | Inovelli | VZW31-SN | zwave_js | `5f2a916e6391b5ef7f7870b1bfbfeef2` |
| Basement Living Room Fan | Inovelli | Fan controller | zigbee2mqtt | `1a7e2cf8716fb2232f4db9c239616f6b` |
| Basement Living Room Fan Light | Inovelli | VZW31-SN | zwave_js | `8e7537323b71c98f358ff0600656ee21` |
| Basement Living Room Nightlight Motion | Third Reality | Zigbee multi-function night light | zigbee2mqtt | `0778b990736dfe32ea44d88985029d77` |
| Basement Living Room Surge Protector | TP-Link | HS300 | unknown | `c6af9bea46ed22f333395448ecf4c2bd` |
| Basement Main Light | Inovelli | VZW31-SN | zwave_js | `82a109e57f9455fe4a75e763093b3dcf` |
| Basement Mini-Fridge | Zooz | ZEN15 | zwave_js | `6540f2b1306c534fe9f7771289c50df2` |
| Basement Samsung TV | Samsung Electronics Co.,Ltd | QN85QN90CAFXZA | unknown | `fe58b94aed1e20c94ba7f1d38b60004d` |
| Basement Stairs Light | Inovelli | VZW31-SN | zwave_js | `94ca989a1ba7e164555736e2a89897ae` |
| Onkyo-TX-NR7100 | Onkyo Technology K.K. | TX-NR7100 | unknown | `d42475e3ab7fc67d3e013f71b68159aa` |
| Samsung QN90CA 85 | Samsung | QN85QN90CAFXZA | samsungtv | `fc9201036e841a7ba82711a562a42c75` |
| Samsung QN90CA 85 | Samsung | QN85QN90CAFXZA | unknown | `e091e3f8cba1432fb6b88c5aa4c4c8cf` |

## Entities

| Entity ID | Friendly name | Domain |
|---|---|---|
| `automation.basement_nightlight` | Basement Nightlight | automation |
| `automation.mikes_office_night_light_motion` | Mikes Office Nightlight | automation |
| `automation.movie_time` | Movie Time | automation |
| `binary_sensor.basement_bar_light_overheat` | binary_sensor.basement_bar_light_overheat | binary_sensor |
| `binary_sensor.basement_basement_mini_fridge_over_current_detected` | Basement Mini-Fridge Over-current detected | binary_sensor |
| `binary_sensor.basement_entertainment_outlet_5` | Basement Entertainment Outlet 5 Power | binary_sensor |
| `binary_sensor.basement_entertainment_outlet_6` | Basement Entertainment Outlet 6 Power | binary_sensor |
| `binary_sensor.basement_hallway_light_overheat` | binary_sensor.basement_hallway_light_overheat | binary_sensor |
| `binary_sensor.basement_living_room_nightlight_motion_occupancy` | Basement Living Room Nightlight Motion Occupancy | binary_sensor |
| `binary_sensor.basement_living_room_nightlight_motion_update_available` | binary_sensor.basement_living_room_nightlight_motion_update_available | binary_sensor |
| `binary_sensor.basement_main_light_overheat` | binary_sensor.basement_main_light_overheat | binary_sensor |
| `binary_sensor.basement_stairs_light_overheat` | binary_sensor.basement_stairs_light_overheat | binary_sensor |
| `button.basement_bar_light_identify` | Basement Bar Light Identify | button |
| `button.basement_bar_light_ping` | Basement Bar Light Ping | button |
| `button.basement_bar_light_reset_accumulated_values` | Basement Bar Light Reset accumulated values | button |
| `button.basement_basement_mini_fridge_identify` | Basement Mini-Fridge Identify | button |
| `button.basement_basement_mini_fridge_idle_power_management_over_current_status` | button.basement_basement_mini_fridge_idle_power_management_over_current_status | button |
| `button.basement_basement_mini_fridge_ping` | Basement Mini-Fridge Ping | button |
| `button.basement_basement_mini_fridge_reset_accumulated_values` | Basement Mini-Fridge Reset accumulated values | button |
| `button.basement_hallway_light_identify` | Basement Hallway Light Identify | button |
| `button.basement_hallway_light_ping` | Basement Hallway Light Ping | button |
| `button.basement_hallway_light_reset_accumulated_values` | Basement Hallway Light Reset accumulated values | button |
| `button.basement_living_room_fan_identify` | Basement Living Room Fan Identify | button |
| `button.basement_living_room_fan_light_identify` | Basement Living Room Fan Light Identify | button |
| `button.basement_living_room_fan_light_ping` | Basement Living Room Fan Light Ping | button |
| `button.basement_living_room_fan_light_reset_accumulated_values` | Basement Living Room Fan Light Reset accumulated values | button |
| `button.basement_main_light_identify` | Basement Main Light Identify | button |
| `button.basement_main_light_ping` | Basement Main Light Ping | button |
| `button.basement_main_light_reset_accumulated_values` | Basement Main Light Reset accumulated values | button |
| `button.basement_stairs_light_identify` | Basement Stairs Light Identify | button |
| `button.basement_stairs_light_ping` | Basement Stairs Light Ping | button |
| `button.basement_stairs_light_reset_accumulated_values` | Basement Stairs Light Reset accumulated values | button |
| `device_tracker.basement_entertainment_surge_protector` | Basement Entertainment Surge Protector Bsmt-Entertainment-HS300 | device_tracker |
| `device_tracker.onkyo` | Onkyo-TX-NR7100 Onkyo-TX-NR7100 | device_tracker |
| `device_tracker.samsung` | Basement Samsung TV Basement Samsung TV | device_tracker |
| `device_tracker.server_rack_surge_protector` | Basement Living Room Surge Protector HS300 | device_tracker |
| `event.basement_bar_light_scene_001` | Basement Bar Light Scene 001 | event |
| `event.basement_bar_light_scene_002` | Basement Bar Light Scene 002 | event |
| `event.basement_bar_light_scene_003` | Basement Bar Light Scene 003 | event |
| `event.basement_basement_mini_fridge_scene_id` | Basement Mini-Fridge Scene ID | event |
| `event.basement_hallway_light_scene_001` | Basement Hallway Light Scene 001 | event |
| `event.basement_hallway_light_scene_002` | Basement Hallway Light Scene 002 | event |
| `event.basement_hallway_light_scene_003` | Basement Hallway Light Scene 003 | event |
| `event.basement_hallway_light_scene_004` | Basement Hallway Light Scene 004 | event |
| `event.basement_hallway_light_scene_005` | Basement Hallway Light Scene 005 | event |
| `event.basement_living_room_fan_light_scene_001` | Basement Living Room Fan Light Scene 001 | event |
| `event.basement_living_room_fan_light_scene_002` | Basement Living Room Fan Light Scene 002 | event |
| `event.basement_living_room_fan_light_scene_003` | Basement Living Room Fan Light Scene 003 | event |
| `event.basement_main_light_scene_001` | Basement Main Light Scene 001 | event |
| `event.basement_main_light_scene_002` | Basement Main Light Scene 002 | event |
| `event.basement_main_light_scene_003` | Basement Main Light Scene 003 | event |
| `event.basement_main_light_scene_004` | Basement Main Light Scene 004 | event |
| `event.basement_main_light_scene_005` | Basement Main Light Scene 005 | event |
| `event.basement_main_light_scene_006` | Basement Main Light Scene 006 | event |
| `event.basement_stairs_light_scene_001` | Basement Stairs Light Scene 001 | event |
| `event.basement_stairs_light_scene_002` | Basement Stairs Light Scene 002 | event |
| `event.basement_stairs_light_scene_003` | Basement Stairs Light Scene 003 | event |
| `event.basement_stairs_light_scene_004` | Basement Stairs Light Scene 004 | event |
| `event.basement_stairs_light_scene_005` | Basement Stairs Light Scene 005 | event |
| `event.basement_stairs_light_scene_006` | Basement Stairs Light Scene 006 | event |
| `fan.basement_core_400` | Basement Core 400 | fan |
| `fan.basement_living_room_fan` | Basement Living Room Fan | fan |
| `light.basement_bar_light` | Basement Bar Light | light |
| `light.basement_hallway_light` | Basement Hallway Light | light |
| `light.basement_living_room_fan_light` | Basement Living Room Fan Light | light |
| `light.basement_living_room_nightlight_motion` | Basement Living Room Nightlight Motion | light |
| `light.basement_main_light` | Basement Main Light | light |
| `light.basement_stairs_light` | Basement Stairs Light | light |
| `media_player.basement_echo` | Basement Echo | media_player |
| `media_player.samsung_qn90ca_85` | Samsung QN90CA 85 | media_player |
| `media_player.samsung_qn90ca_85_2` | Samsung QN90CA 85 | media_player |
| `media_player.samsung_qn90ca_85_3` | Samsung QN90CA 85 | media_player |
| `number.basement_bar_light_all_led_strip_effect_color` | number.basement_bar_light_all_led_strip_effect_color | number |
| `number.basement_bar_light_all_led_strip_effect_duration` | number.basement_bar_light_all_led_strip_effect_duration | number |
| `number.basement_bar_light_all_led_strip_effect_level` | number.basement_bar_light_all_led_strip_effect_level | number |
| `number.basement_bar_light_auto_off_timer` | number.basement_bar_light_auto_off_timer | number |
| `number.basement_bar_light_default_all_led_strip_brightness_when_off` | number.basement_bar_light_default_all_led_strip_brightness_when_off | number |
| `number.basement_bar_light_default_all_led_strip_brightness_when_on` | number.basement_bar_light_default_all_led_strip_brightness_when_on | number |
| `number.basement_bar_light_default_all_led_strip_color_when_off` | number.basement_bar_light_default_all_led_strip_color_when_off | number |
| `number.basement_bar_light_default_all_led_strip_color_when_on` | number.basement_bar_light_default_all_led_strip_color_when_on | number |
| `number.basement_bar_light_default_level_local` | number.basement_bar_light_default_level_local | number |
| `number.basement_bar_light_default_level_remote` | number.basement_bar_light_default_level_remote | number |
| `number.basement_bar_light_dimming_speed_down_local` | number.basement_bar_light_dimming_speed_down_local | number |
| `number.basement_bar_light_dimming_speed_down_remote` | number.basement_bar_light_dimming_speed_down_remote | number |
| `number.basement_bar_light_dimming_speed_up_local` | number.basement_bar_light_dimming_speed_up_local | number |
| `number.basement_bar_light_dimming_speed_up_remote` | number.basement_bar_light_dimming_speed_up_remote | number |
| `number.basement_bar_light_double_down_level` | number.basement_bar_light_double_down_level | number |
| `number.basement_bar_light_double_up_level` | number.basement_bar_light_double_up_level | number |
| `number.basement_bar_light_energy_change_report_threshold` | number.basement_bar_light_energy_change_report_threshold | number |
| `number.basement_bar_light_indicator_value` | Basement Bar Light Indicator value | number |
| `number.basement_bar_light_led1_strip_effect_color` | number.basement_bar_light_led1_strip_effect_color | number |
| `number.basement_bar_light_led1_strip_effect_duration` | number.basement_bar_light_led1_strip_effect_duration | number |
| `number.basement_bar_light_led1_strip_effect_level` | number.basement_bar_light_led1_strip_effect_level | number |
| `number.basement_bar_light_led2_strip_effect_color` | number.basement_bar_light_led2_strip_effect_color | number |
| `number.basement_bar_light_led2_strip_effect_duration` | number.basement_bar_light_led2_strip_effect_duration | number |
| `number.basement_bar_light_led2_strip_effect_level` | number.basement_bar_light_led2_strip_effect_level | number |
| `number.basement_bar_light_led3_strip_effect_color` | number.basement_bar_light_led3_strip_effect_color | number |
| `number.basement_bar_light_led3_strip_effect_duration` | number.basement_bar_light_led3_strip_effect_duration | number |
| `number.basement_bar_light_led3_strip_effect_level` | number.basement_bar_light_led3_strip_effect_level | number |
| `number.basement_bar_light_led4_strip_effect_color` | number.basement_bar_light_led4_strip_effect_color | number |
| `number.basement_bar_light_led4_strip_effect_duration` | number.basement_bar_light_led4_strip_effect_duration | number |
| `number.basement_bar_light_led4_strip_effect_level` | number.basement_bar_light_led4_strip_effect_level | number |
| `number.basement_bar_light_led5_strip_effect_color` | number.basement_bar_light_led5_strip_effect_color | number |
| `number.basement_bar_light_led5_strip_effect_duration` | number.basement_bar_light_led5_strip_effect_duration | number |
| `number.basement_bar_light_led5_strip_effect_level` | number.basement_bar_light_led5_strip_effect_level | number |
| `number.basement_bar_light_led6_strip_effect_color` | number.basement_bar_light_led6_strip_effect_color | number |
| `number.basement_bar_light_led6_strip_effect_duration` | number.basement_bar_light_led6_strip_effect_duration | number |
| `number.basement_bar_light_led6_strip_effect_level` | number.basement_bar_light_led6_strip_effect_level | number |
| `number.basement_bar_light_led7_strip_effect_color` | number.basement_bar_light_led7_strip_effect_color | number |
| `number.basement_bar_light_led7_strip_effect_duration` | number.basement_bar_light_led7_strip_effect_duration | number |
| `number.basement_bar_light_led7_strip_effect_level` | number.basement_bar_light_led7_strip_effect_level | number |
| `number.basement_bar_light_load_level_indicator_timeout` | number.basement_bar_light_load_level_indicator_timeout | number |
| `number.basement_bar_light_maximum_level` | number.basement_bar_light_maximum_level | number |
| `number.basement_bar_light_minimum_level` | number.basement_bar_light_minimum_level | number |
| `number.basement_bar_light_power_change_report_threshold` | number.basement_bar_light_power_change_report_threshold | number |
| `number.basement_bar_light_power_energy_report_interval` | number.basement_bar_light_power_energy_report_interval | number |
| `number.basement_bar_light_ramp_rate_off_to_on_local` | number.basement_bar_light_ramp_rate_off_to_on_local | number |
| `number.basement_bar_light_ramp_rate_off_to_on_remote` | number.basement_bar_light_ramp_rate_off_to_on_remote | number |
| `number.basement_bar_light_ramp_rate_on_to_off_local` | number.basement_bar_light_ramp_rate_on_to_off_local | number |
| `number.basement_bar_light_ramp_rate_on_to_off_remote` | number.basement_bar_light_ramp_rate_on_to_off_remote | number |
| `number.basement_bar_light_state_after_power_restored` | number.basement_bar_light_state_after_power_restored | number |
| `number.basement_basement_mini_fridge_auto_off_timer` | number.basement_basement_mini_fridge_auto_off_timer | number |
| `number.basement_basement_mini_fridge_auto_on_timer` | number.basement_basement_mini_fridge_auto_on_timer | number |
| `number.basement_basement_mini_fridge_current_a_change_report_threshold` | number.basement_basement_mini_fridge_current_a_change_report_threshold | number |
| `number.basement_basement_mini_fridge_current_a_report_interval` | number.basement_basement_mini_fridge_current_a_report_interval | number |
| `number.basement_basement_mini_fridge_delay_turn_on_after_power_failure` | number.basement_basement_mini_fridge_delay_turn_on_after_power_failure | number |
| `number.basement_basement_mini_fridge_energy_kwh_report_interval` | number.basement_basement_mini_fridge_energy_kwh_report_interval | number |
| `number.basement_basement_mini_fridge_indicator_value` | number.basement_basement_mini_fridge_indicator_value | number |
| `number.basement_basement_mini_fridge_overload_protection` | number.basement_basement_mini_fridge_overload_protection | number |
| `number.basement_basement_mini_fridge_overload_protection_turn_on_delay` | number.basement_basement_mini_fridge_overload_protection_turn_on_delay | number |
| `number.basement_basement_mini_fridge_power_report_percentage_threshold` | number.basement_basement_mini_fridge_power_report_percentage_threshold | number |
| `number.basement_basement_mini_fridge_power_w_change_report_threshold` | number.basement_basement_mini_fridge_power_w_change_report_threshold | number |
| `number.basement_basement_mini_fridge_power_w_report_interval` | number.basement_basement_mini_fridge_power_w_report_interval | number |
| `number.basement_basement_mini_fridge_voltage_v_change_report_threshold` | number.basement_basement_mini_fridge_voltage_v_change_report_threshold | number |
| `number.basement_basement_mini_fridge_voltage_v_report_interval` | number.basement_basement_mini_fridge_voltage_v_report_interval | number |
| `number.basement_hallway_light_all_led_strip_effect_color` | number.basement_hallway_light_all_led_strip_effect_color | number |
| `number.basement_hallway_light_all_led_strip_effect_duration` | number.basement_hallway_light_all_led_strip_effect_duration | number |
| `number.basement_hallway_light_all_led_strip_effect_level` | number.basement_hallway_light_all_led_strip_effect_level | number |
| `number.basement_hallway_light_auto_off_timer` | number.basement_hallway_light_auto_off_timer | number |
| `number.basement_hallway_light_default_all_led_strip_brightness_when_off` | number.basement_hallway_light_default_all_led_strip_brightness_when_off | number |
| `number.basement_hallway_light_default_all_led_strip_brightness_when_on` | number.basement_hallway_light_default_all_led_strip_brightness_when_on | number |
| `number.basement_hallway_light_default_all_led_strip_color_when_off` | number.basement_hallway_light_default_all_led_strip_color_when_off | number |
| `number.basement_hallway_light_default_all_led_strip_color_when_on` | number.basement_hallway_light_default_all_led_strip_color_when_on | number |
| `number.basement_hallway_light_default_level_local` | number.basement_hallway_light_default_level_local | number |
| `number.basement_hallway_light_default_level_remote` | number.basement_hallway_light_default_level_remote | number |
| `number.basement_hallway_light_dimming_speed_down_local` | number.basement_hallway_light_dimming_speed_down_local | number |
| `number.basement_hallway_light_dimming_speed_down_remote` | number.basement_hallway_light_dimming_speed_down_remote | number |
| `number.basement_hallway_light_dimming_speed_up_local` | number.basement_hallway_light_dimming_speed_up_local | number |
| `number.basement_hallway_light_dimming_speed_up_remote` | number.basement_hallway_light_dimming_speed_up_remote | number |
| `number.basement_hallway_light_double_down_level` | number.basement_hallway_light_double_down_level | number |
| `number.basement_hallway_light_double_up_level` | number.basement_hallway_light_double_up_level | number |
| `number.basement_hallway_light_energy_change_report_threshold` | number.basement_hallway_light_energy_change_report_threshold | number |
| `number.basement_hallway_light_indicator_value` | Basement Hallway Light Indicator value | number |
| `number.basement_hallway_light_led1_strip_effect_color` | number.basement_hallway_light_led1_strip_effect_color | number |
| `number.basement_hallway_light_led1_strip_effect_duration` | number.basement_hallway_light_led1_strip_effect_duration | number |
| `number.basement_hallway_light_led1_strip_effect_level` | number.basement_hallway_light_led1_strip_effect_level | number |
| `number.basement_hallway_light_led2_strip_effect_color` | number.basement_hallway_light_led2_strip_effect_color | number |
| `number.basement_hallway_light_led2_strip_effect_duration` | number.basement_hallway_light_led2_strip_effect_duration | number |
| `number.basement_hallway_light_led2_strip_effect_level` | number.basement_hallway_light_led2_strip_effect_level | number |
| `number.basement_hallway_light_led3_strip_effect_color` | number.basement_hallway_light_led3_strip_effect_color | number |
| `number.basement_hallway_light_led3_strip_effect_duration` | number.basement_hallway_light_led3_strip_effect_duration | number |
| `number.basement_hallway_light_led3_strip_effect_level` | number.basement_hallway_light_led3_strip_effect_level | number |
| `number.basement_hallway_light_led4_strip_effect_color` | number.basement_hallway_light_led4_strip_effect_color | number |
| `number.basement_hallway_light_led4_strip_effect_duration` | number.basement_hallway_light_led4_strip_effect_duration | number |
| `number.basement_hallway_light_led4_strip_effect_level` | number.basement_hallway_light_led4_strip_effect_level | number |
| `number.basement_hallway_light_led5_strip_effect_color` | number.basement_hallway_light_led5_strip_effect_color | number |
| `number.basement_hallway_light_led5_strip_effect_duration` | number.basement_hallway_light_led5_strip_effect_duration | number |
| `number.basement_hallway_light_led5_strip_effect_level` | number.basement_hallway_light_led5_strip_effect_level | number |
| `number.basement_hallway_light_led6_strip_effect_color` | number.basement_hallway_light_led6_strip_effect_color | number |
| `number.basement_hallway_light_led6_strip_effect_duration` | number.basement_hallway_light_led6_strip_effect_duration | number |
| `number.basement_hallway_light_led6_strip_effect_level` | number.basement_hallway_light_led6_strip_effect_level | number |
| `number.basement_hallway_light_led7_strip_effect_color` | number.basement_hallway_light_led7_strip_effect_color | number |
| `number.basement_hallway_light_led7_strip_effect_duration` | number.basement_hallway_light_led7_strip_effect_duration | number |
| `number.basement_hallway_light_led7_strip_effect_level` | number.basement_hallway_light_led7_strip_effect_level | number |
| `number.basement_hallway_light_load_level_indicator_timeout` | number.basement_hallway_light_load_level_indicator_timeout | number |
| `number.basement_hallway_light_maximum_level` | number.basement_hallway_light_maximum_level | number |
| `number.basement_hallway_light_minimum_level` | number.basement_hallway_light_minimum_level | number |
| `number.basement_hallway_light_power_change_report_threshold` | number.basement_hallway_light_power_change_report_threshold | number |
| `number.basement_hallway_light_power_energy_report_interval` | number.basement_hallway_light_power_energy_report_interval | number |
| `number.basement_hallway_light_ramp_rate_off_to_on_local` | number.basement_hallway_light_ramp_rate_off_to_on_local | number |
| `number.basement_hallway_light_ramp_rate_off_to_on_remote` | number.basement_hallway_light_ramp_rate_off_to_on_remote | number |
| `number.basement_hallway_light_ramp_rate_on_to_off_local` | number.basement_hallway_light_ramp_rate_on_to_off_local | number |
| `number.basement_hallway_light_ramp_rate_on_to_off_remote` | number.basement_hallway_light_ramp_rate_on_to_off_remote | number |
| `number.basement_hallway_light_state_after_power_restored` | number.basement_hallway_light_state_after_power_restored | number |
| `number.basement_living_room_fan_autotimeroff` | Basement Living Room Fan AutoTimerOff | number |
| `number.basement_living_room_fan_brightnesslevelfordoubletapdown` | Basement Living Room Fan BrightnessLevelForDoubleTapDown | number |
| `number.basement_living_room_fan_brightnesslevelfordoubletapup` | Basement Living Room Fan BrightnessLevelForDoubleTapUp | number |
| `number.basement_living_room_fan_defaultled1colorwhenoff` | Basement Living Room Fan DefaultLed1ColorWhenOff | number |
| `number.basement_living_room_fan_defaultled1colorwhenon` | Basement Living Room Fan DefaultLed1ColorWhenOn | number |
| `number.basement_living_room_fan_defaultled1intensitywhenoff` | Basement Living Room Fan DefaultLed1IntensityWhenOff | number |
| `number.basement_living_room_fan_defaultled1intensitywhenon` | Basement Living Room Fan DefaultLed1IntensityWhenOn | number |
| `number.basement_living_room_fan_defaultled2colorwhenoff` | Basement Living Room Fan DefaultLed2ColorWhenOff | number |
| `number.basement_living_room_fan_defaultled2colorwhenon` | Basement Living Room Fan DefaultLed2ColorWhenOn | number |
| `number.basement_living_room_fan_defaultled2intensitywhenoff` | Basement Living Room Fan DefaultLed2IntensityWhenOff | number |
| `number.basement_living_room_fan_defaultled2intensitywhenon` | Basement Living Room Fan DefaultLed2IntensityWhenOn | number |
| `number.basement_living_room_fan_defaultled3colorwhenoff` | Basement Living Room Fan DefaultLed3ColorWhenOff | number |
| `number.basement_living_room_fan_defaultled3colorwhenon` | Basement Living Room Fan DefaultLed3ColorWhenOn | number |
| `number.basement_living_room_fan_defaultled3intensitywhenoff` | Basement Living Room Fan DefaultLed3IntensityWhenOff | number |
| `number.basement_living_room_fan_defaultled3intensitywhenon` | Basement Living Room Fan DefaultLed3IntensityWhenOn | number |
| `number.basement_living_room_fan_defaultled4colorwhenoff` | Basement Living Room Fan DefaultLed4ColorWhenOff | number |
| `number.basement_living_room_fan_defaultled4colorwhenon` | Basement Living Room Fan DefaultLed4ColorWhenOn | number |
| `number.basement_living_room_fan_defaultled4intensitywhenoff` | Basement Living Room Fan DefaultLed4IntensityWhenOff | number |
| `number.basement_living_room_fan_defaultled4intensitywhenon` | Basement Living Room Fan DefaultLed4IntensityWhenOn | number |
| `number.basement_living_room_fan_defaultled5colorwhenoff` | Basement Living Room Fan DefaultLed5ColorWhenOff | number |
| `number.basement_living_room_fan_defaultled5colorwhenon` | Basement Living Room Fan DefaultLed5ColorWhenOn | number |
| `number.basement_living_room_fan_defaultled5intensitywhenoff` | Basement Living Room Fan DefaultLed5IntensityWhenOff | number |
| `number.basement_living_room_fan_defaultled5intensitywhenon` | Basement Living Room Fan DefaultLed5IntensityWhenOn | number |
| `number.basement_living_room_fan_defaultled6colorwhenoff` | Basement Living Room Fan DefaultLed6ColorWhenOff | number |
| `number.basement_living_room_fan_defaultled6colorwhenon` | Basement Living Room Fan DefaultLed6ColorWhenOn | number |
| `number.basement_living_room_fan_defaultled6intensitywhenoff` | Basement Living Room Fan DefaultLed6IntensityWhenOff | number |
| `number.basement_living_room_fan_defaultled6intensitywhenon` | Basement Living Room Fan DefaultLed6IntensityWhenOn | number |
| `number.basement_living_room_fan_defaultled7colorwhenoff` | Basement Living Room Fan DefaultLed7ColorWhenOff | number |
| `number.basement_living_room_fan_defaultled7colorwhenon` | Basement Living Room Fan DefaultLed7ColorWhenOn | number |
| `number.basement_living_room_fan_defaultled7intensitywhenoff` | Basement Living Room Fan DefaultLed7IntensityWhenOff | number |
| `number.basement_living_room_fan_defaultled7intensitywhenon` | Basement Living Room Fan DefaultLed7IntensityWhenOn | number |
| `number.basement_living_room_fan_defaultlevellocal` | Basement Living Room Fan DefaultLevelLocal | number |
| `number.basement_living_room_fan_defaultlevelremote` | Basement Living Room Fan DefaultLevelRemote | number |
| `number.basement_living_room_fan_dimmingspeeddownlocal` | Basement Living Room Fan DimmingSpeedDownLocal | number |
| `number.basement_living_room_fan_dimmingspeeddownremote` | Basement Living Room Fan DimmingSpeedDownRemote | number |
| `number.basement_living_room_fan_dimmingspeeduplocal` | Basement Living Room Fan DimmingSpeedUpLocal | number |
| `number.basement_living_room_fan_dimmingspeedupremote` | Basement Living Room Fan DimmingSpeedUpRemote | number |
| `number.basement_living_room_fan_fanledleveltype` | Basement Living Room Fan FanLedLevelType | number |
| `number.basement_living_room_fan_highlevelforfancontrolmode` | Basement Living Room Fan HighLevelForFanControlMode | number |
| `number.basement_living_room_fan_ledcolorforfancontrolmode` | Basement Living Room Fan LedColorForFanControlMode | number |
| `number.basement_living_room_fan_ledcolorwhenoff` | Basement Living Room Fan LedColorWhenOff | number |
| `number.basement_living_room_fan_ledcolorwhenon` | Basement Living Room Fan LedColorWhenOn | number |
| `number.basement_living_room_fan_ledintensitywhenoff` | Basement Living Room Fan LedIntensityWhenOff | number |
| `number.basement_living_room_fan_ledintensitywhenon` | Basement Living Room Fan LedIntensityWhenOn | number |
| `number.basement_living_room_fan_light_all_led_strip_effect_color` | number.basement_living_room_fan_light_all_led_strip_effect_color | number |
| `number.basement_living_room_fan_light_all_led_strip_effect_duration` | number.basement_living_room_fan_light_all_led_strip_effect_duration | number |
| `number.basement_living_room_fan_light_all_led_strip_effect_level` | number.basement_living_room_fan_light_all_led_strip_effect_level | number |
| `number.basement_living_room_fan_light_auto_off_timer` | number.basement_living_room_fan_light_auto_off_timer | number |
| `number.basement_living_room_fan_light_default_all_led_strip_brightness_when_off` | number.basement_living_room_fan_light_default_all_led_strip_brightness_when_off | number |
| `number.basement_living_room_fan_light_default_all_led_strip_brightness_when_on` | number.basement_living_room_fan_light_default_all_led_strip_brightness_when_on | number |
| `number.basement_living_room_fan_light_default_all_led_strip_color_when_off` | number.basement_living_room_fan_light_default_all_led_strip_color_when_off | number |
| `number.basement_living_room_fan_light_default_all_led_strip_color_when_on` | number.basement_living_room_fan_light_default_all_led_strip_color_when_on | number |
| `number.basement_living_room_fan_light_default_level_local` | number.basement_living_room_fan_light_default_level_local | number |
| `number.basement_living_room_fan_light_default_level_remote` | number.basement_living_room_fan_light_default_level_remote | number |
| `number.basement_living_room_fan_light_dimming_speed_down_local` | number.basement_living_room_fan_light_dimming_speed_down_local | number |
| `number.basement_living_room_fan_light_dimming_speed_down_remote` | number.basement_living_room_fan_light_dimming_speed_down_remote | number |
| `number.basement_living_room_fan_light_dimming_speed_up_local` | number.basement_living_room_fan_light_dimming_speed_up_local | number |
| `number.basement_living_room_fan_light_dimming_speed_up_remote` | number.basement_living_room_fan_light_dimming_speed_up_remote | number |
| `number.basement_living_room_fan_light_double_down_level` | number.basement_living_room_fan_light_double_down_level | number |
| `number.basement_living_room_fan_light_double_up_level` | number.basement_living_room_fan_light_double_up_level | number |
| `number.basement_living_room_fan_light_energy_change_report_threshold` | number.basement_living_room_fan_light_energy_change_report_threshold | number |
| `number.basement_living_room_fan_light_indicator_value` | number.basement_living_room_fan_light_indicator_value | number |
| `number.basement_living_room_fan_light_led1_strip_effect_color` | number.basement_living_room_fan_light_led1_strip_effect_color | number |
| `number.basement_living_room_fan_light_led1_strip_effect_duration` | number.basement_living_room_fan_light_led1_strip_effect_duration | number |
| `number.basement_living_room_fan_light_led1_strip_effect_level` | number.basement_living_room_fan_light_led1_strip_effect_level | number |
| `number.basement_living_room_fan_light_led2_strip_effect_color` | number.basement_living_room_fan_light_led2_strip_effect_color | number |
| `number.basement_living_room_fan_light_led2_strip_effect_duration` | number.basement_living_room_fan_light_led2_strip_effect_duration | number |
| `number.basement_living_room_fan_light_led2_strip_effect_level` | number.basement_living_room_fan_light_led2_strip_effect_level | number |
| `number.basement_living_room_fan_light_led3_strip_effect_color` | number.basement_living_room_fan_light_led3_strip_effect_color | number |
| `number.basement_living_room_fan_light_led3_strip_effect_duration` | number.basement_living_room_fan_light_led3_strip_effect_duration | number |
| `number.basement_living_room_fan_light_led3_strip_effect_level` | number.basement_living_room_fan_light_led3_strip_effect_level | number |
| `number.basement_living_room_fan_light_led4_strip_effect_color` | number.basement_living_room_fan_light_led4_strip_effect_color | number |
| `number.basement_living_room_fan_light_led4_strip_effect_duration` | number.basement_living_room_fan_light_led4_strip_effect_duration | number |
| `number.basement_living_room_fan_light_led4_strip_effect_level` | number.basement_living_room_fan_light_led4_strip_effect_level | number |
| `number.basement_living_room_fan_light_led5_strip_effect_color` | number.basement_living_room_fan_light_led5_strip_effect_color | number |
| `number.basement_living_room_fan_light_led5_strip_effect_duration` | number.basement_living_room_fan_light_led5_strip_effect_duration | number |
| `number.basement_living_room_fan_light_led5_strip_effect_level` | number.basement_living_room_fan_light_led5_strip_effect_level | number |
| `number.basement_living_room_fan_light_led6_strip_effect_color` | number.basement_living_room_fan_light_led6_strip_effect_color | number |
| `number.basement_living_room_fan_light_led6_strip_effect_duration` | number.basement_living_room_fan_light_led6_strip_effect_duration | number |
| `number.basement_living_room_fan_light_led6_strip_effect_level` | number.basement_living_room_fan_light_led6_strip_effect_level | number |
| `number.basement_living_room_fan_light_led7_strip_effect_color` | number.basement_living_room_fan_light_led7_strip_effect_color | number |
| `number.basement_living_room_fan_light_led7_strip_effect_duration` | number.basement_living_room_fan_light_led7_strip_effect_duration | number |
| `number.basement_living_room_fan_light_led7_strip_effect_level` | number.basement_living_room_fan_light_led7_strip_effect_level | number |
| `number.basement_living_room_fan_light_level_after_power_restored` | number.basement_living_room_fan_light_level_after_power_restored | number |
| `number.basement_living_room_fan_light_load_level_indicator_timeout` | number.basement_living_room_fan_light_load_level_indicator_timeout | number |
| `number.basement_living_room_fan_light_maximum_level` | number.basement_living_room_fan_light_maximum_level | number |
| `number.basement_living_room_fan_light_minimum_level` | number.basement_living_room_fan_light_minimum_level | number |
| `number.basement_living_room_fan_light_power_change_report_threshold` | number.basement_living_room_fan_light_power_change_report_threshold | number |
| `number.basement_living_room_fan_light_power_energy_report_interval` | number.basement_living_room_fan_light_power_energy_report_interval | number |
| `number.basement_living_room_fan_light_ramp_rate_off_to_on_local` | number.basement_living_room_fan_light_ramp_rate_off_to_on_local | number |
| `number.basement_living_room_fan_light_ramp_rate_off_to_on_remote` | number.basement_living_room_fan_light_ramp_rate_off_to_on_remote | number |
| `number.basement_living_room_fan_light_ramp_rate_on_to_off_local` | number.basement_living_room_fan_light_ramp_rate_on_to_off_local | number |
| `number.basement_living_room_fan_light_ramp_rate_on_to_off_remote` | number.basement_living_room_fan_light_ramp_rate_on_to_off_remote | number |
| `number.basement_living_room_fan_lowlevelforfancontrolmode` | Basement Living Room Fan LowLevelForFanControlMode | number |
| `number.basement_living_room_fan_maximumlevel` | Basement Living Room Fan MaximumLevel | number |
| `number.basement_living_room_fan_mediumlevelforfancontrolmode` | Basement Living Room Fan MediumLevelForFanControlMode | number |
| `number.basement_living_room_fan_minimumlevel` | Basement Living Room Fan MinimumLevel | number |
| `number.basement_living_room_fan_nonneutralauxlowgear` | Basement Living Room Fan NonNeutralAuxLowGear | number |
| `number.basement_living_room_fan_nonneutralauxmediumgear` | Basement Living Room Fan NonNeutralAuxMediumGear | number |
| `number.basement_living_room_fan_quickstarttime` | Basement Living Room Fan QuickStartTime | number |
| `number.basement_living_room_fan_ramprateofftoonlocal` | Basement Living Room Fan RampRateOffToOnLocal | number |
| `number.basement_living_room_fan_ramprateofftoonremote` | Basement Living Room Fan RampRateOffToOnRemote | number |
| `number.basement_living_room_fan_ramprateontoofflocal` | Basement Living Room Fan RampRateOnToOffLocal | number |
| `number.basement_living_room_fan_ramprateontooffremote` | Basement Living Room Fan RampRateOnToOffRemote | number |
| `number.basement_living_room_fan_stateafterpowerrestored` | Basement Living Room Fan StateAfterPowerRestored | number |
| `number.basement_main_light_all_led_strip_effect_color` | number.basement_main_light_all_led_strip_effect_color | number |
| `number.basement_main_light_all_led_strip_effect_duration` | number.basement_main_light_all_led_strip_effect_duration | number |
| `number.basement_main_light_all_led_strip_effect_level` | number.basement_main_light_all_led_strip_effect_level | number |
| `number.basement_main_light_auto_off_timer` | number.basement_main_light_auto_off_timer | number |
| `number.basement_main_light_default_all_led_strip_brightness_when_off` | number.basement_main_light_default_all_led_strip_brightness_when_off | number |
| `number.basement_main_light_default_all_led_strip_brightness_when_on` | number.basement_main_light_default_all_led_strip_brightness_when_on | number |
| `number.basement_main_light_default_all_led_strip_color_when_off` | number.basement_main_light_default_all_led_strip_color_when_off | number |
| `number.basement_main_light_default_all_led_strip_color_when_on` | number.basement_main_light_default_all_led_strip_color_when_on | number |
| `number.basement_main_light_default_level_local` | number.basement_main_light_default_level_local | number |
| `number.basement_main_light_default_level_remote` | number.basement_main_light_default_level_remote | number |
| `number.basement_main_light_dimming_speed_down_local` | number.basement_main_light_dimming_speed_down_local | number |
| `number.basement_main_light_dimming_speed_down_remote` | number.basement_main_light_dimming_speed_down_remote | number |
| `number.basement_main_light_dimming_speed_up_local` | number.basement_main_light_dimming_speed_up_local | number |
| `number.basement_main_light_dimming_speed_up_remote` | number.basement_main_light_dimming_speed_up_remote | number |
| `number.basement_main_light_double_down_level` | number.basement_main_light_double_down_level | number |
| `number.basement_main_light_double_up_level` | number.basement_main_light_double_up_level | number |
| `number.basement_main_light_energy_change_report_threshold` | number.basement_main_light_energy_change_report_threshold | number |
| `number.basement_main_light_indicator_value` | Basement Main Light Indicator value | number |
| `number.basement_main_light_led1_strip_effect_color` | number.basement_main_light_led1_strip_effect_color | number |
| `number.basement_main_light_led1_strip_effect_duration` | number.basement_main_light_led1_strip_effect_duration | number |
| `number.basement_main_light_led1_strip_effect_level` | number.basement_main_light_led1_strip_effect_level | number |
| `number.basement_main_light_led2_strip_effect_color` | number.basement_main_light_led2_strip_effect_color | number |
| `number.basement_main_light_led2_strip_effect_duration` | number.basement_main_light_led2_strip_effect_duration | number |
| `number.basement_main_light_led2_strip_effect_level` | number.basement_main_light_led2_strip_effect_level | number |
| `number.basement_main_light_led3_strip_effect_color` | number.basement_main_light_led3_strip_effect_color | number |
| `number.basement_main_light_led3_strip_effect_duration` | number.basement_main_light_led3_strip_effect_duration | number |
| `number.basement_main_light_led3_strip_effect_level` | number.basement_main_light_led3_strip_effect_level | number |
| `number.basement_main_light_led4_strip_effect_color` | number.basement_main_light_led4_strip_effect_color | number |
| `number.basement_main_light_led4_strip_effect_duration` | number.basement_main_light_led4_strip_effect_duration | number |
| `number.basement_main_light_led4_strip_effect_level` | number.basement_main_light_led4_strip_effect_level | number |
| `number.basement_main_light_led5_strip_effect_color` | number.basement_main_light_led5_strip_effect_color | number |
| `number.basement_main_light_led5_strip_effect_duration` | number.basement_main_light_led5_strip_effect_duration | number |
| `number.basement_main_light_led5_strip_effect_level` | number.basement_main_light_led5_strip_effect_level | number |
| `number.basement_main_light_led6_strip_effect_color` | number.basement_main_light_led6_strip_effect_color | number |
| `number.basement_main_light_led6_strip_effect_duration` | number.basement_main_light_led6_strip_effect_duration | number |
| `number.basement_main_light_led6_strip_effect_level` | number.basement_main_light_led6_strip_effect_level | number |
| `number.basement_main_light_led7_strip_effect_color` | number.basement_main_light_led7_strip_effect_color | number |
| `number.basement_main_light_led7_strip_effect_duration` | number.basement_main_light_led7_strip_effect_duration | number |
| `number.basement_main_light_led7_strip_effect_level` | number.basement_main_light_led7_strip_effect_level | number |
| `number.basement_main_light_load_level_indicator_timeout` | number.basement_main_light_load_level_indicator_timeout | number |
| `number.basement_main_light_maximum_level` | number.basement_main_light_maximum_level | number |
| `number.basement_main_light_minimum_level` | number.basement_main_light_minimum_level | number |
| `number.basement_main_light_power_change_report_threshold` | number.basement_main_light_power_change_report_threshold | number |
| `number.basement_main_light_power_energy_report_interval` | number.basement_main_light_power_energy_report_interval | number |
| `number.basement_main_light_ramp_rate_off_to_on_local` | number.basement_main_light_ramp_rate_off_to_on_local | number |
| `number.basement_main_light_ramp_rate_off_to_on_remote` | number.basement_main_light_ramp_rate_off_to_on_remote | number |
| `number.basement_main_light_ramp_rate_on_to_off_local` | number.basement_main_light_ramp_rate_on_to_off_local | number |
| `number.basement_main_light_ramp_rate_on_to_off_remote` | number.basement_main_light_ramp_rate_on_to_off_remote | number |
| `number.basement_main_light_state_after_power_restored` | number.basement_main_light_state_after_power_restored | number |
| `number.basement_stairs_light_all_led_strip_effect_color` | number.basement_stairs_light_all_led_strip_effect_color | number |
| `number.basement_stairs_light_all_led_strip_effect_duration` | number.basement_stairs_light_all_led_strip_effect_duration | number |
| `number.basement_stairs_light_all_led_strip_effect_level` | number.basement_stairs_light_all_led_strip_effect_level | number |
| `number.basement_stairs_light_auto_off_timer` | number.basement_stairs_light_auto_off_timer | number |
| `number.basement_stairs_light_default_all_led_strip_brightness_when_off` | number.basement_stairs_light_default_all_led_strip_brightness_when_off | number |
| `number.basement_stairs_light_default_all_led_strip_brightness_when_on` | number.basement_stairs_light_default_all_led_strip_brightness_when_on | number |
| `number.basement_stairs_light_default_all_led_strip_color_when_off` | number.basement_stairs_light_default_all_led_strip_color_when_off | number |
| `number.basement_stairs_light_default_all_led_strip_color_when_on` | number.basement_stairs_light_default_all_led_strip_color_when_on | number |
| `number.basement_stairs_light_default_level_local` | number.basement_stairs_light_default_level_local | number |
| `number.basement_stairs_light_default_level_remote` | number.basement_stairs_light_default_level_remote | number |
| `number.basement_stairs_light_dimming_speed_down_local` | number.basement_stairs_light_dimming_speed_down_local | number |
| `number.basement_stairs_light_dimming_speed_down_remote` | number.basement_stairs_light_dimming_speed_down_remote | number |
| `number.basement_stairs_light_dimming_speed_up_local` | number.basement_stairs_light_dimming_speed_up_local | number |
| `number.basement_stairs_light_dimming_speed_up_remote` | number.basement_stairs_light_dimming_speed_up_remote | number |
| `number.basement_stairs_light_double_down_level` | number.basement_stairs_light_double_down_level | number |
| `number.basement_stairs_light_double_up_level` | number.basement_stairs_light_double_up_level | number |
| `number.basement_stairs_light_energy_change_report_threshold` | number.basement_stairs_light_energy_change_report_threshold | number |
| `number.basement_stairs_light_indicator_value` | Basement Stairs Light Indicator value | number |
| `number.basement_stairs_light_led1_strip_effect_color` | number.basement_stairs_light_led1_strip_effect_color | number |
| `number.basement_stairs_light_led1_strip_effect_duration` | number.basement_stairs_light_led1_strip_effect_duration | number |
| `number.basement_stairs_light_led1_strip_effect_level` | number.basement_stairs_light_led1_strip_effect_level | number |
| `number.basement_stairs_light_led2_strip_effect_color` | number.basement_stairs_light_led2_strip_effect_color | number |
| `number.basement_stairs_light_led2_strip_effect_duration` | number.basement_stairs_light_led2_strip_effect_duration | number |
| `number.basement_stairs_light_led2_strip_effect_level` | number.basement_stairs_light_led2_strip_effect_level | number |
| `number.basement_stairs_light_led3_strip_effect_color` | number.basement_stairs_light_led3_strip_effect_color | number |
| `number.basement_stairs_light_led3_strip_effect_duration` | number.basement_stairs_light_led3_strip_effect_duration | number |
| `number.basement_stairs_light_led3_strip_effect_level` | number.basement_stairs_light_led3_strip_effect_level | number |
| `number.basement_stairs_light_led4_strip_effect_color` | number.basement_stairs_light_led4_strip_effect_color | number |
| `number.basement_stairs_light_led4_strip_effect_duration` | number.basement_stairs_light_led4_strip_effect_duration | number |
| `number.basement_stairs_light_led4_strip_effect_level` | number.basement_stairs_light_led4_strip_effect_level | number |
| `number.basement_stairs_light_led5_strip_effect_color` | number.basement_stairs_light_led5_strip_effect_color | number |
| `number.basement_stairs_light_led5_strip_effect_duration` | number.basement_stairs_light_led5_strip_effect_duration | number |
| `number.basement_stairs_light_led5_strip_effect_level` | number.basement_stairs_light_led5_strip_effect_level | number |
| `number.basement_stairs_light_led6_strip_effect_color` | number.basement_stairs_light_led6_strip_effect_color | number |
| `number.basement_stairs_light_led6_strip_effect_duration` | number.basement_stairs_light_led6_strip_effect_duration | number |
| `number.basement_stairs_light_led6_strip_effect_level` | number.basement_stairs_light_led6_strip_effect_level | number |
| `number.basement_stairs_light_led7_strip_effect_color` | number.basement_stairs_light_led7_strip_effect_color | number |
| `number.basement_stairs_light_led7_strip_effect_duration` | number.basement_stairs_light_led7_strip_effect_duration | number |
| `number.basement_stairs_light_led7_strip_effect_level` | number.basement_stairs_light_led7_strip_effect_level | number |
| `number.basement_stairs_light_load_level_indicator_timeout` | number.basement_stairs_light_load_level_indicator_timeout | number |
| `number.basement_stairs_light_maximum_level` | number.basement_stairs_light_maximum_level | number |
| `number.basement_stairs_light_minimum_level` | number.basement_stairs_light_minimum_level | number |
| `number.basement_stairs_light_power_change_report_threshold` | number.basement_stairs_light_power_change_report_threshold | number |
| `number.basement_stairs_light_power_energy_report_interval` | number.basement_stairs_light_power_energy_report_interval | number |
| `number.basement_stairs_light_ramp_rate_off_to_on_local` | number.basement_stairs_light_ramp_rate_off_to_on_local | number |
| `number.basement_stairs_light_ramp_rate_off_to_on_remote` | number.basement_stairs_light_ramp_rate_off_to_on_remote | number |
| `number.basement_stairs_light_ramp_rate_on_to_off_local` | number.basement_stairs_light_ramp_rate_on_to_off_local | number |
| `number.basement_stairs_light_ramp_rate_on_to_off_remote` | number.basement_stairs_light_ramp_rate_on_to_off_remote | number |
| `number.basement_stairs_light_state_after_power_restored` | number.basement_stairs_light_state_after_power_restored | number |
| `remote.samsung_qn90ca_85` | Samsung QN90CA 85 | remote |
| `remote.samsung_qn90ca_85_2` | Samsung QN90CA 85 | remote |
| `select.basement_bar_light_all_led_strip_effect_effect` | select.basement_bar_light_all_led_strip_effect_effect | select |
| `select.basement_bar_light_aux_switch_scenes` | select.basement_bar_light_aux_switch_scenes | select |
| `select.basement_bar_light_button_delay_time` | select.basement_bar_light_button_delay_time | select |
| `select.basement_bar_light_dimmer_mode` | select.basement_bar_light_dimmer_mode | select |
| `select.basement_bar_light_double_down_to_param_56_level` | select.basement_bar_light_double_down_to_param_56_level | select |
| `select.basement_bar_light_double_tap_config_to_clear_notification` | select.basement_bar_light_double_tap_config_to_clear_notification | select |
| `select.basement_bar_light_double_up_to_param_55_level` | select.basement_bar_light_double_up_to_param_55_level | select |
| `select.basement_bar_light_exclusion_behavior` | select.basement_bar_light_exclusion_behavior | select |
| `select.basement_bar_light_firmware_progress_led` | select.basement_bar_light_firmware_progress_led | select |
| `select.basement_bar_light_forward_z_wave_commands_to_associated_devices` | select.basement_bar_light_forward_z_wave_commands_to_associated_devices | select |
| `select.basement_bar_light_increase_output_power_non_neutral` | select.basement_bar_light_increase_output_power_non_neutral | select |
| `select.basement_bar_light_invert_switch` | select.basement_bar_light_invert_switch | select |
| `select.basement_bar_light_led_bar_in_on_off_mode` | select.basement_bar_light_led_bar_in_on_off_mode | select |
| `select.basement_bar_light_led_brightness_scaling` | select.basement_bar_light_led_brightness_scaling | select |
| `select.basement_bar_light_led1_strip_effect_effect` | select.basement_bar_light_led1_strip_effect_effect | select |
| `select.basement_bar_light_led2_strip_effect_effect` | select.basement_bar_light_led2_strip_effect_effect | select |
| `select.basement_bar_light_led3_strip_effect_effect` | select.basement_bar_light_led3_strip_effect_effect | select |
| `select.basement_bar_light_led4_strip_effect_effect` | select.basement_bar_light_led4_strip_effect_effect | select |
| `select.basement_bar_light_led5_strip_effect_effect` | select.basement_bar_light_led5_strip_effect_effect | select |
| `select.basement_bar_light_led6_strip_effect_effect` | select.basement_bar_light_led6_strip_effect_effect | select |
| `select.basement_bar_light_led7_strip_effect_effect` | select.basement_bar_light_led7_strip_effect_effect | select |
| `select.basement_bar_light_local_protection_state` | Basement Bar Light Local protection state | select |
| `select.basement_bar_light_relay_click_in_on_off_mode` | select.basement_bar_light_relay_click_in_on_off_mode | select |
| `select.basement_bar_light_rf_protection_state` | Basement Bar Light RF protection state | select |
| `select.basement_bar_light_send_local_commands_to_associated_devices` | select.basement_bar_light_send_local_commands_to_associated_devices | select |
| `select.basement_bar_light_smart_bulb_mode` | select.basement_bar_light_smart_bulb_mode | select |
| `select.basement_bar_light_switch_type` | select.basement_bar_light_switch_type | select |
| `select.basement_basement_mini_fridge_led_power_consumption_indicator` | select.basement_basement_mini_fridge_led_power_consumption_indicator | select |
| `select.basement_basement_mini_fridge_manual_control` | select.basement_basement_mini_fridge_manual_control | select |
| `select.basement_basement_mini_fridge_on_off_status_change_notifications` | select.basement_basement_mini_fridge_on_off_status_change_notifications | select |
| `select.basement_basement_mini_fridge_state_after_power_failure` | select.basement_basement_mini_fridge_state_after_power_failure | select |
| `select.basement_basement_mini_fridge_z_wave_off_control` | select.basement_basement_mini_fridge_z_wave_off_control | select |
| `select.basement_basement_mini_fridge_z_wave_on_control` | select.basement_basement_mini_fridge_z_wave_on_control | select |
| `select.basement_core_400_night_light_level` | Basement Core 400 Night light level | select |
| `select.basement_hallway_light_all_led_strip_effect_effect` | select.basement_hallway_light_all_led_strip_effect_effect | select |
| `select.basement_hallway_light_aux_switch_scenes` | select.basement_hallway_light_aux_switch_scenes | select |
| `select.basement_hallway_light_button_delay_time` | select.basement_hallway_light_button_delay_time | select |
| `select.basement_hallway_light_dimmer_mode` | select.basement_hallway_light_dimmer_mode | select |
| `select.basement_hallway_light_double_down_to_param_56_level` | select.basement_hallway_light_double_down_to_param_56_level | select |
| `select.basement_hallway_light_double_tap_config_to_clear_notification` | select.basement_hallway_light_double_tap_config_to_clear_notification | select |
| `select.basement_hallway_light_double_up_to_param_55_level` | select.basement_hallway_light_double_up_to_param_55_level | select |
| `select.basement_hallway_light_exclusion_behavior` | select.basement_hallway_light_exclusion_behavior | select |
| `select.basement_hallway_light_firmware_progress_led` | select.basement_hallway_light_firmware_progress_led | select |
| `select.basement_hallway_light_forward_z_wave_commands_to_associated_devices` | select.basement_hallway_light_forward_z_wave_commands_to_associated_devices | select |
| `select.basement_hallway_light_increase_output_power_non_neutral` | select.basement_hallway_light_increase_output_power_non_neutral | select |
| `select.basement_hallway_light_invert_switch` | select.basement_hallway_light_invert_switch | select |
| `select.basement_hallway_light_led_bar_in_on_off_mode` | select.basement_hallway_light_led_bar_in_on_off_mode | select |
| `select.basement_hallway_light_led_brightness_scaling` | select.basement_hallway_light_led_brightness_scaling | select |
| `select.basement_hallway_light_led1_strip_effect_effect` | select.basement_hallway_light_led1_strip_effect_effect | select |
| `select.basement_hallway_light_led2_strip_effect_effect` | select.basement_hallway_light_led2_strip_effect_effect | select |
| `select.basement_hallway_light_led3_strip_effect_effect` | select.basement_hallway_light_led3_strip_effect_effect | select |
| `select.basement_hallway_light_led4_strip_effect_effect` | select.basement_hallway_light_led4_strip_effect_effect | select |
| `select.basement_hallway_light_led5_strip_effect_effect` | select.basement_hallway_light_led5_strip_effect_effect | select |
| `select.basement_hallway_light_led6_strip_effect_effect` | select.basement_hallway_light_led6_strip_effect_effect | select |
| `select.basement_hallway_light_led7_strip_effect_effect` | select.basement_hallway_light_led7_strip_effect_effect | select |
| `select.basement_hallway_light_local_protection_state` | Basement Hallway Light Local protection state | select |
| `select.basement_hallway_light_relay_click_in_on_off_mode` | select.basement_hallway_light_relay_click_in_on_off_mode | select |
| `select.basement_hallway_light_rf_protection_state` | Basement Hallway Light RF protection state | select |
| `select.basement_hallway_light_send_local_commands_to_associated_devices` | select.basement_hallway_light_send_local_commands_to_associated_devices | select |
| `select.basement_hallway_light_smart_bulb_mode` | select.basement_hallway_light_smart_bulb_mode | select |
| `select.basement_hallway_light_switch_type` | select.basement_hallway_light_switch_type | select |
| `select.basement_living_room_fan_auxswitchuniquescenes` | Basement Living Room Fan AuxSwitchUniqueScenes | select |
| `select.basement_living_room_fan_bindingofftoonsynclevel` | Basement Living Room Fan BindingOffToOnSyncLevel | select |
| `select.basement_living_room_fan_buttondelay` | Basement Living Room Fan ButtonDelay | select |
| `select.basement_living_room_fan_doubletapclearnotifications` | Basement Living Room Fan DoubleTapClearNotifications | select |
| `select.basement_living_room_fan_doubletapdowntoparam56` | Basement Living Room Fan DoubleTapDownToParam56 | select |
| `select.basement_living_room_fan_doubletapuptoparam55` | Basement Living Room Fan DoubleTapUpToParam55 | select |
| `select.basement_living_room_fan_fancontrolmode` | Basement Living Room Fan FanControlMode | select |
| `select.basement_living_room_fan_fantimermode` | Basement Living Room Fan FanTimerMode | select |
| `select.basement_living_room_fan_firmwareupdateinprogressindicator` | Basement Living Room Fan FirmwareUpdateInProgressIndicator | select |
| `select.basement_living_room_fan_invertswitch` | Basement Living Room Fan InvertSwitch | select |
| `select.basement_living_room_fan_light_all_led_strip_effect_effect` | select.basement_living_room_fan_light_all_led_strip_effect_effect | select |
| `select.basement_living_room_fan_light_aux_switch_scenes` | select.basement_living_room_fan_light_aux_switch_scenes | select |
| `select.basement_living_room_fan_light_button_delay_time` | select.basement_living_room_fan_light_button_delay_time | select |
| `select.basement_living_room_fan_light_dimmer_mode` | select.basement_living_room_fan_light_dimmer_mode | select |
| `select.basement_living_room_fan_light_double_down_level_enable` | select.basement_living_room_fan_light_double_down_level_enable | select |
| `select.basement_living_room_fan_light_double_tap_config_to_clear_notification` | select.basement_living_room_fan_light_double_tap_config_to_clear_notification | select |
| `select.basement_living_room_fan_light_double_up_level_enable` | select.basement_living_room_fan_light_double_up_level_enable | select |
| `select.basement_living_room_fan_light_exclusion_behavior` | select.basement_living_room_fan_light_exclusion_behavior | select |
| `select.basement_living_room_fan_light_firmware_progress_led` | select.basement_living_room_fan_light_firmware_progress_led | select |
| `select.basement_living_room_fan_light_forward_z_wave_commands_to_associated_devices` | select.basement_living_room_fan_light_forward_z_wave_commands_to_associated_devices | select |
| `select.basement_living_room_fan_light_increase_output_power_non_neutral` | select.basement_living_room_fan_light_increase_output_power_non_neutral | select |
| `select.basement_living_room_fan_light_invert_switch` | select.basement_living_room_fan_light_invert_switch | select |
| `select.basement_living_room_fan_light_led_bar_in_on_off_mode` | select.basement_living_room_fan_light_led_bar_in_on_off_mode | select |
| `select.basement_living_room_fan_light_led_brightness_scaling` | select.basement_living_room_fan_light_led_brightness_scaling | select |
| `select.basement_living_room_fan_light_led1_strip_effect_effect` | select.basement_living_room_fan_light_led1_strip_effect_effect | select |
| `select.basement_living_room_fan_light_led2_strip_effect_effect` | select.basement_living_room_fan_light_led2_strip_effect_effect | select |
| `select.basement_living_room_fan_light_led3_strip_effect_effect` | select.basement_living_room_fan_light_led3_strip_effect_effect | select |
| `select.basement_living_room_fan_light_led4_strip_effect_effect` | select.basement_living_room_fan_light_led4_strip_effect_effect | select |
| `select.basement_living_room_fan_light_led5_strip_effect_effect` | select.basement_living_room_fan_light_led5_strip_effect_effect | select |
| `select.basement_living_room_fan_light_led6_strip_effect_effect` | select.basement_living_room_fan_light_led6_strip_effect_effect | select |
| `select.basement_living_room_fan_light_led7_strip_effect_effect` | select.basement_living_room_fan_light_led7_strip_effect_effect | select |
| `select.basement_living_room_fan_light_local_protection_state` | Basement Living Room Fan Light Local protection state | select |
| `select.basement_living_room_fan_light_relay_click_in_on_off_mode` | select.basement_living_room_fan_light_relay_click_in_on_off_mode | select |
| `select.basement_living_room_fan_light_rf_protection_state` | Basement Living Room Fan Light RF protection state | select |
| `select.basement_living_room_fan_light_send_local_commands_to_associated_devices` | select.basement_living_room_fan_light_send_local_commands_to_associated_devices | select |
| `select.basement_living_room_fan_light_smart_bulb_mode` | select.basement_living_room_fan_light_smart_bulb_mode | select |
| `select.basement_living_room_fan_light_switch_type` | select.basement_living_room_fan_light_switch_type | select |
| `select.basement_living_room_fan_loadlevelindicatortimeout` | Basement Living Room Fan LoadLevelIndicatorTimeout | select |
| `select.basement_living_room_fan_localprotection` | Basement Living Room Fan LocalProtection | select |
| `select.basement_living_room_fan_onoffledmode` | Basement Living Room Fan OnOffLedMode | select |
| `select.basement_living_room_fan_outputmode` | Basement Living Room Fan OutputMode | select |
| `select.basement_living_room_fan_singletapbehavior` | Basement Living Room Fan SingleTapBehavior | select |
| `select.basement_living_room_fan_smartbulbmode` | Basement Living Room Fan SmartBulbMode | select |
| `select.basement_living_room_fan_switchtype` | Basement Living Room Fan SwitchType | select |
| `select.basement_living_room_nightlight_motion_effect` | Basement Living Room Nightlight Motion Effect | select |
| `select.basement_living_room_nightlight_motion_power_on_behavior` | Basement Living Room Nightlight Motion Power-on behavior | select |
| `select.basement_main_light_all_led_strip_effect_effect` | select.basement_main_light_all_led_strip_effect_effect | select |
| `select.basement_main_light_aux_switch_scenes` | select.basement_main_light_aux_switch_scenes | select |
| `select.basement_main_light_button_delay_time` | select.basement_main_light_button_delay_time | select |
| `select.basement_main_light_dimmer_mode` | select.basement_main_light_dimmer_mode | select |
| `select.basement_main_light_double_down_to_param_56_level` | select.basement_main_light_double_down_to_param_56_level | select |
| `select.basement_main_light_double_tap_config_to_clear_notification` | select.basement_main_light_double_tap_config_to_clear_notification | select |
| `select.basement_main_light_double_up_to_param_55_level` | select.basement_main_light_double_up_to_param_55_level | select |
| `select.basement_main_light_exclusion_behavior` | select.basement_main_light_exclusion_behavior | select |
| `select.basement_main_light_firmware_progress_led` | select.basement_main_light_firmware_progress_led | select |
| `select.basement_main_light_forward_z_wave_commands_to_associated_devices` | select.basement_main_light_forward_z_wave_commands_to_associated_devices | select |
| `select.basement_main_light_increase_output_power_non_neutral` | select.basement_main_light_increase_output_power_non_neutral | select |
| `select.basement_main_light_invert_switch` | select.basement_main_light_invert_switch | select |
| `select.basement_main_light_led_bar_in_on_off_mode` | select.basement_main_light_led_bar_in_on_off_mode | select |
| `select.basement_main_light_led_brightness_scaling` | select.basement_main_light_led_brightness_scaling | select |
| `select.basement_main_light_led1_strip_effect_effect` | select.basement_main_light_led1_strip_effect_effect | select |
| `select.basement_main_light_led2_strip_effect_effect` | select.basement_main_light_led2_strip_effect_effect | select |
| `select.basement_main_light_led3_strip_effect_effect` | select.basement_main_light_led3_strip_effect_effect | select |
| `select.basement_main_light_led4_strip_effect_effect` | select.basement_main_light_led4_strip_effect_effect | select |
| `select.basement_main_light_led5_strip_effect_effect` | select.basement_main_light_led5_strip_effect_effect | select |
| `select.basement_main_light_led6_strip_effect_effect` | select.basement_main_light_led6_strip_effect_effect | select |
| `select.basement_main_light_led7_strip_effect_effect` | select.basement_main_light_led7_strip_effect_effect | select |
| `select.basement_main_light_local_protection_state` | Basement Main Light Local protection state | select |
| `select.basement_main_light_relay_click_in_on_off_mode` | select.basement_main_light_relay_click_in_on_off_mode | select |
| `select.basement_main_light_rf_protection_state` | Basement Main Light RF protection state | select |
| `select.basement_main_light_send_local_commands_to_associated_devices` | select.basement_main_light_send_local_commands_to_associated_devices | select |
| `select.basement_main_light_smart_bulb_mode` | select.basement_main_light_smart_bulb_mode | select |
| `select.basement_main_light_switch_type` | select.basement_main_light_switch_type | select |
| `select.basement_stairs_light_all_led_strip_effect_effect` | select.basement_stairs_light_all_led_strip_effect_effect | select |
| `select.basement_stairs_light_aux_switch_scenes` | select.basement_stairs_light_aux_switch_scenes | select |
| `select.basement_stairs_light_button_delay_time` | select.basement_stairs_light_button_delay_time | select |
| `select.basement_stairs_light_dimmer_mode` | select.basement_stairs_light_dimmer_mode | select |
| `select.basement_stairs_light_double_down_to_param_56_level` | select.basement_stairs_light_double_down_to_param_56_level | select |
| `select.basement_stairs_light_double_tap_config_to_clear_notification` | select.basement_stairs_light_double_tap_config_to_clear_notification | select |
| `select.basement_stairs_light_double_up_to_param_55_level` | select.basement_stairs_light_double_up_to_param_55_level | select |
| `select.basement_stairs_light_exclusion_behavior` | select.basement_stairs_light_exclusion_behavior | select |
| `select.basement_stairs_light_firmware_progress_led` | select.basement_stairs_light_firmware_progress_led | select |
| `select.basement_stairs_light_forward_z_wave_commands_to_associated_devices` | select.basement_stairs_light_forward_z_wave_commands_to_associated_devices | select |
| `select.basement_stairs_light_increase_output_power_non_neutral` | select.basement_stairs_light_increase_output_power_non_neutral | select |
| `select.basement_stairs_light_invert_switch` | select.basement_stairs_light_invert_switch | select |
| `select.basement_stairs_light_led_bar_in_on_off_mode` | select.basement_stairs_light_led_bar_in_on_off_mode | select |
| `select.basement_stairs_light_led_brightness_scaling` | select.basement_stairs_light_led_brightness_scaling | select |
| `select.basement_stairs_light_led1_strip_effect_effect` | select.basement_stairs_light_led1_strip_effect_effect | select |
| `select.basement_stairs_light_led2_strip_effect_effect` | select.basement_stairs_light_led2_strip_effect_effect | select |
| `select.basement_stairs_light_led3_strip_effect_effect` | select.basement_stairs_light_led3_strip_effect_effect | select |
| `select.basement_stairs_light_led4_strip_effect_effect` | select.basement_stairs_light_led4_strip_effect_effect | select |
| `select.basement_stairs_light_led5_strip_effect_effect` | select.basement_stairs_light_led5_strip_effect_effect | select |
| `select.basement_stairs_light_led6_strip_effect_effect` | select.basement_stairs_light_led6_strip_effect_effect | select |
| `select.basement_stairs_light_led7_strip_effect_effect` | select.basement_stairs_light_led7_strip_effect_effect | select |
| `select.basement_stairs_light_local_protection_state` | Basement Stairs Light Local protection state | select |
| `select.basement_stairs_light_relay_click_in_on_off_mode` | select.basement_stairs_light_relay_click_in_on_off_mode | select |
| `select.basement_stairs_light_rf_protection_state` | Basement Stairs Light RF protection state | select |
| `select.basement_stairs_light_send_local_commands_to_associated_devices` | select.basement_stairs_light_send_local_commands_to_associated_devices | select |
| `select.basement_stairs_light_smart_bulb_mode` | select.basement_stairs_light_smart_bulb_mode | select |
| `select.basement_stairs_light_switch_type` | select.basement_stairs_light_switch_type | select |
| `sensor.0x048727fffe19568d_last_seen` | sensor.0x048727fffe19568d_last_seen | sensor |
| `sensor.0x048727fffe19568d_linkquality` | sensor.0x048727fffe19568d_linkquality | sensor |
| `sensor.basement_bar_light_commands_dropped_rx` | sensor.basement_bar_light_commands_dropped_rx | sensor |
| `sensor.basement_bar_light_commands_dropped_tx` | sensor.basement_bar_light_commands_dropped_tx | sensor |
| `sensor.basement_bar_light_dimming_mode` | sensor.basement_bar_light_dimming_mode | sensor |
| `sensor.basement_bar_light_electric_consumption_kwh` | Basement Bar Light Electric Consumption [kWh] | sensor |
| `sensor.basement_bar_light_electric_consumption_w` | Basement Bar Light Electric Consumption [W] | sensor |
| `sensor.basement_bar_light_internal_temperature` | sensor.basement_bar_light_internal_temperature | sensor |
| `sensor.basement_bar_light_last_seen` | Basement Bar Light Last seen | sensor |
| `sensor.basement_bar_light_node_status` | Basement Bar Light Node status | sensor |
| `sensor.basement_bar_light_overheat_detected` | sensor.basement_bar_light_overheat_detected | sensor |
| `sensor.basement_bar_light_power_type` | sensor.basement_bar_light_power_type | sensor |
| `sensor.basement_bar_light_round_trip_time` | sensor.basement_bar_light_round_trip_time | sensor |
| `sensor.basement_bar_light_rssi` | sensor.basement_bar_light_rssi | sensor |
| `sensor.basement_bar_light_successful_commands_rx` | sensor.basement_bar_light_successful_commands_rx | sensor |
| `sensor.basement_bar_light_successful_commands_tx` | sensor.basement_bar_light_successful_commands_tx | sensor |
| `sensor.basement_bar_light_timed_out_responses` | sensor.basement_bar_light_timed_out_responses | sensor |
| `sensor.basement_basement_mini_fridge_alarm_level` | Basement Mini-Fridge Alarm Level | sensor |
| `sensor.basement_basement_mini_fridge_alarm_type` | Basement Mini-Fridge Alarm Type | sensor |
| `sensor.basement_basement_mini_fridge_commands_dropped_rx` | sensor.basement_basement_mini_fridge_commands_dropped_rx | sensor |
| `sensor.basement_basement_mini_fridge_commands_dropped_tx` | sensor.basement_basement_mini_fridge_commands_dropped_tx | sensor |
| `sensor.basement_basement_mini_fridge_electric_consumption_a` | Basement Mini-Fridge Electric Consumption [A] | sensor |
| `sensor.basement_basement_mini_fridge_electric_consumption_kwh` | Basement Mini-Fridge Electric Consumption [kWh] | sensor |
| `sensor.basement_basement_mini_fridge_electric_consumption_v` | Basement Mini-Fridge Electric Consumption [V] | sensor |
| `sensor.basement_basement_mini_fridge_electric_consumption_w` | Basement Mini-Fridge Electric Consumption [W] | sensor |
| `sensor.basement_basement_mini_fridge_last_seen` | sensor.basement_basement_mini_fridge_last_seen | sensor |
| `sensor.basement_basement_mini_fridge_node_status` | Basement Mini-Fridge Node status | sensor |
| `sensor.basement_basement_mini_fridge_round_trip_time` | sensor.basement_basement_mini_fridge_round_trip_time | sensor |
| `sensor.basement_basement_mini_fridge_signal_strength` | sensor.basement_basement_mini_fridge_signal_strength | sensor |
| `sensor.basement_basement_mini_fridge_successful_commands_rx` | sensor.basement_basement_mini_fridge_successful_commands_rx | sensor |
| `sensor.basement_basement_mini_fridge_successful_commands_tx` | sensor.basement_basement_mini_fridge_successful_commands_tx | sensor |
| `sensor.basement_basement_mini_fridge_timed_out_responses` | sensor.basement_basement_mini_fridge_timed_out_responses | sensor |
| `sensor.basement_core_400_air_quality` | Basement Core 400 Air quality | sensor |
| `sensor.basement_core_400_filter_lifetime` | Basement Core 400 Filter lifetime | sensor |
| `sensor.basement_core_400_pm2_5` | Basement Core 400 PM2.5 | sensor |
| `sensor.basement_echo_next_alarm` | Basement Echo Next alarm | sensor |
| `sensor.basement_echo_next_reminder` | Basement Echo Next reminder | sensor |
| `sensor.basement_echo_next_timer` | Basement Echo Next timer | sensor |
| `sensor.basement_entertainment_outlet_5_bill_energy` | Basement Entertainment Outlet 5 Bill energy | sensor |
| `sensor.basement_entertainment_outlet_5_daily_energy` | Basement Entertainment Outlet 5 Daily energy | sensor |
| `sensor.basement_entertainment_outlet_5_monthly_energy` | Basement Entertainment Outlet 5 Monthly energy | sensor |
| `sensor.basement_entertainment_outlet_5_usage` | Basement Entertainment Outlet 5 Power | sensor |
| `sensor.basement_entertainment_outlet_5_weekly_energy` | Basement Entertainment Outlet 5 Weekly energy | sensor |
| `sensor.basement_entertainment_outlet_5_yearly_energy` | Basement Entertainment Outlet 5 Yearly energy | sensor |
| `sensor.basement_entertainment_outlet_6_bill_energy` | Basement Entertainment Outlet 6 Bill energy | sensor |
| `sensor.basement_entertainment_outlet_6_daily_energy` | Basement Entertainment Outlet 6 Daily energy | sensor |
| `sensor.basement_entertainment_outlet_6_monthly_energy` | Basement Entertainment Outlet 6 Monthly energy | sensor |
| `sensor.basement_entertainment_outlet_6_usage` | Basement Entertainment Outlet 6 Power | sensor |
| `sensor.basement_entertainment_outlet_6_weekly_energy` | Basement Entertainment Outlet 6 Weekly energy | sensor |
| `sensor.basement_entertainment_outlet_6_yearly_energy` | Basement Entertainment Outlet 6 Yearly energy | sensor |
| `sensor.basement_hallway_light_commands_dropped_rx` | sensor.basement_hallway_light_commands_dropped_rx | sensor |
| `sensor.basement_hallway_light_commands_dropped_tx` | sensor.basement_hallway_light_commands_dropped_tx | sensor |
| `sensor.basement_hallway_light_dimming_mode` | sensor.basement_hallway_light_dimming_mode | sensor |
| `sensor.basement_hallway_light_electric_consumption_kwh` | Basement Hallway Light Electric Consumption [kWh] | sensor |
| `sensor.basement_hallway_light_electric_consumption_w` | Basement Hallway Light Electric Consumption [W] | sensor |
| `sensor.basement_hallway_light_internal_temperature` | sensor.basement_hallway_light_internal_temperature | sensor |
| `sensor.basement_hallway_light_last_seen` | Basement Hallway Light Last seen | sensor |
| `sensor.basement_hallway_light_node_status` | Basement Hallway Light Node status | sensor |
| `sensor.basement_hallway_light_overheat_detected` | sensor.basement_hallway_light_overheat_detected | sensor |
| `sensor.basement_hallway_light_power_type` | sensor.basement_hallway_light_power_type | sensor |
| `sensor.basement_hallway_light_round_trip_time` | sensor.basement_hallway_light_round_trip_time | sensor |
| `sensor.basement_hallway_light_rssi` | sensor.basement_hallway_light_rssi | sensor |
| `sensor.basement_hallway_light_successful_commands_rx` | sensor.basement_hallway_light_successful_commands_rx | sensor |
| `sensor.basement_hallway_light_successful_commands_tx` | sensor.basement_hallway_light_successful_commands_tx | sensor |
| `sensor.basement_hallway_light_timed_out_responses` | sensor.basement_hallway_light_timed_out_responses | sensor |
| `sensor.basement_living_room_fan_breezemode` | Basement Living Room Fan Breeze mode | sensor |
| `sensor.basement_living_room_fan_devicebindnumber` | Basement Living Room Fan DeviceBindNumber | sensor |
| `sensor.basement_living_room_fan_individual_led_effect` | Basement Living Room Fan Individual led effect | sensor |
| `sensor.basement_living_room_fan_internaltemperature` | Basement Living Room Fan Temperature | sensor |
| `sensor.basement_living_room_fan_led_effect` | Basement Living Room Fan Led effect | sensor |
| `sensor.basement_living_room_fan_light_commands_dropped_rx` | sensor.basement_living_room_fan_light_commands_dropped_rx | sensor |
| `sensor.basement_living_room_fan_light_commands_dropped_tx` | sensor.basement_living_room_fan_light_commands_dropped_tx | sensor |
| `sensor.basement_living_room_fan_light_dimming_mode` | sensor.basement_living_room_fan_light_dimming_mode | sensor |
| `sensor.basement_living_room_fan_light_electric_consumption_kwh` | Basement Living Room Fan Light Electric Consumption [kWh] | sensor |
| `sensor.basement_living_room_fan_light_electric_consumption_w` | Basement Living Room Fan Light Electric Consumption [W] | sensor |
| `sensor.basement_living_room_fan_light_internal_temperature` | sensor.basement_living_room_fan_light_internal_temperature | sensor |
| `sensor.basement_living_room_fan_light_last_seen` | sensor.basement_living_room_fan_light_last_seen | sensor |
| `sensor.basement_living_room_fan_light_node_status` | Basement Living Room Fan Light Node status | sensor |
| `sensor.basement_living_room_fan_light_overheat_detected` | sensor.basement_living_room_fan_light_overheat_detected | sensor |
| `sensor.basement_living_room_fan_light_power_type` | sensor.basement_living_room_fan_light_power_type | sensor |
| `sensor.basement_living_room_fan_light_round_trip_time` | sensor.basement_living_room_fan_light_round_trip_time | sensor |
| `sensor.basement_living_room_fan_light_signal_strength` | sensor.basement_living_room_fan_light_signal_strength | sensor |
| `sensor.basement_living_room_fan_light_successful_commands_rx` | sensor.basement_living_room_fan_light_successful_commands_rx | sensor |
| `sensor.basement_living_room_fan_light_successful_commands_tx` | sensor.basement_living_room_fan_light_successful_commands_tx | sensor |
| `sensor.basement_living_room_fan_light_timed_out_responses` | sensor.basement_living_room_fan_light_timed_out_responses | sensor |
| `sensor.basement_living_room_fan_notificationcomplete` | Basement Living Room Fan NotificationComplete | sensor |
| `sensor.basement_living_room_fan_overheat` | Basement Living Room Fan Overheat | sensor |
| `sensor.basement_living_room_fan_powertype` | Basement Living Room Fan PowerType | sensor |
| `sensor.basement_living_room_fan_remoteprotection` | Basement Living Room Fan RemoteProtection | sensor |
| `sensor.basement_living_room_nightlight_motion_illuminance` | Basement Living Room Nightlight Motion Illuminance | sensor |
| `sensor.basement_living_room_nightlight_motion_illuminance_raw` | Basement Living Room Nightlight Motion Illuminance raw | sensor |
| `sensor.basement_living_room_nightlight_motion_last_seen` | sensor.basement_living_room_nightlight_motion_last_seen | sensor |
| `sensor.basement_living_room_nightlight_motion_linkquality` | sensor.basement_living_room_nightlight_motion_linkquality | sensor |
| `sensor.basement_living_room_nightlight_motion_power_on_behavior` | sensor.basement_living_room_nightlight_motion_power_on_behavior | sensor |
| `sensor.basement_living_room_nightlight_motion_update_state` | sensor.basement_living_room_nightlight_motion_update_state | sensor |
| `sensor.basement_main_light_commands_dropped_rx` | sensor.basement_main_light_commands_dropped_rx | sensor |
| `sensor.basement_main_light_commands_dropped_tx` | sensor.basement_main_light_commands_dropped_tx | sensor |
| `sensor.basement_main_light_dimming_mode` | sensor.basement_main_light_dimming_mode | sensor |
| `sensor.basement_main_light_electric_consumption_kwh` | Basement Main Light Electric Consumption [kWh] | sensor |
| `sensor.basement_main_light_electric_consumption_w` | Basement Main Light Electric Consumption [W] | sensor |
| `sensor.basement_main_light_internal_temperature` | sensor.basement_main_light_internal_temperature | sensor |
| `sensor.basement_main_light_last_seen` | Basement Main Light Last seen | sensor |
| `sensor.basement_main_light_node_status` | Basement Main Light Node status | sensor |
| `sensor.basement_main_light_overheat_detected` | sensor.basement_main_light_overheat_detected | sensor |
| `sensor.basement_main_light_power_type` | sensor.basement_main_light_power_type | sensor |
| `sensor.basement_main_light_round_trip_time` | sensor.basement_main_light_round_trip_time | sensor |
| `sensor.basement_main_light_rssi` | sensor.basement_main_light_rssi | sensor |
| `sensor.basement_main_light_successful_commands_rx` | sensor.basement_main_light_successful_commands_rx | sensor |
| `sensor.basement_main_light_successful_commands_tx` | sensor.basement_main_light_successful_commands_tx | sensor |
| `sensor.basement_main_light_timed_out_responses` | sensor.basement_main_light_timed_out_responses | sensor |
| `sensor.basement_onkyo_receiver_link_speed` | sensor.basement_onkyo_receiver_link_speed | sensor |
| `sensor.basement_stairs_light_commands_dropped_rx` | sensor.basement_stairs_light_commands_dropped_rx | sensor |
| `sensor.basement_stairs_light_commands_dropped_tx` | sensor.basement_stairs_light_commands_dropped_tx | sensor |
| `sensor.basement_stairs_light_dimming_mode` | sensor.basement_stairs_light_dimming_mode | sensor |
| `sensor.basement_stairs_light_electric_consumption_kwh` | Basement Stairs Light Electric Consumption [kWh] | sensor |
| `sensor.basement_stairs_light_electric_consumption_w` | Basement Stairs Light Electric Consumption [W] | sensor |
| `sensor.basement_stairs_light_internal_temperature` | sensor.basement_stairs_light_internal_temperature | sensor |
| `sensor.basement_stairs_light_last_seen` | Basement Stairs Light Last seen | sensor |
| `sensor.basement_stairs_light_node_status` | Basement Stairs Light Node status | sensor |
| `sensor.basement_stairs_light_overheat_detected` | sensor.basement_stairs_light_overheat_detected | sensor |
| `sensor.basement_stairs_light_power_type` | sensor.basement_stairs_light_power_type | sensor |
| `sensor.basement_stairs_light_round_trip_time` | sensor.basement_stairs_light_round_trip_time | sensor |
| `sensor.basement_stairs_light_rssi` | sensor.basement_stairs_light_rssi | sensor |
| `sensor.basement_stairs_light_successful_commands_rx` | sensor.basement_stairs_light_successful_commands_rx | sensor |
| `sensor.basement_stairs_light_successful_commands_tx` | sensor.basement_stairs_light_successful_commands_tx | sensor |
| `sensor.basement_stairs_light_timed_out_responses` | sensor.basement_stairs_light_timed_out_responses | sensor |
| `sensor.samsung_qn90ca_85_link_speed` | sensor.samsung_qn90ca_85_link_speed | sensor |
| `switch.basement_basement_mini_fridge` | Basement Mini-Fridge | switch |
| `switch.basement_core_400_child_lock` | Basement Core 400 Child lock | switch |
| `switch.basement_core_400_display` | Basement Core 400 Display | switch |
| `switch.basement_echo_do_not_disturb_switch` | Basement Echo Do not disturb | switch |
| `switch.basement_echo_repeat_switch` | Basement Echo Repeat | switch |
| `switch.basement_echo_shuffle_switch` | Basement Echo Shuffle | switch |
| `update.basement_bar_light_firmware` | Basement Bar Light Firmware | update |
| `update.basement_basement_mini_fridge_firmware` | Basement Mini-Fridge Firmware | update |
| `update.basement_core_400_firmware` | Basement Core 400 Firmware | update |
| `update.basement_hallway_light_firmware` | Basement Hallway Light Firmware | update |
| `update.basement_living_room_fan` | Basement Living Room Fan | update |
| `update.basement_living_room_fan_light_firmware` | Basement Living Room Fan Light Firmware | update |
| `update.basement_living_room_nightlight_motion` | Basement Living Room Nightlight Motion | update |
| `update.basement_main_light_firmware` | Basement Main Light Firmware | update |
| `update.basement_stairs_light_firmware` | Basement Stairs Light Firmware | update |
