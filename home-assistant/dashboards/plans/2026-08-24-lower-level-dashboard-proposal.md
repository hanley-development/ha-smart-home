# Lower Level Dashboard Proposal

## Scope and execution boundary

This is a non-deployable, reviewed proposal for the UI-managed `Georgetown-HAAS` dashboard at `url_path: "default"`. It neither changes Home Assistant nor authorizes a dashboard write. Every write must use a fresh approved read, the returned `config_hash`, the execution-time `BestPracticeKey`, and a separately approved literal body.

The scoped baseline intentionally does not retain a whole-dashboard payload: the broad read contained sensitive configuration and was discarded. Therefore the `living-areas` transform below is literal about the seven replacement cards and verifies the committed three-section shape before changing only the Lower Level grid. It rejects any drift rather than guessing or reconstructing Main/Upper JSON.

## Verified building blocks

- Existing card/resource syntax: `custom:mushroom-title-card`, `custom:mushroom-template-card`, `custom:mushroom-chips-card`, `custom:stack-in-card`, `grid`, `horizontal-stack`, and `tile` are present in the sanitized `living-areas` baseline; the resource inventory returned 63 registered resources.
- Existing reusable paths: `office-of-mike`, `utility_room`, and `server-room` each occur once in the scoped baseline. New-path scoped reads reported `basement-entertainment`, `basement-bathroom`, `network`, and `home-assistant` as absent.
- All entity IDs in this document are listed as selected candidates in `2026-08-24-lower-level-entity-map.md`. The Home-Assistant area ID in that map is `ha_services`; no `home_assistant` area ID is assumed.
- No card below invokes a service, script, automation, reload, restart, shutdown, firmware/update install, power action, or direct control from the Areas directory.

## Shared conventions

The card JSON uses the verified Mushroom syntax from the existing Areas view. Each directory card is a `custom:stack-in-card` with one navigation-only `custom:mushroom-template-card` and exactly two `custom:mushroom-chips-card` template chips. The main-card `tap_action` is always `navigate`; chip `tap_action` is always `more-info`; `hold_action` and `double_tap_action` are absent.

`unknown` and `unavailable` receive a red warning icon and literal state in each chip. The first chip is the alert/operational priority; it therefore displaces routine presentation rather than creating a third chip.

## Literal proposed subviews

### `basement-entertainment`

```json
{
  "theme": "Mushroom",
  "title": "Basement Entertainment",
  "path": "basement-entertainment",
  "subview": true,
  "badges": [],
  "cards": [
    {"type":"custom:mushroom-title-card","title":"Basement Entertainment","subtitle":"Status, everyday controls, and media"},
    {"type":"grid","square":false,"columns":2,"cards":[
      {"type":"tile","entity":"light.basement_main_light","name":"Main Light"},
      {"type":"tile","entity":"light.basement_bar_light","name":"Bar Light"},
      {"type":"tile","entity":"fan.basement_living_room_fan","name":"Living Room Fan"},
      {"type":"tile","entity":"fan.basement_core_400","name":"Air Purifier"}
    ]},
    {"type":"custom:mushroom-title-card","title":"Environment and media"},
    {"type":"grid","square":false,"columns":2,"cards":[
      {"type":"tile","entity":"sensor.basement_ecobee_sensor_temperature","name":"Temperature"},
      {"type":"tile","entity":"media_player.basement_receiver","name":"Receiver"},
      {"type":"tile","entity":"media_player.basement_firetv","name":"Fire TV"},
      {"type":"tile","entity":"media_player.samsung_qn90ca_85","name":"TV"}
    ]}
  ]
}
```

### `basement-bathroom`

```json
{
  "theme": "Mushroom",
  "title": "Basement Bathroom",
  "path": "basement-bathroom",
  "subview": true,
  "badges": [],
  "cards": [
    {"type":"custom:mushroom-title-card","title":"Basement Bathroom","subtitle":"Lighting, ventilation, and moisture"},
    {"type":"grid","square":false,"columns":2,"cards":[
      {"type":"tile","entity":"light.basement_bathroom_light","name":"Bathroom Light"},
      {"type":"tile","entity":"light.basement_shower_light","name":"Shower Light"},
      {"type":"tile","entity":"fan.basement_bathroom_fan","name":"Ventilation Fan"}
    ]},
    {"type":"custom:mushroom-title-card","title":"Environmental status"},
    {"type":"grid","square":false,"columns":2,"cards":[
      {"type":"tile","entity":"sensor.basement_bathroom_airguard_th_humidity","name":"Humidity"},
      {"type":"tile","entity":"sensor.basement_bathroom_airguard_th_temperature","name":"Temperature"},
      {"type":"tile","entity":"sensor.basement_bathroom_fan_humidity","name":"Fan Humidity"}
    ]}
  ]
}
```

### `office-of-mike`

