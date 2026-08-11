# PPIA-03 Items, Equipment & Inventory Source and Design Inventory

**Work item:** PPIA-03 — Items, Equipment & Inventory Experience  
**Status:** IN PROGRESS — FOUNDATION INVENTORY  
**Owner:** John Brandon Turner  
**Repository branch:** `governance/ppia-03-items-equipment-inventory`

## 1. Authority boundary

PPIA-03 is an experience/design tranche. It deepens the already-approved Internal Alpha inventory model without reviving the earlier unsuccessful 487-object semantic-parse database as game-content authority.

Use authority in this order:

1. current canonical repository governance, Universal Object Experience, Character, Campaign/Scene/Session, Inventory/Ownership, combat, permissions, recovery, provenance, and screen-design contracts;
2. the later governed 8E-009 CSV-first registry for structured Item-domain content and its final 20-dataset / 19,199-row reconciliation;
3. retained original Item PDFs for exact source truth and source recovery;
4. PPIA-01 source/provenance/inference distinctions and routed unresolved cases;
5. recovered 8E-008G-R1 formal deferrals only as source-accountability/reference candidates, never as automatic canonical Item Definitions.

The obsolete 487-object semantic database is compatibility debt only. PPIA-03 does not use it to measure Item completeness.

## 2. Retained Item-domain source library

The retained Item source library contains **13 dedicated PDFs / 218 pages**. The SHA-256 values below are from the exact retained copies in `MV_Master_01_Core.zip` and provide a stable evidence anchor without replacing repository governance.

| Source | Pages | SHA-256 |
|---|---:|---|
| `Armor & Shields.PDF` | 3 | `b1723305140265f02b19383617e781c7dd56c1b9d036d3ab2dcac6574111f852` |
| `Computers 2-7-25.PDF` | 31 | `3068aa7db4661a48113e5905a31db2661894cd9d5761937d601c4824f44c2ebe` |
| `Cybernetics.PDF` | 10 | `52ebe4c4d74f0a036fdaf9b9c670be173ba015dc002a6532eec7afdc5b386c5e` |
| `EVA Suits.PDF` | 8 | `f7785ccbd5c8e8123cd8963ca584137748a5546e8ec74122d8f59bbdbf73f670` |
| `Guns 11-8-24.PDF` | 7 | `3004d548f59b1860dd2f5f860b1aea90048706b75046322389abd037f6fa107b` |
| `Items 1.PDF` | 42 | `728bed92e50577085490fc9a111c92aff142b837d4fa122fa1e9d0b0866718b3` |
| `Living Spellbooks.PDF` | 11 | `1c860f5697f278210b8afd1275e88c544d4bfff5e28db3d84209c4b600d3c1c1` |
| `Magic charge holders.PDF` | 12 | `7db1b047a24037ebfd783c6a25d210546584e90f272f85031bba1f9eb22b745d` |
| `Magitech Items.PDF` | 35 | `3585426199c974f6b50018cfa09c2692053edca614ecccec96be0d7b690d3b4c` |
| `Magitech Rules.PDF` | 28 | `c926ff7ff22865e3e974f377c0a931551e070e6e4b929a11b44aeeec57a9620f` |
| `Materials.PDF` | 9 | `a3d2ed227115adc22e11568e4a49091b9ff733fafeb0a53902a775e0520f0e26` |
| `Melee Weapons.PDF` | 7 | `fd85cb32f449307501bcdd8d368c7de560fab1b7158084bc06cb47d9f6b53d46` |
| `Symbiotes 11-9-24.PDF` | 15 | `4ab91b8c57cd4b3da22589628291f1f9698e23a86c0c3add12c81487c5f54651` |

## 3. Structured CSV content surface

The current `CSV_SOURCE_REGISTRY.json` identifies **nine direct Item-domain datasets totaling 5,389 governed rows**:

| Dataset | Rows | Primary Item surface |
|---|---:|---|
| `expanded_melee_weapons_all_genres.csv` | 327 | melee / thrown / powered melee weapons |
| `expanded_ranged_weapons_catalog.csv` | 230 | firearms, ranged weapons, energy-weapon gap routing |
| `weapons_and_ammo.csv` | 36 | weapon overlap and ammunition references |
| `expanded_items_all_genres.csv` | 761 | consumables, containers, tools, devices, miscellaneous items |
| `expanded_magitech_items_all_genres.csv` | 532 | magic/technology items, weapons, devices, modules |
| `expanded_eva_suits_and_modules_all_genres.csv` | 430 | suit chassis, modules, interfaces, accessories |
| `expanded_computers_all_genres.csv` | 1,000 | computers, components, software/protocols, AI/control systems |
| `expanded_living_spellbooks_and_magic_charge_holders_all_genres.csv` | 1,501 | living spellbooks and charge/storage implements |
| `expanded_symbiotes_and_cybernetics_all_genres.csv` | 572 | symbiotes, cybernetics, integrated upgrades |

