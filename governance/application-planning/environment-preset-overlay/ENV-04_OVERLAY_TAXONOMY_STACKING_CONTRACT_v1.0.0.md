# ENV-04 — Overlay Taxonomy & Stacking Rules

**Program:** ENV — Environment Preset & Overlay  
**Tranche:** ENV-04  
**Application implementation authority:** none  
**Owner and final authority:** John Brandon Turner

## Purpose

ENV-04 defines how reusable environmental overlays are classified, combined, deduplicated, rejected, transformed, and traced. It resolves the conflict/stacking detail explicitly deferred by ENV-01 and provides the contract ENV-05 needs before converting the existing forty source-backed environments into modular presets.

This tranche defines **composition semantics**, not the complete authored overlay content library. Weather/disaster content is principally authored in ENV-11, planetary/physical-condition content in ENV-12, and magical/supernatural/Multiversal content in ENV-13.

No `Multiversal-app`, SCL, runtime schema, migration, encounter runtime, creature distribution, or environment UI implementation is authorized by ENV-04.

## 1. Overlay identity

An Environment Overlay is a reusable environmental **delta**, not a replacement environment identity.

Every governed overlay must identify:

- stable overlay identity and name;
- overlay family;
- environment property domains it may affect;
- applicability predicates;
- typed deltas;
- effect keys and stack modes for effects that participate in stacking;
- provenance.

An overlay may additionally identify intensity, duration class, exclusive groups, authored relations to other overlays, Habitat Signature deltas, hazard hooks, encounter hooks, resource hooks, and GM-facing presentation guidance.

## 2. Overlay families

ENV-04 establishes twelve broad families. These are organizational and validation categories, **not implicit precedence levels**.

1. **Weather & Precipitation** — rain, snow, fog, storms, wind and similar meteorological conditions.
2. **Temperature & Thermal** — unusual or temporary heat/cold conditions.
3. **Hydrology & Water State** — flood, drought, altered water levels, current/surge, saturation and ice/water-state changes.
4. **Atmosphere & Air Quality** — breathability, gas composition, smoke, particulates, toxic/corrosive air and atmospheric contamination.
5. **Light & Visibility** — darkness, glare, obscuration, haze and unusual illumination.
6. **Gravity & Inertial Conditions** — low/high/zero/variable gravity and related environmental regimes.
7. **Pressure** — atmospheric, hydrostatic or other environmental pressure deviations.
8. **Radiation & Contamination** — radiation, chemical/biological contamination, fallout and pollution.
9. **Geologic & Physical Disaster** — volcanic activity, earthquakes, landslides, avalanches, unstable ground, ashfall and comparable physical events.
10. **Ecological & Landscape State** — overgrowth, blight, die-off, wildfire state, invasive growth, severe erosion and similar landscape conditions.
11. **Infrastructure & Operational State** — abandoned, derelict, damaged, blackout, powered-down, failing-life-support and other constructed-environment operational states.
12. **Magical, Supernatural & Multiversal Influence** — magical saturation/dead zones, reality instability, dimensional bleed, psychic influence, corruption, temporal disturbance, Chaos/Foam influence, Dream influence and similar nonordinary conditions.

A family answers “what broad environmental dimension is this?” It does **not** answer “which overlay wins?”

## 3. Intensity and state

Not every overlay needs intensity. A binary or categorical state such as `abandoned` may not benefit from a numeric severity.

Where intensity is useful, the shared qualitative order is:

`trace < mild < moderate < severe < extreme`

An overlay may also carry a source-supported numeric value or a domain-specific scale. Numeric values from different scales are not comparable unless the overlay contract explicitly declares them comparable.

A stronger intensity does not automatically supersede a weaker activation merely because it has a higher band. Supersession must be declared for that phenomenon and overlapping scope.

## 4. Scope

Overlay definitions are reusable. Overlay **activations** may apply to an entire environment, local instance, route, zone, volume, or a runtime-owned scene scope.

Two activations that would conflict in the same scope may coexist when their scopes do not materially overlap. ENV stores the reusable definition and composition semantics; live scene ownership remains outside ENV.

## 5. Typed deltas

ENV-01 established explicit override/delta semantics. ENV-04 retains and refines the allowed operation vocabulary:

- `set`
- `add`
- `remove`
- `constrain`
- `expand`
- `multiply`
- `replace_reference`
- `merge_unique`

Each stack-relevant delta identifies:

- target domain/property;
- stable `effect_key`;
- operation;
- value/reference;
- stack mode;
- provenance.

The allowed stack modes are:

- `nonstacking`
- `additive`
- `multiplicative`
- `strongest`
- `weakest`
- `replace`
- `merge_unique`

A delta is never silently made additive merely because two overlays affect the same thing.

## 6. Overlay relations

Explicit overlay-to-overlay relations may use:

- `requires`
- `excludes`
- `supersedes`
- `transforms_with`
- `amplifies`
- `dampens`

Relations must be authored and attributable. The engine/content resolver must not infer them from names alone.

Examples:

- Heavy Rain does not automatically extinguish Wildfire unless a `dampens` or `transforms_with` relation is authored.
- Magical Saturation does not automatically amplify Reality Instability unless ENV-13 later establishes that interaction.
- Zero Gravity may supersede Low Gravity in an explicitly governed shared gravity-regime exclusive group; absent that rule, the conflict stays visible.

## 7. Deterministic stacking pipeline

Overlay composition follows this order:

