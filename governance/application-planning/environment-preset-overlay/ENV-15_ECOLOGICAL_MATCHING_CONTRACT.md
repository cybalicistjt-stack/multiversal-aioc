# ENV-15 — Habitat Signature & Ecological Matching Contract

**Program:** ENV — Environment Preset & Overlay  
**Tranche:** ENV-15 — Habitat Signature & Ecological Matching Contract  
**Authority:** environment-side content/design/provenance only; no application implementation authority.

## Purpose

ENV-15 defines the stable environment-side vocabulary that CEW can consume when classifying creature ecology. It does not create creature records, creature distribution, encounter frequency, NPC state, mount/pet/familiar state, or runtime behavior.

The contract is intentionally asymmetric: **ENV owns the environment-side signature; CEW owns creature-side ecology**. A resolved Habitat Signature describes the environmental conditions that exist. CEW separately describes what a creature requires, prefers, tolerates, excludes, or depends on.

## Habitat Signature identity

The governed signature version is `ENV-HS-1.0`. A Habitat Signature is a derived, read-only projection from the existing ENV composition stack. It is not a fifth durable authored environment object and must never write changes back into archetypes, presets, overlays, local instances, source profiles, creature records, or runtime-owned state.

Each material signature fact carries:

- dimension identity;
- value;
- state (`known`, `unknown`, `not_applicable`, or `unresolved_conflict`);
- scope;
- provenance/contribution trace.

**unknown is not a match and not an exclusion**. Source silence must remain unknown instead of becoming a default assumption. `not_applicable` is reserved for a dimension that genuinely does not apply in the scoped environment.

## Governed environment-side dimensions

`ENV-HS-1.0` defines eighteen comparison dimensions:

1. **Habitat medium** — terrestrial, aquatic, aerial, subterranean, artificial-interior, and exposed-space environmental spaces.
2. **Water salinity** — none, freshwater, brackish, saltwater, hypersaline, or mixed.
3. **Water permanence** — none, ephemeral, seasonal, permanent, or variable.
4. **Water flow** — still/slow/flowing/rapid/tidal/wave-exposed and related resolved regimes.
5. **Temperature band** — qualitative thermal regimes from extreme cold through extreme heat, with variable permitted.
6. **Moisture band** — hyperarid through submerged, with variable permitted.
7. **Vegetation density** — none through closed vegetation structure, with variable permitted.
8. **Substrates** — rock, sediment classes, soil/peat/organic litter, coral, ice/snow, artificial structure/metal, and mixed substrate where supported.
9. **Elevation band** — below-sea-level through extreme-altitude qualitative bands.
10. **Depth band** — surface, shallow, intermediate, deep, abyssal, or subsurface regimes.
11. **Light regime** — darkness, dim, normal, bright, glare, or variable.
12. **Atmosphere regime** — breathable, low-oxygen, toxic, corrosive, nonbreathable, vacuum, or variable.
13. **Pressure regime** — low, standard, high, extreme, or variable.
14. **Gravity regime** — zero, low, standard, high, or variable/directional.
15. **Shelter availability** — none/scarce/limited/moderate/abundant/structured/variable.
16. **Food/resource conditions** — environment-side production, prey-base, detritus, cultivated-food, waste-scavenging, stored-supply, scarcity, or other governed resource states. Creature diets and trophic identities remain CEW-owned.
17. **Settlement intensity** — wilderness through megacity/industrial conditions.
18. **Special environment contexts** — governed overlay/context references for magical, supernatural, multiversal, contamination, or comparable conditions. World/Reality/Place distribution does not belong in this dimension.

These are environment descriptors, not creature traits. For example, `aquatic` in a Habitat Signature means aquatic habitat exists; it does not state that any particular creature is aquatic.

## Composition and overlay resolution

The Habitat Signature consumes the already-governed ENV composition pipeline. Archetype baselines resolve first, followed by preset parameterization, local-instance configuration, active overlays, and current scoped scene state. The read-only Habitat Signature is then projected from that result.

**active overlays resolve before ecological comparison**. ENV-04 effect-key deduplication, explicit relation handling, visible conflicts, scope rules, and input-order independence remain controlling. A Habitat Signature never bypasses unresolved overlay conflicts or silently chooses a winner.

