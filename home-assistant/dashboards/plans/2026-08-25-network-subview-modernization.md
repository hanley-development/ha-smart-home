# Network Subview Modernization Proposal

**Status:** Applied and verified; seamless chip styling approved and pending

**Date:** 2026-08-25

## Scope

Modernize the UI-managed `Network` subview at `default/network`. The view remains
diagnostic and read-only. It includes UniFi infrastructure assigned to the
`Network` area and carrying the `Networking` or `Unifi-Device` label.

The proposal replaces stale legacy entities with live, verified entities and
adds the requested Clients, State, Uptime, CPU utilization, Memory utilization,
and Temperature metrics where each device exposes them. It also shows read-only
firmware status. It excludes client devices and every restart, power-cycle, PoE,
outlet, port-control, service, script, and automation action.

## Verified live baseline

- Dashboard: `default` (`Georgetown-HAAS`), storage mode
- Fresh configuration hash: `4e5c06aefe9337ca`
- Target path: `network`, exactly once, at view index 30
- Current target: title `Network`, `subview: true`, four top-level cards
- All eight Lower Level destination paths occur exactly once
- `sensor.unifi_dream_machine_wan_status` is a stale `unknown` sensor
- `sensor.hanley_dream_machine_se_state` is the verified gateway-state sensor
- Network sensor inventory: 273 visible entities over three complete pages;
  `partial: false` and `has_more: false` on the final page

The current target view below is the rollback object and the exact optimistic
guard. The transform makes no change if it has drifted.

## Device selection

The replacement contains these labeled infrastructure devices:

- Gateway: Hanley Dream Machine SE
- Access points: U6-IW Living Room, U6 Lite Garage, U6 Lite Basement Living
  Room, U7 Pro XGS Hallway, U7 Pro XGS Mike's Office, and U7 Pro XGS Master
  Bedroom
- Switches: US 8, US XG 6 PoE, USW Enterprise 8 PoE, USW Pro 24 PoE, and USW
  Pro Aggregation
- Other infrastructure: USP PDU Pro

The unavailable, unlabeled legacy USW Aggregation and ordinary network clients
are intentionally excluded. A metric that later becomes `unknown` or
`unavailable` remains visible with warning coloring.

## Exact proposed write body

The repository records the exact transform before execution. At execution time,
the hash must be refreshed if the dashboard changes. `BestPracticeKey` is omitted
because this Home Assistant MCP server is configured in non-strict mode.

```json
{
  "url_path": "default",
  "config_hash": "4e5c06aefe9337ca",
  "python_transform": "<the literal Python transform below>",
  "return_screenshot": false
}
```

