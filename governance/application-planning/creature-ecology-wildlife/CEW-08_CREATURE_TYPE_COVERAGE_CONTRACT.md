# CEW-08 — Creature-Type Coverage Audit Contract

**Contract:** `CEW-TYPE-COV-1.0`  
**Work item:** CEW-08 — Creature-Type Coverage Audit  
**Authority:** content/recovery/design/provenance only; **no application implementation authority**.

## Purpose

CEW-08 measures how completely the recovered CEW-02 creature-type system is represented across the retained source corpus and the current canonical Creature Definition catalog. It consumes `CEW-ID-1.0`, `CEW-TAX-1.0`, and `CEW-COV-1.0` without changing their identity or taxonomy semantics.

**Type coverage is not creature identity coverage.** A creature can have governed identity without an explicit governed game-type binding, and a source family can have extensive type evidence without establishing a binding to any canonical stable ID.

**Source-family coverage does not create canonical stable-ID type bindings.** Counts in this tranche describe source-collection evidence only. They do not authorize name matching, namespace interpretation, mechanical similarity, source-family membership, or apparent thematic fit as identity/type binding mechanisms.

## Recovered type-family coverage

CEW-08 audits the fourteen game-facing base-type usages retained by `CEW-TAX-1.0`:

- **Recovered family semantics:** Aberration, Chaos, Construct, Demonic, Digital, Divine, Elemental, Fell, Fey, Toon, Undead.
- **Partial family normalization:** Dragon.
- **Repeated stat-block usage without a dedicated recovered family contract:** Beast.
- **Orphan unresolved base-type usage:** Illusion.

For the thirteen type families/usages whose supporting source collections are safely attributable, the retained corpus contains **683 safe statblock records**. This is source-collection representation, not a count of canonical Creature Definitions and not a creature/type completeness score. Illusion occurs in a mixed Incorporeal source and is not assigned a fabricated count.

**A missing family contract is an audit gap, not permission to invent one.** Beast and Illusion remain explicit gaps; Dragon remains partially normalized. CEW-08 does not create a new type contract, rewrite CEW-02, or normalize those terms by fiat.

## Canonical stable-ID coverage

CEW-07 established 27 canonical Creature Definitions. CEW-08 confirms that the current governed artifacts contain **zero explicit stable-ID game-type/taxonomy bindings** for those 27 definitions.

That yields an audited state of 0 explicit and 27 unknown type bindings. `Unknown` does not mean the underlying creature has no type; it means CEW has no explicit governed stable-ID binding at this point in the program.

The following are forbidden as substitutes for explicit authority:

- display-name similarity or exact-name overlap;
- namespace such as `mv.setting.havalaea` or `mv.playtest`;
- mechanics, powers, morphology, encounter role or ecology;
- source collection or PDF filename;
- biological identity such as Animal or Plant;
- environmental suitability or canonical distribution.

## Cross-cutting systems

**Cross-cutting systems are not base-type gaps merely because they use the word type.** CEW-08 therefore does not count these as missing global base types:

- Plant biological tag and movement categories;
- Incorporeal manifestation axis;
- Zombie conversion templates;
- Ghost and spirit conversion templates;
- Vampirism and lycanthropy transformations;
- Animal biological/ecological identity;
- Fire/Cold/Shadow/Chaos/Mechanical animal modifiers;
- Havalaea or Skoaltarran setting collections;
- Toon behavioral tags;
- Dragon age stages.

Only an explicit source rule may replace a base game type, such as the CEW-02 recovered `Undead-Type Animal` or `Mechanical-Type Animal` type-change statements. Those modifier rules do not create canonical Creature Definition bindings by themselves.

## Preserved unresolved taxonomy

The seven CEW-02 unresolved conflicts remain unresolved and visible:

1. Vampire / Fell / Undead.
2. Chaos Demons / Chaos / Demonic.
3. Hardlight / Digital / Construct / Magitech.
4. Divinetech / Divine / Construct.
5. Beast / Animal / Beastfolk.
6. Illusion orphan type usage.
7. Dragon category / type / stage normalization.

CEW-08 is an audit, not an owner-resolution tranche. No last-write-wins or single-axis collapse is authorized.

## Gap queue

CEW-08 records four bounded type-coverage gaps:

- Beast family-contract gap;
- Illusion orphan-type-usage gap;
- Dragon partial-normalization gap;
- canonical stable-ID type-binding coverage gap.

These gaps do not create creatures, types, aliases, promotions, or application changes. Later governed source/taxonomy reconciliation may resolve them; broad creature/type gap expansion remains owned by CEW-15.

## Future-owner boundary

**CEW-09 is the strict successor.** It owns intelligence, personhood, domestication and partnership classification and must not infer those dimensions from game type.

Subsequent owners remain:

- CEW-10 — Havalaea native fauna and Time-of-Troubles lineage;
- CEW-11 — mount, pet, familiar and companion-system crosswalk;
- CEW-12 — Earthlike animal and wildlife baseline;
- CEW-13 — environment-driven wildlife gap expansion;
- CEW-14 — multiversal and alien wildlife expansion;
- CEW-15 — monster, extraordinary-creature and creature-type gap expansion.

## Non-authorities

CEW-08 does not:

- assign game types to the 27 canonical Creature Definitions;
- bind source records or labels to stable IDs;
- create, promote, merge or delete Creature Definitions;
- invent a Beast or Illusion family contract;
- normalize Dragon beyond the recovered CEW-02 evidence;
- resolve the seven CEW-02 taxonomy conflicts;
- infer intelligence, personhood, domestication, partnership, mount, pet, familiar or NPC status from type;
- alter habitat, distribution or encounter facts;
- calculate a numeric creature/type quality or completeness score;
- mutate `Multiversal-app` schemas, runtime, UI, search, migrations or placement state.

## Handoff

CEW-08 closes when the type-family coverage matrix, canonical stable-ID type-binding gap, unresolved type-gap queue and preserved CEW-02 conflicts are verified and **CEW-09 — Intelligence, Personhood, Domestication & Partnership Classification** is selected as the strict successor.
