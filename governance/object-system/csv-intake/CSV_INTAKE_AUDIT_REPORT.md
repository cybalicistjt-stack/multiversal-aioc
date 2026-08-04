# Governed CSV Intake Audit

**Workstream:** 8E-009L1 through 8E-009L3  
**Status:** STRUCTURAL AUDIT COMPLETE; SOURCE ROUTING AND INITIAL MAPPING CONTRACTS DEFINED  
**Archive:** `Csv.zip`

## Verified archive structure

- 20 CSV files
- 19,199 data rows
- 50,376,355 uncompressed bytes
- zero exact duplicate full rows
- all CSV data rows match their declared header width

## Completed follow-on work

- every CSV is routed to its governed primary domain and intended template or future registry;
- all 11 existing item templates are assessed against the CSV corpus;
- nine required item-template gaps are recorded;
- initial deterministic mapping contracts exist for melee weapons, ranged/firearm/energy weapon classification, and computers;
- rows remain staging evidence and are not treated as canonical objects.

## Required item-template gaps

1. ordinary ranged weapon;
2. energy weapon;
3. ammunition and power-cell object;
4. implant;
5. modular upgrade;
6. mundane or skill tool;
7. general device;
8. deployable trap;
9. software/program.

## Structural risks requiring governed handling

- ranged weapons overlap with `weapons_and_ammo.csv`;
- magitech rows must retain a physical template separate from discipline overlays;
- EVA suits and modules must be split into host and modification records;
- symbiotes and cybernetics must not share one primary template;
- bases/facilities/materials/homesteads must be routed into separate object families;
- hazards must be separated from deployable trap items;
- mecha and spacecraft components require vehicle-family registries;
- structurally consistent rows may still contain semantic, identity, category, source-reference, or mixed-domain conflicts requiring governed mapping and verification.

## Promotion boundary

This audit and routing work verifies structure and intended destinations only. It does not certify semantic accuracy, source fidelity, completeness, canonical identity, runtime readiness, promotion, or owner approval.

## Next executable action

Define the nine missing item-template or subtype contracts, then complete mapping contracts for general items, EVA suits/modules, living spellbooks/charge holders, and symbiotes/cybernetics before cross-file identity reconciliation.
