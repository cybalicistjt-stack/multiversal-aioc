# PPIA-02 Completion Candidate

**Work item:** PPIA-02 — Creature & NPC Experience  
**State:** READY FOR FINAL EXACT-HEAD VALIDATION — NOT COMPLETE UNTIL MERGED  
**Branch:** `governance/ppia-02-creature-npc-experience`  
**Pull request:** #217

## Completion-gate requirement

PPIA-02 must deliver an implementation-ready Creature/NPC experience packet with permission-safe presentation, authoring, encounter, variant, relationship, asset, transformation, accessibility, and source-grounded reference contracts.

The branch now contains all required design artifacts.

## Source and authority package

- `PPIA-02_SOURCE_AND_DESIGN_INVENTORY.md`
- 23 dedicated Creature PDFs + `Player Creatures.PDF` inventoried with SHA-256 provenance.
- Representative source review covers Creature Types, Havalaea Creatures, Dragons, and Player Creatures.
- The later 8E-009 CSV-first registry is respected for its own domains but is not falsely treated as a dedicated Creature catalog.
- The unsuccessful 487-object semantic-parse database is explicitly excluded from Creature/NPC content authority.

## Experience architecture

- `PPIA-02_EXPERIENCE_TAXONOMY_v0.1.0.json`
  - 7 object/experience layers;
  - 8 presentation profiles;
  - 10 experience contexts;
  - 13 Inspector section families;
  - explicit no-A2/no-runtime-mutation boundaries.

- `PPIA-02_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json`
  - permission-before-serialization model;
  - Player/GM/Assistant-GM/Creator-Owner-Admin/service-AI projection boundaries;
  - profile section ordering and context overlays;
  - responsive/accessibility behavior;
  - source/recommendation/conflict/provenance handling.

## Workflow package

`PPIA-02_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json` defines ten governed workflows:

1. Library / Inspector reference
2. GM NPC & Creature Manager authoring
3. Scene quick-add / placement
4. Encounter preparation / balance analysis
5. Live runtime
6. Investigation / social NPC use
7. Exploration / bestiary / discovery
8. Variant / template / stage comparison
9. Summon / minion / spawn
10. Playable creature conversion

Each workflow identifies entry points, preconditions, actions, outputs, owning mutation surface, revalidation, privacy, recovery, accessibility, and identity boundaries. Nine explicit cross-workflow handoff contracts prevent provisional/read-only surfaces from becoming authoritative mutation paths.

## Integrated specification

`PPIA-02_CREATURE_NPC_EXPERIENCE_SPEC_v1.0.0.md` consolidates:

- definitive Creature/NPC presentation hierarchy;
- ordinary creature, NPC persona, sentient hybrid, swarm/group, summon/minion, stage/variant/form, type-modifier, and playable-conversion behavior;
- Definition/placement/live-instance distinction;
- GM Manager and authoring rules;
- quick-add and placement rules;
- Encounter preparation and launch boundary;
- live runtime action/reconnect boundary;
- named NPC versus generic creature behavior;
- ecology/bestiary/discovery;
- relationships/factions/investigation/social use;
- equipment/inventory/loot linkage;
- variants/forms/transformations;
- summons/minions/spawns;
- playable conversion;
- search/filter/compare/quick actions;
- responsive/accessibility;
- recovery/offline;
- provenance/conflict;
- downstream dependency routing.

## Reference cases

`PPIA-02_REFERENCE_CASES_v0.1.0.json` now contains **13** cases:

- **7 source-grounded** cases:
  - Sapcrawl Varnet ordinary bestiary/Behavior;
  - Mossling Glider movement/reaction;
  - Fire-Type Animals type-modifier semantics;
  - Dragon age/power stage chain;
  - Dragon sentience spectrum;
  - monster-to-playable-species conversion;
  - Havalaean Sapient Animal conversion.

- **6 explicitly noncanonical synthetic QA** cases:
  - named NPC hidden motive/testimony/inventory;
  - hidden Scene placement/reinforcement privacy;
  - summon/minion lifecycle/controller;
  - swarm/group projection;
  - incomplete/conflicted source record;
  - live alternate-form transformation/privacy/reconnect.

Synthetic QA cases are not lore/canonical content.

## Acceptance and traceability

`PPIA-02_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.0.json` defines **36 requirements** with upstream/source, contract, reference-case, and verification traceability.

`PPIA-02_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.1.json` corrects the original summary category count from 15 to the effective **16 categories** without changing the 36 requirement bodies.

The sixteen categories are:

1. identity
2. presentation
3. privacy
4. authoring
5. Scene placement
6. encounter
7. runtime
8. social/investigation
9. ecology/bestiary
10. assets
11. variants/forms
12. summons
13. playable conversion
14. accessibility
15. provenance
16. recovery

## Key non-negotiable outcomes

- Hidden Creature/NPC existence and derived cardinality never reach unauthorized projections.
- Definition, placement, and live-instance identities remain separate.
- Presentation profile never grants authority or creates a canonical type.
- Linked governed mechanics remain references to owning objects.
- Campaign-local authoring never becomes source truth silently.
- Encounter balance output remains advisory.
- Runtime state never writes back to reusable Definitions.
- Type modifiers and source variants never auto-merge by name.
- Runtime transformations use the owning Ability/Action/Session workflow.
- Summons preserve source/placement/instance/controller/master distinctions.
- Playable conversion produces Character/species draft/provenance, not identity equivalence.
- Incomplete/conflicted sources remain usable without invented replacement facts.
- Dense stat presentation has keyboard, screen-reader, touch, high-zoom, reduced-motion, and textual comparison alternatives.
- PPIA-02 does not activate A2, implement runtime behavior, release, deploy, or promote unsupported source content.

## Validation gates

The branch includes:

- `validate-ppia02-foundation.py`
- `validate-ppia02-experience-contracts.py`
- `validate-ppia02-completion-contracts.py`
- `validate-ppia-02-foundation.yml`
- `validate-ppia-02-completion.yml`

PPIA-02 must not be declared complete unless the final candidate head passes all applicable exact-head repository gates and PR #217 merges canonically.

## Optional owner-side provenance recovery

Not blocking PPIA-02: if the owner has `Aaac (1).zip` or the exact package `Multiversal_8E-008G-R1_Source_Boundary_and_Provenance_Closure_v0.1.0`, upload it. It may close the old historical 8E-008G provenance question. It is not needed to validate the current Creature/NPC experience package.
