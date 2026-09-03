# ENV-01 — Environment Model & Composition Contract

**Work item:** ENV-01  
**Program:** ENV — Environment Preset & Overlay  
**Status:** completion candidate  
**Application implementation authority:** none  
**Owner and final authority:** John Brandon Turner

## 1. Purpose

ENV-01 establishes the canonical content/design model for reusable environments without changing `Multiversal-app` runtime behavior. It replaces the authoring assumption that every named environment must independently carry a comprehensive rules profile.

The canonical authoring model has four durable layers:

1. **Environment Archetype** — reusable environmental structure and baseline properties.
2. **Environment Preset** — a ready-to-use authored composition that parameterizes one or more archetypes and may nominate default overlays.
3. **Environment Overlay** — a reusable delta representing a condition or influence that changes an environment without becoming a new base environment identity.
4. **Local Environment Instance** — a setting/campaign/location-specific realization of a preset or archetype composition with local facts and selected overlays.

A fifth concept, **Resolved Environment**, is evaluation output only. It is a derived, read-only projection produced from the four durable layers plus current scene/runtime state. It is not a separately authored canonical environment identity and must never be written back into an archetype, preset, overlay, or local instance merely because it was evaluated.

## 2. Controlling source/framework boundary

The retained DB-004 exploration/environment framework permits environment records to define, when source-supported:

- terrain;
- climate;
- gravity;
- atmosphere;
- pressure;
- light;
- radiation;
- corruption or supernatural influence;
- hazards;
- movement constraints;
- visibility;
- resources;
- encounters;
- adaptations / environment-linked mechanical relationships.

The same framework requires environment effects to work through shared conditions/resources/modifiers and requires species, equipment, vehicles, powers, and temporary adaptations to be **evaluated against** the environment rather than duplicated into environment records.

ENV therefore owns environment-side composition facts and references. It does not acquire authority over Character, Species, Creature, Item, Vehicle, Ability, Condition, World/Reality, or encounter-runtime identity.

## 3. Durable object responsibilities

### 3.1 Environment Archetype

An archetype owns reusable baseline environmental structure that can occur across many worlds/settings.

It may own/source-reference:

- stable archetype identity and aliases;
- broad physical medium / spatial mode where useful;
- baseline terrain/substrate structure;
- baseline water/air/space context;
- baseline climate envelope where intrinsic rather than transient;
- baseline movement and navigation implications;
- baseline visibility/light relationships;
- baseline shelter/resource patterns;
- generic hazard families intrinsic to the archetype;
- generic encounter/ecology slots or tags, never world-specific creature distribution;
- composition hooks / parameter slots;
- a Habitat Signature envelope whose exact vocabulary is deferred to ENV-15;
- provenance for every source-derived baseline claim.

An archetype must not own:

- a named world's current geography;
- a particular settlement/site's local lore;
- a campaign's current weather;
- exact local creature populations;
- Character/species adaptations;
- runtime scene state;
- a full copied rules profile for each preset using it.

### 3.2 Environment Preset

A preset is the main GM-ready reusable environment selection. It is a composition recipe, not an independent replacement ruleset.

A preset may own/source-reference:

- stable preset identity and aliases;
- one **primary archetype**;
- zero or more **secondary archetype/component references** when a meaningful environment is compound (for example, a submerged ruin may combine underwater and ruin-like structure);
- archetype parameter values/defaults;
- reusable feature selections;
- default overlay references or recommended overlay options;
- preset-specific encounter/resource/hazard references that are genuinely more specific than the archetype;
- presentation summary / GM-facing descriptive guidance;
- source-profile linkage and transformation/provenance notes;
- setting scope only when the preset is intentionally setting-specific.

A preset must not copy all inherited archetype rules merely to appear complete. Preset completeness means the composition resolves to a complete usable environment, not that every field is physically duplicated in the preset record.

### 3.3 Environment Overlay

An overlay is a reusable environmental delta. Examples include Flooded, Blizzard, Low Gravity, Radiation, Magical Saturation, Reality Instability, or Heavy Rain.

An overlay may own/source-reference:

- stable overlay identity;
- overlay family/category;
- applicability predicates / compatibility hints;
- parameterization such as severity or intensity where supported;
- explicit environmental deltas to one or more property domains;
- hazard/effect/resource/encounter hooks caused by the overlay;
- Habitat Signature deltas;
- duration class or persistence metadata where the overlay itself establishes it;
- provenance.