```json
{
  "theme": "Mushroom",
  "title": "Mike's Office",
  "path": "office-of-mike",
  "subview": true,
  "badges": [],
  "cards": [
    {"type":"custom:mushroom-title-card","title":"Mike's Office","subtitle":"Lighting, comfort, and office equipment"},
    {"type":"grid","square":false,"columns":2,"cards":[
      {"type":"tile","entity":"light.mikes_office_light","name":"Office Light"},
      {"type":"tile","entity":"light.mikes_office_motion_nightlight","name":"Nightlight"},
      {"type":"tile","entity":"fan.mikes_office_ceiling_fan","name":"Ceiling Fan"},
      {"type":"tile","entity":"fan.office_of_mike_core_300s","name":"Air Purifier"}
    ]},
    {"type":"custom:mushroom-title-card","title":"Environment and diagnostics"},
    {"type":"grid","square":false,"columns":2,"cards":[
      {"type":"tile","entity":"sensor.mikes_office_airthings_temperature","name":"Temperature"},
      {"type":"tile","entity":"sensor.mikes_office_airthings_humidity","name":"Humidity"},
      {"type":"tile","entity":"binary_sensor.mikes_office_motion_nightlight_update_available","name":"Nightlight Update Status"}
    ]}
  ]
}
```

### `utility_room`

```json
{
  "theme": "Mushroom",
  "title": "Utility Room",
  "path": "utility_room",
  "subview": true,
  "badges": [],
  "cards": [
    {"type":"custom:mushroom-title-card","title":"Utility Room","subtitle":"Leak, water, lighting, and mechanical status"},
    {"type":"grid","square":false,"columns":2,"cards":[
      {"type":"tile","entity":"light.utility_room_light","name":"Utility Room Light"},
      {"type":"tile","entity":"binary_sensor.water_monitor_pending_system_alerts","name":"Water Monitor Alerts"},
      {"type":"tile","entity":"binary_sensor.sump_pump","name":"Sump Pump Power"}
    ]},
    {"type":"custom:mushroom-title-card","title":"Water and environment"},
    {"type":"grid","square":false,"columns":2,"cards":[
      {"type":"tile","entity":"sensor.water_monitor_water_flow_rate","name":"Water Flow"},
      {"type":"tile","entity":"sensor.water_monitor_water_pressure","name":"Water Pressure"},
      {"type":"tile","entity":"sensor.water_monitor_water_temperature","name":"Water Temperature"},
      {"type":"tile","entity":"sensor.sump_pump_usage","name":"Sump Pump Power"}
    ]}
  ]
}
```

### `server-room`

```json
{
  "theme": "Mushroom",
  "title": "Server Room",
  "path": "server-room",
  "subview": true,
  "badges": [],
  "cards": [
    {"type":"custom:mushroom-title-card","title":"Server Room","subtitle":"Read-only equipment health and temperature"},
    {"type":"grid","square":false,"columns":2,"cards":[
      {"type":"tile","entity":"sensor.server_rack_airguard_th_temperature","name":"Rack Temperature","tap_action":{"action":"more-info"}},
      {"type":"tile","entity":"sensor.cyberpower_status","name":"UPS Status","tap_action":{"action":"more-info"}},
      {"type":"tile","entity":"sensor.cyberpower_battery_charge","name":"UPS Battery","tap_action":{"action":"more-info"}},
      {"type":"tile","entity":"sensor.cyberpower_load","name":"UPS Load","tap_action":{"action":"more-info"}}
    ]},
    {"type":"custom:mushroom-title-card","title":"Storage temperatures"},
    {"type":"grid","square":false,"columns":2,"cards":[
      {"type":"tile","entity":"sensor.mediastorage_temperature","name":"Media Storage","tap_action":{"action":"more-info"}},
      {"type":"tile","entity":"sensor.r2d2_temperature","name":"R2D2","tap_action":{"action":"more-info"}},
      {"type":"tile","entity":"sensor.tripp_lite_ups_status","name":"Tripp Lite UPS","tap_action":{"action":"more-info"}}
    ]}
  ]
}
```

### `network`

```json
{
  "theme": "Mushroom",
  "title": "Network",
  "path": "network",
  "subview": true,
  "badges": [],
  "cards": [
    {"type":"custom:mushroom-title-card","title":"Network","subtitle":"Read-only connectivity and equipment health"},
    {"type":"grid","square":false,"columns":2,"cards":[
      {"type":"tile","entity":"binary_sensor.unifi_dream_machine_wan_status","name":"WAN Status","tap_action":{"action":"more-info"}},
      {"type":"tile","entity":"sensor.unifi_dream_machine_wan_status","name":"Gateway Status","tap_action":{"action":"more-info"}},
      {"type":"tile","entity":"sensor.usw_aggregation_clients","name":"Aggregation Clients","tap_action":{"action":"more-info"}},
      {"type":"tile","entity":"sensor.us_8_poe_150w_clients","name":"US 8 Clients","tap_action":{"action":"more-info"}}
    ]},
    {"type":"custom:mushroom-title-card","title":"Connectivity diagnostics"},
    {"type":"grid","square":false,"columns":2,"cards":[
      {"type":"tile","entity":"sensor.usw_aggregation_uptime","name":"Aggregation Uptime","tap_action":{"action":"more-info"}},
      {"type":"tile","entity":"sensor.us_8_poe_150w_uptime","name":"US 8 Uptime","tap_action":{"action":"more-info"}}
    ]}
  ]
}
```

### `home-assistant`