1. **Validate references and applicability.** Missing references remain `missing_reference`; overlays that cannot apply to the resolved base become `unsupported_overlay`.
2. **Normalize identity and scope.** Resolve aliases to stable IDs and compare conflicts only where activation scopes overlap.
3. **Resolve repeated activation of the same overlay identity.** Merge only using that overlay's declared intensity/duration/parameter policy. Otherwise mark redundant or unresolved.
4. **Resolve exclusive groups and authored relation edges.** Apply `requires`, `excludes`, `supersedes`, and `transforms_with` rules.
5. **Compile typed deltas.** Preserve contribution-level provenance.
6. **Deduplicate equivalent effects by `effect_key`.** Apply the declared stack mode; do not double-apply a movement, visibility, hazard, resource, or other effect simply because multiple overlays mention it.
7. **Apply authored cross-overlay interactions.** `amplifies`, `dampens`, and transformation rules apply only where explicitly defined.
8. **Validate remaining domain conflicts.** Incompatible `set`, `replace`, or constraint operations without a merge/relation rule become `unresolved_conflict`.
9. **Produce a resolved overlay projection.** Record applied, merged, redundant, superseded, transformed, blocked and unresolved contributions. This projection is derived and read-only.

The result must be independent of input ordering.

## 8. Duplicate-effect suppression

The same gameplay/environmental consequence must not be applied multiple times simply because several environment layers describe it.

Every stack-participating effect uses a stable `effect_key`. When two contributions share the key:

- `nonstacking` applies the effect once;
- `additive` combines only when the effect explicitly allows addition;
- `multiplicative` combines only when explicitly allowed;
- `strongest`/`weakest` require a declared comparable scale;
- `replace` requires an authored precedence/relation rule;
- `merge_unique` unions unique references/tags without duplication.

Suppressing one duplicate contribution never suppresses unrelated effects from the same overlay.

If two nonstacking contributions differ and cannot be compared under a declared rule, the state is `unresolved_conflict`, not an arbitrary winner.

## 9. Compatibility and exclusion

Compatibility is explicit and property-aware:

- family membership alone never implies compatibility or conflict;
- same-family overlays may coexist;
- different-family overlays may conflict;
- exclusive groups represent genuinely mutually exclusive regimes, not whole-family exclusion;
- an overlay can be valid but redundant against an archetype/preset baseline;
- an overlay requiring a medium or structural condition absent from the resolved environment is unsupported unless an authored transformation establishes that condition.

Supported resolution states are:

- `compatible`
- `merged`
- `redundant`
- `superseded`
- `transformed`
- `blocked`
- `unresolved_conflict`
- `unsupported_overlay`

These supplement ENV-01's wider environment validation states rather than replacing them.

## 10. Examples

### Heavy Rain + Flooded

Both may remain active. If both contribute the same footing/visibility penalty, the shared `effect_key` prevents it from applying twice. Heavy Rain does not automatically increase flood depth unless an authored amplification rule says it does.

### Radiation + Toxic Atmosphere

They can coexist because they affect distinct contamination/atmosphere properties. Any shared health/hazard contribution still follows effect-key deduplication.

### Low Gravity + Zero Gravity

If both target the same scope and gravity regime, an exclusive/supersession rule is required. If Zero Gravity is defined to supersede Low Gravity, the lower-gravity activation remains in the trace as superseded. Otherwise the composition is unresolved.

### Wildfire + Heavy Rain

Both remain active unless a governed relation defines dampening/extinguishing/transformation. Name-based common-sense inference is not authoritative enough to mutate canonical composition.

### Abandoned + Blackout

Both infrastructure-state overlays may coexist. Power-loss effects deduplicate, while abandonment keeps its separate maintenance, access, salvage and encounter implications.

### Magical Saturation + Reality Instability

They are compatible by default in ENV-04. ENV-13 may later establish setting/source-backed interactions.

## 11. What is not automatically an overlay

The modular system must not recreate large vague environment categories as overlays.

- **Post-apocalyptic** is normally a preset/local-state composition of narrower conditions—such as dereliction, contamination, flooding, overgrowth and other source-supported circumstances—not one universal overlay.
- **Cyberpunk** is principally a technology/social/presentation style or preset/local context, not automatically an environmental condition.
- **Ruined** may use infrastructure/structural-state overlays where reusable, while unique ruin identity and history remain preset/local-instance content.
- Stable **climate bands** belong in archetype/preset parameterization when intrinsic. Exceptional/transient departures belong in overlays.

## 12. Provenance and auditability

Overlay resolution must preserve a contribution trace sufficient to answer:

- which overlay activation contributed each resulting property/effect;
- which source or owner authority supported that overlay or relation;
- whether a contribution applied, merged, was deduplicated, was superseded, transformed, blocked, or remained unresolved;
- which active overlays were evaluated but had no effect because they were redundant or unsupported.

Composition precedence never overwrites canonical/source authority.

## 13. Downstream contract

ENV-05 may now convert the existing forty profiles into presets because archetype inheritance and overlay conflict semantics are both established.

ENV-11 through ENV-13 populate the substantive overlay libraries using this contract rather than inventing their own stacking behavior.

ENV-15 may add Habitat Signature delta vocabulary without changing ENV-04 stacking semantics.

ENV-16 and CEW may consume resolved overlay effects for creature-discovery matching, but creature identity/distribution remains CEW-owned.

## Completion invariants

ENV-04 is complete when:

- overlay families are stable and broad enough for the planned environment program;
- overlay family is explicitly separated from precedence;
- intensity is optional and cross-scale comparison is bounded;
- overlay relations are explicit and attributable;
- a deterministic, input-order-independent stacking pipeline exists;
- duplicate environmental effects cannot silently double-apply;
- incompatible overlay writes fail visibly when no governed resolution exists;
- source profiles and durable environment layers remain immutable;
- post-apocalyptic/cyberpunk and similar broad categories are not allowed to become accidental monolithic overlay identities;
- later ENV overlay-content tranches consume this contract;
- no application/runtime implementation authority is introduced.
