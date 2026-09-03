# CEW-02 — Creature Type System Recovery & Taxonomy Audit

**Contract:** `CEW-TAX-1.0`  
**Work item:** CEW-02  
**State:** completion candidate  
**Owner:** John Brandon Turner  
**Application implementation authority:** none

## Result

CEW-02 recovers the creature-type vocabulary from the retained 23-document Creature corpus plus `Player Creatures.PDF` without forcing every source use of the word **type** into one taxonomy axis.

The source system is genuinely multidimensional and sometimes internally inconsistent. This tranche therefore records what each source actually means, preserves disagreements, and hands CEW-03 a clean semantic boundary instead of a flattened list.

## Recovered base-type families

The source corpus supports these game-facing base-type usages at different strengths:

- **Explicit or strongly defined families:** Aberration, Chaos, Construct, Demonic, Digital, Divine, Elemental, Fell, Fey, Toon, Undead.
- **Strong category/stat-block usage with incomplete normalization:** Dragon.
- **Repeated stat-block type usage without a dedicated recovered family contract:** Beast.
- **Orphan unresolved base-type usage:** Illusion, used in `Incorporeal Creatures.PDF` without a recovered Illusion family contract.

CEW-02 does **not** promote Plant, Incorporeal, Fire, Cold, Shadow, Mechanical, Zombie, Ghost, Vampire, Lycanthrope or Toon behavioral tags into additional global base types merely because a source uses the word `type`.

## Why `Creature types.PDF` is not a flat type list

The three-page `Creature types.PDF` is an adjustment-layer source:

| Source heading | CEW-02 role | Explicit base-type replacement |
| --- | --- | --- |
| Fire-Type Animals | affinity modifier | none |
| Cold-Type Animals | affinity modifier | none |
| Shadow-Type Animals | affinity modifier | none |
| Undead-Type Animals | modifier/template | `Undead` |
| Chaos-Type Animals | modifier/template | none stated |
| Mechanical-Type Animals | modifier/template | `Construct` |

The same source also contains **Follow The White Rabbit**, which is scenario material rather than creature taxonomy. A file or section heading is therefore never enough by itself to create a type.

## Nested systems recovered

### Aberration
Base type with source subdivisions: Causal, Geometric, Fractal, Conceptual, Synthetic, Cognitive and Temporal.

### Chaos
Base type plus ten explicitly named **body types**: Amorphic; Spined / Multilimbed; Crystalline or Faceted; Modular; Chimeric; Avian / Gliding / Levitating; Humanoid / Mock-Humanoid; Rooted / Burrowing; Serpentine / Tentacular; Bound / Encased.

### Construct
Base type with Golem, Soulcage, Enchanted Shell, Mechanical, Cybernetic and Toykin subtypes.

### Demonic
Base type with Devils (Infernal), Demons (Abyssal), Chaos Demons, Warpdemons, Eldritch Demons, Witchspawn, Bloodspawn, Industrial Demons, Theocratic Demons, Emotionals / Sinspawn and Toonspawn.

### Digital
Base family with Malware, Constructed AI, Emergent, Virtual Entity, Hardlight, Glitched and Patchling. Hardlight also participates in cross-tag semantics with Construct/Magitech in its own source and is not flattened.

### Divine
Base type with Deific, Demideific, Avataric, Empyrean, Sainted, Judicator, Divinetech and Seraphic subtypes. Divinetech's machine/construct language remains an overlap rather than a forced Construct replacement.

### Dragon
The source uses `Type: Dragon (...)` for Reptilian, Arcane-Born and Chromatic material and separately names Reptilian, Bird-Dragon/Aviform, Chromatic, Arcane-Born and Exo as Dragon categories/types. Its age ladder is intentionally partial: not every Dragon category follows the same stages.

### Elemental
Base type `Elemental`; Fire, Water, Air, Earth, Acid, Electricity and Metal are recovered as elemental affinities/types within the family rather than seven unrelated global base types.

### Fell
A distinct source creature family with method-of-misalignment categories: Contrarian, Corrupted, Aberrant Evolution, Unstable Construct, Echo and Parasymmetric.