```json
{
  "theme": "Mushroom",
  "title": "Home-Assistant",
  "path": "home-assistant",
  "subview": true,
  "badges": [],
  "cards": [
    {"type":"custom:mushroom-title-card","title":"Home-Assistant","subtitle":"Read-only platform health, updates, and backups"},
    {"type":"grid","square":false,"columns":2,"cards":[
      {"type":"tile","entity":"sensor.backup_backup_manager_state","name":"Backup Manager","tap_action":{"action":"more-info"}},
      {"type":"tile","entity":"binary_sensor.home_assistant_google_drive_backup_running","name":"Backup Running","tap_action":{"action":"more-info"}},
      {"type":"tile","entity":"update.home_assistant_core_update","name":"Core Update","tap_action":{"action":"more-info"}},
      {"type":"tile","entity":"update.home_assistant_operating_system_update","name":"OS Update","tap_action":{"action":"more-info"}}
    ]},
    {"type":"custom:mushroom-title-card","title":"Backup history"},
    {"type":"grid","square":false,"columns":2,"cards":[
      {"type":"tile","entity":"sensor.backup_last_successful_automatic_backup","name":"Last Successful Backup","tap_action":{"action":"more-info"}},
      {"type":"tile","entity":"sensor.backup_next_scheduled_automatic_backup","name":"Next Scheduled Backup","tap_action":{"action":"more-info"}}
    ]}
  ]
}
```

## Literal Lower Level replacement cards

The following are the complete Lower Level content blocks used by the guarded `living-areas` transform. Each outer object is one paired row except the final, full-width Home-Assistant row. All directory main cards navigate; all chips open More Info. The two chip slots are fixed and no third chip can render.

```json
[
  {"type":"custom:mushroom-title-card","title":"Lower Level"},
  {"type":"horizontal-stack","cards":[
    {"type":"custom:stack-in-card","cards":[
      {"type":"custom:mushroom-template-card","primary":"Basement Entertainment","secondary":"{{ states('sensor.basement_ecobee_sensor_temperature') if states('sensor.basement_ecobee_sensor_temperature') not in ['unknown', 'unavailable'] else 'Temperature unavailable' }}","icon":"mdi:movie-filter-outline","entity":"media_player.basement_receiver","tap_action":{"action":"navigate","navigation_path":"basement-entertainment"},"icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","fill_container":true,"layout":"horizontal"},
      {"type":"custom:mushroom-chips-card","alignment":"end","chips":[
        {"type":"template","entity":"media_player.basement_receiver","icon":"mdi:audio-video","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}},
        {"type":"template","entity":"sensor.basement_ecobee_sensor_temperature","icon":"mdi:thermometer","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}}
      ]}
    ]},
    {"type":"custom:stack-in-card","cards":[
      {"type":"custom:mushroom-template-card","primary":"Basement Bathroom","secondary":"{{ states('sensor.basement_bathroom_airguard_th_humidity') if states('sensor.basement_bathroom_airguard_th_humidity') not in ['unknown', 'unavailable'] else 'Humidity unavailable' }}","icon":"mdi:shower","entity":"fan.basement_bathroom_fan","tap_action":{"action":"navigate","navigation_path":"basement-bathroom"},"icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","fill_container":true,"layout":"horizontal"},
      {"type":"custom:mushroom-chips-card","alignment":"end","chips":[
        {"type":"template","entity":"fan.basement_bathroom_fan","icon":"mdi:fan","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}},
        {"type":"template","entity":"sensor.basement_bathroom_airguard_th_humidity","icon":"mdi:water-percent","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}}
      ]}
    ]}
  ]},
  {"type":"horizontal-stack","cards":[
    {"type":"custom:stack-in-card","cards":[
      {"type":"custom:mushroom-template-card","primary":"Mike's Office","secondary":"{{ states('sensor.mikes_office_airthings_temperature') if states('sensor.mikes_office_airthings_temperature') not in ['unknown', 'unavailable'] else 'Temperature unavailable' }}","icon":"mdi:desk","entity":"light.mikes_office_light","tap_action":{"action":"navigate","navigation_path":"office-of-mike"},"icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","fill_container":true,"layout":"horizontal"},
      {"type":"custom:mushroom-chips-card","alignment":"end","chips":[
        {"type":"template","entity":"binary_sensor.mikes_office_motion_nightlight_update_available","icon":"mdi:update","icon_color":"{{ 'red' if states(entity) in ['on', 'unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}},
        {"type":"template","entity":"sensor.mikes_office_airthings_temperature","icon":"mdi:thermometer","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}}
      ]}
    ]},
    {"type":"custom:stack-in-card","cards":[
      {"type":"custom:mushroom-template-card","primary":"Utility Room","secondary":"{{ states('binary_sensor.water_monitor_pending_system_alerts') if states('binary_sensor.water_monitor_pending_system_alerts') not in ['unknown', 'unavailable'] else 'Alert status unavailable' }}","icon":"mdi:washing-machine","entity":"light.utility_room_light","tap_action":{"action":"navigate","navigation_path":"utility_room"},"icon_color":"{{ 'red' if states('binary_sensor.water_monitor_pending_system_alerts') in ['on', 'unknown', 'unavailable'] else 'blue' }}","fill_container":true,"layout":"horizontal"},
      {"type":"custom:mushroom-chips-card","alignment":"end","chips":[
        {"type":"template","entity":"binary_sensor.water_monitor_pending_system_alerts","icon":"mdi:water-alert","icon_color":"{{ 'red' if states(entity) in ['on', 'unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}},
        {"type":"template","entity":"sensor.sump_pump_usage","icon":"mdi:pump","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}}
      ]}
    ]}
  ]},
  {"type":"horizontal-stack","cards":[
    {"type":"custom:stack-in-card","cards":[
      {"type":"custom:mushroom-template-card","primary":"Server Room","secondary":"{{ states('sensor.server_rack_airguard_th_temperature') if states('sensor.server_rack_airguard_th_temperature') not in ['unknown', 'unavailable'] else 'Temperature unavailable' }}","icon":"mdi:server","entity":"sensor.cyberpower_status","tap_action":{"action":"navigate","navigation_path":"server-room"},"icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","fill_container":true,"layout":"horizontal"},
      {"type":"custom:mushroom-chips-card","alignment":"end","chips":[
        {"type":"template","entity":"sensor.cyberpower_status","icon":"mdi:ups","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}},
        {"type":"template","entity":"sensor.server_rack_airguard_th_temperature","icon":"mdi:thermometer","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}}
      ]}
    ]},
    {"type":"custom:stack-in-card","cards":[
      {"type":"custom:mushroom-template-card","primary":"Network","secondary":"{{ states('binary_sensor.unifi_dream_machine_wan_status') if states('binary_sensor.unifi_dream_machine_wan_status') not in ['unknown', 'unavailable'] else 'WAN status unavailable' }}","icon":"mdi:wan","entity":"binary_sensor.unifi_dream_machine_wan_status","tap_action":{"action":"navigate","navigation_path":"network"},"icon_color":"{{ 'red' if states(entity) in ['off', 'unknown', 'unavailable'] else 'blue' }}","fill_container":true,"layout":"horizontal"},
      {"type":"custom:mushroom-chips-card","alignment":"end","chips":[
        {"type":"template","entity":"binary_sensor.unifi_dream_machine_wan_status","icon":"mdi:web","icon_color":"{{ 'red' if states(entity) in ['off', 'unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}},
        {"type":"template","entity":"sensor.usw_aggregation_clients","icon":"mdi:lan-connect","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}}
      ]}
    ]}
  ]},
  {"type":"custom:stack-in-card","cards":[
    {"type":"custom:mushroom-template-card","primary":"Home-Assistant","secondary":"{{ states('sensor.backup_backup_manager_state') if states('sensor.backup_backup_manager_state') not in ['unknown', 'unavailable'] else 'Backup status unavailable' }}","icon":"mdi:home-assistant","entity":"sensor.backup_backup_manager_state","tap_action":{"action":"navigate","navigation_path":"home-assistant"},"icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","fill_container":true,"layout":"horizontal"},
    {"type":"custom:mushroom-chips-card","alignment":"end","chips":[
      {"type":"template","entity":"binary_sensor.home_assistant_google_drive_backup_running","icon":"mdi:backup-restore","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}},
      {"type":"template","entity":"update.home_assistant_core_update","icon":"mdi:update","icon_color":"{{ 'red' if states(entity) in ['on', 'unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}}
    ]}
  ]}
]
```

