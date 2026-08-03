# Multiversal AIOC Bridge

The AIOC Bridge makes the governed Multiversal development system available natively to ChatGPT and Codex through a remote Model Context Protocol (MCP) server.

## Architecture

The bridge is intentionally split into three layers:

1. **Canonical repository layer** — certified content, governance, current state, receipts, and approved changes stored in GitHub.
2. **Remote MCP layer** — typed read and proposal tools exposed at `/mcp` for ChatGPT and Codex.
3. **AIOC browser layer** — the existing operational UI, Content Structure Pipeline, Completion Assistant, Library, and Design Studio.

Browser `localStorage` is not remotely accessible. Working drafts and structure decisions must therefore be migrated to shared server-side storage before ChatGPT or Codex can read and edit them across devices. Until that migration is implemented, the bridge reads canonical repository data and writes governed proposals rather than directly mutating certified objects.

## Phase 1 tools

- `aioc_status`
- `search_aioc_content`
- `get_aioc_object`
- `get_aioc_current_state`
- `create_aioc_change_proposal`

The proposal tool writes reviewable JSON records under `governance/bridge-proposals/`. It does not directly modify canonical content.

## Local run

```bash
cd bridge/mcp-server
npm install
npm run check
npm start
```

Default endpoint:

```text
http://localhost:8787/mcp
```

Health endpoint:

```text
http://localhost:8787/health
```

## Environment

```text
PORT=8787
AIOC_GITHUB_REPOSITORY=cybalicistjt-stack/multiversal-aioc
AIOC_GITHUB_REF=main
AIOC_ALLOW_WRITES=false
GITHUB_TOKEN=
```

For read-only use, no token is required while the repository remains public. For proposal writes, set `AIOC_ALLOW_WRITES=true` and provide a narrowly scoped GitHub token with repository contents permission.

## Deployment

GitHub Pages cannot host an MCP server. Deploy `bridge/mcp-server` to a Node-capable remote host such as Railway, Render, Fly.io, or another HTTPS service. ChatGPT connects to remote MCP servers; a private server can instead be exposed through a supported secure MCP tunnel.

## Planned phases

### Phase 2 — shared working state

Move browser-only working objects, structure decisions, pack lists, balance evidence, and testing evidence into an authenticated shared store. The browser UI becomes one client of that store, and ChatGPT/Codex become additional clients.

### Phase 3 — governed mutation tools

Add tools for:

- creating and updating working copies;
- recording structure decisions;
- assigning parents and relationships;
- running validation;
- producing review packages;
- approving promotion;
- triggering certification and deployment.

Mutations remain proposal-first and require explicit approval where appropriate.

### Phase 4 — ChatGPT app UI

Add an Apps SDK widget for queue review, object inspection, structure classification, and approval. Data tools remain reusable without the widget.

### Phase 5 — plugin and Codex skill

Package the MCP app together with an AIOC operating skill so ChatGPT and Codex understand the canonical workflow:

```text
Structure → Completion → Design Studio → Balance/Testing → Review Package → Approval → Promotion → Certification
```
