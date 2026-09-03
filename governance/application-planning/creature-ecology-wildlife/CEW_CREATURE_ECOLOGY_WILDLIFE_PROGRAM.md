# CEW — Creature Ecology & Wildlife Program

**Program ID:** CEW  
**Status:** in_progress_parallel_content_authoring  
**Current:** CEW-05 — World, Reality & Geographic Distribution (`selected_not_started`)  
**Completed through:** CEW-04  
**Owner and final authority:** John Brandon Turner  
**Application implementation authority:** none  
**Environment dependency:** consumes completed ENV composition, `ENV-HS-1.0` Habitat Signature and `ENV-CD-1.0` creature-discovery contracts.  
**Classification dependency:** consumes completed `CEW-ID-1.0`, `CEW-TAX-1.0`, `CEW-CLASS-1.0` and `CEW-HAB-1.0` contracts.  
**Parallel-track rule:** CEW may advance as governed content/recovery/design work while the application software roadmap continues. CEW must not mutate `Multiversal-app` runtime creature schemas, creature/NPC UI, encounter runtime, mount/familiar/pet runtime, SCL terrain behavior, or migrations until a separately governed application-integration tranche is authorized.

## Purpose

Recover, classify, audit and expand Multiversal creatures and wildlife so that:

- selecting an environment can expose appropriate creatures and wildlife to the GM;
- creature ecology matches ENV archetypes/presets/overlays through Habitat Signatures;
- canonical World/Reality distribution remains distinct from mere environmental survivability;
- creature-type coverage can be measured and extended where genuinely incomplete;
- ordinary animal/wildlife coverage is broad enough for the GM to populate environments without every encounter being a monster;
- source creature material is recovered before new content is invented;
- mount, pet/companion and familiar pathways reuse completed CCP systems rather than becoming new creature types;
- Havalaea native-born fauna descended from the Time of Troubles can preserve human-level intelligence/personhood and can project through the NPC system when appropriate.

## ENV handoff consumed

CEW begins from two completed environment-side contracts:

- `ENV-HS-1.0` — eighteen-dimension read-only Habitat Signature plus explainable ecological-fit states;
- `ENV-CD-1.0` — read-only GM creature-discovery projection contract that keeps ecological fit, canonical distribution, visibility, frequency, season/activity and overlay interactions independent.

Missing creature-side facts fail closed as unresolved. CEW is responsible for progressively supplying the source-backed creature identity, ecology, distribution and facets consumed by `ENV-CD-1.0`; it must not backfill them from environment similarity.

## CEW identity, taxonomy, classification and habitat handoff

The first four CEW tranches now provide the common semantic envelope consumed by later work:

- `CEW-ID-1.0` — conservative creature identity/source ledger; classification similarity never creates identity equivalence;
- `CEW-TAX-1.0` — recovered multidimensional type vocabulary and unresolved source-disagreement queue;
- `CEW-CLASS-1.0` — sixteen-axis open-world classification model keeping biology, game type, subtype, manifestation, affinity, template, state, cognition, personhood, ecology, distribution, ecological role, domestication/training, relationship pathways, NPC presentation and encounter/runtime role independent;
- `CEW-HAB-1.0` — source-backed creature habitat/ecology predicates against `ENV-HS-1.0`, including section-scoped habitat profiles and direct migration/season/activity evidence without creating canonical distribution.

`CEW-CLASS-1.0` is structural authority, not a bulk corpus-classification step. Source silence remains unknown. `CEW-HAB-1.0` similarly does not infer ecology from game type, affinity, movement, resistance, creature name or environmental abilities. CEW-05 and later tranches populate their owned axes only from source/owner-supported evidence.

## Existing authority consumed, not replaced

CEW must reuse and preserve:

- PPIA-02 Creature & NPC identity/presentation/placement/runtime distinctions;
- CCP-03 taming/recruitment/bond pathways;
- CCP-04 training/commands/tasks/behavior;
- CCP-05 care/health/recovery/aging/welfare;
- CCP-06 mounts, pack, service, work and travel integration;
- CCP-07 combat companions, familiars and supernatural bond seams;
- CCP-08 breeding/reproduction/lineage/inheritance;
- CCP-09 habitats/herds/stables/kennels/facility operations;
- CCP-10 creature ecology/social behavior/lifecycle/World integration;
- governed source/provenance rules and explicit unresolved-field handling.

CEW creates content authority/crosswalks and coverage decisions. It does not create competing creature, NPC, mount, pet, familiar, relationship or runtime systems.

## Required multidimensional creature classification

A creature record may independently express, where source-supported:

