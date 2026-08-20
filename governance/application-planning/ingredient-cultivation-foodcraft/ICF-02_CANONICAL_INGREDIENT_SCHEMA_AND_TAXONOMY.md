# ICF-02 — Canonical Ingredient Schema & Taxonomy

**Program:** ICF — Ingredient, Cultivation & Foodcraft Foundation  
**Work item:** ICF-02  
**Status:** implementation candidate  
**Normative machine contracts:** `ICF-02_CANONICAL_INGREDIENT_SCHEMA.json`, `ICF-02_TAXONOMY_AND_SOURCE_MAPPINGS.json`  
**Conformance examples:** `ICF-02_CONFORMANCE_EXAMPLES.json`

## 1. Purpose

ICF-02 resolves the open normalization decisions identified by ICF-01 and defines one provider-neutral ingredient definition model that later ICF tranches can populate. The schema is reusable across mundane crops, forage, animal/aquatic products, magical ingredients, creature-derived ingredients, processed preparations, cooking, magical cooking, alchemy, medicine, ritual, crafting and trade.

The schema is **definition authority only**. It does not create a second live-state ledger. Current ownership, custody, quantity, quality and condition remain owner-domain Asset state; current market price and market scarcity remain MIB-13 economy state; crafting mutations remain MIB-12/D17 owner-domain operations; creature biology and authored harvest references remain canonical creature authority.

## 2. Identity and stable IDs

### 2.1 Stable ID families

- Primary reusable feedstocks use `ingredient:<slug>`.
- Reusable processed ingredient-like intermediates reserve `preparation:<slug>` for ICF-10.
- Finished meals, potions, medicines, equipment and other finished products remain the owning item/content kind unless explicitly authored as a reusable preparation input.
- A purely structural crafting material with no ICF ingredient role may remain `material:<slug>`. A biological or magical substance used across culinary, alchemical, medicine, ritual or crafting profiles should remain one ingredient identity rather than being duplicated by subsystem.

Stable IDs are manually governed identities. They are immutable after active publication. They are **not** automatically generated, merged or renamed from display-name spelling.

### 2.2 Alias discovery is not identity authority

Alias matching uses deterministic normalization only to produce review candidates:

1. Unicode NFKC normalization.
2. Lowercase comparison.
3. Punctuation/separator normalization.
4. Whitespace collapse.
5. A token-preserving `lexicalKey`.
6. A separator-free `compactedKey`.

A matching key, singular/plural similarity, or spacing difference never merges records by itself. Identity merges require explicit reconciliation and provenance.

ICF-01's two direct alias candidates are resolved for identity only:

- `Fire Blossom` / `Fireblossom` → `ingredient:fire-blossom`, preferred display `Fire Blossom`.
- `Phoenix Feather` / `Phoenix Feathers` → `ingredient:phoenix-feather`, preferred singular display `Phoenix Feather`.

Those identity resolutions do **not** silently resolve rarity, price, creature crosswalk, cultivation or effect properties.

## 3. Rarity is not classification, availability or market scarcity

ICF-01 proved that the legacy sources overloaded top-level words such as `Legendary`, `Exotic` and `Supernatural`. ICF-02 separates four concepts:

1. **Canonical rarity** — authored baseline scarcity in a defined scope.
2. **Nature/origin classification** — what kind of thing it is or where it comes from.
3. **Acquisition availability** — how accessible it is through cultivation, foraging, husbandry, harvesting, mining, processing or trade.
4. **Market scarcity** — current market-state scarcity owned by MIB-13.

### 3.1 Canonical rarity bands

The canonical rarity ladder is:

`common → uncommon → rare → exceptional → legendary → unique`

`unique` is used only when explicitly authored as singular/effectively singular in scope. Power, fame or magical intensity do not imply rarity.

A definition's canonical rarity can be scoped. If supported rarity assertions conflict, the canonical `defaultBand` must remain `null` until a governed reconciliation decision cites the material assertions, records rationale and records authority.

### 3.2 Source mappings

Direct mappings are permitted only when the source semantics support them:

- Cooking `Common / Uncommon / Rare / Legendary` → canonical `common / uncommon / rare / legendary`.
- Alchemy `Common / Uncommon / Rare / Exotic` → canonical `common / uncommon / rare / exceptional` because Alchemy explicitly places `Exotic` inside its rarity ladder and gives it the DC-18 identification tier. The original word `Exotic` is still preserved.
- Agriculture's `Type` column is **not** automatically treated as canonical rarity. `Exotic` maps to origin context `origin:exotic`; `Supernatural` maps to nature `nature:supernatural`; Agriculture `Common` and `Rare` remain source-classification assertions unless separately reconciled as scarcity.
- `Bases_Facilities.csv` Common/Uncommon/Rare values can be mapped as source-scoped normalized rarity assertions, but they never silently override contradictory original source assertions.

