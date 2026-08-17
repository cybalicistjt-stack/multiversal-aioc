# Bootstrap Current-State Amendment — CCTI Read-Only Integration

**Effective:** 2026-08-17  
**Owner and final authority:** John Brandon Turner  
**Status:** OWNER-SELECTED PARALLEL MISSION / READ-ONLY TRANCHE ACTIVE

This amendment supplements, but does not replace, `MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`.

## Recovery instruction

When this CCTI branch/attempt is the newest internally consistent owner-selected work evidence, recover:

- program: `governance/application-planning/content-catalog-taxonomy-integration/CONTENT_CATALOG_TAXONOMY_INTEGRATION_PROGRAM.md`;
- roadmap supplement: `governance/application-planning/content-catalog-taxonomy-integration/CONTENT_CATALOG_TAXONOMY_INTEGRATION_ROADMAP_SUPPLEMENT.md`;
- baseline: `governance/application-planning/content-catalog-taxonomy-integration/CCTI_READ_ONLY_BASELINE_20260817.md`;
- checkpoint: `governance/ai/work-state/CCTI-READONLY-01-attempt-001.json`;
- branch: `governance/content-catalog-taxonomy-integration`.

Resume from the checkpoint's exact `active_substep` and `next_action`. Do not treat the read-only tranche as complete merely because audit artifacts exist.

## Current owner direction

The owner selected integration of the linked Content V2 corpus with the later Item/Platform taxonomy systems, including:

- 5,389 Item records;
- 1,200 Vehicle catalog rows;
- 2,117 Mecha catalog rows;
- 2,311 Spacecraft catalog rows;
- all linked identity/provenance/normalization/relationship/supersession/review evidence required to interpret those rows correctly.

CCTI-01 through CCTI-08 are authorized read-only discovery/reconciliation. CCTI-09 through CCTI-12 and persistent taxonomy/catalog adoption remain owner-gated.

## Mandatory integrity rules

- Do not mutate source/master CSVs in the read-only tranche.
- Do not discard existing Content V2 identity/provenance/normalization/relationship evidence.
- Do not force the 2,644 non-model Vehicle/Mecha/Spacecraft catalog rows into platform-model taxonomy.
- Do not reconstruct the checksum-bound Item v0.12.0 or Platform v0.11.0 complete registries from memory or partial extracts.
- Preserve Item Definition vs live Asset Instance and Platform Model vs individual asset boundaries.
- Unknown remains review-required rather than fabricated.

## Parallel state

- GATX-T07-REMOTE and GATX-T08 remain completed_verified.
- Multiversal-app PR #185 remains unfinished and is not superseded or distribution-approved by CCTI.
- DS-008 remains separately blocked.
- No A13, release, deployment, paid-provider, production-credential, APK, or public authority is added.

## Exact next action

Continue CCTI-01 read-only corpus/sidecar reconstruction and deterministic preprojection crosswalk preparation. In parallel, locate the exact Item v0.12.0 and Platform v0.11.0 archive bytes and verify them against their canonical SHA-256 identities before complete-registry row-level projection.
