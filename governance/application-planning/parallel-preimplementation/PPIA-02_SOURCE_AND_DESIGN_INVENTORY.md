# PPIA-02 Creature & NPC Source and Design Inventory

**Work item:** PPIA-02 — Creature & NPC Experience  
**Status:** IN PROGRESS — FOUNDATION INVENTORY  
**Owner:** John Brandon Turner  
**Repository branch:** `governance/ppia-02-creature-npc-experience`

## 1. Authority boundary

PPIA-02 is an experience/design tranche. It must not revive the earlier unsuccessful semantic-parse database as canonical creature content.

Use authority in this order:

1. current canonical repository governance, feature, screen, permission, provenance, and workflow contracts;
2. retained original Creature/creation PDFs for creature-domain source truth;
3. later governed PPIA-01 source/provenance/inference distinctions;
4. legacy `content-db/objects/mv-object-creature-definition/*` only as compatibility/test references where useful, never as proof that their sparse semantic object bodies are complete source truth.

The later 8E-009 CSV-first registry is the current structured-content authority for its 20 governed CSV datasets / 19,199 rows, but it does **not** contain a dedicated creature catalog. PPIA-02 therefore does not pretend that those CSVs are a complete creature source.

## 2. Retained Creature-domain source library

`MV_Master_01_Core.zip` retains **23 dedicated Creature PDFs** plus **Player Creatures.PDF**. These are preserved source evidence and must remain distinguishable from later authored recommendations.

| Source | SHA-256 |
|---|---|
| `Creatures/Elementals.PDF` | `052b28f5214acc3c8aebc1c2c80631faf16bb5da58e0165bbb798830ae8355db` |
| `Creatures/Incorporeal Creatures.PDF` | `658d7e0dcdd48c3604be9e7d60040ec96226dcf1b9009e7a06ddce934ca4dc8a` |
| `Creatures/Chaos Creatures.PDF` | `29087e478cbd37b710d8203b0b9256fe76b816a7c686bb5efab3adf816df8fc6` |
| `Creatures/Zombies 11-16-24.PDF` | `73e0e520b0fe8ca7d0376ddbcc87bdccad9d87dcf98caea0528a852cc297830f` |
| `Creatures/Toon Creatures.PDF` | `6f8e5d58ebe2fb3e57408c5e419f67162ba9145d54821f94e94afa015710433e` |
| `Creatures/Demonic Creatures.PDF` | `20840a7aa6e501bf68707d06187e414f4ef25d2329ef77cf585ba805890ecee2` |
| `Creatures/The Fey.PDF` | `f1003ac5edb75a32c917d68b182cdcfd9d77303ae2376e1aefe99a976886c69e` |
| `Creatures/Vampirism&Lycanthropy.PDF` | `f2e39d2781f174e1fff41001e98842158b06946c21a777189021ed2dae840685` |
| `Creatures/Havalaea Creatures.PDF` | `78bc18c5026c623261ccd312c4fbae8b015f8c2d42d212904b7dfeb5b20afeab` |
| `Creatures/Beasts 2.PDF` | `e595d7b6738316e5858c1688f16758d00edbffd60904f4ab2aeabac31d873c26` |
| `Creatures/Divine Creatures.PDF` | `918197d02b18b9ab9162bd2c40c3202ddc461924d0e4d26c01c45ec9d5ce4f7c` |
| `Creatures/Creature types.PDF` | `5001dc9dd25096ea559c7d6c0f11bfd2113bd4637b07cb64455fc448cfed6fd5` |
| `Creatures/Digital Creatures(1).PDF` | `8305da4bafb7d4d97142afc61b02f5f61973ade2d5b164a96a20ae527fee7482` |
| `Creatures/Skoaltarran Creatures.PDF` | `dc6e17315b7059f9742f5fef12362ea3de8fd2a2d4215a8b2b9f65274982a344` |
| `Creatures/The Fell.PDF` | `ec6f7c7840b4516e3efeb626a173ce6344fef8c864c9cb9fb6389f202a6e45d0` |
| `Creatures/Undead Creatures.PDF` | `f0f79b8a154a31a20d3911932faa3dd7fc8ceac582f6638bf709c10147344e75` |
| `Creatures/Dragons(1).PDF` | `21a188666b72e0d083fb40e4105b240d9c12a9989198ac416e568900a4dc29fc` |
| `Creatures/Plant Creatures.PDF` | `d5b284b25d30587119764a1220d828aabb5f104455341890f7bb00ff2641ee40` |
| `Creatures/animals 11-16-24.PDF` | `6b9e8a4b1e30001f38bf2012933a7ec5704a02b6177dbc38b0707d6f44545f3e` |
| `Creatures/Constructs.PDF` | `eb48c74bc68a4c8865aad6f5076aedd525a7b1199dbe5075d4643aeb7f91a0b4` |
| `Creatures/Ghosts 11-16-24.PDF` | `b5da36cc7e3bce0a45b28dc6f68b45ea01b2c3c11e1284c3d38414ed6a7ec647` |
| `Creatures/Beast Creatures 1.PDF` | `3b7a1b666e142cf0dd4bf74449855cd1fc5abccd881cec64c0c0e095faaa8b4b` |
| `Creatures/Aberrations.PDF` | `6f83737e34ded4910219b9d967951cda714a48c3ba02146fdf1cf5b2cf603d08` |
| `Part 1/Creation/Player Creatures.PDF` | `b6626049ddab2cc30295602fa03581a7d66b4352dc4e0cdc30fd1dc5929613f3` |