- biological/ecological identity;
- game creature type/category;
- body plan;
- origin/affinity/template/modifier;
- intelligence/cognition;
- personhood/sapience;
- habitat preferences/tolerances/exclusions;
- World/Reality/geographic distribution;
- ecological roles;
- domestication/training state or potential;
- mount/pack/work/service eligibility;
- pet/companion pathway eligibility;
- familiar/supernatural-bond pathway eligibility;
- NPC-capable presentation;
- encounter/runtime roles.

`Animal` is an ecological/biological classification and must not automatically imply `Beast`, nonsapience, pet status, ownership, tamability or lack of NPC presentation.

## Havalaea native-fauna authority

For playable-setting Havalaea, CEW must explicitly distinguish:

1. **Native-born Havalaean fauna** — descendants of animal lineages affected by/descending from the Time of Troubles. These may possess human-level intelligence/personhood where source/owner authority establishes it.
2. **Later imported fauna** — animals introduced after the relevant native lineage history. Importation does not automatically grant the native-born cognition/personhood property.

Native-born Havalaean animals with human-level intelligence/personhood must be eligible for **NPC-system projection** using the existing Creature/NPC experience. They remain biologically/ecologically animals if that is their source identity; NPC presentation does not convert them into humanoids or a different species category.

Sapient/person-level animals must preserve autonomy and consent boundaries. Physical ability to carry a rider, accept training or form a bond never implies ownership, tamability or involuntary mount/pet/familiar status.

## Mount, pet/companion and familiar cross-system rule

Mount, pet/companion and familiar are **relationship/pathway capabilities or roles**, not base creature types.

A creature may be eligible for zero, one or several pathways. Eligibility may depend on source-supported morphology, size, locomotion, capacity, environment, temperament, training, equipment compatibility, intelligence/personhood and consent. CEW must not invent universal carrying, speed, endurance, equipment or bonding formulas where completed CCP authority deliberately left those profile-scoped.

Required crosswalk states may include, where supported:

- trainable animal;
- domesticated/domesticable;
- pet/companion eligible;
- mount-capable;
- pack/work-capable;
- service-capable;
- familiar-compatible;
- summon/bond-compatible;
- sapient voluntary-partnership only;
- not normally bondable;
- unknown/not established.

## Tranches

1. **CEW-01 — Creature Source Census & Identity Ledger** — `completed_verified`  
   Inventory all retained creature material across dedicated Creature PDFs, Player Creatures, GPT/Evernote/source recovery, governed content objects and related setting sources. Reconcile exact duplicates/aliases only where supported. Produce canonical, recoverable, unresolved and rejected identity states.

2. **CEW-02 — Creature Type System Recovery & Taxonomy Audit** — `completed_verified`  
   Fully recover the existing creature-type material and usages. Distinguish base categories from body plans, origins, affinities, templates/modifiers, conditions and legacy organizational headings. Preserve source disagreements for owner resolution rather than flattening them.

3. **CEW-03 — Creature Classification Model** — `completed_verified`  
   Establish the multidimensional classification model required above. Prevent single-axis type taxonomies from erasing ecology, personhood, template or origin distinctions.

4. **CEW-04 — Habitat & Environment Crosswalk** — `completed_verified`  
   Apply ENV Habitat Signature vocabulary to recovered creatures where source evidence supports habitat/ecology. Record `requires`, `prefers`, `tolerates`, `excludes`, `depends_on`, `unknown`, migration/seasonality and special-context facts without fabricating missing ecology or canonical distribution.

5. **CEW-05 — World, Reality & Geographic Distribution** — `selected_not_started`  
   Separate environmental suitability from actual canonical distribution. Record native range, introduced range, domesticated distribution, invasive range and generic/unrestricted distribution as source-supported.

6. **CEW-06 — Ecological Role & Encounter-Use Classification**  
   Add GM-useful ecological/search facets such as predator, prey, grazer, browser, scavenger, decomposer, pollinator, parasite, herd, pack, solitary territorial, aerial hunter, aquatic grazer, burrower, domestic, nuisance and dangerous megafauna without redefining creature type.

7. **CEW-07 — Existing Creature Coverage Audit**  
   Measure the recovered creature corpus against ENV archetypes/presets and ecological scales/roles. Identify genuine habitat coverage holes across tiny/small/medium/large fauna, prey/herbivores, predators, scavengers, aerial/aquatic life, decomposers/invertebrates, dangerous wildlife and extraordinary creatures.

8. **CEW-08 — Creature-Type Coverage Audit**  
   Measure depth and overlap across the recovered creature-type system. Identify overrepresented, thin and missing categories and determine whether any new creature types are actually required rather than merely adding more creatures.

9. **CEW-09 — Intelligence, Personhood, Domestication & Partnership Classification**  
   Audit cognition/personhood, domestication, trainability, autonomy, consent and relationship potential across the corpus. Explicitly prevent `animal = beast = nonsapient = pet` collapse.

