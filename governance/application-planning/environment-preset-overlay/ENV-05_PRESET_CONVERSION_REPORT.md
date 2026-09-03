# ENV-05 — Existing 40 Preset Conversion Report

**Program:** ENV — Environment Preset & Overlay  
**Tranche:** ENV-05  
**Application implementation authority:** none  
**Owner and final authority:** John Brandon Turner

## Result

ENV-05 converts the completed forty promoted Environment Definitions into the first governed preset registry under the ENV-01 composition model.

The conversion does **not** replace or rewrite the source profiles. Each preset is a lightweight composition/selection identity that references:

- its immutable source `Environment_Definition_ID`;
- the completed ENV-02 effective profile content;
- its ENV-03 primary archetype;
- any ENV-03 secondary archetypes required for compound environments;
- source-derived distinguishing trait notes;
- broad preset context tags where useful;
- likely ENV-04 overlay-family destinations for later normalization.

The authoritative registry is `ENV-05_PRESET_REGISTRY_v1.0.0.csv` and its structural contract is `ENV-05_PRESET_MODEL_v1.0.0.json`.

## Coverage

- Source profiles converted: **40/40**
- Unique preset IDs: **40/40**
- Unique source Environment Definition references: **40/40**
- Compound presets retaining multiple archetypes: **12**
- Unmapped source profiles: **0**
- Source profiles mutated: **0**
- Source comprehensive prose duplicated into preset records: **0**
- Concrete ENV-11/12/13 overlay definitions authored: **0**

Every preset points back to `ENV-02_EFFECTIVE_COMPLETENESS_MATRIX_v1.0.0.csv`, where all forty effective profiles satisfy the current minimum GM-usable content contract.

## Conversion rules

### Preset identity is not a second rules document

The preset is the GM-ready selection/composition record. The comprehensive source-backed content remains referenced rather than copied. This prevents two independent versions of Swamps, At Sea, Cyberpunk City, and the other existing profiles from drifting apart.

### ENV-03 structure is preserved exactly

ENV-05 does not reinterpret the archetype extraction. Examples include:

- `Mangrove Swamp` = Wetland + Forest + Coastal Interface;
- `Sunken City` = Submerged + Urban + Built Complex;
- `Underwater Caves` = Submerged + Subterranean;
- `Flooded Suburbs` = Settlement + Wetland;
- `Underground Bunker Network` = Constructed Habitat + Subterranean + Industrial & Infrastructure;
- `Port City` = Urban + Coastal Interface.

### Existing traits stay source-visible until their owning tranche can normalize them

The ENV-03 `Deferred_Preset_Or_Overlay_Traits` are preserved as `Source_Trait_Notes`. Where a trait clearly points toward one of the twelve ENV-04 overlay families, ENV-05 records a `Deferred_Overlay_Family_Hint` only.

A family hint is **not** an overlay ID, effect, delta, intensity, stacking rule, or runtime instruction. Concrete overlay content remains owned by:

- ENV-11 — weather/climate/disaster overlay definitions;
- ENV-12 — planetary and physical-condition overlay definitions;
- ENV-13 — magical/supernatural/multiversal overlay definitions.

This allows a source-backed preset such as Sandy Desert to preserve `extreme heat` and `sandstorm` as part of its known profile today while reserving their reusable overlay implementation for the correct later tranches.

### Broad styles remain preset context

ENV-04 forbids accidental monolithic catch-all overlays. ENV-05 therefore keeps concepts such as:

- post-apocalyptic;
- cyberpunk;
- ruined-civilization context;
- populated/commercial/social configuration;
- rural/permanent or temporary/mobile settlement configuration;

as preset/source context rather than inventing universal environmental overlays for them.

Narrow reusable conditions inside those presets can later become governed overlays. For example, `Post-Apocalyptic Overgrown City` can eventually project overgrowth and structural decay into ecological/infrastructure overlays while retaining its post-apocalyptic identity/context as a preset concern.

## Deferred refinement is non-destructive

Some of the forty are intentionally retained as historical/source-backed presets even though later expansion tranches may split or refine them. Notable examples:

- `Arctic Tundra and Taiga` remains usable now but records ENV-09 as the future split/refinement owner.
- freshwater/marine chemistry distinctions point into ENV-06/07;
- reef structure points into ENV-07;
- broken highway/transport-corridor concerns point into ENV-10;
- weather, pressure, gravity, contamination, infrastructure failure, and supernatural traits point into ENV-11/12/13 as appropriate.

Later refinement must preserve the original preset/source identity and provenance even if newer curated presets supersede it for ordinary GM selection.

## Relationship to GM use

The current forty are now modeled as presets rather than forty isolated architecture islands. A future GM/environment creator can select a preset, inherit its archetype composition and source-backed profile content, then apply governed overlays and local-instance differences without cloning the complete profile.

ENV-05 does not implement that UI or runtime behavior. It establishes the content authority the later implementation may consume.

## Non-interference boundary

ENV-05 does not authorize changes to:

- `Multiversal-app` runtime schemas;
- SCL terrain/zone mechanics;
- environment database migrations;
- encounter runtime;
- creature distribution;
- NPC/mount/pet/familiar systems;
- environment-selection UI;
- Habitat Signature vocabulary.

The parallel software roadmap remains independently governed.
