# LXG-01 — Local Execution Gateway for ChatGPT and Local Agents

**Work order ID:** LXG-01  
**Status:** OWNER-AUTHORIZED PARALLEL DEVELOPER INFRASTRUCTURE  
**Lifecycle intent:** CURRENT_COMPATIBLE while implementation/setup is active  
**Approved:** 2026-09-10  
**Product implementation authority:** none  
**Current product selector:** unchanged; `CURRENT_WORK_POINTER.json` remains authoritative  

## Purpose

Turn the completed MLR-01 workstation into a governed local compute fabric that ordinary ChatGPT conversations, Codex, Goose and local scripts can use through one stable Model Context Protocol (MCP) gateway.

The gateway exists so frontier-agent credits are not required merely to invoke deterministic tools, local retrieval, local inference or other already-installed workstation capabilities.

LXG-01 is developer infrastructure. It does not own game state, canon, content rights, repository authority, provider selection, or any gameplay domain.

## OpenAI product compatibility basis

As of 2026-09-10, current OpenAI documentation supports custom MCP apps in ChatGPT developer mode. ChatGPT does not connect directly to ordinary localhost MCP endpoints; a private/on-premises/developer-machine server is connected through Secure MCP Tunnel or another approved remote HTTPS deployment path. Full MCP write/modify actions are plan/workspace dependent; therefore LXG-01 must provide a useful read-only/search/fetch baseline that can operate where only read/fetch MCP permissions are available, and may expose mutating actions only when the actual ChatGPT surface authorizes them.

## Authorized implementation surfaces

Application repository (`cybalicistjt-stack/Multiversal-app`) on a dedicated LXG branch:

- `tools/local_execution_gateway/**`
- `tests/tools/local_execution_gateway/**`
- `docs/development/LXG-01-*.md`

Machine-local setup after code is merged or checked out:

- `/home/antiquaria/multiversal/resources/gateway/**`
- `/home/antiquaria/multiversal/bootstrap/lxg/**`
- user-local service/autostart configuration required to launch the gateway and approved Secure MCP Tunnel

No LXG mutation belongs on the active ARI implementation branch.

## Phase-1 tool contract — safe read/compute surface

The first gateway must be `tool-only` and useful without a widget. It shall expose:

1. `search` — standard ChatGPT/MCP read-only search contract over allowlisted local project/document roots.
2. `fetch` — standard ChatGPT/MCP read-only fetch contract for an ID returned by `search`.
3. `gateway_status` — installed-tool/service availability, versions where cheap to obtain, configured roots and policy mode; never secrets.
4. `inspect_file` — path-safe stat/hash/type/metadata inspection for a file beneath an allowlisted root.
5. `inspect_media` — path-safe ExifTool/ffprobe/ImageMagick-backed metadata inspection where available.
6. `local_model_query` — bounded prompt execution against loopback Ollama, with no file access unless explicit text is supplied to the call.

Phase 1 must expose **no arbitrary shell**, arbitrary executable path, unrestricted filesystem path, raw SQL, arbitrary URL fetch, repository write, delete, move, install, package-manager mutation, credential access, or operating-system control.

## Phase-2 action contract — only after supported ChatGPT permission surface is verified

Later approved tools may include deterministic recipe execution, transcription, media derivatives, test profiles, graph rendering, local retrieval indexing, asset conversion and other idempotent/bounded actions. They must be allowlisted operations with typed inputs and receipts, not a disguised general shell.

No Phase-2 action is enabled merely because the gateway code supports it. Its ChatGPT app action must be explicitly enabled under the then-current workspace/app permissions.

## Security invariants

- Gateway binds to `127.0.0.1`/loopback only by default.
- Remote ChatGPT access uses Secure MCP Tunnel or an explicitly approved authenticated HTTPS endpoint; never expose a raw unauthenticated local port publicly.
- Filesystem access is deny-by-default and resolved through named allowlisted roots.
- Symlink/path traversal outside allowed roots fails closed.
- Command execution uses fixed argv templates and resolved executable allowlists; user text is never interpolated into a shell string.
- Returned data is size-bounded and privacy-minimized.
- Environment variables, tokens, browser cookies, SSH material, Git credentials and secret-bearing config are excluded by policy.
- `.git`, dependency caches, binary archives, model weights and known secret/config patterns are excluded from generic text search/fetch unless a future explicit operation narrowly permits them.
- Gateway produces structured audit receipts locally for action-class operations; read-only requests may be summarized without retaining sensitive content.
- Local model calls may receive only the explicit tool input unless a separate authorized retrieval tool supplies content.

## Implementation strategy

Use the official stable MCP SDK rather than writing the protocol from scratch. Prefer a small isolated Python implementation because MLR-01 already validated Python/uv and the MCP Python SDK supports Streamable HTTP. Keep its dependency environment outside the application runtime dependency graph.

The server must run on a dedicated loopback port and expose `/mcp` using Streamable HTTP. It must provide a deterministic policy/config file and a self-test that can validate tool registration without requiring ChatGPT.

## ChatGPT setup target

After local validation:

1. launch gateway on loopback;
2. establish Secure MCP Tunnel to the gateway's `/mcp` endpoint (or another OpenAI-supported private-machine bridge available to the user's plan/workspace);
3. in ChatGPT developer-mode app settings, create a private custom app pointing at the tunneled MCP endpoint;
4. scan/refresh tools;
5. enable only the read-only Phase-1 tools initially;
6. test from a regular ChatGPT conversation using `gateway_status`, then `search` → `fetch`, then bounded file/media inspection and local-model query;
7. record connection mode, permissions and successful tool calls without recording secrets.

## Plan compatibility

The gateway must degrade cleanly:

- where only read/fetch custom MCP capability is available, `search`, `fetch` and other permitted read-only tools remain useful;
- where full MCP actions are available, later approved Phase-2 tools can be enabled individually;
- if ChatGPT custom MCP is unavailable on the user's current plan/workspace, the same server remains usable by Codex, Goose and other MCP clients while ChatGPT connection waits for an eligible surface. This is a product-availability condition, not a reason to discard the gateway.

## Completion evidence

LXG-01 setup is complete only when:

- gateway source, tests and documentation are merged without altering the active product work pointer;
- the local gateway installs in an isolated environment and passes self-tests;
- localhost `/mcp` is reachable only on loopback;
- ChatGPT connection succeeds through a supported secure bridge when the user's plan/workspace permits it;
- at least `gateway_status`, `search` and `fetch` execute successfully from an ordinary ChatGPT conversation;
- no arbitrary-shell or unrestricted-filesystem surface exists;
- a setup/validation receipt records the actual ChatGPT capability tier and any unsupported Phase-2 actions.

If the ChatGPT account/workspace does not presently permit custom MCP connection, record `chatgpt_connection_blocked_by_product_tier` while retaining the fully validated local gateway; do not misclassify the local gateway implementation as failed.