## 3. Source patterns already verified

A render-first review of representative sources establishes several design requirements without requiring semantic reconstruction of the entire corpus.

### `Creature types.PDF`

Creature types may function as **adjustment/modifier layers**. The source describes type-driven resistance/vulnerability, special abilities, environmental adaptation, and appearance changes. PPIA-02 must therefore support modifier/template/affinity relationships rather than assuming every type is a separate base identity.

### `Player Creatures.PDF`

The source defines a procedure for converting a monster into a playable species, including base-version selection, retained physical traits, XP costing, unlockable abilities, HP/defense normalization, and ability-score conversion. PPIA-02 must expose a **playable-conversion relationship** without presenting the converted Character/species result as if it were the same live creature instance.

### `Dragons(1).PDF`

The source explicitly distinguishes intelligence spectrum and age/power stages such as Hatchling/Wyrmling, Juvenile, Adult, Elder, Ancient, and some category-specific stages. PPIA-02 must support **stage/variant chains** and cannot flatten all age stages into one stat block.

### `Havalaea Creatures.PDF`

Representative entries combine CR, size/type, alignment, AC, HP, movement, attributes, resistances, senses, languages, traits, actions, and **Behavior**. Ecology/behavior is therefore a first-class inspection region alongside combat data rather than optional flavor hidden in notes.

## 4. Controlling feature/design surfaces

### MV-IA-F002 — Universal Object Experience

Controls common Library/Inspector/Picker behavior:

- stable-ID identity;
- role-safe summary/detail projections;
- provenance and source coordinates;
- incomplete-source/conflict presentation;
- permitted relationships and variants;
- Definition versus Campaign placement versus live instance distinction;
- authorization before results, counts, facets, relationships, and provenance;
- responsive and nonvisual inspection paths.

PPIA-02 must **specialize** F002 for creatures/NPCs, not create a second incompatible browser/inspector system.

### MV-IA-F005 — Campaign, Scene, and Session Builder

Controls creature/NPC placement semantics:

- source creature/NPC Definition remains immutable;
- Scene placement gets a distinct `placementId`;
- quantity, visibility, initial state, and local override belong to the placement;
- launch snapshots are immutable authority for a live Session;
- Player projection must not expose hidden creature/NPC existence or exact counts.

### MV-IA-F012 — Encounter Builder and Balance Lab

Controls preparation/analysis semantics:

- creature/NPC participant selection by stable ID;
- exact source/version/pack binding;
- placement quantity/wave/visibility/starting assumptions;
- source provenance for normalized analysis fields;
- no guaranteed-balance claim;
- Player/observer projections exclude hidden participants, counts, waves, tactics, secret objectives, and GM-only warnings.

### Screen Design Bible surfaces

The consolidated Screen Design Bible establishes directly relevant screens:

- `SD-203` — Item Inspector: carried assets/loot/equipment inspection dependency.
- `SD-301` through `SD-309` — combat, targeting, log, initiative, Conditions, encounter summary.
- `SD-405` — Witness & NPC Profiles: identity, relationships, reputation, statements, contradictions, reliability, timeline participation.
- `SD-503` — Relationship Graph.
- `SD-506` — Organization & Faction Profiles.
- `SD-601` through `SD-608` — exploration/discovery/environment context.
- `SD-1003` — Scene Builder.
- `SD-1004` — Encounter Builder.
- `SD-1007` — Content Library.
- `SD-1107` — Audit & Provenance Explorer.

The UI Design Bible additionally requires an **NPC & Creature Manager** in the GM core toolset and reusable Rule Inspector, provenance, permission, validation, responsive, keyboard, touch, and noncolor patterns.

## 5. Required data/experience distinctions

PPIA-02 must preserve these distinctions even when legacy files used one broad creature object family:

