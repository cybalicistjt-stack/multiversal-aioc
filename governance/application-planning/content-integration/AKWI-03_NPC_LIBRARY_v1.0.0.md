# AKWI-03 — Akwi NPC Library

Version: 1.0.0  
Status: IMPLEMENTATION AUTHORIZED / IN PROGRESS  
Owner authority: John Brandon Turner  
Authorized: 2026-08-30  
Application baseline: `0c12b20b96add5aa2a82583d7bd33cb86f08c8f8`  
AIOC baseline: `29376e3472dd9c7eaba461760729df6c6a69a5c9`

## Objective

Integrate the owner-authorized 400-row Akwi NPC suite into the existing Universal Library while preserving the source package's proposal/canon labels, keeping unresolved mechanics unresolved, and preventing Character-private or GM-only dossier fields from entering the current allow-all local A2 client corpus.

## Source identity

- Package: `akwi_game_integration_package_v0.1.zip`
- Package SHA-256: `f5f065d893369947dc4b62f4bb54fc760671bb68f08030eb578d7429bb83a2ca`
- NPC table: `akwi_npc_suite_400.csv`
- NPC table SHA-256: `6beb67730a0c2a6051501dd1d78d5a1d420127f1ae281a2eac05e7fbccee7b34`
- Exact source row count: 400.

## Authorized content

AKWI-03 may publish all 400 NPC identities as `P-A2-NPC` Universal Objects. Authorization to import does not change source truth status: 399 source rows remain `Proposed new content`; Fylander "Fy" Mariposa remains `Mixed: supplied canon plus proposed scaffolding`; all 400 retain `Pending creator acceptance` unless a later owner action explicitly changes them.

The runtime projection may carry source-backed public-safe identity and descriptive Character fields, including name/callsign, Species reference, appearance, age/life-stage/pronouns when supplied, occupation, cultural/diaspora context, languages, public description/knowledge, encounter guidance without numeric rule invention, and explicit source status/provenance labels.

Existing governed references may be resolved without copying their definitions:

- every NPC resolves Species to `species.akwi`;
- Akwi homeworld may resolve to governed `world.aiwiio`;
- source background candidates may resolve to the corresponding governed AKWI-02 Background stable ID, while remaining candidate/proposed selections rather than authoritative Character grants.

## Visibility boundary

The current A2 authorization contract filters whole objects before search/inspection, while the local-alpha application deliberately uses a development allow-all projection. Therefore AKWI-03 must not place field-level hidden dossier content inside any A2-loaded NPC object.

The following source columns are expressly excluded from the client runtime:

- `character_private_knowledge`;
- `gm_only_secret`.

GM-oriented plot material that would reveal undisclosed internal state or twists must likewise not be promoted merely to make the current client object appear complete. The source package remains the recovery authority for omitted dossier material until a role-aware GM/private projection exists.

Tests must prove forbidden private field names and source values are absent from every AKWI-03 runtime JSONL file.

## Mechanical boundary

- No HP, Armor Class, speed, proficiency bonus, initiative bonus, level, resource math, action math, or other rules-profile numbers may be invented where the source does not define them.
- `encounter_tier`, `skills_or_competencies`, Burst use, Aural Sensory training, Spring-Leg use, conflict style, and source mechanics-status text are descriptive guidance only.
- The 22 proposed mechanical-archetype definitions and the 400-row archetype mapping are not authoritative numerical Character state and are not automatically granted by this tranche.
- Species abilities resolve from existing shared Species/ability records; modifiers are not copied into NPC rows.

## Dependency boundary

The NPC reference map contains generated/proposed world, faction, setting, location, and other scaffolding. Owner authorization of the NPC library does not automatically promote those dependencies into canonical Universal Objects.

AKWI-03 may preserve unresolved names as descriptive NPC text. It must not create canonical dependency objects merely because an NPC row names a faction, setting, birthplace, or location. Existing governed AKWI-01/02 objects may be linked only where identity is already resolved.

## Existing-content boundary

AKWI-03 reuses the current `P-A2-NPC` profile, Universal Library loader, authorization-first search/inspection, relationship graph, and provenance projection. No Akwi-only NPC UI and no change to the active SSA software roadmap are authorized.

## Acceptance

AKWI-03 is complete only when:

1. exactly 400 owner-authorized Akwi NPC objects load through the normal A2 corpus;
2. all 400 have unique source `npc_id` stable IDs and `P-A2-NPC` presentation;
3. source canon/approval labels remain unchanged;
4. all NPCs resolve `species.akwi` without copying Species mechanics;
5. candidate background relationships resolve only to already-governed AKWI-02 Background objects and remain non-authoritative;
6. no generated setting/faction/location dependency object is promoted by this tranche;
7. no `character_private_knowledge` or `gm_only_secret` data leaks into A2 runtime content;
8. no invented numeric combat/Character mechanics are introduced;
9. provenance exists for all 400 NPC objects and binds to the exact source table hash;
10. exact-head repository health, self-hosted Linux, self-hosted Windows, and deterministic comparison are green before merge.
