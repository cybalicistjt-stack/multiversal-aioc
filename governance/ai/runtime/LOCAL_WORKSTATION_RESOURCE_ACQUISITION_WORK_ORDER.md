# MLR-01 — Local Workstation Resource Acquisition & Bootstrap

**Work order ID:** MLR-01  
**Status:** OWNER-AUTHORIZED PARALLEL MACHINE-LOCAL WORK ORDER  
**Lifecycle intent:** CURRENT_COMPATIBLE  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-09-09  
**Product implementation authority:** none  
**Repository mutation authority:** none, except read-only governance/repository inspection needed to avoid conflicts

## Purpose

Prepare the owner's Windows/WSL development laptop with the approved free/open-source workstation, local-AI, media, data, QA, mapping and asset-production resources. This work is machine-local infrastructure. It does not select, replace, pause or modify the current Multiversal application tranche.

The canonical `CURRENT_WORK_POINTER.json` continues to govern product/application implementation. MLR-01 may execute in parallel because its authorized mutations are outside the application and AIOC repository worktrees.

## Stale-checkout rule

Before acting, refresh the canonical AIOC `main` bootstrap/authority evidence. Historical WP-011 text, old cloned governance snapshots, archived dispatches and local bootstrap copies do not override current AIOC `main`. If a local clone says WP-011 or another historical item is the only active authority while canonical AIOC `main` says otherwise, treat the local clone as stale and refresh it before applying governance decisions.

## Authorized machine-local roots

MLR-01 authorizes creation and use of:

- `/home/antiquaria/multiversal/resources/` and its subdirectories;
- `/home/antiquaria/multiversal/bootstrap/` for machine-local bootstrap scripts, receipts and manifests;
- existing `/home/antiquaria/multiversal/dwc-tts/` only where reuse of its Piper/wheelhouse resources avoids redundant downloads;
- normal Windows user download/cache/temp directories;
- normal vendor-recommended Windows installation locations and per-user application/configuration locations;
- isolated WSL/Python virtual environments beneath the machine-local resource/bootstrap roots.

Do **not** place downloaded third-party binaries, models, archives or generated installation state inside `Multiversal-app` or `multiversal-aioc` worktrees.

## Machine facts already established

- Windows host with WSL/Ubuntu.
- x86-64/AMD64 architecture.
- NVIDIA GeForce RTX 4060 Laptop GPU with approximately 8 GB VRAM.
- Existing WSL Piper/DWC TTS environment may be reused when healthy.

Re-inventory RAM, free disk, driver/CUDA state and existing package versions before heavyweight local-model or ComfyUI downloads.

## Source and verification policy

1. Prefer the canonical upstream/vendor release page or official package repository.
2. SourceForge or another mirror may be used only when it is an exact/authorized mirror and upstream identity/version can be verified.
3. Never install an architecture-mismatched artifact.
4. Calculate SHA-256 for every retained installer/archive/model package.
5. Verify publisher/code signatures when the upstream format provides them.
6. Record exact version, source, license, architecture, hash, signature result, install path and smoke-test result.
7. Unsigned software is not automatically rejected, but an unsigned binary must have stronger upstream provenance/checksum evidence before execution.
8. Quarantine ambiguous, corrupted, wrong-architecture or unverifiable downloads instead of silently executing them.
9. Use permissive/open licenses as normal tooling where appropriate; any code/library/asset proposed for embedding in Multiversal still requires its own ARI/license/provenance decision.

## Authorized actions

MLR-01 may:

- inventory installed/downloaded software;
- verify and reuse good existing downloads;
- obtain current correct x86-64 builds from official upstream sources;
- install, update or configure approved workstation software;
- configure user/system PATH where required;
- create isolated Python environments and local service data directories;
- install local-only services and bind them to loopback by default;
- configure Ollama/local inference, Qdrant/local retrieval, Docling/MarkItDown processing and local transcription tooling;
- run deterministic smoke tests and local benchmarks;
- replace/quarantine incompatible downloaded archives such as ARM64 or i686 builds on this AMD64 machine;
- create machine-local install scripts, manifests and receipts under the authorized bootstrap/resource roots;
- reuse already-installed healthy components instead of reinstalling them;
- skip a package when a superior already-installed equivalent fully satisfies the same function and record the reason.

## Not authorized

MLR-01 does not authorize:

- application/AIOC feature implementation, commits, merges or branch cleanup;
- changing the active application work pointer/checkpoint/family;
- purchasing subscriptions, activating paid providers or entering payment credentials;
- uploading private project/user content to external services;
- scraping/ripping protected services or bypassing access controls;
- installing firmware/BIOS changes or unrelated kernel/system drivers;
- disabling security controls to make an install succeed;
- opening public network listeners when loopback/local operation suffices;
- deleting unrelated user files or pre-existing untracked repository data;
- bulk mirroring third-party asset libraries without a specific rights/storage decision.

## Acquisition tiers

### Tier A — core deterministic workstation; install/configure now

