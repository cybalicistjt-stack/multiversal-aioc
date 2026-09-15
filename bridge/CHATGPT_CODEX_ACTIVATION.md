# ChatGPT / Codex AIOC Executor Adapter

**Disposition:** EXECUTOR_ADAPTER — not an authority or work selector.

Before using AIOC MCP, Codex configuration, live-deployment inspection, or any other executor capability, enter the project through:

`operations/BOOTSTRAP.md`

The selected lane/work item determines whether these capabilities are relevant. This adapter never chooses current work and never overrides `operations/CURRENT.json` or `operations/OPERATING_CONTRACT.md`.

## AIOC capability notes

- Repository content and connected AIOC tools can provide implementation or deployment evidence when the selected lane needs them.
- A successful CI/deployment status is evidence, not authority.
- Shared working state and browser-local state are separate from canonical repository content.
- Mutating external state requires the authority already granted by the selected work item and the connected tool's own permissions.

If the AIOC MCP or another executor is unavailable, preserve the same work item and use another lawful executor/evidence path when possible. Do not create a replacement governance path.
