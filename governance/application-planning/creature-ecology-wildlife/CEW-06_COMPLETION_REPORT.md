# CEW-06 — Ecological Role & Encounter-Use Classification Completion Report

**Work item:** CEW-06 — Ecological Role & Encounter-Use Classification  
**Status:** completion candidate pending exact-head validation and merge  
**Contract:** `CEW-ECO-1.0`

## Completed scope

CEW-06 establishes a provenance-preserving ecological-role and reusable encounter-use vocabulary without collapsing identity, habitat, distribution or Campaign placement.

Completed artifacts:

- `CEW-06_ECOLOGICAL_ROLE_ENCOUNTER_USE_v1.0.0.json`
- `CEW-06_ECOLOGICAL_ROLE_SOURCE_EVIDENCE_v1.0.0.json`
- `CEW-06_ECOLOGICAL_ROLE_ENCOUNTER_USE_CONTRACT.md`
- `tests/control_plane/test_cew06_ecological_role_encounter_use.py`

The representative evidence packet covers directly sourced feeding/resource roles, herd/pack/swarm aggregation, guardian behavior, ambush/lure/lookout/terrain-control encounter facets, and multiversal resource consumption. Plant Immobile/Creeping/Spreading gameplay categories are retained as explicit source-category profiles rather than promoted to global creature identities.

## Preserved boundaries

- ecological role does not create identity, type, habitat or geographic range;
- encounter-use facets do not create Scene/Encounter placement state;
- source silence remains unknown;
- named prey/host/symbiont relationships are not inferred from a general role;
- guardian/community-use wording does not establish personhood, ownership, domestication or partnership;
- exotic feeding targets remain source-specific rather than being normalized to Earth biology;
- no numeric encounter-use or ecological score is authorized;
- no bulk corpus role population is authorized in CEW-06;
- no `Multiversal-app` runtime/schema/UI/migration mutation is authorized.

## Validation history

TDD RED was established on exact branch head `80532d4d00ecf5c659d9ba066264c3d170aaf3dd` in repository-health workflow `33806039954`: repository health passed and the new CEW-06 acceptance suite failed because the CEW-06 model/evidence/contract were absent and backlog still ended at CEW-05. A concurrent unrelated MAL-03 closeout advanced `main`; the unchanged CEW-06 acceptance test was transplanted onto that new exact base before GREEN implementation.

Exact GREEN validation and canonical merge evidence are supplied by the repository workflow/PR record, not preclaimed in this candidate document.

## Successor

Upon verified merge, **CEW-07 — Existing Creature Coverage Audit** is the strict successor. CEW-07 measures coverage across the now-established CEW-01..06 contracts before creature/type gap expansion.
