# PPIA-03 — Items, Equipment & Inventory Experience Specification v1.0.0

**Work item:** PPIA-03  
**Status:** IMPLEMENTATION-READY DESIGN SPECIFICATION  
**Owner:** John Brandon Turner  
**Primary repository:** `cybalicistjt-stack/multiversal-aioc`  
**Application runtime mutation authorized by this document:** No  
**STAGE-A-A2 activation authorized by this document:** No

## 1. Purpose

PPIA-03 defines the Item-, equipment-, Asset-, and inventory-facing experience that downstream implementation can build without re-deciding identity, authority, containment, equipment, quantity, mutable-state, permission, provenance, or recovery semantics.

It extends the already-approved Internal Alpha Asset model rather than replacing it. The governing runtime baseline remains **MV-IA-F008 — Inventory, Ownership, and Shared Assets**. The shared browse/inspect/compare/picker behavior remains **MV-IA-F002 — Universal Object Experience**. Permissions, hidden information, and recovery remain governed by **MV-IA-F020** and **MV-IA-F021**.

This specification is deliberately broader than a character-sheet equipment list. Multiversal Items include ordinary weapons and armor, ammunition, consumables, containers, tools, computers and software, EVA chassis and modules, living spellbooks, charge holders, symbiotes, cybernetics, materials, modifications, special devices, party/shared Assets, Scene loot, and Campaign-scoped instances whose live state differs from their reusable Definitions.

## 2. Authority and source basis

### 2.1 Structured content authority

PPIA-03 uses the later governed **8E-009 CSV-first registry** rather than the obsolete 487-object semantic-parse database.

The direct Item content surface contains **nine Item-domain CSV datasets / 5,389 governed rows**. Mixed-domain material/hazard sources and vehicle/mecha/spacecraft component sources are routed only where their object family actually belongs.

### 2.2 Retained source library

The retained Item source library contains **13 dedicated PDFs / 218 pages**, with exact SHA-256 evidence recorded in `PPIA-03_SOURCE_AND_DESIGN_INVENTORY.md`.

### 2.3 Recovered R1 evidence

Recovered 8E-008G-R1 evidence contributes **53 Item-classified structural candidates**, but those candidates are source-accountability headings rather than 53 automatic Item Definitions. The routing register preserves all 53 and explicitly separates supporting Item context, specific source-review candidates, vehicle contexts, creature/body contexts, unresolved contexts, and non-Item GM/world contexts.

### 2.4 Source-truth rule

A UI that looks complete is not evidence that the source was complete. Every relevant field can retain one of several epistemic/provenance states, including:

- source-backed fact;
- source-unspecified or absent;
- reference-only;
- explicit conflict;
- governed inference;
- owner-delegated recommendation;
- Campaign-local override/state;
- runtime state.

These states must not be flattened into a single undifferentiated value.

## 3. Core object and state model

PPIA-03 uses ten distinct layers. Implementations may package them differently internally, but must preserve their semantics.

### 3.1 Reusable Item Definition

Owns stable source identity, version, intrinsic mechanics, provenance, presentation profile, and compatible capabilities. It does not own Campaign possession, current charges, current durability, container location, or equipped state.

### 3.2 Definition variant or configuration

Represents source-backed variants, version alternatives, compatible modification profiles, or conflict alternatives. A variant/configuration does not become a live Asset merely by being selected or compared.

### 3.3 Asset Instance

Represents one Campaign-scoped owned/held/tracked occurrence of a governed Definition or explicitly tracked non-physical Asset. It has its own stable instance identity and lineage anchor.

### 3.4 Authority relations

The system represents separately:

- ownership interest;
- custody;
- physical possession;
- control;
- access/usage grant.

No one relation silently implies the others.

### 3.5 Location and containment

An Asset may be located on a Character, in a Scene, in a vehicle, in a shop, in a vault, in an evidence store, in transit, or within another governed container. Containment is acyclic and permission-safe.

### 3.6 Equipment assignment

Equipment state includes slots, hands, layers, readiness, quick access, stations, installations, attunement, and bonds where the profile allows them. Equipment assignment never silently transfers ownership.

### 3.7 Quantity lot / stack / ledger representation

