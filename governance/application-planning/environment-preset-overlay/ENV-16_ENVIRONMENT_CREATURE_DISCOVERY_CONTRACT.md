# ENV-16 — Environment Creature-Discovery Contract & GM Preset Projection

**Program:** ENV — Environment Preset & Overlay  
**Tranche:** ENV-16 — Environment Creature-Discovery Contract & GM Preset Projection  
**Contract:** `ENV-CD-1.0`  
**Authority:** content/API contract only; no `Multiversal-app` implementation authority.

## Purpose

ENV-16 closes the environment side of creature discovery. It defines how an authorized GM-facing projection can take a resolved ENV environment and intersect it with creature facts owned elsewhere without turning environment similarity into creature canon.

The core rule is:

> **Environment selection can discover creature candidates; it cannot create creature identity, range, frequency, visibility, encounter placement or relationship state.**

ENV-16 therefore composes existing authorities instead of creating another creature, ecology, World or visibility ledger.

## Inputs and owners

The projection consumes three classes of input.

### 1. Resolved environment context — ENV-owned

The environment side supplies:

- a resolved environment/preset/local-instance reference;
- `ENV-HS-1.0` Habitat Signature;
- current scope;
- active overlay/context references;
- environment contribution/provenance trace;
- ENV-15 categorical ecological-fit result and per-dimension reasons when a CEW creature habitat profile is available.

All ordinary ENV composition rules remain intact. Active overlays resolve before ecological comparison. Unknown and unresolved Habitat Signature facts remain first-class.

### 2. Creature-side facts — CEW / existing creature authorities

A candidate creature may supply, when source-supported:

- governed creature identity;
- habitat requirements/preferences/tolerances/exclusions/dependencies;
- canonical World/Reality/geographic distribution;
- native/introduced/invasive/domesticated/resident/migratory/transient state;
- rarity/frequency;
- season/activity/time window;
- explicit overlay/context requirements, enabling conditions or exclusions;
- ecological roles and encounter-use facets;
- NPC-capable presentation;
- mount/pet/familiar/companion pathway facets;
- intelligence/personhood/consent facets.

ENV-16 reads these facts but never authors them. Missing facts stay unresolved for CEW/source recovery.

### 3. World/Campaign/visibility context — external authority

Existing World/Reality/Setting/Place and Campaign/GM/visibility owners retain:

- canonical placement/range context;
- local/campaign overrides or introductions where separately authoritative;
- campaign visibility and hidden-information state;
- GM-only/reveal/suppression controls.

The projection must not leak player-hidden or campaign-suppressed material merely because a creature matches the environment.

## Discovery is an intersection, not a score

There is no universal numeric discovery score and no hidden weighted priority. Discovery is an explainable intersection of explicit facts.

Each candidate is evaluated through these gates in order:

1. governed creature identity/authority;
2. campaign/GM visibility;
3. canonical distribution;
4. ENV-15 ecological fit;
5. explicit overlay/context interaction;
6. season/activity/current-scope condition;
7. GM-facing facet derivation;
8. stable grouping plus full reason/provenance trace.

Changing input order must not change the supported outcome. Contradictory authority is surfaced as a conflict rather than resolved by last-write-wins.

## Distribution remains stronger than habitat similarity

**Ecological suitability is not canonical distribution.** A compatible environment cannot manufacture a range assertion.

- Explicit distribution absence blocks a habitat-derived presence claim unless a separately authoritative campaign/local-placement fact explicitly establishes an introduction or placement.
- Unknown or not-established distribution does **not** become present by default. The result remains unresolved.
- Explicit native/resident/introduced/migratory/etc. distribution may continue through discovery.

A second rule protects source canon in the opposite direction: if controlling source authority explicitly places a creature in the current range while the current ecological comparison is `incompatible` or `indeterminate`, ENV-16 does **not** silently delete the creature. It returns a **canonical presence conflict**: the candidate remains discoverable to the authorized GM with a warning and both provenance chains. CEW/source reconciliation can then determine whether the habitat profile, local adaptation, source exception or environment data needs refinement.

This preserves the ENV-15 rule that canonical occurrence can exist in harsh or marginal conditions without allowing ENV to rewrite creature ecology.

## GM projection facets

The projection exposes independent, explainable facets rather than one monolithic category.

### `native_common`

Requires source-supported native/resident distribution plus common or equivalently explicit ordinary-occurrence authority. Habitat compatibility cannot create either half.

### `possible_tolerated`

A bounded GM-facing possibility for a creature with source-supported allowance/presence and compatible/preferred/conditional ecological fit where no stronger occurrence facet is established. It means **can occur here**, not **normally occurs here**.

### `migratory_seasonal`

Requires explicit migration, season or time-window authority. Baseline range and current activity remain separate.

### `introduced_invasive`

Requires source-supported introduced, invasive or domesticated distribution. Environmental similarity never invents an introduction history.

### `rare_exceptional`

Requires explicit rarity/exceptionality/unique occurrence authority. ENV-16 does not turn those labels into percentages or encounter rates.

