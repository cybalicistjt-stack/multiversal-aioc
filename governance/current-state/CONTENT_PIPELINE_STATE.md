# Content Generation Pipeline State

**Status:** REPAIRED — CERTIFICATION PENDING  
**Repository:** `cybalicistjt-stack/multiversal-aioc`  
**Workflow:** `.github/workflows/build-content-database.yml`

## Governed pipeline

The content-generation path now executes in four isolated stages:

1. Materialize the 487-record canonical Phase 1–8 source bundle.
2. Recover the Phase 1–7 inventory by strict Base64 decoding, raw binary concatenation, gzip verification, and JSON parsing.
3. Assemble the generated content database in the GitHub Actions runner workspace.
4. Independently certify seed integrity, canonical-source integrity, record counts, manifest consistency, identifier uniqueness, full-object coverage, and semantic output fingerprint.

## Durable evidence

A successful run produces:

- `content-db/`
- `evidence/content-pipeline/latest-certificate.json`
- GitHub artifact `certified-content-database-<COMMIT_SHA>` retained for 30 days.

The repository is not mutated by the certification workflow. Generated outputs are evidence artifacts until a separate governed promotion operation is approved.

## Failure behavior

Any decoding, archive, source, assembly, uniqueness, coverage, or manifest failure stops certification. The failure is then recorded on branch `ci/failure-records` under `governance/ci-failures/`.

Before every follow-on operation, inspect `governance/ci-failures/INDEX.md` on `ci/failure-records`.

## Promotion rule

The quarantined legacy write-back workflow remains retired. Automatic commits of generated content are prohibited until the rebuilt pipeline has a clean certification result and a separate promotion workflow with rollback and provenance controls is implemented.

## Next executable action

Read the CI failure index. If the new `Certify Content Database Pipeline` run passes, close the repair portion of Step 3 and implement governed artifact promotion. If it fails, correct the newest recorded failure before advancing.