Quantity-bearing Assets preserve units, lot identity, stack compatibility, ownership, restrictions, and provenance lineage. Visual similarity does not imply fungibility.

### 3.8 Mutable runtime Item state

Where supported by the profile, current state can include ammunition, charges, doses, durability, condition, damage, reservations, maintenance, disabled state, and consumption state.

**Unknown is not zero.** A source-unspecified maximum capacity is not zero, empty, unlimited, or inferred merely to make a UI complete.

### 3.9 Identification / reveal / knowledge state

The authoritative Asset can have true identity/properties/value/drawbacks/contents/provenance while a role knows only a subset. Knowledge projection never rewrites underlying truth.

### 3.10 Transaction, lineage, and history

Acquisition, transfer, lending, trade, split, merge, consume, equip, repair, craft, salvage, destroy, reveal, and provenance history remain attributable to accepted commands/events.

## 4. Presentation profiles

The experience must support profile-driven presentation without creating new identities or authority. Minimum profiles are:

1. weapon;
2. armor/protective equipment;
3. consumable;
4. tool/general device;
5. ammunition/resource;
6. container/storage;
7. magic/special item;
8. computer/software;
9. EVA frame/module;
10. material/crafting resource;
11. living/sentient item;
12. symbiote/cybernetic implant;
13. modification/attachment;
14. currency/treasury;
15. loot bundle/shop offer.

A profile changes field emphasis, section order, actions, and specialized state—not stable identity and not permission.

## 5. Item Inspector information architecture

The implementation-ready Inspector matrix defines fourteen field groups:

1. identity and Definition status;
2. intrinsic mechanics;
3. Asset Instance authority;
4. location and containment;
5. quantity and stacks;
6. equipment and readiness;
7. charges, ammunition, and uses;
8. condition, durability, and maintenance;
9. identification and knowledge;
10. economy, trade, and transfer;
11. crafting, repair, and salvage;
12. variants, modifications, and relationships;
13. source provenance and conflict;
14. history and recovery.

### 5.1 Definition versus instance labeling

Whenever a screen includes both source Definition and Asset Instance data, the distinction must be explicit. A user should be able to tell, for example, that `Laser Assault Rifle` has a governed 40-charge standard capacity while their specific rifle currently has 17 charges.

### 5.2 Missing and unknown values

The Inspector must render source-unspecified, not applicable, unknown, conflicted, reference-only, recommended, zero, empty, depleted, destroyed, and hidden as distinct states. It must not normalize them into a single dash or numeric default when the difference affects rules or user decisions.

### 5.3 Linked governed objects

Attachments, modules, software, ammunition, Abilities, Effects, Conditions, hosts, variants, replacements, and related records should open through stable references where such governed objects exist rather than copying mutable or source-sensitive text into every Item instance.

## 6. Core Item/Inventory contexts

The same Item or Asset can appear in multiple contexts without changing source truth:

- Library/reference browse and compare;
- Item Inspector;
- Character inventory;
- container/tree/encumbrance view;
- equipment/loadout/quick-access view;
- party/shared Assets and treasury;
- Scene loot/reward/placed Assets;
- shop/purchase/trade/transfer/lending;
- combat use/reload/recharge/consume;
- condition/durability/repair/maintenance;
- crafting/modification/salvage;
- GM identification/reveal;
- provenance/history/conflict/recovery;
- accessible nonvisual equivalents.

## 7. Governed workflow set

`PPIA-03_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json` defines twelve implementation-ready workflows.

### IT-WF-001 — Library / Item Inspector reference flow

Read-only browse, inspect, provenance, relationship traversal, and comparison. Any selection handed to another workflow is provisional and revalidated by the destination.

### IT-WF-002 — Character inventory acquisition, movement, and containment

Moves exact Asset Instances/lots between authorized locations/containers without implicitly changing ownership. Capacity, compatibility, containment cycles, and hidden aggregates are checked before commit.

### IT-WF-003 — Equipment, loadout, installation, and attunement

Assigns Assets to hands, slots, layers, hosts, stations, quick access, installations, attunements, or bonds. Equipment never becomes an ownership transfer shortcut.

### IT-WF-004 — Quantity, stack, split, and merge

Splits or merges only compatible authorized lots and preserves lineage, ownership, provenance, and restrictions.