## Guarded stage transforms

For every stage, the execution operator must first obtain approval for `ha_config_get_dashboard({"url_path":"default","force_reload":true})`. The approved `ha_config_set_dashboard` body uses `url_path: "default"`, `config_hash: "${EXECUTION_TIME_CONFIG_HASH}"`, `BestPracticeKey: "${EXECUTION_TIME_BEST_PRACTICE_KEY}"`, the complete literal `python_transform` in that stage below, and `return_screenshot: false`. The hash and BestPracticeKey are the only execution-time values; each transform is otherwise fully literal.

### Python-transform security compatibility

The dashboard transform schema rejects imports. Every transform below is intentionally limited to literal dictionaries/lists, variable assignment, list comprehensions, `assert`, `len`, equality comparison, dictionary/list indexing, and list `append` or assignment. It contains no import, function/class definition, exception handling, loop statement, dynamic execution, dunder name, or filesystem/network operation.

### Stage 1: create `basement-entertainment`

```python
target_path = "basement-entertainment"
replacement = {"theme":"Mushroom","title":"Basement Entertainment","path":"basement-entertainment","subview":True,"badges":[],"cards":[{"type":"custom:mushroom-title-card","title":"Basement Entertainment","subtitle":"Status, everyday controls, and media"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"light.basement_main_light","name":"Main Light"},{"type":"tile","entity":"light.basement_bar_light","name":"Bar Light"},{"type":"tile","entity":"fan.basement_living_room_fan","name":"Living Room Fan"},{"type":"tile","entity":"fan.basement_core_400","name":"Air Purifier"}]},{"type":"custom:mushroom-title-card","title":"Environment and media"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"sensor.basement_ecobee_sensor_temperature","name":"Temperature"},{"type":"tile","entity":"media_player.basement_receiver","name":"Receiver"},{"type":"tile","entity":"media_player.basement_firetv","name":"Fire TV"},{"type":"tile","entity":"media_player.samsung_qn90ca_85","name":"TV"}]}]}
assert replacement["path"] == target_path
assert replacement["subview"] == True
matches = [view for view in config["views"] if view["path"] == target_path]
assert len(matches) == 0, "target path is occupied"
config["views"].append(replacement)
```

