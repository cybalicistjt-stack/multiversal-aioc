# STAGE-A-A2 App-Ready Runtime Corpus Handoff v2.4.0

**Status:** COMPLETE PRE-IMPLEMENTATION INPUT / DOES NOT ACTIVATE A2

## Purpose

Preassemble the governed A2 current-release content into one deterministic local runtime/adapter input so Sunday Codex does not spend A2-01 reconstructing frozen object identity, search projection, profile routing, relationship adjacency, and provenance coordinates from historical CSV packages.

## Artifact

`STAGE_A_A2_APP_READY_RUNTIME_CORPUS_v2.4.0.zip`

SHA-256: `0ad803159e317a167628321252e3b1a07bc1546d261f92e38d69d0b6a01c2e10`

Validator: `tools/validate_a2_runtime_corpus_v2.4.0.py`

Validator result: `PASS`

## Frozen metrics

- governed runtime objects: **11,881**
- search projection documents: **11,881**
- current objects using `P-A2-GENERIC`: **0**
- current-stable-ID navigable relationships: **1,587**
- relationship source/evidence coordinates that are intentionally non-navigable: **81**
- explicitly unresolved relationships: **86**
- objects with outbound navigable relationships: **1,005**
- objects with inbound navigable relationships: **498**
- objects with direct frozen provenance summary: **9,065**
- source-field projection routes: **1,897**
- presentation routing rows: **53**

## Runtime files

Production/data inputs include:

- `runtime/objects.jsonl`
- `runtime/search-documents.jsonl`
- `runtime/provenance-summary.jsonl`
- `runtime/relationships.jsonl`
- `runtime/relationship-source-coordinates.jsonl`
- `runtime/unresolved-relationships.jsonl`
- `runtime/indexes/object-id-index.json`
- `runtime/indexes/relationship-adjacency.jsonl`
- `runtime/indexes/profile-counts.json`
- `runtime/indexes/domain-counts.json`
- `runtime/reference/presentation-profile-routing.csv`
- `runtime/reference/source-field-projection-map.csv`
- `runtime/source-only-diagnostics.json`

Acceptance-only security data is physically separated under:

- `test_only/authorization-overlays.json`

## Security and identity locks

1. The runtime corpus is data/adapter input, **not authorization or entitlement authority**.
2. `test_only/authorization-overlays.json` must never be imported into production authorization logic or shipped as a permissions database.
3. `runtime/relationships.jsonl` contains only relationships whose source and target resolve to current governed stable IDs.
4. Source-coordinate and unresolved relationship files are evidence only and cannot become navigable identity without later governed resolution.
5. Search documents are projection data; ranking remains governed by the v1.2.3 search/ranking contract.
6. Presentation profile comes from explicit mapping metadata, never stable-ID-prefix parsing.
7. Provenance absence remains absence; missing source detail must not be invented.
8. Scene placement, Evidence reveal state, authorization state and other campaign/live state remain caller-local/projection state and are not baked into immutable Definitions.
9. `P-A2-GENERIC` remains required as a future/unknown-kind fallback even though no current governed object uses it.

## Sunday master refresh

The app-ready corpus is included in:

`STAGE_A_A2_SUNDAY_CODEX_MASTER_EXECUTION_v2.4.0.zip`

SHA-256: `e7ef33ee162ff14e5858fbd03a53e265fed0cc9f58429b7ef0b49893bd1aa74f`

Master validator result:

`STAGE-A-A2 SUNDAY MASTER v2.4.0: PASS`

Frozen master counts:

- nested controlling packages: **11**
- governed release objects: **11,881**
- runtime objects: **11,881**
- runtime navigable relationships: **1,587**
- execution phases: **16**
- blocking evidence ledger entries: **16**

v2.4.0 supersedes v2.3.0 and all earlier Sunday master archives.

## Repository authority at consolidation

Application repository recent-commit verification on 2026-08-10 still placed `main` at:

`dced7f92163050690c807c1fda937146bb8dce85`

Commit message: `Prepare governed Stage A A2 work order (#104)`.

A2 remains prepared but not activated. Codex must re-read current repository authority before mutation and must not reset a legitimate newer main merely to match this snapshot.

## Boundaries

This handoff does **not**:

- activate A2 implementation;
- change `CURRENT_WORK_POINTER`;
- alter the parallel Design Standards primary attempt;
- authorize release, deployment, paid services, public exposure, credentials, or production infrastructure;
- promote the remaining source-only content rows;
- claim recovery of the exact 8D-002 exhaustive 245-kind catalog.

## Next pre-Sunday tranche

Build the hostile/failure-condition acceptance corpus against this frozen 11,881-object runtime input, then perform a clean-room Sunday-master rehearsal after all remaining pre-Sunday tooling is complete.
