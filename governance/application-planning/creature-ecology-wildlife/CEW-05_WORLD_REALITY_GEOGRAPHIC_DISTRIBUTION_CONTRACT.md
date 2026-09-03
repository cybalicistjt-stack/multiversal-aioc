# CEW-05 — World, Reality & Geographic Distribution Contract

**Contract:** `CEW-DIST-1.0`  
**Work item:** CEW-05 — World, Reality & Geographic Distribution  
**Authority:** content/recovery/design/provenance only; no application implementation authority.

## Purpose

CEW-05 establishes the creature-side canonical distribution envelope used by later ecology, encounter and GM-discovery work. It consumes `CEW-ID-1.0`, `CEW-CLASS-1.0`, `CEW-HAB-1.0`, PPIA-12 World & Setting authority, and `ENV-CD-1.0`.

The central rule is strict: **Habitat suitability is not canonical distribution.** A creature may be ecologically compatible with an environment in a World, Reality, Setting, Region or Location where it does not canonically occur. Conversely, canonical source-backed presence is not erased merely because later ecological evidence looks surprising.

## Typed distribution scope

Distribution facts use the smallest supported typed scope and keep that scope through projection:

1. `reality_or_cosmology` — branch, plane, layer, reality or comparable cosmological container;
2. `world` — a named world-scale container where the source establishes one;
3. `setting` — a reusable PPIA-12 setting definition or source-backed setting label;
4. `region` — a named region, territory, zone, biome-region, settlement region or comparable geographic subdivision;
5. `location_or_site` — a named site, district, station, landmark, route endpoint, cave system or other source-backed place.

Typed hierarchy supports nonplanetary settings. CEW-05 does not infer that a Setting is a planet, that a Reality contains a named World, or that similarly named places are nested unless source or governed authoring authority says so.

## Distribution relation states

A scoped distribution assertion may describe `present`, `native`, `introduced`, `domesticated`, `invasive`, `explicitly_absent`, `unknown`, or `unresolved_conflict`.

Every material assertion retains state and provenance. Source silence remains `unknown`; it never becomes absence. `native`, `introduced`, `domesticated`, `invasive`, and `explicitly_absent` require explicit source or governed owner authority. Conflicts remain visible; there is no last-write-wins reconciliation.

## Setting membership versus range status

PPIA-12 distinguishes world-local content extensions from the owning Creature Definition domain. **World-local content membership is not native-range proof.**

A setting-scoped creature Definition may establish setting membership while native, introduced, domesticated and invasive status remain unknown. The current canonical `mv.setting.havalaea.creature.*` Definitions therefore support an asserted `present` membership relation to Havalaea, but their native status is not promoted by namespace alone.

Likewise, a dedicated source collection such as `Havalaea Creatures.PDF` or `Skoaltarran Creatures.PDF` is setting-association evidence. It does not by itself merge source-only identities, prove every listed creature is native, or create a complete geographic range.

Campaign placement and live runtime location remain separate from reusable distribution truth. A GM placing a creature in a Scene does not rewrite the species/creature Definition's canonical range.

## Habitat and distribution boundary

`CEW-HAB-1.0` owns creature-side ecological predicates. CEW-05 does not convert those predicates into geography.

- a swamp preference does not prove presence in every swamp;
- a cold tolerance does not prove polar or mountain range;
- an aquatic requirement does not prove oceanic or river distribution;
- environment overlays do not create range;
- taxonomy, affinity, movement, damage resistance or creature name do not create geography;
- a habitat section heading does not widen a creature beyond its sourced distribution scope.

**Explicit source-backed absence blocks environment-derived presence.** `ENV-CD-1.0` must treat such absence as a hard distribution gate while retaining the independent habitat-fit explanation.

## Migration, seasonality and current occurrence

Migration and seasonality remain occurrence qualifiers. **Migration or seasonality without named geographic endpoints does not create a range map.**

`Hurricane Manta`, `Cave-Tusk Mammoth`, and `Flicker Stag` retain the temporal facts recovered by CEW-04, but CEW-05 records their geographic endpoints as unknown because the cited evidence does not establish those endpoints.

An occurrence qualifier may refine a separately sourced range fact. It cannot supply the missing World, Reality, Setting, Region or Location itself.

## Generic and Earthlike material

**Generic creature sources remain geographically unknown unless the source or governed authority establishes scope.** Generic Beast, Fey, Dragon, Undead or other creature collections do not automatically become Earth, Havalaea, Skoaltarran, or multiversal-everywhere distributions.

**CEW-05 does not infer Earth distribution from mundane or Earthlike resemblance.** A wolf-like, horse-like, insect-like, fish-like or otherwise familiar creature remains geographically unknown unless source/owner authority establishes Earth or another named range.

This preserves the later CEW-12 Earthlike-animal baseline as a deliberate content tranche rather than a hidden assumption introduced here.

## Havalaea boundary

Five current canonical creature Definitions are explicitly setting-scoped to Havalaea and may therefore be projected as Havalaea-present world-local content:

- Rootstalker;
- Hisscap Frog;
- Mossling Glider;
- Sapcrawl Varnet;
- Jungle-Slip Beetle.

CEW-05 does **not** classify those five as native-born Time-of-Troubles lineages. That dedicated lineage/native-fauna determination remains CEW-10-owned. Until explicit source/owner evidence establishes native, imported, introduced, domesticated or invasive status, those dimensions remain `unknown`.

Human-level cognition, personhood, NPC projection, mount/pet/familiar eligibility and relationship state remain outside this tranche.

## Discovery projection

For environment-driven GM creature discovery, gate order remains source-first:

1. valid creature identity or source candidate authority;
2. permission/visibility filtering;
3. typed World/Reality/Setting/Place scope;
4. explicit distribution fact, absence or unresolved conflict;
5. temporal occurrence qualifier if independently established;
6. habitat suitability considered separately;
7. stable result grouping with both distribution and habitat provenance.

Environment similarity never creates range. Setting membership never creates native status. Source conflict is surfaced, not silently normalized.

## Non-authorities

CEW-05 does not:

- mutate `Multiversal-app` creature schemas, UI, runtime, migrations, maps or encounter systems;
- create a second World/Setting hierarchy;
- create canonical identity from source-collection membership;
- infer geographic range from habitat fit, taxonomy, powers, abilities, names, genre expectations or visual resemblance;
- infer native/introduced/domesticated/invasive status from setting namespace alone;
- create ownership, taming, bond, mount, pet, familiar or NPC state;
- turn Campaign/Scene placement into reusable canonical distribution;
- universalize setting-local creatures or mechanics;
- resolve source conflicts without stronger authority.

## Handoff

The strict successor is **CEW-06 — Ecological Role & Encounter-Use Classification**. CEW-06 owns ecological role and encounter-use classification. This includes ecological/trophic/resource/social roles and encounter-use/search facets while preserving both `CEW-HAB-1.0` habitat facts and `CEW-DIST-1.0` distribution facts as independent axes.