```python
target_path = "network"
expected_current = {"theme":"Mushroom","title":"Network","path":"network","subview":True,"badges":[],"cards":[{"type":"custom:mushroom-title-card","title":"Network","subtitle":"Read-only connectivity and equipment health"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"binary_sensor.unifi_dream_machine_wan_status","name":"WAN Status","tap_action":{"action":"more-info"}},{"type":"tile","entity":"sensor.unifi_dream_machine_wan_status","name":"Gateway Status","tap_action":{"action":"more-info"}},{"type":"tile","entity":"sensor.usw_aggregation_clients","name":"Aggregation Clients","tap_action":{"action":"more-info"}},{"type":"tile","entity":"sensor.us_8_poe_150w_clients","name":"US 8 Clients","tap_action":{"action":"more-info"}}]},{"type":"custom:mushroom-title-card","title":"Connectivity diagnostics"},{"type":"grid","square":False,"columns":2,"cards":[{"type":"tile","entity":"sensor.usw_aggregation_uptime","name":"Aggregation Uptime","tap_action":{"action":"more-info"}},{"type":"tile","entity":"sensor.us_8_poe_150w_uptime","name":"US 8 Uptime","tap_action":{"action":"more-info"}}]}]}
devices = [
    {"group":"gateway","name":"Hanley Dream Machine SE","icon":"mdi:router-network","state":"sensor.hanley_dream_machine_se_state","update":"update.hanley_dream_machine_se","metrics":[
        {"entity":"sensor.hanley_dream_machine_se_clients","icon":"mdi:account-network","content":"{{ states(entity) }} clients"},
        {"entity":"sensor.hanley_dream_machine_se_uptime","icon":"mdi:timer-outline","content":"{{ relative_time(states(entity) | as_datetime) if states(entity) not in ['unknown', 'unavailable'] else states(entity) }}"},
        {"entity":"sensor.hanley_dream_machine_se_cpu_utilization","icon":"mdi:cpu-64-bit","content":"CPU {{ states(entity) }}%"},
        {"entity":"sensor.hanley_dream_machine_se_memory_utilization","icon":"mdi:memory","content":"RAM {{ states(entity) }}%"},
        {"entity":"sensor.hanley_dream_machine_se_hanley_dream_machine_se_cpu_temperature","icon":"mdi:thermometer","content":"CPU {{ states(entity) }}{{ state_attr(entity, 'unit_of_measurement') or '' }}"},
        {"entity":"sensor.hanley_dream_machine_se_hanley_dream_machine_se_local_temperature","icon":"mdi:thermometer","content":"Local {{ states(entity) }}{{ state_attr(entity, 'unit_of_measurement') or '' }}"},
        {"entity":"sensor.hanley_dream_machine_se_hanley_dream_machine_se_phy_temperature","icon":"mdi:thermometer","content":"PHY {{ states(entity) }}{{ state_attr(entity, 'unit_of_measurement') or '' }}"}
    ]},
    {"group":"ap","name":"U6-IW Living Room","icon":"mdi:access-point-network","state":"sensor.basement_office_u6_iw_state","update":"update.basement_office_u6_iw","metrics":[
        {"entity":"sensor.basement_office_u6_iw_clients","icon":"mdi:account-network","content":"{{ states(entity) }} clients"},
        {"entity":"sensor.basement_office_u6_iw_uptime","icon":"mdi:timer-outline","content":"{{ relative_time(states(entity) | as_datetime) if states(entity) not in ['unknown', 'unavailable'] else states(entity) }}"},
        {"entity":"sensor.basement_office_u6_iw_cpu_utilization","icon":"mdi:cpu-64-bit","content":"CPU {{ states(entity) }}%"},
        {"entity":"sensor.basement_office_u6_iw_memory_utilization","icon":"mdi:memory","content":"RAM {{ states(entity) }}%"}
    ]},
    {"group":"ap","name":"U6 Lite Garage","icon":"mdi:access-point-network","state":"sensor.master_bedroom_ap_state","update":"update.master_bedroom_ap","metrics":[
        {"entity":"sensor.master_bedroom_ap_clients","icon":"mdi:account-network","content":"{{ states(entity) }} clients"},
        {"entity":"sensor.master_bedroom_ap_uptime","icon":"mdi:timer-outline","content":"{{ relative_time(states(entity) | as_datetime) if states(entity) not in ['unknown', 'unavailable'] else states(entity) }}"},
        {"entity":"sensor.master_bedroom_ap_cpu_utilization","icon":"mdi:cpu-64-bit","content":"CPU {{ states(entity) }}%"},
        {"entity":"sensor.master_bedroom_ap_memory_utilization","icon":"mdi:memory","content":"RAM {{ states(entity) }}%"}
    ]},
    {"group":"ap","name":"U6 Lite Basement Living Room","icon":"mdi:access-point-network","state":"sensor.upstairs_hallway_ap_state","update":"update.upstairs_hallway_ap","metrics":[
        {"entity":"sensor.upstairs_hallway_ap_clients","icon":"mdi:account-network","content":"{{ states(entity) }} clients"},
        {"entity":"sensor.upstairs_hallway_ap_uptime","icon":"mdi:timer-outline","content":"{{ relative_time(states(entity) | as_datetime) if states(entity) not in ['unknown', 'unavailable'] else states(entity) }}"},
        {"entity":"sensor.upstairs_hallway_ap_cpu_utilization","icon":"mdi:cpu-64-bit","content":"CPU {{ states(entity) }}%"},
        {"entity":"sensor.upstairs_hallway_ap_memory_utilization","icon":"mdi:memory","content":"RAM {{ states(entity) }}%"}
    ]},
    {"group":"ap","name":"U7 Pro XGS Hallway","icon":"mdi:access-point-network","state":"sensor.u7_pro_xgs_state","update":"update.u7_pro_xgs","metrics":[
        {"entity":"sensor.u7_pro_xgs_clients","icon":"mdi:account-network","content":"{{ states(entity) }} clients"},
        {"entity":"sensor.u7_pro_xgs_uptime","icon":"mdi:timer-outline","content":"{{ relative_time(states(entity) | as_datetime) if states(entity) not in ['unknown', 'unavailable'] else states(entity) }}"},
        {"entity":"sensor.u7_pro_xgs_hallway_cpu_utilization","icon":"mdi:cpu-64-bit","content":"CPU {{ states(entity) }}%"},
        {"entity":"sensor.u7_pro_xgs_hallway_memory_utilization","icon":"mdi:memory","content":"RAM {{ states(entity) }}%"}
    ]},
    {"group":"ap","name":"U7 Pro XGS Mike's Office","icon":"mdi:access-point-network","state":"sensor.u7_pro_xgs_state_2","update":"update.u7_pro_xgs_2","metrics":[
        {"entity":"sensor.u7_pro_xgs_clients_2","icon":"mdi:account-network","content":"{{ states(entity) }} clients"},
        {"entity":"sensor.u7_pro_xgs_uptime_2","icon":"mdi:timer-outline","content":"{{ relative_time(states(entity) | as_datetime) if states(entity) not in ['unknown', 'unavailable'] else states(entity) }}"},
        {"entity":"sensor.u7_pro_xgs_cpu_utilization","icon":"mdi:cpu-64-bit","content":"CPU {{ states(entity) }}%"},
        {"entity":"sensor.u7_pro_xgs_memory_utilization","icon":"mdi:memory","content":"RAM {{ states(entity) }}%"}
    ]},
    {"group":"ap","name":"U7 Pro XGS Master Bedroom","icon":"mdi:access-point-network","state":"sensor.none_state","update":"update.unifi_device_update_8c_30_66_78_e4_f2","metrics":[
        {"entity":"sensor.none_clients","icon":"mdi:account-network","content":"{{ states(entity) }} clients"},
        {"entity":"sensor.none_uptime","icon":"mdi:timer-outline","content":"{{ relative_time(states(entity) | as_datetime) if states(entity) not in ['unknown', 'unavailable'] else states(entity) }}"},
        {"entity":"sensor.u7_pro_xgs_master_bedroom_cpu_utilization","icon":"mdi:cpu-64-bit","content":"CPU {{ states(entity) }}%"},
        {"entity":"sensor.u7_pro_xgs_master_bedroom_memory_utilization","icon":"mdi:memory","content":"RAM {{ states(entity) }}%"}
    ]},
    {"group":"switch","name":"US 8","icon":"mdi:switch","state":"sensor.laundry_room_switch_state","update":"update.laundry_room_switch","metrics":[
        {"entity":"sensor.laundry_room_switch_clients","icon":"mdi:account-network","content":"{{ states(entity) }} clients"},
        {"entity":"sensor.laundry_room_switch_uptime","icon":"mdi:timer-outline","content":"{{ relative_time(states(entity) | as_datetime) if states(entity) not in ['unknown', 'unavailable'] else states(entity) }}"},
        {"entity":"sensor.laundry_room_switch_cpu_utilization","icon":"mdi:cpu-64-bit","content":"CPU {{ states(entity) }}%"},
        {"entity":"sensor.laundry_room_switch_memory_utilization","icon":"mdi:memory","content":"RAM {{ states(entity) }}%"}
    ]},
    {"group":"switch","name":"US XG 6 PoE","icon":"mdi:switch","state":"sensor.us_xg_6poe_state","update":"update.us_xg_6poe","metrics":[
        {"entity":"sensor.us_xg_6poe_clients","icon":"mdi:account-network","content":"{{ states(entity) }} clients"},
        {"entity":"sensor.us_xg_6poe_uptime","icon":"mdi:timer-outline","content":"{{ relative_time(states(entity) | as_datetime) if states(entity) not in ['unknown', 'unavailable'] else states(entity) }}"},
        {"entity":"sensor.us_xg_6poe_cpu_utilization","icon":"mdi:cpu-64-bit","content":"CPU {{ states(entity) }}%"},
        {"entity":"sensor.us_xg_6poe_memory_utilization","icon":"mdi:memory","content":"RAM {{ states(entity) }}%"},
        {"entity":"sensor.us_xg_6poe_temperature","icon":"mdi:thermometer","content":"{{ states(entity) }}{{ state_attr(entity, 'unit_of_measurement') or '' }}"}
    ]},
    {"group":"switch","name":"USW Enterprise 8 PoE","icon":"mdi:switch","state":"sensor.usw_enterprise_8_poe_state","update":"update.usw_enterprise_8_poe","metrics":[
        {"entity":"sensor.usw_enterprise_8_poe_clients","icon":"mdi:account-network","content":"{{ states(entity) }} clients"},
        {"entity":"sensor.usw_enterprise_8_poe_uptime","icon":"mdi:timer-outline","content":"{{ relative_time(states(entity) | as_datetime) if states(entity) not in ['unknown', 'unavailable'] else states(entity) }}"},
        {"entity":"sensor.usw_enterprise_8_poe_cpu_utilization","icon":"mdi:cpu-64-bit","content":"CPU {{ states(entity) }}%"},
        {"entity":"sensor.usw_enterprise_8_poe_memory_utilization","icon":"mdi:memory","content":"RAM {{ states(entity) }}%"},
        {"entity":"sensor.usw_enterprise_8_poe_temperature","icon":"mdi:thermometer","content":"{{ states(entity) }}{{ state_attr(entity, 'unit_of_measurement') or '' }}"}
    ]},
    {"group":"switch","name":"USW Pro 24 PoE","icon":"mdi:switch","state":"sensor.usw_pro_24_poe_state","update":"update.usw_pro_24_poe","metrics":[
        {"entity":"sensor.usw_pro_24_poe_clients","icon":"mdi:account-network","content":"{{ states(entity) }} clients"},
        {"entity":"sensor.usw_pro_24_poe_uptime","icon":"mdi:timer-outline","content":"{{ relative_time(states(entity) | as_datetime) if states(entity) not in ['unknown', 'unavailable'] else states(entity) }}"},
        {"entity":"sensor.usw_pro_24_poe_cpu_utilization","icon":"mdi:cpu-64-bit","content":"CPU {{ states(entity) }}%"},
        {"entity":"sensor.usw_pro_24_poe_memory_utilization","icon":"mdi:memory","content":"RAM {{ states(entity) }}%"},
        {"entity":"sensor.usw_pro_24_poe_temperature","icon":"mdi:thermometer","content":"{{ states(entity) }}{{ state_attr(entity, 'unit_of_measurement') or '' }}"}
    ]},
    {"group":"switch","name":"USW Pro Aggregation","icon":"mdi:switch","state":"sensor.usw_pro_aggregation_state","update":"update.usw_pro_aggregation","metrics":[
        {"entity":"sensor.usw_pro_aggregation_clients","icon":"mdi:account-network","content":"{{ states(entity) }} clients"},
        {"entity":"sensor.usw_pro_aggregation_uptime","icon":"mdi:timer-outline","content":"{{ relative_time(states(entity) | as_datetime) if states(entity) not in ['unknown', 'unavailable'] else states(entity) }}"},
        {"entity":"sensor.usw_pro_aggregation_cpu_utilization","icon":"mdi:cpu-64-bit","content":"CPU {{ states(entity) }}%"},
        {"entity":"sensor.usw_pro_aggregation_memory_utilization","icon":"mdi:memory","content":"RAM {{ states(entity) }}%"},
        {"entity":"sensor.usw_pro_aggregation_temperature","icon":"mdi:thermometer","content":"{{ states(entity) }}{{ state_attr(entity, 'unit_of_measurement') or '' }}"}
    ]},
    {"group":"other","name":"USP PDU Pro","icon":"mdi:power-socket-us","state":"sensor.usp_pdu_pro_state","update":"update.usp_pdu_pro","metrics":[
        {"entity":"sensor.usp_pdu_pro_clients","icon":"mdi:account-network","content":"{{ states(entity) }} clients"},
        {"entity":"sensor.usp_pdu_pro_uptime","icon":"mdi:timer-outline","content":"{{ relative_time(states(entity) | as_datetime) if states(entity) not in ['unknown', 'unavailable'] else states(entity) }}"},
        {"entity":"sensor.usp_pdu_pro_cpu_utilization","icon":"mdi:cpu-64-bit","content":"CPU {{ states(entity) }}%"},
        {"entity":"sensor.usp_pdu_pro_memory_utilization","icon":"mdi:memory","content":"RAM {{ states(entity) }}%"}
    ]}
]
device_cards = []
for device in devices:
    metric_chips = [{"type":"template","entity":metric["entity"],"icon":metric["icon"],"content":metric["content"],"icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable'] else 'blue' }}","tap_action":{"action":"more-info"}} for metric in device["metrics"]]
    device_cards.append({"group":device["group"],"card":{"type":"custom:stack-in-card","cards":[{"type":"custom:mushroom-template-card","primary":device["name"],"secondary":"{{ states(entity) }}","icon":device["icon"],"entity":device["state"],"tap_action":{"action":"more-info"},"icon_color":"{{ 'red' if states(entity) in ['unknown', 'unavailable', 'disconnected'] else 'green' }}","fill_container":True,"layout":"horizontal"},{"type":"custom:mushroom-chips-card","alignment":"start","chips":metric_chips}]}})
firmware_cards = [{"type":"custom:mushroom-template-card","primary":device["name"],"secondary":"{{ 'Update available' if is_state(entity, 'on') else ('Unavailable' if is_state(entity, 'unavailable') else 'Current') }}","icon":"mdi:update","entity":device["update"],"tap_action":{"action":"more-info"},"icon_color":"{{ 'orange' if is_state(entity, 'on') else ('red' if is_state(entity, 'unavailable') else 'green') }}","layout":"horizontal"} for device in devices]
replacement = {"theme":"Mushroom","title":"Network","path":"network","subview":True,"badges":[],"cards":[
    {"type":"custom:mushroom-title-card","title":"Network","subtitle":"Read-only connectivity and UniFi infrastructure health"},
    {"type":"grid","square":False,"columns":2,"cards":[
        {"type":"tile","entity":"binary_sensor.unifi_dream_machine_wan_status","name":"WAN Status","tap_action":{"action":"more-info"}},
        {"type":"tile","entity":"sensor.hanley_dream_machine_se_state","name":"Gateway State","tap_action":{"action":"more-info"}},
        {"type":"tile","entity":"sensor.unifi_dream_machine_kib_s_received","name":"Download Speed","tap_action":{"action":"more-info"}},
        {"type":"tile","entity":"sensor.unifi_dream_machine_kib_s_sent","name":"Upload Speed","tap_action":{"action":"more-info"}}
    ]},
    {"type":"custom:mushroom-title-card","title":"Gateway"},
    {"type":"grid","square":False,"columns":1,"cards":[item["card"] for item in device_cards if item["group"] == "gateway"]},
    {"type":"custom:mushroom-title-card","title":"Access Points"},
    {"type":"grid","square":False,"columns":1,"cards":[item["card"] for item in device_cards if item["group"] == "ap"]},
    {"type":"custom:mushroom-title-card","title":"Switches"},
    {"type":"grid","square":False,"columns":1,"cards":[item["card"] for item in device_cards if item["group"] == "switch"]},
    {"type":"custom:mushroom-title-card","title":"Other Infrastructure"},
    {"type":"grid","square":False,"columns":1,"cards":[item["card"] for item in device_cards if item["group"] == "other"]},
    {"type":"custom:mushroom-title-card","title":"Firmware","subtitle":"Status only; tap for More Info"},
    {"type":"grid","square":False,"columns":2,"cards":firmware_cards}
]}
matches = [(index, view) for index, view in enumerate(config["views"]) if view.get("path") == target_path]
if len(matches) == 1 and matches[0][1] == expected_current and replacement["path"] == target_path and replacement["subview"] == True:
    config["views"][matches[0][0]] = replacement
```

