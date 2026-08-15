# Shared Multiversal Content Context Contract

**Status:** owner-approved A8 foundation seam  
**Source:** Item Preparation v0.12.0 + Reality Preparation v0.14.0 + Platform Preparation v0.11.0  
**Runtime owner:** shared content/catalog foundation; no single Item, Vehicle, or Reality domain owns the master vocabulary.

## Purpose

The Item, Platform/Vehicle, and Reality preparation work converged on a common contextual classification vocabulary. A8 must not create a parallel genre/era/technology/environment taxonomy that later World/Reality work would need to replace.

The shared foundation consists of nine independent facets and **241 controlled values** in the Item v0.12.0 source registry set:

1. **Setting Family** — broad setting/cosmological family.
2. **Genre Tradition** — genre and subgenre traditions; multi-valued rather than one-world/one-genre.
3. **Era / Development** — historical/developmental context.
4. **Technology Paradigm** — intrinsic/contextual technology environment.
5. **Power Paradigm** — magic, psionics, superhuman, divine, cultivation and comparable extraordinary-power contexts.
6. **Environment** — operational/environmental context.
7. **Play Domain** — combat, exploration, investigation, trade, crafting, rescue, logistics and other play uses.
8. **Tone / Style** — grounded, heroic, horror, noir, whimsical, etc.
9. **Content Scale** — personal through multiversal scope.

## Machine-identity rule

Where semantically identical facet values are reused by Items, Vehicles/Platforms and Realities, they must reuse the same machine identity rather than creating domain-prefixed synonyms.

Domain-specific classification remains separate. For example, Vehicle class/scale and Item physical form are not replaced by these contextual facets.

## Assertion rule

A contextual facet is not automatically an intrinsic fact.

- **Intrinsic requirement**: required for operation/existence/function.
- **Affinity**: thematically or conventionally associated.
- **Context assertion**: describes a setting/local scope.
- **Compatibility result**: computed/evaluated against a specific context.

A Cyberpunk affinity does not mean an Item only works in Cyberpunk settings. A localized cyberpunk district does not relabel its entire parent world. A shared source document does not automatically propagate every facet to every contained entity.

## Scope rule

The later Reality/World system may assert facets at whole-setting, reality, region, settlement or other governed scopes. A8 consumes the effective authorized context; it does not infer broader scope.

## Permission rule

Contextual facets and compatibility output inherit F020 permission filtering. Hidden setting facts must be removed before search counts, filters, recommendations, compatibility explanations, exports or AI context.

## A8 implementation rule

A8 revalidation must create/reuse one provider-neutral `ContentContext`/equivalent seam capable of supplying the nine facets and required intrinsic context without freezing future table, ORM, API or component names.

Until a full setting provider exists, values may be unknown/unavailable. Unknown must not silently become compatible or incompatible.

## Source registry preservation

The exact source registry values remain checksum-bound to `Multiversal_IA_Item_Taxonomy_Preparation_v0.12.0.zip` in `STAGE_A_A8_SUPPLEMENTAL_SOURCE_MANIFEST.json`. A8 revalidation is required to preserve the machine identities rather than re-author the vocabulary from memory.