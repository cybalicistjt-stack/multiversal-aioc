# CEW-03 — Creature Classification Contract

**Contract:** `CEW-CLASS-1.0`  
**Work item:** CEW-03 — Creature Classification Model  
**Authority:** content/recovery/design/provenance only; no application implementation authority.

## Purpose

CEW-03 establishes the common multidimensional classification envelope used by later Creature Ecology & Wildlife tranches. It consumes `CEW-ID-1.0`, `CEW-TAX-1.0`, the PPIA-02 Creature/NPC identity and presentation boundaries, completed CCP relationship authority, and the completed ENV habitat/discovery contracts.

The model is deliberately **not** a replacement Creature Definition schema and is not a one-axis taxonomy. A reusable Definition may carry source-backed facts on several independent axes at once, with each asserted fact retaining its source/authority, scope and provenance.

## Core rule: independent axes

No axis is allowed to infer another axis merely from category similarity.

Classification never changes reusable Definition identity. Definition identity, presentation profile, variant/template relationship, Campaign/Scene placement and live runtime instance remain the distinguishable PPIA-02 layers. A classification assertion can describe a governed Definition, but it cannot silently create a new Definition, merge identities, place a creature in a Campaign, or create runtime state.

The governed axes are:

1. biological / ecological identity;
2. game creature type;
3. nested subtype / category;
4. body plan / manifestation;
5. origin / affinity;
6. template / modifier / transformation;
7. condition / state;
8. intelligence / cognition;
9. personhood / sapience;
10. habitat / ecology;
11. World / Reality / geographic distribution;
12. ecological role;
13. domestication / training;
14. relationship / pathway eligibility;
15. NPC-capable presentation;
16. encounter / runtime role.

The list defines semantic slots, not mandatory values. A creature may have no established value on many axes.

## Open-world fact semantics

Every material classification assertion is provenance-bearing. The permitted fact states are `asserted`, `explicitly_absent`, `unknown`, `unresolved_conflict`, and `not_applicable`.

Unknown is not false, absent, incompatible, nonsapient, nonnative, or ineligible. Source silence remains `unknown`; it does not become a negative fact merely because a field is empty. `explicitly_absent` requires authority that actually establishes absence. `unresolved_conflict` preserves competing source claims or classifications until governed resolution.

There is no last-write-wins conflict rule. A later file, prettier label, more familiar genre convention, or stronger-looking category name cannot silently erase a source disagreement.

## Identity and taxonomy boundaries

`CEW-ID-1.0` remains the creature identity authority. CEW-03 does not create duplicate/alias bindings, does not promote source-only records into canonical Creature Definitions, and does not turn classification similarity into identity equivalence.

`CEW-TAX-1.0` remains the recovered type-system authority. Game type, subtype, body plan, affinity, modifier and biological identity stay separate:

- `Animal` does not imply `Beast`, nonsapience, tamability, pet status or non-NPC status.
- `Plant` biological/ecological identity does not turn Plant movement categories into global base types.
- `Incorporeal` manifestation does not become one universal base type.
- Fire/Cold/Shadow affinities do not replace base type unless a source explicitly says they do.
- Undead-Type Animal and Mechanical-Type Animal may replace the game type only because their source explicitly states those type changes.
- Zombie, Ghost, Vampirism and Lycanthropy transformation/template systems remain relationship layers to a base creature rather than automatic global base types.

A template or modifier never replaces a base game type without an explicit source rule authorizing the replacement.

## Personhood, cognition and NPC presentation

Intelligence/cognition and personhood/sapience are independent axes. Neither follows from biological class, game type, body plan, social presentation or relationship eligibility.

NPC presentation is a projection choice, not a biological or personhood reclassification. PPIA-02 can present a source-supported intelligent creature as a Sentient Creature / NPC Hybrid while preserving its animal, dragon, construct, or other source-backed identities.

For Havalaea, a native-born animal descended from Time-of-Troubles lineages may remain biologically/ecologically an animal while independently carrying human-level cognition/personhood where source/owner authority establishes it. NPC-system projection does not convert that animal into a humanoid, does not create ownership, and does not remove autonomy.

CEW-09 owns the dedicated cognition/personhood/domestication pass and CEW-10 owns the dedicated Havalaea pass. CEW-03 supplies the slots and boundaries only.