## Expected result

- Twelve top-level cards with Gateway, Access Points, Switches, Other
  Infrastructure, and Firmware sections
- Thirteen labeled infrastructure device blocks
- Every status header and metric chip opens More Info
- Every firmware card opens More Info and exposes no install action
- No state-changing dashboard action, service, script, automation, port, PoE,
  outlet, power, restart, or reboot control
- One-column device grids preserve readable mobile layouts; the summary and
  firmware grids use two columns

## Verification and rollback

After a separately approved live write:

1. Read back `default/network` with `force_reload: true`.
2. Confirm the exact title, path, `subview`, section order, 13 device blocks,
   entity IDs, and `more-info` actions.
3. Scan recursively for forbidden action values and service/script/automation
   keys.
4. Confirm no unrelated dashboard view changed and all eight Lower Level paths
   remain unique.
5. If the write or read-back differs, stop. Restoring `expected_current` is a
   separate write requiring its own exact approval.

## Implementation receipt

- Proposal commit: `7c194de`
- Proposal branch: `origin/feature/lower-level-dashboard`
- Approved pre-write hash: `4e5c06aefe9337ca`
- Result: `write_committed: true`; `post_write_verified: true`
- Post-write and read-back hash: `bff59e65d79e65ac`
- Read-back: `network` at view index 30; title and path `Network` / `network`;
  `subview: true`; 12 top-level cards; 13 device blocks; 89 entity references
  and 88 unique entity IDs
