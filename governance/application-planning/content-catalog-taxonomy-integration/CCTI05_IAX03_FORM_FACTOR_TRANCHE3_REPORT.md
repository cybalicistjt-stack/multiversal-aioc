# CCTI Write Phase — Tranche 3: Item IAX-03 Form-Factor Candidate Projection

**Date:** 2026-08-17  
**Status:** candidate sidecars produced; source masters unchanged; canonical adoption disabled

## Axis authority

Exact Item Taxonomy v0.12.0 defines `IAX-03 form_factor` as a **multi-select** axis with **21 controlled values**. Unknown form remains unresolved; `generic_unspecified` is not used as a blanket substitute for missing evidence.

## Result

All **5,389 Item-corpus rows** have an explicit IAX-03 disposition:

- **3,487** rows: high-confidence candidate set only.
- **1,648** rows: one or more medium-confidence/review-required form candidates.
- **218** rows: explicitly unresolved because structured evidence did not support a safe form-factor assignment.
- **36** `Weapons_Ammo.csv` legacy/reference-only rows: not applicable.
- silently unaccounted rows: **0**.

The 5,353 current Item Definition rows therefore contain **5,135** rows with at least one form-factor candidate plus **218** explicit unresolved rows.

Candidate assertions: **7,642** total:
- high-confidence assertions: **5,938**
- medium-confidence assertions: **1,704**
- low-confidence assertions: **0**

Value distribution:
- `handheld`: 1,212
- `document_tome_media`: 914
- `module_board`: 871
- `companion_entity`: 752
- `weapon_form`: 676
- `implant_internal`: 561
- `tool_instrument`: 469
- `substance_dose`: 409
- `worn`: 355
- `bonded_external`: 343
- `software_virtual`: 267
- `terminal_console`: 238
- `fixed_installation`: 229
- `deployable`: 95
- `cartridge_cell_canister`: 67
- `garment_suit`: 49
- `kit_package`: 48
- `container`: 47
- `structure`: 39
- `projectile_ammunition`: 1

## Conservative form semantics

- Weapon catalogs receive `weapon_form`; `handheld`/`worn` is added only from explicit Hands evidence.
- Computers use current `Form_Factor` and `Record_Type` evidence to distinguish software/virtual, module/board, terminal/console, fixed installation, deployable, handheld/worn and companion-entity forms.
- EVA suits distinguish garment/suit chassis, modules/interfaces, customization kits and evidence-backed support-equipment forms.
- Living Spellbooks preserve document/tome/media plus companion-entity form; Magic Charge Holders use explicit delivery-form evidence such as scroll/tome, wand/staff/orb, wearable, cell/canister, substance or kit.
- Symbiote/Cybernetic host-integrated definitions use implant/internal, with bonded-external or weapon form added only where supported; maintenance/bonding/surgical support items are classified separately.
- General Items and Magitech use explicit category/subcategory/name form evidence. Rows with functional/contextual evidence but no safe physical/virtual form remain unresolved rather than being coerced.

The **218 unresolved rows** are confined to `Items.csv` (148) and `Magitech_Items.csv` (70). They remain explicit review work rather than receiving invented form factors.

## Validation

Deterministic checks passed:

- exact axis ID/cardinality: `IAX-03 form_factor`, multi;
- controlled-value membership: 21 exact v0.12.0 values, zero foreign IDs;
- source row accounting: 5,389/5,389;
- current Definition accounting: 5,353/5,353 candidate-or-explicit-unresolved;
- reference-only accounting: 36/36;
- duplicate same-value assertions per source row: 0;
- source/master mutation flags: false for every assertion;
- canonical adoption state: `CANDIDATE_SIDECAR_NOT_ENABLED`.

Private assertion sidecar SHA-256: `638d8e4246054496ec2e7a12307aaffdecd06d7eed01dc9ffaa6708f1a2cc0c0`  
Private 5,389-row summary SHA-256: `f66a20cb6d5ba16129a0c7163ff9648f4cdd8341b17d667a3cd4e0d9e2257c83`  
Rule-usage manifest SHA-256: `07c71c3686a3f09e12290eac67c967f2b555a5123ee31da4aba9485116c0bd65`  
Baseline SHA-256: `9382b54d39573341695729b3115889a46372ee629762381ec19e5d8d8b4e6683`

## Private tranche artifact

`CCTI_Item_Taxonomy_Tranche3_IAX03_20260817.zip`  
SHA-256: `312fe4f8f442279d06c6299271ce134d4f60a7c0b8fb61a3da6994e3fef31202`

## Exact next content operation

Proceed to **IAX-04 — use_relation** as another bounded multi-select candidate tranche. IAX-02 and IAX-03 unresolved states remain explicit review work and do not block independent axes. Mechanics reauthoring remains outside taxonomy projection.
