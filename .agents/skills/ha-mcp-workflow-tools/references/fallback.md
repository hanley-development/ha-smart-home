# Fallback Workflow

## Scope

Use for error handling and safe fallback behavior.

## Failure handling

When a tool fails:

1. Report the failure plainly.
2. Do not guess the result.
3. Try a narrower read-only tool if appropriate.
4. If the required tool is unavailable, explain which capability is missing.
5. Provide a safe manual/UI path only when useful.
6. Do not retry destructive/write actions by guessing.

## Ambiguity handling

If targets are ambiguous:

- present the shortlist
- ask one concise clarification
- do not write/control until resolved

## Unsafe request handling

For unsafe or destructive requests:

- explain the risk
- ask for exact confirmation
- offer a safer read-only or notification-only alternative

## Tool availability

Some ha-mcp capabilities may depend on optional custom components or feature flags, especially filesystem/YAML editing tools.

If file/YAML tools are unavailable, prefer UI-managed MCP tools and repo documentation snapshots.