- Sections: Network, Gateway, Access Points, Switches, Other Infrastructure,
  and Firmware
- Interaction verification: the only action value is `more-info`; no service,
  target, navigation, script, automation, restart, power, PoE, or port-control
  key is present
- Stale-entity verification: the removed legacy gateway and aggregation entity
  IDs are absent
- Home Assistant warning: one unrelated dashboard view lacks a stable path and
  uses a fragile numeric render index; this warning existed before the write
- Rollback source: the literal `expected_current` object above remains usable
  through a separately approved guarded write

## Seamless metric-chip styling amendment

The approved presentation-only amendment copies the established Main Level
chip treatment onto the 13 Network device metric rows. It removes the
individual chip background and shadow, uses the compact 30-pixel chip height,
and changes alignment from `start` to `justify` so available width is shared
evenly. Entity IDs, templates, colors, card order, and More Info actions remain
unchanged.

Verified pre-write state:

- Fresh dashboard hash: `bff59e65d79e65ac`
- Target: `default/network`, view index 30
- Exactly 13 `custom:mushroom-chips-card` metric rows
- All 13 use `alignment: start` and have no `card_mod`
- Metric counts: one row with seven chips, eight rows with four chips, and four
  rows with five chips
- The only configured action value remains `more-info`

Exact proposed write body:

