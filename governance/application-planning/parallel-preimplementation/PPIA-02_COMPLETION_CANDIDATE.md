# PPIA-02 Completion Candidate

**Work item:** PPIA-02 — Creature & NPC Experience  
**State:** READY FOR FINAL EXACT-HEAD VALIDATION — NOT COMPLETE UNTIL MERGED  
**Branch:** `governance/ppia-02-creature-npc-experience`  
**Pull request:** #217

## Completion-gate requirement

PPIA-02 must deliver an implementation-ready Creature/NPC experience packet with permission-safe presentation, authoring, encounter, variant, relationship, asset, transformation, accessibility, and source-grounded reference contracts.

The branch contains the required design artifacts. Completion still requires exact-head validation and canonical merge.

## Source and authority package

- `PPIA-02_SOURCE_AND_DESIGN_INVENTORY.md`
- 23 dedicated Creature PDFs + `Player Creatures.PDF` inventoried with SHA-256 provenance.
- Representative source review covers Creature Types, Havalaea Creatures, Dragons, and Player Creatures.
- The later 8E-009 CSV-first registry is respected for its own domains but is not falsely treated as a dedicated Creature catalog.
- The unsuccessful 487-object semantic-parse database is explicitly excluded from Creature/NPC content authority.

### Recovered 8E-008G-R1 source accountability

Owner-supplied `This.zip` recovered the substantive 8E-008G-R1 closure outputs and was canonically recorded in merge `d271d1e7ec453cd153a7bf5768b3df837ba677a9`.

Recovered R1 result:

- 101 / 101 acceptance checks PASS;
- 7,144 / 7,144 structural candidates accounted;
- 2,766 formerly unbound candidates closed;
- 0 unbound source sections remain;
- 158,189 authoritative records provenance-accounted;
- 1,671 candidates formally deferred rather than silently excluded.

R1 passes source accountability, not Public Canon completeness. Formal deferral is neither canonical promotion nor exclusion.

The recovered R1 register contains **93 formally deferred creature candidates**. PPIA-02 retains their exact identity/source/page/heading subset in `PPIA-02_R1_DEFERRED_CREATURE_CANDIDATES.csv` and governs their experience in `PPIA-02_R1_PROVENANCE_AND_DEFERRED_CREATURE_ADDENDUM_v0.1.0.json`.

A formally deferred creature candidate may be inspected as authorized source-recovery/provenance evidence but is not a canonical Creature/NPC Definition, is not included in ordinary canonical Library results, cannot be quick-added/launched as a participant without a governed usable Definition or Campaign-local authored object, and receives no invented stat block or mechanics merely to make it usable.

**This historical recovery request is now resolved.** No further upload of `Aaac (1).zip` or the historically named R1 wrapper is required to complete PPIA-02.

## Experience architecture

`PPIA-02_EXPERIENCE_TAXONOMY_v0.1.0.json` defines:

- 7 object/experience layers;
- 8 presentation profiles;
- 10 experience contexts;
- 13 Inspector section families;
- explicit no-A2/no-runtime-mutation boundaries.

`PPIA-02_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json` defines:

- permission-before-serialization behavior;
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

The R1 provenance/deferred-creature addendum supplements the integrated specification's source, Inspector, provenance, and completion sections with the explicit `formally_deferred_source_candidate` state and no-silent-promotion rule.

## Reference cases

`PPIA-02_REFERENCE_CASES_v0.1.0.json` contains **13** cases.

Seven source-grounded cases:

- Sapcrawl Varnet ordinary bestiary/Behavior;
- Mossling Glider movement/reaction;
- Fire-Type Animals type-modifier semantics;
- Dragon age/power stage chain;
- Dragon sentience spectrum;
- monster-to-playable-species conversion;
- Havalaean Sapient Animal conversion.

Six explicitly noncanonical synthetic QA cases:

- named NPC hidden motive/testimony/inventory;
- hidden Scene placement/reinforcement privacy;
- summon/minion lifecycle/controller;
- swarm/group projection;
- incomplete/conflicted source record;
- live alternate-form transformation/privacy/reconnect.

Synthetic QA cases are not lore/canonical content.

The recovered 93 R1 creature candidates are **not** added as synthetic or canonical reference creatures. They are a provenance/source-recovery dataset governed by existing provenance requirements plus the R1 addendum.

## Acceptance and traceability

`PPIA-02_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.0.json` defines **36 requirements**.

`PPIA-02_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.1.json` corrects the original summary category count to the effective **16 categories** without changing the 36 requirement bodies.

The R1 addendum maps formal-deferral behavior to existing requirements:

- PPIA02-REQ-003 — no identity/merge from name similarity;
- PPIA02-REQ-007 — privacy filtering before serialization and derived counts;
- PPIA02-REQ-034 — provenance state distinctions;
- PPIA02-REQ-035 — incomplete/deferred evidence remains usable without invented replacement fields.

The sixteen categories remain identity, presentation, privacy, authoring, Scene placement, encounter, runtime, social/investigation, ecology/bestiary, assets, variants/forms, summons, playable conversion, accessibility, provenance, and recovery.

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
- Formally deferred R1 creature candidates remain source-recovery/provenance evidence until a separate governed disposition creates/binds/excludes/supersedes/waives them.
- Dense stat presentation has keyboard, screen-reader, touch, high-zoom, reduced-motion, and textual comparison alternatives.
- PPIA-02 does not activate A2, implement runtime behavior, release, deploy, or promote unsupported source content.

## Validation gates

The branch includes:

- `validate-ppia02-foundation.py`
- `validate-ppia02-experience-contracts.py`
- `validate-ppia02-completion-contracts.py`
- `validate-ppia-02-foundation.yml`
- `validate-ppia-02-completion.yml`

The final completion validator additionally verifies the recovered R1 PASS evidence, the 93-candidate reference-set count/distribution/hash, formal-deferral behavior, and no-promotion boundaries.

PPIA-02 must not be declared complete unless the final candidate head passes all applicable exact-head repository gates and PR #217 merges canonically.