10. **CEW-10 — Havalaea Native Fauna & Time-of-Troubles Ecology**  
    Perform a dedicated Havalaea pass. Separate native-born Time-of-Troubles-descended fauna from later imports; recover native animal intelligence/personhood; classify habitats, distribution and ecological/social roles; and mark human-level native animals as NPC-capable using existing Creature/NPC presentation semantics. Preserve sapient autonomy and consent.

11. **CEW-11 — Mount, Pet, Familiar & Companion-System Crosswalk**  
    Bind source-supported creatures into existing CCP pathways: training/behavior, care/welfare, mounts/pack/work/travel, familiars/supernatural bonds, breeding, habitats/facilities and ecology. Mount/pet/familiar remain pathway/relationship roles, not creature types. Sapient creatures require voluntary-partnership handling.

12. **CEW-12 — Earthlike Animal & Wildlife Baseline**  
    Build a broad ordinary-wildlife library sufficient for GM population of mundane environments. Cover useful representatives across mammals, birds, reptiles, amphibians, fish, cartilaginous fish, insects, arachnids, crustaceans, mollusks and other ecologically important invertebrates without attempting an exhaustive Earth species encyclopedia.

13. **CEW-13 — Environment-Driven Wildlife Gap Expansion**  
    Use CEW-07 coverage results to fill weak ecological niches across rivers, wetlands, reefs, oceans, grasslands, alpine/polar environments, deserts, caves, settlements and other ENV families. Expansion is coverage-driven rather than quota-driven.

14. **CEW-14 — Multiversal & Alien Wildlife Expansion**  
    Recover native setting fauna first, then design additional non-sapient Multiversal/alien wildlife only where actual world/environment ecology remains thin. Add ecological niches, not arbitrary monster counts.

15. **CEW-15 — Monster, Extraordinary Creature & Creature-Type Gap Expansion**  
    Fill genuine supernatural/monster/type gaps revealed by CEW-08 while preserving existing source families such as Elementals, Incorporeal, Chaos, Zombies, Toon, Demonic, Fey, Divine, Digital, Fell, Undead, Dragons, Plant Creatures, Constructs, Ghosts, Aberrations and other recovered categories.

16. **CEW-16 — GM Environment Discovery, Encounter Ecology & Full Integration Handoff**  
    Produce the content/API handoff by which a composed ENV environment exposes likely ordinary wildlife, dangerous wildlife, extraordinary creatures, sapient inhabitants where appropriate, overlay-enabled/excluded creatures, rarity/frequency, ecological role, time/season/activity, World restrictions, NPC-capable sapient fauna, and mount/pet/familiar pathway facets. Distinguish `can occur here` from `normally occurs here`. Application implementation remains deferred to a separately governed software tranche.

## GM discovery projection requirements

Selecting a composed environment may eventually expose, subject to authorization and source coverage:

- native/common wildlife;
- possible/tolerated wildlife;
- migratory/seasonal wildlife;
- introduced/invasive wildlife;
- predators;
- prey/grazers/herd animals;
- small fauna/invertebrates;
- aerial/aquatic/subterranean fauna;
- dangerous wildlife;
- monsters/anomalies/extraordinary creatures;
- sapient native fauna;
- NPC-capable creatures;
- pet/companion candidates;
- mount/pack/work/service candidates;
- familiar-compatible creatures;
- creatures enabled/excluded by active overlays.

These facets do not bypass hidden-information, World-distribution, personhood, consent or campaign-visibility rules. `ENV-CD-1.0` is the controlling environment-side projection contract for this handoff.

## Completion invariants

- source creature recovery precedes broad new-creature invention;
- environmental suitability and canonical distribution remain separate;
- animal, beast, sapience, pet, mount, familiar and NPC presentation remain independent dimensions;
- Havalaea native-born Time-of-Troubles fauna and later imported fauna remain distinguishable;
- source/owner-supported human-level Havalaean native animals can use NPC-system presentation without losing animal ecological identity;
- mounts consume CCP-06 pathways rather than a new mount system;
- familiars consume CCP-07 rather than a new familiar system;
- pets/companions consume completed CCP bond/training/care authorities rather than a new pet system;
- sapient/person-level creatures preserve autonomy and explicit-consent boundaries;
- CEW does not create a duplicate canonical creature catalog outside governed creature identity;
- CEW consumes `ENV-HS-1.0`/`ENV-CD-1.0` without rewriting environment authority;
- no CEW tranche grants `Multiversal-app` implementation authority;
- ENV and CEW may run in parallel with software development only while respecting their read/content-authoring boundary.
