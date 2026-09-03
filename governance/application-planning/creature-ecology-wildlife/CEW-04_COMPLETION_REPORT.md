# CEW-04 — Completion Report

**Work item:** CEW-04 — Habitat & Environment Crosswalk  
**Contract:** `CEW-HAB-1.0`  
**Completion state:** `completed_verified` candidate pending exact-head repository validation and merge  
**Application implementation authority:** none

## Delivered

CEW-04 establishes the creature-side habitat/ecology crosswalk for the completed `ENV-HS-1.0` Habitat Signature.

The contract supports `requires`, `prefers`, `tolerates`, `excludes`, `depends_on`, and `unknown` facts with explicit provenance and source scope. It keeps source silence first-class as unknown, forbids numeric ecological-fit scoring, and preserves `ENV-HS-1.0` explainable matching semantics.

## Source-backed crosswalk

Sixteen explicit habitat-section profiles were recovered from retained creature sources:

- five from `Beast Creatures 1.PDF`;
- four from `Beasts 2.PDF`;
- two from `Havalaea Creatures.PDF`;
- five from `Skoaltarran Creatures.PDF`.

Each section profile applies only to the statblocks authored beneath its source heading. Section membership creates neither canonical creature identity nor geographic distribution.

Direct creature evidence additionally preserves source-supported facts for Jungle-Slip Beetle, Sunblight Sprite, Hurricane Manta, Cave-Tusk Mammoth, Flicker Stag and Tundra Saberfang. Fire-Type Animal and Cold-Type Animal environment adaptation is retained as source modifier ecology without automatic creature binding.

## Conservative projection rules

Exact ENV-HS values are used only where the source wording supports them directly. Broader biome labels remain `source_context_ref` facts instead of being decomposed into invented temperature, moisture, vegetation, salinity or other attributes.

Game type, affinity, damage resistance, movement mode, creature name and environment-manipulating abilities do not create habitat facts by themselves.

Migration, seasonal occurrence and activity conditions remain occurrence qualifiers. They do not create native range or canonical presence.

## Authority boundary

CEW-04 performs no creature identity promotion, duplicate/alias binding, World distribution authoring, encounter placement, relationship-state mutation, runtime/schema/UI/migration work, or `Multiversal-app` implementation.

Canonical World/Reality/geographic distribution remains intentionally unpopulated here.

## Strict successor

**CEW-05 — World, Reality & Geographic Distribution** is selected as `selected_not_started` by CEW-04 closeout. CEW-05 must keep ecological suitability separate while independently sourcing native, introduced, domesticated, invasive and generic/unrestricted distribution.
