# Safe Refactoring Guide

## Goals

Refactoring should preserve behavior unless explicitly changing it.

## Rules

- Make small changes.
- Avoid broad formatting-only rewrites.
- Preserve comments.
- Preserve entity IDs.
- Preserve automation IDs.
- Preserve unique IDs.
- Preserve aliases unless asked.
- Do not delete helpers or entities without approval.
- Do not rename entities without approval.

## Do not change without explicit instruction

- entity IDs
- unique IDs
- device names
- helper names
- automation IDs
- script IDs
- ESPHome device names
- ESPHome static IPs
- API/OTA/Wi-Fi settings
- dashboard storage
