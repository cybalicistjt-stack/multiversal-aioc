# CEW-04 — Habitat & Environment Crosswalk Contract

**Contract:** `CEW-HAB-1.0`  
**Work item:** CEW-04 — Habitat & Environment Crosswalk  
**Authority:** content/recovery/design/provenance only; no application implementation authority.

## Purpose

CEW-04 supplies the creature-side habitat/ecology seam that `ENV-HS-1.0` deliberately leaves to CEW. It consumes `CEW-ID-1.0`, `CEW-TAX-1.0`, `CEW-CLASS-1.0`, `ENV-HS-1.0`, and the read-only discovery seam `ENV-CD-1.0`.

Habitat suitability is not canonical distribution. CEW-04 records only source-supported creature ecology and occurrence qualifiers. CEW-05 owns canonical World, Reality and geographic distribution.

## Open-world ecology facts

The creature-side predicate classes are `requires`, `prefers`, `tolerates`, `excludes`, `depends_on`, and `unknown`.

Source silence remains unknown. Unknown is not incompatible, absent, unsuitable, nonnative, rare, or undiscoverable. An `excludes` fact requires explicit source/owner evidence of incompatibility; the absence of an exclusion does not prove compatibility.

Every asserted ecology fact retains predicate, ENV-HS-1.0 dimension or source context, value, scope and provenance. No numeric ecological-fit score is authorized.

## Source-section scope

A source-section habitat heading applies only to the statblocks authored under that heading. Section membership does not create a canonical creature identity, alias, duplicate binding, World range, native status, commonness or runtime placement.

The retained source families provide explicit section scopes including Swamp, Desert, Aquatic, Mountain and Cold Climate in `Beast Creatures 1.PDF`; Subterranean, Aerial, Urban and Grasslands in `Beasts 2.PDF`; Jungle/Forest and Aquatic in `Havalaea Creatures.PDF`; and Ice Shelf, Twilight Forest, Necrotic Wetlands, Skeinspire Mountains and Underground Vaults in `Skoaltarran Creatures.PDF`.

Where a source heading directly matches an ENV-HS-1.0 controlled value, CEW-04 may project that value. Examples include Aquatic → `habitat_medium:aquatic`, Subterranean → `habitat_medium:subterranean`, Urban → `settlement_intensity:urban`, Mountain → `elevation_band:montane`, and Cold Climate → `temperature_band:cold`.

Biome words that do not support an exact ENV-HS-1.0 dimension value remain source_context_ref facts rather than being decomposed by guesswork. Swamp, desert, grassland, jungle, forest edge, named Skoaltarran ecological zones, and similar labels therefore survive as source context unless the source itself supplies a more exact dimension fact.

## Direct creature evidence

Direct prose can add narrower facts than a section heading when the source actually states them. Examples retained in the CEW-04 evidence packet include:

- Jungle-Slip Beetle preference for warm metal and damp stone;
- Sunblight Sprite thriving in open grasslands and forest edges;
- Hurricane Manta storm-front use and explicit migration;
- Cave-Tusk Mammoth frostcave/tunnel habitat and explicit migratory behavior;
- Flicker Stag seasonal occurrence;
- Tundra Saberfang dusk/storm hunting conditions.

These facts remain scoped to their cited source records. They do not automatically transfer to creatures with similar names, types, powers or appearances.

## Non-inference boundaries

Game type, affinity, damage resistance, movement mode and creature name do not by themselves create habitat facts.

A creature that flies is not automatically classified as preferring aerial habitat. Aquatic movement does not by itself establish salinity, depth or geographic range. Fire resistance does not by itself establish hot-environment preference. Magical, elemental, divine, digital, fell or other type/affinity labels do not manufacture environment affinity.

`Creature types.PDF` explicitly supplies environmental adaptation for Fire-Type Animals and Cold-Type Animals. Those source modifier profiles may carry hot/cold tolerance, but CEW-04 does not automatically bind the modifier to any creature lacking explicit source authority.

Abilities that manipulate fog, light, temperature, wind, terrain or other environmental properties remain abilities unless the source separately states an ecology relationship. Environment similarity and ability similarity never create such a relationship.

## Migration, seasonality and activity

Migration and seasonality are occurrence qualifiers, not geographic range assertions. CEW-04 may preserve source-backed migration, seasonal occurrence and activity conditions for later `ENV-CD-1.0` discovery projection. CEW-05 separately determines where the creature canonically occurs.

A creature following another creature's migration is not automatically classified as having the same geographic distribution. Activity at dusk, in storms, during seasonal pivots or under other stated conditions is retained at that narrower scope.

## Overlay and special-context interaction

`special_environment_contexts` is the conservative bridge for source environmental concepts that are not safely decomposed into another Habitat Signature dimension. A context may later reference a governed `overlay_id` only where explicit source/owner authority establishes the creature relationship. CEW-04 does not infer overlay affinity from creature type, spell list, resistance, ability or environment resemblance.

## Matching seam

Resolved ENV facts compare against CEW habitat predicates dimension by dimension. Results remain `preferred`, `compatible`, `conditional`, `incompatible`, or `indeterminate` as defined by `ENV-HS-1.0`.

Hard incompatibility requires an explicit conflict. Material unknown/unresolved facts remain indeterminate. Preferred requires explicit preference support. Conditional fit requires an explicit dependency or scope condition. Explanations retain the creature and environment provenance chains.

No habitat result creates native status, canonical presence, rarity/frequency, campaign visibility, ownership, encounter placement, NPC state, mount/pet/familiar state, or application runtime state.

## Handoff

The strict successor is **CEW-05 — World, Reality & Geographic Distribution**.

CEW-05 owns canonical World, Reality and geographic distribution. It may consume CEW-04 ecology as a separate suitability fact but must source native range, introduced range, domesticated distribution, invasive range and generic/unrestricted distribution independently.