Overlay deltas may change habitat facts when the overlay owns the relevant environment domain. Examples include flood changing hydrology/moisture, vacuum changing atmosphere/pressure context, altered gravity changing gravity regime, or supernatural overlays contributing governed special-environment context. The signature retains the contributing overlay IDs and provenance.

A local environment instance may refine a signature without mutating its referenced source preset or archetype.

## Creature-side comparison seam

CEW may express creature-side ecological predicates against Habitat Signature dimensions using these semantic classes:

- `requires` — explicit condition necessary for ecological suitability;
- `prefers` — condition explicitly favorable to the creature;
- `tolerates` — condition the creature can use/endure without making it preferred;
- `excludes` — explicit condition incompatible with the creature;
- `depends_on` — explicit conditional dependency such as a resource, substrate, environmental context, season, or scoped condition;
- `unknown` — the creature-side source does not establish the relevant ecology.

ENV-15 defines the comparison seam but does not populate these creature predicates. That belongs to CEW-04 and later CEW work.

## Matching result states

A comparison may return only an explainable categorical state:

- **preferred** — explicit creature preference is satisfied and no explicit incompatibility or material unresolved fact blocks the result;
- **compatible** — explicit requirements/tolerances are satisfied sufficiently for ecological fit, without claiming preferred conditions;
- **conditional** — suitability depends on an explicitly identified condition, scope, resource, season, overlay, or other dependency;
- **incompatible** — an explicit required condition is contradicted or an explicit exclusion is present;
- **indeterminate** — material environment or creature ecology is unknown/unresolved, preventing a supported conclusion.

**hard incompatibility requires an explicit conflict**. Mere absence of a preferred condition does not prove incompatibility.

**preference may improve ordering without creating distribution authority**. Preferred habitat is still only ecological fit.

There is **no universal numeric ecological-fit score**. A percentage or hidden weighted score would imply unsupported precision and would make future source reconciliation harder. A later governed tranche could add numeric treatment only if source/owner authority establishes a legitimate scale.

## Suitability versus distribution

The central boundary is: **ecological suitability is not canonical distribution**.

A creature can be environmentally compatible with a place where it canonically does not live. Conversely, a creature can canonically occur in a harsh or marginal environment because source authority establishes that distribution.

**Habitat Signature never proves that a creature is native, common, present, or known to the GM**. Native range, introduced range, migration, domesticated distribution, invasive range, rarity/frequency, season/activity, campaign visibility and GM-only information remain outside ENV-15.

**World/Reality/Place authority remains external**. ENV-16 must intersect ecological fit with CEW distribution and World/Reality/Place constraints before projecting creatures to the GM. Those authorities may veto a merely suitable ecological match.

## Unknown and conflict handling

Unknown must remain contagious only when it is material to the conclusion:

- unknown required environmental fact -> `indeterminate`;
- unknown creature requirement/exclusion on a material dimension -> `indeterminate`;
- unknown irrelevant dimension does not automatically poison an otherwise supported comparison;
- explicit incompatibility may still establish `incompatible` even when unrelated dimensions are unknown;
- an ENV-04 unresolved environmental conflict remains unresolved in the signature and cannot be guessed away by CEW.

Source gaps remain visible for later recovery rather than being backfilled by general ecological assumptions.

## Non-authorities

ENV-15 does not:

- create or edit canonical creature identities;
- establish World/Reality/geographic distribution;
- decide native/common/rare frequency;
- author mount, pet, companion, familiar, NPC, personhood, tamability or ownership state;
- create new environment-to-ability links;
- infer ability/adaptation relationships from habitat similarity;
- invent universal exposure, pressure, gravity, temperature, radiation or survival formulas;
- mutate `Multiversal-app` schemas, runtime, UI, migrations, encounter systems, SCL terrain behavior, creature runtime, or CCP systems.

## ENV-16 handoff

ENV-16 may consume:

- resolved Habitat Signature;
- categorical ecological-fit state;
- per-dimension reasons;
- environment contribution trace.

ENV-16 must still intersect or attach external authority for canonical World/Reality distribution, rarity/frequency, season/activity, visibility/GM-only information and CEW creature facets. Ecological fit alone can never become a creature-discovery claim.
