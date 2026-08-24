# Custom Card Repositories

## Purpose

This file tracks custom Home Assistant dashboard cards that may be used in this project.

The agent should use this file as a reference only.

Before using a custom card:

- confirm the card is installed through MCP, HACS, dashboard resources, or existing dashboard inspection
- prefer built-in cards when they solve the problem cleanly
- use custom cards only when they provide a clear dashboard benefit
- do not invent card syntax
- do not use stale or unmaintained cards for critical controls unless explicitly approved

## Card status labels

Use these labels:

- `preferred` — good default custom card for this project
- `use-case` — useful for specific situations
- `optional` — nice to have, not required
- `caution` — use carefully
- `legacy` — avoid unless already installed and working
- `unknown` — needs review

## Cards

| Card                                     | Status    | HACS / Repo                                      | Card Type          | Best Used For                                   | Notes                                                      |
| ---------------------------------------- | --------- | ------------------------------------------------ | ------------------ | ----------------------------------------------- | ---------------------------------------------------------- |
| Mushroom                                 | preferred | [piitaya/lovelace-mushroom](https://github.com/piitaya/lovelace-mushroom) | Cards Collection   | mobile dashboards, chips, rooms, clean controls | Confirm installed before use                               |
| Bubble Card                              | preferred | [Clooos/Bubble-Card](https://github.com/Clooos/Bubble-Card) | Cards Collection   | mobile-first layouts, pop-ups, compact controls | Avoid hiding critical controls in unclear pop-ups          |
| auto-entities                            | preferred | [thomasloven/lovelace-auto-entities](https://github.com/thomasloven/lovelace-auto-entities) | Helper Card        | dynamic lists                                   | Great for low batteries, unavailable devices, open doors   |
| card-mod                                 | caution   | [thomasloven/lovelace-card-mod](https://github.com/thomasloven/lovelace-card-mod) | Styling Tool       | styling                                         | Use sparingly; avoid fragile CSS-heavy dashboards          |
| Battery State Card / Entity Row          | use-case  | [cyberjunky/home-assistant-custom-components](https://github.com/cyberjunky/home-assistant-custom-components) | Entity Row / Card  | battery maintenance views                       | Useful for low battery dashboards                          |
| Navbar Card                              | use-case  | [thomasloven/lovelace-navbar](https://github.com/thomasloven/lovelace-navbar) | Navigation         | mobile navigation                               | Good for bottom nav / side nav                             |
| Vertical Stack In Card                   | optional  | [ofekashery/vertical-stack-in-card](https://github.com/ofekashery/vertical-stack-in-card) | Layout Card        | visual grouping                                 | Avoid deep nesting                                         |
| Stack In Card                            | optional  | [custom-cards/stack-in-card](https://github.com/custom-cards/stack-in-card) | Layout Card        | visual grouping                                 | Avoid deep nesting                                         |
| Config Template Card                     | caution   | [thomasloven/lovelace-config-template-card](https://github.com/thomasloven/lovelace-config-template-card) | Helper Card        | templated cards                                 | Use only when truly needed                                 |
| state-switch                             | caution   | [thomasloven/lovelace-state-switch](https://github.com/thomasloven/lovelace-state-switch) | Helper Card        | user/device/mode-specific views                 | Can make dashboards harder to troubleshoot                 |
| Custom Features for Home Assistant Cards | use-case  | [thomasloven/lovelace-card-features](https://github.com/thomasloven/lovelace-card-features) | Features Extension | extending Tile cards                            | Good if it improves usability                              |
| status-card                              | use-case  | [iantrich/status-card](https://github.com/iantrich/status-card) | Status Card        | status summaries                                | Good for maintenance/network views                         |
| Gauge Card Pro                           | use-case  | [rianadon/lovelace-gauge-card-pro](https://github.com/rianadon/lovelace-gauge-card-pro) | Gauge Card         | visual gauges                                   | Good for power, battery, storage, UPS                      |
| Entity Progress Card                     | use-case  | [custom-cards/entity-progress-card](https://github.com/custom-cards/entity-progress-card) | Progress Card      | progress-style values                           | Good for battery/storage/tank levels                       |
| area-card-plus                           | use-case  | [gurumike/area-card-plus](https://github.com/gurumike/area-card-plus) | Area Card          | area summaries                                  | Good for room/area cards                                   |
| Device Card                              | use-case  | [custom-cards/device-card](https://github.com/custom-cards/device-card) | Device Card        | device summaries                                | Good for servers/network/appliances                        |
| Light Entity Card                        | use-case  | [custom-cards/light-entity-card](https://github.com/custom-cards/light-entity-card) | Light Card         | light control                                   | Use if better than built-in Tile/Mushroom                  |
| Simple Thermostat                        | caution   | [nathanielhass/simple-thermostat](https://github.com/nathanielhass/simple-thermostat) | Climate Card       | climate controls                                | Check maintenance before using for new critical dashboards |
| Weather Chart Card                       | use-case  | [bramkragten/weather-card](https://github.com/bramkragten/weather-card) | Weather Card       | weather charts                                  | Good for weather/climate view                              |
| Simple Weather Card                      | legacy    | [kalkih/simple-weather-card](https://github.com/kalkih/simple-weather-card) | Weather Card       | simple weather                                  | Check maintenance before new use                           |
| Horizon Card                             | use-case  | [sersorrel/lovelace-horizon-card](https://github.com/sersorrel/lovelace-horizon-card) | Sun Card           | sun position                                    | Useful for sunrise/sunset visibility                       |
| Firemote Card                            | use-case  | [jcwillox/lovelace-firemote](https://github.com/jcwillox/lovelace-firemote) | Remote Card        | media remotes                                   | Use only for relevant media devices                        |
| TV Remote Card                           | use-case  | [custom-cards/tv-remote-card](https://github.com/custom-cards/tv-remote-card) | Remote Card        | TV/media remote                                 | Use only for relevant media devices                        |
| Xiaomi Vacuum Map Card                   | use-case  | [PiotrMachowski/lovelace-xiaomi-vacuum-map-card](https://github.com/PiotrMachowski/lovelace-xiaomi-vacuum-map-card) | Vacuum Card        | map-based vacuum control                        | Confirm vacuum compatibility                               |
| Purifier Card                            | use-case  | [aneisch/lovelace-purifier-card](https://github.com/aneisch/lovelace-purifier-card) | Purifier Card      | purifier controls                               | Use only if purifier integration exists                    |
| surveillance-card                        | caution   | [custom-cards/surveillance-card](https://github.com/custom-cards/surveillance-card) | Camera Card        | camera grid                                     | Check maintenance before relying on it                     |
| Custom Brand Icons                       | optional  | [vigonotion/hass-brand-icons](https://github.com/vigonotion/hass-brand-icons) | Icons              | visual polish                                   | Do not make functionality depend on icons                  |
| Text Divider Row                         | optional  | [thomasloven/lovelace-text-divider-row](https://github.com/thomasloven/lovelace-text-divider-row) | Helper Row         | visual separation                               | Mostly useful in entity lists                              |
| Entity Attributes Card                   | use-case  | [custom-cards/entity-attributes-card](https://github.com/custom-cards/entity-attributes-card) | Attributes Card    | diagnostics                                     | Avoid on family-facing dashboards                          |
| Mail and Packages Custom Card            | legacy    | [custom-cards/mail-and-packages-card](https://github.com/custom-cards/mail-and-packages-card) | Mail Card          | mail/packages                                   | Check maintenance and sensors first                        |
| Roomba Vacuum Card                       | legacy    | [custom-cards/roomba-vacuum-card](https://github.com/custom-cards/roomba-vacuum-card) | Vacuum Card        | Roomba control                                  | Prefer newer/general vacuum cards if possible              |

## Usage rule

Do not choose a custom card because it is popular.

Choose it because it makes the dashboard:

- safer
- clearer
- easier to use
- easier to maintain
- better on mobile

## Critical-control rule

For critical controls, prefer built-in or well-maintained cards.

Critical controls include:

- locks
- garage doors
- alarm systems
- HVAC
- cameras
- water valves
- sirens
- security modes

Do not use stale, abandoned, or unknown custom cards for critical controls unless explicitly approved.

## Maintenance notes

When reviewing this file, prefer official upstream repositories, HACS default entries, or the current installed HACS metadata.

If a repository appears abandoned, mark it as `legacy` or `caution`.

If the correct repo/card type is unknown, keep `TODO` until verified.
