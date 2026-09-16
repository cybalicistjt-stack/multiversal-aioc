# Multiversal canonical content sources

The certified 3.0 content pipeline is authoritative:

1. `scripts/materialize-content-source.mjs` materializes the preserved compressed Phase 1–8 baseline as `phase-1-8-canonical-objects.json`.
2. `scripts/lib/canonical-content-source.mjs` loads that 487-record baseline plus every supplemental JSON bundle in this directory whose format is `multiversal-canonical-content-source` and whose status is `owner-approved-canonical-incorporation`.
3. `scripts/build-canonical-content-database.mjs` generates `content-db/` from the composite canonical source set.
4. `scripts/certify-canonical-content-pipeline.mjs` certifies the exact composite source digest, per-source provenance, unique stable IDs, generated semantic fingerprint, and database counts.

`build-content-database.mjs` is retained only as a compatibility entrypoint and delegates to the certified 3.0 pipeline; it is not a second content algorithm.

The preserved baseline must remain exactly 487 records. Supplemental canonical records may grow independently, but duplicate stable IDs across baseline and supplemental bundles are rejected.

Current supplemental canonical content includes the Beacon Debt Havalaea/Vertigon bundle and the exact-version materialization of the existing Administrative Syndicate stable identity.
