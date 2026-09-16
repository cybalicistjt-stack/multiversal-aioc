# PDCP MRCS Family Design Closure

**Program:** MRCS — Multiversal Rules & Content Studio  
**Status:** DESIGN_CLOSED_FOR_REDUCTION  
**Implementation authority:** none  
**Historical baseline:** 21 tranches  
**Effective implementation/proof plan:** 13 tranches

## Decision

MRCS remains the creator-facing governed definition-authoring system. It does not become a second runtime, simulator, provenance ledger, package registry, Character/NPC studio, map studio, audio studio, or canonical rules owner.

The safe reduced order is:

`MRCS-01 → 03 → 04 → 05 → 08 → 11 → 12 → 13 → 14 → 16 → 17 → 19 → 21`

The historical 21-tranche baseline remains provenance in the reduction receipt.

## Owner boundaries

- owner-domain contracts retain semantic authority for Attributes, Skills, Abilities, Actions, Effects, Conditions, Resources, Species, Forms, Professions, Items, Magic, Creatures, Vehicles, Environments, Encounters, Economy and other governed records;
- Content Forge remains the product foundation MRCS converges and expands rather than replacing;
- CAB retains advancement/balance authority;
- CNI retains conditional-content runtime authority;
- reduced GPR + Action/Event execute accepted definitions and own gameplay-instance execution/replay;
- PCA-12 + PDCP Packet 08 own generic simulation, optimization, graph/SAT/SMT and Monte Carlo machinery;
- Packet 07 owns generic preview/dry-run/commit/explanation/intervention/compensation/debug semantics;
- ARI/PCA retain generic identity, rights, derivative provenance, version/review/import-export infrastructure;
- MCS/MCCS/MNCS/MSAS retain specialist map, character/creature, NPC/creature and audio authoring;
- MERA/MBES consume MRCS engineering/construction definitions but own execution in their domains.

## Intra-family folds

### `MRCS-01 + MRCS-02 → MRCS-01`
One workspace/schema kernel owns workspace state, governed content-type registry, schema-aware forms, progressive disclosure, definition/instance separation, ownership display and validation routing.

### `MRCS-05 + MRCS-06 + MRCS-07 → MRCS-05`
Actions/Effects/Conditions/Resources and advancement-facing Abilities/trees/prerequisites/Attributes/Skills/Knowledges/Proficiencies use one governed mechanical-definition editor family. CAB and domain owners remain authoritative. `MRCS-05` remains a downstream DAG milestone.

### `MRCS-08 + MRCS-09 → MRCS-08`
Profession/Background/Culture/Faction/social packages and Species/Form/Archetype/Template/Variant/Trait packages share package composition, inheritance/reference, compatibility and scoped-override machinery. Identity and social domain semantics remain external.

### `MRCS-10 + MRCS-13 → MRCS-13`
Items/equipment/weapons/armor/tools/loadouts plus vehicles/mounts/companions/constructs/modular components share slot/component/loadout/reference and compatibility authoring. `MRCS-13` remains the MERA rotation milestone.

### `MRCS-14 + MRCS-15 → MRCS-14`
Environment/hazard/terrain/world content plus encounter/challenge/reward/loot/economy/service definitions share world/challenge composition and reusable-table/reference authoring. Runtime placement and economy truth remain external. `MRCS-14` remains the MBES rotation milestone.

### `MRCS-17 + MRCS-18 → MRCS-17`
Dependency/reference/impact/safe-refactor diagnostics and rule/content balance analysis become one diagnostics/evidence seam. PCA-12 supplies generic simulation/formal-analysis execution; MRCS supplies models, CAB harness adapters, impact interpretation and evidence attachment.

### `MRCS-19 + MRCS-20 → MRCS-19`
Bulk import/repair/migration/batch-edit plus pack/version/diff/review/publication workflow become one definition-lifecycle/interchange seam. Generic rights/provenance/version/review/import-export remains ARI/PCA; MRCS owns domain mapping, pack compilation, dependency manifests and rule/content migration behavior.

## Intentional non-merges

- `MRCS-03` remains distinct: guided interviews/templates/clone-fork/optional advisory AI are a substantial creator workflow over the core schema shell.
- `MRCS-04` remains distinct: bounded formula/predicate/selector/expression construction is a reusable technical workbench with its own safety and accessibility burden.
- `MRCS-11` remains distinct: spell/power/casting-method/magic-system packages have materially different owner contracts and cross-record semantics.
- `MRCS-12` remains distinct: creature/monster/NPC-role/behavior/combat packages require taxonomy, behavior and combat-definition integration not equivalent to identity/social packages.
- `MRCS-16` remains distinct: scope/precedence/compatibility/override/rollback conflict behavior is cross-cutting and safety-critical.
- `MRCS-21` remains the golden proof and GPR handoff.

## Reduced tranche scopes