1. **Reusable Definition** — source/governed creature or NPC definition.
2. **Presentation profile** — creature-oriented, NPC-oriented, sentient/hybrid, summon/minion, swarm/group, staged/variant, playable-conversion, etc.; this is presentation metadata and does not silently redefine canonical identity.
3. **Variant/template/type modifier** — relationship to a base definition or sibling definition, preserving source/version provenance.
4. **Campaign/Scene placement** — distinct placement identity with local visibility, notes, quantity, role, starting state, and allowed overrides.
5. **Live instance** — runtime HP/resources/conditions/location/initiative/control state; never written back into the reusable Definition by inspection.
6. **Character/playable conversion** — governed transformation/reference path from creature source to playable character/species rules; not identity equivalence.
7. **Historical/source record** — original source evidence and transformation/provenance history.

## 6. Creature/NPC information domains to support

The specialized experience must be able to present, when available and authorized:

- identity, aliases, category/type/tags, source, pack, version, validation, conflict, source-coverage state;
- encounter summary: role, threat/CR or governed equivalent, size, defenses, HP/resources, speed/movement, senses;
- attributes, saves, skills, proficiencies, immunities/resistances/vulnerabilities;
- Actions, Abilities, traits, reactions, passives, Conditions, Effects, Resources, cooldowns/uses;
- targeting/range/area and rules references where those belong to linked governed objects;
- ecology, habitat, behavior, activity patterns, diet, social structure, environmental adaptation;
- languages, intelligence/personhood indicators, communication, attitudes, motives, goals, roleplay notes when source-supported;
- relationships, organizations/factions, reputation context, witness/investigation material for NPC-like entities;
- equipment, carried items, inventory, loot tables/bundles, ownership and provenance;
- variants, templates, type modifiers, age/power stages, forms, transformations, evolutions;
- summon/minion/master or spawn relationships;
- playable-conversion relationship where governed;
- Campaign placements, local labels/notes/visibility/initial-state assumptions;
- live-instance state only in a runtime context;
- source coordinates, source-versus-recommendation distinction, conflicts, unresolved fields, and audit history.

Absence of a field must not be converted into invented source data merely to fill an Inspector section.

## 7. Role projection requirements

### Player-safe

May show only revealed/authorized identity, visible mechanics, known ecology/lore, permitted relationships, and accessible source detail. Hidden existence, GM-only variants, unrevealed weaknesses, secret motives, exact hidden counts, loot, tactics, spawn/reinforcement data, or private notes must not reach the client projection.

### GM

May show authorized full preparation/runtime data, source warnings, hidden placement data, tactics/behavior notes, encounter roles, private relationships, secret objectives, loot/reward information, and local override provenance.

### Assistant GM

Must be delegation-scoped rather than treated as an unrestricted GM alias.

### Creator/Owner/Admin

May inspect governance/provenance according to separate authority. Administrative capability is not automatic entitlement to every Campaign-private field.

### Service/AI

Receives only the narrower role-safe projection required for the operation. AI remains read-only/proposal-only and may not fill unknown source facts invisibly.

## 8. Accessibility and density requirements

Dense creature stat blocks require more than visual card reduction:

- semantic section/headings and table/list alternatives;
- one linear reading order equivalent to multi-column desktop layouts;
- explicit labels for resistances/vulnerabilities/conditions rather than color-only chips;
- keyboard access to every Action/Ability/source relationship;
- nonvisual relationship/variant traversal;
- touch alternatives for drag/reorder/quick-add;
- high-zoom reflow;
- collapsible detail that does not hide required status, permission, or validation information;
- comparison views that identify changed fields textually;
- compact GM density without reducing touch/focus/accessibility requirements.

## 9. Initial PPIA-02 implementation taxonomy

PPIA-02 will design one shared specialized Creature/NPC experience around these contexts:

1. **Library/Reference** — browse, search, inspect, compare, provenance.
2. **GM Authoring** — create/edit Campaign-local drafts or references without mutating source Definitions.
3. **Scene Placement** — quick-add, quantity, visibility, starting-state, encounter role.
4. **Encounter Preparation** — participant/wave/role/analysis inputs and warnings.
5. **Live Runtime** — current instance state, actions, conditions, initiative, target/approval context.
6. **Investigation/Social** — witness/persona/reputation/relationship/secret projection for NPC-capable entities.
7. **Exploration/Bestiary** — ecology, habitat, discovery, known-versus-hidden information.
8. **Comparison/Variant** — sibling variants, templates/modifiers, age stages/forms, source conflicts.
9. **Summon/Minion/Spawn** — master/source relationship, control/ownership, lifecycle and placement distinctions.
10. **Playable Conversion** — explicit source-to-playable relationship and conversion provenance.

## 10. Next bounded substep

Convert this inventory into a machine-verifiable PPIA-02 experience taxonomy and screen/role/field matrix, then define the Creature/NPC Inspector hierarchy and reference cases. No source content repair or canonical promotion is authorized by this inventory.
