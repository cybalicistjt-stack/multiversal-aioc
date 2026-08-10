# STAGE-A-A2 Behavioral Interaction Handoff v0.5.0

**Work item:** STAGE-A-A2 — Universal Object Experience  
**Design status:** behavioral interaction specification complete; implementation not started by this handoff  
**Branch:** `governance/stage-a-a2-detailed-design`  
**Owner/final authority:** John Brandon Turner

## Completed design scope

An owner-visible package was produced:

`STAGE_A_A2_BEHAVIORAL_INTERACTION_SPEC_v0.5.0.zip`

SHA-256:

`27078d7782610d4109b008b8d4ebc9a8a52e27bfe5088f5617b327e689e5ce7f`

The package contains 15 files / 2,020 lines and defines the behavioral layer over the locked v0.2.0–v0.4.0 A2 screen/presentation designs.

Completed behavior specifications:

1. Library → Inspector → relationship traversal → exact return/context restoration.
2. Single-select and bounded multi-select Picker behavior.
3. Mandatory final permission/entitlement/pack/version/compatibility revalidation before selection receipt.
4. Version, variant, stale-version and unresolved-conflict comparison.
5. Progressive provenance: badge → object summary → field evidence → authorized source view.
6. Keyboard/focus/nonvisual navigation and deterministic focus restoration.
7. Permission-safe URL/deep-link/browser-history semantics.
8. Local recovery of query/filter/provisional Picker intent with reauthorization/revalidation.
9. First concrete A2 reference slice: `Scene Builder → Add Object`.
10. State-machine, telemetry, URL-state schema and 20 behavioral acceptance gates.

## Locked behavior boundary

- A2 browsing, inspection, comparison and provisional selection are nonauthoritative.
- Stable IDs and version policy cross the A2/caller boundary; display names never become identity.
- The Picker issues a receipt only after current revalidation.
- The calling workflow owns authoritative mutation after receipt.
- In the Scene Builder reference slice, the caller creates new Campaign-local placement IDs pointing to selected source Definition stable IDs; source Definitions are not mutated.
- Authorization precedes results, facets, suggestions, relationships and source projections.
- Browser/URL state never grants access.
- Relationship traversal independently reauthorizes each target.
- Compare is read-only and never silently resolves conflicts.
- Provenance/source views are read-only evidence.
- Desktop/mobile/keyboard flows must yield equivalent selection semantics.

## Reference-slice source basis

`MV-IA-F005_CAMPAIGN_SCENE_AND_SESSION_BUILDER.md` requires the GM to select Locations, environments, hazards, creatures, NPCs, items, vehicles, clues, objectives and other governed objects by stable ID and create Campaign-local placements/overrides without mutating source Definitions. The v0.5.0 reference slice deliberately implements only enough caller fixture behavior to prove that A2 boundary; it does not claim full A5 Scene Builder or Session implementation.

## Validation

- package ZIP CRC: PASS;
- no TODO/TBD/FIXME/PLACEHOLDER markers;
- deterministic package manifest and SHA256SUMS included;
- behavioral acceptance set: 20 blocking gates.

## Preservation boundary

This handoff deliberately does **not** change `CURRENT_WORK_POINTER.json`. The owner-selected Content v2 Batch 8E governed-promotion attempt remains primary until separately completed or redirected. STAGE-A-A2 remains the authorized application work item and this package is preparatory/parallel design.

Do not claim A2 implementation, A2 exit-gate completion, A5 Scene Builder completion, production content migration, canonical promotion, release, or deployment authority from this handoff alone.