Two mixed-domain datasets are important adjuncts but **must not be counted wholesale as personal Items**:

- `expanded_bases_facilities_materials_and_homesteads_all_genres.csv` — 1,080 rows; contains governed material/crafting-resource candidates alongside facilities/bases/homesteads.
- `expanded_hazards_and_traps_all_genres.csv` — 1,901 rows; contains trap/deployable intersections alongside hazards.

Vehicle/mecha/spacecraft component rows remain primarily PPIA-04 territory even when their names resemble weapons, armor, computers, or inventory components.

## 4. Verified content-family patterns

The retained CSV copies establish several implementation requirements without requiring a new semantic parse.

### General Items

`Items.csv` contains 761 rows spanning, among other categories, consumables, magic items, technology, tools, professional gear, containers, communication, information, explosives, medical gear, sensors, space gear, weapons, survival gear, and mobility equipment. PPIA-03 therefore cannot reduce inventory to weapon/armor slots plus a generic bag.

### EVA equipment

The 430-row EVA dataset includes 25 complete suit chassis, 360 modules, 26 suit interfaces, 10 accessories/consumables, and 9 customization packages. A suit frame, installed module, loose module, interface, and consumable must remain distinguishable Assets with explicit compatibility/installation state.

### Computers and software

The 1,000-row computer dataset includes complete computers, software/protocols, core components, network components, control systems, expansion modules, security/interface/power/sensor components, vehicle computers, and AI-related records. Software-like Assets need install/compatibility/license/access semantics without pretending every software record is a physical carried object.

### Living items and charge holders

The 1,501-row living-spellbook/charge-holder dataset contains 720 original living spellbooks and 720 original charge holders plus source chassis, progression, personality, ability-module, upgrade, and source charge-holder records. The Item experience must distinguish a living/sentient Asset, a spell/charge storage Asset, and supporting progression/rule records.

### Symbiotes and cybernetics

The 572-row dataset separates symbiotes, cybernetic implants/systems, integrated symbiotech, maintenance/bonding/surgical items, cybernetic weapons/projectors, limbs/replacements, and an external frame. PPIA-03 owns the Asset/inventory/equipment/ownership/provenance view; biological form/host-body consequences route to PPIA-05 where they become Character-biology concerns.

### Materials

The mixed base/facility dataset contains explicit material records and construction/crafting-material categories. Material lots can participate in inventory, quantities, crafting reservations, transfers, provenance, and consumption without converting facilities or bases into ordinary carried Items.

## 5. Controlling design surfaces

### MV-IA-F002 — Universal Object Experience

Controls shared browse/inspect/compare/Picker behavior, stable identity/version, provenance, incomplete/conflicting source presentation, authorization-before-projection, and Definition-versus-context distinctions. PPIA-03 specializes this surface for Items rather than creating a second object browser.

### MV-IA-F008 — Inventory, Ownership, and Shared Assets

This is the primary runtime design baseline. It already requires separate Asset Definition, Asset Instance, ownership, custody, control, access, possession/location, containment, equipment assignment, quantity lot/stack, reservation, transfer receipt, usage/consumption, condition/durability/repair, crafting/salvage boundary, and history records.

PPIA-03 deepens the **human-facing Item/Equipment/Inventory experience** around those contracts; it does not replace them.

### MV-IA-F004 — Character Creation and Advancement

Controls Character-owned/equipped references, loadout implications, prerequisites/proficiencies, and Character-state boundaries. Equipping an Item never silently changes ownership or rewrites Character source Definitions.

### MV-IA-F005 — Campaign, Scene, and Session Builder

Controls Scene-local Assets, loot/reward placement, hidden existence, local labels/notes, launch snapshots, and Campaign-local authoring. Source Item Definitions remain immutable.

### MV-IA-F007 / combat and approval surfaces

Combat use must reference exact authorized Asset Instances, ammunition/charges, equipment state, reservations, and expected versions. Denied or failed-before-commit Actions cannot consume authoritative inventory.

### MV-IA-F020 — Permissions and Hidden Information

Authorization occurs before existence, counts, aggregate weight/value, container totals, search suggestions, loot previews, history, provenance, or diagnostics are computed. Hidden contents cannot leak through totals or empty/nonempty signals.

### MV-IA-F021 — Recovery and bounded offline use

Transfer/equip/consume/repair/craft mutations require idempotency and expected-version recovery. Offline private planning may exist, but authoritative inventory mutation requires revalidation and server-authoritative commit.

