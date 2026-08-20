# ICF-08 — Creature Part Effect Taxonomy & Affinity Grammar

## Purpose
ICF-08 defines a reusable, deterministic grammar for describing **broad tendencies** of governed creature-derived ingredients without inventing anatomy or turning descriptive tendencies into exact gameplay effects.

## Canonical inheritance chain
`part baseline → body-plan/creature-type profile → creature affinity/trait profile → explicit species/variant override → harvested-instance quality/condition`

The chain is additive and provenance-bearing. Later layers may add or suppress tendencies only when their evidence permits it. A species/variant override requires explicit evidence. Harvested-instance quality/condition may modulate confidence, potency and stability of an already-supported tendency but may never introduce a new semantic tendency.

## Part baselines
The baseline catalog includes blood/ichor; heart/core; neural/brain; eyes; liver/kidneys; lungs/gills; glands; fat/oil; bone/horn/antler; teeth/fangs/claws; hide/skin; scale/shell/chitin; feathers; muscle/meat; marrow; eggs/roe; silk/webbing; slime/mucus; magical organs/cores; and venom/poison sacs.

These are **tendencies**, not exact effects. For example, eyes tend toward perception/detection; this does not create a gaze attack, detection bonus or potion effect. A liver/kidney baseline may carry purification/toxin-interaction tendencies; it does not create detoxification or poison immunity.

## Body-plan/type profiles
Profiles are combinable and may include mammalian, avian, reptilian, amphibian, piscine/aquatic, arthropod, molluscan, plant, fungal, ooze, draconic, giant, elemental, undead, celestial/divine, infernal/fiendish, aberrant/psychic, spirit/ectoplasmic, synthetic/biotech, construct-with-biological-components, and extradimensional/anomalous.

A type profile does not prove that a creature possesses any particular part. The part must already be supported by authored creature evidence or a governed ICF-09 crosswalk.

## Trait/affinity profiles
Trait overlays represent authored creature facts such as fire-attuned, venomous, regenerative, psychic, planar or arcane. They may enrich an already-authorized part projection. They do not create the trait merely because a creature name or trope suggests it.

## Exact-effect boundary
ICF-08 never emits exact alchemical, culinary, magical, medical, combat or ritual outcomes. Exact effect status is always `unresolved-downstream-rule-content`.
- ICF-11 owns alchemical rule grammar.
- ICF-12 owns culinary/magical-culinary rule grammar.
- Recipe-specific exact ingredient requirements may reference an ingredient later, but the part grammar itself does not manufacture the recipe effect.

## Harvest and owner boundaries
ICF-07 owns harvest opportunity/resolution and must already have authorized the part/output. ICF-08 is a semantic projection over that governed output. D17 remains live Asset state; MIB-13 remains price/scarcity; MIB-11 remains world/reality context. ICF-09 owns the mass creature-catalog crosswalk.

## Fail-closed rules
The projection resolves to no tendencies when:
- creature evidence is absent;
- the part itself is not authored/governed for the creature;
- a required species/variant override has no evidence;
- a requested body/type or trait profile is unknown;
- a layer attempts to emit an `effect:` token;
- quality/condition attempts to introduce a new tendency.

No biology-only inference may create edibility, usefulness, legality, cultural acceptability, cannibalism rules or market value.

## Instance propagation
Quality and condition are deliberately narrow:
- quality can move potency/confidence bands of existing tendencies;
- condition can reduce stability/confidence and surface contamination risk;
- neither changes identity, anatomy, affinity semantics or exact effects.

## ICF-09 handoff
ICF-09 may bind real governed creatures to these part/type/trait profiles. Where source creature detail is insufficient, it records a gap rather than guessing. ICF-08 therefore supplies the grammar; ICF-09 supplies catalog-scale evidence-backed bindings.
