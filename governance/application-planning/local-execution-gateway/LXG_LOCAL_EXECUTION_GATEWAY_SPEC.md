# LXG — Local Execution Gateway Specification

**Program/work order:** LXG-01  
**Status:** owner-authorized parallel developer infrastructure  
**Purpose:** make MLR-01's installed workstation capabilities callable through one governed local MCP interface without making Codex the only operator.

## Architecture

```text
Regular ChatGPT / Codex / Goose / MCP client
                  |
       approved MCP connection
                  |
      Secure MCP Tunnel / HTTPS bridge
                  |
          127.0.0.1:<port>/mcp
                  |
        Local Execution Gateway
       /          |           \
 policy       resource IDs     adapters
   |              |              |
 allowed roots  bounded text  rg/fd/ExifTool/ffprobe/
                                ImageMagick/Ollama/...
```

The gateway is a control adapter, not a general remote shell.

## Phase 1 — universal read/compute baseline

### Standard `search`

Use the ChatGPT/MCP standard company-knowledge shape:

- input: one `query` string;
- output: exactly one text content item containing JSON with `results`;
- each result: `id`, `title`, `url`;
- read-only annotation;
- IDs are opaque `mvlocal://` resource IDs, never raw host paths.

Search executes deterministic text search over configured roots, preferring `ripgrep` when available and a safe Python fallback when not. Results are bounded by count, bytes and time.

### Standard `fetch`

- input: one `id` returned by `search`;
- output: exactly one text content item containing JSON with `id`, `title`, `text`, `url`, optional `metadata`;
- read-only annotation.

The resource-ID store must validate the ID against the current allowlisted root and re-resolve the path safely on every fetch. Fetch must not accept arbitrary filesystem paths.

### `gateway_status`

Returns:

- gateway version;
- policy mode;
- configured root aliases, not hidden absolute paths unless explicitly safe;
- available adapter/tool names;
- availability/version summaries for deterministic installed tools;
- loopback service health for configured local services;
- ChatGPT action tier if configured by setup receipt;
- no credentials, environment variables or tokens.

### `inspect_file`

Input is `root` alias + relative path. Validate using realpath containment. Return size, modified timestamp, SHA-256 (bounded/optional for very large files), guessed type and safe deterministic metadata. Reject directories, secret patterns and files outside the root.

### `inspect_media`

Input is `root` alias + relative path. Depending on type and available tools, return structured ExifTool, `ffprobe` or ImageMagick `identify` metadata. Commands are fixed argv vectors with timeouts and byte limits.

### `local_model_query`

Input: prompt text, optional configured local model alias, bounded output-token/character budget. Call only the configured loopback Ollama endpoint. No automatic filesystem, browser or repository context. The result is advisory model output and includes model/runtime identity where available.

## Phase 2 — action tools

Candidate action tools, disabled initially:

- `run_recipe`
- `transcribe_audio`
- `synthesize_proxy_voice`
- `create_media_derivative`
- `render_graph`
- `run_test_profile`
- `index_local_documents`
- `run_security_scan`
- `benchmark_command_profile`

Every action must use a named recipe/profile, typed arguments, fixed executable mappings, output-root containment, bounded runtime/resource limits and a receipt. No action may accept raw shell text.

## Filesystem policy

Default named roots are configured locally, not hard-coded into the repository. Expected examples:

- `app` → local `Multiversal-app` checkout
- `aioc` → local `multiversal-aioc` checkout
- `resources` → `/home/antiquaria/multiversal/resources/`
- `bootstrap` → `/home/antiquaria/multiversal/bootstrap/`

Generic search/fetch excludes at minimum:

- `.git/**`
- `node_modules/**`, package caches and virtual environments
- `.env*`, credential/key/cookie/token files
- private key formats and SSH/GPG material
- binary archives and executable installers
- local model weights
- generated caches/large build outputs

Specific future tools may access a normally excluded class only through an explicitly scoped adapter.

## Tool adapter strategy

Adapters are classified:

1. **read metadata** — ExifTool, ffprobe, ImageMagick identify;
2. **search/discovery** — ripgrep, fd;
3. **local compute** — Ollama and later FastEmbed/Qdrant retrieval;
4. **action/derivative** — FFmpeg, ImageMagick conversion, Blender, Graphviz, Piper/Whisper, security scanners; Phase 2 only.

Do not expose the underlying executable invocation directly through MCP.

## Security and failure behavior

- deny unknown root alias;
- deny absolute paths from tool inputs;
- normalize and resolve symlinks before containment check;
- time out every subprocess;
- cap captured stdout/stderr;
- never invoke `shell=True`;
- redact configured sensitive patterns before returning text;
- fail closed when an adapter is missing;
- use deterministic error codes suitable for ChatGPT retry/recovery;
- preserve an audit record for action-class operations.

## ChatGPT compatibility

The first implementation is a `tool-only` custom MCP app. A widget is unnecessary for the bridge's initial purpose.

Use Streamable HTTP on `/mcp`. For local ChatGPT access, use OpenAI Secure MCP Tunnel or another supported private-machine bridge. Do not expose the raw local port publicly.

The gateway must support a read-only baseline because current ChatGPT plan/workspace capabilities can differ. Full write/modify tools are enabled only when supported and explicitly authorized.

## Cost doctrine

The gateway exists to make this execution order practical:

`deterministic local tool → approved reusable library → local model/agent → local specialist engine → hosted provider → frontier reasoning → owner-only judgment`

A successful repeated operation should become a named recipe/profile instead of consuming repeated agent reasoning.

## Product ownership boundary

Gateway output is evidence, derivative media, analysis or an execution receipt. It is never automatically:

- game canon;
- mechanical authority;
- permission/rights approval;
- a canonical Campaign/Character/World mutation;
- a production-provider selection;
- a release authorization.

Those remain with their existing Multiversal owners.
