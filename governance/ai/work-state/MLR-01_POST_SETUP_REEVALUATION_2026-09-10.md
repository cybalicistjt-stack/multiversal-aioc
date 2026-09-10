# Initial post-setup reevaluation — read-only

Authority checked: canonical AIOC main `51bcc4e25cb65b95ab293176990a6958e0e7d16e`, `CURRENT_WORK_POINTER.json` and `ARI_PROGRAM_BACKLOG.json`. This report does not modify product authority, priority, branches or dependencies.

The active product item remains **ARI-04 — Safe ZIP Staging & Extraction** on `implementation/ari-04-safe-zip-staging-extraction`. ARI-01 through ARI-03 are completed. ARI-05 and later require their own governed successor start. A roadmap amendment's historical ARI-02 wording does not override the current pointer.

| Work area | Best use of installed resources | Boundary / higher-capability work |
|---|---|---|
| ARI-04 archive safety | 7-Zip for independent fixture inspection; rg/ast-grep for implementation discovery; jq for receipt assertions; hyperfine for resource-bound regressions; local native act for synthetic workflow tests | Keep traversal, links, decompression limits, atomicity, failure recovery and cross-platform correctness under governed implementation and strong review. A working external tool is not permission to embed it. |
| Future ARI-05 archive adapters | Study 7-Zip behavior using small original fixtures; compare output/error contracts and versions | Separate adapter design and license review; no vendoring or activation under MLR-01. |
| Future ARI-06 discovery/classification | fd/rg enumerate; ExifTool, FFmpeg and ImageMagick inspect actual content; DuckDB measures coverage and duplicates | Prefer deterministic signatures/metadata over asking an LLM to guess file types. Validate hostile inputs. |
| Future ARI-07 sidecars/manifests | jq, DuckDB and OpenRefine normalize synthetic or rights-cleared samples; ast-grep traces schema consumers | Preserve authoritative schema/rights decisions; local model drafts are suggestions only. |
| Future ARI-09 maps/tilesets | QGIS, Inkscape, Krita and Blender produce small original fixtures and inspect coordinate/image metadata | No bulk third-party asset acquisition or copyrighted setting imports. |
| Documentation and evidence retrieval | MarkItDown/Docling convert locally; FastEmbed + Qdrant retrieve candidate passages; retain exact file/revision citations | Local semantic search is not governance authority. Never replace exact-source verification with model memory. PDF model packs remain a separate bounded need, not automatic downloads. |
| Later media and narrative tooling | Whisper/Buzz, existing Piper, Audacity and OBS can assist rights-cleared local media work; Graphviz/Gephi visualize relationships | No DWC retraining under this task; ComfyUI checkpoint selection needs a concrete task and license. Preserve native CNI and the Candlekeep/WeiDU restrictions. |

## Practical credit-saving order

1. Start with deterministic commands and cached local references. Use exact-match search and structural queries before semantic search or AI summarization.
2. Reduce input to the smallest relevant files/receipts, recording versions and hashes. Keep test scripts and environments reusable.
3. Use the tested local 4B model only for bounded drafting, extraction or classification with machine-checkable outputs. Its thinking mode can add overhead; benchmark each real task before redirecting work. Two successful synthetic tests are not an autonomous-coding qualification.
4. Reserve higher-capability reasoning for ambiguous requirements, security-sensitive archive handling, cross-system architecture, rights decisions and final review. Do not mechanically route all work to the cheapest model.

## Exact next review

Inspect the current ARI-04 implementation checkpoint and focused tests read-only, then produce a task-to-tool checklist for the remaining acceptance criteria. Determine what can already be run deterministically, what needs new fixtures, and which decisions still require strong reasoning. Do not rewrite the roadmap merely because additional software is installed.

Owner choices outside completed workstation installation: real backup destination/encryption/retention; which original image-production workflow merits a first checkpoint; whether a future Linux-container workflow justifies Docker setup; exact Candlekeep source identity if further pattern study is requested.
