# Current Game-Object Source Authority

**Authority ID:** `MV-OBJECT-SOURCE-AUTHORITY-2026-09-17`  
**Status:** OWNER AUTHORIZED — CURRENT SOURCE POPULATION AUTHORITY  
**Effective:** 2026-09-17

## Purpose

This is the population-selection authority for Multiversal asset-like game objects used by Item/Object readiness work.

It exists because older intake, P1, CCTI and FIAA artifacts continued to expose obsolete population counts after later all-genres content expansion. Those artifacts remain valuable evidence, but they no longer select the working object population.

This file distinguishes **current source population** from **runtime/canonical promotion**. A record can be a current source record without yet being a promoted or GAME_READY Definition.

## Mandatory selection rule

For Item/Object corpus work:

1. Load `CURRENT_GAME_OBJECT_SOURCE_AUTHORITY.json`.
2. Use only its `current_primary_sources` as the primary source population.
3. Add listed supplemental sources when their routed domains are in scope.
4. Route cross-domain sources row-by-row.
5. Treat every older/alternate same-domain dataset not listed as current as **HISTORICAL_REFERENCE_ONLY** by default.
6. Never substitute an old P1/CCTI/FIAA count merely because its ledger is easier to access.

Historical material may still supply provenance, conflict evidence, lineage, stable identifiers and validation evidence. It may not replace the current population.

## Current totals

- Primary current object-source rows: **16,133**
- Known current supplemental object-source rows: **2,427**
- Known direct current object-source rows before cross-file identity reconciliation: **18,560**
- Additional cultural-ephemera rows requiring cross-domain routing: **5,000**
- Current melee weapon source population: **1,000**
- Current ranged weapon source population: **1,000**

These are **source-row counts**, not deduplicated Definition counts.

## Weapon correction

The earlier weapon files are now seed/reference inputs:

- `expanded_melee_weapons_all_genres.csv` — 327 rows → superseded as population authority.
- `expanded_ranged_weapons_catalog.csv` — 230 rows → superseded as population authority.

Their rows are preserved inside:

- `expanded_melee_weapons_canonical_multigenre_v2.csv` — 1,000 rows = 327 preserved seed + 673 owner-authorized authored expansion.
- `expanded_ranged_weapons_canonical_multigenre_v2.csv` — 1,000 rows = 230 preserved seed + 770 owner-authorized authored expansion.

Both v2 catalogs use the mature **31-genre matrix** already established by the expanded computer/object catalogs. New rows are explicitly labeled `OWNER_AUTHORIZED_AUTHORED_EXPANSION`. Existing source mechanics are not relabeled or overwritten.

## Explicitly obsolete as population totals

Do not use any of the following as the current Item/Object population:

- 5,389
- 5,353
- 5,346
- 5,443
- melee = 327
- ranged = 230
- 19,199

Those figures remain historical accounting for their specific prior programs.

## Source hierarchy for object work

1. This authority manifest and its exact current file IDs/hashes.
2. Latest governed owner corrections/adoption overlays applicable to those current records.
3. Current promoted Definition/runtime registries, where already reconciled to the current source records.
4. Earlier P1/CCTI/FIAA/CSV-intake artifacts for provenance, mappings, validation evidence and conflict history.
5. Historical PDFs/zips only for explicit provenance/conflict recovery.

If a current source record conflicts with an older derived record, preserve the conflict and resolve it through governed precedence; never silently discard the current row.

## Cross-domain caveat

`multiversal_cultural_ephemera_5000.csv` is current content but is **not** 5,000 Item Definitions. It includes services, facilities, media and other world content. It must be routed row-by-row, and Item-like entries may then join Item/Object readiness.

## Later additions

`multiversal_books_catalog_2400.csv` is a later additive current object source and is not part of the August-4 15-catalog expansion total.

The two small fruit/nut CSVs are retained as current supplemental object sources until a later food/ingredient authority supersedes them. Their batch numbering gap is explicit and must not be interpreted as complete food coverage.

## Historical disposition rule

Any earlier Item/Object CSV, archive, projection, private ledger or derivative not explicitly listed as current by `CURRENT_GAME_OBJECT_SOURCE_AUTHORITY.json` is **HISTORICAL_REFERENCE_ONLY** for population selection.

Retirement does not erase history. It removes authority to steer the working corpus.

## FIAA restart rule

The next FIAA corpus audit must rebuild its subject roster from this authority manifest. Existing FIAA/P1/CCTI row-level work can be mapped forward where identities/provenance reconcile, but old totals may not define tranche sizes.

The first FIAA step after this cutover is therefore **current-source identity reconciliation**, not “Ranged 230.”
