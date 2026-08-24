# Mikes Office

> Read-only Home Assistant inventory captured 2026-08-24. No devices or configuration were changed.

- Floor classification: Basement
- Area: Mikes Office
- Devices: 22
- Entities: 402
- Inclusion rule: assigned to this Basement-floor area.

## Devices

| Device | Manufacturer | Model | Integration | Device ID |
|---|---|---|---|---|
| Mikes Office Ceiling Fan | Inovelli | Fan controller | zigbee2mqtt | `b1cb54ccee5be00d4382aac519ba4cc0` |
| Basement Amazon Fire Outlet | Sense Labs, Inc. | Sense | sense | `ea152c71ec44e9353556973d94a3c249` |
| Basement Bluetooth Proxy (B0:B2:1C:A8:D9:66) | Espressif Inc. (esphome) | esp32 | unknown | `d203c1ede096efd49d70e5822973a711` |
| HS300 | TP-Link | HS300 | unknown | `fb39dfb19eb5314b40c5720a903317d9` |
| michael's 2nd Alexa App for PC | Amazon | Windows App | alexa_media | `ba444c5037079c2e50cb9ff4186ea706` |
| michael's 3rd Alexa App for PC | Amazon | Windows App | alexa_media | `448e2b1ec8886f0eee76068b59dad72e` |
| michael's Alexa App for PC | Amazon | Windows App | alexa_media | `db04dc25d4629b702263746b3178c37b` |
| Mikes Office Airthings | Airthings | View Plus | airthings | `89e947496e6b8e51c86543c23208f73c` |
| Mikes Office Desk Button | SmartThings | Button | zigbee2mqtt | `98853abe2ead4cab005c38b0cf3a6ccd` |
| Mikes Office Light | Inovelli | VZW31-SN | zwave_js | `bc2ceb6c5e4ff6e731c4553b3d3cdde5` |
| Mikes Office Motion Nightlight | Third Reality | Zigbee multi-function night light | zigbee2mqtt | `349e29757b18381510772026c9d78e52` |
| Office of Mike Core 300s | VeSync | Core300S | vesync | `db8627f119757ec00c84e221e472c8d8` |
| Office of Mike Ecobee Sensor | ecobee | ecobee Room Sensor | ecobee | `c68fac5af6e7fbb16f08960519b5ce10` |
| Office of Mike Surge Protector | TP-Link | HS300 | tplink | `5154f33f15432f4ea97f51aeeb659f6e` |
| Office of Mike Surge Protector | TP-Link | HS300 | unknown | `c324a778b8bfee11af64d838b9c10c3e` |
| TP-LINK_Power Strip_9041 | TP-Link | HS300 | tplink | `a8a74629bef2a2baa6c4b3aca5e7aaeb` |
| TP-LINK_Power Strip_9041 Mikes Office AirPurifier Outlet | TP-Link | Socket for HS300(US) | tplink | `57009250d23e41a4d2a560bb11a71163` |
| TP-LINK_Power Strip_9041 Mikes Office Amazon Echo Outlet | TP-Link | Socket for HS300(US) | tplink | `d26c0c643f35d8406d9e5d65a2d9afb3` |
| TP-LINK_Power Strip_9041 Mikes Office BT Proxy Outlet | TP-Link | Socket for HS300(US) | tplink | `9f9e98194c9eee4202bc5a00d47af606` |
| TP-LINK_Power Strip_9041 Mikes Office Grow Light Outlet | TP-Link | Socket for HS300(US) | tplink | `9c6f78aa4cbd036a0dd1572f8d14cd1f` |
| TP-LINK_Power Strip_9041 Mikes Office Open Plug 1 | TP-Link | Socket for HS300(US) | tplink | `232d0bdb1264a048d6b87f6862d05d02` |
| TP-LINK_Power Strip_9041 Mikes Office Printer Outlet | TP-Link | Socket for HS300(US) | tplink | `fd1995eed36df870242b9fc8038743ca` |

## Entities

