# CEW-06 — Ecological Role & Encounter-Use Classification Contract

**Contract:** `CEW-ECO-1.0`  
**Work item:** CEW-06 — Ecological Role & Encounter-Use Classification  
**Authority:** content/recovery/design/provenance only; no application implementation authority.

## Purpose

CEW-06 populates the `ecological_role` and reusable encounter-search portions of `CEW-CLASS-1.0` from retained creature-source evidence. It consumes `CEW-ID-1.0`, `CEW-TAX-1.0`, `CEW-CLASS-1.0`, `CEW-HAB-1.0`, `CEW-DIST-1.0`, and the PPIA-02 Creature & NPC experience boundary.

**Ecological role is not creature identity, habitat, or geographic distribution.** A creature can be a predator, scavenger, sap-feeder, guardian, herd animal, swarm creature or exotic resource consumer without those labels changing its stable identity, creature type, habitat requirements or canonical range.

## Four role dimensions

CEW-06 keeps four independently sourced dimensions:

1. `trophic_resource_role` — predator, scavenger, herbivore, sap-feeder, parasite, unusual resource-feeder or unknown;
2. `social_aggregation` — solitary, pair, pack, herd, swarm, colony or unknown;
3. `ecosystem_interaction` — territorial defender, guardian, ecosystem engineer, symbiont, resource source or unknown;
4. `encounter_use_facet` — reusable GM-facing discovery/preparation facets such as ambusher, lure/trapper, pack or swarm pressure, lookout/alarm, sentinel/guardian, terrain control, area denial, pursuit/stalking, hit-and-run, noncombat/negotiable or unknown.

Values are not mutually exclusive. Multiple source-backed values may coexist, and conflicts or missing information remain explicit.

## Source-evidence rule

Every asserted value requires direct retained-source wording or separate governed authority strong enough to support that value. Source silence remains unknown.

Game type, subtype, CR/threat value, size, alignment, movement mode, damage type, resistance, habitat fit, canonical range, name, visual resemblance or a single combat mechanic does not automatically create an ecological role.

A mechanic may corroborate directly sourced behavior, but CEW-06 does not reverse-engineer ecology from mechanics merely because a tactic looks plausible.

**A predator label does not imply a specific prey species.** Predator, parasite, symbiont, resource-source and comparable relationship labels require separately sourced target relationships before a named target is attached.

**A guardian label does not imply ownership, faction allegiance, personhood, or domestication.** It records only the source-backed protective/guarding role. Cognition, personhood, domestication, autonomy and partnership remain CEW-09/10/11 concerns.

Statements that communities use an animal or creature do not establish domestication, training, ownership, mount capability, pet/companion status or familiar compatibility.

## Multiversal resource feeding

The source corpus includes beings whose consumption does not fit ordinary Earth trophic categories. `resource_feeder` is therefore a controlled bridge term for directly sourced consumption of unusual physical, spatial, energetic or comparable resources.

**Exotic resource feeding remains source-specific rather than being forced into Earth trophic vocabulary.** The raw target is retained with provenance. For example, the Tesseravore source explicitly says it feeds on volume and spatial structure; CEW-06 preserves that target rather than inventing an Earth-food analogue.

## Source category profiles

`Plant Creatures.PDF` explicitly defines Immobile, Creeping and Spreading movement/gameplay categories with encounter implications. CEW-06 records these as scoped source-category profiles rather than global creature types.

**Plant category profiles apply only where the source explicitly establishes that category.** A Plant-like name, plant biology, rooting ability or similar mechanic does not auto-bind an individual record to one of those categories. Category membership also creates neither identity nor distribution.

## Encounter-use boundary

**Encounter-use facets are reusable search and preparation hints, not Campaign placement state.** They can help an authorized GM discover or filter creatures by source-backed behavior, but PPIA-02 remains the authority for a particular Scene/Encounter participant role, quantity, wave, starting position/assumption, visibility, hidden tactics and runtime state.

A reusable `ambusher` facet does not place a creature in ambush. A `swarm_pressure` facet does not select quantity. A `sentinel_guardian` facet does not assign a faction or objective. A `terrain_controller` facet does not author a map or starting terrain.

No CEW-06 role or facet guarantees encounter difficulty, challenge rating, balance, lethality or outcome. There is no universal numeric CEW-06 encounter-role score.

Authorization filtering occurs before result counts, facets or derived search groupings are computed. GM diagnostics retain source provenance. Hidden creature facts do not leak through unauthorized facet counts.

## Habitat and distribution separation

`CEW-HAB-1.0` remains the habitat authority and `CEW-DIST-1.0` remains the canonical World/Reality/Setting/Place distribution authority.

A swamp predator is not present in every swamp. A herd animal is not globally distributed. A territorial creature does not acquire a geographic territory unless source-backed range/territory evidence establishes one. A migratory creature does not gain ecological-role facts merely from migration.

CEW-06 facts may be consumed alongside habitat and distribution during later GM discovery, but none of these axes silently writes the others.

## Coverage boundary

This tranche establishes the controlled vocabulary, non-inference contract, scoped source-category profiles and a representative direct-evidence packet. It does not bulk-populate every recovered statblock.

**CEW-07 owns the existing-creature coverage audit.** CEW-07 will measure what the recovered/canonical corpus already covers across CEW-01 through CEW-06 and will preserve missing facts as gaps rather than inventing them. CEW-08 separately owns creature-type coverage.

## Non-authorities

CEW-06 does not:

- mutate `Multiversal-app` schemas, creature UI, bestiary runtime, encounter runtime, search runtime or migrations;
- redefine creature identity or game type;
- create habitat facts or canonical distribution;
- create Campaign/Scene placement, quantity, wave, objective or starting state;
- create cognition, personhood, domestication, taming, ownership, bond, mount, pet/companion or familiar state;
- infer named prey/host/symbiont relationships from a general role;
- invent Earth trophic analogues for exotic source behavior;
- calculate a universal encounter-use or ecological numeric score;
- bulk-fill missing source facts from general knowledge.

## Handoff

The strict successor is **CEW-07 — Existing Creature Coverage Audit**. CEW-07 consumes the now-stable identity, taxonomy, classification, habitat, distribution and ecological-role contracts to measure existing coverage before later gap expansion.
