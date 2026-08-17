# CCTI Item Taxonomy Cross-Axis Review / Consolidation

**Date:** 2026-08-17  
**Status:** review complete for available exact row-level evidence; adoption proposal prepared; canonical enablement remains blocked

## Scope

Reviewed the completed first-pass Item taxonomy candidate work for all **5,389 Item-corpus rows** against the exact Item Taxonomy v0.12.0 rules. The source/master CSV hash manifest still matches exactly; no source/master row was mutated.

All ten axes remain sealed historical candidate evidence. This review creates only additive review/correction proposals.

## Evidence continuity

Exact row-level private artifacts are present and checksum-match their sealed receipts for **IAX-01 through IAX-05, IAX-09 and IAX-10**.

The active workspace does **not** contain the private row-level ZIP bytes for **IAX-06, IAX-07 or IAX-08**. Their canonical aggregate baselines and sealed SHA-256 identities remain available in the repository. This is an evidence-availability issue, not a claim that those tranches were incomplete.

**Adoption rule:** do not enable those axes until the original row-level bytes are recovered at the sealed hashes or a new governed, versioned superseding reprojection is produced and reviewed. Do not fabricate the old bytes or silently reconstruct them as if identical.

## Cross-axis invariant results

Pass:
- 5,389-row identity/accounting continuity;
- source/master SHA-256 continuity;
- IAX-10 `none_general` exclusivity;
- zero `integrated_internal` rows with `none_general` target;
- zero `implant_internal` rows lacking `implanted`;
- zero `implanted` rows lacking `person_body` or `biological_host`;
- later axes IAX-06 through IAX-10 preserve the seven IAX-01 non-item support rows as N/A.

Review findings:
- **7** `non_item_support_record` rows still carry pre-scope IAX-02/IAX-03/IAX-04 candidate evidence, and six also carry IAX-05 candidates. The adoption overlay should mark IAX-02 through IAX-05 N/A for all seven rather than rewriting the sealed historical tranches.
- **5** rows combine IAX-05 `vehicle_mounted` with IAX-10 `none_general`.
- **28** rows combine IAX-04 `mounted` with IAX-10 `none_general`.
- **34** rows combine IAX-04 `installed` with IAX-10 `none_general`.
- **24** rows combine IAX-01 `standalone_item` with IAX-03 `module_board`.
- **3** `interface` scope rows still have IAX-10 `none_general`.
- **30** `software_data` rows have embodied `module_board` form; this is retained as an informational hybrid review signal, not an automatic error.

The union of structural blocking/review cohorts above is **91 rows** (excluding the informational software/embodied hybrid cohort).

## Source-backed correction proposals

Prepared **85** additive correction proposals. High-confidence examples include:

- `Space Laser`: preserve `vehicle_mounted`; change use relation from `wielded` to `mounted|operated`; change integration target from `none_general` to `vehicle`.
- `Heavy Cavalry Lance`: remove the false platform-mount interpretation from use relation and change portability from `vehicle_mounted` to `personal_standard`; its source says mounted combat, not installation on a platform.
- `Bayonet`: change portability from `vehicle_mounted` to `personal_light` and integration target to `weapon`.
- `Chainsaw Bayonet`: change portability from `vehicle_mounted` to `personal_standard` and integration target to `weapon`.
- `Puckle Gun`: change portability from `vehicle_mounted` to `team_portable`; it is a 70-lb crew-served mounted heavy weapon, while the actual Vehicle Weapon records remain platform-mounted.
- all seven `non_item_support_record` rows: suppress IAX-02 through IAX-05 at adoption time as N/A.
- 24 `Titan-Rune` cockpit grimoires receive **medium-confidence** review proposals for `mecha` integration and `vehicle_mounted` portability because their source explicitly says they are mounted in a cockpit control halo and scale through a bonded machine frame. These are not auto-corrections until the host class is confirmed.

## Review-state scale

Exact available axes already show **4,940** rows with at least one medium/review-required candidate and **338** rows with at least one explicit unresolved state.

Sealed aggregate receipts additionally record:
- IAX-06: 4,550 rows with review-required candidates;
- IAX-07: 1,541 review-required rows, including 225 exact `unknown`;
- IAX-08: 2,248 review-required rows.

These are legitimate review states; they are not defects to erase by guessing.

## Adoption proposal

**Do not enable the Item taxonomy yet.**

Proposed governed adoption sequence:
1. preserve all ten sealed historical candidate tranches unchanged;
2. apply a separate correction/suppression overlay from this cross-axis review;
3. recover the exact IAX-06/IAX-07/IAX-08 row-level evidence or create explicitly versioned superseding reprojections;
4. regenerate one complete 5,389-row, ten-axis adoption candidate ledger;
5. re-run axis cardinality, controlled-value, scope-N/A, host/integration, provenance, source-hash, and Definition-vs-Instance checks;
6. present the resulting adoption candidate and remaining unresolved queue to the owner;
7. only after owner approval mark taxonomy metadata canonical/available to later app-facing work.

Mechanics reauthoring, runtime Asset creation, app-facing enablement, and `GAME_READY` certification remain outside this gate.

## Next safe CCTI operation

Item canonical adoption is gated, but the already-authorized additive CCTI program can continue without waiting: proceed to the exact **Platform v0.11.0 candidate projection/review across the 5,628 Vehicles/Mecha/Spacecraft-domain rows**, preserving the existing **2,984 platform/model vs 2,644 non-model** routing.
