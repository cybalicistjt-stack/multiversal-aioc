# Multiversal Expert Authoring Suite v10

## Designer-first contract

Every authoring tool must let the designer think in the language of the game while the software maintains the structured record. The interface must not expose raw schemas as the primary workflow.

Each builder produces four synchronized artifacts:

1. a guided designer draft;
2. a reader-facing manual entry;
3. a governed Multiversal game object;
4. an expert review receipt and optional Pack List placement.

## Shared rules

- Choose the correct record layer and subtype before authoring details.
- Preserve Definition, Variant, Placement, Live Instance, Snapshot, and Projection boundaries.
- Use stable IDs and explicit dependencies.
- Reference shared Actions, Effects, Conditions, Resources, abilities, items, environments, and rules profiles rather than copying mechanics into prose.
- Keep presentation text separate from runtime mechanics.
- Draft and incomplete content may be saved, but blocking validation prevents ready/approved status.
- Every final preview offers Manual Entry, Game Object, and Expert Review views.
- Saving to a Pack List must never bypass validation or provenance warnings.

## Domain responsibilities

### Abilities and trees
Single abilities are governed capability records. Trees are stable-node progression graphs with explicit tiers, prerequisites, exclusions, grants, costs, and respec policy.

### Creatures, NPCs, and species
Preserve species, creature type, archetype, template, variant, form, and individual-instance distinctions. Stat blocks are projections. Campaign state does not overwrite source definitions.

### Items, vehicles, mecha, and ships
Begin from canonical operational families and subtypes. Separate frame/platform identity, installed systems, granted abilities, resources, ownership, maintenance, and mutable condition.

### Worlds and timelines
World definitions reference independently reusable locations, factions, environments, species, rules, and events. Timeline events explicitly record causes, participants, visibility, consequences, and continuity.

### Adventures
Objectives, scenes, branches, failure states, secrets, relationship changes, rewards, and world-state changes must be explicit and referenceable.

### Dialogue and story flow
Presentation text remains separate from entry conditions, checks, flags, transitions, relationship effects, and visibility. Story flows are testable graphs, not prose outlines.

### Relationships
Reusable relationship definitions and mutable campaign relationship state are separate records. Directionality, visibility, triggers, permissions, complications, and history are explicit.

## Review roles

The built-in consultant review checks:

- identity and stable-ID quality;
- required domain fields;
- layer correctness;
- dependency closure;
- provenance and canon status;
- manual readability;
- runtime object readiness;
- accidental duplication of shared mechanics;
- missing transitions, base definitions, or progression policies;
- campaign state overwriting canonical content.

This contract applies to all future authoring tools and expansions.