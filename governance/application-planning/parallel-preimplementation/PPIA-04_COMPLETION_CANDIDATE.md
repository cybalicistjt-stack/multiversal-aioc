# PPIA-04 — Completion Candidate

**Work item:** PPIA-04 — Vehicle, Mecha & Starship Experience  
**State:** COMPLETION CANDIDATE — NOT COMPLETE UNTIL THIS EXACT HEAD PASSES REQUIRED VALIDATION AND MERGES  
**Owner:** John Brandon Turner

## Verified upstream milestones

### Foundation — PR #226

Squash merge: `8afc51555dbb46d68536fb95adcb6b2cc0a9c4e8`

Established:

- 24 retained Vehicle/Mecha/Spacecraft/Operations PDFs / 608 pages;
- three governed Vehicle-domain CSV datasets / 5,628 rows;
- 14-layer Vehicle/Mecha/Starship experience taxonomy;
- the 8E-009 rule that name similarity/source-document grouping cannot create component parentage;
- 10 recovered R1 vehicle/system candidates preserved as source-review-only evidence with zero automatic Definition promotion;
- explicit IA-D08-003 advanced-feature deferrals;
- deterministic foundation validation.

### Inspector / projection / reference cases — PR #227

Squash merge: `67017018b8a50694dd041230bc1b6f66395903d8`

Established:

- 14 Vehicle Inspector/projection field groups;
- 14 governed action contracts;
- 20 reference cases: 9 contract-grounded, 8 synthetic QA and 3 guardrail, with zero canonical synthetic records;
- permission-safe hidden aggregate protection;
- ownership/custody/control/station separation;
- source-unspecified/unknown Resource and capacity semantics;
- semantic movement and nonvisual operation requirements;
- idempotent recovery boundaries.

### Integrated workflows — PR #228

Squash merge: `4768a5ac6854f9b5f82a2bc81ae807f99d23f576`

Established:

- 15 integrated Vehicle/Mecha/Starship workflows;
- 13 authoritative mutation workflows with revalidation, expected-version and operation-ID/idempotency boundaries;
- 10 cross-domain handoff contracts;
- explicit coverage of all 20 PPIA-04 reference cases;
- cross-domain routing to PPIA-03, F007, F013, F014, F020 and F021 without inventing those domains' semantics.

## Current completion-candidate package

This final package adds:

- `PPIA-04_VEHICLE_MECHA_STARSHIP_EXPERIENCE_SPEC_v1.0.0.md` — integrated implementation-ready specification;
- `PPIA-04_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.0.json` — 42 requirements across 14 acceptance categories;
- explicit trace coverage for 14 projection groups, 14 action contracts, 15 workflows, 10 handoffs and all 20 reference cases;
- deterministic completion validation and CI.

The candidate branch continuity projection is aligned to the same active PPIA-04 completion action before exact-head validation; no completion state is projected early. The checkpoint also retains explicit dependency evidence for both PPIA-03 completion and the validated PPIA-03→PPIA-04 transition merge.

## Completion coverage

The candidate packet covers:

1. reusable Vehicle Definition, variant/configuration, component Definition, owned Asset, deployment and live-state separation;
2. ownership, custody, control, access, remote-operation and station-authority separation;
3. explicit component parent/compatibility evidence and no name-similarity auto-link;
4. installed configuration, hardpoint/slot and component-ownership separation;
5. crew, passengers, station assignment, revocation and declared command policy;
6. cargo, containers and carried/attached craft with PPIA-03 generic Asset handoff;
7. Scene deploy/recall without Asset duplication;
8. F013 semantic movement over canvas/pixel authority;
9. F007/F014 Player and GM/NPC vehicle operation and approval;
10. atomic system outcome and Resource cost behavior;
11. unknown/source-unspecified Resource/capacity semantics;
12. bounded power/fuel/ammunition/heat/maintenance behavior without deferred topology simulation;
13. damage/failure identity preservation and append-only repair/service history;
14. docking, boarding, launch, attach/detach and carried-craft relations;
15. capture/salvage custody/control versus ownership lineage;
16. permission-before-projection and hidden-information non-inference;
17. operation-ID, expected-version, idempotency, ambiguous-network recovery and reconnect reauthorization;
18. keyboard/touch/screen-reader/nonvisual movement, compact/mobile/high-zoom and reduced-motion operation;
19. source/provenance/conflict/recommendation distinctions, 10 R1 candidates accounted for and obsolete semantic database excluded;
20. IA-D08-003 deferred simulation boundaries preserved and inactive.

## Completion boundaries

PPIA-04 completion does **not**:

- alter raw Vehicle/Mecha/Spacecraft CSV source material;
- restore the obsolete 487-object semantic database as content authority;
- automatically promote any recovered R1 candidate;
- create component parentage or compatibility from name similarity or source-document grouping;
- invent source-unspecified capacities, Resources, systems or operating envelopes;
- make canvas pixels or visual overlap authoritative movement/docking rules;
- activate continuous Newtonian flight, full orbital mechanics, detailed power-grid routing, subsystem circuit simulation, structural finite-element damage, atmospheric-transition simulation, carrier fleet command, autonomous drones, programmable vehicle AI, full synchronized interior/exterior geometry or unrestricted custom processors;
- activate STAGE-A-A2;
- mutate application runtime;
- authorize release, deployment, tester access, paid services, production credentials or unsupported canonical promotion.

## Required completion evidence

PPIA-04 may become `completed_verified` only after:

1. the exact candidate head passes PPIA-04 completion validation;
2. applicable PPIA Program, PPIA-04 foundation/workflow, continuity and operational regression gates pass on that same head;
3. the candidate PR merges into canonical `main`;
4. the post-merge continuity checkpoint records the exact validated head, PR, merge SHA, `completed_verified` state and next dependency-optimized PPIA tranche.

Until those four conditions are satisfied, this document is a candidate, not a completion claim.
