# Repository Solidity — Legacy PR Dispositions

**Date:** 2026-08-13  
**Purpose:** classify open historical pull requests against current canonical `main` before any salvage, closure, or Stage A activation.

## Rules

- Current canonical `main`, later verified program evidence, and current source/provenance contracts outrank older open pull requests.
- A green partial validator does not make an old pull request merge-ready when another required validator on the same head failed.
- Historical source/provenance evidence is preserved even when the old pull request is closed or superseded.
- Old branches are not merged wholesale into current `main`; useful material is reconciled onto a fresh current-main basis.

## PR #48 — visual Laser Assault Rifle extraction

**Head:** `01c8afc3134da9c67844e67c3409c2ac7ed89cc5`  
**Disposition:** `SUPERSEDED_DEFECTIVE_SALVAGE_SOURCE`  
**Merge as-is:** **NO**

### Evidence retained

- The dedicated `Validate Visual Firearm Example` workflow passed on the exact PR head.
- The extraction preserves rendered-page visual evidence for Laser Assault Rifle identity/statistics, capacity evidence, Burst Fire context, and unresolved rules-bearing fields.
- Later canonical PPIA-03 reference case `PPIA03-RC-002` independently corroborates the Laser Assault Rifle identity and governed CSV values, including 1d10 Radiant damage, 80/320 ft range, 8 lb weight, 1200 credits, and 40/60/80 charge capacities.

### Defects preventing wholesale merge

- `Validate Item Example Selections` failed on the same exact head.
- The selection artifact uses `selectionState = visually-verified-and-extracted`, while the changed validator requires `visually-verified-partial-extraction`.
- Page references are internally inconsistent: the selection records source page 6 and supporting pages 2/5, while the extraction attributes capacity to pages 4/5 and Burst Fire to page 2.
- The branch predates later canonical PPIA/source-conversion authority.

### Salvage rule

Preserve PR #48 and its branch as provenance history. If the page-level visual evidence is needed downstream, re-extract/reconcile it on a fresh current-main branch, use one internally consistent partial/certification state, cite all rendered pages actually carrying the retained fields, and validate against current PPIA/content-provenance authority. Do not represent the old PR as completed or canonical.

## PR #34 — weapons/ammunition/explosives domain review

**Head:** `d1fcfcd9909c85090027dc8e5d35a29c6d82bca5`  
**Disposition:** `HISTORICAL_TAXONOMY_SALVAGE_SOURCE`  
**Merge as-is:** **NO**

### Evidence retained

The branch contains an early weapons-domain classification contract, review fixture, pilot coverage record, validator, and workflow. Its classification snapshot covers 596 sections across weapon profiles, special rules, ammunition, explosives, fantasy battlegear, improvised armour, and modern-crime armour.

### Why it is not current implementation authority

Later 8E-009 work completed the broader CSV-first conversion/reconciliation/promotion program and current canonical object/content structures are newer authority. The old classification contract may still contain useful taxonomy/provenance evidence but must be compared field-by-field only when a current content question requires it.

### Salvage rule

Keep PR #34/branch as historical taxonomy evidence. Do not merge wholesale. Reuse only unique classifications or source mappings that are absent from later canonical conversion artifacts, and carry them forward through current validators/provenance rules.

## Current consequence

Neither PR #34 nor PR #48 is a blocker for STAGE-A-A2. They are retained historical/salvage inputs. PR #48 may be closed as superseded after this disposition record is durable; PR #34 remains available for targeted taxonomy salvage review without being treated as active current work.
