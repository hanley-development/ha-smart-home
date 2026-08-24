# Basement Device Area Migration

Status: Proposed; not applied to Home Assistant.

## Purpose

Move every device currently documented in `docs/zones/basement/basement.md` out of the generic Basement area:

- Sense integration devices move to Energy.
- All other devices move to Basement Entertainment.

This changes Home Assistant device-registry organization only. It does not rename entities or devices and does not control physical devices.

## Pre-change snapshot

- Source: `docs/zones/basement/basement.md`
- Current area ID: `basement`
- Rollback: assign every device below back to `basement`

## Target: Energy

Target area ID: `energy`

| Device | Integration | Device ID |
|---|---|---|
| Basement Entertainment Outlet 5 | sense | `33a960e1204bd76baf7d81e5afa7dac9` |
| Basement Entertainment Outlet 6 | sense | `58040579a15e84f9f5ca0f7d8fe01497` |

## Target: Basement Entertainment

Target area ID: `basement_entertainment`

| Device | Integration | Device ID |
|---|---|---|
| Basement Bar Light | zwave_js | `43dff434ef45af9c228b2e1d0be5274d` |
| Basement Core 400 | vesync | `8783729d922d632a7ca48785dd126195` |
| Basement Echo | alexa_media | `06c6c34df5a70a7ca495b1f122fa01ae` |
| Basement Entertainment Surge Protector | unknown | `83c0f9e8ee312f47d027e6a0438bb821` |
| Basement Hallway Light | zwave_js | `5f2a916e6391b5ef7f7870b1bfbfeef2` |
| Basement Living Room Fan | zigbee2mqtt | `1a7e2cf8716fb2232f4db9c239616f6b` |
| Basement Living Room Fan Light | zwave_js | `8e7537323b71c98f358ff0600656ee21` |
| Basement Living Room Nightlight Motion | zigbee2mqtt | `0778b990736dfe32ea44d88985029d77` |
| Basement Living Room Surge Protector | unknown | `c6af9bea46ed22f333395448ecf4c2bd` |
| Basement Main Light | zwave_js | `82a109e57f9455fe4a75e763093b3dcf` |
| Basement Mini-Fridge | zwave_js | `6540f2b1306c534fe9f7771289c50df2` |
| Basement Samsung TV | unknown | `fe58b94aed1e20c94ba7f1d38b60004d` |
| Basement Stairs Light | zwave_js | `94ca989a1ba7e164555736e2a89897ae` |
| Onkyo-TX-NR7100 | unknown | `d42475e3ab7fc67d3e013f71b68159aa` |
| Samsung QN90CA 85 | samsungtv | `fc9201036e841a7ba82711a562a42c75` |
| Samsung QN90CA 85 | unknown | `e091e3f8cba1432fb6b88c5aa4c4c8cf` |

## Expected effects

- Entities without their own explicit area may inherit the new device area.
- Dashboard and voice-assistant room grouping may change.
- Integrations that expose duplicate representations remain separate registry devices.
- No device state, service, automation, entity ID, or device name should change.

## Apply sequence

1. Confirm all 18 devices are still assigned to `basement`.
2. Confirm target areas `energy` and `basement_entertainment` still exist.
3. Push this reviewed proposal and the pre-change snapshot after explicit approval.
4. Apply the 18 exact `ha_set_device` area updates after explicit approval.
5. Read all 18 devices back and verify their target area IDs.
6. Refresh `docs/zones/basement/` from live Home Assistant.
7. If verification fails, assign the affected device back to `basement`.