### Stage 2: create `basement-bathroom`

```python
target_path = "basement-bathroom"
replacement = {"theme":"Mushroom","title":"Basement Bathroom","path":"basement-bathroom","subview":True,"badges":[],"cards":[{"type":"custom:mushroom-title-card","title":"Basement Bathroom","subtitle":"Lighting, ventilation, and moisture"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"light.basement_bathroom_light","name":"Bathroom Light"},{"type":"tile","entity":"light.basement_shower_light","name":"Shower Light"},{"type":"tile","entity":"fan.basement_bathroom_fan","name":"Ventilation Fan"}]},{"type":"custom:mushroom-title-card","title":"Environmental status"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"sensor.basement_bathroom_airguard_th_humidity","name":"Humidity"},{"type":"tile","entity":"sensor.basement_bathroom_airguard_th_temperature","name":"Temperature"},{"type":"tile","entity":"sensor.basement_bathroom_fan_humidity","name":"Fan Humidity"}]}]}
assert replacement["path"] == target_path
assert replacement["subview"] == True
matches = [view for view in config["views"] if view["path"] == target_path]
assert len(matches) == 0, "target path is occupied"
config["views"].append(replacement)
```

### Stage 3: create `network`

```python
target_path = "network"
replacement = {"theme":"Mushroom","title":"Network","path":"network","subview":True,"badges":[],"cards":[{"type":"custom:mushroom-title-card","title":"Network","subtitle":"Read-only connectivity and equipment health"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"binary_sensor.unifi_dream_machine_wan_status","name":"WAN Status","tap_action":{"action":"more-info"}},{"type":"tile","entity":"sensor.unifi_dream_machine_wan_status","name":"Gateway Status","tap_action":{"action":"more-info"}},{"type":"tile","entity":"sensor.usw_aggregation_clients","name":"Aggregation Clients","tap_action":{"action":"more-info"}},{"type":"tile","entity":"sensor.us_8_poe_150w_clients","name":"US 8 Clients","tap_action":{"action":"more-info"}}]},{"type":"custom:mushroom-title-card","title":"Connectivity diagnostics"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"sensor.usw_aggregation_uptime","name":"Aggregation Uptime","tap_action":{"action":"more-info"}},{"type":"tile","entity":"sensor.us_8_poe_150w_uptime","name":"US 8 Uptime","tap_action":{"action":"more-info"}}]}]}
assert replacement["path"] == target_path
assert replacement["subview"] == True
matches = [view for view in config["views"] if view["path"] == target_path]
assert len(matches) == 0, "target path is occupied"
config["views"].append(replacement)
```

### Stage 4: create `home-assistant`

```python
target_path = "home-assistant"
replacement = {"theme":"Mushroom","title":"Home-Assistant","path":"home-assistant","subview":True,"badges":[],"cards":[{"type":"custom:mushroom-title-card","title":"Home-Assistant","subtitle":"Read-only platform health, updates, and backups"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"sensor.backup_backup_manager_state","name":"Backup Manager","tap_action":{"action":"more-info"}},{"type":"tile","entity":"binary_sensor.home_assistant_google_drive_backup_running","name":"Backup Running","tap_action":{"action":"more-info"}},{"type":"tile","entity":"update.home_assistant_core_update","name":"Core Update","tap_action":{"action":"more-info"}},{"type":"tile","entity":"update.home_assistant_operating_system_update","name":"OS Update","tap_action":{"action":"more-info"}}]},{"type":"custom:mushroom-title-card","title":"Backup history"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"sensor.backup_last_successful_automatic_backup","name":"Last Successful Backup","tap_action":{"action":"more-info"}},{"type":"tile","entity":"sensor.backup_next_scheduled_automatic_backup","name":"Next Scheduled Backup","tap_action":{"action":"more-info"}}]}]}
assert replacement["path"] == target_path
assert replacement["subview"] == True
matches = [view for view in config["views"] if view["path"] == target_path]
assert len(matches) == 0, "target path is occupied"
config["views"].append(replacement)
```

### Stage 5: replace `office-of-mike`

```python
target_path = "office-of-mike"
replacement = {"theme":"Mushroom","title":"Mike's Office","path":"office-of-mike","subview":True,"badges":[],"cards":[{"type":"custom:mushroom-title-card","title":"Mike's Office","subtitle":"Lighting, comfort, and office equipment"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"light.mikes_office_light","name":"Office Light"},{"type":"tile","entity":"light.mikes_office_motion_nightlight","name":"Nightlight"},{"type":"tile","entity":"fan.mikes_office_ceiling_fan","name":"Ceiling Fan"},{"type":"tile","entity":"fan.office_of_mike_core_300s","name":"Air Purifier"}]},{"type":"custom:mushroom-title-card","title":"Environment and diagnostics"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"sensor.mikes_office_airthings_temperature","name":"Temperature"},{"type":"tile","entity":"sensor.mikes_office_airthings_humidity","name":"Humidity"},{"type":"tile","entity":"binary_sensor.mikes_office_motion_nightlight_update_available","name":"Nightlight Update Status"}]}]}
assert replacement["path"] == target_path
assert replacement["subview"] == True
matches = [view for view in config["views"] if view["path"] == target_path]
assert len(matches) == 1, "expected one reusable view"
view_index = [index for index in range(len(config["views"])) if config["views"][index]["path"] == target_path]
assert len(view_index) == 1, "expected one reusable index"
config["views"][view_index[0]] = replacement
```