```json
{
  "url_path": "default",
  "config_hash": "bff59e65d79e65ac",
  "python_transform": "<the literal Python transform below>",
  "return_screenshot": false
}
```

```python
target_path = "network"
matches = [view for view in config["views"] if view.get("path") == target_path]
if len(matches) == 1:
    target = matches[0]
    cards = target.get("cards", [])
    groups = [cards[index] for index in [3, 5, 7, 9]] if len(cards) == 12 else []
    stacks = [card for group in groups for card in group.get("cards", [])] if len(groups) == 4 else []
    metric_rows = [stack.get("cards", [])[1] for stack in stacks if stack.get("type") == "custom:stack-in-card" and len(stack.get("cards", [])) == 2 and stack.get("cards", [])[1].get("type") == "custom:mushroom-chips-card"]
    expected_counts = [7, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 4]
    safe = len(metric_rows) == 13 and [len(row.get("chips", [])) for row in metric_rows] == expected_counts and all(row.get("alignment") == "start" and row.get("card_mod") == None for row in metric_rows)
    if safe:
        for row in metric_rows:
            row["alignment"] = "justify"
            row["card_mod"] = {"style":"ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n}\n"}
```

Expected read-back:

- The Network view remains at the same title, path, and card structure.
- All 13 metric rows use `alignment: justify`.
- All 13 metric rows have the exact Main Level-derived `card_mod` variables.
- Every entity, template, color, chip count, and action remains unchanged.
- No state-changing or navigation action is introduced.
