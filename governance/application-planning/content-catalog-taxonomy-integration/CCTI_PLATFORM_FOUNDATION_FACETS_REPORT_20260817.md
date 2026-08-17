# CCTI Platform Foundation Facets — Record Scope + Platform Family

**Date:** 2026-08-17  
**Status:** candidate disposition complete; not enabled

The exact Platform v0.11.0 preparation establishes `record_scope` as single-select and `platform_family` as single-select. This tranche validates those cardinalities instead of blindly adopting the preparation preview.

## Record scope

All **5,628/5,628** rows have one exact controlled record-scope candidate. The established routing remains **2,984 platform/model/named/archetype** and **2,644 non-model** records.

## Platform family

- **5,352** rows have one exact single platform-family candidate.
- **241** rows are explicitly host/record-dependent with no family assignment.
- **35** rows are explicitly unresolved because the prepared preview contains more than one family ID while the v0.11.0 Platform Family facet is single-select.

The 35 rows are not forced. They consist of 33 amphibious vehicle models plus two vehicle modules carrying multi-family compatibility signals. Their operating-media/compatibility information remains valid evidence, but it cannot be silently adopted as multiple primary Platform Family values.

This is a correction overlay only. The sealed prepared crosswalk is not rewritten.

## Validation

PASS: 5,628-row accounting; zero record-scope cardinality violations; 5,352 exact single family candidates; 241 explicit host-dependent states; 35 explicit primary-family review states; 2,984/2,644 route preservation; no source/master mutation; no enablement/mechanics/runtime/game-ready change.

## Next

Proceed to `operating_medium`, which is legitimately multi-select, while retaining host-dependent and unresolved states rather than forcing values.