### Fey
The source explicitly says **Fey is a creature type, not a species**. Spritekin, Beastkin, Plantkin, Humanoidkin and Mistkin/Wispkin are explicitly body-type categories even though later shorthand sometimes calls them Fey types.

### Toon
The source explicitly says **Toon is a creature type, not a species**. Its thirteen subtypes remain separate from optional Behavioral Tags.

### Undead
Base type with Soulless, Corpsebound, Revenant, Cosmic Undead, Cursed Undead and Environmental Undead subdivisions.

## Cross-cutting systems that must not become base types

- **Incorporeal:** source explicitly says it is *not a single category*. It combines with Undead, Aberration, Construct, Illusion and Elemental base-type usages. Spectral, Psionic, Aetherial, Mirage, Temporal, Dreamborne, Resonant and Voidbound are recovered as cross-cutting manifestation/origin subtypes.
- **Plant:** source calls Plant a **tag** and then categorizes Plant creatures by movement: Immobile, Creeping, Spreading and Mobile. The stat-block field `Type:` for those movement values is preserved as source usage but not interpreted as a global game type.
- **Zombies:** explicit **Zombie Conversion Template System**. Shambler, Runner, infection, elemental, supernatural, cybernetic and horror variants are cumulative templates.
- **Ghosts / Spirits:** explicit **Ghost & Spirit Template System**. Poltergeist, Wraith, Phantom Guardian, Specter, Revenant Spirit, Haunting Spirit and Ancestor Spirit remain templates.
- **Vampirism / Lycanthropy:** explicit curse/transformation/template systems, not universal base types.
- **Animal:** ecological/biological identity, not automatically Beast, nonsapient, tamable, pet, mount, familiar or non-NPC.

## Preserved source disagreements

CEW-02 intentionally does not resolve these by fiat:

1. **Vampire / Fell / Undead:** `The Fell.PDF` gives classic vampires as Fell examples; `Vampirism&Lycanthropy.PDF` treats vampirism as a curse/transformation; `Undead Creatures.PDF` defines Undead separately. No universal collapse is source-supported.
2. **Chaos Demons / Chaos:** Chaos Demons are a Demonic subtype while Chaos is also a standalone base type family.
3. **Hardlight:** Digital subtype/usage plus Construct/Magitech cross-tag semantics.
4. **Divinetech:** Divine subtype described as sacred machines/constructs; no authority says Divine and Construct are mutually exclusive.
5. **Beast / Animal / Beastfolk:** Beast is repeated stat-block type usage, while `Player Creatures.PDF` introduces Beast, Monstrous Beast, Beast (Sapient) and Beastfolk conversion labels. These do not erase animal ecology or establish personhood by taxonomy.
6. **Illusion:** appears as a base `Type:` value in Incorporeal stat blocks without a dedicated retained Illusion type contract.
7. **Dragon:** category terminology, type fields and age stages are uneven across the source family and remain partial.

## Havalaea boundary

`Player Creatures.PDF` contains a Havalaean Sapient Animal Template with conversion labels such as `Beast (Sapient)` and `Beastfolk`. CEW-02 records those labels but does not let them overwrite the program's stronger invariant:

- native-born Havalaean animals may remain biologically/ecologically animals;
- human-level intelligence/personhood is an independent dimension;
- NPC-system projection is permitted when appropriate;
- sapient autonomy/consent is preserved;
- mount/pet/familiar status is never inferred from type.

CEW-09 and CEW-10 own the dedicated cognition/personhood/Havalaea passes.

## Source-family audit

All 23 retained Creature PDFs have an explicit CEW-02 taxonomy role in `CEW-02_CREATURE_TYPE_RECOVERY_v1.0.0.json`. Setting collections (`Havalaea Creatures.PDF`, `Skoaltarran Creatures.PDF`), generic animal material and organizational headings remain scoped to their actual source role rather than becoming global taxonomic authority.

## Handoff to CEW-03

CEW-03 must build a multidimensional classification model that can simultaneously represent:

- base game type;
- nested subtype/category;
- biological/ecological class;
- body plan/manifestation;
- origin/affinity;
- template/modifier/transformation;
- condition/state;
- intelligence/personhood;
- setting/distribution scope;
- relationship/pathway eligibility.

It must preserve the unresolved queue in `CEW-TAX-1.0` rather than forcing a single-axis answer.
