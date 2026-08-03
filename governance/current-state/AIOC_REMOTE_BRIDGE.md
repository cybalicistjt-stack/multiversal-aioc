# Multiversal AIOC Remote Bridge

**Status:** DEPLOYED_READ_ONLY  
**Recorded:** 2026-08-03

## Hosted service

- Provider: Railway
- Project: Multiversal AIOC Bridge
- Service: aioc-mcp-bridge
- Environment: production
- Base URL: https://aioc-mcp-bridge-production.up.railway.app
- MCP endpoint: https://aioc-mcp-bridge-production.up.railway.app/mcp
- Health endpoint: https://aioc-mcp-bridge-production.up.railway.app/health
- Live verification endpoint: https://aioc-mcp-bridge-production.up.railway.app/live-verification

## Current security mode

- Repository: cybalicistjt-stack/multiversal-aioc
- Ref: main
- Writes: disabled
- GitHub write token: not configured
- Shared-state mutation: unavailable until authenticated write configuration is approved

## Available bridge capabilities

- Read canonical AIOC status and current state
- Search canonical content
- Fetch canonical objects
- Read shared working state
- List and fetch shared working objects
- Inspect live Pages deployment
- Run bounded live route and content smoke checks
- Compare live deployment commit with repository main
- Create governed write proposals only after write credentials and explicit policy are enabled

## Verification authority

Railway deployment `db88bbcc-7d14-4c07-9a7b-24b7c0746d65` completed successfully after configuring:

- root directory `bridge/mcp-server`
- build command `npm install --no-audit --no-fund`
- start command `npm start`
- health check `/health`
- continuous production runtime

The Railway internal health gate passed. External DNS was not yet resolvable from the ChatGPT execution environment at the time this record was written, so direct external rendering remains to be confirmed after DNS propagation.

## Next activation steps

1. Connect the MCP endpoint as a private ChatGPT custom app.
2. Add the same endpoint to Codex MCP configuration.
3. Verify read tools from both products.
4. Add authenticated browser synchronization.
5. Configure least-privilege GitHub credentials and enable proposal/shared-state writes only after owner approval.
