# Network

> Read-only Home Assistant inventory captured 2026-08-24. No devices or configuration were changed.

- Floor classification: Basement
- Area: Network
- Devices: 20
- Entities: 533
- Inclusion rule: assigned to this Basement-floor area.

## Devices

| Device | Manufacturer | Model | Integration | Device ID |
|---|---|---|---|---|
| Basement Entertainment USW-Flex-Mini | Ubiquiti Networks | USMINI | unknown | `f6346c4a6edc8d57f2dc202dffb628bc` |
| Basement FireTV Stick | ASIX Electronics Corporation | — | unknown | `40bc819877059a3e54811c388941ad6c` |
| Basement Utility Room Camera | Reolink Innovation Limited | — | unknown | `4b7a54c3e413500d1947e28a0cfd822e` |
| FBI Van 25 | Ubiquiti Networks | UniFi WLAN | unifi | `825aa1108458a32a90c21fe2e89ee4fb` |
| FBI Van 25 IoT | Ubiquiti Networks | UniFi WLAN | unifi | `10e891869b26c23daf15aa04b32edbe6` |
| FBI VAN 25-Surveillance | Ubiquiti Networks | UniFi WLAN | unifi | `2b3f0021a3fcd7900ffe6272fe2ee5f0` |
| Garage UAP-AC-Pro | Ubiquiti Networks | U7PG2 | unknown | `3fcc0f688ad3218ef6d1a53ffad63553` |
| U6 Lite Basement Living Room | Ubiquiti Networks | UAL6 | unknown | `14e41815ea2a7068050a21fcb3242c87` |
| U6 Lite Garage | Ubiquiti Networks | UAL6 | unknown | `b2c8a1e9e453e856bcde662032edf70e` |
| U6-IW Living Room | Ubiquiti Networks | U6IW | unknown | `1b0b675ba38544d2b5a725c98546f9fe` |
| UniFi Dream Machine | Ubiquiti Networks | UDM-SE | upnp_serial_number | `caf90a5e6230f143b6dc283a7862511d` |
| UniFi Network | Ubiquiti Networks | UniFi Network | switch | `e99d92ad3bb4fbb777a4dc1d92e62866` |
| UniFi Network | Ubiquiti Networks | UniFi Network Application | unifi | `30b0e877caf99a4719c77586e02e7804` |
| US 8 | Ubiquiti Networks | USC8 | unknown | `3a142129ca4bac6f611fa07d5a7cbf3c` |
| US 8 PoE 150W | Ubiquiti Networks | US8P150 | unknown | `8e041d71f2f789bb22f405b783c5b878` |
| US XG 6 PoE | Ubiquiti Networks | US6XG150 | unknown | `045a4a8dbf463f6776a6fadfdc7f0d75` |
| USP PDU Pro | Ubiquiti Networks | USPPDUP | unknown | `64913363a5fdca84970ef64ea07e2939` |
| USW Aggregation | Ubiquiti Networks | USL8A | unknown | `100a7b0d8cf4ec836e541019684d0534` |
| USW Enterprise 8 PoE | Ubiquiti Networks | US68P | unknown | `4e91b77ec2f0996fd2762ff58f7f70b2` |
| USW Pro 24 PoE | Ubiquiti Networks | US24PRO | unknown | `149959dc30aec02cc17627ab83ef83fc` |

## Entities

