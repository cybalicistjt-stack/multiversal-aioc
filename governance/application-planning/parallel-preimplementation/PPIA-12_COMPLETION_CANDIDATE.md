# PPIA-12 — Completion Candidate

**Work item:** PPIA-12 — World & Setting Authoring System  
**State:** COMPLETION CANDIDATE — NOT COMPLETE UNTIL THIS EXACT HEAD PASSES REQUIRED VALIDATION AND MERGES  
**Owner:** John Brandon Turner

## Verified upstream milestones

### Foundation — PR #236

Squash merge: `f5feda7d8250cd20fbe59176dff9af397ac61932`

Established:

- 22 primary setting/cosmology/location PDFs / 693 pages;
- 8 reusable environment-template PDFs / 238 pages;
- 2 authoring-guidance PDFs / 30 pages;
- 32 retained PDFs / 961 pages total;
- no dedicated World/Setting CSV catalog;
- 14-layer World/Setting identity-state taxonomy and 12 presentation profiles;
- explicit source-scope, typed-hierarchy, environment-template, world-local-extension, Campaign-state, permission, provenance, recovery and accessibility boundaries.

### Inspector / projection / reference cases — PR #237

Squash merge: `fc95b079dbeaeec5dbcaf468423687f0b0760499`

Established:

- 14 World/Setting Inspector projection groups aligned one-to-one with the taxonomy;
- 16 governed action contracts;
- 12 authoritative mutation action paths;
- 20 reference cases: 13 contract-grounded, 4 synthetic QA and 3 guardrails;
- explicit hierarchy-evidence, nonplanetary setting, route/connectivity, local-rules, environment-template, mixed-facet, conflict, privacy, recovery and nonvisual-accessibility contracts.

### Integrated workflows — PR #238

Squash merge: `9d85d019ac6eb701846f4f8edb0eddd6adfd31ac`

Established:

- 16 integrated World/Setting workflows;
- 12 authoritative mutation workflows with revalidation, expected-version and operation-ID/idempotency boundaries;
- 10 cross-domain handoff contracts;
- explicit coverage of all 16 Inspector actions and all 20 PPIA-12 reference cases;
- routing to F002, PPIA-08, PPIA-02/03/04/05, owning Ability/rules domains, PPIA-11, F020/F021 and F022 without absorbing those domains.

## Current completion-candidate package

This final package adds:

- `PPIA-12_WORLD_SETTING_AUTHORING_EXPERIENCE_SPEC_v1.0.0.md` — integrated implementation-ready specification;
- `PPIA-12_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.0.json` — 48 requirements across 16 acceptance categories;
- exact trace coverage for 14 projection groups, 16 action contracts, 16 workflows, 10 handoffs and all 20 reference cases;
- deterministic completion validation and CI.

The candidate continuity projection remains aligned to active PPIA-12 completion work before exact-head validation. No `completed_verified` state is projected early.

## Completion coverage

The candidate packet covers:

1. reusable Setting Definition versus Campaign instance/current state separation;
2. source fact, unknown, conflict/revision, proposal and accepted-authored state separation;
3. 14-layer typed World/Setting identity-state model;
4. nonplanetary hierarchy for worlds, branches, planes, layers, city-stations, generation ships, routes, districts and other sourced entities;
5. Havalaea→Vertigon explicit hierarchy evidence and no co-occurrence auto-link;
6. reusable environment-template versus setting-attached environment separation;
7. infrastructure/landmark typing without generic Item/Vehicle conflation;
8. faction/institution/governance separation from location identity;
9. culture/society/economy separation from Species biology;
10. history/era/timeline evidence and Stratebrait-style conflict preservation;
11. world-local Species/Creature/Item/Vehicle/Ability extension scoping with owning-domain preservation;
12. Musical Reality, branch-local and unusual-local-physics rule scoping without universalization;
13. explicit route/portal/connectivity evidence and hidden-route filtering before pathfinding;
14. PPIA-08 Campaign/Scene instantiation handoff and Campaign-local mutation isolation;
15. permission-before-search/count/map/pathfinding/export/AI-context behavior;
16. authoring guidance/random tables/templates/AI suggestions as proposals only;
17. operation-ID, expected-version, idempotency, ambiguous-network recovery and reconnect reauthorization;
18. keyboard/touch/screen-reader, compact/high-zoom/reflow, reduced-motion and semantic non-map operation;
19. source/provenance/conflict/revision/authoring-decision distinctions;
20. explicit downstream ownership and no runtime/release authorization.

## Completion boundaries

PPIA-12 completion does **not**:

- mutate retained raw World/Setting/environment PDFs;
- invent or restore a World/Setting CSV authority that does not exist;
- create hierarchy, membership, routes, chronology or compatibility from co-occurrence, same document, name similarity, theme, proximity, document order or AI inference;
- force all settings into planet/continent/country/city geography;
- automatically instantiate reusable environment templates into named settings;
- universalize Musical Reality, branch-specific or other setting-local mechanics;
- replace PPIA-02 Creature/NPC, PPIA-03 Item, PPIA-04 Vehicle, PPIA-05 Species/Form or owning Ability/rules Definitions;
- rewrite reusable Setting Definitions from Campaign destruction, occupation, discovery, renaming, current control or Scene state;
- silently reconcile Stratebrait-style older/current/new conflicts or overwrite raw source;
- turn random tables, Worldbuilding guidance, templates or AI suggestions into accepted canon automatically;
- expose hidden locations, routes, factions, history or secrets through aggregates, maps, pathfinding, errors, exports, diagnostics, notifications or AI context;
- permit broad offline authoritative World/Setting mutation;
- activate STAGE-A-A2;
- mutate application runtime;
- authorize release, deployment, tester access, paid services, production credentials or unsupported canonical promotion.

## Required completion evidence

PPIA-12 may become `completed_verified` only after:

1. the exact candidate head passes PPIA-12 completion validation;
2. every applicable PPIA Program, transition, continuity, interaction, operational and regression gate passes on that same exact head;
3. the candidate PR merges into canonical `main`;
4. the post-merge continuity checkpoint records the exact validated head, PR, merge SHA, `completed_verified` state and next dependency-optimized PPIA tranche.

Until all four conditions are satisfied, this document is a candidate, not a completion claim.