This resolves the ICF-01 Medicinal Herbs / Fire Blossom / Etherleaf problem without selecting a winner by file order.

## 4. Taxonomy dimensions

Every ingredient definition may combine multiple orthogonal taxonomies.

### 4.1 Ingredient classes

The initial controlled classes include plant, fungus, animal-derived, aquatic-derived, insect-derived, mineral, chemical, microbial, magical-material, creature-derived, synthetic, prepared-intermediate and other. These are broad organizational classes, not effect rules.

### 4.2 Nature classes

The initial combinable nature vocabulary includes mundane, botanical, fungal, animal, aquatic, insectoid, mineral, chemical, magical, elemental, psychic, planar, chronal, necrotic, divine, infernal, synthetic, biotech, alien, supernatural and reality-specific.

A definition may have multiple nature classes where explicitly authored. These classes never imply culinary safety or alchemical effect by themselves.

### 4.3 Origin context

Origin context is separate from nature and rarity: native, non-native, exotic, extraplanar, cross-reality and unknown.

## 5. Availability and acquisition

Definition-level availability describes authored acquisition/access, not a live market quote. The baseline vocabulary is abundant, available, limited, restricted, seasonal, unavailable and unknown.

Acquisition modes include cultivation, foraging, husbandry, fishing, hunting, renewable harvest, post-mortem harvest, mining, collection, synthesis, processing, trade-only and explicitly authored extensions.

Availability can be scoped to a world/location/reality reference. MIB-13 may still report a different current merchant availability or scarcity state.

## 6. Units and quantity

Each definition declares a primary typed unit and allowed units. Core dimensions are count, mass, volume, length, area, energy, bundle, serving, custom and source-generic.

Core reusable unit IDs begin with examples such as `unit:piece`, `unit:leaf`, `unit:bloom`, `unit:egg`, `unit:feather`, `unit:gram`, `unit:kilogram`, `unit:milliliter`, `unit:liter`, `unit:bundle`, `unit:serving` and `unit:source-generic`.

Conversions are deterministic only when an explicit exact rational conversion is authored. Cross-dimension and ingredient-specific conversions require an ingredient-specific conversion rule. No name-based or heuristic conversion is allowed.

Legacy `Food Units`, `Material Units`, `resource unit` and bare `units` remain source assertions. They may be represented as `unit:source-generic` during reconciliation, but they are not sufficient typed outputs for ICF-13 deterministic production.

## 7. Profiles

A canonical ingredient is one identity with optional domain profiles rather than separate Cooking Ingredients and Alchemy Ingredients catalogs.

### 7.1 Physical profile

May describe authored physical forms, part classes, perishability, shelf-life rules, storage requirements, preparation requirements and contamination risks.

### 7.2 Ecology profile

May describe habitats, biomes, climate/season references, world/reality ranges and renewability.

### 7.3 Agriculture profile

May declare cultivation, husbandry or foraging eligibility plus facility, growth, yield and resource-requirement rule references. ICF-13 will supply the production integration; ICF-02 only defines the profile boundary.

### 7.4 Economic profile

May expose trade classes, legality references and provenance-scoped **source value assertions**. Each legacy value preserves amount text, original currency term/context, whether it was inferred, and the supporting source assertion.

The economic profile explicitly records:

- current price authority: `MIB-13`;
- market scarcity authority: `MIB-13`.

`gp`, `CR`, `credits`, `MC` and other legacy values are never averaged into a global price or silently converted into one currency.

### 7.5 Culinary profile

May declare edibility as known-edible, conditional, unsafe, inedible or unknown, plus namespaced flavor, texture, technique, nutrition, restoration and pairing references.

Harvestability does not imply edibility. `unknown` is valid and preferred to unsupported inference.

### 7.6 Magical-culinary profile

May declare namespaced magical-culinary affinities, potency rules, overload rules and compatibility rules. Magical-cooking properties are not silently copied into ordinary culinary or alchemical namespaces.

### 7.7 Alchemical profile

May declare explicit roles such as active, modifier, catalyst, stabilizer, solvent, binder, preservative, enhancer and carrier, plus namespaced essence/effect, volatility, extraction and identification rule references.

### 7.8 Creature-source profile

Creature-derived definitions can reference canonical creature definitions and authored harvest references. `evidenceRequired` is always true. Evidence status may be authored, partial or gap.

Missing creature anatomy, harvestability, edibility or magical effects remain coverage gaps. Generic body-plan or part rules introduced in ICF-07/08/09 cannot retroactively invent unsupported species-specific facts.

## 8. Property namespaces

Properties remain domain-scoped so identical words do not imply identical mechanics:

