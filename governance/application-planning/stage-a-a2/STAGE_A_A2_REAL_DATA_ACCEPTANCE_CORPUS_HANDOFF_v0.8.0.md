# STAGE-A-A2 Real-Data Acceptance Corpus Handoff v0.8.0

**Work item:** STAGE-A-A2 — Universal Object Experience  
**Design/test status:** second real-domain golden tranche complete; application implementation not started by this handoff  
**Branch:** `governance/stage-a-a2-detailed-design`  
**Owner/final authority:** John Brandon Turner

## Completed tranche

Owner-visible package produced:

`STAGE_A_A2_REAL_DATA_ACCEPTANCE_CORPUS_v0.8.0.zip`

SHA-256:

`38cc06cc0eb031419adbc8355ace15f88ef9b50545c4b3a2f821b71d13d32648`

The expanded corpus preserves all 12 v0.7.0 real golden cases and adds 12 more, for **24 selected real golden cases and 115 blocking assertions**.

## New real cases

13. Vertigon — governed Setting `SET-1C4C2E7C93D9`; 24 places, 5 rules, 3 events, 51 hooks, 69 preserved source sections.
14. Swamps + Mire Walker — governed Environment `ENVDEF-BB71C8719980` with four resolved adaptation Ability links; Mire Walker resolves to `DEF-ABL-2C6FBF6ADE4B` while preserving source row `ABL3-00310`.
15. Civilian Car — source Vehicle `VEH-0001`; explicit 61-field stat block; source-only/noncanonical in the portable release.
16. Primax RX-07 "Hollowstep" — source Named Mecha `MCH-0031`; dense specialized source shape; source-only/noncanonical.
17. Orrukhal Bastion-Class Carrier — source Named Spacecraft `SCF-0027`; dense spacecraft shape; source-only/noncanonical.
18. Frost Wire — source Trap `HTR-0079`; dense trap shape; source-only/noncanonical.
19. Mecha Workshop — governed Facility `DEF-FAC-77501B32CCA3`; extracted source facts plus explicit best-judgment completion.
20. Goblin Imperial Throne — governed Faction/Organization `mv.setting.faction.goblin-imperial-throne`; sparse source-backed record with one resolved governance relationship.
21. Environment Promotion Package — real package manifest `MV-CONTENT-V2-BATCH8B-ENVIRONMENT-PROFILE-PROMOTION-001`, version 1.3.0, with counts, completion boundary and per-file SHA receipts.
22. Swamps source capture — real source/provenance record `ENVSRC-9B9B2ACA9AFF`; Aquatic Environments.PDF pages 4–6 with full-range source capture and normalization provenance.
23. Dagger — governed weapon `DEF-WPN-68A77E852F73`; 35 resolved cross-package relationship edges, the highest-degree non-Species cross-domain object observed in this selection pass.
24. Mythragara role/redaction variants — same real `SPC-MYTHRAGARA` 128-feature fixture run through full-authority and source-redacted projection policies; source data itself is unchanged.

## Authority finding locked by the corpus

Batch 8E contains large Vehicle, Mecha, Spacecraft and Hazard/Trap catalogs in the frozen source snapshot, but the selected source records above are absent from `PORTABLE_RELEASE_ID_REGISTRY_v1.0.0.csv`. Their source-local IDs therefore must **not** be treated as promoted canonical Definition IDs by A2.

The v0.8 acceptance suite requires the deterministic adapter to parse/render these real shapes in source-fixture/diagnostic mode while refusing to manufacture canonical identity or ordinary authoritative Picker receipts.

By contrast, Vertigon, Swamps, Mecha Workshop, Goblin Imperial Throne and Dagger have governed portable identities and are tested through normal governed A2 search/detail/relationship/provenance/Picker behavior.

## Validation

- corpus validator: PASS;
- selected real golden cases: 24;
- blocking assertions: 115;
- Vertigon child-density invariant: 24 places / 51 hooks / 69 source sections;
- Swamps linked-Ability invariant: 4;
- source-only authority invariants for Vehicle/Mecha/Spacecraft/Trap: PASS;
- Mecha Workshop governed ID invariant: PASS;
- Dagger relationship edge invariant: 35;
- Mythragara role fixture feature count invariant: 128;
- deterministic ZIP CRC/integrity: PASS.

## Preserved gap

`A2-RD-GAP-001` remains open. Batch 8E permits `Owner Corrected` as a provenance/origin state but contains no actual record using it. Do not synthesize an owner-corrected content fixture merely to close test coverage.

## Preservation boundary

This handoff does **not** change `CURRENT_WORK_POINTER.json`, does not activate A2 repository implementation, and does not alter the owner-selected Content v2 Batch 8E governed-promotion operation. It is preparatory/parallel A2 design and test evidence only.

Do not claim A2 implementation, A2 exit-gate completion, canonical promotion of source-only Vehicle/Mecha/Spacecraft/Hazard records, Public Canon completeness, internal-alpha release, production release, or deployment authority from this handoff alone.

## Exact next corpus operation

Turn the 24-case real corpus into the bounded A2 implementation work order/Codex execution package: exact fixture destinations under the application repository, ordered implementation slices, day-one test commands, CI gates, changed-path scope, preview evidence, owner-review evidence and rollback. Preserve the source-only/noncanonical acceptance boundary and the owner-corrected real-data gap.