### IT-WF-005 — Party/shared Asset lending, transfer, and return

Makes relation-by-relation changes explicit. A loan can grant custody/access/use while ownership remains unchanged.

### IT-WF-006 — GM Scene loot, rewards, hidden Assets, and identification

Keeps hidden loot absent from unauthorized projections and supports discovery/identification as authoritative knowledge/reveal events rather than client-side unhide.

### IT-WF-007 — Shop, purchase, trade, and acquisition

Distinguishes offer/cart/proposal from accepted transaction. Asset and currency/consideration changes commit atomically according to the governing economy profile.

### IT-WF-008 — Combat use, ammunition, charges, reload, and consumption

Uses the authoritative Action/Session pipeline. Denied or failed-before-commit Actions cannot consume ammunition, charges, or consumables.

### IT-WF-009 — Condition, durability, maintenance, and repair

Uses profile-specific condition semantics. Zero durability does not universally mean deletion, and repair preserves history.

### IT-WF-010 — Crafting, modification, salvage, and material reservation

Reserves exact inputs, prevents double-spend, and creates outputs only on successful atomic completion with lineage.

### IT-WF-011 — Special Assets

Handles living items, symbiotes, software, cybernetics, EVA/modules, and similar profiles without forcing them into ordinary physical-bag semantics. Vehicle and host-biology consequences route to PPIA-04/PPIA-05.

### IT-WF-012 — Conflict, provenance, history, export, and reconnect

Preserves exact source/version identity, prohibits same-name auto-merge, performs operation-status lookup after ambiguous results, and filters history/provenance before export.

## 8. Cross-workflow handoff rules

Ten explicit handoff contracts govern movement between reference, inventory, equipment, Scene loot, transaction, combat, repair, crafting, special-Asset, and recovery workflows.

Every handoff carries stable IDs and current context rather than assuming the destination inherits authority. The destination reauthorizes and validates current versions/state before any authoritative mutation.

Key examples:

- Inspector selection to inventory/equipment/Scene/shop remains provisional.
- Reveal and acquisition are separate unless an owning workflow explicitly combines them atomically.
- A shop/cart proposal changes no Asset ownership until transaction commit.
- Equipment receives an Asset Instance reference but not ownership-mutation authority.
- Combat receives current equipment/resource state but revalidates before use.
- Crafting outputs enter inventory only after successful work-order commit.
- Recovery hands the original operation ID back to the original mutation owner rather than inventing a second operation.

## 9. Permissions and hidden information

Authorization occurs before:

- result existence;
- search ranking and suggestions;
- facets and counts;
- stack/quantity totals;
- aggregate weight/value;
- container occupancy or child counts;
- loot previews;
- equipment lists;
- transaction offers/history;
- provenance and diagnostics;
- exports;
- AI/service context.

A Player cannot infer a hidden object because a backpack suddenly weighs more, a container says `2 hidden items`, a shop count changes, a party total includes it, or a compare/provenance target appears.

GM authority applies only within authorized Campaign scope. Owner/Admin status does not automatically grant Player-private or unrelated Campaign-private content. Assistant GM authority is delegation-scoped. AI/service actors receive only the minimum authorized projection for their operation.

## 10. Ownership, custody, possession, control, and access

The UI and command contracts must make these relations understandable without forcing users to understand database internals.

Examples:

- a jointly owned party scanner can be physically carried by one Character;
- a GM-controlled loaner weapon can be equipped by a Player Character without changing ownership;
- a sentient item can be owned but have independent action/autonomy rules;
- software may be licensed/access-controlled and installed without behaving like a physical carried object;
- a symbiote can be bonded to a host while ownership/control remains governed separately.

Transfer dialogs show exactly which relationships will change before confirmation.

## 11. Containers and nesting

Containers support governed capacity and compatibility rules where defined. Nested containers form an acyclic graph.

The server filters unauthorized children before producing child lists, counts, weights, values, occupancy, capacity summaries, search indexes, exports, diagnostics, or AI context.

Every tree/drag experience has a semantic list/tree alternative and commands such as **Move to…**, **Remove from…**, **Equip**, or **Store**.

## 12. Quantities, stacks, currency, and lots

