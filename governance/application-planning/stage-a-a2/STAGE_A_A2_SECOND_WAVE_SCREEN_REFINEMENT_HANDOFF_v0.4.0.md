# STAGE-A-A2 Second-Wave Screen Refinement Handoff v0.4.0

**Work item:** STAGE-A-A2 — Universal Object Experience  
**Design status:** second-wave screen refinement complete; implementation not started by this handoff  
**Branch:** `governance/stage-a-a2-detailed-design`  
**Owner/final authority:** John Brandon Turner

## Completed design scope

Owner-visible package produced:

`STAGE_A_A2_SECOND_WAVE_SCREEN_REFINEMENT_v0.4.0.zip`

SHA-256:

`5112362edf19e5159306fefaa7b99e809e7395e2a9fa4b903e9b297897ae91b5`

The package contains 22 files and 1,956 lines of detailed design specification/matrices. It continues the locked v0.3.0 Universal Library and inspector-shell architecture and completes detailed screen specifications for the remaining presentation families:

1. Action / Reaction / Maneuver
2. Effect / Modifier
3. Condition / Status
4. Resource / Pool
5. Environment / Biome
6. Hazard / Trap
7. Facility / Base / Structure
8. Location / Region / Settlement
9. Faction / Organization
10. Relationship / Reputation
11. Scene / Encounter / Adventure
12. Clue / Evidence
13. Rule / Rules Profile
14. Pack / Collection
15. Source / Provenance
16. Generic Structured Source fallback

Supporting material includes:

- explicit source-basis classification separating directly source-shaped screens from contract-shaped screens;
- exact source-field/section mapping matrix;
- responsive/action-placement matrix;
- second-wave acceptance gates;
- package manifest with per-file hashes.

## Locked decisions

- v0.3.0 universal Library/Inspector shell remains controlling; no new duplicate browser architecture is introduced.
- `presentationProfileId` remains explicit metadata and must never be inferred from display name, filename, or stable-ID prefix.
- Directly source-shaped profiles are Environment, Hazard/Trap, Facility/Base, Location, Faction/Organization, Branch Rules Profile, and Source/Provenance.
- Contract-shaped profiles define UI slots only when the governed projection supplies data; they do not authorize invented values.
- Hazard source rows explicitly classified as `Rules Framework` route to the Rule profile, not the Hazard encounter profile.
- `Bases_Facilities.csv` rows route by explicit record type/profile; support/material rows must not be presented as facilities.
- Definition, Variant, Placement, Live Instance, Snapshot, and Projection remain distinct record layers.
- Hidden information is removed at projection/search/facet/relationship level rather than hidden visually in the client.
- Generic Structured Source remains lossless and does not infer unknown domain semantics.
- Pack inspection does not authorize install/update/remove; Source inspection does not authorize source editing; no screen authorizes canonical promotion or deployment.

## Source basis used

- A2 v0.2.0 presentation-profile contracts.
- A2 v0.3.0 screen architecture and seven anchor inspector patterns.
- Batch 8E Content v2 Environment definitions/evidence and Environment-Ability links.
- Frozen `Hazards_Traps.csv` and `Bases_Facilities.csv` source catalogs.
- World/Setting place, relationship, connection, rule, event and hook tables.
- Batch 8D Empire faction/organization definitions.
- Batch 8C Branch Rules Profile definitions/source text/page evidence/branch-setting links.
- Batch 8E source/provenance/completeness/relationship receipts and ledgers.
- Canonical Internal Alpha/Stage A contracts for Action, Effect, Condition, Resource, Scene, Evidence, Pack and role-safe relationships.

## Preservation boundary

This handoff deliberately does **not** modify `CURRENT_WORK_POINTER.json`. The owner-selected Content v2 Batch 8E governed-promotion attempt remains primary until separately completed or redirected. STAGE-A-A2 remains the authorized application work item and this material is parallel preparatory design.

Do not claim A2 implementation, A2 exit-gate completion, exhaustive production data mapping, production content migration, Public Canon completeness, or release/deployment authority from this handoff.