### Stage 6: replace `utility_room`

```python
target_path = "utility_room"
replacement = {"theme":"Mushroom","title":"Utility Room","path":"utility_room","subview":True,"badges":[],"cards":[{"type":"custom:mushroom-title-card","title":"Utility Room","subtitle":"Leak, water, lighting, and mechanical status"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"light.utility_room_light","name":"Utility Room Light"},{"type":"tile","entity":"binary_sensor.water_monitor_pending_system_alerts","name":"Water Monitor Alerts"},{"type":"tile","entity":"binary_sensor.sump_pump","name":"Sump Pump Power"}]},{"type":"custom:mushroom-title-card","title":"Water and environment"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"sensor.water_monitor_water_flow_rate","name":"Water Flow"},{"type":"tile","entity":"sensor.water_monitor_water_pressure","name":"Water Pressure"},{"type":"tile","entity":"sensor.water_monitor_water_temperature","name":"Water Temperature"},{"type":"tile","entity":"sensor.sump_pump_usage","name":"Sump Pump Power"}]}]}
assert replacement["path"] == target_path
assert replacement["subview"] == True
matches = [view for view in config["views"] if view["path"] == target_path]
assert len(matches) == 1, "expected one reusable view"
view_index = [index for index in range(len(config["views"])) if config["views"][index]["path"] == target_path]
assert len(view_index) == 1, "expected one reusable index"
config["views"][view_index[0]] = replacement
```

### Stage 7: replace `server-room`

```python
target_path = "server-room"
replacement = {"theme":"Mushroom","title":"Server Room","path":"server-room","subview":True,"badges":[],"cards":[{"type":"custom:mushroom-title-card","title":"Server Room","subtitle":"Read-only equipment health and temperature"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"sensor.server_rack_airguard_th_temperature","name":"Rack Temperature","tap_action":{"action":"more-info"}},{"type":"tile","entity":"sensor.cyberpower_status","name":"UPS Status","tap_action":{"action":"more-info"}},{"type":"tile","entity":"sensor.cyberpower_battery_charge","name":"UPS Battery","tap_action":{"action":"more-info"}},{"type":"tile","entity":"sensor.cyberpower_load","name":"UPS Load","tap_action":{"action":"more-info"}}]},{"type":"custom:mushroom-title-card","title":"Storage temperatures"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"sensor.mediastorage_temperature","name":"Media Storage","tap_action":{"action":"more-info"}},{"type":"tile","entity":"sensor.r2d2_temperature","name":"R2D2","tap_action":{"action":"more-info"}},{"type":"tile","entity":"sensor.tripp_lite_ups_status","name":"Tripp Lite UPS","tap_action":{"action":"more-info"}}]}]}
assert replacement["path"] == target_path
assert replacement["subview"] == True
matches = [view for view in config["views"] if view["path"] == target_path]
assert len(matches) == 1, "expected one reusable view"
view_index = [index for index in range(len(config["views"])) if config["views"][index]["path"] == target_path]
assert len(view_index) == 1, "expected one reusable index"
config["views"][view_index[0]] = replacement
```

### Stage 8: replace only the `living-areas` Lower Level slice

This transform matches the committed scoped `living-areas` baseline: its top-level `cards` list has exactly three grids, whose leading title cards are `Main Level`, `Lower Level`, and `Upper Level ` (including its retained trailing space). It binds and equality-checks the untouched Main and Upper grids, then replaces only top-level card 1 with the complete literal Lower Level grid.

