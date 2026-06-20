# Template helper migration — 2026-06-04

Migrated the following former YAML template sensors to UI-managed Home Assistant template helpers via ha-mcp.

## Recreated helper entities

- `sensor.dead_zwave_devices`
- `sensor.date_and_time`
- `sensor.current_electricity_rate`
- `sensor.current_spire_gas_rate`
- `sensor.gas_energy_metric`
- `sensor.water_energy_metric`

## Additional recreated helper entities

- `sensor.water_price_rate`
- `sensor.home_lights`
- `sensor.washer_door_lock`
- `sensor.washer_time_display`
- `sensor.dryer_time_display`
- `sensor.guest_bedroom_fire_tv_source`
- `sensor.living_room_fire_tv_source`

## Intentionally skipped / deferred

- `sensor.current_lights_on`
  - Replaced by the new UI-managed helper `sensor.home_lights` to avoid keeping a duplicate entity with the same purpose.
- `sensor.blank`
  - Placeholder-style empty template; not recreated as a helper.
- `sensor.spire_ft3_price_rate`
  - Existing entity already present in Home Assistant but currently stale/`unavailable`; not recreated in this pass.
- `mini_washer_*`
  - Deferred because the expected source entities were not verified during discovery.
- `history_stats` sensors
  - Kept out of this template-helper pass because they are not template helpers.
- `time_date` sensors
  - Integration-managed; not part of template-helper migration.

## Original source templates

### Dead ZWave Devices

```yaml
- sensor:
    - name: "Dead ZWave Devices"
      unique_id: dead_zwave_devices
      unit_of_measurement: entities
      state: >
        {% if state_attr('sensor.dead_zwave_devices','entity_id') != none %}
          {{ state_attr('sensor.dead_zwave_devices','entity_id') | count }}
        {% else %}
          {{ 0 }}
        {% endif %}
      attributes:
        entity_id: >
          {% set exclude_filter = ['sensor.700_series_based_controller_node_status'] %}
          {{
            expand(integration_entities('Z-Wave JS') )
            | rejectattr("entity_id", "in", exclude_filter)
            | selectattr("entity_id", "search", "node_status")
            | selectattr('state', 'in', 'dead, unavailable, unknown')
            | map(attribute="object_id")
            | map('regex_replace', find='(.*)_node_status', replace='button.\\1_ping', ignorecase=False)
            | list
          }}
```

### Date and time

```yaml
- sensor:
    - name: "Date and time"
      state: "{{ as_timestamp(states('sensor.date_time_iso')) | timestamp_custom('%A %B %-d, %I:%M %p') }}"
      icon: "mdi:calendar-clock"
```

### Current Electricity Rate

```yaml
- sensor:
    - name: "Current Electricity Rate"
      unit_of_measurement: "USD/kWh"
      device_class: monetary
      state: >
        {% set timenow = states('sensor.time').split(':') -%}
        {% set hour = timenow[0] | int(0) -%}
        {% set today = states('sensor.date').split('-') -%}
        {% set month = today[1]|int(0) -%}
        {% if month in [9, 10, 11, 12, 1, 2, 3, 4, 5] -%}
          {% if hour in [16, 17, 18, 19] %}
            0.21629
          {%- elif hour in [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23] -%}
            0.08727
          {%- elif hour in [0, 1, 2, 3, 4, 5] -%}
            0.03667
          {%- endif %}
        {%- elif month in [6, 7, 8] -%}
          {%- if hour in [16, 17, 18, 19] -%}
            0.26577
          {%- elif hour in [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23] -%}
            0.08859
          {%- elif hour in [0, 1, 2, 3, 4, 5] -%}
            0.04429
          {%- endif -%}
        {%- endif -%}
```

### Current Spire Gas Rate

```yaml
- sensor:
    - name: "Current Spire Gas Rate"
      unique_id: current_spire_gas_rate
      unit_of_measurement: "USD/CCF"
      device_class: monetary
      state: >
        {% set today = states('sensor.date').split('-') -%}
        {% set month = today[1]|int(0) -%}
        {% set current_ccf = states('sensor.spire_gas') | int -%}
        {% if month in [11, 12, 1, 2, 3, 4] %}
          {{states('sensor.spire_purchased_gas_adjustment') | float + states('sensor.spire_winter_rate') | float(0) -}}
        {%- elif month in [5, 6, 7, 8, 9, 10] -%}
          {% if current_ccf < 50 %}
          {{states('sensor.spire_purchased_gas_adjustment') | float(0) + states('sensor.spire_summer_rate_tier_1') | float(0) -}}
          {% else %}
            {{states('sensor.spire_purchased_gas_adjustment') | float(0) + states('sensor.spire_summer_rate_tier_2') | float(0) -}}
          {% endif %}
        {%- endif %}
```

### Gas Energy Metric

```yaml
- sensor:
    - name: Gas Energy Metric
      unique_id: gas_energy_metric
      state: >-
        {{ states('sensor.spire_gas_ft3_mqtt_rtlamr')}}
      icon: mdi:fire
      unit_of_measurement: "ft³"
      state_class: "total_increasing"
      device_class: "gas"
```

### Water Energy Metric

```yaml
- sensor:
    - name: Water Energy Metric
      unique_id: water_energy_metric
      state: >-
        {{ states('sensor.city_of_lees_ummit_water_gal_mqtt_rtlamr')}}
      icon: mdi:water-pump
      unit_of_measurement: "gal"
      state_class: "total_increasing"
      device_class: "water"
```

## Notes

- `Date and time` was recreated because existing references still depend on `sensor.date_and_time`.
- The recreated helper version of `Date and time` includes a guard for `unknown`/`unavailable` source values.
- `Dead ZWave Devices` was successfully recreated as a UI-managed template helper including its custom `entity_id` attribute template.
- `Water Price Rate` was recreated and verified with state `0.00481`.
- The former `current_lights_on` YAML sensor was not recreated under the same entity ID; a new UI-managed helper `sensor.home_lights` was created instead by user choice to avoid a duplicate legacy-style entity.
- `Washer Door Lock`, `Washer Time Display`, `Dryer Time Display`, `Guest Bedroom Fire TV Source`, and `Living Room Fire TV Source` were recreated and verified.