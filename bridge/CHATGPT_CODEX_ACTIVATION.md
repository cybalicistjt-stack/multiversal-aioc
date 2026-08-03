# Activate the Multiversal AIOC Bridge in ChatGPT and Codex

## Production endpoints

- MCP server: `https://aioc-mcp-bridge-production.up.railway.app/mcp`
- Health: `https://aioc-mcp-bridge-production.up.railway.app/health`
- Live verification: `https://aioc-mcp-bridge-production.up.railway.app/live-verification`

The production bridge is currently read-only. It can inspect canonical content, shared working state, and the live AIOC deployment. It cannot modify GitHub or shared state until write credentials and approval controls are deliberately enabled.

## ChatGPT private app connection

This is a one-time account or workspace action:

1. Open ChatGPT settings for Apps, Connectors, or Developer Mode.
2. Choose the option to create or connect a private/custom MCP app.
3. Name it `Multiversal AIOC`.
4. Enter the MCP URL:
   `https://aioc-mcp-bridge-production.up.railway.app/mcp`
5. Authentication: none for the current read-only bridge.
6. Set permissions to allow reads and require approval before writes. Writes are also disabled server-side.
7. Save or connect the app.
8. Start a new conversation and ask:
   `Use Multiversal AIOC to verify the live deployment.`
9. Confirm the app exposes tools including `aioc_status`, `inspect_aioc_live_deployment`, and `verify_aioc_live_deployment`.

Private-app registration is performed in the ChatGPT account/workspace UI and cannot be completed by repository code alone.

## Codex activation

The repository includes `.codex/config.toml` with the production MCP server. When Codex opens this repository:

1. Allow the repository MCP configuration when prompted.
2. Read `AGENTS.md` and `bridge/skills/multiversal-aioc/SKILL.md`.
3. Confirm the `multiversal_aioc` MCP server is connected.
4. Run `aioc_status`.
5. Run `verify_aioc_live_deployment` before and after deployment-affecting work.

If a Codex installation does not automatically read repository `.codex/config.toml`, add the same server to the user Codex configuration:

```toml
[mcp_servers.multiversal_aioc]
url = "https://aioc-mcp-bridge-production.up.railway.app/mcp"
```

## Verification standard

A deployment-affecting task is complete only when the bridge reports:

- the live deployment is reachable;
- required AIOC routes and assets pass;
- the live database has 487 records unless the certified contract intentionally changes;
- the deployed commit matches the expected repository commit;
- the result is `PASS` rather than `FAIL` or `DEGRADED`.

CI success alone is not sufficient.

## Future write activation

Do not enable writes merely by changing `AIOC_ALLOW_WRITES`.

Before write activation, add:

1. A least-privilege GitHub credential stored only in Railway secrets.
2. Authentication for the MCP endpoint.
3. Per-tool approval requirements.
4. Revision-conflict handling tests.
5. Audit logging and rollback verification.
6. Separate proposal, shared-draft, and canonical-promotion permissions.

Canonical content promotion must remain owner-approved and independently certified.