### `overlay_enabled`

Requires an explicit creature-side/source predicate and the relevant active overlay/context. **Interaction is not causation**: an overlay can satisfy an existing creature requirement, but its presence does not invent creature affinity, adaptation, ability, summon, bond or range.

### `canonical_presence_conflict`

Used when explicit canonical/local presence survives but ecological/local-condition evidence is incompatible, indeterminate or contradictory. The GM sees the conflict and its sources rather than a fabricated resolution.

### `excluded_or_blocked`

An explicit controlling distribution, visibility, ecological, overlay or current-time condition blocks current discovery. Authorized GM diagnostics retain the blocked candidate and the exact gate reason instead of silently losing it.

### `unresolved`

Material authority is unknown, not established or contradictory. Unresolved candidates cannot be promoted into native/common/present claims.

## Current scope versus baseline range

Season, migration, activity and temporary overlays affect **current occurrence**, not canonical baseline range.

For example, a migratory animal can remain canonically distributed through a region while being inactive/absent in the current season. A severe active condition can temporarily suppress current occurrence without erasing the creature's baseline range. Conversely, a temporary overlay can enable a source-supported anomalous creature without making that creature a permanent native.

The projection therefore keeps baseline distribution and current-scope eligibility as separate facts.

## Visibility and hidden information

Visibility is an explicit gate, not a presentation afterthought.

- `gm_discoverable` may appear in normal authorized GM discovery.
- `gm_only` may appear only to an authorized GM/assistant surface.
- `hidden_until_revealed` remains suppressed unless the controlling campaign/GM authority explicitly allows the current view.
- `campaign_suppressed` does not appear in normal discovery.
- unknown/conflicting visibility is unresolved, not guessed open.

A later player-facing implementation must consume the same authority rather than treating GM discovery output as player-safe.

## Result contract

Every returned candidate carries at least:

- `creature_ref`;
- `outcome` (`discoverable`, `discoverable_with_warning`, `conditional`, `excluded`, or `unresolved`);
- zero or more explicit discovery facets;
- ENV-15 ecological-fit state;
- distribution state;
- visibility state;
- gate-by-gate reason trace;
- provenance/source references.

When available, the projection may additionally carry frequency, season/activity, active-overlay reasons, ecological/encounter roles, NPC capability and mount/pet/familiar/personhood facets. Those remain externally owned facts.

Blocked and unresolved candidates may be returned in **authorized GM diagnostic modes**. This is important for content work: a creature should not vanish from auditing simply because one gate blocks current play.

## GM query modes

`ENV-CD-1.0` defines three provider-neutral query modes:

1. **normal discovery** — discoverable and conditional candidates appropriate to the current authorized GM context;
2. **include blocked** — additionally expose excluded candidates with blocking reasons/provenance for GM/content diagnostics;
3. **include unresolved** — additionally expose unresolved candidates so CEW/source gaps remain visible instead of being guessed away.

The candidate universe comes from governed creature/CEW/distribution indexes or an explicit caller-provided candidate set. ENV-16 does **not** require a duplicate all-creatures database.

## Selection is not acquisition or placement

Selecting an environment or seeing a creature candidate does not:

- place an encounter;
- spawn a creature;
- add it to a campaign;
- tame or domesticate it;
- grant ownership;
- create a pet/companion/familiar bond;
- make it a mount;
- convert it into an NPC;
- alter personhood or consent;
- grant an ability/adaptation;
- reveal it to players.

Those systems remain owned by their existing authorities. ENV-16 only provides the discovery seam that a later authorized application integration can consume.

## CEW handoff

The contract is deliberately usable before CEW is fully populated: missing creature-side facts fail closed as `unresolved` instead of being invented.

CEW will progressively supply the data needed by this projection:

- **CEW-01** recovered creature identity/source ledger;
- **CEW-02/03** type and multidimensional classification;
- **CEW-04** Habitat Signature predicates;
- **CEW-05** World/Reality/geographic distribution;
- **CEW-06** ecological/encounter facets;
- **CEW-09/10/11** personhood, Havalaea NPC-capable fauna and partnership facets;
- later CEW expansion tranches for coverage gaps;
- **CEW-16** final content/API handoff populated with the completed creature corpus.

This means ENV can finish now without pre-empting CEW's source recovery or fabricating creature ecology.

## Non-authorities

ENV-16 does not authorize:

- `Multiversal-app` schema, UI, runtime, migration, terrain, SCL or encounter mutation;
- new creature identities;
- habitat-to-distribution inference;
- rarity percentages, weighted spawn rates or universal encounter tables;
- generic migration/activity formulas;
- automatic ability/adaptation grants;
- mount, pet, familiar or NPC eligibility inference;
- taming, ownership or consent inference;
- player-hidden information disclosure;
- automatic creature or encounter placement.

## Strict successor

ENV-16 completes the ENV content-authoring program. The strict successor for this parallel content sequence is:

**CEW-01 — Creature Source Census & Identity Ledger.**