| Entity ID | Friendly name | Domain |
|---|---|---|
| `automation.mikes_office_night_light_motion` | Mikes Office Nightlight | automation |
| `automation.test_automation2` | Mikes Office SmartThings Button - MQTT | automation |
| `binary_sensor.mikes_office_ceiling_fan_update_available` | binary_sensor.mikes_office_ceiling_fan_update_available | binary_sensor |
| `binary_sensor.mikes_office_light_overheat` | binary_sensor.mikes_office_light_overheat | binary_sensor |
| `binary_sensor.mikes_office_motion_nightlight_occupancy` | Mikes Office Motion Nightlight Occupancy | binary_sensor |
| `binary_sensor.mikes_office_motion_nightlight_update_available` | Mikes Office Motion Nightlight | binary_sensor |
| `binary_sensor.office_of_mike_ecobee_sensor_occupancy` | Office of Mike Ecobee Sensor Occupancy | binary_sensor |
| `binary_sensor.office_of_mike_surge_protector_cloud_connection` | Office of Mike Surge Protector Cloud connection | binary_sensor |
| `binary_sensor.tp_link_power_strip_9041_cloud_connection` | TP-LINK_Power Strip_9041 Cloud connection | binary_sensor |
| `button.mikes_office_ceiling_fan_identify` | Mikes Office Ceiling Fan Identify | button |
| `button.mikes_office_light_identify` | Mikes Office Light Identify | button |
| `button.mikes_office_light_ping` | Mikes Office Light Ping | button |
| `button.mikes_office_light_reset_accumulated_values` | Mikes Office Light Reset accumulated values | button |
| `button.office_of_mike_surge_protector_restart` | button.office_of_mike_surge_protector_restart | button |
| `button.tp_link_power_strip_9041_restart` | button.tp_link_power_strip_9041_restart | button |
| `device_tracker.mike_s_office_surge_protector` | HS300 Mike's Office Cabinet Surge Protector | device_tracker |
| `device_tracker.office_of_mike_surge_protector` | Office of Mike Surge Protector HS300 | device_tracker |
| `event.mikes_office_light_scene_001` | Mikes Office Light Scene 001 | event |
| `event.mikes_office_light_scene_002` | Mikes Office Light Scene 002 | event |
| `event.mikes_office_light_scene_003` | Mikes Office Light Scene 003 | event |
| `fan.mikes_office_ceiling_fan` | Mikes Office Ceiling Fan | fan |
| `fan.office_of_mike_core_300s` | Office of Mike Core 300s | fan |
| `light.mikes_office_light` | Mikes Office Light | light |
| `light.mikes_office_motion_nightlight` | Mikes Office Motion Nightlight | light |
| `media_player.michael_s_2nd_alexa_app_for_pc` | michael's 2nd Alexa App for PC | media_player |
| `media_player.michael_s_3rd_alexa_app_for_pc` | michael's 3rd Alexa App for PC | media_player |
| `media_player.michael_s_alexa_app_for_pc` | michael's Alexa App for PC | media_player |
| `number.mikes_office_ceiling_fan_autotimeroff` | Mikes Office Ceiling Fan AutoTimerOff | number |
| `number.mikes_office_ceiling_fan_brightnesslevelfordoubletapdown` | Mikes Office Ceiling Fan BrightnessLevelForDoubleTapDown | number |
| `number.mikes_office_ceiling_fan_brightnesslevelfordoubletapup` | Mikes Office Ceiling Fan BrightnessLevelForDoubleTapUp | number |
| `number.mikes_office_ceiling_fan_defaultled1colorwhenoff` | Mikes Office Ceiling Fan DefaultLed1ColorWhenOff | number |
| `number.mikes_office_ceiling_fan_defaultled1colorwhenon` | Mikes Office Ceiling Fan DefaultLed1ColorWhenOn | number |
| `number.mikes_office_ceiling_fan_defaultled1intensitywhenoff` | Mikes Office Ceiling Fan DefaultLed1IntensityWhenOff | number |
| `number.mikes_office_ceiling_fan_defaultled1intensitywhenon` | Mikes Office Ceiling Fan DefaultLed1IntensityWhenOn | number |
| `number.mikes_office_ceiling_fan_defaultled2colorwhenoff` | Mikes Office Ceiling Fan DefaultLed2ColorWhenOff | number |
| `number.mikes_office_ceiling_fan_defaultled2colorwhenon` | Mikes Office Ceiling Fan DefaultLed2ColorWhenOn | number |
| `number.mikes_office_ceiling_fan_defaultled2intensitywhenoff` | Mikes Office Ceiling Fan DefaultLed2IntensityWhenOff | number |
| `number.mikes_office_ceiling_fan_defaultled2intensitywhenon` | Mikes Office Ceiling Fan DefaultLed2IntensityWhenOn | number |
| `number.mikes_office_ceiling_fan_defaultled3colorwhenoff` | Mikes Office Ceiling Fan DefaultLed3ColorWhenOff | number |
| `number.mikes_office_ceiling_fan_defaultled3colorwhenon` | Mikes Office Ceiling Fan DefaultLed3ColorWhenOn | number |
| `number.mikes_office_ceiling_fan_defaultled3intensitywhenoff` | Mikes Office Ceiling Fan DefaultLed3IntensityWhenOff | number |
| `number.mikes_office_ceiling_fan_defaultled3intensitywhenon` | Mikes Office Ceiling Fan DefaultLed3IntensityWhenOn | number |
| `number.mikes_office_ceiling_fan_defaultled4colorwhenoff` | Mikes Office Ceiling Fan DefaultLed4ColorWhenOff | number |
| `number.mikes_office_ceiling_fan_defaultled4colorwhenon` | Mikes Office Ceiling Fan DefaultLed4ColorWhenOn | number |
| `number.mikes_office_ceiling_fan_defaultled4intensitywhenoff` | Mikes Office Ceiling Fan DefaultLed4IntensityWhenOff | number |
| `number.mikes_office_ceiling_fan_defaultled4intensitywhenon` | Mikes Office Ceiling Fan DefaultLed4IntensityWhenOn | number |
| `number.mikes_office_ceiling_fan_defaultled5colorwhenoff` | Mikes Office Ceiling Fan DefaultLed5ColorWhenOff | number |
| `number.mikes_office_ceiling_fan_defaultled5colorwhenon` | Mikes Office Ceiling Fan DefaultLed5ColorWhenOn | number |
| `number.mikes_office_ceiling_fan_defaultled5intensitywhenoff` | Mikes Office Ceiling Fan DefaultLed5IntensityWhenOff | number |
| `number.mikes_office_ceiling_fan_defaultled5intensitywhenon` | Mikes Office Ceiling Fan DefaultLed5IntensityWhenOn | number |
| `number.mikes_office_ceiling_fan_defaultled6colorwhenoff` | Mikes Office Ceiling Fan DefaultLed6ColorWhenOff | number |
| `number.mikes_office_ceiling_fan_defaultled6colorwhenon` | Mikes Office Ceiling Fan DefaultLed6ColorWhenOn | number |
| `number.mikes_office_ceiling_fan_defaultled6intensitywhenoff` | Mikes Office Ceiling Fan DefaultLed6IntensityWhenOff | number |
| `number.mikes_office_ceiling_fan_defaultled6intensitywhenon` | Mikes Office Ceiling Fan DefaultLed6IntensityWhenOn | number |
| `number.mikes_office_ceiling_fan_defaultled7colorwhenoff` | Mikes Office Ceiling Fan DefaultLed7ColorWhenOff | number |
| `number.mikes_office_ceiling_fan_defaultled7colorwhenon` | Mikes Office Ceiling Fan DefaultLed7ColorWhenOn | number |
| `number.mikes_office_ceiling_fan_defaultled7intensitywhenoff` | Mikes Office Ceiling Fan DefaultLed7IntensityWhenOff | number |
| `number.mikes_office_ceiling_fan_defaultled7intensitywhenon` | Mikes Office Ceiling Fan DefaultLed7IntensityWhenOn | number |
| `number.mikes_office_ceiling_fan_defaultlevellocal` | Mikes Office Ceiling Fan DefaultLevelLocal | number |
| `number.mikes_office_ceiling_fan_defaultlevelremote` | Mikes Office Ceiling Fan DefaultLevelRemote | number |
| `number.mikes_office_ceiling_fan_dimmingspeeddownlocal` | Mikes Office Ceiling Fan DimmingSpeedDownLocal | number |
| `number.mikes_office_ceiling_fan_dimmingspeeddownremote` | Mikes Office Ceiling Fan DimmingSpeedDownRemote | number |
| `number.mikes_office_ceiling_fan_dimmingspeeduplocal` | Mikes Office Ceiling Fan DimmingSpeedUpLocal | number |
| `number.mikes_office_ceiling_fan_dimmingspeedupremote` | Mikes Office Ceiling Fan DimmingSpeedUpRemote | number |
| `number.mikes_office_ceiling_fan_fanledleveltype` | Mikes Office Ceiling Fan FanLedLevelType | number |
| `number.mikes_office_ceiling_fan_highlevelforfancontrolmode` | Mikes Office Ceiling Fan HighLevelForFanControlMode | number |
| `number.mikes_office_ceiling_fan_ledcolorforfancontrolmode` | Mikes Office Ceiling Fan LedColorForFanControlMode | number |
| `number.mikes_office_ceiling_fan_ledcolorwhenoff` | Mikes Office Ceiling Fan LedColorWhenOff | number |
| `number.mikes_office_ceiling_fan_ledcolorwhenon` | Mikes Office Ceiling Fan LedColorWhenOn | number |
| `number.mikes_office_ceiling_fan_ledintensitywhenoff` | Mikes Office Ceiling Fan LedIntensityWhenOff | number |
| `number.mikes_office_ceiling_fan_ledintensitywhenon` | Mikes Office Ceiling Fan LedIntensityWhenOn | number |
| `number.mikes_office_ceiling_fan_lowlevelforfancontrolmode` | Mikes Office Ceiling Fan LowLevelForFanControlMode | number |
| `number.mikes_office_ceiling_fan_maximumlevel` | Mikes Office Ceiling Fan MaximumLevel | number |
| `number.mikes_office_ceiling_fan_mediumlevelforfancontrolmode` | Mikes Office Ceiling Fan MediumLevelForFanControlMode | number |
| `number.mikes_office_ceiling_fan_minimumlevel` | Mikes Office Ceiling Fan MinimumLevel | number |
| `number.mikes_office_ceiling_fan_nonneutralauxlowgear` | Mikes Office Ceiling Fan NonNeutralAuxLowGear | number |
| `number.mikes_office_ceiling_fan_nonneutralauxmediumgear` | Mikes Office Ceiling Fan NonNeutralAuxMediumGear | number |
| `number.mikes_office_ceiling_fan_quickstarttime` | Mikes Office Ceiling Fan QuickStartTime | number |
| `number.mikes_office_ceiling_fan_ramprateofftoonlocal` | Mikes Office Ceiling Fan RampRateOffToOnLocal | number |
| `number.mikes_office_ceiling_fan_ramprateofftoonremote` | Mikes Office Ceiling Fan RampRateOffToOnRemote | number |
| `number.mikes_office_ceiling_fan_ramprateontoofflocal` | Mikes Office Ceiling Fan RampRateOnToOffLocal | number |
| `number.mikes_office_ceiling_fan_ramprateontooffremote` | Mikes Office Ceiling Fan RampRateOnToOffRemote | number |
| `number.mikes_office_ceiling_fan_stateafterpowerrestored` | Mikes Office Ceiling Fan StateAfterPowerRestored | number |
| `number.mikes_office_light_all_led_strip_effect_color` | number.mikes_office_light_all_led_strip_effect_color | number |
| `number.mikes_office_light_all_led_strip_effect_duration` | number.mikes_office_light_all_led_strip_effect_duration | number |
| `number.mikes_office_light_all_led_strip_effect_level` | number.mikes_office_light_all_led_strip_effect_level | number |
| `number.mikes_office_light_auto_off_timer` | number.mikes_office_light_auto_off_timer | number |
| `number.mikes_office_light_default_all_led_strip_brightness_when_off` | number.mikes_office_light_default_all_led_strip_brightness_when_off | number |
| `number.mikes_office_light_default_all_led_strip_brightness_when_on` | number.mikes_office_light_default_all_led_strip_brightness_when_on | number |
| `number.mikes_office_light_default_all_led_strip_color_when_off` | number.mikes_office_light_default_all_led_strip_color_when_off | number |
| `number.mikes_office_light_default_all_led_strip_color_when_on` | number.mikes_office_light_default_all_led_strip_color_when_on | number |
| `number.mikes_office_light_default_level_local` | number.mikes_office_light_default_level_local | number |
| `number.mikes_office_light_default_level_remote` | number.mikes_office_light_default_level_remote | number |
| `number.mikes_office_light_dimming_speed_down_local` | number.mikes_office_light_dimming_speed_down_local | number |
| `number.mikes_office_light_dimming_speed_down_remote` | number.mikes_office_light_dimming_speed_down_remote | number |
| `number.mikes_office_light_dimming_speed_up_local` | number.mikes_office_light_dimming_speed_up_local | number |
| `number.mikes_office_light_dimming_speed_up_remote` | number.mikes_office_light_dimming_speed_up_remote | number |
| `number.mikes_office_light_double_down_level` | number.mikes_office_light_double_down_level | number |
| `number.mikes_office_light_double_up_level` | number.mikes_office_light_double_up_level | number |
| `number.mikes_office_light_energy_change_report_threshold` | number.mikes_office_light_energy_change_report_threshold | number |
| `number.mikes_office_light_indicator_value` | Mikes Office Light Indicator value | number |
| `number.mikes_office_light_led1_strip_effect_color` | number.mikes_office_light_led1_strip_effect_color | number |
| `number.mikes_office_light_led1_strip_effect_duration` | number.mikes_office_light_led1_strip_effect_duration | number |
| `number.mikes_office_light_led1_strip_effect_level` | number.mikes_office_light_led1_strip_effect_level | number |
| `number.mikes_office_light_led2_strip_effect_color` | number.mikes_office_light_led2_strip_effect_color | number |
| `number.mikes_office_light_led2_strip_effect_duration` | number.mikes_office_light_led2_strip_effect_duration | number |
| `number.mikes_office_light_led2_strip_effect_level` | number.mikes_office_light_led2_strip_effect_level | number |
| `number.mikes_office_light_led3_strip_effect_color` | number.mikes_office_light_led3_strip_effect_color | number |
| `number.mikes_office_light_led3_strip_effect_duration` | number.mikes_office_light_led3_strip_effect_duration | number |
| `number.mikes_office_light_led3_strip_effect_level` | number.mikes_office_light_led3_strip_effect_level | number |
| `number.mikes_office_light_led4_strip_effect_color` | number.mikes_office_light_led4_strip_effect_color | number |
| `number.mikes_office_light_led4_strip_effect_duration` | number.mikes_office_light_led4_strip_effect_duration | number |
| `number.mikes_office_light_led4_strip_effect_level` | number.mikes_office_light_led4_strip_effect_level | number |
| `number.mikes_office_light_led5_strip_effect_color` | number.mikes_office_light_led5_strip_effect_color | number |
| `number.mikes_office_light_led5_strip_effect_duration` | number.mikes_office_light_led5_strip_effect_duration | number |
| `number.mikes_office_light_led5_strip_effect_level` | number.mikes_office_light_led5_strip_effect_level | number |
| `number.mikes_office_light_led6_strip_effect_color` | number.mikes_office_light_led6_strip_effect_color | number |
| `number.mikes_office_light_led6_strip_effect_duration` | number.mikes_office_light_led6_strip_effect_duration | number |
| `number.mikes_office_light_led6_strip_effect_level` | number.mikes_office_light_led6_strip_effect_level | number |
| `number.mikes_office_light_led7_strip_effect_color` | number.mikes_office_light_led7_strip_effect_color | number |
| `number.mikes_office_light_led7_strip_effect_duration` | number.mikes_office_light_led7_strip_effect_duration | number |
| `number.mikes_office_light_led7_strip_effect_level` | number.mikes_office_light_led7_strip_effect_level | number |
| `number.mikes_office_light_load_level_indicator_timeout` | number.mikes_office_light_load_level_indicator_timeout | number |
| `number.mikes_office_light_maximum_level` | number.mikes_office_light_maximum_level | number |
| `number.mikes_office_light_minimum_level` | number.mikes_office_light_minimum_level | number |
| `number.mikes_office_light_power_change_report_threshold` | number.mikes_office_light_power_change_report_threshold | number |
| `number.mikes_office_light_power_energy_report_interval` | number.mikes_office_light_power_energy_report_interval | number |
| `number.mikes_office_light_ramp_rate_off_to_on_local` | number.mikes_office_light_ramp_rate_off_to_on_local | number |
| `number.mikes_office_light_ramp_rate_off_to_on_remote` | number.mikes_office_light_ramp_rate_off_to_on_remote | number |
| `number.mikes_office_light_ramp_rate_on_to_off_local` | number.mikes_office_light_ramp_rate_on_to_off_local | number |
| `number.mikes_office_light_ramp_rate_on_to_off_remote` | number.mikes_office_light_ramp_rate_on_to_off_remote | number |
| `number.mikes_office_light_state_after_power_restored` | number.mikes_office_light_state_after_power_restored | number |
| `select.mikes_office_ceiling_fan_auxswitchuniquescenes` | Mikes Office Ceiling Fan AuxSwitchUniqueScenes | select |
| `select.mikes_office_ceiling_fan_bindingofftoonsynclevel` | Mikes Office Ceiling Fan BindingOffToOnSyncLevel | select |
| `select.mikes_office_ceiling_fan_buttondelay` | Mikes Office Ceiling Fan ButtonDelay | select |
| `select.mikes_office_ceiling_fan_doubletapclearnotifications` | Mikes Office Ceiling Fan DoubleTapClearNotifications | select |
| `select.mikes_office_ceiling_fan_doubletapdowntoparam56` | Mikes Office Ceiling Fan DoubleTapDownToParam56 | select |
| `select.mikes_office_ceiling_fan_doubletapuptoparam55` | Mikes Office Ceiling Fan DoubleTapUpToParam55 | select |
| `select.mikes_office_ceiling_fan_fancontrolmode` | Mikes Office Ceiling Fan FanControlMode | select |
| `select.mikes_office_ceiling_fan_fantimermode` | Mikes Office Ceiling Fan FanTimerMode | select |
| `select.mikes_office_ceiling_fan_firmwareupdateinprogressindicator` | Mikes Office Ceiling Fan FirmwareUpdateInProgressIndicator | select |
| `select.mikes_office_ceiling_fan_identify` | Mikes Office Ceiling Fan MQTT Select | select |
| `select.mikes_office_ceiling_fan_invertswitch` | Mikes Office Ceiling Fan InvertSwitch | select |
| `select.mikes_office_ceiling_fan_loadlevelindicatortimeout` | Mikes Office Ceiling Fan LoadLevelIndicatorTimeout | select |
| `select.mikes_office_ceiling_fan_localprotection` | Mikes Office Ceiling Fan LocalProtection | select |
| `select.mikes_office_ceiling_fan_onoffledmode` | Mikes Office Ceiling Fan OnOffLedMode | select |
| `select.mikes_office_ceiling_fan_outputmode` | Mikes Office Ceiling Fan OutputMode | select |
| `select.mikes_office_ceiling_fan_singletapbehavior` | Mikes Office Ceiling Fan SingleTapBehavior | select |
| `select.mikes_office_ceiling_fan_smartbulbmode` | Mikes Office Ceiling Fan SmartBulbMode | select |
| `select.mikes_office_ceiling_fan_switchtype` | Mikes Office Ceiling Fan SwitchType | select |
| `select.mikes_office_light_all_led_strip_effect_effect` | select.mikes_office_light_all_led_strip_effect_effect | select |
| `select.mikes_office_light_aux_switch_scenes` | select.mikes_office_light_aux_switch_scenes | select |
| `select.mikes_office_light_button_delay_time` | select.mikes_office_light_button_delay_time | select |
| `select.mikes_office_light_dimmer_mode` | select.mikes_office_light_dimmer_mode | select |
| `select.mikes_office_light_double_down_to_param_56_level` | select.mikes_office_light_double_down_to_param_56_level | select |
| `select.mikes_office_light_double_tap_config_to_clear_notification` | select.mikes_office_light_double_tap_config_to_clear_notification | select |
| `select.mikes_office_light_double_up_to_param_55_level` | select.mikes_office_light_double_up_to_param_55_level | select |
| `select.mikes_office_light_exclusion_behavior` | select.mikes_office_light_exclusion_behavior | select |
| `select.mikes_office_light_firmware_progress_led` | select.mikes_office_light_firmware_progress_led | select |
| `select.mikes_office_light_forward_z_wave_commands_to_associated_devices` | select.mikes_office_light_forward_z_wave_commands_to_associated_devices | select |
| `select.mikes_office_light_increase_output_power_non_neutral` | select.mikes_office_light_increase_output_power_non_neutral | select |
| `select.mikes_office_light_invert_switch` | select.mikes_office_light_invert_switch | select |
| `select.mikes_office_light_led_bar_in_on_off_mode` | select.mikes_office_light_led_bar_in_on_off_mode | select |
| `select.mikes_office_light_led_brightness_scaling` | select.mikes_office_light_led_brightness_scaling | select |
| `select.mikes_office_light_led1_strip_effect_effect` | select.mikes_office_light_led1_strip_effect_effect | select |
| `select.mikes_office_light_led2_strip_effect_effect` | select.mikes_office_light_led2_strip_effect_effect | select |
| `select.mikes_office_light_led3_strip_effect_effect` | select.mikes_office_light_led3_strip_effect_effect | select |
| `select.mikes_office_light_led4_strip_effect_effect` | select.mikes_office_light_led4_strip_effect_effect | select |
| `select.mikes_office_light_led5_strip_effect_effect` | select.mikes_office_light_led5_strip_effect_effect | select |
| `select.mikes_office_light_led6_strip_effect_effect` | select.mikes_office_light_led6_strip_effect_effect | select |
| `select.mikes_office_light_led7_strip_effect_effect` | select.mikes_office_light_led7_strip_effect_effect | select |
| `select.mikes_office_light_local_protection_state` | Mikes Office Light Local protection state | select |
| `select.mikes_office_light_relay_click_in_on_off_mode` | select.mikes_office_light_relay_click_in_on_off_mode | select |
| `select.mikes_office_light_rf_protection_state` | Mikes Office Light RF protection state | select |
| `select.mikes_office_light_send_local_commands_to_associated_devices` | select.mikes_office_light_send_local_commands_to_associated_devices | select |
| `select.mikes_office_light_smart_bulb_mode` | select.mikes_office_light_smart_bulb_mode | select |
| `select.mikes_office_light_switch_type` | select.mikes_office_light_switch_type | select |
| `select.mikes_office_motion_nightlight_effect` | Mikes Office Motion Nightlight Effect | select |
| `select.mikes_office_motion_nightlight_power_on_behavior` | Mikes Office Motion Nightlight Power-on behavior | select |
| `select.office_of_mike_core_300s_night_light_level` | Office of Mike Core 300s Night light level | select |
| `sensor.0x286d970001130470_last_seen` | Mikes Office Desk Button Last seen | sensor |
| `sensor.0x286d970001130470_linkquality` | sensor.0x286d970001130470_linkquality | sensor |
| `sensor.michael_s_2nd_alexa_app_for_pc_next_alarm` | michael's 2nd Alexa App for PC Next alarm | sensor |
| `sensor.michael_s_2nd_alexa_app_for_pc_next_reminder` | michael's 2nd Alexa App for PC Next reminder | sensor |
| `sensor.michael_s_2nd_alexa_app_for_pc_next_timer` | michael's 2nd Alexa App for PC Next timer | sensor |
| `sensor.michael_s_3rd_alexa_app_for_pc_next_alarm` | michael's 3rd Alexa App for PC Next alarm | sensor |
| `sensor.michael_s_3rd_alexa_app_for_pc_next_reminder` | michael's 3rd Alexa App for PC Next reminder | sensor |
| `sensor.michael_s_3rd_alexa_app_for_pc_next_timer` | michael's 3rd Alexa App for PC Next timer | sensor |
| `sensor.michael_s_alexa_app_for_pc_next_alarm` | michael's Alexa App for PC Next alarm | sensor |
| `sensor.michael_s_alexa_app_for_pc_next_reminder` | michael's Alexa App for PC Next reminder | sensor |
| `sensor.michael_s_alexa_app_for_pc_next_timer` | michael's Alexa App for PC Next timer | sensor |
| `sensor.mikes_office_airpurifier_outlet_current` | TP-LINK_Power Strip_9041 Mikes Office AirPurifier Outlet Current | sensor |
| `sensor.mikes_office_airpurifier_outlet_current_consumption` | TP-LINK_Power Strip_9041 Mikes Office AirPurifier Outlet Current consumption | sensor |
| `sensor.mikes_office_airpurifier_outlet_today_s_consumption` | TP-LINK_Power Strip_9041 Mikes Office AirPurifier Outlet Today's consumption | sensor |
| `sensor.mikes_office_airpurifier_outlet_total_consumption` | TP-LINK_Power Strip_9041 Mikes Office AirPurifier Outlet Total consumption | sensor |
| `sensor.mikes_office_airpurifier_outlet_voltage` | TP-LINK_Power Strip_9041 Mikes Office AirPurifier Outlet Voltage | sensor |
| `sensor.mikes_office_airthings_battery` | Mikes Office Airthings Battery | sensor |
| `sensor.mikes_office_airthings_co2` | Mikes Office Airthings Carbon dioxide | sensor |
| `sensor.mikes_office_airthings_humidity` | Mikes Office Airthings Humidity | sensor |
| `sensor.mikes_office_airthings_pm1` | Mikes Office Airthings PM1 | sensor |
| `sensor.mikes_office_airthings_pm25` | Mikes Office Airthings PM2.5 | sensor |
| `sensor.mikes_office_airthings_pressure` | Mikes Office Airthings Atmospheric pressure | sensor |
| `sensor.mikes_office_airthings_radon` | Mikes Office Airthings Radon | sensor |
| `sensor.mikes_office_airthings_signal_strength` | sensor.mikes_office_airthings_signal_strength | sensor |
| `sensor.mikes_office_airthings_temperature` | Mikes Office Airthings Temperature | sensor |
| `sensor.mikes_office_airthings_voc` | Mikes Office Airthings Volatile organic compounds parts | sensor |
| `sensor.mikes_office_amazon_echo_outlet_current` | TP-LINK_Power Strip_9041 Mikes Office Amazon Echo Outlet Current | sensor |
| `sensor.mikes_office_amazon_echo_outlet_current_consumption` | TP-LINK_Power Strip_9041 Mikes Office Amazon Echo Outlet Current consumption | sensor |
| `sensor.mikes_office_amazon_echo_outlet_today_s_consumption` | TP-LINK_Power Strip_9041 Mikes Office Amazon Echo Outlet Today's consumption | sensor |
| `sensor.mikes_office_amazon_echo_outlet_total_consumption` | TP-LINK_Power Strip_9041 Mikes Office Amazon Echo Outlet Total consumption | sensor |
| `sensor.mikes_office_amazon_echo_outlet_voltage` | TP-LINK_Power Strip_9041 Mikes Office Amazon Echo Outlet Voltage | sensor |
| `sensor.mikes_office_bt_proxy_outlet_current` | TP-LINK_Power Strip_9041 Mikes Office BT Proxy Outlet Current | sensor |
| `sensor.mikes_office_bt_proxy_outlet_current_consumption` | TP-LINK_Power Strip_9041 Mikes Office BT Proxy Outlet Current consumption | sensor |
| `sensor.mikes_office_bt_proxy_outlet_today_s_consumption` | TP-LINK_Power Strip_9041 Mikes Office BT Proxy Outlet Today's consumption | sensor |
| `sensor.mikes_office_bt_proxy_outlet_total_consumption` | TP-LINK_Power Strip_9041 Mikes Office BT Proxy Outlet Total consumption | sensor |
| `sensor.mikes_office_bt_proxy_outlet_voltage` | TP-LINK_Power Strip_9041 Mikes Office BT Proxy Outlet Voltage | sensor |
| `sensor.mikes_office_ceiling_fan_autotimeroff` | sensor.mikes_office_ceiling_fan_autotimeroff | sensor |
| `sensor.mikes_office_ceiling_fan_auxswitchuniquescenes` | sensor.mikes_office_ceiling_fan_auxswitchuniquescenes | sensor |
| `sensor.mikes_office_ceiling_fan_bindingofftoonsynclevel` | sensor.mikes_office_ceiling_fan_bindingofftoonsynclevel | sensor |
| `sensor.mikes_office_ceiling_fan_breezemode` | Mikes Office Ceiling Fan Breeze mode | sensor |
| `sensor.mikes_office_ceiling_fan_brightnesslevelfordoubletapdown` | sensor.mikes_office_ceiling_fan_brightnesslevelfordoubletapdown | sensor |
| `sensor.mikes_office_ceiling_fan_brightnesslevelfordoubletapup` | sensor.mikes_office_ceiling_fan_brightnesslevelfordoubletapup | sensor |
| `sensor.mikes_office_ceiling_fan_buttondelay` | sensor.mikes_office_ceiling_fan_buttondelay | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled1colorwhenoff` | sensor.mikes_office_ceiling_fan_defaultled1colorwhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled1colorwhenon` | sensor.mikes_office_ceiling_fan_defaultled1colorwhenon | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled1intensitywhenoff` | sensor.mikes_office_ceiling_fan_defaultled1intensitywhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled1intensitywhenon` | sensor.mikes_office_ceiling_fan_defaultled1intensitywhenon | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled2colorwhenoff` | sensor.mikes_office_ceiling_fan_defaultled2colorwhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled2colorwhenon` | sensor.mikes_office_ceiling_fan_defaultled2colorwhenon | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled2intensitywhenoff` | sensor.mikes_office_ceiling_fan_defaultled2intensitywhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled2intensitywhenon` | sensor.mikes_office_ceiling_fan_defaultled2intensitywhenon | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled3colorwhenoff` | sensor.mikes_office_ceiling_fan_defaultled3colorwhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled3colorwhenon` | sensor.mikes_office_ceiling_fan_defaultled3colorwhenon | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled3intensitywhenoff` | sensor.mikes_office_ceiling_fan_defaultled3intensitywhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled3intensitywhenon` | sensor.mikes_office_ceiling_fan_defaultled3intensitywhenon | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled4colorwhenoff` | sensor.mikes_office_ceiling_fan_defaultled4colorwhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled4colorwhenon` | sensor.mikes_office_ceiling_fan_defaultled4colorwhenon | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled4intensitywhenoff` | sensor.mikes_office_ceiling_fan_defaultled4intensitywhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled4intensitywhenon` | sensor.mikes_office_ceiling_fan_defaultled4intensitywhenon | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled5colorwhenoff` | sensor.mikes_office_ceiling_fan_defaultled5colorwhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled5colorwhenon` | sensor.mikes_office_ceiling_fan_defaultled5colorwhenon | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled5intensitywhenoff` | sensor.mikes_office_ceiling_fan_defaultled5intensitywhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled5intensitywhenon` | sensor.mikes_office_ceiling_fan_defaultled5intensitywhenon | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled6colorwhenoff` | sensor.mikes_office_ceiling_fan_defaultled6colorwhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled6colorwhenon` | sensor.mikes_office_ceiling_fan_defaultled6colorwhenon | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled6intensitywhenoff` | sensor.mikes_office_ceiling_fan_defaultled6intensitywhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled6intensitywhenon` | sensor.mikes_office_ceiling_fan_defaultled6intensitywhenon | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled7colorwhenoff` | sensor.mikes_office_ceiling_fan_defaultled7colorwhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled7colorwhenon` | sensor.mikes_office_ceiling_fan_defaultled7colorwhenon | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled7intensitywhenoff` | sensor.mikes_office_ceiling_fan_defaultled7intensitywhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_defaultled7intensitywhenon` | sensor.mikes_office_ceiling_fan_defaultled7intensitywhenon | sensor |
| `sensor.mikes_office_ceiling_fan_defaultlevellocal` | sensor.mikes_office_ceiling_fan_defaultlevellocal | sensor |
| `sensor.mikes_office_ceiling_fan_defaultlevelremote` | sensor.mikes_office_ceiling_fan_defaultlevelremote | sensor |
| `sensor.mikes_office_ceiling_fan_devicebindnumber` | Mikes Office Ceiling Fan DeviceBindNumber | sensor |
| `sensor.mikes_office_ceiling_fan_dimmingspeeddownlocal` | sensor.mikes_office_ceiling_fan_dimmingspeeddownlocal | sensor |
| `sensor.mikes_office_ceiling_fan_dimmingspeeddownremote` | sensor.mikes_office_ceiling_fan_dimmingspeeddownremote | sensor |
| `sensor.mikes_office_ceiling_fan_dimmingspeeduplocal` | sensor.mikes_office_ceiling_fan_dimmingspeeduplocal | sensor |
| `sensor.mikes_office_ceiling_fan_dimmingspeedupremote` | sensor.mikes_office_ceiling_fan_dimmingspeedupremote | sensor |
| `sensor.mikes_office_ceiling_fan_doubletapclearnotifications` | sensor.mikes_office_ceiling_fan_doubletapclearnotifications | sensor |
| `sensor.mikes_office_ceiling_fan_doubletapdowntoparam56` | sensor.mikes_office_ceiling_fan_doubletapdowntoparam56 | sensor |
| `sensor.mikes_office_ceiling_fan_doubletapuptoparam55` | sensor.mikes_office_ceiling_fan_doubletapuptoparam55 | sensor |
| `sensor.mikes_office_ceiling_fan_fancontrolmode` | sensor.mikes_office_ceiling_fan_fancontrolmode | sensor |
| `sensor.mikes_office_ceiling_fan_fanledleveltype` | sensor.mikes_office_ceiling_fan_fanledleveltype | sensor |
| `sensor.mikes_office_ceiling_fan_fantimermode` | sensor.mikes_office_ceiling_fan_fantimermode | sensor |
| `sensor.mikes_office_ceiling_fan_firmwareupdateinprogressindicator` | sensor.mikes_office_ceiling_fan_firmwareupdateinprogressindicator | sensor |
| `sensor.mikes_office_ceiling_fan_highlevelforfancontrolmode` | sensor.mikes_office_ceiling_fan_highlevelforfancontrolmode | sensor |
| `sensor.mikes_office_ceiling_fan_individual_led_effect` | Mikes Office Ceiling Fan Individual led effect | sensor |
| `sensor.mikes_office_ceiling_fan_internaltemperature` | Mikes Office Ceiling Fan Temperature | sensor |
| `sensor.mikes_office_ceiling_fan_invertswitch` | sensor.mikes_office_ceiling_fan_invertswitch | sensor |
| `sensor.mikes_office_ceiling_fan_last_seen` | sensor.mikes_office_ceiling_fan_last_seen | sensor |
| `sensor.mikes_office_ceiling_fan_led_effect` | Mikes Office Ceiling Fan Led effect | sensor |
| `sensor.mikes_office_ceiling_fan_ledcolorforfancontrolmode` | sensor.mikes_office_ceiling_fan_ledcolorforfancontrolmode | sensor |
| `sensor.mikes_office_ceiling_fan_ledcolorwhenoff` | sensor.mikes_office_ceiling_fan_ledcolorwhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_ledcolorwhenon` | sensor.mikes_office_ceiling_fan_ledcolorwhenon | sensor |
| `sensor.mikes_office_ceiling_fan_ledintensitywhenoff` | sensor.mikes_office_ceiling_fan_ledintensitywhenoff | sensor |
| `sensor.mikes_office_ceiling_fan_ledintensitywhenon` | sensor.mikes_office_ceiling_fan_ledintensitywhenon | sensor |
| `sensor.mikes_office_ceiling_fan_linkquality` | sensor.mikes_office_ceiling_fan_linkquality | sensor |
| `sensor.mikes_office_ceiling_fan_loadlevelindicatortimeout` | sensor.mikes_office_ceiling_fan_loadlevelindicatortimeout | sensor |
| `sensor.mikes_office_ceiling_fan_localprotection` | sensor.mikes_office_ceiling_fan_localprotection | sensor |
| `sensor.mikes_office_ceiling_fan_lowlevelforfancontrolmode` | sensor.mikes_office_ceiling_fan_lowlevelforfancontrolmode | sensor |
| `sensor.mikes_office_ceiling_fan_maximumlevel` | sensor.mikes_office_ceiling_fan_maximumlevel | sensor |
| `sensor.mikes_office_ceiling_fan_mediumlevelforfancontrolmode` | sensor.mikes_office_ceiling_fan_mediumlevelforfancontrolmode | sensor |
| `sensor.mikes_office_ceiling_fan_minimumlevel` | sensor.mikes_office_ceiling_fan_minimumlevel | sensor |
| `sensor.mikes_office_ceiling_fan_nonneutralauxlowgear` | sensor.mikes_office_ceiling_fan_nonneutralauxlowgear | sensor |
| `sensor.mikes_office_ceiling_fan_nonneutralauxmediumgear` | sensor.mikes_office_ceiling_fan_nonneutralauxmediumgear | sensor |
| `sensor.mikes_office_ceiling_fan_notificationcomplete` | Mikes Office Ceiling Fan NotificationComplete | sensor |
| `sensor.mikes_office_ceiling_fan_onoffledmode` | sensor.mikes_office_ceiling_fan_onoffledmode | sensor |
| `sensor.mikes_office_ceiling_fan_outputmode` | sensor.mikes_office_ceiling_fan_outputmode | sensor |
| `sensor.mikes_office_ceiling_fan_overheat` | Mikes Office Ceiling Fan Overheat | sensor |
| `sensor.mikes_office_ceiling_fan_powertype` | Mikes Office Ceiling Fan PowerType | sensor |
| `sensor.mikes_office_ceiling_fan_quickstarttime` | sensor.mikes_office_ceiling_fan_quickstarttime | sensor |
| `sensor.mikes_office_ceiling_fan_ramprateofftoonlocal` | sensor.mikes_office_ceiling_fan_ramprateofftoonlocal | sensor |
| `sensor.mikes_office_ceiling_fan_ramprateofftoonremote` | sensor.mikes_office_ceiling_fan_ramprateofftoonremote | sensor |
| `sensor.mikes_office_ceiling_fan_ramprateontoofflocal` | sensor.mikes_office_ceiling_fan_ramprateontoofflocal | sensor |
| `sensor.mikes_office_ceiling_fan_ramprateontooffremote` | sensor.mikes_office_ceiling_fan_ramprateontooffremote | sensor |
| `sensor.mikes_office_ceiling_fan_remoteprotection` | Mikes Office Ceiling Fan RemoteProtection | sensor |
| `sensor.mikes_office_ceiling_fan_singletapbehavior` | sensor.mikes_office_ceiling_fan_singletapbehavior | sensor |
| `sensor.mikes_office_ceiling_fan_smartbulbmode` | sensor.mikes_office_ceiling_fan_smartbulbmode | sensor |
| `sensor.mikes_office_ceiling_fan_stateafterpowerrestored` | sensor.mikes_office_ceiling_fan_stateafterpowerrestored | sensor |
| `sensor.mikes_office_ceiling_fan_switchtype` | sensor.mikes_office_ceiling_fan_switchtype | sensor |
| `sensor.mikes_office_ceiling_fan_update_state` | sensor.mikes_office_ceiling_fan_update_state | sensor |
| `sensor.mikes_office_desk_button_battery` | Mikes Office Desk Button Battery | sensor |
| `sensor.mikes_office_desk_button_temperature` | Mikes Office Desk Button Temperature | sensor |
| `sensor.mikes_office_grow_light_outlet_current` | TP-LINK_Power Strip_9041 Mikes Office Grow Light Outlet Current | sensor |
| `sensor.mikes_office_grow_light_outlet_current_consumption` | TP-LINK_Power Strip_9041 Mikes Office Grow Light Outlet Current consumption | sensor |
| `sensor.mikes_office_grow_light_outlet_today_s_consumption` | TP-LINK_Power Strip_9041 Mikes Office Grow Light Outlet Today's consumption | sensor |
| `sensor.mikes_office_grow_light_outlet_total_consumption` | TP-LINK_Power Strip_9041 Mikes Office Grow Light Outlet Total consumption | sensor |
| `sensor.mikes_office_grow_light_outlet_voltage` | TP-LINK_Power Strip_9041 Mikes Office Grow Light Outlet Voltage | sensor |
| `sensor.mikes_office_light_commands_dropped_rx` | sensor.mikes_office_light_commands_dropped_rx | sensor |
| `sensor.mikes_office_light_commands_dropped_tx` | sensor.mikes_office_light_commands_dropped_tx | sensor |
| `sensor.mikes_office_light_dimming_mode` | sensor.mikes_office_light_dimming_mode | sensor |
| `sensor.mikes_office_light_electric_consumption_kwh` | Mikes Office Light Electric Consumption [kWh] | sensor |
| `sensor.mikes_office_light_electric_consumption_w` | Mikes Office Light Electric Consumption [W] | sensor |
| `sensor.mikes_office_light_internal_temperature` | sensor.mikes_office_light_internal_temperature | sensor |
| `sensor.mikes_office_light_last_seen` | Mikes Office Light Last seen | sensor |
| `sensor.mikes_office_light_node_status` | Mikes Office Light Node status | sensor |
| `sensor.mikes_office_light_overheat_detected` | sensor.mikes_office_light_overheat_detected | sensor |
| `sensor.mikes_office_light_power_type` | sensor.mikes_office_light_power_type | sensor |
| `sensor.mikes_office_light_round_trip_time` | sensor.mikes_office_light_round_trip_time | sensor |
| `sensor.mikes_office_light_rssi` | sensor.mikes_office_light_rssi | sensor |
| `sensor.mikes_office_light_successful_commands_rx` | sensor.mikes_office_light_successful_commands_rx | sensor |
| `sensor.mikes_office_light_successful_commands_tx` | sensor.mikes_office_light_successful_commands_tx | sensor |
| `sensor.mikes_office_light_timed_out_responses` | sensor.mikes_office_light_timed_out_responses | sensor |
| `sensor.mikes_office_motion_nightlight_illuminance` | Mikes Office Motion Nightlight Illuminance | sensor |
| `sensor.mikes_office_motion_nightlight_illuminance_raw` | Mikes Office Motion Nightlight Illuminance raw | sensor |
| `sensor.mikes_office_motion_nightlight_last_seen` | Mikes Office Motion Nightlight Last seen | sensor |
| `sensor.mikes_office_motion_nightlight_linkquality` | Mikes Office Motion Nightlight Linkquality | sensor |
| `sensor.mikes_office_motion_nightlight_power_on_behavior` | sensor.mikes_office_motion_nightlight_power_on_behavior | sensor |
| `sensor.mikes_office_motion_nightlight_update_state` | Mikes Office Motion Nightlight Update state | sensor |
| `sensor.mikes_office_open_plug_1_current` | TP-LINK_Power Strip_9041 Mikes Office Open Plug 1 Current | sensor |
| `sensor.mikes_office_open_plug_1_current_consumption` | TP-LINK_Power Strip_9041 Mikes Office Open Plug 1 Current consumption | sensor |
| `sensor.mikes_office_open_plug_1_today_s_consumption` | TP-LINK_Power Strip_9041 Mikes Office Open Plug 1 Today's consumption | sensor |
| `sensor.mikes_office_open_plug_1_total_consumption` | TP-LINK_Power Strip_9041 Mikes Office Open Plug 1 Total consumption | sensor |
| `sensor.mikes_office_open_plug_1_voltage` | TP-LINK_Power Strip_9041 Mikes Office Open Plug 1 Voltage | sensor |
| `sensor.mikes_office_printer_outlet_current` | TP-LINK_Power Strip_9041 Mikes Office Printer Outlet Current | sensor |
| `sensor.mikes_office_printer_outlet_current_consumption` | TP-LINK_Power Strip_9041 Mikes Office Printer Outlet Current consumption | sensor |
| `sensor.mikes_office_printer_outlet_today_s_consumption` | TP-LINK_Power Strip_9041 Mikes Office Printer Outlet Today's consumption | sensor |
| `sensor.mikes_office_printer_outlet_total_consumption` | TP-LINK_Power Strip_9041 Mikes Office Printer Outlet Total consumption | sensor |
| `sensor.mikes_office_printer_outlet_voltage` | TP-LINK_Power Strip_9041 Mikes Office Printer Outlet Voltage | sensor |
| `sensor.office_of_mike_core_300s_air_quality` | Office of Mike Core 300s Air quality | sensor |
| `sensor.office_of_mike_core_300s_filter_lifetime` | Office of Mike Core 300s Filter lifetime | sensor |
| `sensor.office_of_mike_core_300s_pm2_5` | Office of Mike Core 300s PM2.5 | sensor |
| `sensor.office_of_mike_ecobee_sensor_temperature` | Office of Mike Ecobee Sensor Temperature | sensor |
| `sensor.office_of_mike_surge_protector_current` | Office of Mike Surge Protector Current | sensor |
| `sensor.office_of_mike_surge_protector_current_consumption` | Office of Mike Surge Protector Current consumption | sensor |
| `sensor.office_of_mike_surge_protector_on_since` | sensor.office_of_mike_surge_protector_on_since | sensor |
| `sensor.office_of_mike_surge_protector_signal_strength` | sensor.office_of_mike_surge_protector_signal_strength | sensor |
| `sensor.office_of_mike_surge_protector_this_month_s_consumption` | Office of Mike Surge Protector This month's consumption | sensor |
| `sensor.office_of_mike_surge_protector_today_s_consumption` | Office of Mike Surge Protector Today's consumption | sensor |
| `sensor.office_of_mike_surge_protector_total_consumption` | Office of Mike Surge Protector Total consumption | sensor |
| `sensor.office_of_mike_surge_protector_voltage` | Office of Mike Surge Protector Voltage | sensor |
| `sensor.tp_link_power_strip_9041_current` | TP-LINK_Power Strip_9041 Current | sensor |
| `sensor.tp_link_power_strip_9041_current_consumption` | TP-LINK_Power Strip_9041 Current consumption | sensor |
| `sensor.tp_link_power_strip_9041_mikes_office_airpurifier_outlet_on_since` | sensor.tp_link_power_strip_9041_mikes_office_airpurifier_outlet_on_since | sensor |
| `sensor.tp_link_power_strip_9041_mikes_office_airpurifier_outlet_this_month_s_consumption` | TP-LINK_Power Strip_9041 Mikes Office AirPurifier Outlet This month's consumption | sensor |
| `sensor.tp_link_power_strip_9041_mikes_office_amazon_echo_outlet_on_since` | sensor.tp_link_power_strip_9041_mikes_office_amazon_echo_outlet_on_since | sensor |
| `sensor.tp_link_power_strip_9041_mikes_office_amazon_echo_outlet_this_month_s_consumption` | TP-LINK_Power Strip_9041 Mikes Office Amazon Echo Outlet This month's consumption | sensor |
| `sensor.tp_link_power_strip_9041_mikes_office_bt_proxy_outlet_on_since` | sensor.tp_link_power_strip_9041_mikes_office_bt_proxy_outlet_on_since | sensor |
| `sensor.tp_link_power_strip_9041_mikes_office_bt_proxy_outlet_this_month_s_consumption` | TP-LINK_Power Strip_9041 Mikes Office BT Proxy Outlet This month's consumption | sensor |
| `sensor.tp_link_power_strip_9041_mikes_office_grow_light_outlet_on_since` | sensor.tp_link_power_strip_9041_mikes_office_grow_light_outlet_on_since | sensor |
| `sensor.tp_link_power_strip_9041_mikes_office_grow_light_outlet_this_month_s_consumption` | TP-LINK_Power Strip_9041 Mikes Office Grow Light Outlet This month's consumption | sensor |
| `sensor.tp_link_power_strip_9041_mikes_office_open_plug_1_on_since` | sensor.tp_link_power_strip_9041_mikes_office_open_plug_1_on_since | sensor |
| `sensor.tp_link_power_strip_9041_mikes_office_open_plug_1_this_month_s_consumption` | TP-LINK_Power Strip_9041 Mikes Office Open Plug 1 This month's consumption | sensor |
| `sensor.tp_link_power_strip_9041_mikes_office_printer_outlet_on_since` | sensor.tp_link_power_strip_9041_mikes_office_printer_outlet_on_since | sensor |
| `sensor.tp_link_power_strip_9041_mikes_office_printer_outlet_this_month_s_consumption` | TP-LINK_Power Strip_9041 Mikes Office Printer Outlet This month's consumption | sensor |
| `sensor.tp_link_power_strip_9041_on_since` | sensor.tp_link_power_strip_9041_on_since | sensor |
| `sensor.tp_link_power_strip_9041_signal_strength` | sensor.tp_link_power_strip_9041_signal_strength | sensor |
| `sensor.tp_link_power_strip_9041_this_month_s_consumption` | TP-LINK_Power Strip_9041 This month's consumption | sensor |
| `sensor.tp_link_power_strip_9041_today_s_consumption` | TP-LINK_Power Strip_9041 Today's consumption | sensor |
| `sensor.tp_link_power_strip_9041_total_consumption` | TP-LINK_Power Strip_9041 Total consumption | sensor |
| `sensor.tp_link_power_strip_9041_voltage` | TP-LINK_Power Strip_9041 Voltage | sensor |
| `switch.michael_s_2nd_alexa_app_for_pc_do_not_disturb_switch` | michael's 2nd Alexa App for PC Do not disturb | switch |
| `switch.michael_s_2nd_alexa_app_for_pc_repeat_switch` | michael's 2nd Alexa App for PC Repeat | switch |
| `switch.michael_s_2nd_alexa_app_for_pc_shuffle_switch` | michael's 2nd Alexa App for PC Shuffle | switch |
| `switch.michael_s_3rd_alexa_app_for_pc_do_not_disturb_switch` | michael's 3rd Alexa App for PC Do not disturb | switch |
| `switch.michael_s_3rd_alexa_app_for_pc_repeat_switch` | michael's 3rd Alexa App for PC Repeat | switch |
| `switch.michael_s_3rd_alexa_app_for_pc_shuffle_switch` | michael's 3rd Alexa App for PC Shuffle | switch |
| `switch.michael_s_alexa_app_for_pc_do_not_disturb_switch` | michael's Alexa App for PC Do not disturb | switch |
| `switch.michael_s_alexa_app_for_pc_repeat_switch` | michael's Alexa App for PC Repeat | switch |
| `switch.michael_s_alexa_app_for_pc_shuffle_switch` | michael's Alexa App for PC Shuffle | switch |
| `switch.office_of_mike_bl_monitor` | Office of Mike Surge Protector Office of Mike - BL Monitor | switch |
| `switch.office_of_mike_core_300s_child_lock` | Office of Mike Core 300s Child lock | switch |
| `switch.office_of_mike_core_300s_display` | Office of Mike Core 300s Display | switch |
| `switch.office_of_mike_laptop` | Office of Mike Surge Protector Office of Mike - Laptop | switch |
| `switch.office_of_mike_surge_protector` | Office of Mike Surge Protector | switch |
| `switch.office_of_mike_ul_monitor` | Office of Mike Surge Protector Office of Mike - UL Monitor | switch |
| `switch.office_of_mike_ur_monitor` | Office of Mike Surge Protector Office of Mike - UR Monitor | switch |
| `switch.office_of_mike_usb_hub` | Office of Mike Surge Protector Office of Mike - USB Hub | switch |
| `switch.office_of_mike_usb_hub_haas` | Office of Mike Surge Protector Office of Mike - USB Hub HAAS | switch |
| `switch.tp_link_power_strip_9041` | TP-LINK_Power Strip_9041 | switch |
| `switch.tp_link_power_strip_9041_led` | TP-LINK_Power Strip_9041 LED | switch |
| `switch.tp_link_power_strip_9041_mikes_office_airpurifier_outlet` | TP-LINK_Power Strip_9041 Mikes Office AirPurifier Outlet | switch |
| `switch.tp_link_power_strip_9041_mikes_office_amazon_echo_outlet` | TP-LINK_Power Strip_9041 Mikes Office Amazon Echo Outlet | switch |
| `switch.tp_link_power_strip_9041_mikes_office_bt_proxy_outlet` | TP-LINK_Power Strip_9041 Mikes Office BT Proxy Outlet | switch |
| `switch.tp_link_power_strip_9041_mikes_office_grow_light_outlet` | TP-LINK_Power Strip_9041 Mikes Office Grow Light Outlet | switch |
| `switch.tp_link_power_strip_9041_mikes_office_open_plug_1` | TP-LINK_Power Strip_9041 Mikes Office Open Plug 1 | switch |
| `switch.tp_link_power_strip_9041_mikes_office_printer_outlet` | TP-LINK_Power Strip_9041 Mikes Office Printer Outlet | switch |
| `switch.tp_link_power_strip_de41_led` | Office of Mike Surge Protector LED | switch |
| `update.mikes_office_ceiling_fan` | Mikes Office Ceiling Fan | update |
| `update.mikes_office_light_firmware` | Mikes Office Light Firmware | update |
| `update.mikes_office_motion_nightlight` | Mikes Office Motion Nightlight | update |
| `update.office_of_mike_core_300s_firmware` | Office of Mike Core 300s Firmware | update |
