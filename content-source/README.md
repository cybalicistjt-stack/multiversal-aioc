# Multiversal canonical content sources

The certified 3.0 content pipeline is authoritative:

1. `scripts/materialize-content-source.mjs` materializes the preserved compressed Phase 1–8 baseline as `phase-1-8-canonical-objects.json`.
2. `scripts/lib/canonical-content-source.mjs` loads that fixed 487-record baseline plus governed supplemental JSON bundles in this directory.
3. `scripts/build-canonical-content-database.mjs` generates `content-db/` from the effective composite canonical source set.
4. `scripts/certify-canonical-content-pipeline.mjs` certifies exact source digests, replacement lineage, unique effective stable IDs, generated semantic fingerprint, and database counts.

`build-content-database.mjs` is retained only as a compatibility entrypoint and delegates to the certified 3.0 pipeline; it is not a second content algorithm.

## Supplemental contracts

### New identities

A bundle with:

- `format: multiversal-canonical-content-source`
- `status: owner-approved-canonical-incorporation`

may append new canonical stable identities. If one of those IDs already exists anywhere in the effective source set, the build fails. Ordinary incorporation can never silently overwrite an existing object.

### Existing-identity version replacement

A bundle with:

- `format: multiversal-canonical-content-source`
- `status: owner-approved-canonical-replacement`

may replace an existing stable identity only when every replacement record:

- keeps exactly the same stable ID;
- declares `replacementOf.stableId` equal to that ID;
- declares the exact `replacementOf.expectedContentVersion` (`null` is permitted only for a currently unversioned predecessor);
- supplies an exact semantic `contentVersion`;
- advances the version when the predecessor already has an exact version.

The loader resolves replacement chains by explicit predecessor version rather than filename order and rejects missing predecessors, version mismatches, forks, and accidental duplicates. Replacement source/provenance and predecessor lineage remain visible in the generated database and certificate.

This path exists so governed completion work — including Object Game Readiness / Item completion — can version-materialize or improve an already-canonical stable identity without either duplicating it or mutating the preserved 487-record baseline.

## Readiness boundary

The preserved baseline remains exactly 487 records, but the effective certified canonical database may grow through appends and may improve existing objects through governed replacements.

**Canonical source/database certification is not Object Game Readiness certification.** It proves source-set integrity, identity/version/provenance resolution, and deterministic generation. `GAME_READY`, mechanics completeness, runtime behavior completeness, validation, and playtest status remain owned by the Object Game Readiness Program (OGR) and its domain-specific evidence.

The current 516-record certified database is therefore a canonical-source snapshot, not the total Multiversal game-object corpus and not a claim that 516 objects are game-ready.
