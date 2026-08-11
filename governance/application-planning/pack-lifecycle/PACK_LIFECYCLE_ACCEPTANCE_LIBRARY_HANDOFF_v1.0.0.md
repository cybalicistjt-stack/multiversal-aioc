# Multiversal Pack Lifecycle Acceptance Library — Handoff v1.0.0

Status: **PREPARED COMPLETE — NOT APP-INTEGRATED**

Owner/final authority: John Brandon Turner

## Artifact

`MULTIVERSAL_PACK_LIFECYCLE_ACCEPTANCE_LIBRARY_v1.0.0.zip`

SHA-256:

`1d962ceee0bad98ce3cb2ca1373cd86ef0d83abbf72e9819e3b863ae6137bfd7`

Validator result:

`MULTIVERSAL PACK LIFECYCLE ACCEPTANCE LIBRARY v1.0.0: PASS`

Reference oracle result:

`PACK LIFECYCLE REFERENCE ORACLE: PASS`

Validated counts:
- real fixture pack archives: 33
- deterministic lifecycle scenarios: 50
- lifecycle/security threat cases: 25
- blocking acceptance gates: 24
- actual bounded large-pack object count: 12,000

## Purpose

Provide one governed, executable acceptance source for safe pack installation, enable/disable, update, uninstall, exact-version pinning, migration, rollback, Campaign-local content, source-only content, import/export, corruption handling, orphan prevention, unavailable dependencies and large-pack boundedness.

The library is intended for:
- A2 Universal Object Experience;
- A5 Campaign/Scene source-version pinning;
- A10 World/content authoring and D06 pack lifecycle;
- A12 hardening/Internal Alpha regression.

## Canonical ownership boundary

The existing bounded-domain architecture remains controlling:
- D06 `pack-registry` owns pack manifest/version/install/enable/disable/pinning lifecycle;
- D07 `entity-catalog` owns reusable definition identity/version/variant/dependency semantics;
- D29 `authoring-provenance` owns drafts/proposals/reviews/publication provenance and creator/local authoring workflow;
- D05 owns audience-safe projections;
- D30 owns migration/compatibility policy;
- D12 owns export/recovery concerns.

No domain may write another domain's canonical persistence directly. Stable references, expected versions, transactions, lifecycle Events/tombstones, sagas/compensation and public contracts remain required.

## Current repository compatibility

The immutable P9 baseline already contains:
- `content_packs` with stable ID, version, visibility and manifest;
- `canonical_objects` with pack ID, stable ID, object type, version, visibility, payload and provenance.

`database/migrations/0001_initial_logical_schema.json` must not be rewritten for this library. Future lifecycle persistence is additive.

`packages/contracts/src/pack-registry/README.md` is still a WP-006 placeholder. Therefore the fixture archives deliberately use `fixture-pack-envelope/1.0`, marked **ACCEPTANCE ONLY — NOT PRODUCTION MANIFEST SCHEMA**. A future D06 implementation should adapt these fixtures rather than treating the envelope as the final public API.

## Acceptance coverage

The real ZIP corpus includes:
- valid base/update/dependent packs;
- Campaign-local and source-only packs;
- disabled-by-default packs;
- missing/unavailable dependencies;
- dependency cycles;
- duplicate stable IDs;
- missing parents;
- cross-pack stable-ID collisions;
- active reference/orphan cases;
- good and forced-failure migrations;
- malformed JSON manifests;
- truncated archives;
- checksum mismatch;
- ZIP path traversal and duplicate-entry archives;
- forbidden script/network processors;
- unsupported manifest version;
- invalid semantic version;
- clean export/import pack;
- one actual 12,000-object pack plus a safe larger-pack generator.

The 50 scenario suite covers transactionality, idempotent reinstall, dependency/version closure, disable/enable ordering, uninstall safety, exact Campaign pins, no auto-follow on update, migration/rollback, source-only runtime exclusion, Campaign-local visibility, canonical-promotion separation, corrupted import rejection, large-pack interrupted-install rollback and bounded-resource outcomes.

## Nonnegotiable lifecycle rules

- validate archive/integrity/dependencies before mutation;
- install/update/import are all-or-none;
- same stable ID + same version with changed bytes conflicts;
- normal uninstall/update cannot silently orphan active references;
- disabled packs leave historical identity/provenance resolvable while becoming unavailable for active runtime use;
- Campaign pins remain on exact versions until explicit reviewed migration;
- migration failure rolls back to exact prior state;
- Campaign-local install/import never implies global/canonical promotion;
- source-only objects remain authoring/export provenance but are excluded from runtime-active indexes;
- arbitrary scripts/network processors are rejected;
- import/export is checksum-complete and dependency-complete;
- large-pack success or resource-limit failure must be bounded and all-or-none.

## Reference oracle

`oracle/reference_pack_lifecycle_oracle.py` is fixture/acceptance code only, not a D06 implementation. It produces the exact expected semantic receipts for all 50 scenarios so future Codex work can compare a real D06 adapter against the fixed acceptance corpus with minimal reinterpretation.

## Current authority

This package does not:
- activate A10 or D06 implementation;
- change the Stage A work pointer;
- authorize canonical promotion;
- authorize real-user content intake;
- authorize a public marketplace;
- authorize release/deployment/paid services/production credentials.

A2 remains the current authorized Stage A implementation pointer.

## Future execution

When D06/A2/A10 pack lifecycle implementation is reached:
1. adapt the fixture envelope through a test loader;
2. run the reference oracle;
3. run the same 50 scenarios against the real implementation;
4. compare semantic lifecycle receipts;
5. execute the 25 threat cases and 24 blocking gates;
6. attach exact build/commit/checksum/rollback/projection evidence;
7. use the library again as an A12 candidate-hardening lane.
