# Basement Bathroom

> Read-only Home Assistant inventory captured 2026-08-24. No devices or configuration were changed.

- Floor classification: Basement
- Area: Basement Bathroom
- Devices: 4
- Entities: 309
- Inclusion rule: assigned to this Basement-floor area.

## Devices

| Device | Manufacturer | Model | Integration | Device ID |
|---|---|---|---|---|
| Basement Bathroom AirGuard TH | SONOFF | Temperature and humidity sensor with display and relay control | zigbee2mqtt | `311718e1bc37deec23d5a75725ad2f4e` |
| Basement Bathroom Fan | Inovelli | On/off switch | zigbee2mqtt | `13c41e928d30b027dddac9ae4e17da7e` |
| Basement Bathroom Light | Inovelli | VZW31-SN | zwave_js | `3500bf1541c3615305a4167b916c55e5` |
| Basement Shower Light | Inovelli | VZW31-SN | zwave_js | `942ee74ada8d8e0c7f13291d0f61ca51` |

## Entities

| Entity ID | Friendly name | Domain |
|---|---|---|
| `automation.basement_bathroom_humidity_control` | Basement Bathroom Humidity Control | automation |
| `button.basement_bathroom_fan_energy_reset` | Basement Bathroom Fan Energy reset | button |
| `button.basement_bathroom_fan_identify` | Basement Bathroom Fan Identify | button |
| `button.basement_bathroom_light_identify` | Basement Bathroom Light Identify | button |
| `button.basement_bathroom_light_ping` | Basement Bathroom Light Ping | button |
| `button.basement_bathroom_light_reset_accumulated_values` | Basement Bathroom Light Reset accumulated values | button |
| `button.basement_shower_light_identify` | Basement Shower Light Identify | button |
| `button.basement_shower_light_ping` | Basement Shower Light Ping | button |
| `button.basement_shower_light_reset_accumulated_values` | Basement Shower Light Reset accumulated values | button |
| `event.basement_bathroom_light_scene_001` | Basement Bathroom Light Scene 001 | event |
| `event.basement_bathroom_light_scene_002` | Basement Bathroom Light Scene 002 | event |
| `event.basement_bathroom_light_scene_003` | Basement Bathroom Light Scene 003 | event |
| `event.basement_shower_light_scene_001` | Basement Shower Light Scene 001 | event |
| `event.basement_shower_light_scene_002` | Basement Shower Light Scene 002 | event |
| `event.basement_shower_light_scene_003` | Basement Shower Light Scene 003 | event |
| `fan.basement_bathroom_fan` | Basement Bathroom Fan | fan |
| `light.basement_bathroom_fan` | Basement Bathroom Fan | light |
| `light.basement_bathroom_light` | Basement Bathroom Light | light |
| `light.basement_shower_light` | Basement Shower Light | light |
| `number.basement_bathroom_airguard_th_comfort_humidity_max` | Basement Bathroom AirGuard TH Comfort humidity max | number |
| `number.basement_bathroom_airguard_th_comfort_humidity_min` | Basement Bathroom AirGuard TH Comfort humidity min | number |
| `number.basement_bathroom_airguard_th_comfort_temperature_max` | Basement Bathroom AirGuard TH Temperature | number |
| `number.basement_bathroom_airguard_th_comfort_temperature_min` | Basement Bathroom AirGuard TH Temperature | number |
| `number.basement_bathroom_airguard_th_external_humidity` | Basement Bathroom AirGuard TH External humidity | number |
| `number.basement_bathroom_airguard_th_external_temperature` | Basement Bathroom AirGuard TH Temperature | number |
| `number.basement_bathroom_airguard_th_humidity_calibration` | Basement Bathroom AirGuard TH Humidity calibration | number |
| `number.basement_bathroom_airguard_th_temperature_calibration` | Basement Bathroom AirGuard TH Temperature calibration | number |
| `number.basement_bathroom_fan_activeenergyreports` | Basement Bathroom Fan ActiveEnergyReports | number |
| `number.basement_bathroom_fan_activepowerreports` | Basement Bathroom Fan ActivePowerReports | number |
| `number.basement_bathroom_fan_autotimeroff` | Basement Bathroom Fan AutoTimerOff | number |
| `number.basement_bathroom_fan_brightnesslevelfordoubletapdown` | Basement Bathroom Fan BrightnessLevelForDoubleTapDown | number |
| `number.basement_bathroom_fan_brightnesslevelfordoubletapup` | Basement Bathroom Fan BrightnessLevelForDoubleTapUp | number |
| `number.basement_bathroom_fan_defaultled1colorwhenoff` | Basement Bathroom Fan DefaultLed1ColorWhenOff | number |
| `number.basement_bathroom_fan_defaultled1colorwhenon` | Basement Bathroom Fan DefaultLed1ColorWhenOn | number |
| `number.basement_bathroom_fan_defaultled1intensitywhenoff` | Basement Bathroom Fan DefaultLed1IntensityWhenOff | number |
| `number.basement_bathroom_fan_defaultled1intensitywhenon` | Basement Bathroom Fan DefaultLed1IntensityWhenOn | number |
| `number.basement_bathroom_fan_defaultled2colorwhenoff` | Basement Bathroom Fan DefaultLed2ColorWhenOff | number |
| `number.basement_bathroom_fan_defaultled2colorwhenon` | Basement Bathroom Fan DefaultLed2ColorWhenOn | number |
| `number.basement_bathroom_fan_defaultled2intensitywhenoff` | Basement Bathroom Fan DefaultLed2IntensityWhenOff | number |
| `number.basement_bathroom_fan_defaultled2intensitywhenon` | Basement Bathroom Fan DefaultLed2IntensityWhenOn | number |
| `number.basement_bathroom_fan_defaultled3colorwhenoff` | Basement Bathroom Fan DefaultLed3ColorWhenOff | number |
| `number.basement_bathroom_fan_defaultled3colorwhenon` | Basement Bathroom Fan DefaultLed3ColorWhenOn | number |
| `number.basement_bathroom_fan_defaultled3intensitywhenoff` | Basement Bathroom Fan DefaultLed3IntensityWhenOff | number |
| `number.basement_bathroom_fan_defaultled3intensitywhenon` | Basement Bathroom Fan DefaultLed3IntensityWhenOn | number |
| `number.basement_bathroom_fan_defaultled4colorwhenoff` | Basement Bathroom Fan DefaultLed4ColorWhenOff | number |
| `number.basement_bathroom_fan_defaultled4colorwhenon` | Basement Bathroom Fan DefaultLed4ColorWhenOn | number |
| `number.basement_bathroom_fan_defaultled4intensitywhenoff` | Basement Bathroom Fan DefaultLed4IntensityWhenOff | number |
| `number.basement_bathroom_fan_defaultled4intensitywhenon` | Basement Bathroom Fan DefaultLed4IntensityWhenOn | number |
| `number.basement_bathroom_fan_defaultled5colorwhenoff` | Basement Bathroom Fan DefaultLed5ColorWhenOff | number |
| `number.basement_bathroom_fan_defaultled5colorwhenon` | Basement Bathroom Fan DefaultLed5ColorWhenOn | number |
| `number.basement_bathroom_fan_defaultled5intensitywhenoff` | Basement Bathroom Fan DefaultLed5IntensityWhenOff | number |
| `number.basement_bathroom_fan_defaultled5intensitywhenon` | Basement Bathroom Fan DefaultLed5IntensityWhenOn | number |
| `number.basement_bathroom_fan_defaultled6colorwhenoff` | Basement Bathroom Fan DefaultLed6ColorWhenOff | number |
| `number.basement_bathroom_fan_defaultled6colorwhenon` | Basement Bathroom Fan DefaultLed6ColorWhenOn | number |
| `number.basement_bathroom_fan_defaultled6intensitywhenoff` | Basement Bathroom Fan DefaultLed6IntensityWhenOff | number |
| `number.basement_bathroom_fan_defaultled6intensitywhenon` | Basement Bathroom Fan DefaultLed6IntensityWhenOn | number |
| `number.basement_bathroom_fan_defaultled7colorwhenoff` | Basement Bathroom Fan DefaultLed7ColorWhenOff | number |
| `number.basement_bathroom_fan_defaultled7colorwhenon` | Basement Bathroom Fan DefaultLed7ColorWhenOn | number |
| `number.basement_bathroom_fan_defaultled7intensitywhenoff` | Basement Bathroom Fan DefaultLed7IntensityWhenOff | number |
| `number.basement_bathroom_fan_defaultled7intensitywhenon` | Basement Bathroom Fan DefaultLed7IntensityWhenOn | number |
| `number.basement_bathroom_fan_defaultlevellocal` | Basement Bathroom Fan DefaultLevelLocal | number |
| `number.basement_bathroom_fan_defaultlevelremote` | Basement Bathroom Fan DefaultLevelRemote | number |
| `number.basement_bathroom_fan_dimmingspeeddownlocal` | Basement Bathroom Fan DimmingSpeedDownLocal | number |
| `number.basement_bathroom_fan_dimmingspeeddownremote` | Basement Bathroom Fan DimmingSpeedDownRemote | number |
| `number.basement_bathroom_fan_dimmingspeeduplocal` | Basement Bathroom Fan DimmingSpeedUpLocal | number |
| `number.basement_bathroom_fan_dimmingspeedupremote` | Basement Bathroom Fan DimmingSpeedUpRemote | number |
| `number.basement_bathroom_fan_fanledleveltype` | Basement Bathroom Fan FanLedLevelType | number |
| `number.basement_bathroom_fan_highlevelforfancontrolmode` | Basement Bathroom Fan HighLevelForFanControlMode | number |
| `number.basement_bathroom_fan_ledcolorforfancontrolmode` | Basement Bathroom Fan LedColorForFanControlMode | number |
| `number.basement_bathroom_fan_ledcolorwhenoff` | Basement Bathroom Fan LedColorWhenOff | number |
| `number.basement_bathroom_fan_ledcolorwhenon` | Basement Bathroom Fan LedColorWhenOn | number |
| `number.basement_bathroom_fan_ledintensitywhenoff` | Basement Bathroom Fan LedIntensityWhenOff | number |
| `number.basement_bathroom_fan_ledintensitywhenon` | Basement Bathroom Fan LedIntensityWhenOn | number |
| `number.basement_bathroom_fan_lowlevelforfancontrolmode` | Basement Bathroom Fan LowLevelForFanControlMode | number |
| `number.basement_bathroom_fan_mediumlevelforfancontrolmode` | Basement Bathroom Fan MediumLevelForFanControlMode | number |
| `number.basement_bathroom_fan_periodicpowerandenergyreports` | Basement Bathroom Fan PeriodicPowerAndEnergyReports | number |
| `number.basement_bathroom_fan_ramprateofftoonlocal` | Basement Bathroom Fan RampRateOffToOnLocal | number |
| `number.basement_bathroom_fan_ramprateofftoonremote` | Basement Bathroom Fan RampRateOffToOnRemote | number |
| `number.basement_bathroom_fan_ramprateontoofflocal` | Basement Bathroom Fan RampRateOnToOffLocal | number |
| `number.basement_bathroom_fan_ramprateontooffremote` | Basement Bathroom Fan RampRateOnToOffRemote | number |
| `number.basement_bathroom_fan_stateafterpowerrestored` | Basement Bathroom Fan StateAfterPowerRestored | number |
| `number.basement_bathroom_light_all_led_strip_effect_color` | number.basement_bathroom_light_all_led_strip_effect_color | number |
| `number.basement_bathroom_light_all_led_strip_effect_duration` | number.basement_bathroom_light_all_led_strip_effect_duration | number |
| `number.basement_bathroom_light_all_led_strip_effect_level` | number.basement_bathroom_light_all_led_strip_effect_level | number |
| `number.basement_bathroom_light_auto_off_timer` | number.basement_bathroom_light_auto_off_timer | number |
| `number.basement_bathroom_light_default_all_led_strip_brightness_when_off` | number.basement_bathroom_light_default_all_led_strip_brightness_when_off | number |
| `number.basement_bathroom_light_default_all_led_strip_brightness_when_on` | number.basement_bathroom_light_default_all_led_strip_brightness_when_on | number |
| `number.basement_bathroom_light_default_all_led_strip_color_when_off` | number.basement_bathroom_light_default_all_led_strip_color_when_off | number |
| `number.basement_bathroom_light_default_all_led_strip_color_when_on` | number.basement_bathroom_light_default_all_led_strip_color_when_on | number |
| `number.basement_bathroom_light_default_level_local` | number.basement_bathroom_light_default_level_local | number |
| `number.basement_bathroom_light_default_level_remote` | number.basement_bathroom_light_default_level_remote | number |
| `number.basement_bathroom_light_dimming_speed_down_local` | number.basement_bathroom_light_dimming_speed_down_local | number |
| `number.basement_bathroom_light_dimming_speed_down_remote` | number.basement_bathroom_light_dimming_speed_down_remote | number |
| `number.basement_bathroom_light_dimming_speed_up_local` | number.basement_bathroom_light_dimming_speed_up_local | number |
| `number.basement_bathroom_light_dimming_speed_up_remote` | number.basement_bathroom_light_dimming_speed_up_remote | number |
| `number.basement_bathroom_light_double_down_level` | number.basement_bathroom_light_double_down_level | number |
| `number.basement_bathroom_light_double_up_level` | number.basement_bathroom_light_double_up_level | number |
| `number.basement_bathroom_light_energy_change_report_threshold` | number.basement_bathroom_light_energy_change_report_threshold | number |
| `number.basement_bathroom_light_indicator_value` | number.basement_bathroom_light_indicator_value | number |
| `number.basement_bathroom_light_led1_strip_effect_color` | number.basement_bathroom_light_led1_strip_effect_color | number |
| `number.basement_bathroom_light_led1_strip_effect_duration` | number.basement_bathroom_light_led1_strip_effect_duration | number |
| `number.basement_bathroom_light_led1_strip_effect_level` | number.basement_bathroom_light_led1_strip_effect_level | number |
| `number.basement_bathroom_light_led2_strip_effect_color` | number.basement_bathroom_light_led2_strip_effect_color | number |
| `number.basement_bathroom_light_led2_strip_effect_duration` | number.basement_bathroom_light_led2_strip_effect_duration | number |
| `number.basement_bathroom_light_led2_strip_effect_level` | number.basement_bathroom_light_led2_strip_effect_level | number |
| `number.basement_bathroom_light_led3_strip_effect_color` | number.basement_bathroom_light_led3_strip_effect_color | number |
| `number.basement_bathroom_light_led3_strip_effect_duration` | number.basement_bathroom_light_led3_strip_effect_duration | number |
| `number.basement_bathroom_light_led3_strip_effect_level` | number.basement_bathroom_light_led3_strip_effect_level | number |
| `number.basement_bathroom_light_led4_strip_effect_color` | number.basement_bathroom_light_led4_strip_effect_color | number |
| `number.basement_bathroom_light_led4_strip_effect_duration` | number.basement_bathroom_light_led4_strip_effect_duration | number |
| `number.basement_bathroom_light_led4_strip_effect_level` | number.basement_bathroom_light_led4_strip_effect_level | number |
| `number.basement_bathroom_light_led5_strip_effect_color` | number.basement_bathroom_light_led5_strip_effect_color | number |
| `number.basement_bathroom_light_led5_strip_effect_duration` | number.basement_bathroom_light_led5_strip_effect_duration | number |
| `number.basement_bathroom_light_led5_strip_effect_level` | number.basement_bathroom_light_led5_strip_effect_level | number |
| `number.basement_bathroom_light_led6_strip_effect_color` | number.basement_bathroom_light_led6_strip_effect_color | number |
| `number.basement_bathroom_light_led6_strip_effect_duration` | number.basement_bathroom_light_led6_strip_effect_duration | number |
| `number.basement_bathroom_light_led6_strip_effect_level` | number.basement_bathroom_light_led6_strip_effect_level | number |
| `number.basement_bathroom_light_led7_strip_effect_color` | number.basement_bathroom_light_led7_strip_effect_color | number |
| `number.basement_bathroom_light_led7_strip_effect_duration` | number.basement_bathroom_light_led7_strip_effect_duration | number |
| `number.basement_bathroom_light_led7_strip_effect_level` | number.basement_bathroom_light_led7_strip_effect_level | number |
| `number.basement_bathroom_light_load_level_indicator_timeout` | number.basement_bathroom_light_load_level_indicator_timeout | number |
| `number.basement_bathroom_light_maximum_level` | number.basement_bathroom_light_maximum_level | number |
| `number.basement_bathroom_light_minimum_level` | number.basement_bathroom_light_minimum_level | number |
| `number.basement_bathroom_light_power_change_report_threshold` | number.basement_bathroom_light_power_change_report_threshold | number |
| `number.basement_bathroom_light_power_energy_report_interval` | number.basement_bathroom_light_power_energy_report_interval | number |
| `number.basement_bathroom_light_ramp_rate_off_to_on_local` | number.basement_bathroom_light_ramp_rate_off_to_on_local | number |
| `number.basement_bathroom_light_ramp_rate_off_to_on_remote` | number.basement_bathroom_light_ramp_rate_off_to_on_remote | number |
| `number.basement_bathroom_light_ramp_rate_on_to_off_local` | number.basement_bathroom_light_ramp_rate_on_to_off_local | number |
| `number.basement_bathroom_light_ramp_rate_on_to_off_remote` | number.basement_bathroom_light_ramp_rate_on_to_off_remote | number |
| `number.basement_bathroom_light_state_after_power_restored` | number.basement_bathroom_light_state_after_power_restored | number |
| `number.basement_shower_light_all_led_strip_effect_color` | number.basement_shower_light_all_led_strip_effect_color | number |
| `number.basement_shower_light_all_led_strip_effect_duration` | number.basement_shower_light_all_led_strip_effect_duration | number |
| `number.basement_shower_light_all_led_strip_effect_level` | number.basement_shower_light_all_led_strip_effect_level | number |
| `number.basement_shower_light_auto_off_timer` | number.basement_shower_light_auto_off_timer | number |
| `number.basement_shower_light_default_all_led_strip_brightness_when_off` | number.basement_shower_light_default_all_led_strip_brightness_when_off | number |
| `number.basement_shower_light_default_all_led_strip_brightness_when_on` | number.basement_shower_light_default_all_led_strip_brightness_when_on | number |
| `number.basement_shower_light_default_all_led_strip_color_when_off` | number.basement_shower_light_default_all_led_strip_color_when_off | number |
| `number.basement_shower_light_default_all_led_strip_color_when_on` | number.basement_shower_light_default_all_led_strip_color_when_on | number |
| `number.basement_shower_light_default_level_local` | number.basement_shower_light_default_level_local | number |
| `number.basement_shower_light_default_level_remote` | number.basement_shower_light_default_level_remote | number |
| `number.basement_shower_light_dimming_speed_down_local` | number.basement_shower_light_dimming_speed_down_local | number |
| `number.basement_shower_light_dimming_speed_down_remote` | number.basement_shower_light_dimming_speed_down_remote | number |
| `number.basement_shower_light_dimming_speed_up_local` | number.basement_shower_light_dimming_speed_up_local | number |
| `number.basement_shower_light_dimming_speed_up_remote` | number.basement_shower_light_dimming_speed_up_remote | number |
| `number.basement_shower_light_double_down_level` | number.basement_shower_light_double_down_level | number |
| `number.basement_shower_light_double_up_level` | number.basement_shower_light_double_up_level | number |
| `number.basement_shower_light_energy_change_report_threshold` | number.basement_shower_light_energy_change_report_threshold | number |
| `number.basement_shower_light_indicator_value` | number.basement_shower_light_indicator_value | number |
| `number.basement_shower_light_led1_strip_effect_color` | number.basement_shower_light_led1_strip_effect_color | number |
| `number.basement_shower_light_led1_strip_effect_duration` | number.basement_shower_light_led1_strip_effect_duration | number |
| `number.basement_shower_light_led1_strip_effect_level` | number.basement_shower_light_led1_strip_effect_level | number |
| `number.basement_shower_light_led2_strip_effect_color` | number.basement_shower_light_led2_strip_effect_color | number |
| `number.basement_shower_light_led2_strip_effect_duration` | number.basement_shower_light_led2_strip_effect_duration | number |
| `number.basement_shower_light_led2_strip_effect_level` | number.basement_shower_light_led2_strip_effect_level | number |
| `number.basement_shower_light_led3_strip_effect_color` | number.basement_shower_light_led3_strip_effect_color | number |
| `number.basement_shower_light_led3_strip_effect_duration` | number.basement_shower_light_led3_strip_effect_duration | number |
| `number.basement_shower_light_led3_strip_effect_level` | number.basement_shower_light_led3_strip_effect_level | number |
| `number.basement_shower_light_led4_strip_effect_color` | number.basement_shower_light_led4_strip_effect_color | number |
| `number.basement_shower_light_led4_strip_effect_duration` | number.basement_shower_light_led4_strip_effect_duration | number |
| `number.basement_shower_light_led4_strip_effect_level` | number.basement_shower_light_led4_strip_effect_level | number |
| `number.basement_shower_light_led5_strip_effect_color` | number.basement_shower_light_led5_strip_effect_color | number |
| `number.basement_shower_light_led5_strip_effect_duration` | number.basement_shower_light_led5_strip_effect_duration | number |
| `number.basement_shower_light_led5_strip_effect_level` | number.basement_shower_light_led5_strip_effect_level | number |
| `number.basement_shower_light_led6_strip_effect_color` | number.basement_shower_light_led6_strip_effect_color | number |
| `number.basement_shower_light_led6_strip_effect_duration` | number.basement_shower_light_led6_strip_effect_duration | number |
| `number.basement_shower_light_led6_strip_effect_level` | number.basement_shower_light_led6_strip_effect_level | number |
| `number.basement_shower_light_led7_strip_effect_color` | number.basement_shower_light_led7_strip_effect_color | number |
| `number.basement_shower_light_led7_strip_effect_duration` | number.basement_shower_light_led7_strip_effect_duration | number |
| `number.basement_shower_light_led7_strip_effect_level` | number.basement_shower_light_led7_strip_effect_level | number |
| `number.basement_shower_light_load_level_indicator_timeout` | number.basement_shower_light_load_level_indicator_timeout | number |
| `number.basement_shower_light_maximum_level` | number.basement_shower_light_maximum_level | number |
| `number.basement_shower_light_minimum_level` | number.basement_shower_light_minimum_level | number |
| `number.basement_shower_light_power_change_report_threshold` | number.basement_shower_light_power_change_report_threshold | number |
| `number.basement_shower_light_power_energy_report_interval` | number.basement_shower_light_power_energy_report_interval | number |
| `number.basement_shower_light_ramp_rate_off_to_on_local` | number.basement_shower_light_ramp_rate_off_to_on_local | number |
| `number.basement_shower_light_ramp_rate_off_to_on_remote` | number.basement_shower_light_ramp_rate_off_to_on_remote | number |
| `number.basement_shower_light_ramp_rate_on_to_off_local` | number.basement_shower_light_ramp_rate_on_to_off_local | number |
| `number.basement_shower_light_ramp_rate_on_to_off_remote` | number.basement_shower_light_ramp_rate_on_to_off_remote | number |
| `number.basement_shower_light_state_after_power_restored` | number.basement_shower_light_state_after_power_restored | number |
| `select.basement_bathroom_airguard_th_temperature_sensor_select` | Basement Bathroom AirGuard TH Temperature sensor select | select |
| `select.basement_bathroom_airguard_th_temperature_units` | Basement Bathroom AirGuard TH Temperature units | select |
| `select.basement_bathroom_fan_auxswitchuniquescenes` | Basement Bathroom Fan AuxSwitchUniqueScenes | select |
| `select.basement_bathroom_fan_bindingofftoonsynclevel` | Basement Bathroom Fan BindingOffToOnSyncLevel | select |
| `select.basement_bathroom_fan_buttondelay` | Basement Bathroom Fan ButtonDelay | select |
| `select.basement_bathroom_fan_doubletapclearnotifications` | Basement Bathroom Fan DoubleTapClearNotifications | select |
| `select.basement_bathroom_fan_doubletapdowntoparam56` | Basement Bathroom Fan DoubleTapDownToParam56 | select |
| `select.basement_bathroom_fan_doubletapuptoparam55` | Basement Bathroom Fan DoubleTapUpToParam55 | select |
| `select.basement_bathroom_fan_fancontrolmode` | Basement Bathroom Fan FanControlMode | select |
| `select.basement_bathroom_fan_fantimermode` | Basement Bathroom Fan FanTimerMode | select |
| `select.basement_bathroom_fan_firmwareupdateinprogressindicator` | Basement Bathroom Fan FirmwareUpdateInProgressIndicator | select |
| `select.basement_bathroom_fan_invertswitch` | Basement Bathroom Fan InvertSwitch | select |
| `select.basement_bathroom_fan_ledbarscaling` | Basement Bathroom Fan LedBarScaling | select |
| `select.basement_bathroom_fan_loadlevelindicatortimeout` | Basement Bathroom Fan LoadLevelIndicatorTimeout | select |
| `select.basement_bathroom_fan_localprotection` | Basement Bathroom Fan LocalProtection | select |
| `select.basement_bathroom_fan_onoffledmode` | Basement Bathroom Fan OnOffLedMode | select |
| `select.basement_bathroom_fan_outputmode` | Basement Bathroom Fan OutputMode | select |
| `select.basement_bathroom_fan_singletapbehavior` | Basement Bathroom Fan SingleTapBehavior | select |
| `select.basement_bathroom_fan_smartbulbmode` | Basement Bathroom Fan SmartBulbMode | select |
| `select.basement_bathroom_fan_switchtype` | Basement Bathroom Fan SwitchType | select |
| `select.basement_bathroom_light_all_led_strip_effect_effect` | select.basement_bathroom_light_all_led_strip_effect_effect | select |
| `select.basement_bathroom_light_aux_switch_scenes` | select.basement_bathroom_light_aux_switch_scenes | select |
| `select.basement_bathroom_light_button_delay_time` | select.basement_bathroom_light_button_delay_time | select |
| `select.basement_bathroom_light_dimmer_mode` | select.basement_bathroom_light_dimmer_mode | select |
| `select.basement_bathroom_light_double_down_level_enable` | select.basement_bathroom_light_double_down_level_enable | select |
| `select.basement_bathroom_light_double_tap_config_to_clear_notification` | select.basement_bathroom_light_double_tap_config_to_clear_notification | select |
| `select.basement_bathroom_light_double_up_level_enable` | select.basement_bathroom_light_double_up_level_enable | select |
| `select.basement_bathroom_light_exclusion_behavior` | select.basement_bathroom_light_exclusion_behavior | select |
| `select.basement_bathroom_light_firmware_progress_led` | select.basement_bathroom_light_firmware_progress_led | select |
| `select.basement_bathroom_light_forward_z_wave_commands_to_associated_devices` | select.basement_bathroom_light_forward_z_wave_commands_to_associated_devices | select |
| `select.basement_bathroom_light_increase_output_power_non_neutral` | select.basement_bathroom_light_increase_output_power_non_neutral | select |
| `select.basement_bathroom_light_invert_switch` | select.basement_bathroom_light_invert_switch | select |
| `select.basement_bathroom_light_led_bar_in_on_off_mode` | select.basement_bathroom_light_led_bar_in_on_off_mode | select |
| `select.basement_bathroom_light_led_brightness_scaling` | select.basement_bathroom_light_led_brightness_scaling | select |
| `select.basement_bathroom_light_led1_strip_effect_effect` | select.basement_bathroom_light_led1_strip_effect_effect | select |
| `select.basement_bathroom_light_led2_strip_effect_effect` | select.basement_bathroom_light_led2_strip_effect_effect | select |
| `select.basement_bathroom_light_led3_strip_effect_effect` | select.basement_bathroom_light_led3_strip_effect_effect | select |
| `select.basement_bathroom_light_led4_strip_effect_effect` | select.basement_bathroom_light_led4_strip_effect_effect | select |
| `select.basement_bathroom_light_led5_strip_effect_effect` | select.basement_bathroom_light_led5_strip_effect_effect | select |
| `select.basement_bathroom_light_led6_strip_effect_effect` | select.basement_bathroom_light_led6_strip_effect_effect | select |
| `select.basement_bathroom_light_led7_strip_effect_effect` | select.basement_bathroom_light_led7_strip_effect_effect | select |
| `select.basement_bathroom_light_local_protection_state` | Basement Bathroom Light Local protection state | select |
| `select.basement_bathroom_light_relay_click_in_on_off_mode` | select.basement_bathroom_light_relay_click_in_on_off_mode | select |
| `select.basement_bathroom_light_rf_protection_state` | Basement Bathroom Light RF protection state | select |
| `select.basement_bathroom_light_send_local_commands_to_associated_devices` | select.basement_bathroom_light_send_local_commands_to_associated_devices | select |
| `select.basement_bathroom_light_smart_bulb_mode` | select.basement_bathroom_light_smart_bulb_mode | select |
| `select.basement_bathroom_light_switch_type` | select.basement_bathroom_light_switch_type | select |
| `select.basement_shower_light_all_led_strip_effect_effect` | select.basement_shower_light_all_led_strip_effect_effect | select |
| `select.basement_shower_light_aux_switch_scenes` | select.basement_shower_light_aux_switch_scenes | select |
| `select.basement_shower_light_button_delay_time` | select.basement_shower_light_button_delay_time | select |
| `select.basement_shower_light_dimmer_mode` | select.basement_shower_light_dimmer_mode | select |
| `select.basement_shower_light_double_down_level_enable` | select.basement_shower_light_double_down_level_enable | select |
| `select.basement_shower_light_double_tap_config_to_clear_notification` | select.basement_shower_light_double_tap_config_to_clear_notification | select |
| `select.basement_shower_light_double_up_level_enable` | select.basement_shower_light_double_up_level_enable | select |
| `select.basement_shower_light_exclusion_behavior` | select.basement_shower_light_exclusion_behavior | select |
| `select.basement_shower_light_firmware_progress_led` | select.basement_shower_light_firmware_progress_led | select |
| `select.basement_shower_light_forward_z_wave_commands_to_associated_devices` | select.basement_shower_light_forward_z_wave_commands_to_associated_devices | select |
| `select.basement_shower_light_increase_output_power_non_neutral` | select.basement_shower_light_increase_output_power_non_neutral | select |
| `select.basement_shower_light_invert_switch` | select.basement_shower_light_invert_switch | select |
| `select.basement_shower_light_led_bar_in_on_off_mode` | select.basement_shower_light_led_bar_in_on_off_mode | select |
| `select.basement_shower_light_led_brightness_scaling` | select.basement_shower_light_led_brightness_scaling | select |
| `select.basement_shower_light_led1_strip_effect_effect` | select.basement_shower_light_led1_strip_effect_effect | select |
| `select.basement_shower_light_led2_strip_effect_effect` | select.basement_shower_light_led2_strip_effect_effect | select |
| `select.basement_shower_light_led3_strip_effect_effect` | select.basement_shower_light_led3_strip_effect_effect | select |
| `select.basement_shower_light_led4_strip_effect_effect` | select.basement_shower_light_led4_strip_effect_effect | select |
| `select.basement_shower_light_led5_strip_effect_effect` | select.basement_shower_light_led5_strip_effect_effect | select |
| `select.basement_shower_light_led6_strip_effect_effect` | select.basement_shower_light_led6_strip_effect_effect | select |
| `select.basement_shower_light_led7_strip_effect_effect` | select.basement_shower_light_led7_strip_effect_effect | select |
| `select.basement_shower_light_local_protection_state` | Basement Shower Light Local protection state | select |
| `select.basement_shower_light_relay_click_in_on_off_mode` | select.basement_shower_light_relay_click_in_on_off_mode | select |
| `select.basement_shower_light_rf_protection_state` | Basement Shower Light RF protection state | select |
| `select.basement_shower_light_send_local_commands_to_associated_devices` | select.basement_shower_light_send_local_commands_to_associated_devices | select |
| `select.basement_shower_light_smart_bulb_mode` | select.basement_shower_light_smart_bulb_mode | select |
| `select.basement_shower_light_switch_type` | select.basement_shower_light_switch_type | select |
| `sensor.0x8c8b48fffe4c5267_last_seen` | sensor.0x8c8b48fffe4c5267_last_seen | sensor |
| `sensor.0x8c8b48fffe4c5267_linkquality` | sensor.0x8c8b48fffe4c5267_linkquality | sensor |
| `sensor.0xa4c13809cf47ffff_last_seen` | Basement Bathroom AirGuard TH Last seen | sensor |
| `sensor.0xa4c13809cf47ffff_linkquality` | Basement Bathroom AirGuard TH Linkquality | sensor |
| `sensor.basement_bathroom_airguard_th_battery` | Basement Bathroom AirGuard TH Battery | sensor |
| `sensor.basement_bathroom_airguard_th_humidity` | Basement Bathroom AirGuard TH Humidity | sensor |
| `sensor.basement_bathroom_airguard_th_temperature` | Basement Bathroom AirGuard TH Temperature | sensor |
| `sensor.basement_bathroom_airguard_th_voltage` | Basement Bathroom AirGuard TH Voltage | sensor |
| `sensor.basement_bathroom_fan_current` | Basement Bathroom Fan Current | sensor |
| `sensor.basement_bathroom_fan_devicebindnumber` | Basement Bathroom Fan DeviceBindNumber | sensor |
| `sensor.basement_bathroom_fan_energy` | Basement Bathroom Fan Energy | sensor |
| `sensor.basement_bathroom_fan_humidity` | Basement Bathroom Fan Humidity | sensor |
| `sensor.basement_bathroom_fan_individual_led_effect` | Basement Bathroom Fan Individual led effect | sensor |
| `sensor.basement_bathroom_fan_internaltemperature` | Basement Bathroom Fan Temperature | sensor |
| `sensor.basement_bathroom_fan_led_effect` | Basement Bathroom Fan Led effect | sensor |
| `sensor.basement_bathroom_fan_notificationcomplete` | Basement Bathroom Fan NotificationComplete | sensor |
| `sensor.basement_bathroom_fan_overheat` | Basement Bathroom Fan Overheat | sensor |
| `sensor.basement_bathroom_fan_power` | Basement Bathroom Fan Power | sensor |
| `sensor.basement_bathroom_fan_remoteprotection` | Basement Bathroom Fan RemoteProtection | sensor |
| `sensor.basement_bathroom_fan_stopwatch` | Basement Bathroom Fan StopWatch | sensor |
| `sensor.basement_bathroom_fan_temperature` | Basement Bathroom Fan Temperature | sensor |
| `sensor.basement_bathroom_fan_voltage` | Basement Bathroom Fan Voltage | sensor |
| `sensor.basement_bathroom_light_commands_dropped_rx` | sensor.basement_bathroom_light_commands_dropped_rx | sensor |
| `sensor.basement_bathroom_light_commands_dropped_tx` | sensor.basement_bathroom_light_commands_dropped_tx | sensor |
| `sensor.basement_bathroom_light_dimming_mode` | sensor.basement_bathroom_light_dimming_mode | sensor |
| `sensor.basement_bathroom_light_electric_consumption_kwh` | Basement Bathroom Light Electric Consumption [kWh] | sensor |
| `sensor.basement_bathroom_light_electric_consumption_w` | Basement Bathroom Light Electric Consumption [W] | sensor |
| `sensor.basement_bathroom_light_internal_temperature` | sensor.basement_bathroom_light_internal_temperature | sensor |
| `sensor.basement_bathroom_light_last_seen` | sensor.basement_bathroom_light_last_seen | sensor |
| `sensor.basement_bathroom_light_node_status` | Basement Bathroom Light Node status | sensor |
| `sensor.basement_bathroom_light_overheat_detected` | sensor.basement_bathroom_light_overheat_detected | sensor |
| `sensor.basement_bathroom_light_power_type` | sensor.basement_bathroom_light_power_type | sensor |
| `sensor.basement_bathroom_light_round_trip_time` | sensor.basement_bathroom_light_round_trip_time | sensor |
| `sensor.basement_bathroom_light_signal_strength` | sensor.basement_bathroom_light_signal_strength | sensor |
| `sensor.basement_bathroom_light_successful_commands_rx` | sensor.basement_bathroom_light_successful_commands_rx | sensor |
| `sensor.basement_bathroom_light_successful_commands_tx` | sensor.basement_bathroom_light_successful_commands_tx | sensor |
| `sensor.basement_bathroom_light_timed_out_responses` | sensor.basement_bathroom_light_timed_out_responses | sensor |
| `sensor.basement_shower_light_commands_dropped_rx` | sensor.basement_shower_light_commands_dropped_rx | sensor |
| `sensor.basement_shower_light_commands_dropped_tx` | sensor.basement_shower_light_commands_dropped_tx | sensor |
| `sensor.basement_shower_light_dimming_mode` | sensor.basement_shower_light_dimming_mode | sensor |
| `sensor.basement_shower_light_electric_consumption_kwh` | Basement Shower Light Electric Consumption [kWh] | sensor |
| `sensor.basement_shower_light_electric_consumption_w` | Basement Shower Light Electric Consumption [W] | sensor |
| `sensor.basement_shower_light_internal_temperature` | sensor.basement_shower_light_internal_temperature | sensor |
| `sensor.basement_shower_light_last_seen` | sensor.basement_shower_light_last_seen | sensor |
| `sensor.basement_shower_light_node_status` | Basement Shower Light Node status | sensor |
| `sensor.basement_shower_light_overheat_detected` | sensor.basement_shower_light_overheat_detected | sensor |
| `sensor.basement_shower_light_power_type` | sensor.basement_shower_light_power_type | sensor |
| `sensor.basement_shower_light_round_trip_time` | sensor.basement_shower_light_round_trip_time | sensor |
| `sensor.basement_shower_light_signal_strength` | sensor.basement_shower_light_signal_strength | sensor |
| `sensor.basement_shower_light_successful_commands_rx` | sensor.basement_shower_light_successful_commands_rx | sensor |
| `sensor.basement_shower_light_successful_commands_tx` | sensor.basement_shower_light_successful_commands_tx | sensor |
| `sensor.basement_shower_light_timed_out_responses` | sensor.basement_shower_light_timed_out_responses | sensor |
| `update.basement_bathroom_airguard_th` | Basement Bathroom AirGuard TH | update |
| `update.basement_bathroom_fan` | Basement Bathroom Fan | update |
| `update.basement_bathroom_light_firmware` | Basement Bathroom Light Firmware | update |
| `update.basement_shower_light_firmware` | Basement Shower Light Firmware | update |