An overlay does not become a new base environment identity merely because it substantially changes play. It must not silently rewrite the underlying archetype/preset/instance.

Exact stacking, incompatibility, conflict ordering, severity merging, and equivalent-effect deduplication are owned by **ENV-04**. ENV-01 establishes only that overlays are deltas and that unresolved conflicts fail visibly rather than being guessed.

### 3.4 Local Environment Instance

A local instance represents the actual environmental context of a particular world, region, settlement, location, route segment, campaign site, or scene-authoring location.

It may own/reference:

- stable local environment identity;
- World/Reality/Setting/Place/Region/Location references owned by their respective systems;
- chosen preset or direct archetype composition;
- local parameter adjustments;
- local persistent conditions/features;
- selected/default overlays;
- setting-specific geography/lore/context;
- local resources and encounter/discovery references;
- local creature/ecology distribution relationships when CEW/World authority later supplies them;
- local GM notes/visibility metadata where separately authorized;
- provenance and local-authoring history.

A local instance does not mutate its preset/archetypes/overlays. Local overrides belong only to the instance.

## 4. Environment property domains

The composition model must be capable of carrying or referencing the following domains without requiring every object/layer to populate every domain:

- `terrain_substrate`
- `climate_temperature`
- `water_hydrology`
- `atmosphere_air_quality`
- `gravity`
- `pressure`
- `light_visibility`
- `radiation`
- `supernatural_multiversal_influence`
- `hazards`
- `movement_navigation`
- `shelter_rest`
- `resources_foraging`
- `encounter_discovery_context`
- `habitat_signature`
- `environment_ability_relationships`
- `source_provenance`

These are composition domains, not a claim that every domain already has a finalized schema. ENV-03 through ENV-15 refine the reusable vocabularies and detailed mechanics.

## 5. Composition and evaluation order

Composition order is distinct from source/canonical authority order.

For a resolved environment, evaluate durable layers in this order:

1. **Archetype baseline(s)** — primary plus any explicitly declared secondary component archetypes.
2. **Preset parameterization/defaults** — where a preset is used.
3. **Local instance configuration** — local persistent facts and explicit local parameter adjustments.
4. **Active overlays** — reusable environmental deltas currently active for the evaluated context.
5. **Current runtime/scene state** — transient state is consumed for evaluation but remains owned by runtime systems and is not written back into ENV definitions.
6. **Participant evaluation** — species, creatures, characters, equipment, vehicles, powers, conditions, adaptations and similar owner-domain objects evaluate against the resolved environment without being copied into it.

Within-step conflicts are not resolved by arbitrary last-write-wins behavior. ENV-04 must define deterministic overlay stacking/conflict rules. Until then, an unresolved composition conflict is an explicit validation state.

A higher composition layer may specialize or locally override a lower layer only where the relevant field is declared overrideable. It may not override source/canonical authority simply because it appears later in composition order.

## 6. Field ownership / mutation rules

### Immutable inheritance

- Editing an archetype never implicitly rewrites historical source profiles.
- Editing a preset never mutates its referenced archetype.
- Editing an overlay never mutates compatible archetypes/presets/instances.
- Editing a local instance never mutates its preset, archetypes, or overlay definitions.
- Evaluating a resolved environment never mutates any durable definition.

### Explicit override only

A layer may alter an inherited property only through a typed override/delta relationship that records:

- target property/domain;
- operation intent (`set`, `add`, `remove`, `constrain`, `expand`, `multiply`, `replace_reference`, or later-governed equivalent);
- value/reference;
- provenance/authoring basis;
- conflict state if another active layer affects the same property incompatibly.

ENV-04 may refine the allowed operation vocabulary but must preserve the rule that overrides are explicit rather than implicit object replacement.

## 7. Provenance preservation contract

The existing forty promoted environment profiles and their source text/evidence remain preserved as source/provenance authority. Modularization does not rewrite those source artifacts.

For every source-backed archetype/preset/overlay/local fact derived from an existing profile, retain enough provenance to answer:

- which source file/profile/pages support this claim;
- whether the claim is exact source text, normalized identity, decomposed/derived structure, owner-authored addition, or later recommendation;
- what transformation occurred;
- whether the source contains unresolved conflicts or gaps.

