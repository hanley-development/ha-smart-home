# Known Issues

Current issues identified during Home Assistant organization work.

## Resolved

- `1st_foor` was fully replaced by `1st_floor`.
  Verified on 2026-04-23: `1st_foor` no longer exists and no areas, entities, or devices still reference it.

- `notifications` was renamed to `Notifications`.
  Verified on 2026-04-23: the label name is title-cased and its existing entity assignments were preserved.

## Notes

- Check for any dashboards, automations, or organization rules that rely on the current naming.