```python
target_path = "living-areas"
matches = [view for view in config["views"] if view["path"] == target_path]
assert len(matches) == 1, "expected one living-areas view"
view = matches[0]
assert view["title"] == "Areas" and view["subview"] == True
assert len(view["cards"]) == 3
main_before = view["cards"][0]
lower_before = view["cards"][1]
upper_before = view["cards"][2]
assert main_before["type"] == "grid" and main_before["columns"] == 1 and main_before["square"] == False
assert lower_before["type"] == "grid" and lower_before["columns"] == 1 and lower_before["square"] == False
assert upper_before["type"] == "grid" and upper_before["columns"] == 1 and upper_before["square"] == False
assert len(main_before["cards"]) > 0
assert len(lower_before["cards"]) > 0
assert len(upper_before["cards"]) > 0
assert main_before["cards"][0] == {"type": "custom:mushroom-title-card", "title": "Main Level"}
assert lower_before["cards"][0] == {"type": "custom:mushroom-title-card", "title": "Lower Level"}
assert upper_before["cards"][0] == {"type": "custom:mushroom-title-card", "title": "Upper Level "}
replacement = {"square":False,"columns":1,"type":"grid","cards":[
  {"type":"custom:mushroom-title-card","title":"Lower Level"},
  {"type":"horizontal-stack","cards":[
    {"type":"custom:stack-in-card","cards":[{"type":"custom:mushroom-template-card","primary":"Basement Entertainment","secondary":"{{ states('sensor.basement_ecobee_sensor_temperature') if states('sensor.basement_ecobee_sensor_temperature') not in ['unknown', 'unavailable'] else 'Temperature unavailable' }}","icon":"mdi:movie-filter-outline","entity":"media_player.basement_receiver","tap_action":{"action":"navigate","navigation_path":"basement-entertainment"},"icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","fill_container":True,"layout":"horizontal"},{"type":"custom:mushroom-chips-card","alignment":"end","chips":[{"type":"template","entity":"media_player.basement_receiver","icon":"mdi:audio-video","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}},{"type":"template","entity":"sensor.basement_ecobee_sensor_temperature","icon":"mdi:thermometer","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}}]}]},
    {"type":"custom:stack-in-card","cards":[{"type":"custom:mushroom-template-card","primary":"Basement Bathroom","secondary":"{{ states('sensor.basement_bathroom_airguard_th_humidity') if states('sensor.basement_bathroom_airguard_th_humidity') not in ['unknown', 'unavailable'] else 'Humidity unavailable' }}","icon":"mdi:shower","entity":"fan.basement_bathroom_fan","tap_action":{"action":"navigate","navigation_path":"basement-bathroom"},"icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","fill_container":True,"layout":"horizontal"},{"type":"custom:mushroom-chips-card","alignment":"end","chips":[{"type":"template","entity":"fan.basement_bathroom_fan","icon":"mdi:fan","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}},{"type":"template","entity":"sensor.basement_bathroom_airguard_th_humidity","icon":"mdi:water-percent","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}}]}]}
  ]},
  {"type":"horizontal-stack","cards":[
    {"type":"custom:stack-in-card","cards":[{"type":"custom:mushroom-template-card","primary":"Mike's Office","secondary":"{{ states('sensor.mikes_office_airthings_temperature') if states('sensor.mikes_office_airthings_temperature') not in ['unknown', 'unavailable'] else 'Temperature unavailable' }}","icon":"mdi:desk","entity":"light.mikes_office_light","tap_action":{"action":"navigate","navigation_path":"office-of-mike"},"icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","fill_container":True,"layout":"horizontal"},{"type":"custom:mushroom-chips-card","alignment":"end","chips":[{"type":"template","entity":"binary_sensor.mikes_office_motion_nightlight_update_available","icon":"mdi:update","icon_color":"{{ 'red' if states(entity) in ['on', 'unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}},{"type":"template","entity":"sensor.mikes_office_airthings_temperature","icon":"mdi:thermometer","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}}]}]},
    {"type":"custom:stack-in-card","cards":[{"type":"custom:mushroom-template-card","primary":"Utility Room","secondary":"{{ states('binary_sensor.water_monitor_pending_system_alerts') if states('binary_sensor.water_monitor_pending_system_alerts') not in ['unknown', 'unavailable'] else 'Alert status unavailable' }}","icon":"mdi:washing-machine","entity":"light.utility_room_light","tap_action":{"action":"navigate","navigation_path":"utility_room"},"icon_color":"{{ 'red' if states('binary_sensor.water_monitor_pending_system_alerts') in ['on', 'unknown', 'unavailable'] else 'blue' }}","fill_container":True,"layout":"horizontal"},{"type":"custom:mushroom-chips-card","alignment":"end","chips":[{"type":"template","entity":"binary_sensor.water_monitor_pending_system_alerts","icon":"mdi:water-alert","icon_color":"{{ 'red' if states(entity) in ['on', 'unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}},{"type":"template","entity":"sensor.sump_pump_usage","icon":"mdi:pump","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}}]}]}
  ]},
  {"type":"horizontal-stack","cards":[
    {"type":"custom:stack-in-card","cards":[{"type":"custom:mushroom-template-card","primary":"Server Room","secondary":"{{ states('sensor.server_rack_airguard_th_temperature') if states('sensor.server_rack_airguard_th_temperature') not in ['unknown', 'unavailable'] else 'Temperature unavailable' }}","icon":"mdi:server","entity":"sensor.cyberpower_status","tap_action":{"action":"navigate","navigation_path":"server-room"},"icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","fill_container":True,"layout":"horizontal"},{"type":"custom:mushroom-chips-card","alignment":"end","chips":[{"type":"template","entity":"sensor.cyberpower_status","icon":"mdi:ups","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}},{"type":"template","entity":"sensor.server_rack_airguard_th_temperature","icon":"mdi:thermometer","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}}]}]},
    {"type":"custom:stack-in-card","cards":[{"type":"custom:mushroom-template-card","primary":"Network","secondary":"{{ states('binary_sensor.unifi_dream_machine_wan_status') if states('binary_sensor.unifi_dream_machine_wan_status') not in ['unknown', 'unavailable'] else 'WAN status unavailable' }}","icon":"mdi:wan","entity":"binary_sensor.unifi_dream_machine_wan_status","tap_action":{"action":"navigate","navigation_path":"network"},"icon_color":"{{ 'red' if states(entity) in ['off', 'unknown', 'unavailable'] else 'blue' }}","fill_container":True,"layout":"horizontal"},{"type":"custom:mushroom-chips-card","alignment":"end","chips":[{"type":"template","entity":"binary_sensor.unifi_dream_machine_wan_status","icon":"mdi:web","icon_color":"{{ 'red' if states(entity) in ['off', 'unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}},{"type":"template","entity":"sensor.usw_aggregation_clients","icon":"mdi:lan-connect","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}}]}]}
  ]},
  {"type":"custom:stack-in-card","cards":[{"type":"custom:mushroom-template-card","primary":"Home-Assistant","secondary":"{{ states('sensor.backup_backup_manager_state') if states('sensor.backup_backup_manager_state') not in ['unknown', 'unavailable'] else 'Backup status unavailable' }}","icon":"mdi:home-assistant","entity":"sensor.backup_backup_manager_state","tap_action":{"action":"navigate","navigation_path":"home-assistant"},"icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","fill_container":True,"layout":"horizontal"},{"type":"custom:mushroom-chips-card","alignment":"end","chips":[{"type":"template","entity":"binary_sensor.home_assistant_google_drive_backup_running","icon":"mdi:backup-restore","icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}},{"type":"template","entity":"update.home_assistant_core_update","icon":"mdi:update","icon_color":"{{ 'red' if states(entity) in ['on', 'unknown', 'unavailable'] else 'green' }}","content":"{{ states(entity) }}","tap_action":{"action":"more-info"}}]}]}
]}
assert replacement["square"] == False and replacement["columns"] == 1 and replacement["type"] == "grid"
assert len(replacement["cards"]) == 5 and replacement["cards"][0] == {"type": "custom:mushroom-title-card", "title": "Lower Level"}
view["cards"][1] = replacement
assert view["cards"][0] == main_before and view["cards"][2] == upper_before
```

