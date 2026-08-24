# Basement Zone

> Read-only Home Assistant inventory captured 2026-08-24. No devices or configuration were changed.

This directory inventories devices and entities assigned to the Home Assistant `Basement` floor, plus unassigned or outside-area records whose device name, entity ID, or friendly name contains `basement`.

## Summary

| Area | Floor classification | Devices | Entities | Inventory |
|---|---|---:|---:|---|
| Basement | Basement | 18 | 692 | [View](basement.md) |
| Home-Assistant | Basement | 111 | 469 | [View](home-assistant.md) |
| Mikes Office | Basement | 22 | 401 | [View](mikes-office.md) |
| Network | Basement | 20 | 533 | [View](network.md) |
| Server Room | Basement | 20 | 172 | [View](server-room.md) |
| Utility Room | Basement | 12 | 225 | [View](utility-room.md) |
| Basement Bathroom | Basement | 4 | 309 | [View](basement-bathroom.md) |
| Basement Entertainment | Basement | 22 | 174 | [View](basement-entertainment.md) |
| Unassigned | Unassigned | 3 | 27 | [View](unassigned.md) |
| Energy | Outside Basement floor | 0 | 10 | [View](energy.md) |
| Security | Outside Basement floor | 1 | 20 | [View](security.md) |
| **Total** |  | **233** | **3,032** |  |

## Scope

- The Basement floor currently contains 8 areas: Basement, Home-Assistant, Mikes Office, Network, Server Room, Utility Room, Basement Bathroom, Basement Entertainment.
- Basement-floor area files include all devices and entities assigned to that area.
- Unassigned and outside-area files include only records with `basement` in the device name, entity ID, or friendly name.
- Entity states are intentionally omitted because they are transient and may contain sensitive or noisy values.
- Device registry IDs are included as stable lookup references; credentials, connection URLs, hardware addresses, and serial numbers are omitted.

## Notes

- Alexa, Sense, discovery, and other integrations can create secondary or virtual representations of the same physical device.
- A Basement-related record outside the Basement floor is not automatically misconfigured; review integration ownership before changing its area.
- This is a point-in-time documentation snapshot, not authoritative live Home Assistant configuration.
