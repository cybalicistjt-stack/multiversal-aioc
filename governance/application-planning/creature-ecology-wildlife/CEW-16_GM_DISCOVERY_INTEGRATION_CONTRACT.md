# CEW-16 — GM Environment Discovery, Encounter Ecology & Full Integration Handoff Contract

**Contract:** `CEW-GM-DISC-1.0`  
**Work item:** CEW-16 — GM Environment Discovery, Encounter Ecology & Full Integration Handoff  
**Controlling environment projection:** `ENV-CD-1.0`  
**Habitat vocabulary:** `ENV-HS-1.0`  
**Authority:** terminal CEW content/API handoff only; application implementation remains deferred.

## Purpose

CEW-16 closes the Creature Ecology & Wildlife program by binding completed CEW identity, taxonomy, classification, habitat, distribution, ecological-role, cognition/personhood, Havalaea-lineage, relationship-pathway, ordinary-wildlife, alien-wildlife and extraordinary-creature authorities into the already-completed `ENV-CD-1.0` read-only GM discovery projection.

This contract does not create a second creature database, a placement engine, a spawn system, a relationship engine, or a runtime implementation. It defines what an eventual separately governed application integration may read and how it must preserve the completed authority boundaries.

## The central semantic distinction

**`can occur here` is not `normally occurs here`.**

`can occur here` is a bounded discovery statement. It may be asserted only when controlling identity/visibility/distribution authority permits the candidate and its ecology is compatible or conditionally compatible. It does not mean native, resident, common, frequent, or ordinarily encountered.

`normally occurs here` requires independent occurrence authority: canonical distribution/presence plus source/governance-supported frequency, resident/native, season, or comparable ordinary-occurrence evidence. Habitat compatibility alone cannot establish normal occurrence.

Therefore:

- ecological suitability never creates canonical distribution;
- canonical presence is stronger than environmental similarity;
- unknown distribution remains unresolved rather than becoming possible-by-default;
- ordinary/common/native status is not inferred from compatibility;
- current activity/season is separate from baseline distribution;
- canonical presence with incompatible/indeterminate ecology remains visible as a warning conflict rather than being silently deleted.

## Required gate order

Every candidate is processed in this exact order inherited from `ENV-CD-1.0`:

1. `identity_and_authority_gate`
2. `campaign_visibility_gate`
3. `canonical_distribution_gate`
4. `ecological_fit_gate`
5. `overlay_condition_gate`
6. `season_activity_gate`
7. `projection_facet_derivation`
8. `stable_grouping_and_trace`

No later facet may bypass an earlier gate. In particular, habitat fit, type, danger, NPC capability, or relationship-pathway eligibility may never bypass visibility or canonical distribution.

Supported query modes remain:

- `normal_discovery` — normal GM-facing allowed results;
- `include_blocked` — authorized diagnostics may expose blocked/excluded candidates and the blocking authority;
- `include_unresolved` — authorized diagnostics may expose material unknowns rather than guessing them away.

## Candidate universe and identity boundary

The GM discovery seam may consume multiple governed candidate partitions, but it does not merge them into a duplicate canonical catalog.

Current governed partitions include:

- 27 canonical Creature Definitions;
- 100 CEW-12 noncanonical ordinary Earthlike baseline profiles;
- 29 CEW-13 noncanonical environment-gap profiles;
- 10 CEW-14 noncanonical nonsapient alien-wildlife profiles;
- 6 CEW-15 noncanonical extraordinary-creature profiles;
- 46 Havalaea setting-associated source profiles carried through source recovery;
- 39 Skoaltarran recoverable source records.

The noncanonical CEW-12/13/14/15 libraries have no prepopulated canonical distribution. Their default presence state is therefore `unresolved` until a separate distribution authority exists. Likewise, source-collection membership never creates a stable-ID binding, native status, or canonical range.

## GM discovery facets

The companion `CEW-16_DISCOVERY_FACET_BINDING_MATRIX_v1.0.0.json` binds each GM-facing facet to its controlling authority. It includes:

- native/common;
- possible/tolerated;
- migratory/seasonal;
- introduced/invasive;
- predator and prey/grazer/herd search groupings;
- small fauna/invertebrates;
- aerial/aquatic/subterranean fauna;
- dangerous wildlife;
- extraordinary creatures;
- sapient native fauna;
- NPC-capable creatures;
- pet/companion candidates;
- mount/pack/work/service candidates;
- familiar-compatible creatures;
- overlay-enabled candidates;
- canonical-presence conflicts;
- excluded/blocked candidates;
- unresolved candidates.

Facets are nonexclusive and nonnumeric. Their order is not hidden precedence, and facet count is not a ranking score.

## Encounter ecology is discovery/preparation, not placement

`CEW-ECO-1.0` supplies trophic, social, ecosystem-interaction, and encounter-use facets for filtering and GM preparation. Those facets do not create:

- encounter participants;
- participant quantities;
- waves;
- starting positions;
- difficulty guarantees;
- campaign placement;
- hidden tactics;
- live scene state.

Existing Campaign/Scene/Encounter authority remains controlling for placement and runtime participation. Environment selection never spawns or inserts a creature.

## Overlay handling

An active ENV overlay or local resolved condition may satisfy an explicitly authored creature-side predicate and yield `overlay_enabled` or a conditional outcome. This does not infer that a creature is fire-aligned, cold-aligned, magical, vacuum-native, radioactive, aquatic, or otherwise associated merely because the environment has a matching condition.

Overlays do not create canonical distribution or identity.

## Cognition, personhood, Havalaea and NPC projection

`CEW-COG-PART-1.0` and `CEW-HAV-LIN-1.0` remain authoritative.

- intelligence, language, personhood, sapience, animal ecology and NPC presentation remain independent facts;
- native-born Havalaean Time-of-Troubles-descended fauna remain distinguishable from later imported fauna;
- a human-level Havalaean animal retains animal ecological identity;
- source/owner-supported human-level native animals may be NPC-capable without becoming humanoids;
- NPC projection creates no ownership, tamability, obedience, or loss of autonomy;
- material lineage/personhood unknowns stay unknown.

A `sapient_native_fauna` facet requires both independent sapience/personhood authority and independent native-lineage/distribution authority. Neither is inferred from setting namespace, source collection, ecology, or the other fact.

## Mount, pet, companion and familiar facets

`CEW-REL-PATH-1.0` and the completed CCP authorities control pathway eligibility.

A discovery facet such as `pet_companion_candidate`, `mount_pack_work_service_candidate`, or `familiar_compatible` means only that a source/governance-supported pathway may be available for later governed relationship handling. It creates no:

- ownership;
- bond;
- taming;
- training state;
- obedience;
- equipment;
- recruitment;
- placement;
- consent.

Sapient/person-level creatures require voluntary consent for partnership roles. Physical ability, size, intelligence, magical type, NPC projection, or habitat fit never overrides that rule.

## Required result trace

Every projected result must retain enough structured evidence to explain why it appeared or was blocked. Required fields are:

- creature/candidate reference;
- outcome;
- facets;
- ecological fit;
- distribution state;
- visibility state;
- gate trace;
- provenance.

Optional result details may include frequency, season/activity, active-overlay reasons, ecological roles, encounter facets, NPC capability, relationship-pathway eligibility, consent/personhood facets, `can occur here` state, and `normally occurs here` state.

Material conflicts may not be silently dropped. `canonical_presence_conflict` is a first-class warning state.

## Software integration handoff

The CEW content program is complete when this contract is `completed_verified`.

The application handoff state is **`ready_for_separately_governed_software_selection`**. That state means the content/API contracts are mature enough to be consumed by a future selected application tranche. It is not permission to implement them now.

Any future software integration must consume `ENV-HS-1.0`, `ENV-CD-1.0`, and `CEW-GM-DISC-1.0` without reinterpreting the core invariants. In particular it must not infer:

- distribution from habitat similarity;
- encounter placement from discovery;
- relationship state from eligibility;
- personhood from cognition/type;
- player visibility from GM discovery.

## Mutation boundary

CEW-16 authorizes no `Multiversal-app` runtime, schema, UI, migration, canonical Creature Definition, canonical distribution, live relationship, encounter-placement, campaign-placement, terrain/SCL, mount, pet, familiar, or NPC-runtime mutation.

Application implementation remains deferred to a separately selected and governed software tranche.
