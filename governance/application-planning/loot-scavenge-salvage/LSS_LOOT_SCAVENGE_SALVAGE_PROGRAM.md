# LSS — Loot, Scavenge & Salvage Program

**Program ID:** LSS  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL  
**Activation:** after MIB-15  
**Successor:** LNG-01  
**Owner and final authority:** John Brandon Turner

## Purpose

LSS makes recoverable physical things composable, inspectable, dismantlable, repairable and reusable without creating a second inventory, crafting, vehicle/base, economy, Project or creature-harvest ledger.

The owner-provided `Looting_Salvaging_Scavenging.mht` is a design-intent source, not a direct implementation specification. Current Multiversal owner domains are stronger and govern the implementation.

## Core jurisdiction

- **Loot**: acquire/transfer already-existing Assets or explicit authored drop outputs.
- **Scavenge**: search an authored location/opportunity for recoverable resources or objects.
- **Salvage**: inspect and partially or fully dismantle an object/Asset/wreck into authored components, subassemblies or materials.

ICF-07 remains the authority for biological creature harvesting/butchery. LSS owns object/Asset decomposition after a recoverable object exists.

## Tranches

1. **LSS-01 — Source Inventory, Existing-System Crosswalk & Authority Map**  
   Reconcile source intent against D17, MIB-03, MIB-12, MIB-13, MIB-14, APW, CEL and ICF; enumerate real gaps and preserve owner boundaries.

2. **LSS-02 — Recoverable Object, Component, Assembly & Provenance Schema**  
   Define salvage profiles, recoverable slots, components, subassemblies, parent/child assembly graphs, critical/noncritical parts, depletion and lineage references.

3. **LSS-03 — Condition, Quality, Grade, Rarity & Compatibility Grammar**  
   Separate instance condition, manufacture/functional quality, definition rarity and compatibility. Reuse D17/shared-asset condition/history rather than inventing a parallel damage model.

4. **LSS-04 — Loot Acquisition & Transfer Foundation**  
   Govern ordinary loot, containers, caches, defeated-owner possessions and explicit drop-table outputs with version-safe ownership/permission checks and duplication-safe transfer.

5. **LSS-05 — Scavenge Zones, Search, Concentration & Opportunity Engine**  
   Define World-linked scavenging opportunities, access, expertise, tools, hazards, resource concentration/depletion and authored search outcomes.

6. **LSS-06 — Salvage, Disassembly & Component Extraction Engine**  
   Implement inspect → select target → validate requirements → reserve source → resolve extraction → create D17 outputs → update/finalize source. Support partial stripping, damaged extraction, failed extraction and total teardown.

7. **LSS-07 — Component Family Taxonomy & Decomposition Profile Library**  
   Build reusable governed families for weapons, armor, tools, electronics, machinery, vehicles, mecha, ships, bases, magical devices, constructs and other appropriate objects without asserting universal anatomy.

8. **LSS-08 — Repair, Refurbishment, Cannibalization, Substitution & Reassembly**  
   Connect salvaged components to MIB-12 repair/crafting and MIB-14 compatibility. Support donor parts, substitutions, combining damaged assemblies, refurbishment, installation and leftovers with conservation-safe receipts.

9. **LSS-09 — Economy, Projects, Hazards, Legality & Cozy Integration**  
   Connect salvage to MIB-13 value/markets, APW Projects, MIB-14 workshops/storage, CEL restoration/business loops, and governed hazardous/restricted-material rules.

10. **LSS-10 — Content Packs, Search, Workbench, Balance & Golden Proof**  
    Deliver searchable component/decomposition libraries, reverse lookup (“what uses this?” / “what can I recover?”), provenance inspection, fixtures and a wreck → extract → repair → reuse golden scenario.

## Program-wide invariants

- D17 remains Asset/inventory truth.
- MIB-12 remains crafting/repair transformation authority.
- MIB-14 remains vehicle/platform/base/component compatibility authority.
- MIB-13 remains economy truth.
- ICF-07 remains biological creature-harvest authority.
- No universal salvage yield, condition-upgrade formula or rarity conversion may be inferred.
- No output exists until durable owner-domain receipt evidence exists.
- Partial salvage must not implicitly destroy unrecovered components.
- Repeated/lost-response recovery must not duplicate outputs or source depletion.
- AI may suggest plans but has no mechanical/canonical authority.
