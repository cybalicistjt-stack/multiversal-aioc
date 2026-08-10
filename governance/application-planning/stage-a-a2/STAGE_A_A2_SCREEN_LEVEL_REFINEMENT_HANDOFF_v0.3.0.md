# STAGE-A-A2 Screen-Level Refinement Handoff v0.3.0

**Work item:** STAGE-A-A2 — Universal Object Experience  
**Design status:** detailed screen refinement complete for eight anchor screens; implementation not started by this handoff  
**Branch:** `governance/stage-a-a2-detailed-design`  
**Owner/final authority:** John Brandon Turner

## Completed design scope

A local owner-visible package was produced for the next A2 design tranche:

`STAGE_A_A2_SCREEN_LEVEL_REFINEMENT_v0.3.0.zip`

SHA-256:

`d34dc57872a4700a4e5f978564326e3a46af7d75b232859f738b3363810dd472`

The package contains 2,409 lines of Markdown design specification plus machine-readable CSV matrices. It refines the existing A2 v0.2.0 universal-shell/presentation-profile design into screen-level implementation detail for:

1. Universal Content Library / Search
2. Item Inspector
3. Species Inspector
4. Ability Inspector
5. Creature Inspector
6. NPC Inspector
7. Vehicle Inspector
8. World / Setting Inspector

It also contains:

- shared screen architecture and pane/layout contract;
- exact source-backed field grouping for the seven anchor profiles;
- card and list signatures;
- filter/sort behavior;
- large/medium/compact responsive rules;
- relationship/provenance placement;
- Definition-versus-Live-Instance presentation rules;
- picker action behavior;
- profile comparison priorities;
- loading/offline/stale/conflict/permission state matrix;
- anchor profile field matrix;
- screen-refinement acceptance criteria.

## Locked design decisions

- A2 uses one universal Library/Inspector shell plus explicit `presentationProfileId` metadata.
- Presentation profile is never guessed from display name, filename, or stable-ID prefix.
- Definition, Variant, Placement, Live Instance, Snapshot, and Projection remain distinct record layers.
- Item, Species, Ability, Creature, NPC, Vehicle and World inspectors use different field priorities/section structures while sharing the same outer shell.
- Empty optional source fields are omitted rather than filled with invented/default content.
- Live mutable state appears in a separate `Current State` panel and never overwrites reusable Definition values.
- Relationship graph is optional; grouped relationship list/table is the required accessible default/equivalent.
- Provenance is progressive: badge → summary → field evidence → authorized source view.
- Mobile uses one-column Library flow and full-screen inspector with sticky caller action.
- The package does not claim an exhaustive mapping of all 245 governed object kinds because the row-level authoritative 8D-002 catalog is not currently exposed in the active canonical files; unknown kinds fall back to the structured-source profile until explicitly mapped.

## Source basis used

Design requirements were reconciled against:

- `.ai/current-work-order.md`;
- `MV-IA-F002_UNIVERSAL_OBJECT_EXPERIENCE.md`;
- `STAGE_A_UI_IMPLEMENTATION_PROGRAM.md`;
- UI and Screen Design Bibles;
- A2 v0.2.0 detailed design package;
- Content v2 / Batch 8E source shapes for Items, Abilities, Species, Creatures, NPCs, Vehicles/Mecha/Spacecraft, and World/Setting tables.

## Preservation boundary

This handoff deliberately does **not** change `CURRENT_WORK_POINTER.json`. The owner-selected Content v2 Batch 8E governed-promotion attempt remains primary until separately completed or redirected. STAGE-A-A2 remains the authorized application work item and this design work is preparatory/parallel.

Do not claim A2 implementation, A2 exit-gate completion, exhaustive 245-kind profile mapping, production content migration, or release/deployment authority from this handoff alone.