## Relationship and partnership boundary

Mount, pet/companion and familiar remain relationship/pathway roles, not creature types. Pack/work/service and supernatural-bond compatibility are the same kind of pathway facts.

Eligibility is not relationship state. A creature marked as physically mount-capable or familiar-compatible is not therefore owned, bonded, tamed, recruited, equipped, assigned, or currently acting in that role. Existing CCP authority continues to own bond, training, care, work/travel, familiar, reproduction, habitat/facility, ecology/lifecycle, autonomy and consent semantics.

Sapient/person-level creatures require voluntary-partnership handling where the relationship would otherwise imply control or ownership.

CEW-11 owns the corpus-wide relationship/pathway crosswalk. CEW-03 does not pre-classify creatures into those pathways.

## Habitat and distribution boundary

Habitat suitability is not canonical distribution. `ENV-HS-1.0` supplies environment-side descriptors; CEW-04 will populate source-backed creature-side `requires`, `prefers`, `tolerates`, `excludes`, `depends_on`, and `unknown` predicates.

CEW-05 separately owns World/Reality/geographic distribution such as native, introduced, domesticated, invasive or migratory range. A creature can be ecologically compatible with an environment where it canonically does not occur, and canonical source-backed occurrence is not erased merely because later ecological evidence looks surprising.

No Habitat Signature, environment preset, overlay, environmental similarity or ecological-fit category is allowed to manufacture creature range, frequency, native status, ability, adaptation or hidden-information visibility.

## Later-population ownership

CEW-03 does not bulk-populate later-tranche classifications. The model establishes structure now while leaving future source-backed population to the strict owners:

- CEW-04 — habitat/ecology predicates;
- CEW-05 — World/Reality/geographic distribution;
- CEW-06 — ecological and encounter-search roles;
- CEW-09 — cognition, personhood, domestication, training and partnership semantics;
- CEW-10 — Havalaea native-fauna distinctions and personhood/NPC projection;
- CEW-11 — mount/pet/familiar/companion pathway crosswalk.

CEW-12 and later expansion tranches may add source-backed or newly governed creature content only inside these established boundaries.

## Preserved CEW-02 unresolved queue

The classification model carries, but does not resolve by fiat, these `CEW-TAX-1.0` disagreements:

- `CEW02-CONFLICT-005` — Vampire / Fell / Undead;
- `CEW02-CONFLICT-006` — Chaos Demons / Chaos / Demonic;
- `CEW02-CONFLICT-007` — Hardlight / Digital / Construct / Magitech;
- `CEW02-CONFLICT-008` — Divinetech / Divine / Construct;
- `CEW02-CONFLICT-009` — Beast / Animal / Beastfolk;
- `CEW02-CONFLICT-010` — orphan Illusion type usage;
- `CEW02-CONFLICT-011` — Dragon category/type/stage normalization.

Each remains `unresolved_conflict` until stronger source/owner authority supports a governed resolution.

## Permission and runtime boundary

Classification truth and what a viewer is authorized to see are separate concerns. PPIA-02 permission-safe projection still occurs before search suggestions, counts, facets, relationships or derived disclosures. Hidden creature existence or hidden classification facts must not leak through filtering, counts or discovery.

Encounter role may be source-backed or placement-scoped, but Campaign placement identity and live HP/resources/conditions/location/initiative/control state remain outside reusable Definition classification and stay with their existing runtime authorities.

## Non-authorities

CEW-03 does not:

- mutate `Multiversal-app` creature schemas, UI, runtime, migrations or encounter systems;
- create a second creature identity catalog;
- mass-promote recovered source candidates;
- infer one axis from another;
- invent ecology, distribution, personhood, domestication or partnership facts from genre expectations;
- create ownership, bond, taming, mount, pet, familiar or NPC state;
- replace unresolved source conflict with a convenient normalization;
- authorize release, deployment or application integration.

## Handoff

The strict successor is **CEW-04 — Habitat & Environment Crosswalk**. CEW-04 consumes `CEW-CLASS-1.0` and `ENV-HS-1.0` to populate only source-supported creature-side habitat/ecology predicates while keeping distribution and all other classification axes independent.
