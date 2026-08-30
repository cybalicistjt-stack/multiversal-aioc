# AKWI-03 — Akwi NPC Library

Version: 1.0.0  
Status: COMPLETED / VERIFIED  
Owner authority: John Brandon Turner  
Authorized: 2026-08-30  
Completed: 2026-08-30  
Application baseline: `0c12b20b96add5aa2a82583d7bd33cb86f08c8f8`  
Tested application head: `41a5bee4726213ad8572ab194c9b36c63bee2edf`  
Application merge: `5110a564d6541d3e81a321339fe5173bad52765b`  
AIOC baseline: `29376e3472dd9c7eaba461760729df6c6a69a5c9`

## Objective

Integrate the owner-authorized 400-row Akwi NPC suite into the existing Universal Library while preserving the source package's proposal/canon labels, keeping unresolved mechanics unresolved, and preventing Character-private or GM-only dossier fields from entering the current allow-all local A2 client corpus.

## Source identity

- Package: `akwi_game_integration_package_v0.1.zip`
- Package SHA-256: `f5f065d893369947dc4b62f4bb54fc760671bb68f08030eb578d7429bb83a2ca`
- NPC table: `akwi_npc_suite_400.csv`
- NPC table SHA-256: `6beb67730a0c2a6051501dd1d78d5a1d420127f1ae281a2eac05e7fbccee7b34`
- Exact source row count: 400.
- Source-integrity run: `33332294496`.
- Materialization run: `33332324262`.

## Implemented content

AKWI-03 publishes all 400 NPC identities as `P-A2-NPC` Universal Objects. Import did not change source truth status: 399 source rows remain `Proposed new content`; Fylander "Fy" Mariposa remains `Mixed: supplied canon plus proposed scaffolding`; all 400 retain `Pending creator acceptance` unless a later owner action explicitly changes them.

The runtime projection carries only public-safe/source-backed identity and descriptive Character fields. Existing governed references are reused rather than copied:

- every NPC resolves Species to `species.akwi`;
- every NPC resolves homeworld to governed `world.aiwiio`;
- 186 source background candidates resolve to corresponding governed AKWI-02 Background stable IDs as candidate/proposed selections;
- 214 NPCs intentionally remain without a background candidate.

The resulting governed corpus contains:

- 400 NPC objects;
- 986 safe relationships;
- 400 provenance rows bound to the exact source-table hash.

## Visibility boundary

The current A2 authorization contract filters whole objects before search/inspection, while the local-alpha application deliberately uses a development allow-all projection. AKWI-03 therefore excludes field-level hidden dossier content from every A2-loaded NPC object.

The following source columns remain outside the client runtime:

- `character_private_knowledge`;
- `gm_only_secret`.

GM-oriented plot material that would reveal undisclosed internal state or twists was not promoted merely to make current client objects appear complete. The source package remains recovery authority for omitted dossier material until a role-aware GM/private projection exists.

Verified result: `private_runtime_fields = 0`.

## Mechanical boundary

- No HP, Armor Class, speed, proficiency bonus, initiative bonus, level, resource math, action math, or other missing rules-profile numbers were invented.
- `encounter_tier`, `skills_or_competencies`, Burst use, Aural Sensory training, Spring-Leg use, conflict style, and source mechanics-status text remain descriptive guidance only.
- The 22 proposed mechanical-archetype definitions and 400-row archetype mapping were not converted into authoritative numerical Character state.
- Species abilities continue to resolve from existing shared Species/ability records; modifiers are not copied into NPC rows.

Verified result: `invented_numeric_mechanics = 0`.

## Dependency boundary

Generated/proposed world, faction, setting, location, birthplace, and other scaffolding named by the NPC suite were not promoted into canonical Universal Objects. Unresolved names may remain descriptive NPC text; existing governed AKWI-01/02 objects are linked only where identity was already resolved.

Verified result: `generated_dependency_objects_promoted = 0`.

## Existing-content boundary

AKWI-03 reuses the existing `P-A2-NPC` profile, Universal Library loader, authorization-first search/inspection, relationship graph, and provenance projection. No Akwi-only NPC UI was introduced and the active SSA software roadmap was not changed.

## Verification and completion evidence

The final application candidate was `41a5bee4726213ad8572ab194c9b36c63bee2edf` on PR #356.

Validation run `33332830247` passed on the exact candidate with:

- repository health job `99329132794`: PASS;
- Linux shared validation job `99329133213`: PASS;
- Windows shared validation job `99329132747`: PASS after the owner restored the existing self-hosted Windows runner environment;
- deterministic cross-platform comparison job `99329216298`: PASS;
- deterministic comparison receipt SHA-256: `fdf43933d64ebc08bb9cb2e356b667c39a5717c27a217c8cceb991a89e2ba93c`;
- successful comparison artifact `9739942238`, artifact digest `sha256:fcc0e4921444f2a7f8238cfa26c46f6ece24004f148732aa387441557361b2a1`.

PR #356 was squash-merged in accordance with repository policy. Live application `main` was re-read after merge and confirmed at `5110a564d6541d3e81a321339fe5173bad52765b`.

## Acceptance result

All ten AKWI-03 acceptance conditions are satisfied. Implementation authority is retired. Any future work involving field-level GM/private NPC dossier projection, promotion of generated world/faction/location dependencies, or authoritative NPC rules-profile mechanics requires a separately governed tranche.