## Preconditions and read-back assertions

| Stage | Target | Precondition | Read-back assertions | Rollback source |
| --- | --- | --- | --- | --- |
| 1 | `basement-entertainment` | Path count 0; proposal commit pushed; fresh hash | title/path exact, `subview: true`, eight selected entities, navigation-safe cards | Remove only the new path after separate approval; pre-change path absence receipt |
| 2 | `basement-bathroom` | Path count 0; stage 1 receipt matches; fresh hash | title/path exact, `subview: true`, light/fan/humidity modules | Remove only the new path after separate approval; pre-change path absence receipt |
| 3 | `network` | Path count 0; earlier receipts match; fresh hash | title/path exact, `subview: true`, only read-only diagnostic cards; no gateway/switch/AP/PoE/reboot/power action | Remove only the new path after separate approval; pre-change path absence receipt |
| 4 | `home-assistant` | Path count 0; earlier receipts match; fresh hash | title/path exact, `subview: true`, health/update/backup status only; no restart/shutdown/reload/install action | Remove only the new path after separate approval; pre-change path absence receipt |
| 5 | `office-of-mike` | Path count 1 and fresh scoped rollback object; fresh hash | title `Mike's Office`, stable path, `subview: true`, selected light/fan/environment cards | Fresh scoped `office-of-mike` rollback JSON in pre-change snapshot |
| 6 | `utility_room` | Path count 1 and fresh scoped rollback object; fresh hash | stable path, `subview: true`, alert/water/environment priority | Fresh scoped `utility_room` rollback JSON in pre-change snapshot |
| 7 | `server-room` | Path count 1 and fresh scoped rollback object; fresh hash | stable path, `subview: true`, status/temperature only; no power/reboot/shutdown controls | Fresh scoped `server-room` rollback JSON in pre-change snapshot |
| 8 | `living-areas` | Exactly one target view and each of seven destination paths exactly once; fresh scoped rollback object; unique ordered headings | exact seven-card order, paired rows, full final Home-Assistant row, no more than two chips/card, all main taps navigate, all chip taps More Info, Main/Upper title-bounded slices logically unchanged | Fresh scoped `living-areas` rollback JSON in pre-change snapshot |

For every stage, compare the immediately read-back object with its literal replacement, verify the listed entity IDs, check all selected states render honestly, and stop on a missing identifier, resource, path collision, write failure, read-back mismatch, unrelated change, sensitive-content exposure, or unusable rollback artifact.

## Consistency checklist

- Seven destinations are ordered: Basement Entertainment, Basement Bathroom, Mike's Office, Utility Room, Server Room, Network, Home-Assistant.
- Existing paths remain stable: `office-of-mike`, `utility_room`, `server-room`.
- The directory has three paired rows and a full-width fourth row; no generic Basement card or intermediate view exists.
- Every proposed entity is selected in the verified entity map. No custom card type is unverified.
- Server Room, Network, and Home-Assistant are read-only status views; no risky system, power, network, or update-install action is present.
- Areas directory cards and chips cannot change an entity state. No main card has hidden hold/double-tap behavior.
- The document contains no token, credential, cookie, private URL, calendar/event, person, or device-tracker content.