Stacking is conditional rather than universal. Merge compatibility can include:

- exact Definition/version;
- state and quality;
- ownership interests;
- restrictions;
- provenance/lot policy;
- profile-specific fields.

Split/merge creates attributable lineage. Currency behavior is rules-profile bound and must not assume one universal fungibility or denomination model.

## 13. Equipment, readiness, installations, and modifications

Equipment state can include hands, layers, slots, readiness, quick access, stations, hardpoints, module installation, attunement, or bond relationships.

Requirements and proficiency can warn, block, or modify use according to the governing rules profile; PPIA-03 does not invent a universal penalty.

Installing an EVA module, software package, cybernetic component, or special attachment changes its relationship/state according to its profile and does not automatically transfer ownership.

## 14. Charges, ammunition, uses, and consumption

Current amount and maximum capacity are separate values.

The system must preserve three important source cases:

1. **Laser Assault Rifle** has explicit governed 40 standard / 60 extended / 80 high-capacity charge values and can therefore display a known maximum when the selected capacity configuration is known.
2. **Seven energy-weapon records** have source-unspecified capacity fields and cannot receive fabricated maximums just to enable a reload UI.
3. **Energy Sniper Rifle, Plasma Carbine, and Cryo Blaster** are ammo-reference-only names and cannot become full selectable weapon Definitions merely because capacity references exist.

Use/reload/recharge/consume commits atomically with its owning action or Asset command. A failed-before-commit operation spends nothing.

## 15. Taser conflict handling

The governed corpus contains multiple published `Taser` contexts with differing mechanics and provenance. Same display name is insufficient evidence of one identity.

The experience must:

- present exact source/version/context provenance;
- distinguish source-backed fields from inference/recommendation;
- allow authorized field-level comparison;
- prohibit silent auto-merge;
- require an exact governed identity/version or explicit later resolution before a caller that needs one Definition can commit.

Numerical balance conclusions route to PPIA-11.

## 16. Identification and reveal

Identification is a knowledge/reveal concern, not a rewrite of true Item state.

A Campaign can support stages such as:

- hidden/unrevealed existence;
- discovered but generically described;
- partially identified;
- fully identified;
- provenance or drawback still unknown.

Only fields authorized at the current knowledge state are serialized. An identification event changes future authorized projection.

## 17. Durability, damage, repair, and maintenance

Durability and condition are profile-driven. An implementation must not assume every Item has hit points or every zero-durability Item disappears.

Damage, disabled/broken state, maintenance, repair requirements, repair cost, and destruction behavior follow governed profile/rules data. Repair changes current state and appends history; it does not erase prior damage or provenance.

## 18. Crafting, modification, and salvage

Crafting uses explicit work orders/reservations so ingredients/material lots cannot be double-spent.

Before commit:

- inputs remain identifiable and reserved;
- cancellation can release reservations;
- no outputs are authoritative.

On successful commit:

- exact inputs are consumed/transformed as governed;
- outputs/byproducts are created;
- lineage connects outputs to contributing inputs and work order.

PPIA-07 owns the Rune construction system where rune-specific construction/enchantment rules are required.

## 19. Special Asset profiles

### Living/sentient items

A living item can have personality, autonomy, bonding, progression, capabilities, durability, and repair while remaining an Asset rather than silently becoming a Character.

### Symbiotes and cybernetics

PPIA-03 owns Asset/bond/equipment/ownership/provenance behavior. Host biology, morphology, transformations, and species/form consequences route to PPIA-05.

### EVA and modular equipment

Suit chassis, loose modules, installed modules, interfaces, and consumables remain distinct identities. Installation and hardpoint compatibility do not imply ownership changes.

### Computers and software

Software-like Assets are not forced into physical weight/container semantics. Installation, license/access, compatibility, and historical usage can be tracked separately.

### Vehicle/mecha/starship components

Personal Item behavior may provide shared primitives, but vehicle crew/station/component/damage/power/cargo semantics route to PPIA-04.

## 20. Recovery, concurrency, and interruption

Every authoritative Asset mutation uses:

- stable client operation ID;
- expected version or equivalent concurrency check;
- durable accepted/rejected status;
- idempotent retry behavior;
- role-safe recovery receipt.