1. **MRCS-01 — Studio Workspace, Content Registry & Schema-Aware Forms**: product shell, registry, schema-driven forms, progressive disclosure, definition/instance invariant, owner-routing and draft state.
2. **MRCS-03 — Guided Forge Interviews, Templates, Clone/Fork & Advisory Authoring**: guided creation, templates, lineage-safe clone/fork, save/resume, decide-later and optional advisory AI.
3. **MRCS-04 — Rule Atom, Formula, Predicate, Selector & Expression Workbench**: bounded typed expression construction, linting, dependency references, preview and accessible non-graph alternatives.
4. **MRCS-05 — Mechanical & Advancement Definition Authoring**: Actions/Effects/Conditions/Resources/durations/triggers plus Abilities/trees/prerequisites/Attributes/Skills/Knowledges/Proficiencies/advancement packages.
5. **MRCS-08 — Social, Identity, Species, Form & Template Package Authoring**: Profession/Background/Culture/Faction/social packages plus Species/Form/Archetype/Template/Variant/Trait definition composition.
6. **MRCS-11 — Magic, Power & Casting-System Authoring**.
7. **MRCS-12 — Creature, Monster, NPC Role, Behavior & Combat-Package Authoring**.
8. **MRCS-13 — Item, Equipment, Vehicle, Mount, Companion, Construct & Modular-Component Authoring**.
9. **MRCS-14 — Environment, Hazard, Encounter, Reward, Loot, Economy & World-Content Authoring**.
10. **MRCS-16 — System Extension, House Rule, Scope, Compatibility & Override Authoring**.
11. **MRCS-17 — Dependency, Impact, Safe Refactoring, Balance & Evidence Diagnostics**.
12. **MRCS-19 — Import, Repair, Migration, Pack, Version, Review & Publication Lifecycle**.
13. **MRCS-21 — Golden Cross-Domain Definition Construction & Runtime Consumption Proof**.

## Cross-family overlap decisions

- no runtime movement/combat/economy/project engine in MRCS; reduced GPR/domain owners execute;
- no generic simulation engine in `MRCS-17`; PCA-12/Packet 08 execute analysis;
- no generic creator-debug framework in MRCS; Packet 07 semantics are consumed;
- no generic provenance/version/review/import-export engine in `MRCS-19`; ARI/PCA own it;
- no duplicate visual/entity/audio studio behavior; MCS/MCCS/MNCS/MSAS remain specialist owners;
- no duplicate engineering/built-environment runtime; MERA/MBES consume accepted definitions.

## Golden vectors

`PDCP-MRCS-001` workspace does not create canonical instances.  
`002` registry metadata drives forms without hard-coded per-type screens.  
`003` unknown owner field remains unresolved.  
`004` required/optional fields remain distinguishable.  
`005` progressive disclosure preserves complete advanced access.  
`006` draft save/resume is noncanonical.  
`007` clone preserves source/derivative lineage.  
`008` fork creates distinct identity with provenance.  
`009` advisory AI cannot publish or canonize.  
`010` guided and advanced authoring converge on the same governed schema.  
`011` expression workbench rejects unrestricted-script fallback.  
`012` expression inputs and references are inspectable.  
`013` expression cycles fail safely.  
`014` nonvisual expression editing has functional parity.  
`015` Action/Effect/Condition/Resource references preserve owner semantics.  
`016` ability/prerequisite authoring cannot override CAB.  
`017` Attribute/Skill/Knowledge/Proficiency packages preserve owner advancement economics.  
`018` stacking/interaction stays definition-driven rather than universal.  
`019` social package authoring cannot mutate live relationships.  
`020` Species/Form/Template definitions remain distinct from live Characters.  
`021` inheritance conflicts remain explicit.  
`022` unknown compatibility remains unresolved.  
`023` magic-system definitions cannot invent runtime casting authority.  
`024` creature definitions remain distinct from encounter instances.  
`025` behavior packages cannot autonomously mutate NPC truth.  
`026` item/loadout definitions remain distinct from owned Inventory state.  
`027` vehicle/mount/construct definitions preserve owner references.  
`028` modular compatibility is explicit and versioned.  
`029` environment definitions do not place canonical World state.  
`030` encounter definitions do not execute encounters.  
`031` reward/economy definitions do not grant/spend value.  
`032` house-rule scopes resolve explicitly.  
`033` conflicting overrides remain diagnosable.  
`034` disable/rollback restores prior effective-rule resolution without deleting history.  
`035` dependency browser filters protected information.  
`036` safe refactor previews impacted references before commit.  
`037` deprecated/replaced IDs preserve migration paths.  
`038` balance analysis uses owner-approved models only.  
`039` solver/Monte Carlo unknown or uncertainty remains inconclusive.  
`040` no universal balance scalar is invented.  
`041` legacy import preserves source text and unresolved gaps.  
`042` batch edit previews deterministic affected-set evidence.  
`043` migration is versioned and reversible where owner contract permits.  
`044` Pack compilation validates dependency manifests.  
`045` rights/provenance checks defer to ARI/PCA authority.  
`046` publication cannot bypass approvals or permissions.  
`047` reduced GPR consumes accepted MRCS definitions without ownership bleed.  
`048` final proof works with optional AI and paid/cloud providers disabled.

## Capability preservation

Every historical tranche maps to a survivor or shared owner in `PDCP_MRCS_REDUCTION_RECEIPT.json`. No capability, golden proof, migration/recovery, accessibility, permission/privacy, provenance or deterministic-validation obligation is removed.

## DAG preservation

`MRCS-05`, `MRCS-13`, `MRCS-14`, and `MRCS-21` survive with equivalent-or-stronger semantics. No `ROADMAP_DEPENDENCY_GRAPH.json` mutation is required by this reduction.

## Result

**Baseline:** 21  
**Effective:** 13  
**Removed standalone tranches:** 8  
**Capability loss detected:** false  
**Next PDCP family:** MSAS
