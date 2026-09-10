# MLR-01 workstation setup

Verified 2026-09-10 against canonical AIOC main `51bcc4e25cb65b95ab293176990a6958e0e7d16e`.

All 45 Tier A/B/C resources have installation/runtime smoke evidence: 40 `installed_verified`, 5 `already_installed_verified`. This is workstation readiness, not certification of every application feature or approval to change Multiversal dependencies.

## What changed

Existing 7-Zip, DocFetcher, DBeaver, PowerToys, WinMerge, ExifTool, search/data utilities, ImageMagick, Tesseract and Piper were verified/reused. DocFetcher was not reinstalled again. Existing Windows Downloads and Piper/DWC resources were used as starting points.

The remaining deterministic CLI tools, Kopia, OpenRefine, local AI/document/retrieval/transcription runtimes, and specialist desktop applications were installed. Graphviz and FreeCAD use isolated application payloads extracted from their already-downloaded, checksum-verified installers; no administrator bypass or second download was needed. Buzz's stalled SourceForge request was replaced with its exact official GitHub release and verified hashes.

Key functional results:

- ast-grep syntax search; ripgrep/fd/jq/fzf; Ruff; DuckDB SQL; hyperfine; ImageMagick; Tesseract OCR; Trivy and Gitleaks passed local tests.
- `act` completed a synthetic native Windows workflow without Docker. Linux-container workflows still require a separately configured Docker runtime. Trivy filesystem scanning does not require Docker.
- Kopia created and verified a snapshot of one synthetic HTML file. **Your actual data is not automatically backed up.** A destination, encryption secret, retention policy and restore drill remain owner choices.
- Docling and MarkItDown converted synthetic HTML offline. FastEmbed/ONNX Runtime embedded three synthetic sentences; Qdrant returned the expected nearest neighbor and the test collection was removed.
- Whisper tiny.en transcribed a Windows-generated synthetic sentence correctly in about 1.6 seconds on CPU.
- Ollama's existing Qwen3 4B Q4_K_M model passed strict arithmetic and extraction tests using its supported thinking mode, about 66 tokens/second. Goose returned the expected answer through loopback Ollama. llama.cpp reused the same GGUF and measured about 68 generation tokens/second. These tiny tests do not establish suitability for unsupervised coding or governance decisions.
- ComfyUI passed CUDA computation and a synthetic image workflow. No image-generation checkpoint collection or third-party custom-node bundle was downloaded. Paid API nodes are disabled.
- Graphviz rendered SVG; FreeCAD calculated a synthetic box volume; all Tier C desktop applications passed bounded startup checks.

## Locations and opening tools

Canonical resource directory: `/home/antiquaria/multiversal/resources/`.

Windows access: `\\wsl.localhost\Ubuntu\home\antiquaria\multiversal\resources\`.

Native Windows programs/environments and reusable caches: `C:\Users\Antiquaria\MultiversalResources\`. The canonical WSL hierarchy links to these native stores rather than duplicating large binaries/models.

The Start menu now has **Multiversal Local Tools**: a prepared tools terminal, FreeCAD, and loopback-only ComfyUI/Qdrant/OpenRefine launchers. Normal installer-created Start menu entries remain available for the other applications.

In the prepared tools terminal, `ast-grep --version`, `act --version`, `trivy --version`, `dot -V`, and `whisper-cli --help` should work. The document-AI environment is exposed there, and Goose's provider/model are explicitly local for that shell. The ordinary Codex configuration and account were not changed.

OpenRefine's isolated launcher uses port 3335 and a separate workspace. Its 3.10.1 distribution reports `3.10-SNAPSHOT` at runtime; both facts are preserved in the manifest. Java 21 hit a Windows Unix-domain socket initialization failure, so the launcher reuses the already-downloaded Java 11 bundle. Keep `Downloads\openrefine-win-with-java-3.10.0\openrefine-3.10.0\server\target\jre` while that launcher references it. The existing user OpenRefine session on port 3333 was left untouched.

## Manifests and repeatability

Under the canonical resource directory:

- `manifests/MLR-01-machine-resource-manifest.json`: every planned Tier A/B/C resource, exact version/path, license, configuration, hashes and linked smoke evidence.
- `manifests/MLR-01-retained-artifacts.json`: retained installers, archives and model files with source, SHA-256, architecture, signature status and disposition.
- `manifests/MLR-01-tier-d-e-registry.json`: 18 Tier D and 10 Tier E entries, no application dependency additions or bulk asset downloads.
- `manifests/document-ai-lock.txt` and `comfyui-lock.txt`: exact installed Python versions; CUDA source/index also recorded by setup scripts.
- `receipts/MLR-01-20260910/`: copied installation, provenance and smoke-test receipts.
- `docs/MLR-01-REEVALUATION.md`: initial read-only mapping of remaining governed work to these tools.

Repeatable scripts are also copied to `/home/antiquaria/multiversal/bootstrap/MLR-01-20260910/`. Preserve the receipts: some older failed/replaced attempts are intentionally retained as history, not represented as final failures.

## Quarantine and limitations

Wrong-architecture fd/ripgrep/act ARM64 and hyperfine i686 archives were quarantined; AMD64 tools are installed. The extracted ARM64 act folder is also recoverable in quarantine. Two abandoned partial Ollama installers and the unused ExifTool ZIP are quarantined. The ExifTool ZIP had 507 files matching the installed distribution, but a different launcher/docs prevented claiming full archive verification; the installed tool remains verified and operational. Nothing was permanently deleted.

Tesseract's installer SHA-256 matches the canonical release and package manifest, but Windows reports a signing-certificate validity-period error. That signature warning is preserved, not suppressed. ExifTool's package-wrapper CC0 label does not relicense its Perl/GPL/Artistic payload; the composite licensing evidence is recorded.

Tier D remains registry/evaluation only. Tier E remains catalog/reference only. Candlekeep Revisited is pattern study only: no Baldur's Gate/Forgotten Realms dialogue, assets, scripts or setting content was copied. Its exact source URL is not recorded in the inspected authority, so the catalog does not invent one. WeiDU remains a separately licensed reference; Multiversal-native CNI is unchanged.

No paid provider was activated, private content uploaded, firmware/security settings changed, or application feature implemented. The identified ChatGPT export and unrelated worktrees, branches and untracked files were left alone.

## Next safe step

Use the read-only reevaluation to assign deterministic searches/conversions/tests to these tools, bounded drafts/classification to the local model with validation, and safety/architecture/governance reasoning to higher-capability review. ARI-04 remains the active product work; setup does not advance the pointer or authorize later tranches.