If the client loses the response after submitting a transfer, purchase, split, consume, repair, crafting completion, or similar mutation, it first queries operation/command status using the same identity. It does not resubmit a new operation and hope the first one failed.

Reconnect revalidates identity, Campaign, role, permissions, entitlements, pack/version state, and relevant lifecycle before restoring sensitive projections. Cached hidden or revoked fields never become authority.

No broad offline authoritative Item mutation is authorized for Internal Alpha. Offline planning/drafts can remain nonauthoritative and must revalidate on reconnect.

## 21. Responsive and accessibility behavior

### Large screens

May use two-pane inventory + Inspector, persistent equipment summaries, and side-by-side comparison where helpful.

### Medium screens

Use primary list/table with detail drawer/sheet and stacked comparison where needed.

### Compact/mobile

Use one semantic column, large touch targets, full-height or bottom sheets, sticky critical status/actions, and no hover-only interactions.

### Keyboard and non-drag operation

Every move, reorder, equip, install, split, merge, transfer, and container action has an explicit command path. Drag-and-drop may accelerate a workflow but is never the only way to complete it.

### Screen reader

Use semantic lists/trees, labeled quantities/units/ownership/equipment/condition fields, explicit source/conflict/unknown states, and filtered counts only from the authorized projection.

### High zoom and reduced motion

Core actions/status survive 200%+ text reflow. Tables convert to labeled records where necessary. Motion is never required to understand transfer, equip, consume, reveal, or error states.

## 22. Reference acceptance corpus

`PPIA-03_REFERENCE_CASES_v0.1.0.json` contains **18 reference cases**:

- Spear inspect/equip;
- Laser Assault Rifle capacities;
- Taser source-context conflict;
- seven source-unspecified energy capacities;
- three reference-only weapon names;
- Backpack hidden nested container;
- Potion of Healing atomic use;
- Living Spellbook autonomy/bond;
- Regenera symbiote;
- modular EVA equipment;
- stack split/merge lineage;
- shared party lending;
- equipment without ownership transfer;
- hidden/unidentified Scene loot;
- durability/repair history;
- ambiguous transfer/network result;
- crafting reservation/cancellation;
- software-like Asset installation.

Synthetic QA cases are explicitly noncanonical and exist only to prove design/permission/recovery behavior.

## 23. Cross-domain boundaries

PPIA-03 intentionally routes rather than invents:

- vehicle/mecha/starship system semantics → **PPIA-04**;
- species/form/host biology → **PPIA-05**;
- rune construction/enchantment rules → **PPIA-07**;
- Campaign/Scene/Session authoring depth → **PPIA-08**;
- faction/social consequences → **PPIA-10**;
- numerical encounter/item balance → **PPIA-11**;
- world-specific Item extensions → **PPIA-12**.

## 24. Implementation handoff

An implementation team can now build PPIA-03 behavior from four governed layers:

1. source/design inventory and R1 routing;
2. Item experience taxonomy;
3. Inspector/projection/action matrix plus 18 reference cases;
4. integrated workflow/handoff matrix.

The implementation must reuse shared Stage A/Internal Alpha systems rather than create duplicate permission, search, picker, history, recovery, or source/provenance logic.

No production runtime code is authorized by this PPIA document itself. Application implementation proceeds only through the separately governed Stage A work orders.

## 25. Completion boundary

PPIA-03 design completion requires deterministic evidence that the packet covers:

- Definition/instance/state separation;
- ownership/custody/possession/control/access;
- containment and hidden aggregates;
- quantities/stacks/lineage;
- equipment/readiness/install/attune;
- charges/ammunition/consumption and source-unspecified capacity;
- identification/reveal;
- GM loot and Scene handoff;
- transfer/trade/shared Assets;
- durability/repair;
- crafting/salvage;
- special Assets;
- provenance/conflict/reference-only behavior;
- responsive/accessibility equivalents;
- idempotency/concurrency/recovery;
- source-grounded and synthetic reference acceptance cases.

The acceptance/traceability matrix is the machine-readable completion contract for those requirements. PPIA-03 completion does not complete PPIA-04 or later tranches, activate A2, mutate application runtime, authorize release/deployment, or promote unsupported content.
