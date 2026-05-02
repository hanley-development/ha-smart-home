# Entity Discovery

## Scope

Use this workflow for read-only discovery:

- find entities by natural language
- list or filter entities by domain
- resolve entities by area or label
- validate current states before writing automations or dashboards
- find likely target entities for service calls
- inspect device/entity registry details

## Preferred tools

Use:

- `ha_search_entities` for natural-language and fuzzy entity lookup
- `ha_get_state` for current state and attributes
- `ha_get_entity` for registry/entity details
- `ha_get_device` for device details
- `ha_get_overview` for system/entity overview
- `ha_deep_search` for broad config/search requests
- `ha_config_list_areas` / `ha_list_floors_areas` for area/floor context
- `ha_config_get_label` for label context when a label is named

## Flow

1. Parse the user's target phrase into likely domains, areas, labels, and keywords.
2. Search with `ha_search_entities`.
3. If the request references an area or label, inspect that area/label before choosing entities.
4. For every entity that may be used in a write/control action, verify:
   - entity_id
   - friendly name
   - domain
   - state
   - relevant attributes
   - area/device, when available
5. If multiple entities match, ask one concise clarification or present the shortlist.
6. Never guess an entity ID.

## Output format

For discovery results, return:

- matched entity IDs
- friendly names
- current state
- why each is relevant
- ambiguity, if any
- next safe action
