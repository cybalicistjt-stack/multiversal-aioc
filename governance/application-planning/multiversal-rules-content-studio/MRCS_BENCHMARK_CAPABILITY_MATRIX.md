# MRCS — Benchmark Capability Matrix

**Program:** Multiversal Rules & Content Studio (MRCS)  
**Status:** OWNER-APPROVED PLANNING EVIDENCE  
**Checked:** 2026-09-11  
**Clean-room control:** `../proprietary-capability-mining/PCM_CLEAN_ROOM_AND_RIGHTS_RULES.md`

## Purpose

This matrix records public capability classes worth reproducing independently in a Multiversal-specific rules/content construction studio. It is requirements evidence, not source authority and not permission to copy vendor implementations.

The target is not to imitate one existing product. MRCS combines approachable guided homebrew, schema-aware system construction, database-centric RPG editing, visual rule relationships, packaging/versioning and Multiversal-native governance.

## External capability classes

| Product / workflow | Public source checked | Capability classes retained as requirements |
|---|---|---|
| D&D Beyond Homebrew | https://www.dndbeyond.com/homebrew | approachable type-specific homebrew creation; templates/collection workflows; downstream use of created backgrounds, feats, magic items, monsters, species, spells and subclasses in the surrounding toolset |
| Foundry VTT System Development / Data Models | https://foundryvtt.com/article/system-development/ ; https://foundryvtt.com/article/system-data-models/ | explicit system manifests; typed document/data models; extensible actor/item-style schemas; separation between system implementation and content |
| Foundry VTT Compendium Packs / Modules | https://foundryvtt.com/article/compendium/ ; https://foundryvtt.com/article/module-development/ | reusable packaged content; world/module/system provenance; content organization; permissions; import/export; dependencies and installable distribution boundaries |
| Foundry Custom System Builder | https://foundryvtt.com/packages/custom-system-builder | no-code custom-system authoring; formulas; custom rolls; reusable actor/item templates; immediate sheet-level feedback |
| Foundry Sandbox | https://foundryvtt.com/packages/sandbox | build broad RPG-system surfaces without requiring ordinary creators to write JavaScript |
| Fantasy Grounds rulesets/extensions/modules | https://www.fantasygrounds.com/modguide/extensions.xcp | base ruleset plus scoped extension layering; dependency order; explicit package identity/version; content/functionality separation |
| RPG Maker-style database editors | public RPG Maker MZ documentation/product workflow | centralized RPG databases for actors/classes/skills/items/equipment/enemies/states and related reusable records; category-specific editors rather than raw data editing |
| Game Creator-style modular RPG tooling | public Game Creator documentation/product workflow | separate but composable stats, inventory, quest and other modules; creator-oriented configuration over reusable runtime systems |
| GDevelop-style event/behavior systems | https://gdevelop.io/ | approachable visual event/condition/action and variable/behavior composition; inspectable logic without requiring a conventional programming workflow |

## Multiversal repository foundations already stronger than the benchmarks

MRCS begins from existing Multiversal capabilities rather than from a blank generic-system editor:

- `docs/FORGE_SYSTEM_DESIGN_v8.md` already defines guided type selection, natural-language interviews, canonical references, validation/provenance, readable + structured previews, Pack Lists and `.pack` compilation.
- `content-db` already carries a broad typed object corpus and by-type indexing across Actions, Attributes, Characters, Creatures, Effects, Encounters, Environments, Items and many other domains.
- CAB already governs advancement/balance distinctions and evidence requirements; MRCS must use those rules instead of inventing a generic point-balancer.
- ARI supplies resource identity/provenance/rights; CNI supplies modular content/runtime semantics; PCA supplies reusable recipe/simulation/QA primitives.
- MCS/MCCS/MAS/MSAS provide specialized authoring surfaces that MRCS can reference and preview without absorbing their ownership.

## Capability synthesis

| Capability | Benchmark lesson | MRCS requirement |
|---|---|---|
| Guided creation | D&D Beyond, current Content Forge | creator selects what they are making, gets domain-specific questions/templates, sees explanations and may save/return without raw-schema knowledge |
| Extensible types | Foundry Data Models | content-type registry drives schemas, fields, vocabularies, relationships and validation instead of hard-coded one-off forms only |
| No-code ordinary path | Custom System Builder, Sandbox | ordinary rule/content creation does not require JavaScript/JSON; advanced formulas/predicates remain bounded and typed |
| RPG database breadth | RPG Maker-class editors | Attributes through creatures/items/magic/economies are first-class structured definitions with cross-reference rather than unrelated text forms |
| Rule logic | GDevelop/event systems | conditions, predicates, selectors, actions/effects and relationships have inspectable visual/structured authoring plus non-graph alternatives |
| Scoped extensions | Fantasy Grounds extensions | house rules and system extensions declare scope, precedence, dependencies, compatibility and rollback instead of mutating core invisibly |
| Packaging | Foundry modules/compendia | Pack Lists compile to versioned dependency-aware content packages with provenance, permissions/visibility, update/migration and rollback evidence |
| Reference reuse | Foundry/RPG databases + Content Forge | shared Actions/Effects/Conditions/Resources/etc. are referenced rather than repeatedly copied into prose |
| Impact analysis | mature package/system workflows | author sees inbound/outbound dependencies before rename, replacement, deprecation, re-ID or deletion |
| Balance evidence | Multiversal CAB/PCA | schema validity is not a balance verdict; approved harnesses/simulations produce attached evidence and explicit uncertainty |
| Legacy migration | package/database ecosystems | bulk import/mapping/batch repair preserves source identity, aliases/history, unresolved fields and deterministic receipts |
| Runtime separation | Multiversal owner model | creating a definition, preview, simulation or pack never claims a live Character/World/Event mutation occurred |

## Negative benchmark lessons

MRCS deliberately avoids several common limitations:

1. **Fixed homebrew categories are insufficient.** A creator must be able to work across Multiversal's governed type registry, not only a small vendor-selected list.
2. **A full programming-language requirement is too high for ordinary content work.** Code remains an implementation escape hatch outside normal authoring rather than the normal creator surface.
3. **One generic formula field is not enough.** Typed rule atoms, timing, resources, stacking, acquisition, prerequisites and owner-domain semantics remain explicit.
4. **One scalar balance rating is prohibited.** CAB's multidimensional approach and domain-specific evidence remain authoritative.
5. **Extension convenience cannot mean invisible rule mutation.** Effective scope, precedence and conflicts must be inspectable and reversible.
6. **Pack portability cannot erase provenance.** Source, derivative lineage, rights, compatibility and migration state remain attached.
7. **Visual graphs cannot become accessibility gates.** Every graph/editor needs keyboard/non-pointer and structured list/tree/table alternatives.

## Clean-room restrictions

This study follows PCM clean-room rules:

- use only public product documentation, public demos, published APIs/SDKs and lawful ordinary-use descriptions;
- extract capability and workflow requirements, not proprietary implementation details;
- do not decompile, reverse engineer, scrape protected services, recover private protocols, copy proprietary source/assets/content, reproduce distinctive sample projects or copy protected UI expression;
- any third-party code, model, SDK, dataset or content later proposed for direct incorporation requires separate ARI rights/license/provenance review;
- vendor terms in this matrix remain planning provenance and do not define Multiversal product identity.

## Result

The benchmark supports a single Multiversal-specific destination: **Content Forge becomes a complete rules/content construction studio whose normal path is approachable and no-code, whose advanced path is structurally powerful, and whose outputs remain governed definitions rather than an alternate source of truth.**