| Entity ID | Friendly name | Domain |
|---|---|---|
| `binary_sensor.unifi_dream_machine_wan_status` | UniFi Dream Machine WAN status | binary_sensor |
| `button.basement_entertainment_usw_flex_mini_restart` | Basement Entertainment USW-Flex-Mini Restart | button |
| `button.basement_office_u6_iw_poe_out_data_power_cycle` | U6-IW Living Room PoE Out + Data power cycle | button |
| `button.basement_office_u6_iw_restart` | U6-IW Living Room Restart | button |
| `button.fbi_van_25_iot_regenerate_password` | button.fbi_van_25_iot_regenerate_password | button |
| `button.fbi_van_25_regenerate_password` | button.fbi_van_25_regenerate_password | button |
| `button.fbi_van_25_surveillance_regenerate_password` | button.fbi_van_25_surveillance_regenerate_password | button |
| `button.garage_uap_ac_pro_restart` | Garage UAP-AC-Pro Restart | button |
| `button.laundry_room_switch_port_8_power_cycle` | US 8 Port 8 power cycle | button |
| `button.laundry_room_switch_restart` | US 8 Restart | button |
| `button.master_bedroom_ap_restart` | U6 Lite Garage Restart | button |
| `button.upstairs_hallway_ap_restart` | U6 Lite Basement Living Room Restart | button |
| `button.us_8_poe_150w_port_5_power_cycle` | US 8 PoE 150W Port 5 Power Cycle | button |
| `button.us_8_poe_150w_port_6_power_cycle` | US 8 PoE 150W Port 6 Power Cycle | button |
| `button.us_8_poe_150w_port_7_power_cycle` | US 8 PoE 150W Port 7 Power Cycle | button |
| `button.us_8_poe_150w_port_8_power_cycle` | US 8 PoE 150W Port 8 Power Cycle | button |
| `button.us_8_poe_150w_pve1_cluster_power_cycle` | US 8 PoE 150W PVE1 - Cluster Power Cycle | button |
| `button.us_8_poe_150w_pve2_cluster_power_cycle` | US 8 PoE 150W PVE2 - Cluster Power Cycle | button |
| `button.us_8_poe_150w_pve3_cluster_power_cycle` | US 8 PoE 150W PVE3 - Cluster Power Cycle | button |
| `button.us_8_poe_150w_pve4_cluster_power_cycle` | US 8 PoE 150W PVE4 - Cluster Power Cycle | button |
| `button.us_8_poe_150w_restart` | US 8 PoE 150W Restart | button |
| `button.us_xg_6poe_port_1_power_cycle` | US XG 6 PoE Port 1 power cycle | button |
| `button.us_xg_6poe_port_2_power_cycle` | US XG 6 PoE Port 2 power cycle | button |
| `button.us_xg_6poe_port_3_power_cycle` | US XG 6 PoE Port 3 power cycle | button |
| `button.us_xg_6poe_port_4_power_cycle` | US XG 6 PoE Port 4 power cycle | button |
| `button.us_xg_6poe_restart` | US XG 6 PoE Restart | button |
| `button.usp_pdu_pro_restart` | USP PDU Pro Restart | button |
| `button.usw_aggregation_restart` | USW Aggregation Restart | button |
| `button.usw_enterprise_8_poe_port_1_power_cycle` | USW Enterprise 8 PoE Port 1 power cycle | button |
| `button.usw_enterprise_8_poe_port_2_power_cycle` | USW Enterprise 8 PoE Port 2 power cycle | button |
| `button.usw_enterprise_8_poe_port_3_power_cycle` | USW Enterprise 8 PoE Port 3 power cycle | button |
| `button.usw_enterprise_8_poe_port_4_power_cycle` | USW Enterprise 8 PoE Port 4 power cycle | button |
| `button.usw_enterprise_8_poe_port_5_power_cycle` | USW Enterprise 8 PoE Port 5 power cycle | button |
| `button.usw_enterprise_8_poe_port_6_power_cycle` | USW Enterprise 8 PoE Port 6 power cycle | button |
| `button.usw_enterprise_8_poe_port_7_power_cycle` | USW Enterprise 8 PoE Port 7 power cycle | button |
| `button.usw_enterprise_8_poe_port_8_power_cycle` | USW Enterprise 8 PoE Port 8 power cycle | button |
| `button.usw_enterprise_8_poe_restart` | USW Enterprise 8 PoE Restart | button |
| `button.usw_pro_24_poe_port_1_power_cycle` | USW Pro 24 PoE Port 1 power cycle | button |
| `button.usw_pro_24_poe_port_10_power_cycle` | USW Pro 24 PoE Port 10 power cycle | button |
| `button.usw_pro_24_poe_port_11_power_cycle` | USW Pro 24 PoE Port 11 power cycle | button |
| `button.usw_pro_24_poe_port_12_power_cycle` | USW Pro 24 PoE Port 12 power cycle | button |
| `button.usw_pro_24_poe_port_13_power_cycle` | USW Pro 24 PoE Port 13 power cycle | button |
| `button.usw_pro_24_poe_port_14_power_cycle` | USW Pro 24 PoE Port 14 power cycle | button |
| `button.usw_pro_24_poe_port_15_power_cycle` | USW Pro 24 PoE Port 15 power cycle | button |
| `button.usw_pro_24_poe_port_16_power_cycle` | USW Pro 24 PoE Port 16 power cycle | button |
| `button.usw_pro_24_poe_port_17_power_cycle` | USW Pro 24 PoE Port 17 power cycle | button |
| `button.usw_pro_24_poe_port_18_power_cycle` | USW Pro 24 PoE Port 18 power cycle | button |
| `button.usw_pro_24_poe_port_19_power_cycle` | USW Pro 24 PoE Port 19 power cycle | button |
| `button.usw_pro_24_poe_port_2_power_cycle` | USW Pro 24 PoE Port 2 power cycle | button |
| `button.usw_pro_24_poe_port_20_power_cycle` | USW Pro 24 PoE Port 20 power cycle | button |
| `button.usw_pro_24_poe_port_21_power_cycle` | USW Pro 24 PoE Port 21 power cycle | button |
| `button.usw_pro_24_poe_port_22_power_cycle` | USW Pro 24 PoE Port 22 power cycle | button |
| `button.usw_pro_24_poe_port_23_power_cycle` | USW Pro 24 PoE Port 23 power cycle | button |
| `button.usw_pro_24_poe_port_24_power_cycle` | USW Pro 24 PoE Port 24 power cycle | button |
| `button.usw_pro_24_poe_port_3_power_cycle` | USW Pro 24 PoE Port 3 power cycle | button |
| `button.usw_pro_24_poe_port_4_power_cycle` | USW Pro 24 PoE Port 4 power cycle | button |
| `button.usw_pro_24_poe_port_5_power_cycle` | USW Pro 24 PoE Port 5 power cycle | button |
| `button.usw_pro_24_poe_port_7_power_cycle` | USW Pro 24 PoE Port 7 power cycle | button |
| `button.usw_pro_24_poe_port_8_power_cycle` | USW Pro 24 PoE Port 8 power cycle | button |
| `button.usw_pro_24_poe_port_9_power_cycle` | USW Pro 24 PoE Port 9 power cycle | button |
| `button.usw_pro_24_poe_pve3_vm_power_cycle` | USW Pro 24 PoE Port 6 power cycle | button |
| `button.usw_pro_24_poe_restart` | USW Pro 24 PoE Restart | button |
| `device_tracker.basement_entertainment_usw_flex_mini` | Basement Entertainment USW-Flex-Mini Basement Entertainment USW-Flex-Mini | device_tracker |
| `device_tracker.basement_office_u6_iw` | U6-IW Living Room U6-IW Living Room | device_tracker |
| `device_tracker.garage_uap_ac_pro` | Garage UAP-AC-Pro Garage UAP-AC-Pro | device_tracker |
| `device_tracker.laundry_room_switch` | US 8 US 8 | device_tracker |
| `device_tracker.master_bedroom_ap` | U6 Lite Garage U6 Lite Garage | device_tracker |
| `device_tracker.unifi_default_20_7b_d2_ab_01_ca` | Basement FireTV Stick Basement FireTV Stick | device_tracker |
| `device_tracker.upstairs_hallway_ap` | U6 Lite Basement Living Room U6 Lite Basement Living Room | device_tracker |
| `device_tracker.us_8_poe_150w` | US 8 PoE 150W US 8 PoE 150W | device_tracker |
| `device_tracker.us_xg_6poe` | US XG 6 PoE US XG 6 PoE | device_tracker |
| `device_tracker.usp_pdu_pro` | USP PDU Pro USP PDU Pro | device_tracker |
| `device_tracker.usw_aggregation` | USW Aggregation USW Aggregation | device_tracker |
| `device_tracker.usw_enterprise_8_poe` | USW Enterprise 8 PoE USW Enterprise 8 PoE | device_tracker |
| `device_tracker.usw_pro_24_poe` | USW Pro 24 PoE USW Pro 24 PoE | device_tracker |
| `image.fbi_van_25_iot_qr_code` | image.fbi_van_25_iot_qr_code | image |
| `image.fbi_van_25_qr_code` | image.fbi_van_25_qr_code | image |
| `image.fbi_van_25_surveillance_qr_code` | image.fbi_van_25_surveillance_qr_code | image |
| `light.basement_entertainment_usw_flex_mini_led` | Basement Entertainment USW-Flex-Mini LED | light |
| `light.laundry_room_switch_led` | US 8 LED | light |
| `light.u6_iw_living_room_led` | U6-IW Living Room LED | light |
| `light.u6_lite_basement_living_room_led` | U6 Lite Basement Living Room LED | light |
| `light.u6_lite_garage_led` | U6 Lite Garage LED | light |
| `light.us_xg_6poe_led` | US XG 6 PoE LED | light |
| `sensor.basement_entertainment_usw_flex_mini_clients` | Basement Entertainment USW-Flex-Mini Clients | sensor |
| `sensor.basement_entertainment_usw_flex_mini_cpu_utilization` | Basement Entertainment USW-Flex-Mini CPU utilization | sensor |
| `sensor.basement_entertainment_usw_flex_mini_memory_utilization` | Basement Entertainment USW-Flex-Mini Memory utilization | sensor |
| `sensor.basement_entertainment_usw_flex_mini_port_1_link_speed` | sensor.basement_entertainment_usw_flex_mini_port_1_link_speed | sensor |
| `sensor.basement_entertainment_usw_flex_mini_port_2_link_speed` | sensor.basement_entertainment_usw_flex_mini_port_2_link_speed | sensor |
| `sensor.basement_entertainment_usw_flex_mini_port_3_link_speed` | sensor.basement_entertainment_usw_flex_mini_port_3_link_speed | sensor |
| `sensor.basement_entertainment_usw_flex_mini_port_4_link_speed` | sensor.basement_entertainment_usw_flex_mini_port_4_link_speed | sensor |
| `sensor.basement_entertainment_usw_flex_mini_state` | Basement Entertainment USW-Flex-Mini State | sensor |
| `sensor.basement_entertainment_usw_flex_mini_uplink_mac` | Basement Entertainment USW-Flex-Mini Uplink MAC | sensor |
| `sensor.basement_entertainment_usw_flex_mini_uptime` | Basement Entertainment USW-Flex-Mini Uptime | sensor |
| `sensor.basement_link_speed` | sensor.basement_link_speed | sensor |
| `sensor.basement_office_u6_iw_clients` | U6-IW Living Room Clients | sensor |
| `sensor.basement_office_u6_iw_cpu_utilization` | U6-IW Living Room CPU utilization | sensor |
| `sensor.basement_office_u6_iw_memory_utilization` | U6-IW Living Room Memory utilization | sensor |
| `sensor.basement_office_u6_iw_poe_out_data_poe_power` | sensor.basement_office_u6_iw_poe_out_data_poe_power | sensor |
| `sensor.basement_office_u6_iw_state` | U6-IW Living Room State | sensor |
| `sensor.basement_office_u6_iw_uplink_mac` | U6-IW Living Room Uplink MAC | sensor |
| `sensor.basement_office_u6_iw_uptime` | U6-IW Living Room Uptime | sensor |
| `sensor.fbi_van_25` | FBI Van 25 Clients | sensor |
| `sensor.fbi_van_25_iot` | FBI Van 25 IoT Clients | sensor |
| `sensor.fbi_van_25_surveillance` | FBI VAN 25-Surveillance Clients | sensor |
| `sensor.garage_uap_ac_pro_clients` | sensor.garage_uap_ac_pro_clients | sensor |
| `sensor.garage_uap_ac_pro_state` | Garage UAP-AC-Pro State | sensor |
| `sensor.garage_uap_ac_pro_uptime` | Garage UAP-AC-Pro Uptime | sensor |
| `sensor.laundry_room_switch_clients` | US 8 Clients | sensor |
| `sensor.laundry_room_switch_cpu_utilization` | US 8 CPU utilization | sensor |
| `sensor.laundry_room_switch_memory_utilization` | US 8 Memory utilization | sensor |
| `sensor.laundry_room_switch_port_8_poe_power` | US 8 Port 8 PoE power | sensor |
| `sensor.laundry_room_switch_state` | US 8 State | sensor |
| `sensor.laundry_room_switch_uplink_mac` | US 8 Uplink MAC | sensor |
| `sensor.laundry_room_switch_uptime` | US 8 Uptime | sensor |
| `sensor.link_speed_6` | sensor.link_speed_6 | sensor |
| `sensor.master_bedroom_ap_clients` | U6 Lite Garage Clients | sensor |
| `sensor.master_bedroom_ap_cpu_utilization` | U6 Lite Garage CPU utilization | sensor |
| `sensor.master_bedroom_ap_memory_utilization` | U6 Lite Garage Memory utilization | sensor |
| `sensor.master_bedroom_ap_state` | U6 Lite Garage State | sensor |
| `sensor.master_bedroom_ap_uplink_mac` | U6 Lite Garage Uplink MAC | sensor |
| `sensor.master_bedroom_ap_uptime` | U6 Lite Garage Uptime | sensor |
| `sensor.network_unifi_dream_machine_download_speed_no_rollover_handling` | sensor.network_unifi_dream_machine_download_speed_no_rollover_handling | sensor |
| `sensor.network_unifi_dream_machine_packet_download_speed_no_rollover_handling` | sensor.network_unifi_dream_machine_packet_download_speed_no_rollover_handling | sensor |
| `sensor.network_unifi_dream_machine_packet_upload_speed_no_rollover_handling` | sensor.network_unifi_dream_machine_packet_upload_speed_no_rollover_handling | sensor |
| `sensor.network_unifi_dream_machine_upload_speed_no_rollover_handling` | sensor.network_unifi_dream_machine_upload_speed_no_rollover_handling | sensor |
| `sensor.u6_iw_living_room_data_link_speed` | sensor.u6_iw_living_room_data_link_speed | sensor |
| `sensor.u6_iw_living_room_iot_link_speed` | sensor.u6_iw_living_room_iot_link_speed | sensor |
| `sensor.unifi_dream_machine_b_received` | sensor.unifi_dream_machine_b_received | sensor |
| `sensor.unifi_dream_machine_b_sent` | sensor.unifi_dream_machine_b_sent | sensor |
| `sensor.unifi_dream_machine_external_ip` | UniFi Dream Machine External IP | sensor |
| `sensor.unifi_dream_machine_kib_s_received` | UniFi Dream Machine Download speed | sensor |
| `sensor.unifi_dream_machine_kib_s_sent` | UniFi Dream Machine Upload speed | sensor |
| `sensor.unifi_dream_machine_number_of_port_mapping_entries_ipv4` | sensor.unifi_dream_machine_number_of_port_mapping_entries_ipv4 | sensor |
| `sensor.unifi_dream_machine_packets_received` | UniFi Dream Machine Packets received | sensor |
| `sensor.unifi_dream_machine_packets_s_received` | sensor.unifi_dream_machine_packets_s_received | sensor |
| `sensor.unifi_dream_machine_packets_s_sent` | sensor.unifi_dream_machine_packets_s_sent | sensor |
| `sensor.unifi_dream_machine_packets_sent` | UniFi Dream Machine Packets sent | sensor |
| `sensor.unifi_dream_machine_uptime` | sensor.unifi_dream_machine_uptime | sensor |
| `sensor.unifi_dream_machine_wan_status` | sensor.unifi_dream_machine_wan_status | sensor |
| `sensor.upstairs_hallway_ap_clients` | U6 Lite Basement Living Room Clients | sensor |
| `sensor.upstairs_hallway_ap_cpu_utilization` | U6 Lite Basement Living Room CPU utilization | sensor |
| `sensor.upstairs_hallway_ap_memory_utilization` | U6 Lite Basement Living Room Memory utilization | sensor |
| `sensor.upstairs_hallway_ap_state` | U6 Lite Basement Living Room State | sensor |
| `sensor.upstairs_hallway_ap_uplink_mac` | U6 Lite Basement Living Room Uplink MAC | sensor |
| `sensor.upstairs_hallway_ap_uptime` | U6 Lite Basement Living Room Uptime | sensor |
| `sensor.us_8_poe_150w_clients` | US 8 PoE 150W Clients | sensor |
| `sensor.us_8_poe_150w_cpu_utilization` | US 8 PoE 150W CPU utilization | sensor |
| `sensor.us_8_poe_150w_memory_utilization` | US 8 PoE 150W Memory utilization | sensor |
| `sensor.us_8_poe_150w_port_5_poe_power` | sensor.us_8_poe_150w_port_5_poe_power | sensor |
| `sensor.us_8_poe_150w_port_6_poe_power` | sensor.us_8_poe_150w_port_6_poe_power | sensor |
| `sensor.us_8_poe_150w_port_7_poe_power` | sensor.us_8_poe_150w_port_7_poe_power | sensor |
| `sensor.us_8_poe_150w_port_8_poe_power` | sensor.us_8_poe_150w_port_8_poe_power | sensor |
| `sensor.us_8_poe_150w_pve1_cluster_poe_power` | sensor.us_8_poe_150w_pve1_cluster_poe_power | sensor |
| `sensor.us_8_poe_150w_pve2_cluster_poe_power` | sensor.us_8_poe_150w_pve2_cluster_poe_power | sensor |
| `sensor.us_8_poe_150w_pve3_cluster_poe_power` | sensor.us_8_poe_150w_pve3_cluster_poe_power | sensor |
| `sensor.us_8_poe_150w_pve4_cluster_poe_power` | sensor.us_8_poe_150w_pve4_cluster_poe_power | sensor |
| `sensor.us_8_poe_150w_state` | US 8 PoE 150W State | sensor |
| `sensor.us_8_poe_150w_uplink_mac` | US 8 PoE 150W Uplink MAC | sensor |
| `sensor.us_8_poe_150w_uptime` | US 8 PoE 150W Uptime | sensor |
| `sensor.us_8_port_1_link_speed` | sensor.us_8_port_1_link_speed | sensor |
| `sensor.us_8_port_2_link_speed` | sensor.us_8_port_2_link_speed | sensor |
| `sensor.us_8_port_3_link_speed` | sensor.us_8_port_3_link_speed | sensor |
| `sensor.us_8_port_4_link_speed` | sensor.us_8_port_4_link_speed | sensor |
| `sensor.us_8_port_5_link_speed` | sensor.us_8_port_5_link_speed | sensor |
| `sensor.us_8_port_6_link_speed` | sensor.us_8_port_6_link_speed | sensor |
| `sensor.us_8_port_7_link_speed` | sensor.us_8_port_7_link_speed | sensor |
| `sensor.us_8_port_8_link_speed` | sensor.us_8_port_8_link_speed | sensor |
| `sensor.us_xg_6_poe_port_1_link_speed` | sensor.us_xg_6_poe_port_1_link_speed | sensor |
| `sensor.us_xg_6_poe_port_2_link_speed` | sensor.us_xg_6_poe_port_2_link_speed | sensor |
| `sensor.us_xg_6_poe_port_3_link_speed` | sensor.us_xg_6_poe_port_3_link_speed | sensor |
| `sensor.us_xg_6_poe_sfp_1_link_speed` | sensor.us_xg_6_poe_sfp_1_link_speed | sensor |
| `sensor.us_xg_6_poe_sfp_2_link_speed` | sensor.us_xg_6_poe_sfp_2_link_speed | sensor |
| `sensor.us_xg_6poe_clients` | US XG 6 PoE Clients | sensor |
| `sensor.us_xg_6poe_cpu_utilization` | US XG 6 PoE CPU utilization | sensor |
| `sensor.us_xg_6poe_memory_utilization` | US XG 6 PoE Memory utilization | sensor |
| `sensor.us_xg_6poe_port_1_poe_power` | sensor.us_xg_6poe_port_1_poe_power | sensor |
| `sensor.us_xg_6poe_port_2_poe_power` | sensor.us_xg_6poe_port_2_poe_power | sensor |
| `sensor.us_xg_6poe_port_3_poe_power` | sensor.us_xg_6poe_port_3_poe_power | sensor |
| `sensor.us_xg_6poe_port_4_poe_power` | sensor.us_xg_6poe_port_4_poe_power | sensor |
| `sensor.us_xg_6poe_state` | US XG 6 PoE State | sensor |
| `sensor.us_xg_6poe_temperature` | US XG 6 PoE Temperature | sensor |
| `sensor.us_xg_6poe_uplink_mac` | US XG 6 PoE Uplink MAC | sensor |
| `sensor.us_xg_6poe_uptime` | US XG 6 PoE Uptime | sensor |
| `sensor.usp_pdu_pro_ac_power_budget` | USP PDU Pro AC power budget | sensor |
| `sensor.usp_pdu_pro_ac_power_consumption` | USP PDU Pro AC power consumption | sensor |
| `sensor.usp_pdu_pro_clients` | USP PDU Pro Clients | sensor |
| `sensor.usp_pdu_pro_cpu_utilization` | USP PDU Pro CPU utilization | sensor |
| `sensor.usp_pdu_pro_google_fiber_plug_outlet_power` | USP PDU Pro Outlet 20 outlet power | sensor |
| `sensor.usp_pdu_pro_memory_utilization` | USP PDU Pro Memory utilization | sensor |
| `sensor.usp_pdu_pro_port_1_link_speed` | sensor.usp_pdu_pro_port_1_link_speed | sensor |
| `sensor.usp_pdu_pro_pve_usb_hub_outlet_power` | USP PDU Pro outlet power | sensor |
| `sensor.usp_pdu_pro_pve1_plug_outlet_power` | USP PDU Pro Outlet 9 outlet power | sensor |
| `sensor.usp_pdu_pro_pve2_plug_outlet_power` | USP PDU Pro USW Pro 24 PoE outlet power | sensor |
| `sensor.usp_pdu_pro_pve3_plug_outlet_power` | USP PDU Pro Internet outlet power | sensor |
| `sensor.usp_pdu_pro_pve4_plug_outlet_power` | USP PDU Pro Outlet 15 outlet power | sensor |
| `sensor.usp_pdu_pro_reolink_plug_outlet_power` | USP PDU Pro US XG 6 PoE outlet power | sensor |
| `sensor.usp_pdu_pro_server_rack_kvm_plug_outlet_power` | USP PDU Pro Outlet 19 outlet power | sensor |
| `sensor.usp_pdu_pro_state` | USP PDU Pro State | sensor |
| `sensor.usp_pdu_pro_synology_ds1522_plug_outlet_power` | USP PDU Pro Outlet 17 outlet power | sensor |
| `sensor.usp_pdu_pro_synology_ds416j_plug_outlet_power` | USP PDU Pro random outlet power | sensor |
| `sensor.usp_pdu_pro_udm_pro_se_plug_outlet_power` | USP PDU Pro USW Enterprise 8 PoE outlet power | sensor |
| `sensor.usp_pdu_pro_uplink_mac` | USP PDU Pro Uplink MAC | sensor |
| `sensor.usp_pdu_pro_uptime` | USP PDU Pro Uptime | sensor |
| `sensor.usp_pdu_pro_us_8_poe_150w_plug_outlet_power` | USP PDU Pro USW Pro XG 10 PoE outlet power | sensor |
| `sensor.usp_pdu_pro_us_xg_6poe_plug_outlet_power` | USP PDU Pro Outlet 14 outlet power | sensor |
| `sensor.usp_pdu_pro_usw_aggregation_plug_outlet_power` | USP PDU Pro Outlet 18 outlet power | sensor |
| `sensor.usp_pdu_pro_usw_enterprise_8_poe_plug_outlet_power` | USP PDU Pro USW Pro Aggregation outlet power | sensor |
| `sensor.usp_pdu_pro_usw_pro_24_poe_plug_outlet_power` | USP PDU Pro Outlet 13 outlet power | sensor |
| `sensor.usw_aggregation_clients` | USW Aggregation Clients | sensor |
| `sensor.usw_aggregation_cpu_utilization` | USW Aggregation CPU utilization | sensor |
| `sensor.usw_aggregation_memory_utilization` | USW Aggregation Memory utilization | sensor |
| `sensor.usw_aggregation_state` | USW Aggregation State | sensor |
| `sensor.usw_aggregation_uplink_mac` | USW Aggregation Uplink MAC | sensor |
| `sensor.usw_aggregation_uptime` | USW Aggregation Uptime | sensor |
| `sensor.usw_enterprise_8_poe_clients` | USW Enterprise 8 PoE Clients | sensor |
| `sensor.usw_enterprise_8_poe_cpu_utilization` | USW Enterprise 8 PoE CPU utilization | sensor |
| `sensor.usw_enterprise_8_poe_memory_utilization` | USW Enterprise 8 PoE Memory utilization | sensor |
| `sensor.usw_enterprise_8_poe_port_1_poe_power` | sensor.usw_enterprise_8_poe_port_1_poe_power | sensor |
| `sensor.usw_enterprise_8_poe_port_2_poe_power` | sensor.usw_enterprise_8_poe_port_2_poe_power | sensor |
| `sensor.usw_enterprise_8_poe_port_3_poe_power` | sensor.usw_enterprise_8_poe_port_3_poe_power | sensor |
| `sensor.usw_enterprise_8_poe_port_4_poe_power` | sensor.usw_enterprise_8_poe_port_4_poe_power | sensor |
| `sensor.usw_enterprise_8_poe_port_5_poe_power` | sensor.usw_enterprise_8_poe_port_5_poe_power | sensor |
| `sensor.usw_enterprise_8_poe_port_6_poe_power` | sensor.usw_enterprise_8_poe_port_6_poe_power | sensor |
| `sensor.usw_enterprise_8_poe_port_7_poe_power` | sensor.usw_enterprise_8_poe_port_7_poe_power | sensor |
| `sensor.usw_enterprise_8_poe_port_8_poe_power` | sensor.usw_enterprise_8_poe_port_8_poe_power | sensor |
| `sensor.usw_enterprise_8_poe_sfp_1_link_speed` | sensor.usw_enterprise_8_poe_sfp_1_link_speed | sensor |
| `sensor.usw_enterprise_8_poe_sfp_2_link_speed` | sensor.usw_enterprise_8_poe_sfp_2_link_speed | sensor |
| `sensor.usw_enterprise_8_poe_state` | USW Enterprise 8 PoE State | sensor |
| `sensor.usw_enterprise_8_poe_temperature` | USW Enterprise 8 PoE Temperature | sensor |
| `sensor.usw_enterprise_8_poe_uplink_mac` | USW Enterprise 8 PoE Uplink MAC | sensor |
| `sensor.usw_enterprise_8_poe_uptime` | USW Enterprise 8 PoE Uptime | sensor |
| `sensor.usw_pro_24_poe_clients` | USW Pro 24 PoE Clients | sensor |
| `sensor.usw_pro_24_poe_cpu_utilization` | USW Pro 24 PoE CPU utilization | sensor |
| `sensor.usw_pro_24_poe_memory_utilization` | USW Pro 24 PoE Memory utilization | sensor |
| `sensor.usw_pro_24_poe_port_1_link_speed` | sensor.usw_pro_24_poe_port_1_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_1_poe_power` | sensor.usw_pro_24_poe_port_1_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_10_link_speed` | sensor.usw_pro_24_poe_port_10_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_10_poe_power` | sensor.usw_pro_24_poe_port_10_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_11_poe_power` | sensor.usw_pro_24_poe_port_11_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_12_link_speed` | sensor.usw_pro_24_poe_port_12_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_12_poe_power` | sensor.usw_pro_24_poe_port_12_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_13_poe_power` | sensor.usw_pro_24_poe_port_13_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_14_link_speed` | sensor.usw_pro_24_poe_port_14_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_14_poe_power` | sensor.usw_pro_24_poe_port_14_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_15_link_speed` | sensor.usw_pro_24_poe_port_15_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_15_poe_power` | sensor.usw_pro_24_poe_port_15_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_16_poe_power` | sensor.usw_pro_24_poe_port_16_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_17_poe_power` | sensor.usw_pro_24_poe_port_17_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_18_link_speed` | sensor.usw_pro_24_poe_port_18_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_18_poe_power` | sensor.usw_pro_24_poe_port_18_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_19_link_speed` | sensor.usw_pro_24_poe_port_19_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_19_poe_power` | sensor.usw_pro_24_poe_port_19_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_2_link_speed` | sensor.usw_pro_24_poe_port_2_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_2_poe_power` | sensor.usw_pro_24_poe_port_2_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_20_link_speed` | sensor.usw_pro_24_poe_port_20_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_20_poe_power` | sensor.usw_pro_24_poe_port_20_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_21_poe_power` | sensor.usw_pro_24_poe_port_21_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_22_link_speed` | sensor.usw_pro_24_poe_port_22_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_22_poe_power` | sensor.usw_pro_24_poe_port_22_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_23_link_speed` | sensor.usw_pro_24_poe_port_23_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_23_poe_power` | sensor.usw_pro_24_poe_port_23_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_24_link_speed` | sensor.usw_pro_24_poe_port_24_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_24_poe_power` | sensor.usw_pro_24_poe_port_24_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_3_link_speed` | sensor.usw_pro_24_poe_port_3_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_3_poe_power` | sensor.usw_pro_24_poe_port_3_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_4_link_speed` | sensor.usw_pro_24_poe_port_4_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_4_poe_power` | sensor.usw_pro_24_poe_port_4_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_5_link_speed` | sensor.usw_pro_24_poe_port_5_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_5_poe_power` | sensor.usw_pro_24_poe_port_5_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_6_link_speed` | sensor.usw_pro_24_poe_port_6_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_7_link_speed` | sensor.usw_pro_24_poe_port_7_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_7_poe_power` | sensor.usw_pro_24_poe_port_7_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_8_link_speed` | sensor.usw_pro_24_poe_port_8_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_8_poe_power` | sensor.usw_pro_24_poe_port_8_poe_power | sensor |
| `sensor.usw_pro_24_poe_port_9_link_speed` | sensor.usw_pro_24_poe_port_9_link_speed | sensor |
| `sensor.usw_pro_24_poe_port_9_poe_power` | sensor.usw_pro_24_poe_port_9_poe_power | sensor |
| `sensor.usw_pro_24_poe_pve3_vm_poe_power` | sensor.usw_pro_24_poe_pve3_vm_poe_power | sensor |
| `sensor.usw_pro_24_poe_sfp_1_link_speed` | sensor.usw_pro_24_poe_sfp_1_link_speed | sensor |
| `sensor.usw_pro_24_poe_sfp_2_link_speed` | sensor.usw_pro_24_poe_sfp_2_link_speed | sensor |
| `sensor.usw_pro_24_poe_state` | USW Pro 24 PoE State | sensor |
| `sensor.usw_pro_24_poe_temperature` | USW Pro 24 PoE Temperature | sensor |
| `sensor.usw_pro_24_poe_uplink_mac` | USW Pro 24 PoE Uplink MAC | sensor |
| `sensor.usw_pro_24_poe_uptime` | USW Pro 24 PoE Uptime | sensor |
| `switch.basement_entertainment_usw_flex_mini_port_1` | switch.basement_entertainment_usw_flex_mini_port_1 | switch |
| `switch.basement_entertainment_usw_flex_mini_port_2` | switch.basement_entertainment_usw_flex_mini_port_2 | switch |
| `switch.basement_entertainment_usw_flex_mini_port_3` | switch.basement_entertainment_usw_flex_mini_port_3 | switch |
| `switch.basement_entertainment_usw_flex_mini_port_4` | switch.basement_entertainment_usw_flex_mini_port_4 | switch |
| `switch.basement_entertainment_usw_flex_mini_port_5` | switch.basement_entertainment_usw_flex_mini_port_5 | switch |
| `switch.basement_office_u6_iw_cerner_laptop` | switch.basement_office_u6_iw_cerner_laptop | switch |
| `switch.basement_office_u6_iw_data` | switch.basement_office_u6_iw_data | switch |
| `switch.basement_office_u6_iw_data_2` | switch.basement_office_u6_iw_data_2 | switch |
| `switch.basement_office_u6_iw_homelab` | switch.basement_office_u6_iw_homelab | switch |
| `switch.basement_office_u6_iw_poe_out_data` | switch.basement_office_u6_iw_poe_out_data | switch |
| `switch.basement_office_u6_iw_poe_out_data_poe` | switch.basement_office_u6_iw_poe_out_data_poe | switch |
| `switch.fbi_van_25` | FBI Van 25 Enabled | switch |
| `switch.fbi_van_25_iot` | FBI Van 25 IoT Enabled | switch |
| `switch.fbi_van_25_surveillance` | FBI VAN 25-Surveillance Enabled | switch |
| `switch.garage_uap_ac_pro_port_1` | switch.garage_uap_ac_pro_port_1 | switch |
| `switch.garage_uap_ac_pro_port_2` | switch.garage_uap_ac_pro_port_2 | switch |
| `switch.laundry_room_switch_port_1` | switch.laundry_room_switch_port_1 | switch |
| `switch.laundry_room_switch_port_2` | switch.laundry_room_switch_port_2 | switch |
| `switch.laundry_room_switch_port_3` | switch.laundry_room_switch_port_3 | switch |
| `switch.laundry_room_switch_port_4` | switch.laundry_room_switch_port_4 | switch |
| `switch.laundry_room_switch_port_5` | switch.laundry_room_switch_port_5 | switch |
| `switch.laundry_room_switch_port_6` | switch.laundry_room_switch_port_6 | switch |
| `switch.laundry_room_switch_port_7` | switch.laundry_room_switch_port_7 | switch |
| `switch.laundry_room_switch_port_8` | switch.laundry_room_switch_port_8 | switch |
| `switch.laundry_room_switch_port_8_poe` | switch.laundry_room_switch_port_8_poe | switch |
| `switch.network_unifi_network_allow_admin_internal_to_all_homelab` | UniFi Network Allow Admin Internal to All Homelab | switch |
| `switch.network_unifi_network_allow_admins_to_homelab_pve` | UniFi Network Allow Admins to HomeLab PVE | switch |
| `switch.unifi_network_allow_admin_devices_to_all` | UniFi Network Allow Admin Devices to All Internal | switch |
| `switch.unifi_network_allow_admin_devices_to_synology` | UniFi Network Allow Admin Devices to Synology | switch |
| `switch.unifi_network_allow_admins_to_all_devices` | UniFi Network Allow Admins to All IOT | switch |
| `switch.unifi_network_allow_all_homelab_to_web_services` | UniFi Network Allow ALL HomeLab to Web Services | switch |
| `switch.unifi_network_allow_all_management` | UniFi Network Allow All Management | switch |
| `switch.unifi_network_allow_all_ntp_requests` | UniFi Network Allow All NTP Requests | switch |
| `switch.unifi_network_allow_all_ntp_requests_2` | UniFi Network Allow All NTP Requests | switch |
| `switch.unifi_network_allow_ansible_ssh_access` | UniFi Network Allow Ansible SSH Access | switch |
| `switch.unifi_network_allow_ansible_to_local_ips` | UniFi Network Allow Ansible to Local IPs | switch |
| `switch.unifi_network_allow_autobot_portainer_access_to_devices` | UniFi Network Allow Autobot Portainer Access to Devices | switch |
| `switch.unifi_network_allow_autobot_to_graylog_portainer` | UniFi Network Allow Autobot to Graylog Portainer | switch |
| `switch.unifi_network_allow_autobot_to_traefik_proxies` | UniFi Network Allow Autobot to Traefik Proxies | switch |
| `switch.unifi_network_allow_bender_to_homeassistant` | UniFi Network Allow Bender to Homeassistant | switch |
| `switch.unifi_network_allow_bender_to_homelab` | UniFi Network Allow Bender to HomeLab | switch |
| `switch.unifi_network_allow_bender_to_marvin_rdp` | UniFi Network Allow Bender to Marvin RDP | switch |
| `switch.unifi_network_allow_dns_to_pihole` | UniFi Network Allow DNS to PIHole | switch |
| `switch.unifi_network_allow_established_and_related` | UniFi Network Allow Established and Related | switch |
| `switch.unifi_network_allow_external_proxy_to_pi_hole_web` | UniFi Network Allow External-Proxy to Pi-Hole Web | switch |
| `switch.unifi_network_allow_external_proxy_to_prometheus_web_port` | UniFi Network Allow External-Proxy to Prometheus Web Port | switch |
| `switch.unifi_network_allow_gitea_to_authentik` | UniFi Network Allow Gitea to Authentik | switch |
| `switch.unifi_network_allow_grafana_stack_to_influxdb_lxc` | UniFi Network Allow grafana-stack to influxdb_lxc | switch |
| `switch.unifi_network_allow_home_admin_to_external_web` | UniFi Network Allow Home Admin to External Web | switch |
| `switch.unifi_network_allow_home_assistant_to_not` | UniFi Network Allow Home Assistant to NOT | switch |
| `switch.unifi_network_allow_home_poxy_to_authentik_https` | UniFi Network Allow Home Poxy to Authentik HTTPS | switch |
| `switch.unifi_network_allow_home_proxy_to_external_ingress_web_traffic` | UniFi Network Allow Home-Proxy to External Ingress Web Traffic | switch |
| `switch.unifi_network_allow_home_proxy_to_megatron` | UniFi Network Allow Home Proxy to Megatron | switch |
| `switch.unifi_network_allow_home_proxy_to_megatron_on_arr_ports` | UniFi Network Allow Home Proxy to Megatron on ARR Ports | switch |
| `switch.unifi_network_allow_home_to_home_assistant` | UniFi Network Allow Home to Home Assistant | switch |
| `switch.unifi_network_allow_home_to_surveillance` | UniFi Network Allow Home to Surveillance | switch |
| `switch.unifi_network_allow_home_to_web_services` | UniFi Network Allow Home to Web Services | switch |
| `switch.unifi_network_allow_homeassistant_integration_to_synology` | UniFi Network Allow Homeassistant Integration to Synology | switch |
| `switch.unifi_network_allow_homeassistant_iot_to_reolink_nvr` | UniFi Network Allow HomeAssistant IOT to Reolink NVR | switch |
| `switch.unifi_network_allow_homeassistant_to_enphase_envoy` | UniFi Network Allow HomeAssistant to Enphase Envoy | switch |
| `switch.unifi_network_allow_homeassistant_to_gitea` | UniFi Network Allow HomeAssistant to Gitea | switch |
| `switch.unifi_network_allow_homeassistant_to_homelab_synology` | UniFi Network Allow HomeAssistant to Homelab Synology | switch |
| `switch.unifi_network_allow_homelab_proxy_synology` | UniFi Network Allow Homelab Proxy Synology | switch |
| `switch.unifi_network_allow_homelab_proxy_to_home_proxy_22` | UniFi Network Allow Homelab-Proxy to Home-Proxy 22 | switch |
| `switch.unifi_network_allow_homelab_proxy_to_homelab_portainer_agents` | UniFi Network Allow HomeLab Proxy to Homelab Portainer Agents | switch |
| `switch.unifi_network_allow_homelab_proxy_to_homeproxy_authentik` | UniFi Network Allow HomeLab Proxy to HomeProxy Authentik | switch |
| `switch.unifi_network_allow_homelab_proxy_to_iot_portainer` | UniFi Network Allow Homelab Proxy to IOT Portainer | switch |
| `switch.unifi_network_allow_homelab_proxy_to_proxmox_hypervisors` | UniFi Network Allow Homelab Proxy to Proxmox Hypervisors | switch |
| `switch.unifi_network_allow_homelab_proxy_to_surveillance_portainer` | UniFi Network Allow Homelab Proxy to Surveillance Portainer | switch |
| `switch.unifi_network_allow_homelab_smb_and_cifs_to_nas` | UniFi Network Allow HomeLab SMB and CIFS to NAS | switch |
| `switch.unifi_network_allow_homelab_to_gitea` | UniFi Network Allow HomeLab to Gitea | switch |
| `switch.unifi_network_allow_homelab_to_pihole` | UniFi Network Allow HomeLab to PiHole | switch |
| `switch.unifi_network_allow_homelab_to_ping_synology` | UniFi Network Allow HomeLab to Ping Synology | switch |
| `switch.unifi_network_allow_homepage_to_piholes` | UniFi Network Allow Homepage to PiHoles | switch |
| `switch.unifi_network_allow_http_s_from_cloudflare_over_ipv4` | UniFi Network Allow HTTP(S) from Cloudflare over IPv4 | switch |
| `switch.unifi_network_allow_ingress_proxy_to_home_proxy` | UniFi Network Allow ingress proxy to home-proxy | switch |
| `switch.unifi_network_allow_internal_devices_to_homeassistant` | UniFi Network Allow Internal Devices to HomeAssistant | switch |
| `switch.unifi_network_allow_internal_gateway_to_mgmt_gateway` | UniFi Network Allow Internal Gateway to Mgmt Gateway | switch |
| `switch.unifi_network_allow_internal_local_to_gitea_repos` | UniFi Network Allow Internal Local to Gitea Repos | switch |
| `switch.unifi_network_allow_iot_to_dns` | UniFi Network Allow IOT to DNS | switch |
| `switch.unifi_network_allow_management_to_internal_pihole` | UniFi Network Allow Management to Internal PiHole | switch |
| `switch.unifi_network_allow_marvin_to_all_iot` | UniFi Network Allow Marvin to All IOT | switch |
| `switch.unifi_network_allow_marvin_to_homelab` | UniFi Network Allow Marvin to HomeLab | switch |
| `switch.unifi_network_allow_marvin_to_internal` | UniFi Network Allow Marvin to Internal | switch |
| `switch.unifi_network_allow_marvin_to_web_services` | UniFi Network Allow Marvin to Web Services | switch |
| `switch.unifi_network_allow_monitoring_to_gitea_https` | UniFi Network Allow Monitoring to Gitea HTTPS | switch |
| `switch.unifi_network_allow_multicast_to_iot` | UniFi Network Allow Multicast to IOT | switch |
| `switch.unifi_network_allow_not_to_mqtt` | UniFi Network Allow NOT to MQTT | switch |
| `switch.unifi_network_allow_optimus_prime_to_nas` | UniFi Network Allow Optimus Prime to NAS | switch |
| `switch.unifi_network_allow_optimus_prime_to_synology_nfs` | UniFi Network Allow Optimus Prime to Synology NFS | switch |
| `switch.unifi_network_allow_paperless_ngx_to_synology` | UniFi Network Allow Paperless-NGX to Synology | switch |
| `switch.unifi_network_allow_plex_to_plex` | UniFi Network Allow Plex to Plex | switch |
| `switch.unifi_network_allow_plex_to_synology_nfs` | UniFi Network Allow Plex to Synology NFS | switch |
| `switch.unifi_network_allow_surveillance_to_internal_pihole` | UniFi Network Allow Surveillance to Internal PiHole | switch |
| `switch.unifi_network_allow_trash_stack_to_plex` | UniFi Network Allow Trash Stack to Plex | switch |
| `switch.unifi_network_allow_trusted_mgmt_to_untrusted_home` | UniFi Network Allow Trusted MGMT to Untrusted Home | switch |
| `switch.unifi_network_allow_tvs_to_plex` | UniFi Network Allow TVs to Plex | switch |
| `switch.unifi_network_allow_web_services_to_internal_pihole_dns` | UniFi Network Allow Web Services to Internal PiHole DNS | switch |
| `switch.unifi_network_amazon_amazon_tcp` | UniFi Network Amazon > Amazon TCP | switch |
| `switch.unifi_network_amazon_amazon_udp` | UniFi Network Amazon> Amazon UDP | switch |
| `switch.unifi_network_ansible_to_homelab_nodes` | UniFi Network Ansible to Homelab Nodes | switch |
| `switch.unifi_network_ansible_to_internal_nodes` | UniFi Network Ansible to Internal Nodes | switch |
| `switch.unifi_network_ansible_to_iot_nodes` | UniFi Network Ansible to IOT Nodes | switch |
| `switch.unifi_network_ansible_to_iot_nodes_2` | UniFi Network Ansible to IOT Nodes | switch |
| `switch.unifi_network_ansible_to_surveillance_nodes` | UniFi Network Ansible to Surveillance Nodes | switch |
| `switch.unifi_network_becky_s_rule` | UniFi Network Becky's Rule | switch |
| `switch.unifi_network_block_http_s_from_internet_over_ipv4` | UniFi Network Block HTTP(S) from Internet over IPv4 | switch |
| `switch.unifi_network_block_inter_vlan_traffic` | UniFi Network Block inter-VLAN traffic | switch |
| `switch.unifi_network_block_inter_vlan_traffic_2` | UniFi Network Block inter-VLAN traffic | switch |
| `switch.unifi_network_block_traffic_not_from_cloudflare` | UniFi Network Block Traffic Not From CloudFlare | switch |
| `switch.unifi_network_cmp_to_mgmt_rdp` | UniFi Network CMP to MGMT RDP | switch |
| `switch.unifi_network_home_amazon_tcp_inbound` | UniFi Network Home >Amazon TCP Inbound | switch |
| `switch.unifi_network_homeassistant_to_pihole` | UniFi Network HomeAssistant to PiHole | switch |
| `switch.unifi_network_iot_haproxy` | UniFi Network IOT-Haproxy | switch |
| `switch.unifi_network_marvin_to_reolink` | UniFi Network Marvin to Reolink | switch |
| `switch.unifi_network_plex` | UniFi Network Plex | switch |
| `switch.unifi_network_plex_gdm_network_discovery` | UniFi Network Plex GDM network discovery | switch |
| `switch.unifi_network_proxy_192_168_80_80` | UniFi Network Proxy 192.168.80.80 | switch |
| `switch.unifi_network_proxy_81` | UniFi Network Proxy 81 | switch |
| `switch.unifi_network_scanner` | UniFi Network Scanner | switch |
| `switch.unifi_network_syslog_to_graylog` | UniFi Network Syslog to Graylog | switch |
| `switch.unifi_network_usa_only_to_surveillance` | UniFi Network USA Only to Surveillance | switch |
| `switch.us_8_poe_150w_port_5_poe` | switch.us_8_poe_150w_port_5_poe | switch |
| `switch.us_8_poe_150w_port_6_poe` | switch.us_8_poe_150w_port_6_poe | switch |
| `switch.us_8_poe_150w_port_7_poe` | switch.us_8_poe_150w_port_7_poe | switch |
| `switch.us_8_poe_150w_port_8_poe` | switch.us_8_poe_150w_port_8_poe | switch |
| `switch.us_8_poe_150w_pve1_cluster_poe` | switch.us_8_poe_150w_pve1_cluster_poe | switch |
| `switch.us_8_poe_150w_pve2_cluster_poe` | switch.us_8_poe_150w_pve2_cluster_poe | switch |
| `switch.us_8_poe_150w_pve3_cluster_poe` | switch.us_8_poe_150w_pve3_cluster_poe | switch |
| `switch.us_8_poe_150w_pve4_cluster_poe` | switch.us_8_poe_150w_pve4_cluster_poe | switch |
| `switch.us_xg_6poe_port_1` | switch.us_xg_6poe_port_1 | switch |
| `switch.us_xg_6poe_port_1_poe` | switch.us_xg_6poe_port_1_poe | switch |
| `switch.us_xg_6poe_port_2` | switch.us_xg_6poe_port_2 | switch |
| `switch.us_xg_6poe_port_2_poe` | switch.us_xg_6poe_port_2_poe | switch |
| `switch.us_xg_6poe_port_3` | switch.us_xg_6poe_port_3 | switch |
| `switch.us_xg_6poe_port_3_poe` | switch.us_xg_6poe_port_3_poe | switch |
| `switch.us_xg_6poe_port_4` | switch.us_xg_6poe_port_4 | switch |
| `switch.us_xg_6poe_port_4_poe` | switch.us_xg_6poe_port_4_poe | switch |
| `switch.us_xg_6poe_sfp_1` | switch.us_xg_6poe_sfp_1 | switch |
| `switch.us_xg_6poe_sfp_2` | switch.us_xg_6poe_sfp_2 | switch |
| `switch.usp_pdu_pro_google_fiber_plug` | USP PDU Pro Outlet 20 | switch |
| `switch.usp_pdu_pro_port_1` | switch.usp_pdu_pro_port_1 | switch |
| `switch.usp_pdu_pro_pve_usb_hub` | USP PDU Pro | switch |
| `switch.usp_pdu_pro_pve1_plug` | USP PDU Pro Outlet 9 | switch |
| `switch.usp_pdu_pro_pve2_plug` | USP PDU Pro USW Pro 24 PoE | switch |
| `switch.usp_pdu_pro_pve3_plug` | USP PDU Pro Internet | switch |
| `switch.usp_pdu_pro_pve4_plug` | USP PDU Pro Outlet 15 | switch |
| `switch.usp_pdu_pro_reolink_plug` | USP PDU Pro US XG 6 PoE | switch |
| `switch.usp_pdu_pro_server_rack_kvm_plug` | USP PDU Pro Outlet 19 | switch |
| `switch.usp_pdu_pro_synology_ds1522_plug` | USP PDU Pro Outlet 17 | switch |
| `switch.usp_pdu_pro_synology_ds416j_plug` | USP PDU Pro random | switch |
| `switch.usp_pdu_pro_udm_pro_se_plug` | USP PDU Pro USW Enterprise 8 PoE | switch |
| `switch.usp_pdu_pro_us_8_poe_150w_plug` | USP PDU Pro USW Pro XG 10 PoE | switch |
| `switch.usp_pdu_pro_us_xg_6poe_plug` | USP PDU Pro Outlet 14 | switch |
| `switch.usp_pdu_pro_usb_outlet_1` | USP PDU Pro USB Outlet 1 | switch |
| `switch.usp_pdu_pro_usb_outlet_2` | USP PDU Pro USB Outlet 2 | switch |
| `switch.usp_pdu_pro_usb_outlet_3` | USP PDU Pro USB Outlet 3 | switch |
| `switch.usp_pdu_pro_usb_outlet_4` | USP PDU Pro USB Outlet 4 | switch |
| `switch.usp_pdu_pro_usw_aggregation_plug` | USP PDU Pro Outlet 18 | switch |
| `switch.usp_pdu_pro_usw_enterprise_8_poe_plug` | USP PDU Pro USW Pro Aggregation | switch |
| `switch.usp_pdu_pro_usw_pro_24_poe_plug` | USP PDU Pro Outlet 13 | switch |
| `switch.usw_aggregation_sfp_1` | switch.usw_aggregation_sfp_1 | switch |
| `switch.usw_aggregation_sfp_2` | switch.usw_aggregation_sfp_2 | switch |
| `switch.usw_aggregation_sfp_3` | switch.usw_aggregation_sfp_3 | switch |
| `switch.usw_aggregation_sfp_4` | switch.usw_aggregation_sfp_4 | switch |
| `switch.usw_aggregation_sfp_5` | switch.usw_aggregation_sfp_5 | switch |
| `switch.usw_aggregation_sfp_6` | switch.usw_aggregation_sfp_6 | switch |
| `switch.usw_aggregation_sfp_7` | switch.usw_aggregation_sfp_7 | switch |
| `switch.usw_aggregation_sfp_8` | switch.usw_aggregation_sfp_8 | switch |
| `switch.usw_enterprise_8_poe_port_1` | switch.usw_enterprise_8_poe_port_1 | switch |
| `switch.usw_enterprise_8_poe_port_1_poe` | switch.usw_enterprise_8_poe_port_1_poe | switch |
| `switch.usw_enterprise_8_poe_port_2` | switch.usw_enterprise_8_poe_port_2 | switch |
| `switch.usw_enterprise_8_poe_port_2_poe` | switch.usw_enterprise_8_poe_port_2_poe | switch |
| `switch.usw_enterprise_8_poe_port_3` | switch.usw_enterprise_8_poe_port_3 | switch |
| `switch.usw_enterprise_8_poe_port_3_poe` | switch.usw_enterprise_8_poe_port_3_poe | switch |
| `switch.usw_enterprise_8_poe_port_4` | switch.usw_enterprise_8_poe_port_4 | switch |
| `switch.usw_enterprise_8_poe_port_4_poe` | switch.usw_enterprise_8_poe_port_4_poe | switch |
| `switch.usw_enterprise_8_poe_port_5` | switch.usw_enterprise_8_poe_port_5 | switch |
| `switch.usw_enterprise_8_poe_port_5_poe` | switch.usw_enterprise_8_poe_port_5_poe | switch |
| `switch.usw_enterprise_8_poe_port_6` | switch.usw_enterprise_8_poe_port_6 | switch |
| `switch.usw_enterprise_8_poe_port_6_poe` | switch.usw_enterprise_8_poe_port_6_poe | switch |
| `switch.usw_enterprise_8_poe_port_7` | switch.usw_enterprise_8_poe_port_7 | switch |
| `switch.usw_enterprise_8_poe_port_7_poe` | switch.usw_enterprise_8_poe_port_7_poe | switch |
| `switch.usw_enterprise_8_poe_port_8` | switch.usw_enterprise_8_poe_port_8 | switch |
| `switch.usw_enterprise_8_poe_port_8_poe` | switch.usw_enterprise_8_poe_port_8_poe | switch |
| `switch.usw_enterprise_8_poe_sfp_1` | switch.usw_enterprise_8_poe_sfp_1 | switch |
| `switch.usw_enterprise_8_poe_sfp_2` | switch.usw_enterprise_8_poe_sfp_2 | switch |
| `switch.usw_pro_24_poe_port_1` | switch.usw_pro_24_poe_port_1 | switch |
| `switch.usw_pro_24_poe_port_1_poe` | switch.usw_pro_24_poe_port_1_poe | switch |
| `switch.usw_pro_24_poe_port_10` | switch.usw_pro_24_poe_port_10 | switch |
| `switch.usw_pro_24_poe_port_10_poe` | switch.usw_pro_24_poe_port_10_poe | switch |
| `switch.usw_pro_24_poe_port_11` | switch.usw_pro_24_poe_port_11 | switch |
| `switch.usw_pro_24_poe_port_11_poe` | switch.usw_pro_24_poe_port_11_poe | switch |
| `switch.usw_pro_24_poe_port_12` | switch.usw_pro_24_poe_port_12 | switch |
| `switch.usw_pro_24_poe_port_12_poe` | switch.usw_pro_24_poe_port_12_poe | switch |
| `switch.usw_pro_24_poe_port_13` | switch.usw_pro_24_poe_port_13 | switch |
| `switch.usw_pro_24_poe_port_13_poe` | switch.usw_pro_24_poe_port_13_poe | switch |
| `switch.usw_pro_24_poe_port_14` | switch.usw_pro_24_poe_port_14 | switch |
| `switch.usw_pro_24_poe_port_14_poe` | switch.usw_pro_24_poe_port_14_poe | switch |
| `switch.usw_pro_24_poe_port_15` | switch.usw_pro_24_poe_port_15 | switch |
| `switch.usw_pro_24_poe_port_15_poe` | switch.usw_pro_24_poe_port_15_poe | switch |
| `switch.usw_pro_24_poe_port_16` | switch.usw_pro_24_poe_port_16 | switch |
| `switch.usw_pro_24_poe_port_16_poe` | switch.usw_pro_24_poe_port_16_poe | switch |
| `switch.usw_pro_24_poe_port_17` | switch.usw_pro_24_poe_port_17 | switch |
| `switch.usw_pro_24_poe_port_17_poe` | switch.usw_pro_24_poe_port_17_poe | switch |
| `switch.usw_pro_24_poe_port_18` | switch.usw_pro_24_poe_port_18 | switch |
| `switch.usw_pro_24_poe_port_18_poe` | switch.usw_pro_24_poe_port_18_poe | switch |
| `switch.usw_pro_24_poe_port_19` | switch.usw_pro_24_poe_port_19 | switch |
| `switch.usw_pro_24_poe_port_19_poe` | switch.usw_pro_24_poe_port_19_poe | switch |
| `switch.usw_pro_24_poe_port_2` | switch.usw_pro_24_poe_port_2 | switch |
| `switch.usw_pro_24_poe_port_2_poe` | switch.usw_pro_24_poe_port_2_poe | switch |
| `switch.usw_pro_24_poe_port_20` | switch.usw_pro_24_poe_port_20 | switch |
| `switch.usw_pro_24_poe_port_20_poe` | switch.usw_pro_24_poe_port_20_poe | switch |
| `switch.usw_pro_24_poe_port_21` | switch.usw_pro_24_poe_port_21 | switch |
| `switch.usw_pro_24_poe_port_21_poe` | switch.usw_pro_24_poe_port_21_poe | switch |
| `switch.usw_pro_24_poe_port_22` | switch.usw_pro_24_poe_port_22 | switch |
| `switch.usw_pro_24_poe_port_22_poe` | switch.usw_pro_24_poe_port_22_poe | switch |
| `switch.usw_pro_24_poe_port_23` | switch.usw_pro_24_poe_port_23 | switch |
| `switch.usw_pro_24_poe_port_23_poe` | switch.usw_pro_24_poe_port_23_poe | switch |
| `switch.usw_pro_24_poe_port_24` | switch.usw_pro_24_poe_port_24 | switch |
| `switch.usw_pro_24_poe_port_24_poe` | switch.usw_pro_24_poe_port_24_poe | switch |
| `switch.usw_pro_24_poe_port_3` | switch.usw_pro_24_poe_port_3 | switch |
| `switch.usw_pro_24_poe_port_3_poe` | switch.usw_pro_24_poe_port_3_poe | switch |
| `switch.usw_pro_24_poe_port_4` | switch.usw_pro_24_poe_port_4 | switch |
| `switch.usw_pro_24_poe_port_4_poe` | switch.usw_pro_24_poe_port_4_poe | switch |
| `switch.usw_pro_24_poe_port_5` | switch.usw_pro_24_poe_port_5 | switch |
| `switch.usw_pro_24_poe_port_5_poe` | switch.usw_pro_24_poe_port_5_poe | switch |
| `switch.usw_pro_24_poe_port_7` | switch.usw_pro_24_poe_port_7 | switch |
| `switch.usw_pro_24_poe_port_7_poe` | switch.usw_pro_24_poe_port_7_poe | switch |
| `switch.usw_pro_24_poe_port_8` | switch.usw_pro_24_poe_port_8 | switch |
| `switch.usw_pro_24_poe_port_8_poe` | switch.usw_pro_24_poe_port_8_poe | switch |
| `switch.usw_pro_24_poe_port_9` | switch.usw_pro_24_poe_port_9 | switch |
| `switch.usw_pro_24_poe_port_9_poe` | switch.usw_pro_24_poe_port_9_poe | switch |
| `switch.usw_pro_24_poe_pve3_vm` | switch.usw_pro_24_poe_pve3_vm | switch |
| `switch.usw_pro_24_poe_pve3_vm_poe` | switch.usw_pro_24_poe_pve3_vm_poe | switch |
| `switch.usw_pro_24_poe_sfp_1` | switch.usw_pro_24_poe_sfp_1 | switch |
| `switch.usw_pro_24_poe_sfp_2` | switch.usw_pro_24_poe_sfp_2 | switch |
| `update.basement_entertainment_usw_flex_mini` | Basement Entertainment USW-Flex-Mini Firmware | update |
| `update.basement_office_u6_iw` | U6-IW Living Room Firmware | update |
| `update.garage_uap_ac_pro` | Garage UAP-AC-Pro | update |
| `update.laundry_room_switch` | US 8 Firmware | update |
| `update.master_bedroom_ap` | U6 Lite Garage Firmware | update |
| `update.upstairs_hallway_ap` | U6 Lite Basement Living Room Firmware | update |
| `update.us_8_poe_150w` | US 8 PoE 150W | update |
| `update.us_xg_6poe` | US XG 6 PoE Firmware | update |
| `update.usp_pdu_pro` | USP PDU Pro Firmware | update |
| `update.usw_aggregation` | USW Aggregation | update |
| `update.usw_enterprise_8_poe` | USW Enterprise 8 PoE Firmware | update |
| `update.usw_pro_24_poe` | USW Pro 24 PoE Firmware | update |
