# Georgetown-HAAS Lower Level Pre-Change Snapshot

## Capture Metadata

- Capture date: 2026-08-24.
- Source: approved, read-only Home Assistant dashboard-view, resource, floor/area, and area-entity inventory reads.
- Dashboard is UI-managed; this file is a non-deployable planning and rollback-reference artifact.
- Sensitive dashboard content is excluded. No credentials, tokens, cookies, private URLs, calendar/event content, or personal device-tracker/image records are persisted.

## Dashboard Identity and Config Hash

- Dashboard URL path: `default`.
- Config hash returned consistently by the scoped view reads: `8bd951df2315db64`.
- The original broad dashboard read was unsafe because it returned sensitive configuration. Its body was discarded, so dashboard mode and a complete ordered view inventory are not independently retained here.

## Ordered View Paths

The safe scoped reads verified only these paths and indices:

| Path | View index | Subview | Top-level cards |
| --- | ---: | --- | ---: |
| `living-areas` | 2 | yes | 3 |
| `utility_room` | 15 | no | 5 |
| `server-room` | 16 | no | 0 |
| `office-of-mike` | 18 | yes | 5 |

Complete path ordering and collision checks for the four proposed new paths require a separately approved safe dashboard-path inventory before any dashboard write.

## Proposed Path Availability

Fresh approved reads returned explicit not-found semantics for each proposed path below. They are available for creation only after the separate dashboard-write approval and fresh conflict check required by the rollout plan.

| Proposed path | Read result |
| --- | --- |
| `basement-entertainment` | Not found |
| `basement-bathroom` | Not found |
| `network` | Not found |
| `home-assistant` | Not found |

## Complete Sanitized Dashboard Representation

The broad dashboard response remains unavailable because it contained sensitive configuration. The following four literal view objects were freshly captured through approved scoped reads, recursively sanitized, and retained for view-scoped rollback. They preserve operational entity IDs and adjudicated project names while excluding credential-like values and URLs.

### `living-areas`

- Fresh config hash: `8bd951df2315db64`
- View index: 2