### PPIA-02 — Creature & NPC Experience

Creature/NPC equipment, carried inventory, loot, and Assets are linked Item/Asset references. PPIA-03 owns the item-side lifecycle; PPIA-02 owns creature/NPC presentation and placement context. Neither copies rule text or invents duplicate Item identities merely to make a creature stat block self-contained.

## 6. PPIA-01 routed Item obligations

PPIA-03 inherits these explicit unresolved/guardrail cases:

- **Taser:** two published source contexts exist. No automatic identity merge is allowed. PPIA-03 must present/author variant or conflict semantics explicitly; numerical balance routes to PPIA-11.
- **Seven source-unspecified energy-weapon capacity fields:** do not invent capacities merely to make reload/charge UI look complete. Unknown maximum/current semantics must remain distinguishable from zero, unlimited, or not-applicable.
- **Three ammo-reference-only names:** `Energy Sniper Rifle`, `Plasma Carbine`, and `Cryo Blaster` remain reference-only until a governed Definition exists. Do not create damage/range/weight/cost from the reference name.
- **Mechanical interpretation rows:** source-backed values remain distinct from owner-delegated recommendations. PPIA-03 may design how recommended mechanics are displayed/edited/reviewed, but may not relabel them as source facts.

## 7. Recovered R1 formal-deferral surface

The recovered 8E-008G-R1 register contributed **53 Item-classified structural candidates** to the PPIA-03 branch. These are not 53 missing Item Definitions. Heading-level review shows substantial cross-domain noise and supporting-rule material.

`PPIA-03_R1_DEFERRED_ITEM_ROUTING_v0.1.0.json` classifies all 53 candidates without canonical promotion:

- 23 supporting Item rule/catalog headings;
- 4 specific Item/loot candidates requiring source review;
- 10 vehicle/vehicle-system contexts routed to PPIA-04;
- 6 creature/body attack contexts routed to PPIA-02/PPIA-05;
- 6 headings requiring more source context before domain assignment;
- 4 GM/world/faction contexts routed outside PPIA-03.

This is source-accountability triage only. A structural heading never becomes an Asset Definition because its label sounds item-like.

## 8. Required Item experience distinctions

PPIA-03 must preserve all of the following:

1. **Reusable Item Definition** — governed source/version identity and intrinsic rules.
2. **Definition variant/configuration** — source-backed version/variant, compatible modification profile, or conflict alternative; not a live Asset Instance.
3. **Asset Instance** — Campaign-scoped owned/held object or explicitly tracked non-physical Asset.
4. **Ownership / custody / possession / control / access** — independent authority relationships.
5. **Location and containment** — Character, Scene, vehicle, shop, vault, evidence store, container, transit, or other governed location.
6. **Equipment assignment** — slot/readiness/hand/layer/station/attunement assignment; does not imply ownership.
7. **Quantity lot / stack / ledger representation** — compatible quantities with lineage; not universal fungibility.
8. **Runtime mutable state** — current charges/ammunition, durability/condition, damage, reservation, cooldown/use state where applicable.
9. **Identification / reveal state** — what a role/Character is authorized to know about identity, properties, value, provenance, curse/drawback, contents, or restrictions.
10. **Transaction and history** — acquisition, transfer, lending, trade, consume, split/merge, equip/unequip, repair, craft/salvage, destroy, and provenance lineage.

## 9. Initial context taxonomy

The specialized Item experience must support the same Asset through different role-safe contexts without changing source truth:

1. Library/reference browse and compare.
2. Item Inspector.
3. Character inventory and loadout.
4. Container/tree/encumbrance view.
5. Equipment and quick-access view.
6. Party/shared Assets and treasury.
7. Scene loot/reward/placed Assets.
8. Shop/trade/transfer/lending flow.
9. Combat/action/reload/consume flow.
10. Charges, ammunition, durability, repair, and maintenance.
11. Crafting/salvage reservation and lineage handoff.
12. GM hidden/identified/unidentified loot authoring.
13. Provenance/history/conflict/variant inspection.
14. Accessible list/table/nonvisual equivalents for every spatial or drag-oriented surface.

## 10. Foundation boundary and next substep

This inventory establishes source and design authority, cross-domain routing, and the state/identity problem space. It does **not** mutate raw CSVs, promote R1 candidates, implement runtime code, activate A2, or authorize release/deployment.

The next bounded PPIA-03 substep is to turn the foundation taxonomy into a machine-verifiable role/field/action projection matrix and concrete Item Inspector + inventory reference cases, including Taser conflict presentation, unspecified capacities, reference-only weapon names, nested hidden containers, stacks/splits, shared ownership, equipment, charges/durability, and transfer/recovery behavior.