7-Zip; WinMerge; Microsoft PowerToys; DocFetcher; ExifTool; OpenRefine; DBeaver Community; ripgrep; fd; jq; fzf; hyperfine; uv; Ruff; DuckDB; FFmpeg; ImageMagick; Tesseract; ast-grep; act; Trivy; Gitleaks; Kopia.

### Tier B — local AI, retrieval and speech; install/configure now with hardware gates

Ollama; Codex CLI/local-provider support when applicable; llama.cpp; Goose; Docling; MarkItDown; Qdrant; FastEmbed; ONNX Runtime; whisper.cpp; Buzz.

Model downloads are conditional on current RAM/disk/VRAM inventory. Prefer a quantization/runtime combination that can operate credibly on the laptop rather than downloading an oversized model merely because it is available. ComfyUI is authorized after GPU/Python compatibility verification. Existing Piper 1.8.0 resources should be reused/evaluated before redundant installation.

### Tier C — production/specialist applications; install/configure unless an existing verified installation is already suitable

Audacity; Inkscape; Krita; Blender; OBS Studio; QGIS LTR; Gephi; Graphviz; FreeCAD.

### Tier D — reusable engineering libraries; registry/evaluation only

MapLibre GL JS; PMTiles; Turf.js; React Flow/XYFlow; Cytoscape.js; Yjs; PixiJS; Three.js; React Aria; TanStack Query; TanStack Virtual; Zod; quicktype; json-schema-faker; Storybook; Playwright; OpenTelemetry; OSS Review Toolkit.

MLR-01 may download documentation/source for isolated evaluation when useful, but **must not add these as Multiversal application dependencies**. Dependency adoption belongs to the future owning product tranche.

### Tier E — asset/data/reference sources; catalog first

Kenney; Poly Haven; Natural Earth; Google Fonts; Azgaar Fantasy Map Generator; MapTool; OpenMW; GemRB; WeiDU; Candlekeep Revisited and other approved reference implementations.

Do not bulk-download whole catalogs by default. Record canonical links/licenses and acquire only bounded useful sample/reference material unless a later asset-intake task authorizes more.

## Existing-download disposition from the 2026-09-09 inventory

- 7-Zip: 26.02 already installed; downloaded 26.03 package requires upstream verification before upgrade.
- DBeaver CE: downloaded candidate had a valid DBeaver signature; verify version/hash against upstream before install.
- DocFetcher: downloaded candidate had a valid publisher signature; verify version/hash before install.
- ExifTool: downloaded archive was structurally readable and contained license material; verify upstream/version/hash.
- fd: downloaded ARM64 archive is incompatible; quarantine and obtain AMD64/x86-64 build.
- hyperfine: downloaded i686 build is not preferred; quarantine and obtain x86-64 build.
- OpenRefine: downloaded bundled-Java archive was structurally readable; compare with current stable upstream before install.
- PowerToys: downloaded candidate had a valid Microsoft signature; verify current stable/version/hash.
- ripgrep: downloaded ARM64 archive is incompatible; quarantine and obtain AMD64/x86-64 build. Codex's bundled ripgrep does not replace the workstation-wide CLI requirement unless it is deliberately exposed and stable outside Codex.
- WinMerge: downloaded candidate had a valid publisher signature; verify version/hash before install.
- The identified ~1.95 GB ChatGPT export ZIP is project/user data, not tooling; leave it untouched by MLR-01.

## Execution strategy

1. Refresh canonical AIOC authority and recognize MLR-01 as parallel machine-local authority.
2. Inventory CPU/RAM/GPU/disk/Windows/WSL/package state and current downloads.
3. Create `/home/antiquaria/multiversal/resources/` with `downloads/`, `packages/`, `models/`, `docs/`, `quarantine/`, `receipts/` and `manifests/` subdirectories.
4. Resolve existing-download dispositions before downloading duplicates.
5. Install Tier A in dependency-safe batches and smoke-test each batch.
6. Install Tier B foundations; benchmark local inference/retrieval/transcription before downloading multiple large models.
7. Install Tier C applications.
8. Create Tier D/E registry entries without changing Multiversal product dependencies.
9. Produce a final machine-local manifest and failure/recovery report. Do not call the setup complete while any required Tier A/B/C item is silently failed or architecture-mismatched; classify explicit skips/blocks instead.

## Credit-efficiency rule

Prefer deterministic local tooling for search, conversion, linting, formatting, metadata, SQL/data processing, image/audio conversion, testing and security scans. Prefer local inference for suitable bounded tasks after quality benchmarks pass. Reserve frontier Codex/Work reasoning for tasks where higher model capability materially changes correctness or value.

## Completion evidence

MLR-01 machine setup is complete when the manifest shows, for every Tier A/B/C entry, one of `installed_verified`, `already_installed_verified`, `conditional_deferred` with an explicit hardware/license reason, or `blocked` with exact recovery instructions; wrong-architecture downloads are quarantined; local smoke tests pass for installed tools; and no product repository or active work authority was mutated by the setup.