```json
{
  "theme": "Mushroom",
  "title": "Areas",
  "path": "living-areas",
  "subview": true,
  "badges": [],
  "cards": [
    {
      "square": false,
      "columns": 1,
      "type": "grid",
      "cards": [
        {
          "type": "custom:mushroom-title-card",
          "title": "Main Level"
        },
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "custom:stack-in-card",
              "cards": [
                {
                  "type": "horizontal-stack",
                  "cards": [
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "conditional",
                          "conditions": [
                            {
                              "entity": "binary_sensor.front_yard_cameras_motion",
                              "state": "on"
                            }
                          ],
                          "chip": {
                            "type": "template",
                            "entity": "binary_sensor.front_yard_cameras_motion",
                            "icon_color": "#9797db",
                            "icon": "mdi:motion-sensor",
                            "tap_action": {
                              "action": "more-info"
                            },
                            "alignment": "start",
                            "card_mod": {
                              "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n}\n"
                            }
                          }
                        }
                      ]
                    },
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "entity",
                          "entity": "sensor.front_yard_energy_meter",
                          "icon_color": "yellow"
                        }
                      ],
                      "alignment": "end",
                      "card_mod": {
                        "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n}\n"
                      }
                    }
                  ]
                },
                {
                  "type": "custom:mushroom-template-card",
                  "primary": "Front Yard",
                  "secondary": "{{ states('sensor.outside_temperature') | round(0) }} °F",
                  "icon": "mdi:flower-outline",
                  "entity": "light.front_yard_lights",
                  "tap_action": {
                    "action": "navigate",
                    "navigation_path": "frontyard"
                  },
                  "hold_action": {
                    "action": "more-info"
                  },
                  "icon_color": "{{ 'orange' if is_state(entity, 'on') else 'disabled' }}",
                  "fill_container": true,
                  "layout": "horizontal",
                  "multiline_secondary": false,
                  "card_mod": {
                    "style": "ha-card {\n padding-top: 0 !important;\n padding-bottom: 0 !important;\n}\n"
                  }
                },
                {
                  "type": "custom:mushroom-chips-card",
                  "chips": [
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "lock.front_door_lock",
                          "state": "unlocked"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "lock.front_door_lock",
                        "icon_color": "red",
                        "icon": "{{\"mdi:lock\" if is_state(entity, 'locked') else \"mdi:lock-open-alert\" }}",
                        "card_mod": {
                          "style": "ha-card {\n  animation: blink 5s linear infinite;\n}\n@keyframes blink {\n  50% {opacity: 0;}\n}\n"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "binary_sensor.front_door",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "binary_sensor.front_door",
                        "icon_color": "red",
                        "icon": "{{\"mdi:door\" if is_state(entity, 'off') else \"mdi:door-open\" }}",
                        "card_mod": {
                          "style": "ha-card {\n  animation: blink 5s linear infinite;\n}\n@keyframes blink {\n  50% {opacity: 0;}\n} \n"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "binary_sensor.front_sprinklers",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "binary_sensor.front_sprinklers",
                        "icon_color": "#0202cc",
                        "tap_action": {
                          "action": "more-info"
                        },
                        "icon": "{{\"mdi:water-off\" if is_state(entity, 'off') else \"mdi:water\" }}",
                        "card_mod": {
                          "style": "ha-card {\n  animation: blink 5s linear infinite;\n}\n@keyframes blink {\n  50% {opacity: 0;}\n} \n"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "light.front_yard_lights",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "light.front_yard_lights",
                        "icon": "mdi:lightbulb",
                        "icon_color": "#e68e02",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "switch.front_outdoor_outlet",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "switch.front_outdoor_outlet",
                        "icon": "mdi:power-socket-us",
                        "icon_color": "green",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    }
                  ],
                  "alignment": "end",
                  "card_mod": {
                    "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n} \n"
                  }
                }
              ],
              "card_mod": {
                "style": "ha-card {\n --chip-height: 30px;\n background: var(--ha-card-background, var(--card-background-color, white) );\n {% if is_state('light.front_yard_lights', 'on') %}\n     background: rgba(255, 152, 0, 0.1) !important;\n{% endif %} \nheight: 115px;\n--vertical-stack-card-gap: 1px;\n}\nelement.style {\n  background: white !important;\n}\n"
              }
            },
            {
              "type": "custom:stack-in-card",
              "cards": [
                {
                  "type": "horizontal-stack",
                  "cards": [
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "conditional",
                          "conditions": [
                            {
                              "entity": "binary_sensor.backyard_cameras_motion",
                              "state": "on"
                            }
                          ],
                          "chip": {
                            "type": "template",
                            "entity": "binary_sensor.backyard_cameras_motion",
                            "icon_color": "#9797db",
                            "icon": "mdi:motion-sensor",
                            "tap_action": {
                              "action": "more-info"
                            },
                            "alignment": "start",
                            "card_mod": {
                              "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n}\n"
                            }
                          }
                        }
                      ]
                    },
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "entity",
                          "entity": "sensor.energy_meter_backyard",
                          "icon_color": "yellow"
                        }
                      ],
                      "alignment": "end",
                      "card_mod": {
                        "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n}\n"
                      }
                    }
                  ]
                },
                {
                  "type": "custom:mushroom-template-card",
                  "primary": "Back Yard",
                  "secondary": "{{ states('sensor.outside_temperature') | round(0) }} °F",
                  "icon": "mdi:grass",
                  "entity": "light.backyard_lights",
                  "tap_action": {
                    "action": "navigate",
                    "navigation_path": "backyard"
                  },
                  "hold_action": {
                    "action": "more-info"
                  },
                  "icon_color": "{{ 'orange' if is_state(entity, 'on') else 'disabled' }}",
                  "fill_container": true,
                  "layout": "horizontal",
                  "multiline_secondary": false,
                  "card_mod": {
                    "style": "ha-card {\n padding-top: 0 !important;\n padding-bottom: 0 !important;\n}\n"
                  }
                },
                {
                  "type": "custom:mushroom-chips-card",
                  "chips": [
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "lock.patio_door_lock",
                          "state": "unlocked"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "lock.patio_door_lock",
                        "icon_color": "red",
                        "icon": "{{\"mdi:lock\" if is_state(entity, 'locked') else \"mdi:lock-open-alert\" }}",
                        "card_mod": {
                          "style": "ha-card {\n  animation: blink 5s linear infinite;\n}\n@keyframes blink {\n  50% {opacity: 0;}\n}\n"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "binary_sensor.side_door",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "binary_sensor.side_door",
                        "icon_color": "red",
                        "icon": "{{\"mdi:door\" if is_state(entity, 'off') else \"mdi:door-open\" }}",
                        "card_mod": {
                          "style": "ha-card {\n  animation: blink 5s linear infinite;\n}\n@keyframes blink {\n  50% {opacity: 0;}\n} \n"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "binary_sensor.back_sprinklers",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "binary_sensor.back_sprinklers",
                        "icon_color": "#0202cc",
                        "tap_action": {
                          "action": "more-info"
                        },
                        "icon": "{{\"mdi:water-off\" if is_state(entity, 'off') else \"mdi:water\" }}",
                        "card_mod": {
                          "style": "ha-card {\n  animation: blink 5s linear infinite;\n}\n@keyframes blink {\n  50% {opacity: 0;}\n} \n"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "light.backyard_lights",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "light.backyard_lights",
                        "icon": "mdi:lightbulb",
                        "icon_color": "#e68e02",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "fan.patio_fan",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "fan.patio_fan",
                        "icon": "mdi:fan",
                        "tap_action": {
                          "action": "more-info"
                        },
                        "icon_color": "green"
                      }
                    }
                  ],
                  "alignment": "end",
                  "card_mod": {
                    "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n} \n"
                  }
                }
              ],
              "card_mod": {
                "style": "ha-card {\n background: var(--ha-card-background, var(--card-background-color, white) );\n {% if is_state('light.back_yard_lights', 'on') %}\n     background: rgba(255, 152, 0, 0.1) !important;\n{% endif %} \nheight: 115px;\n--vertical-stack-card-gap: 1px;\n}\nelement.style {\n  background: white !important;\n}\n"
              }
            }
          ],
          "card_mod": {
            "style": "ha-card {\n  background: var(--ha-card-background, var(--card-background-color, white) );\n  {% if is_state('light.backyard_lights', 'on') %}\n     background: rgba(255, 152, 0, 0.1) !important;\n  {% endif %} \nheight: 115px;\n  }\nelement.style {\n  background: white !important;\n}\n"
          }
        },
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "custom:stack-in-card",
              "cards": [
                {
                  "type": "horizontal-stack",
                  "cards": [
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "conditional",
                          "conditions": [
                            {
                              "entity": "binary_sensor.ecobee_thermostat_occupancy",
                              "state": "on"
                            }
                          ],
                          "chip": {
                            "type": "template",
                            "entity": "binary_sensor.ecobee_thermostat_occupancy",
                            "icon_color": "#9797db",
                            "icon": "mdi:motion-sensor",
                            "tap_action": {
                              "action": "more-info"
                            },
                            "alignment": "start",
                            "card_mod": {
                              "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n}\n"
                            }
                          }
                        }
                      ]
                    },
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "entity",
                          "entity": "sensor.living_room_energy_meter",
                          "icon_color": "yellow"
                        }
                      ],
                      "alignment": "end",
                      "card_mod": {
                        "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n}\n"
                      }
                    }
                  ]
                },
                {
                  "type": "custom:mushroom-template-card",
                  "primary": "Living Room",
                  "secondary": "{{ states('sensor.living_room_temperature') | round(0) }} °F",
                  "icon": "mdi:fireplace",
                  "entity": "light.living_room_lights",
                  "tap_action": {
                    "action": "navigate",
                    "navigation_path": "living-room"
                  },
                  "hold_action": {
                    "action": "more-info"
                  },
                  "icon_color": "{{ 'orange' if is_state(entity, 'on') else 'disabled' }}",
                  "fill_container": true,
                  "layout": "horizontal",
                  "multiline_secondary": false,
                  "card_mod": {
                    "style": "ha-card {\n padding-top: 0 !important;\n padding-bottom: 0 !important;\n}\n"
                  }
                },
                {
                  "type": "custom:mushroom-chips-card",
                  "chips": [
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "light.entryway_light",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "light.entryway_light",
                        "icon": "mdi:lightbulb",
                        "icon_color": "#e68e02",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "light.living_room_light",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "light.living_room_light",
                        "icon": "mdi:lightbulb",
                        "icon_color": "#e68e02",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "light.family_room_light",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "light.family_room_light",
                        "icon": "mdi:lightbulb",
                        "icon_color": "#e68e02",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "fan.living_room_tower_fan",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "fan.living_room_tower_fan",
                        "icon": "mdi:fan",
                        "tap_action": {
                          "action": "more-info"
                        },
                        "icon_color": "green"
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "switch.living_room_entertainment_system",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "switch.living_room_entertainment_system",
                        "icon_color": "blue",
                        "icon": "mdi:television",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    }
                  ],
                  "alignment": "end",
                  "card_mod": {
                    "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n} \n"
                  }
                }
              ],
              "card_mod": {
                "style": "ha-card {\n background: var(--ha-card-background, var(--card-background-color, white) );\n {% if is_state('light.living_room_lights', 'on') %}\n     background: rgba(255, 152, 0, 0.1) !important;\n{% endif %} \nheight: 115px;\n--vertical-stack-card-gap: 1px;\n}\nelement.style {\n  background: white !important;\n}\n.container {\n padding-bottom: 5px; !important\n}\n"
              }
            },
            {
              "type": "custom:stack-in-card",
              "cards": [
                {
                  "type": "custom:mushroom-chips-card",
                  "chips": [
                    {
                      "type": "entity",
                      "entity": "sensor.kitchen_energy_meters",
                      "icon_color": "yellow"
                    }
                  ],
                  "alignment": "end",
                  "card_mod": {
                    "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n}\n"
                  }
                },
                {
                  "type": "custom:mushroom-template-card",
                  "primary": "Kitchen",
                  "secondary": "{{ states('sensor.pantry_motion_air_temperature') | round(0) }} °F",
                  "icon": "mdi:silverware-fork-knife",
                  "entity": "light.kitchen_lights",
                  "tap_action": {
                    "action": "navigate",
                    "navigation_path": "kitchen"
                  },
                  "hold_action": {
                    "action": "more-info"
                  },
                  "icon_color": "{{ 'orange' if is_state(entity, 'on') else 'disabled' }}",
                  "fill_container": true,
                  "layout": "horizontal",
                  "multiline_secondary": false,
                  "card_mod": {
                    "style": "ha-card {\n padding-top: 0 !important;\n padding-bottom: 0 !important;\n}\n"
                  }
                },
                {
                  "type": "custom:mushroom-chips-card",
                  "chips": [
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "binary_sensor.refrigerator_door_open",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "icon_color": "red",
                        "icon": "mdi:fridge-variant-alert",
                        "card_mod": {
                          "style": "ha-card {\n  animation: blink 5s linear infinite;\n}\n@keyframes blink {\n  50% {opacity: 0;}\n}  \n"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "light.kitchen_main_light",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "light.kitchen_main_light",
                        "icon": "mdi:lightbulb",
                        "icon_color": "#e68e02",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "light.kitchen_island_light",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "light.kitchen_island_light",
                        "icon_color": "#e68e02",
                        "icon": "mdi:ceiling-light-multiple",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "light.dinning_room_light",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "light.dinning_room_light",
                        "tap_action": {
                          "action": "more-info"
                        },
                        "icon_color": "#e68e02",
                        "icon": "mdi:table-furniture"
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "light.mudroom_light",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "light.mudroom_light",
                        "icon_color": "#e68e02",
                        "icon": "mdi:coat-rack",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    }
                  ],
                  "alignment": "end",
                  "card_mod": {
                    "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n} \n"
                  }
                }
              ],
              "card_mod": {
                "style": "ha-card {\n background: var(--ha-card-background, var(--card-background-color, white) );\n {% if is_state('light.kitchen_lights', 'on') %}\n     background: rgba(255, 152, 0, 0.1) !important;\n{% endif %} \nheight: 115px;\n--vertical-stack-card-gap: 1px;\n}\nelement.style {\n  background: white !important;\n}\n"
              }
            }
          ]
        },
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "custom:stack-in-card",
              "cards": [
                {
                  "type": "horizontal-stack",
                  "cards": [
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "conditional",
                          "conditions": [
                            {
                              "entity": "binary_sensor.playroom_ecobee_sensor_occupancy",
                              "state": "on"
                            }
                          ],
                          "chip": {
                            "type": "template",
                            "entity": "binary_sensor.playroom_ecobee_sensor_occupancy",
                            "icon_color": "#9797db",
                            "icon": "mdi:motion-sensor",
                            "tap_action": {
                              "action": "more-info"
                            },
                            "alignment": "start",
                            "card_mod": {
                              "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n}\n"
                            }
                          }
                        }
                      ]
                    },
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "entity",
                          "entity": "sensor.playroom_energy_meter",
                          "icon_color": "yellow"
                        }
                      ],
                      "alignment": "end",
                      "card_mod": {
                        "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n}\n"
                      }
                    }
                  ]
                },
                {
                  "type": "custom:mushroom-template-card",
                  "primary": "Playroom",
                  "secondary": "{{ states('sensor.playroom_ecobee_sensor_temperature') | round(0) }} °F",
                  "icon": "mdi:baseball-bat",
                  "entity": "light.playroom_lights",
                  "tap_action": {
                    "action": "navigate",
                    "navigation_path": "playroom"
                  },
                  "hold_action": {
                    "action": "more-info"
                  },
                  "icon_color": "{{ 'orange' if is_state(entity, 'on') else 'disabled' }}",
                  "fill_container": true,
                  "layout": "horizontal",
                  "multiline_secondary": false,
                  "card_mod": {
                    "style": "ha-card {\n padding-top: 0 !important;\n padding-bottom: 0 !important;\n}\n"
                  }
                },
                {
                  "type": "custom:mushroom-chips-card",
                  "chips": [
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "light.playroom_lights",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "light.playroom_lights",
                        "icon": "mdi:lightbulb",
                        "icon_color": "#e68e02",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "fan.playroom_fan",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "fan.playroom_fan",
                        "icon": "mdi:fan",
                        "tap_action": {
                          "action": "more-info"
                        },
                        "icon_color": "green"
                      }
                    }
                  ],
                  "alignment": "end",
                  "card_mod": {
                    "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n} \n"
                  }
                }
              ],
              "card_mod": {
                "style": "ha-card {\n background: var(--ha-card-background, var(--card-background-color, white) );\n {% if is_state('light.playroom_lights', 'on') %}\n     background: rgba(255, 152, 0, 0.1) !important;\n{% endif %} \nheight: 115px;\n--vertical-stack-card-gap: 1px;\n}\nelement.style {\n  background: white !important;\n}\n"
              }
            },
            {
              "type": "custom:stack-in-card",
              "cards": [
                {
                  "type": "horizontal-stack",
                  "cards": [
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "conditional",
                          "conditions": [
                            {
                              "entity": "binary_sensor.garage_motion",
                              "state": "on"
                            }
                          ],
                          "chip": {
                            "type": "template",
                            "entity": "binary_sensor.garage_motion",
                            "icon_color": "#9797db",
                            "icon": "mdi:motion-sensor",
                            "tap_action": {
                              "action": "more-info"
                            },
                            "alignment": "start",
                            "card_mod": {
                              "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n}\n"
                            }
                          }
                        }
                      ]
                    },
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "entity",
                          "entity": "sensor.energy_meter_garage",
                          "icon_color": "yellow"
                        }
                      ],
                      "alignment": "end",
                      "card_mod": {
                        "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n}\n"
                      }
                    }
                  ]
                },
                {
                  "type": "custom:mushroom-template-card",
                  "primary": "Garage",
                  "secondary": "{{ states('sensor.garage_govee_sensor_temperature') | round(0) }} °F",
                  "icon": "mdi:garage",
                  "entity": "light.garage_lights",
                  "tap_action": {
                    "action": "navigate",
                    "navigation_path": "garage"
                  },
                  "hold_action": {
                    "action": "more-info"
                  },
                  "icon_color": "{{ 'orange' if is_state(entity, 'on') else 'disabled' }}",
                  "fill_container": true,
                  "layout": "horizontal",
                  "multiline_secondary": false,
                  "card_mod": {
                    "style": "ha-card {\n padding-top: 0 !important;\n padding-bottom: 0 !important;\n}\n"
                  }
                },
                {
                  "type": "custom:mushroom-chips-card",
                  "chips": [
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "cover.main_garage_door",
                          "state_not": "closed"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "cover.main_garage_door",
                        "icon_color": "red",
                        "icon": "{{\"mdi:lock\" if is_state(entity, 'closed') else \"mdi:garage-alert-variant\" }}",
                        "card_mod": {
                          "style": "ha-card {\n  animation: blink 5s linear infinite;\n}\n@keyframes blink {\n  50% {opacity: 0;}\n}\n"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "cover.shop_garage_door",
                          "state_not": "closed"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "cover.shop_garage_door",
                        "icon_color": "red",
                        "icon": "{{\"mdi:lock\" if is_state(entity, 'closed') else \"mdi:garage-alert\" }}",
                        "card_mod": {
                          "style": "ha-card {\n  animation: blink 5s linear infinite;\n}\n@keyframes blink {\n  50% {opacity: 0;}\n}\n"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "light.garage_light",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "light.garage_light",
                        "icon": "mdi:lightbulb",
                        "icon_color": "#e68e02",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "switch.shop_vac",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "switch.shop_vac",
                        "icon": "mdi:vacuum",
                        "icon_color": "green",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    }
                  ],
                  "alignment": "end",
                  "card_mod": {
                    "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n  --chip-height: 30px;\n} \n"
                  }
                }
              ],
              "card_mod": {
                "style": "ha-card {\n background: var(--ha-card-background, var(--card-background-color, white) );\n {% if is_state('light.garage_lights', 'on') %}\n     background: rgba(255, 152, 0, 0.1) !important;\n{% endif %} \nheight: 115px;\n--vertical-stack-card-gap: 1px;\n}\nelement.style {\n  background: white !important;\n}\n"
              }
            }
          ]
        },
        {
          "type": "custom:popup-card",
          "entity": "light.kitchen_lights",
          "title": "Kitchen Lights",
          "dismissable": true,
          "card": {
            "type": "custom:auto-entities",
            "filter": {
              "include": [
                {
                  "entity_id": "light.kitchen_lights"
                },
                {
                  "group": "light.kitchen_lights"
                }
              ],
              "exclude": []
            },
            "card": {
              "type": "entities"
            },
            "sort": {
              "method": "friendly_name"
            }
          }
        },
        {
          "type": "custom:popup-card",
          "entity": "light.living_room_lights",
          "title": "Living Room Lights",
          "dismissable": true,
          "card": {
            "type": "custom:auto-entities",
            "filter": {
              "include": [
                {
                  "entity_id": "light.living_room_lights"
                },
                {
                  "group": "light.living_room_lights"
                }
              ],
              "exclude": []
            },
            "card": {
              "type": "entities"
            },
            "sort": {
              "method": "friendly_name"
            }
          }
        },
        {
          "type": "custom:popup-card",
          "entity": "light.playroom_lights",
          "title": "Playroom Lights",
          "dismissable": true,
          "card": {
            "type": "custom:auto-entities",
            "filter": {
              "include": [
                {
                  "entity_id": "light.playroom_lights"
                },
                {
                  "group": "light.playroom_lights"
                }
              ],
              "exclude": []
            },
            "card": {
              "type": "entities"
            },
            "sort": {
              "method": "friendly_name"
            }
          }
        },
        {
          "type": "custom:popup-card",
          "entity": "light.backyard_lights",
          "title": "Backyard Lights",
          "dismissable": true,
          "card": {
            "type": "custom:auto-entities",
            "card": {
              "type": "entities"
            },
            "filter": {
              "include": [
                {
                  "entity_id": "light.backyard_lights"
                },
                {
                  "group": "light.backyard_lights"
                }
              ],
              "exclude": []
            },
            "sort": {
              "method": "friendly_name"
            }
          }
        },
        {
          "type": "custom:popup-card",
          "entity": "light.garage_lights",
          "title": "Garage Lights",
          "dismissable": true,
          "card": {
            "type": "custom:auto-entities",
            "card": {
              "type": "entities"
            },
            "filter": {
              "include": [
                {
                  "entity_id": "light.garage_lights"
                },
                {
                  "group": "light.garage_lights"
                }
              ],
              "exclude": []
            },
            "sort": {
              "method": "friendly_name"
            }
          }
        }
      ]
    },
    {
      "square": false,
      "columns": 1,
      "type": "grid",
      "cards": [
        {
          "type": "custom:mushroom-title-card",
          "title": "Lower Level"
        },
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "custom:vertical-stack-in-card",
              "cards": [
                {
                  "type": "custom:mushroom-template-card",
                  "primary": "Utility Room",
                  "secondary": "Landing",
                  "icon": "mdi:door",
                  "layout": "horizontal",
                  "multiline_secondary": false,
                  "tap_action": {
                    "action": "navigate",
                    "navigation_path": "utility_room"
                  },
                  "icon_color": "deep-purple",
                  "hold_action": {
                    "action": "none"
                  },
                  "double_tap_action": {
                    "action": "none"
                  },
                  "style": ":host([dark-mode]) {\n  background: rgba(var(--rgb-primary-background-color), 0.2);\n} \n:host {\n  background: rgba(var(--rgb-primary-text-color), 0.025);\n} \n"
                },
                {
                  "type": "custom:mushroom-chips-card",
                  "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n}\n",
                  "alignment": "end",
                  "chips": [
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "light.foyer_lights",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "entity",
                        "entity": "light.foyer_lights",
                        "icon_color": "amber",
                        "tap_action": {
                          "action": "call-service",
                          "service": "light.turn_off",
                          "service_data": {},
                          "target": {
                            "entity_id": "light.foyer_lights"
                          }
                        },
                        "content_info": "none",
                        "icon": "mdi:lightbulb"
                      }
                    },
                    {
                      "type": "template",
                      "entity": "lock.door_lock_2",
                      "icon": "{% set state=states(entity) %}\n{% if state=='locked' %}\nmdi:lock\n{% elif state=='unlocked' %}\nmdi:lock-open-variant\n{% else %}\ngrey\n{% endif %}",
                      "tap_action": {
                        "action": "more-info"
                      },
                      "icon_color": "{% set state=states(entity) %}\n{% if state=='locked' %}\ngreen\n{% elif state=='unlocked' %}\nred\n{% else %}\ngrey\n{% endif %}"
                    },
                    {
                      "type": "template",
                      "entity": "sensor.front_door_open",
                      "icon": "{% set state=states(entity) %}\n{% if state=='Open' %}\nmdi:door-open\n{% elif state=='Closed' %}\nmdi:door-closed\n{% else %}\nmdi:door\n{% endif %}",
                      "tap_action": {
                        "action": "more-info"
                      },
                      "icon_color": "{% set state=states(entity) %}\n{% if state=='Open' %}\nred\n{% elif state=='Closed' %}\ngreen\n{% else %}\ngrey\n{% endif %}"
                    }
                  ]
                }
              ],
              "style": "element.style {\n  font-weight: 700;\n}\nha-card {\n  height: 102px;\n}\n:host {\n {% if is_state('light.foyer_lights', 'on') %}\n     var(--card-background-color, rgba(255, 152, 0, 0.1));\n  {% endif %}\n}\n"
            }
          ]
        },
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "custom:stack-in-card",
              "cards": [
                {
                  "type": "horizontal-stack",
                  "cards": [
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "conditional",
                          "conditions": [
                            {
                              "entity": "binary_sensor.office_of_mike_ecobee_sensor_occupancy",
                              "state": "on"
                            }
                          ],
                          "chip": {
                            "type": "template",
                            "entity": "binary_sensor.office_of_mike_ecobee_sensor_occupancy",
                            "icon_color": "#9797db",
                            "icon": "mdi:motion-sensor",
                            "tap_action": {
                              "action": "more-info"
                            },
                            "alignment": "start",
                            "card_mod": null,
                            "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n}\n"
                          }
                        }
                      ]
                    },
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "entity",
                          "entity": "sensor.mike_s_office_energy_meter",
                          "icon_color": "yellow"
                        }
                      ],
                      "alignment": "end",
                      "card_mod": {
                        "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n}\n"
                      }
                    }
                  ]
                },
                {
                  "type": "custom:mushroom-template-card",
                  "primary": "Mike's Office",
                  "secondary": "{{ states('sensor.office_of_mike_ecobee_sensor_temperature') | round(0) }} °F",
                  "icon": "mdi:desktop-tower-monitor",
                  "entity": "light.office_of_mike_light",
                  "tap_action": {
                    "action": "navigate",
                    "navigation_path": "office-of-mike"
                  },
                  "hold_action": {
                    "action": "more-info"
                  },
                  "icon_color": "{{ 'orange' if is_state(entity, 'on') else 'disabled' }}",
                  "fill_container": true,
                  "layout": "horizontal",
                  "multiline_secondary": false,
                  "card_mod": {
                    "style": "ha-card {\n padding-top: 0 !important;\n padding-bottom: 0 !important;\n}\n"
                  }
                },
                {
                  "type": "custom:mushroom-chips-card",
                  "chips": [
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "light.office_of_mike_light",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "light.office_of_mike_light",
                        "icon": "mdi:lightbulb",
                        "icon_color": "#e68e02",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "fan.office_of_mike_fan",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "fan.office_of_mike_fan",
                        "icon": "mdi:fan",
                        "tap_action": {
                          "action": "more-info"
                        },
                        "icon_color": "#7dc2fa"
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "binary_sensor.office_of_mike_tv",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "switch.samsung_tv",
                        "icon_color": "blue",
                        "icon": "mdi:television",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    }
                  ],
                  "alignment": "end",
                  "card_mod": {
                    "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n} \n"
                  }
                }
              ],
              "card_mod": {
                "style": "ha-card {\n background: var(--ha-card-background, var(--card-background-color, white) );\n {% if is_state('light.office_of_mike_light', 'on') %}\n     background: rgba(255, 152, 0, 0.1) !important;\n{% endif %} \nheight: 110px;\n}\nelement.style {\n  background: white !important;\n}\n"
              }
            },
            {
              "type": "custom:gap-card"
            }
          ]
        }
      ]
    },
    {
      "square": false,
      "columns": 1,
      "type": "grid",
      "cards": [
        {
          "type": "custom:mushroom-title-card",
          "title": "Upper Level "
        },
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "custom:stack-in-card",
              "cards": [
                {
                  "type": "horizontal-stack",
                  "cards": [
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "conditional",
                          "conditions": [
                            {
                              "entity": "binary_sensor.master_bedroom_ecobee_sensor_occupancy",
                              "state": "on"
                            }
                          ],
                          "chip": {
                            "type": "template",
                            "entity": "binary_sensor.master_bedroom_ecobee_sensor_occupancy",
                            "icon_color": "#9797db",
                            "icon": "mdi:motion-sensor",
                            "tap_action": {
                              "action": "more-info"
                            },
                            "alignment": "start",
                            "card_mod": {
                              "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n}\n"
                            }
                          }
                        }
                      ]
                    },
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "entity",
                          "entity": "sensor.energy_meter_master_bedroom",
                          "icon_color": "yellow"
                        }
                      ],
                      "alignment": "end",
                      "card_mod": {
                        "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n}\n"
                      }
                    }
                  ]
                },
                {
                  "type": "custom:mushroom-template-card",
                  "primary": "Master Bedroom",
                  "secondary": "{{ states('sensor.master_bedroom_temperature') | round(0) }} °F",
                  "icon": "mdi:bed-king",
                  "entity": "light.master_bathroom_light",
                  "tap_action": {
                    "action": "navigate",
                    "navigation_path": "master-bedroom"
                  },
                  "hold_action": {
                    "action": "more-info"
                  },
                  "icon_color": "{{ 'orange' if is_state(entity, 'on') else 'disabled' }}",
                  "fill_container": true,
                  "layout": "horizontal",
                  "multiline_secondary": false,
                  "card_mod": {
                    "style": "ha-card {\n padding-top: 0 !important;\n padding-bottom: 0 !important;\n}\n"
                  }
                },
                {
                  "type": "custom:mushroom-chips-card",
                  "chips": [
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "fan.master_bedroom_fan",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "fan.master_bedroom_fan",
                        "icon": "mdi:fan",
                        "tap_action": {
                          "action": "more-info"
                        },
                        "icon_color": "green"
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "fan.master_bedroom_tower_fan",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "fan.master_bedroom_tower_fan",
                        "icon_color": "green",
                        "icon": "phu:tower-fan",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    }
                  ],
                  "alignment": "end",
                  "card_mod": {
                    "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n} \n"
                  }
                }
              ],
              "card_mod": {
                "style": "ha-card {\n background: var(--ha-card-background, var(--card-background-color, white) );\n {% if is_state('light.master_bedroom_light', 'on') %}\n     background: rgba(255, 152, 0, 0.1) !important;\n{% endif %} \nheight: 118px;\n--vertical-stack-card-gap: 0px;\n}\nelement.style {\n  background: white !important;\n}\n"
              }
            },
            {
              "type": "custom:mushroom-template-card",
              "secondary": "",
              "icon": "mdi:washing-machine",
              "primary": "Laundry Room ",
              "layout": "vertical",
              "tap_action": {
                "action": "navigate",
                "navigation_path": "laundry-room"
              }
            }
          ]
        },
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "custom:mushroom-template-card",
              "secondary": "",
              "icon": "mdi:unicorn",
              "layout": "vertical",
              "primary": "Adelynn's Room",
              "tap_action": {
                "action": "navigate",
                "navigation_path": "adelynns-room"
              }
            },
            {
              "type": "custom:mushroom-template-card",
              "secondary": "",
              "icon": "mdi:football",
              "layout": "vertical",
              "primary": "Caleb's Room ",
              "tap_action": {
                "action": "navigate",
                "navigation_path": "/lovelace/calebs-room"
              }
            }
          ]
        },
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "custom:stack-in-card",
              "cards": [
                {
                  "type": "horizontal-stack",
                  "cards": [
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "conditional",
                          "conditions": [
                            {
                              "entity": "binary_sensor.office_of_mike_ecobee_sensor_occupancy",
                              "state": "on"
                            }
                          ],
                          "chip": {
                            "type": "template",
                            "entity": "binary_sensor.office_of_mike_ecobee_sensor_occupancy",
                            "icon_color": "#9797db",
                            "icon": "mdi:motion-sensor",
                            "tap_action": {
                              "action": "more-info"
                            },
                            "alignment": "start",
                            "card_mod": null,
                            "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n}\n"
                          }
                        }
                      ]
                    },
                    {
                      "type": "custom:mushroom-chips-card",
                      "chips": [
                        {
                          "type": "entity",
                          "entity": "sensor.mike_s_office_energy_meter",
                          "icon_color": "yellow"
                        }
                      ],
                      "alignment": "end",
                      "card_mod": {
                        "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n}\n"
                      }
                    }
                  ]
                },
                {
                  "type": "custom:mushroom-template-card",
                  "primary": "Guest Room",
                  "secondary": "{{ states('sensor.office_of_mike_ecobee_sensor_temperature') | round(0) }} °F",
                  "icon": "mdi:desktop-tower-monitor",
                  "entity": "light.office_of_mike_light",
                  "tap_action": {
                    "action": "navigate",
                    "navigation_path": "office-of-mike"
                  },
                  "hold_action": {
                    "action": "more-info"
                  },
                  "icon_color": "{{ 'orange' if is_state(entity, 'on') else 'disabled' }}",
                  "fill_container": true,
                  "layout": "horizontal",
                  "multiline_secondary": false,
                  "card_mod": {
                    "style": "ha-card {\n padding-top: 0 !important;\n padding-bottom: 0 !important;\n}\n"
                  }
                },
                {
                  "type": "custom:mushroom-chips-card",
                  "chips": [
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "binary_sensor.refrigerator_door_open",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "icon_color": "red",
                        "icon": "mdi:fridge-variant-alert",
                        "card_mod": {
                          "style": "ha-card {\n  animation: blink 5s linear infinite;\n}\n@keyframes blink {\n  50% {opacity: 0;}\n}  \n"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "light.office_of_mike_light",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "light.office_of_mike_light",
                        "icon": "mdi:lightbulb",
                        "icon_color": "#e68e02",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "fan.office_of_mike_fan",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "fan.office_of_mike_fan",
                        "icon": "mdi:fan",
                        "tap_action": {
                          "action": "more-info"
                        },
                        "icon_color": "#7dc2fa"
                      }
                    },
                    {
                      "type": "conditional",
                      "conditions": [
                        {
                          "entity": "binary_sensor.office_of_mike_tv",
                          "state": "on"
                        }
                      ],
                      "chip": {
                        "type": "template",
                        "entity": "switch.samsung_tv",
                        "icon_color": "blue",
                        "icon": "mdi:television",
                        "tap_action": {
                          "action": "more-info"
                        }
                      }
                    }
                  ],
                  "alignment": "end",
                  "card_mod": {
                    "style": "ha-card {\n  --chip-box-shadow: none;\n  --chip-background: none;\n  --chip-spacing: 0;\n} \n"
                  }
                }
              ],
              "card_mod": {
                "style": "ha-card {\n background: var(--ha-card-background, var(--card-background-color, white) );\n {% if is_state('light.office_of_mike_light', 'on') %}\n     background: rgba(255, 152, 0, 0.1) !important;\n{% endif %} \nheight: 110px;\n}\nelement.style {\n  background: white !important;\n}\n"
              }
            },
            {
              "type": "custom:mushroom-template-card",
              "secondary": "",
              "icon": "mdi:tunnel-outline",
              "primary": "Upstairs Hallway",
              "layout": "vertical",
              "tap_action": {
                "action": "navigate",
                "navigation_path": "upstairs-hallway"
              }
            }
          ]
        },
        {
          "type": "custom:mushroom-fan-card",
          "entity": "fan.living_room_fan",
          "icon": "phu:tower-fan"
        },
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "custom:decluttering-card",
              "template": "custom_area_card_template",
              "variables": [
                {
                  "area-name": "Master Bedroom"
                },
                {
                  "area-icon": "mdi:bed-double"
                },
                {
                  "navigation_path": "master-bedroom"
                },
                {
                  "area-energy": "sensor.energy_meter_master_bedroom"
                },
                {
                  "area-fan1": "fan.master_bedroom_fan"
                },
                {
                  "area-fan1-icon": "mdi:fan"
                },
                {
                  "area-motion": "binary_sensor.master_bedroom_ecobee_sensor_occupancy"
                }
              ],
              "card_mod": {
                "style": "$:| {\n  gap: var(--vertical-stack-card-gap, var(--stack-card-gap, 0px)) !important;\n}\n"
              }
            },
            {
              "type": "custom:decluttering-card",
              "template": "custom_area_card_template",
              "variables": [
                {
                  "area-name": "Master Bedroom"
                },
                {
                  "area-icon": "mdi:bed-double"
                },
                {
                  "navigation_path": "master-bedroom"
                },
                {
                  "area-energy": "sensor.energy_meter_master_bedroom"
                },
                {
                  "area-fan1": "fan.master_bedroom_fan"
                },
                {
                  "area-fan1-icon": "mdi:fan"
                },
                {
                  "area-motion": "binary_sensor.master_bedroom_ecobee_sensor_occupancy"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### `utility_room`

- Fresh config hash: `8bd951df2315db64`
- View index: 15

```json
{
  "theme": "Backend-selected",
  "title": "Utility Room",
  "path": "utility_room",
  "badges": [],
  "cards": [
    {
      "square": false,
      "columns": 1,
      "type": "grid",
      "cards": [
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "custom:mushroom-title-card",
              "title": "Water Usage"
            }
          ]
        },
        {
          "type": "custom:vertical-stack-in-card",
          "style": null,
          ".": "ha-card {\n  --ha-card-box-shadow: none;\n  background-color: transparent;\n  border-radius: none;\n\n}\n",
          "cards": [
            {
              "type": "horizontal-stack",
              "cards": [
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.water_monitor_water_flow_rate",
                  "layout": "vertical",
                  "name": "Flow Rate",
                  "fill_container": false,
                  "icon_color": "blue",
                  "tap_action": {
                    "action": "more-info"
                  },
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                },
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.water_monitor_water_pressure",
                  "layout": "vertical",
                  "name": "Pressure",
                  "icon_color": "blue",
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                },
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.water_monitor_water_temperature",
                  "layout": "vertical",
                  "icon_color": "blue",
                  "name": "Water Temp.",
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                }
              ]
            },
            {
              "type": "horizontal-stack",
              "cards": [
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.water_monitor_today_s_water_usage",
                  "name": "Today's Water Usage",
                  "layout": "vertical",
                  "icon_color": "cyan",
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                },
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "switch.water_monitor_shutoff_valve",
                  "layout": "vertical",
                  "icon_color": "cyan",
                  "name": "Water Shutoff Valve",
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                },
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "binary_sensor.water_monitor_pending_system_alerts",
                  "layout": "vertical",
                  "name": "Water Pending Alerts",
                  "icon_color": null,
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                }
              ]
            },
            {
              "type": "horizontal-stack",
              "card_mod": {
                "style": "ha-card {\n#background: red;\nbackground-color: transparent;\nborder-radius: none;\n\n}\n"
              },
              "cards": [
                {
                  "type": "custom:collapsable-cards",
                  "card_mod": {
                    "style": ".card-content {\n#background: red;\nbackground-color: transparent !important;\n}\nha-card {\n--ha-card-box-shadow: none;\nbackground-color: transparent !important;\nborder-radius: none;\n}\n"
                  },
                  "title": "Statistics",
                  "cards": [
                    {
                      "type": "entities",
                      "entities": [
                        {
                          "entity": "sensor.water_utility_meter_hourly"
                        },
                        {
                          "entity": "sensor.water_utility_meter_daily"
                        },
                        {
                          "entity": "sensor.water_utility_meter_weekly"
                        },
                        {
                          "entity": "sensor.water_utility_meter_monthly"
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "tile",
              "entity": "sensor.sump_pump_electric_consumption_w",
              "vertical": true,
              "name": "Sump Pump Power"
            },
            {
              "type": "custom:bignumber-card",
              "entity": "counter.sump_pump_counter"
            }
          ]
        }
      ]
    },
    {
      "square": false,
      "columns": 1,
      "type": "grid",
      "cards": [
        {
          "type": "custom:mushroom-title-card",
          "title": "Solar Energy Production"
        },
        {
          "type": "custom:vertical-stack-in-card",
          "style": null,
          ".": "ha-card {\n  --ha-card-box-shadow: none;\n  background-color: transparent;\n  border-radius: none;\n\n}\n",
          "cards": [
            {
              "type": "horizontal-stack",
              "cards": [
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.evergy_grid_import_power_w",
                  "layout": "vertical",
                  "name": "Power Importing",
                  "fill_container": false,
                  "icon": "mdi:transmission-tower-import",
                  "icon_color": "amber",
                  "tap_action": {
                    "action": "more-info"
                  },
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                },
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.evergy_grid_export_power_w",
                  "layout": "vertical",
                  "name": "Power Exporting",
                  "icon_color": "amber",
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                },
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.nextsunrise",
                  "layout": "vertical",
                  "icon_color": "amber",
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                }
              ]
            },
            {
              "type": "horizontal-stack",
              "cards": [
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.daily_solar_powered_percentage",
                  "layout": "vertical",
                  "icon_color": "orange",
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                },
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.envoy_202210158779_energy_production_today",
                  "layout": "vertical",
                  "icon_color": "orange",
                  "name": "Solar Production Today",
                  "icon": "mdi:solar-power",
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                },
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.envoy_202210158779_current_power_production",
                  "layout": "vertical",
                  "name": "Solar Production Realtime",
                  "icon": "mdi:solar-power-variant-outline",
                  "icon_color": "orange",
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                }
              ]
            },
            {
              "type": "horizontal-stack",
              "card_mod": {
                "style": "ha-card {\n#background: red;\nbackground-color: transparent;\nborder-radius: none;\n\n}\n"
              },
              "cards": [
                {
                  "type": "custom:collapsable-cards",
                  "card_mod": {
                    "style": ".card-content {\n#background: red;\nbackground-color: transparent !important;\n}\nha-card {\n--ha-card-box-shadow: none;\nbackground-color: transparent !important;\nborder-radius: none;\n}\n"
                  },
                  "title": "Statistics",
                  "cards": [
                    {
                      "type": "horizontal-stack",
                      "cards": [
                        {
                          "type": "custom:mushroom-entity-card",
                          "entity": "sensor.energy_production_today",
                          "layout": "vertical",
                          "name": "Estimated Solar Producton Today",
                          "fill_container": false,
                          "icon": "mdi:solar-panel",
                          "icon_color": "amber",
                          "tap_action": {
                            "action": "more-info"
                          },
                          "card_mod": {
                            "style": {
                              "mushroom-state-info": {
                                "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                              }
                            }
                          }
                        },
                        {
                          "type": "custom:mushroom-entity-card",
                          "entity": "sensor.energy_production_tomorrow",
                          "layout": "vertical",
                          "name": "Estimated Solar Production Tomorrow",
                          "icon": "mdi:solar-panel-large",
                          "icon_color": "amber",
                          "card_mod": {
                            "style": {
                              "mushroom-state-info": {
                                "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                              }
                            }
                          }
                        },
                        {
                          "type": "custom:mushroom-entity-card",
                          "entity": "sensor.nextsunrise",
                          "layout": "vertical",
                          "icon_color": "amber",
                          "card_mod": {
                            "style": {
                              "mushroom-state-info": {
                                "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                              }
                            }
                          }
                        }
                      ]
                    },
                    {
                      "type": "horizontal-stack",
                      "cards": [
                        {
                          "type": "entities",
                          "entities": [
                            {
                              "entity": "sun.sun"
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "custom:sun-card"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "square": false,
      "columns": 1,
      "type": "grid",
      "cards": [
        {
          "type": "custom:mushroom-title-card",
          "title": "Energy Consumption"
        },
        {
          "type": "custom:vertical-stack-in-card",
          "style": null,
          ".": "ha-card {\n  --ha-card-box-shadow: none;\n  background-color: transparent;\n  border-radius: none;\n\n}\n",
          "cards": [
            {
              "type": "horizontal-stack",
              "cards": [
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.evergy_grid_import_power_w",
                  "layout": "vertical",
                  "name": "Power Importing",
                  "fill_container": false,
                  "icon": "mdi:transmission-tower-import",
                  "icon_color": "amber",
                  "tap_action": {
                    "action": "more-info"
                  },
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                },
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.evergy_grid_export_power_w",
                  "layout": "vertical",
                  "name": "Power Exporting",
                  "icon_color": "amber",
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                },
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.nextsunrise",
                  "layout": "vertical",
                  "icon_color": "amber",
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                }
              ]
            },
            {
              "type": "horizontal-stack",
              "cards": [
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.daily_solar_powered_percentage",
                  "layout": "vertical",
                  "icon_color": "orange",
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                },
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.envoy_202210158779_energy_consumption_today",
                  "layout": "vertical",
                  "icon_color": "orange",
                  "name": "Energy Consumption Today",
                  "icon": "mdi:factory",
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                },
                {
                  "type": "custom:mushroom-entity-card",
                  "entity": "sensor.envoy_202210158779_current_power_consumption",
                  "layout": "vertical",
                  "name": "Energy Consumption Realtime",
                  "icon": "mdi:solar-power-variant-outline",
                  "icon_color": "orange",
                  "card_mod": {
                    "style": {
                      "mushroom-state-info": {
                        "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                      }
                    }
                  }
                }
              ]
            },
            {
              "type": "horizontal-stack",
              "card_mod": {
                "style": "ha-card {\n#background: red;\nbackground-color: transparent;\nborder-radius: none;\n\n}\n"
              },
              "cards": [
                {
                  "type": "custom:collapsable-cards",
                  "card_mod": {
                    "style": ".card-content {\n#background: red;\nbackground-color: transparent !important;\n}\nha-card {\n--ha-card-box-shadow: none;\nbackground-color: transparent !important;\nborder-radius: none;\n}\n"
                  },
                  "title": "Statistics",
                  "cards": [
                    {
                      "type": "horizontal-stack",
                      "cards": [
                        {
                          "type": "custom:mushroom-entity-card",
                          "entity": "sensor.enphase_energy_production_utility_kwh",
                          "layout": "vertical",
                          "name": "Estimated Solar Producton Today",
                          "fill_container": false,
                          "icon": "mdi:solar-panel",
                          "icon_color": "amber",
                          "tap_action": {
                            "action": "more-info"
                          },
                          "card_mod": {
                            "style": {
                              "mushroom-state-info": {
                                "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                              }
                            }
                          }
                        },
                        {
                          "type": "custom:mushroom-entity-card",
                          "entity": "sensor.energy_production_tomorrow",
                          "layout": "vertical",
                          "name": "Estimated Solar Production Tomorrow",
                          "icon": "mdi:solar-panel-large",
                          "icon_color": "amber",
                          "card_mod": {
                            "style": {
                              "mushroom-state-info": {
                                "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                              }
                            }
                          }
                        },
                        {
                          "type": "custom:mushroom-entity-card",
                          "entity": "sensor.nextsunrise",
                          "layout": "vertical",
                          "icon_color": "amber",
                          "card_mod": {
                            "style": {
                              "mushroom-state-info": {
                                "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                              }
                            }
                          }
                        }
                      ]
                    },
                    {
                      "type": "horizontal-stack",
                      "cards": [
                        {
                          "type": "entities",
                          "entities": [
                            {
                              "entity": "sun.sun"
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "custom:sun-card"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "square": false,
      "columns": 1,
      "type": "grid",
      "cards": [
        {
          "type": "custom:mushroom-title-card",
          "title": "Gas Usage"
        },
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "entities",
              "entities": [
                {
                  "entity": "sensor.spire_gas_ft3_mqtt_rtlamr"
                },
                {
                  "entity": "sensor.gas_utility_hourly"
                },
                {
                  "entity": "sensor.gas_utility_daily"
                },
                {
                  "entity": "sensor.gas_utility_weekly"
                },
                {
                  "entity": "sensor.gas_utility_montly"
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "thermostat",
      "entity": "climate.ecobee_thermostat",
      "features": [
        {
          "type": "climate-hvac-modes",
          "hvac_modes": [
            "heat_cool",
            "heat",
            "cool",
            "off"
          ]
        },
        {
          "type": "climate-preset-modes",
          "style": "dropdown",
          "preset_modes": [
            "Home",
            "Away",
            "Sleep"
          ]
        }
      ]
    }
  ]
}
```

### `server-room`

- Fresh config hash: `8bd951df2315db64`
- View index: 16

```json
{
  "theme": "Backend-selected",
  "title": "Server Room",
  "path": "server-room",
  "badges": [],
  "cards": []
}
```

### `office-of-mike`

- Fresh config hash: `8bd951df2315db64`
- View index: 18

```json
{
  "theme": "Backend-selected",
  "title": "Office of Mike",
  "path": "office-of-mike",
  "subview": true,
  "icon": "mdi:desktop-tower-monitor",
  "badges": [],
  "cards": [
    {
      "square": false,
      "columns": 1,
      "type": "grid",
      "cards": [
        {
          "type": "custom:mushroom-title-card",
          "title": "Controls"
        },
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "custom:vertical-stack-in-card",
              "cards": [
                {
                  "type": "custom:mushroom-chips-card",
                  "alignment": "justify",
                  "chips": [
                    {
                      "type": "entity",
                      "entity": "sensor.mikes_office_light_electric_consumption_w",
                      "icon_color": "yellow"
                    }
                  ]
                },
                {
                  "type": "custom:mushroom-light-card",
                  "entity": "light.mikes_office_light",
                  "icon": "mdi:ceiling-fan-light"
                }
              ]
            },
            {
              "type": "custom:vertical-stack-in-card",
              "cards": [
                {
                  "type": "custom:mushroom-chips-card",
                  "alignment": "justify",
                  "chips": [
                    {
                      "type": "entity",
                      "entity": "sensor.mike_s_office_ceiling_fan_breezemode",
                      "icon_color": "yellow"
                    }
                  ]
                },
                {
                  "type": "custom:mushroom-fan-card",
                  "icon_animation": true,
                  "entity": "fan.mikes_office_ceiling_fan",
                  "fill_container": true,
                  "show_percentage_control": true
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "square": false,
      "columns": 1,
      "type": "grid",
      "cards": [
        {
          "type": "custom:mushroom-title-card",
          "title": "Monitors"
        },
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "custom:vertical-stack-in-card",
              "style": ":host {\npadding-left:0px;\nvar(--card-background-color)\n}\n",
              "styles": {
                "--chip-box-shadow": "none",
                "--chip-background": "none",
                "--chip-spacing": 0
              },
              "cards": [
                {
                  "type": "custom:mushroom-chips-card",
                  "alignment": "justify",
                  "chips": [
                    {
                      "type": "entity",
                      "entity": "sensor.office_of_mike_ul_monitor_current_consumption",
                      "icon_color": "yellow"
                    }
                  ]
                },
                {
                  "type": "custom:mushroom-template-card",
                  "primary": "Upper Left Monitor",
                  "secondary": "{{states('switch.office_of_mike_ul_monitor') | title}}",
                  "icon": "mdi:monitor",
                  "layout": "horizontal",
                  "entity": "switch.office_of_mike_ul_monitor",
                  "tap_action": {
                    "action": "toggle"
                  },
                  "icon_color": "{% if is_state(\"switch.office_of_mike_ul_monitor\", \"on\") %}\n blue\n{% endif %}"
                }
              ]
            },
            {
              "type": "custom:vertical-stack-in-card",
              "style": ":host {\npadding-left:0px;\nvar(--card-background-color)\n}\n",
              "styles": {
                "--chip-box-shadow": "none",
                "--chip-background": "none",
                "--chip-spacing": 0
              },
              "cards": [
                {
                  "type": "custom:mushroom-chips-card",
                  "alignment": "justify",
                  "chips": [
                    {
                      "type": "entity",
                      "entity": "sensor.office_of_mike_ur_monitor_current_consumption",
                      "icon_color": "yellow"
                    }
                  ]
                },
                {
                  "type": "custom:mushroom-template-card",
                  "primary": "Upper Right Monitor",
                  "secondary": "{{states('switch.office_of_mike_ur_monitor') | title}}",
                  "icon": "mdi:monitor",
                  "layout": "horizontal",
                  "entity": "switch.office_of_mike_ur_monitor",
                  "tap_action": {
                    "action": "toggle"
                  },
                  "icon_color": "{% if is_state(\"switch.office_of_mike_ur_monitor\", \"on\") %}\n blue\n{% endif %}"
                }
              ]
            }
          ]
        },
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "custom:vertical-stack-in-card",
              "style": ":host {\npadding-left:0px;\nvar(--card-background-color)\n}\n",
              "styles": {
                "--chip-box-shadow": "none",
                "--chip-background": "none",
                "--chip-spacing": 0
              },
              "cards": [
                {
                  "type": "custom:mushroom-chips-card",
                  "alignment": "justify",
                  "chips": [
                    {
                      "type": "entity",
                      "entity": "sensor.office_of_mike_bl_monitor_current_consumption",
                      "icon_color": "yellow"
                    }
                  ]
                },
                {
                  "type": "custom:mushroom-template-card",
                  "primary": "Bottom Left Monitor",
                  "secondary": "{{states('switch.office_of_mike_bl_monitor') | title}}",
                  "icon": "mdi:monitor",
                  "layout": "horizontal",
                  "entity": "switch.office_of_mike_bl_monitor",
                  "tap_action": {
                    "action": "toggle"
                  },
                  "icon_color": "{% if is_state(\"switch.office_of_mike_bl_monitor\", \"on\") %}\n blue\n{% endif %}"
                }
              ]
            },
            {
              "type": "custom:vertical-stack-in-card",
              "style": ":host {\npadding-left:0px;\nvar(--card-background-color)\n}\n",
              "styles": {
                "--chip-box-shadow": "none",
                "--chip-background": "none",
                "--chip-spacing": 0
              },
              "cards": [
                {
                  "type": "custom:mushroom-chips-card",
                  "alignment": "justify",
                  "chips": [
                    {
                      "type": "entity",
                      "entity": "sensor.mike_s_office_entertainment_current_consumption",
                      "icon_color": "yellow"
                    }
                  ]
                },
                {
                  "type": "custom:mushroom-template-card",
                  "primary": "Television",
                  "secondary": "{{states('binary_sensor.office_of_mike_tv') | title}}",
                  "layout": "horizontal",
                  "entity": "binary_sensor.office_of_mike_tv",
                  "hold_action": {
                    "action": "more-info"
                  },
                  "tap_action": {
                    "action": "call-service",
                    "service": "script.office_of_mike_tv_power",
                    "data": {},
                    "target": {}
                  },
                  "icon": "{% if is_state(\"binary_sensor.office_of_mike_tv\",'on') -%}\n  mdi:television\n{%- else -%}\n  mdi:television-off\n{%- endif -%}",
                  "icon_color": "{% if is_state(\"binary_sensor.office_of_mike_tv\", \"on\") %}\n blue\n{% endif %}"
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "custom:vertical-stack-in-card",
      "style": null,
      ".": "ha-card {\n  --ha-card-box-shadow: none;\n  background-color: transparent;\n  border-radius: none;\n\n}\n",
      "cards": [
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "custom:mushroom-template-card",
              "primary": "Guest Bedroom: {{states('media_player.office_of_mike_fire_tv_android') | title}}",
              "secondary": "{{ states('sensor.office_of_mike_fire_tv_source')}}",
              "icon": "fab:amazon",
              "entity": "media_player.office_of_mike_fire_tv_android",
              "tap_action": {
                "action": "more-info"
              },
              "layout": "vertical",
              "double_tap_action": {
                "action": "navigate",
                "navigation_path": "/lovelace/mikes-office-fire-stick"
              },
              "card_mod": {
                "style": {
                  "mushroom-state-info": {
                    "$": ".primary {\n  white-space: normal !important;\n  font-size: 13px !important;\n}\n"
                  }
                }
              }
            }
          ]
        },
        {
          "type": "horizontal-stack",
          "card_mod": {
            "style": "ha-card {\n#background: red;\nbackground-color: transparent;\nborder-radius: none;\n\n}\n"
          },
          "cards": [
            {
              "type": "custom:collapsable-cards",
              "card_mod": {
                "style": ".card-content {\n#background: red;\nbackground-color: transparent !important;\n}\nha-card {\n--ha-card-box-shadow: none;\nbackground-color: transparent !important;\nborder-radius: none;\n}\n"
              },
              "title": "Remote",
              "cards": [
                {
                  "type": "custom:tv-card",
                  "entity": "media_player.guest_bedroom_fire_tv_android",
                  "title": "Guest Bedroom Fire TV",
                  "power_row": [
                    "power"
                  ],
                  "channel_row": [
                    "return",
                    "home",
                    "menu"
                  ],
                  "volume_row": "buttons",
                  "media_control_row": [
                    "rewind",
                    "play",
                    "fast_forward"
                  ],
                  "navigation_row": "buttons",
                  "apps_row": [
                    "prime_video",
                    "netflix",
                    "hulu"
                  ],
                  "source_row": [
                    "hbo",
                    "disney_plus",
                    "cbs"
                  ],
                  "custom_keys": {
                    "power": {
                      "icon": "mdi:power",
                      "service": "script.office_of_mike_tv_power"
                    },
                    "return": {
                      "icon": "mdi:arrow-left",
                      "service": "androidtv.adb_command",
                      "service_data": {
                        "command": "sendevent /dev/input/event5 4 4 458993 && sendevent /dev/input/event5 1 158 1 && sendevent /dev/input/event5 0 0 0 && sendevent /dev/input/event5 4 4 458993 && sendevent /dev/input/event5 1 158 0 && sendevent /dev/input/event5 0 0 0",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "menu": {
                      "icon": "mdi:menu",
                      "service": "androidtv.adb_command",
                      "service_data": {
                        "command": "sendevent /dev/input/event5 4 4 786496 && sendevent /dev/input/event5 1 139 1 && sendevent /dev/input/event5 0 0 0 && sendevent /dev/input/event5 4 4 786496 && sendevent /dev/input/event5 1 139 0 && sendevent /dev/input/event5 0 0 0",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "volume_up": {
                      "icon": "mdi:volume-plus",
                      "service": "script.office_of_mike_tv_volume_up"
                    },
                    "volume_down": {
                      "icon": "mdi:volume-minus",
                      "service": "script.office_of_mike_tv_volume_down"
                    },
                    "volume_mute": {
                      "icon": "mdi:volume-off",
                      "service": "script.office_of_mike_tv_volume_mute"
                    },
                    "rewind": {
                      "icon": "mdi:rewind",
                      "service": "androidtv.adb_command",
                      "service_data": {
                        "command": "sendevent /dev/input/event5 4 4 786612 && sendevent /dev/input/event5 1 168 1 && sendevent /dev/input/event5 0 0 0 && sendevent /dev/input/event5 4 4 786612 && sendevent /dev/input/event5 1 168 0 && sendevent /dev/input/event5 0 0 0",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "play": {
                      "icon": "mdi:play-pause",
                      "service": "androidtv.adb_command",
                      "service_data": {
                        "command": "sendevent /dev/input/event5 4 4 786637 && sendevent /dev/input/event5 1 164 1 && sendevent /dev/input/event5 0 0 0 && sendevent /dev/input/event5 4 4 786637 && sendevent /dev/input/event5 1 164 0 && sendevent /dev/input/event5 0 0 0",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "fast_forward": {
                      "icon": "mdi:fast-forward",
                      "service": "androidtv.adb_command",
                      "service_data": {
                        "command": "sendevent /dev/input/event5 4 4 786611 && sendevent /dev/input/event5 1 208 1 && sendevent /dev/input/event5 0 0 0 && sendevent /dev/input/event5 4 4 786611 && sendevent /dev/input/event5 1 208 0 && sendevent /dev/input/event5 0 0 0",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "home": {
                      "icon": "mdi:home",
                      "service": "androidtv.adb_command",
                      "service_data": {
                        "command": "sendevent /dev/input/event5 20 0 0 && sendevent /dev/input/event5 20 1 0 && sendevent /dev/input/event5 4 4 786979 && sendevent /dev/input/event5 1 172 1 && sendevent /dev/input/event5 0 0 0 && sendevent /dev/input/event5 4 4 786979 && sendevent /dev/input/event5 1 172 0 && sendevent /dev/input/event5 0 0 0",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "enter": {
                      "icon": "mdi:circle",
                      "service": "androidtv.adb_command",
                      "service_data": {
                        "command": "sendevent /dev/input/event5 4 4 458840 && sendevent /dev/input/event5 1 96 1 && sendevent /dev/input/event5 0 0 0 && sendevent /dev/input/event5 4 4 458840 && sendevent /dev/input/event5 1 96 0 && sendevent /dev/input/event5 0 0 0",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "up": {
                      "icon": "mdi:chevron-up",
                      "service": "androidtv.adb_command",
                      "service_data": {
                        "command": "sendevent /dev/input/event5 4 4 458834 && sendevent /dev/input/event5 1 103 1 && sendevent /dev/input/event5 0 0 0 && sendevent /dev/input/event5 4 4 458834 && sendevent /dev/input/event5 1 103 0 && sendevent /dev/input/event5 0 0 0",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "down": {
                      "icon": "mdi:chevron-down",
                      "service": "androidtv.adb_command",
                      "service_data": {
                        "command": "sendevent /dev/input/event5 4 4 458833 && sendevent /dev/input/event5 1 108 1 && sendevent /dev/input/event5 0 0 0 && sendevent /dev/input/event5 4 4 458833 && sendevent /dev/input/event5 1 108 0 && sendevent /dev/input/event5 0 0 0",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "left": {
                      "icon": "mdi:chevron-left",
                      "service": "androidtv.adb_command",
                      "service_data": {
                        "command": "sendevent /dev/input/event5 4 4 458832 && sendevent /dev/input/event5 1 105 1 && sendevent /dev/input/event5 0 0 0 && sendevent /dev/input/event5 4 4 458832 && sendevent /dev/input/event5 1 105 0 && sendevent /dev/input/event5 0 0 0",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "right": {
                      "icon": "mdi:chevron-right",
                      "service": "androidtv.adb_command",
                      "service_data": {
                        "command": "sendevent /dev/input/event5 4 4 458831 && sendevent /dev/input/event5 1 106 1 && sendevent /dev/input/event5 0 0 0 && sendevent /dev/input/event5 4 4 458831 && sendevent /dev/input/event5 1 106 0 && sendevent /dev/input/event5 0 0 0",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "prime_video": {
                      "icon": "prime_video",
                      "service": "androidtv.adb_command",
                      "service_data": {
                        "command": "sendevent /dev/input/event5 1 745 1 && sendevent /dev/input/event5 0 0 0 && sendevent /dev/input/event5 1 745 0 && sendevent /dev/input/event5 0 0 0",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "netflix": {
                      "icon": "netflix",
                      "service": "androidtv.adb_command",
                      "service_data": {
                        "command": "sendevent /dev/input/event5 1 744 1 && sendevent /dev/input/event5 0 0 0 && sendevent /dev/input/event5 1 744 0 && sendevent /dev/input/event5 0 0 0",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "hulu": {
                      "icon": "hulu",
                      "service": "media_player.select_source",
                      "service_data": {
                        "source": "com.hulu.plus",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "hbo": {
                      "icon": "hbo",
                      "service": "androidtv.adb_command",
                      "service_data": {
                        "command": "adb shell am start -n com.hbo.hbonow/com.hbo.max.HboMaxActivity",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "cbs": {
                      "icon": "fab:paramount-plus",
                      "service": "media_player.select_source",
                      "service_data": {
                        "source": "com.cbs.ott",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    },
                    "disney_plus": {
                      "icon": "fab:disney_plus",
                      "service": "androidtv.adb_command",
                      "service_data": {
                        "command": "adb shell am start -n com.disney.disneyplus/com.bamtechmedia.dominguez.main.MainActivity",
                        "entity_id": "media_player.office_of_mike_fire_tv_android"
                      }
                    }
                  },
                  "custom_icons": {
                    "prime_video": "M0 9.508c0-.043.01-.073.028-.09.018-.017.047-.025.086-.025h.329c.07 0 .112.034.127.101l.032.119c.091-.088.202-.159.33-.21a1.04 1.04 0 0 1 .396-.079c.294 0 .528.109.7.326.171.217.257.51.257.88 0 .254-.042.475-.127.665-.086.19-.201.335-.347.437a.85.85 0 0 1-.502.154c-.125 0-.243-.02-.355-.06a.857.857 0 0 1-.288-.164v1.003c0 .043-.008.073-.025.09-.017.016-.046.025-.09.025H.115c-.04 0-.068-.009-.086-.025-.019-.017-.028-.047-.028-.09zm1.113.32a.868.868 0 0 0-.447.124v1.206a.834.834 0 0 0 .447.124c.17 0 .296-.058.376-.174.081-.117.121-.3.121-.55 0-.254-.04-.439-.118-.555-.08-.116-.206-.174-.379-.174zm2.248-.087c.121-.134.236-.23.344-.286a.733.733 0 0 1 .345-.085h.063c.043 0 .073.009.092.025.018.017.027.047.027.09v.385c0 .04-.008.068-.025.087-.017.018-.046.027-.089.027a.923.923 0 0 1-.082-.004 1.369 1.369 0 0 0-.383.025c-.1.02-.186.045-.256.076v1.54c0 .04-.008.069-.025.087-.016.018-.046.028-.089.028h-.437c-.04 0-.069-.01-.087-.028-.018-.018-.028-.047-.028-.087V9.508c0-.043.01-.073.028-.09.018-.017.047-.025.087-.025h.328c.07 0 .112.034.128.1zm1.526-.71a.396.396 0 0 1-.278-.096.338.338 0 0 1-.105-.262c0-.11.035-.197.105-.26a.395.395 0 0 1 .278-.097c.116 0 .208.032.278.096.07.064.105.151.105.261a.34.34 0 0 1-.105.262.396.396 0 0 1-.278.096zm-.333.477c0-.043.01-.073.027-.09.019-.017.048-.025.087-.025h.438c.043 0 .072.008.089.025s.025.047.025.09v2.113c0 .04-.008.069-.025.087-.017.018-.046.028-.09.028h-.437c-.04 0-.068-.01-.087-.028-.018-.018-.027-.047-.027-.087zm1.837.11c.161-.107.306-.183.435-.227.13-.045.263-.067.4-.067.273 0 .466.098.579.294.155-.104.3-.18.438-.225.137-.046.278-.069.424-.069.213 0 .377.06.495.179.117.12.175.286.175.5v1.618c0 .04-.008.069-.025.087-.017.019-.046.027-.089.027h-.438c-.04 0-.068-.008-.086-.027-.018-.018-.028-.047-.028-.087V10.15c0-.208-.092-.312-.278-.312-.164 0-.33.04-.497.119v1.664c0 .04-.008.069-.025.087-.017.019-.046.027-.09.027h-.437c-.04 0-.068-.008-.086-.027-.019-.018-.028-.047-.028-.087V10.15c0-.208-.093-.312-.278-.312-.17 0-.337.04-.502.123v1.66c0 .04-.008.069-.025.087-.017.019-.046.027-.089.027h-.438c-.039 0-.068-.008-.086-.027-.018-.018-.027-.047-.027-.087V9.508c0-.043.009-.073.027-.09.018-.017.047-.025.086-.025h.329c.07 0 .112.034.128.101zm4.387 1.16a1.81 1.81 0 0 1-.451-.05c.018.204.08.35.185.44.105.088.263.132.476.132.085 0 .168-.005.249-.016a3.08 3.08 0 0 0 .362-.078.143.143 0 0 1 .023-.002c.052 0 .078.035.078.105v.211c0 .049-.007.083-.02.103a.169.169 0 0 1-.08.053 1.953 1.953 0 0 1-.708.128c-.377 0-.666-.103-.868-.312-.203-.207-.304-.505-.304-.893 0-.398.104-.71.31-.935.207-.227.494-.34.862-.34.283 0 .504.069.664.206a.69.69 0 0 1 .24.55c0 .23-.087.403-.258.52-.172.119-.425.177-.76.177zm.064-.99c-.292 0-.46.18-.506.54.122.025.257.037.406.037.155 0 .267-.024.337-.071.07-.047.105-.12.105-.218 0-.193-.114-.289-.342-.289zm2.948 1.946a.21.21 0 0 1-.075-.011.119.119 0 0 1-.05-.037.274.274 0 0 1-.038-.071l-.777-2.04a1.863 1.863 0 0 1-.023-.063.162.162 0 0 1-.009-.05c0-.047.03-.07.091-.07h.454c.049 0 .084.01.107.028.023.018.04.049.052.092l.468 1.622.477-1.622a.175.175 0 0 1 .052-.092c.023-.018.058-.027.107-.027h.44c.061 0 .091.022.091.068a.16.16 0 0 1-.009.05l-.022.065-.777 2.039a.274.274 0 0 1-.039.07.122.122 0 0 1-.047.038.207.207 0 0 1-.078.01zm2.02-2.703a.393.393 0 0 1-.277-.097.338.338 0 0 1-.105-.26c0-.11.035-.198.105-.262a.393.393 0 0 1 .277-.096c.115 0 .207.032.277.096.07.064.104.151.104.261 0 .11-.034.197-.104.261a.393.393 0 0 1-.277.097zm-.218 2.703c-.04 0-.068-.01-.086-.028-.019-.018-.028-.047-.028-.087V9.507c0-.043.01-.072.028-.09.018-.016.047-.024.086-.024h.436c.042 0 .072.008.089.025.016.017.024.046.024.09v2.111c0 .04-.008.07-.024.087-.017.019-.047.028-.09.028zm1.948.05a.869.869 0 0 1-.513-.153.97.97 0 0 1-.334-.426 1.6 1.6 0 0 1-.116-.63c0-.38.09-.682.268-.91a.856.856 0 0 1 .709-.341.98.98 0 0 1 .622.206V8.458c0-.043.01-.073.027-.09.018-.016.047-.025.087-.025h.436c.042 0 .071.009.088.025.017.017.025.047.025.09v3.161c0 .04-.008.07-.025.087-.017.019-.046.028-.088.028h-.364a.135.135 0 0 1-.084-.023.137.137 0 0 1-.043-.078l-.027-.105a.958.958 0 0 1-.668.256zm.218-.504a.762.762 0 0 0 .418-.128v-1.21a.872.872 0 0 0-.45-.114c-.16 0-.28.06-.358.18-.08.121-.118.304-.118.548 0 .245.041.426.124.546.084.119.212.178.384.178zm2.588-.51c-.169 0-.315-.016-.44-.05.018.201.078.345.18.432.103.087.257.13.465.13.083 0 .164-.005.242-.016a2.997 2.997 0 0 0 .354-.076.135.135 0 0 1 .022-.002c.05 0 .075.035.075.103v.207c0 .048-.007.082-.02.101a.165.165 0 0 1-.077.052 1.895 1.895 0 0 1-.69.126c-.367 0-.65-.102-.846-.306-.197-.204-.296-.496-.296-.876 0-.39.1-.695.302-.917.202-.222.482-.333.84-.333.276 0 .492.068.647.203a.678.678 0 0 1 .234.539c0 .225-.084.395-.251.51-.168.115-.415.173-.74.173zm.063-.97c-.285 0-.45.176-.494.53.119.024.25.036.396.036.15 0 .26-.024.329-.07.068-.046.102-.117.102-.213 0-.19-.111-.284-.333-.284zm2.442 2.003c-.36 0-.642-.11-.845-.328-.203-.218-.304-.523-.304-.914 0-.388.101-.691.304-.91.203-.218.485-.327.845-.327s.642.109.845.327c.203.219.304.522.304.91 0 .39-.101.696-.304.914-.203.218-.485.328-.845.328zm0-.514c.318 0 .477-.242.477-.728 0-.483-.16-.724-.477-.724-.318 0-.477.241-.477.724 0 .486.16.728.477.728zm-6.844 1.886c.405-.306.944-.408 1.39-.408.418 0 .756.09.828.185.15.2-.039 1.584-.775 2.244-.112.102-.22.047-.17-.087.166-.442.536-1.436.36-1.677-.175-.242-1.158-.115-1.6-.058-.068.008-.107-.02-.112-.061v-.023c.004-.036.03-.078.079-.115zm-10.184-.172a.105.105 0 0 1 .106-.091c.027 0 .057.009.089.028a11.778 11.778 0 0 0 6.194 1.772c1.52 0 3.19-.34 4.726-1.043.232-.105.426.164.2.346-1.371 1.09-3.359 1.67-5.07 1.67-2.397 0-4.557-.956-6.191-2.547a.173.173 0 0 1-.054-.097Z",
                    "hulu": "M14.707 15.957h1.912V8.043h-1.912zm-3.357-2.256a.517.517 0 01-.512.511H9.727a.517.517 0 01-.512-.511v-3.19H7.303v3.345c0 1.368.879 2.09 2.168 2.09h1.868c1.189 0 1.912-.856 1.912-2.09V10.51h-1.912c.01 0 .01 3.09.01 3.19zm10.75-3.19v3.19a.517.517 0 01-.512.511h-1.112a.517.517 0 01-.511-.511v-3.19h-1.912v3.345c0 1.368.878 2.09 2.167 2.09h1.868c1.19 0 1.912-.856 1.912-2.09V10.51zm-18.32 0H2.557c-.434 0-.645.11-.645.11V8.044H0v7.903h1.9v-3.179c0-.278.234-.511.512-.511h1.112c.278 0 .511.233.511.511v3.19h1.912v-3.446c0-1.445-.967-2-2.167-2Z",
                    "netflix": "M5.398 0v.006c3.028 8.556 5.37 15.175 8.348 23.596 2.344.058 4.85.398 4.854.398-2.8-7.924-5.923-16.747-8.487-24zm8.489 0v9.63L18.6 22.951c-.043-7.86-.004-15.913.002-22.95zM5.398 1.05V24c1.873-.225 2.81-.312 4.715-.398v-9.22z",
                    "cbs": "M668.2 479.9c-3.7-1.5-9.7-8.3.3-27.2l23.4-48.8c.7-1.5-1-3.3-2.1-2.1l-20.4 20.5c-9.7 10.1-26.1 38.5-29.2 43.7l-24.8 41c1.8-.1 3.4 1.4 3.4 3.2 0 .6-.1 1.2-.4 1.7L595.7 550c-5.5 9.5 4.4 16.1 5.8 13.9 35.7-57.4 56.4-52.9 56.4-52.9l11.9-27.6c.6-1.4 0-3-1.4-3.6-.1.1-.1.1-.2.1zM749.3 0C545.4 0 380.1 165.2 380.1 369c-.1 78.9 25.2 155.7 72.2 219.1 15.5-6.7 24.1-16.7 30.2-24.3l68.7-87.9c1.4-1.9 3.3-3.3 5.5-4.2l10.3-4.5 113-143.3 16.4-12.8 33.7-46.8c.9-1.2 1.9-2.3 3.1-3.2l14.7-10.7c3.6-2.6 8.5-2.7 12.2-.1l17.8 12.5c9.5 6.6 17.1 15.5 22.3 25.8L871.8 414c1.2 2.4 3.1 4.3 5.6 5.4 14 7 22.6 8.2 40.9 28.1 8.6 9.3 46 51.2 98.6 116.3 7.6 10.4 17.9 18.7 29.7 24 46.8-63.3 72.1-140 71.9-218.8-.1-203.8-165.3-369-369.2-369zM479.7 389.3l-23.9-7.8-14.8 20.4v-25.1l-24-7.8 23.9-7.8v-25.1l14.8 20.3 23.9-7.8-14.7 20.4 14.8 20.3zm-5.7 82.3-7.8 23.9-7.8-23.9h-25.2l20.4-14.8-7.8-23.9 20.4 14.8 20.4-14.8-7.8 23.9 20.4 14.8H474zm4.8-190.5 7.8 23.9-20.4-14.8-20.3 14.8 7.8-23.9-20.4-14.8h25.2l7.8-23.9 7.8 23.9h25.2l-20.5 14.8zm40.4-54.1-14.8-20.3-23.9 7.8 14.8-20.3-14.8-20.3 23.9 7.8 14.8-20.3v25.1l23.9 7.8-23.9 7.8V227zm62.9-88-7.8 23.9-7.8-23.9h-25.2l20.4-14.8-7.8-23.9 20.4 14.8 20.4-14.8-7.8 23.9 20.4 14.8h-25.2zm79.3-40.4L646.6 119V93.8L622.7 86l23.9-7.8V53.1l14.8 20.3 23.9-7.8-14.8 20.3 14.8 20.3-23.9-7.6zm100.5-23 7.8 23.9-20.4-14.8-20.4 14.8 7.8-23.9-20.4-14.8h25.2l7.8-23.9 7.8 23.9h25.2l-20.4 14.8zM852 93.8V119l-14.8-20.3-23.9 7.8L828 86.1l-14.8-20.3 23.9 7.8L852 53.1v25.1l23.9 7.8-23.9 7.8zm166.9 254.8 23.9 7.8 14.8-20.3v25.1l23.9 7.8-23.9 7.8v25.1l-14.8-20.3-23.9 7.8 14.8-20.3-14.8-20.5zm-94.7-185.7-7.8-23.9h-25.2l20.3-14.8-7.8-23.9 20.3 14.8 20.3-14.8-7.8 23.9 20.3 14.8H932l-7.8 23.9zm55.2 64.1v-25.1l-23.9-7.8 23.9-7.8v-25.2l14.8 20.3 23.9-7.8-14.8 20.3 14.8 20.3-23.9-7.8-14.8 20.6zm45.2 39.4 7.8-23.9 7.8 23.9h25.2l-20.3 14.8 7.8 23.9-20.4-14.8-20.3 14.8 7.8-23.9-20.4-14.8h25zm15.5 205.2-7.8 23.9-7.8-23.9h-25.2l20.4-14.8-7.8-23.9 20.3 14.8 20.4-14.8-7.8 23.9 20.3 14.8h-25zM883 582.2c1.8-2.6 4.7-9.6-.8-22.7l-16.3-43.9c-2.2-5.6 2.6-9 5.9-5.3 0 0 30.9 35.6 38.9 50.4l15.2 25.3c13.1.8 49.2 1.8 84 1.8-3.5-3.5-6.7-7.2-9.7-11.2-59.4-73.6-97-114.5-97.4-114.9-12-13.1-17.6-15.6-26.8-19.8-1.3-.6-2.8-1.3-4.3-2v11.2c.1.8-.4 1.4-1.2 1.5-.6.1-1.2-.3-1.4-.8l-87.3-153.3-.2-.5c-3.6-7.2-9-13.4-15.6-18.1l-8.5-6-41.6 96c5 0 9 4 9 9 0 1.2-.3 2.5-.7 3.6l-38.5 89H721c13.7 0 27.2 2.7 39.8 7.8l9.3 3.8S742 540.9 742 571.3c0 5.5.8 11 2.3 16.4H809l-3-18.2c25.4 5.7 51.1 9.9 77 12.7zm-499.6 93.6c0-59.4-63-88-137.9-88-80.1 0-153.6 35.5-180.6 90.5-7.4 14.7-11.3 30.9-11.3 47.3-.3 14.2 3.6 28.2 11.3 40.2 11.6 17.1 32.2 27.8 62.5 27.8 37.2 0 66.6-20.4 66.6-55.9 0 0 .5-9.9-11-9.9-9.4 0-11.8 6.6-11.6 9.9 1.4 27.8-15.1 50.1-44.6 50.1-33 0-46.8-28.1-46.8-58 0-61.4 46.2-102.1 94.4-119.7 22.5-8.5 46.4-12.7 70.5-12.4 54.5 0 99.1 20.9 99.1 77 0 46.8-39.4 86.7-86.4 90.2l1.9-6.3c9.6-34.4 21.5-72.1 40.7-99.9 1.1-1.7 3-4.4 5.2-7.2l-2.7-3.3c-4.1 2.5-8.1 5.3-11.8 8.3-90.3 70.4-93 268.5-213.3 268.5-4.1 0-8.3-.3-12.4-.8-25-4.1-38.2-20.9-38.2-44.2 0-4.7 1.7-11 1.7-14.6.2-6.6-5-12.2-11.7-12.4H15.4C4.7 853 .3 861.5 0 873.6c-.8 34.9 25 55.3 65 59.2 4.4.3 8.8.5 13.5.5 93.9 0 151.4-71 175.9-157.1 12.4-1.5 24.7-4 36.6-7.7 43.5-12.1 92.4-41.2 92.4-92.7zm894.1 20.6h-33l-7.4 17.3-12.9 29.2h-15.4l-4.7 9.9h16l-19.3 42.6c-13.7 30-35.2 59.4-47.6 59.4-2.7 0-4.4-1.1-4.4-3.8s.8-5.2 3.9-12.9c3.9-9.1 10.2-22.3 14.9-31.9 6.9-14 17.9-35.8 17.9-46.5 0-10.7-6.9-19.3-20.4-19.3-15.1 0-28.9 9.1-41.6 22.3l8.3-19.8h-31.1l-25.3 57.8c-10.2 20.4-30.8 54.2-43.8 54.2-2.7 0-3.9-1.7-3.9-4.4.3-2.5.9-4.9 1.9-7.2 1.1-2.5 16.2-38 16.2-38l27.5-63h-33.6l-26.7 61.3c-8.2 19-29.2 51.2-42.7 51.2-2.4.2-4.4-1.5-4.7-3.8v-1c0-3.3 2.5-9.4 4.4-13.8l14-30.8 28.9-63h-33.3l-6.6 14.3c-4.9 9.6-13.2 20.9-26.4 20.9-6.3 0-9.4-2.5-10.7-5-1.9-21.2-15.4-32.5-35.2-32.5-27.5 0-47.1 16.2-60 36-8.5 13.7-15.1 28.4-19.8 43.7-11.8 19.5-24.2 34.7-34.1 34.7-2.5 0-4.1-1.4-4.1-4.7 0-3.3 3.3-10.7 4.4-13.5l21.7-46.2c6.1-14.3 10.2-23.7 10.2-33 0-9.9-6.9-17.1-18.2-17.1-15.7 0-32.8 9.1-46.2 23.9.5-2.4.6-4.8.5-7.2 0-11-5.5-16.8-16.8-16.8-14.3 0-29.2 8.5-42.7 23.9l8.8-21.5h-30.3l-25.6 57.8c-12.1 27.2-31.7 54.2-42.7 54.2-2.5 0-4.1-1.4-4.1-4.7 0-5.2 5.8-18.2 8-23.4l33.9-76.8c2.5-5.8-13.8-9.4-34.4-9.4-21.2 0-42.9 10.5-58.9 23.9-11.3 9.3-19.5 14-23.7 14-1.3.3-2.7-.6-3-1.9 0-.2-.1-.4-.1-.6 0-4.7 11.3-17.9 11.3-28.1 0-4.7-2.5-7.7-8.8-7.7-12.1 0-26.4 11.6-36.9 23.7l8.8-21.2h-29.7l-25.6 57.8c-12.1 27.2-32.2 55.6-43.2 55.6-2.5 0-4.1-1.4-4.1-4.7 0-5.2 5.5-17.9 8.5-24.5l33.9-77c2.5-5.8-13.8-9.4-34.4-9.4-30.6 0-60.3 20.6-76 41.8-17.3 22.8-29.2 47-29.4 66.9-.3 16 8 25.9 24.5 25.9 18.4 0 33.3-14.6 41.8-25.6-.5 2.2-.9 4.4-1.1 6.6 0 11 4.4 19 17.9 19 11.8 0 27.5-9.9 40.2-25.6L411 872.8h32.2l31.7-71.8c10.5-23.4 22.3-35.5 25.6-35.5.8-.1 1.5.3 1.6 1.1v.3c0 2.5-5 9.1-5 15.1s3.3 10.7 12.1 10.7c6.9 0 14.6-3.3 21.5-7.7-16.2 22-27.3 45.1-27.3 64.1-.3 16 8 25.9 24.5 25.9 17.3 0 33.6-16.5 42.4-27.5-.3 2.6-.5 5.1-.5 7.7 0 10.7 6.1 19.8 18.4 19.8 13.8 0 24.8-8.5 38.5-25.3l-10.2 23.1h33l30.3-68.5c13.2-29.7 31.1-45.7 39.9-45.7 2.2-.2 4.2 1.4 4.4 3.6v.8c-.4 3.3-1.3 6.6-2.8 9.6L678 873.1h33.9l30.8-69.9c13.2-30 27.8-44.6 38.8-44.6 3.3 0 4.7 1.7 4.7 5.2-.3 3.8-1.3 7.6-3 11l-29.7 63.3c-2.7 6.1-4.4 12.6-5 19.3 0 9.6 5.2 18.2 20.1 18.2 19.3 0 33.9-14.6 50.4-36.3v4.7c1.4 17.3 11 32.5 36.6 32.5 30.3 0 54.8-20.9 69.6-54.2 5.6-11.7 9.3-24.3 10.7-37.2 3.3 1.7 7 2.4 10.7 2.2 5 .1 9.9-1.2 14.3-3.6l-5.2 11.3c-6.1 12.7-12.7 26.7-17.9 38.5-3.3 7-5.3 14.6-5.8 22.3 0 11.8 6.6 20.4 20.1 20.4 13.5 0 31.9-12.7 45.1-30.5h.3c-.9 3.7-1.4 7.5-1.4 11.3 0 9.9 3 19.3 16.8 19.3 16 0 28.3-11.6 40.5-26.1l-10.2 23.1h33.3l26.7-60.5c15.1-34.1 30.3-54.7 44.3-54.7 2.4-.1 4.5 1.7 4.7 4.1v.8c0 5.8-8.3 21.5-15.7 37.1-6.9 14.3-12.1 25.3-15.7 33.8-3.3 7.2-5.3 14.9-5.8 22.8 0 10.4 5.8 18.4 18.7 18.4 19.3 0 38.8-18.7 49.2-32.7-2.4 6.7-3.6 13.8-3.8 20.9 0 19.3 11.5 28.9 27.8 28.9 10.8-.1 21.3-3.5 30-9.9 12.7-8.8 22.9-22 31.4-34.1l-5.8-5.5c-8 11.3-16.8 22-25.9 28.6-4.8 4-10.8 6.4-17.1 6.6-6.9 0-11.3-3.6-11.3-12.4s4.1-20.6 10.5-36.6c.3-.3 9.4-20.6 17.9-40.2 7.2-16.5 14.3-32.5 15.7-35.8h21.7l4.4-9.9h-21.5l20.6-46.6zM338.6 855.2c-4.7 0-8-1.6-8-7.7.3-16.2 13.8-45.1 30.6-68.2 11.8-16 27.2-27.8 43.8-27.8l-21 46.7c-15.7 35.3-32.8 57-45.4 57zm205.9 0c-4.7 0-8-1.6-8.3-7.7.3-16.2 13.8-45.1 30.6-68.2 11.8-16 27.2-27.8 43.8-27.8l-20.9 46.8c-16 36-32.3 56.9-45.2 56.9zM910 764.1c-.8 17.9-16.5 61.1-35 86.9-7.4 10.5-13.8 13.5-19.3 13.5-7.7 0-9.9-6.3-8.8-15.7 1.6-16.2 15.1-54.2 33.9-80.3 8.5-11.8 14.3-16.8 20.9-16.8 6.7 0 8.6 5.5 8.3 12.4zm513.7-21.2 30.3-70h-35.9l-30.3 70h-76.3l-12.7 29.3h76.3l-30.3 70h35.9l30.3-70h76.3l12.7-29.3h-76.3z",
                    "hbo": "M7.042 16.896H4.414v-3.754H2.708v3.754H.01L0 7.22h2.708v3.6h1.706v-3.6h2.628zm12.043.046C21.795 16.94 24 14.689 24 11.978a4.89 4.89 0 0 0-4.915-4.92c-2.707-.002-4.09 1.991-4.432 2.795.003-1.207-1.187-2.632-2.58-2.634H7.59v9.674l4.181.001c1.686 0 2.886-1.46 2.888-2.713.385.788 1.72 2.762 4.427 2.76zm-7.665-3.936c.387 0 .692.382.692.817 0 .435-.305.817-.692.817h-1.33v-1.634zm.005-3.633c.387 0 .692.382.692.817 0 .436-.305.818-.692.818h-1.33V9.373zm1.77 2.607c.305-.039.813-.387.992-.61-.063.276-.068 1.074.006 1.35-.204-.314-.688-.701-.998-.74zm3.43 0a2.462 2.462 0 1 1 4.924 0 2.462 2.462 0 0 1-4.925 0zm2.462 1.936a1.936 1.936 0 1 0 0-3.872 1.936 1.936 0 0 0 0 3.872Z"
                  }
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "square": false,
      "columns": 1,
      "type": "grid",
      "cards": [
        {
          "type": "custom:mushroom-title-card",
          "title": "Air Quality"
        },
        {
          "type": "horizontal-stack",
          "cards": [
            {
              "type": "custom:vertical-stack-in-card",
              "styles": {
                "--chip-box-shadow": "none",
                "--chip-background": "none",
                "--chip-spacing": 0
              },
              "cards": [
                {
                  "type": "custom:purifier-card",
                  "entity": "fan.office_of_mike_core_300s",
                  "aqi": {
                    "attribute": "air_quality",
                    "unit": "µg/m³"
                  },
                  "stats": [
                    {
                      "attribute": "filter_life",
                      "unit": "%",
                      "subtitle": "Filter Remaining"
                    },
                    {
                      "value_template": "{% if is_number(state_attr('fan.office_of_mike_core_300s','percentage')) %}\n {{state_attr('fan.office_of_mike_core_300s', 'percentage')}}\n{% else %} \n  5\n{% endif %}\n",
                      "unit": "%",
                      "subtitle": "Motor Speed"
                    },
                    {
                      "value_template": "{{ state_attr('fan.office_of_mike_core_300s', 'mode') | title }}\n",
                      "subtitle": "Mode"
                    }
                  ],
                  "shortcuts": [
                    {
                      "name": "Silent",
                      "icon": "mdi:weather-night",
                      "preset_mode": "sleep"
                    },
                    {
                      "name": "25%",
                      "icon": "mdi:circle-slice-2",
                      "percentage": 25
                    },
                    {
                      "name": "50%",
                      "icon": "mdi:circle-slice-4",
                      "percentage": 66
                    },
                    {
                      "name": "100%",
                      "icon": "mdi:circle-slice-8",
                      "percentage": 100
                    },
                    {
                      "name": "Auto",
                      "icon": "mdi:brightness-auto",
                      "preset_mode": "auto"
                    }
                  ],
                  "show_name": false,
                  "show_state": false,
                  "show_toolbar": true,
                  "compact_view": true
                },
                {
                  "type": "entities",
                  "entities": [
                    {
                      "type": "custom:fold-entity-row",
                      "head": {
                        "entity": "sensor.mikes_office_airthings_temperature",
                        "show_state": false,
                        "type": "custom:multiple-entity-row",
                        "name": "AQI",
                        "secondary_info": "last-updated",
                        "style": ":host .entities-row {\n  justify-content: flex-start;\n  align-items: unset;\n}\n:host .entities-row div.entity:nth-child(1) div::after {\n  color: var(--secondary-text-color);\n  font-size: 0.7rem;\n  content: \"\\A {{relative_time(strptime(states.sensor.office_of_mike_humidity.last_changed,\"%H:%M:%S %d/%m/%Y\"))}}\";\n  white-space: pre;\n}\n:host .entities-row div.entity:nth-child(2) div::after {\n  color: var(--secondary-text-color);\n  font-size: 0.7rem;\n  content: \"\\A {{relative_time(strptime(states.sensor.office_of_mike_temperature_2.last_changed,\"%H:%M:%S %d/%m/%Y\"))}}\";\n  white-space: pre;\n}\n:host .entities-row div.entity:nth-child(3) div::after {\n  color: var(--secondary-text-color);\n  font-size: 0.7rem;\n  content: \"\\A {{relative_time(strptime(states.sensor.office_of_mike_voc.last_changed,\"%H:%M:%S %d/%m/%Y\"))}}\";\n  white-space: pre;\n}\n:host .entities-row div.entity:nth-child(4) div::after {\n  color: var(--secondary-text-color);\n  font-size: 0.7rem;\n  content: \"\\A {{relative_time(strptime(states.sensor.office_of_mike_pm1.last_changed,\"%H:%M:%S %d/%m/%Y\"))}}\";\n  white-space: pre;\n}\n:host .entities-row div.entity:nth-child(5) div::after {\n  color: var(--secondary-text-color);\n  font-size: 0.7rem;\n  content: \"\\A {{relative_time(strptime(states.sensor.office_of_mike_pm25.last_changed,\"%H:%M:%S %d/%m/%Y\"))}}\";\n  white-space: pre;\n}\n",
                        "entities": [
                          {
                            "entity": "sensor.mikes_office_airthings_humidity",
                            "name": "Humidity"
                          },
                          {
                            "entity": "sensor.mikes_office_airthings_temperature",
                            "name": "Temp"
                          },
                          {
                            "entity": "sensor.mikes_office_airthings_voc",
                            "name": "VOC"
                          },
                          {
                            "entity": "sensor.mikes_office_airthings_pm1",
                            "name": "PM1"
                          },
                          {
                            "entity": "sensor.mikes_office_airthings_pm25",
                            "name": "PM2.5"
                          }
                        ]
                      },
                      "entities": [
                        {
                          "type": "custom:mini-graph-card",
                          "style": {
                            ".": "ha-card {\n  --ha-card-box-shadow: none;\n  background-color: transparent;\n  border-radius: none;\n\n}\n",
                            "#states > div > mini-graph-card": {
                              "$": "ha-card {\n  background-color: transparent;\n}\n"
                            }
                          },
                          "entities": [
                            {
                              "entity": "sensor.mikes_office_airthings_humidity",
                              "name": "Humidity",
                              "color": "#4c7daf"
                            }
                          ],
                          "hours_to_show": 168,
                          "line_width": 3,
                          "font_size": 50,
                          "animate": true,
                          "show": {
                            "name": true,
                            "icon": true,
                            "state": true,
                            "legend": false,
                            "fill": "fade"
                          }
                        },
                        {
                          "type": "custom:mini-graph-card",
                          "style": {
                            ".": "ha-card {\n  --ha-card-box-shadow: none;\n  background-color: transparent;\n  border-radius: none;\n\n}\n",
                            "#states > div > mini-graph-card": {
                              "$": "ha-card {\n  background-color: transparent;\n}\n"
                            }
                          },
                          "entities": [
                            {
                              "entity": "sensor.mikes_office_airthings_temperature",
                              "name": "Temp",
                              "color": "#af6b4c"
                            }
                          ],
                          "hours_to_show": 168,
                          "line_width": 3,
                          "font_size": 50,
                          "animate": true,
                          "show": {
                            "name": true,
                            "icon": true,
                            "state": true,
                            "legend": false,
                            "fill": "fade"
                          }
                        },
                        {
                          "type": "custom:mini-graph-card",
                          "style": {
                            ".": "ha-card {\n  --ha-card-box-shadow: none;\n  background-color: transparent;\n  border-radius: none;\n\n}\n",
                            "#states > div > mini-graph-card": {
                              "$": "ha-card {\n  background-color: transparent;\n}\n"
                            }
                          },
                          "entities": [
                            {
                              "entity": "sensor.mikes_office_airthings_voc",
                              "name": "VOC",
                              "color": "#4caf4e"
                            }
                          ],
                          "hours_to_show": 168,
                          "line_width": 3,
                          "font_size": 50,
                          "animate": true,
                          "show": {
                            "name": true,
                            "icon": true,
                            "state": true,
                            "legend": false,
                            "fill": "fade"
                          }
                        },
                        {
                          "type": "custom:mini-graph-card",
                          "style": {
                            ".": "ha-card {\n  --ha-card-box-shadow: none;\n  background-color: transparent;\n  border-radius: none;\n\n}\n",
                            "#states > div > mini-graph-card": {
                              "$": "ha-card {\n  background-color: transparent;\n}\n"
                            }
                          },
                          "entities": [
                            {
                              "entity": "sensor.mikes_office_airthings_pm1",
                              "name": "PM1",
                              "color": "#844caf"
                            },
                            {
                              "entity": "sensor.mikes_office_airthings_pm25",
                              "name": "PM25",
                              "color": "#af8e4c"
                            }
                          ],
                          "hours_to_show": 168,
                          "line_width": 3,
                          "font_size": 50,
                          "animate": true,
                          "show": {
                            "name": true,
                            "icon": true,
                            "state": true,
                            "legend": false,
                            "fill": "fade"
                          }
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "square": false,
      "columns": 1,
      "type": "grid",
      "cards": [
        {
          "type": "entities",
          "style": "ha-card {\n  --ha-card-box-shadow: none;\n  background: transparent !important;\n  border-radius: none;\n}\n",
          "entities": [
            {
              "type": "custom:fold-entity-row",
              "style": ":host {\n  --ha-card-box-shadow: none;\n  background: transparent !important;\n  border-radius: none;\n}\n",
              "head": {
                "type": "custom:vertical-stack-in-card",
                "style": "ha-card {\n  --ha-card-box-shadow: none;\n  background: transparent !important;\n  border-radius: none;\n  color: red;\n}\n",
                "cards": [
                  {
                    "type": "custom:mini-media-player",
                    "style": ":host {\n  --ha-card-box-shadow: none;\n  background: transparent !important;\n  border-radius: none;\n}\n",
                    "entity": "media_player.spotify_michael_hanley",
                    "info": "scroll",
                    "source": "full",
                    "artwork": "full-cover",
                    "group": true,
                    "sound_mode": "full",
                    "replace_mute": "stop"
                  }
                ]
              },
              "entities": [
                {
                  "type": "custom:mini-media-player",
                  "style": ":host {\n  --ha-card-box-shadow: none;\n  background: transparent !important;\n  border-radius: none;\n}\n",
                  "entity": "media_player.office_of_mike_echo",
                  "artwork": "none",
                  "tts": {
                    "platform": "alexa"
                  },
                  "volume_stateless": false,
                  "toggle_power": false,
                  "group": true
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

These objects support rollback only for their named existing views. They do not establish complete dashboard ordering, unrelated-view state, or a rollback payload for the four proposed paths.

## Dashboard Resources

- Registered resources: 63 total; 63 returned.
- Resource types: module: 62, js: 0, css: 1.
- Inline resources: 0.
- Pagination: complete.
- Resource URLs and bodies are intentionally excluded.

## Lower Level and Reusable View Baselines

- Areas directory path `living-areas` exists.
- Reusable paths `utility_room`, `server-room`, and `office-of-mike` exist.
- `utility_room` and `server-room` are not currently subviews; `office-of-mike` is a subview.
- `server-room` has no top-level cards in the scoped baseline.
- The exact seven target areas each have one live registry record on floor ID `basement`; none is unassigned or orphaned.
- No generic area named `Basement` was found.

## Secret Review

The persisted artifact contains no dashboard body, resource URL/body, token, credential, cookie, private URL, calendar/event content, or personal device-tracker/image record. Entity detail is intentionally limited to dashboard-candidate records in the companion entity map.

## Rollback Procedure

### Existing-View, Scoped Restore Strategy

The verified existing paths are `living-areas`, `utility_room`, `server-room`, and `office-of-mike`. Before changing any one of them, obtain renewed explicit approval to read that exact view and capture its complete literal view payload in an approved secure rollback location. Preserve the fresh config hash from that read.

If that individual view's write or read-back fails, stop dependent work. Present the exact supported dashboard restore operation that replaces only the affected view with its freshly captured literal payload, guarded by the matching fresh config hash, and obtain separate approval before applying it. Then read back that exact view and verify its path, subview flag, key cards, and navigation.

### Limitations

Complete literal payloads for all four existing views were not retained from the earlier safe structural reads. They require renewed scoped Home Assistant reads before a view-specific rollback can be executed. The discarded broad dashboard response remains unavailable, so this snapshot is not a complete dashboard restore payload and cannot establish a rollback for unrelated views or unverified new paths.