A source profile may map to multiple modular records. Multiple source profiles may support one reusable archetype. Neither case permits silent source merging: relationships must remain attributable.

When later owner-approved authority supersedes an older source statement, the current composition may use the newer authority while preserving the historical conflicting source record.

## 8. Environment completeness contract

A usable environment does not require every durable layer to independently contain a full profile.

A **resolved environment is complete enough for GM use** when its composed layers provide, directly or by governed reference, all content classes required by the current environment completeness standard. ENV-02 owns repair of the existing forty and the exact current completeness checklist.

Therefore:

- an archetype can be intentionally abstract;
- a preset can rely on archetype inheritance;
- an overlay can contain only its deltas;
- a local instance can contain only local differences;
- completeness is evaluated on the resolved composition, not by demanding duplicate content in every layer.

## 9. Relationship boundaries

### Creature / ecology

ENV may expose Habitat Signatures and environment properties. CEW owns creature habitat preferences/tolerances/exclusions, distribution, ecological role, personhood, and creature discovery classification. ENV must not infer creature distribution solely from habitat compatibility.

### Ability / adaptation

Environment-linked Ability/Adaptation relationships remain references to their governed Ability/Species/Creature owners. Existing source-backed links are preserved. Missing links are not fabricated to make a preset look complete.

### World / Reality / Place

World/Reality/Setting/Place systems own geographic/cosmological identity and canon. A Local Environment Instance references those identities and expresses environmental state; it does not become the canonical place/world record.

### Encounter / runtime

ENV may provide encounter/discovery candidates, modifiers, and environment context. Encounter composition, hidden participants, initiative, current HP/resources, and other live state remain with their existing owners.

### Travel, vehicles, mounts

ENV provides environmental constraints/context. Vehicle, mount, route, logistics, supply, fatigue and movement owners evaluate against that context; ENV does not duplicate their ledgers or capabilities.

## 10. Preset authoring rules

A new ordinary environment should default to being authored as a **preset composed from existing archetypes and overlays** rather than as a new standalone comprehensive profile.

Create a new archetype only when the environment requires a reusable structural/environmental behavior that cannot be expressed cleanly through existing archetypes + parameters + overlays.

Create a new overlay when the distinguishing feature is a condition/influence that can meaningfully recur across multiple base environments.

Create a local instance when the distinction is primarily geographic, historical, setting-specific, campaign-specific, or currently active at one location.

Do not create a new preset merely for every possible overlay combination. Presets are curated useful defaults; overlays provide combinatorial variability.

## 11. Validation states

Composition validation must be able to distinguish at least:

- `valid`
- `incomplete_source`
- `unresolved_conflict`
- `missing_reference`
- `unsupported_overlay`
- `provenance_gap`
- `deferred_schema_detail`

A validation state must not silently become invented content. A GM may be shown incomplete/conflicted source state where role-safe; a content-authoring tool may propose repairs, but proposals are not canonical until governed acceptance.

## 12. ENV-01 completion invariants

ENV-01 is complete when all of the following are true:

- archetype, preset, overlay, local instance, and resolved-environment responsibilities are explicit;
- composition order and mutation isolation are explicit;
- source/canonical authority is not confused with composition precedence;
- existing source profiles are preserved rather than rewritten;
- the framework environment property domains are representable;
- participant adaptations/equipment/vehicles/powers remain external owner-domain evaluations;
- complex/compound presets may use one primary plus optional secondary archetype components;
- overlays are reusable deltas and not environment identity proliferation;
- unresolved conflicts fail visibly pending ENV-04 rather than using implicit last-write-wins;
- Habitat Signature has a stable envelope but exact vocabulary remains deferred to ENV-15;
- no `Multiversal-app` mutation, runtime schema change, migration, SCL behavior change, encounter-runtime change, or environment UI implementation is authorized.

## 13. Downstream handoff

ENV-02 consumes this model to repair the source-backed forty before decomposition.

ENV-03 consumes the model to determine the actual reusable archetype library.

ENV-04 owns detailed overlay family/stacking/conflict semantics.

ENV-05 converts the source-backed forty into modular presets only after ENV-02 through ENV-04 establish sufficient authority.

ENV-15 refines the Habitat Signature vocabulary without changing the four-layer object model.

ENV-16 exposes the composed environment to CEW/GM creature discovery without granting application implementation authority.