- `physical:`
- `culinary:`
- `magical-culinary:`
- `alchemy:`
- `alchemy-role:`
- `part:`

Setting- and reality-specific extensions use explicit namespaces such as `setting:<setting-id>:<domain>:<term>` and `reality:<reality-id>:<domain>:<term>`.

## 9. Quality and condition overlays

Current quality and current condition belong to the live D17 Asset instance. Ingredient definitions may only declare rule references or sensitivities describing how quality/condition modifies downstream behavior.

A quality or condition change does not create a new ingredient identity unless an authored transformation creates a genuinely new preparation/definition.

## 10. Substitution groups

Substitution is explicit data. Membership records include a group ID, role, compatibility level, restrictions and provenance.

Compatibility levels are exact, functional, partial, conditional or none. Roles include member, preferred, fallback and signature-exact-only.

Shared names, rarity, creature part, nature class or effect tags do not automatically authorize substitution. Signature recipes may explicitly require an exact ingredient even where a broader functional substitute exists elsewhere.

## 11. Primary ingredient versus derived preparation

A **primary ingredient** is a raw/directly acquired reusable feedstock whose identity does not require an ICF processing transformation lineage.

A **derived preparation** is a reusable ingredient-like intermediate intentionally produced from one or more ingredients/preparations through an authored transformation. It uses `preparation:<slug>` and must retain input lineage plus a transformation-rule reference.

A finished meal/potion/item is not automatically a preparation. ICF-10 will implement processing transformations against this boundary.

## 12. Provenance and authorship

Every definition records authorship class:

- `source-derived`;
- `governed-first-party`;
- `hybrid`.

Source-derived and hybrid records preserve material source assertions. First-party records cite their governed authoring record. A source assertion records source identity, optional source version/location, original source term/field/raw value, semantic interpretation and reconciliation status.

Normalization never deletes the source form.

## 13. Lifecycle and coverage

Definition lifecycle is draft, active, deprecated or superseded. Superseded records point to their replacement.

Coverage is separate from lifecycle: complete, partial, source-gap or not-applicable. Gaps are typed by domain and carry source references where available. A definition may therefore be active while honestly reporting an unresolved creature crosswalk or source field.

## 14. Normative fail-closed validation rules

The machine schema and taxonomy registry enforce or declare these rules:

1. Stable IDs are globally unique and immutable after active publication.
2. Primary ingredients use `ingredient:<slug>` and cannot have processing lineage.
3. Derived preparations use `preparation:<slug>` and require lineage.
4. Alias collisions generate review, not automatic identity merge.
5. Conflicting rarity assertions remain unresolved until governed reconciliation.
6. Source values retain original currency/context/inference status.
7. Current market price and market scarcity are not ingredient-definition fields.
8. Live owner, custody, quantity, current quality and current condition are not ingredient-definition fields.
9. Unit conversion requires an explicit exact rational rule.
10. Generic legacy output units cannot masquerade as typed production outputs.
11. Creature-source data requires authored evidence; a gap is valid and preferred to fabrication.
12. Substitution requires explicit group membership.
13. Domain properties use their own namespaces or explicit setting/reality extensions.
14. Existing MIB-12 crafting, MIB-13 economy, D17 Asset and creature/world authorities remain unchanged.
15. No production provider, real-money integration or migration 0022 is selected by this schema.

## 15. ICF-01 open-decision closure

ICF-02 resolves all thirteen ICF-01 handoff questions:

1. Stable IDs and aliases: governed immutable IDs plus non-authoritative lexical candidate matching.
2. Rarity: six-band canonical scarcity model with explicit provenance mappings and unresolved-conflict state.
3. Rarity/classification/availability/market scarcity: separate dimensions.
4. Units: typed dimensions plus explicit rational conversions and preserved source-generic assertions.
5. Value metadata: provenance-scoped source assertions; MIB-13 owns current prices.
6. Primary/derived boundary: `ingredient:` versus lineage-bearing `preparation:`.
7. Physical/edible/toxic/perishable/preparation fields: physical and culinary profiles with explicit unknown states.
8. Cultivation/foraging/husbandry: agriculture/ecology acquisition profiles.
9. Culinary/magical-culinary/alchemical properties: distinct namespaces/profiles.
10. Quality/condition: definition rule references with live state retained by D17.
11. Source-derived versus first-party authoring: explicit authorship class and source assertions.
12. Lifecycle/conflict/gaps: definition lifecycle plus separate coverage and provenance-reconciliation status.
13. Creature harvest: evidence-gated creature-source references with missing evidence represented as gaps.

## 16. Handoff to ICF-03

Once this tranche is `completed_verified`, ICF-03 may populate mundane crops and staple plants against the exact schema. It must not weaken the source/provenance, rarity-separation, unit, economy or live-state boundaries established here.
