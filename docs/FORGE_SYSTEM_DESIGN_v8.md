# Multiversal Content Forge — System-Grounded Design Contract v8

## Core rule

Every Forge begins with a guided type-selection experience based on the governed Multiversal content model. The selected path determines interview questions, validation, preview, references, generated object metadata, and Pack List readiness.

The author thinks in creative terms. The Forge translates those choices into governed records.

## Required distinctions

The UI and generated objects must preserve these distinctions:

- Species Definition: reusable biological, physical, adaptation, choice, and compatibility foundation.
- Creature Definition: reusable creature identity with taxonomy, scale, biology or embodiment, movement, senses, defenses, resources, actions, traits, reactions, behavior, habitats, variants, and provenance.
- Archetype: reusable role package built on a Species or Creature Definition.
- Template: reusable governed layer applied to compatible Definitions.
- Variant: identified alteration of a base Definition.
- Form / Transformation: alternate governed state that preserves identity.
- Placement: a Definition or Variant located in a world, scene, or campaign context.
- Live Instance: mutable campaign state; it must not overwrite the source Definition.
- Projection / Stat Block: derived play view; it is not authoritative content.

## Forge experience

1. Choose the record layer.
2. Choose the primary taxonomy family.
3. Choose the closest subtype.
4. Connect a Species or base Creature Definition where applicable.
5. Add secondary taxonomy tags only when needed.
6. Choose an encounter or scenario presentation separately from taxonomy.
7. Complete a natural-language guided interview.
8. Connect canonical Actions, Effects, Conditions, Resources, Abilities, Items, Environments, and other records.
9. Preview the readable entry and the structured object.
10. Validate provenance, dependencies, layer compatibility, and Pack List readiness.

## Creature taxonomy principles

Taxonomy says what a creature is. Encounter role says how it is presented. Origin, habitat, intelligence, faction, social role, and threat are separate dimensions.

Primary families:

- Biological life
- Constructed and synthetic
- Spiritual and post-mortal
- Elemental and environmental
- Extradimensional and anomalous
- Collectives and swarms
- Play-role foundations

The taxonomy is extensible. Setting-specific types may be added without replacing the governed distinctions above.

## Canonical references

Mechanical content should reference shared records instead of reproducing rules in prose. Creature objects should expose reference collections for:

- Actions
- Effects
- Conditions
- Resources
- Abilities
- Items and loadouts
- Environments and adaptations
- Species or base Creature Definitions
- Forms, Templates, and Variants

Free text remains appropriate for appearance, ecology, motivation, behavior guidance, lore, and provenance, but must not substitute for required canonical references.

## Validation expectations

The Forge should warn when:

- a Variant, Template, Form, or Archetype has no identified base Definition;
- taxonomy and encounter role are conflated;
- a campaign Instance is being exported as a canonical Definition;
- mechanical prose lacks corresponding Action, Effect, Condition, Resource, or Ability references;
- dependencies are unresolved;
- transformations do not preserve base identity;
- provenance is missing or uncertain;
- an object is presented as balanced without approved harness evidence.

Warnings should explain the problem in author language and offer a direct correction path.

## Mobile interaction rules

- One major decision per screen.
- Always-visible Back and Close controls.
- Save-and-exit at every stage.
- No hidden required fields.
- Suggested choices include a short explanation of when to use them.
- “Decide later” is available where the system permits it.
- Advanced details remain collapsed until relevant.
- The author can change any earlier classification without losing later answers.

## AI assistance

AI assistance is optional and advisory. It must receive the selected record layer, taxonomy, subtype, base references, interview answers, controlled vocabularies, and expected output fields. AI output remains a suggestion until the author accepts it and validation passes.

## Pack List output

Every completed Forge workflow produces:

1. a readable authoring entry;
2. a structured game object;
3. validation and provenance metadata;
4. optional staging in one or more Pack Lists.

A final `.pack` compiler must preserve object IDs, record layers, dependencies, provenance, validation status, and manifest counts.