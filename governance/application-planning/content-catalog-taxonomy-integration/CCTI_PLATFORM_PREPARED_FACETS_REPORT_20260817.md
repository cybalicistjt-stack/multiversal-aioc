# CCTI Platform Prepared Facets — Operating Medium, Mobility Method, Functional Role

**Date:** 2026-08-17  
**Status:** candidate dispositions complete from exact Platform v0.11.0 preparation; not enabled

This tranche preserves the exact prepared row-level crosswalk without forcing missing values. All 5,628 rows have an explicit disposition for each of the three facets.

## Operating Medium

- 959 exact-controlled rows;
- 2,035 proposed/review-required candidate rows;
- 2,364 host/record-dependent rows with no assignment;
- 270 explicit unresolved rows;
- 4,664 candidate assertions across 2,994 rows.

## Mobility Method

- 1,485 proposed/review-required candidate rows;
- 991 host/record-dependent rows with no assignment;
- 841 explicit unresolved rows;
- 2,311 rows explicitly remain `NOT_MAPPED_FROM_CURRENT_FIELD` in the preparation package, primarily the Spacecraft corpus;
- 2,640 candidate assertions across 1,485 rows.

The 2,311 unprojected rows are not treated as N/A or silently guessed. They remain a preparation gap to be addressed before universal Platform-taxonomy adoption.

## Functional Role

- 3,719 proposed/review-required candidate rows;
- 1,889 explicit unresolved rows;
- 20 not-applicable rules-framework rows;
- 5,643 candidate assertions across 3,719 rows.

## Validation

PASS: exact 5,628-row accounting per facet; all nonblank IDs were previously verified against the exact 99-value Platform registry; multi-select cardinality is preserved; unresolved, host-dependent, not-mapped and N/A states are explicit; source/master CSVs and prepared historical crosswalk are unchanged.

## Next

The universal Platform taxonomy still lacks row-level `control_mode` and `platform_nature` candidates. Those are the next substantive classification tranches, followed by a cross-facet adoption review.
