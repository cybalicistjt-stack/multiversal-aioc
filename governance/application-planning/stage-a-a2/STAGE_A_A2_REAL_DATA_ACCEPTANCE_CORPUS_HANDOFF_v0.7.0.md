# STAGE-A-A2 Real-Data Acceptance Corpus Handoff v0.7.0

**Work item:** STAGE-A-A2 — Universal Object Experience  
**Design status:** first real-data golden-object tranche complete; application implementation not started by this handoff  
**Branch:** `governance/stage-a-a2-detailed-design`  
**Owner/final authority:** John Brandon Turner

## Completed tranche

Owner-visible package produced:

`STAGE_A_A2_REAL_DATA_ACCEPTANCE_CORPUS_v0.7.0.zip`

SHA-256:

`b97e65edc30a6d336269a6813d30bfd678f91ee796493f9f45c78f372e005c70`

The package is grounded in the actual Batch 8E v1.6.0 release content and contains 12 selected real golden cases with 55 blocking assertions, exact source-row fixture envelopes, source SHA receipts, per-case expected assertions, a Codex real-data test plan, and a deterministic corpus validator.

## Selected real golden cases

1. Backpack — simple Item baseline; governed ID `DEF-ITM-99A7C519C317`.
2. Plasma Rifle — dense Weapon/Item module; governed ID `DEF-WPN-8DF4110A9CEF`.
3. Swordsplay Ability Tree — governed tree ID `DEF-ABL-949306248109`; 20 governed child memberships.
4. Iron Golem — `CONSTRUCT-GOL-IRON-GOLEM-SRC01-CR10`; 17 extracted child Features and labeled inferred schema fields.
5. Mythragara — `SPC-MYTHRAGARA`; 40 source pages and 128 extracted child Features.
6. Grendelkin — `SPC-GIANTKIN-GRENDELKIN`; explicit parent `SPC-GIANTKIN` and Subspecies identity.
7. Absolute Authority — duplicate display name resolving to two distinct governed definitions: `DEF-ABL-FFABB689B369` and `DEF-ABL-CFB6E57EB0F4`.
8. WarDog Recruit — `NPC-WD-SRC-001`; real unresolved `HAS_SPECIES` edge with raw target `Any Race` and no governed target ID.
9. Titan's Grip — `DEF-ABL-93540966BC4D`; source-backed correction from frozen Tier 2 / malformed Tier_Name to Tier 1 / `Tier 1 Abilities`, with original values preserved for provenance.
10. Mythragara Runebound Castellan — `NPC-SP-EXP-MYT-FAN`; explicit `Authored Expansion`, `Design judgment` confidence, and child combat Features.
11. Bloom of the Eternal Spiral — `PLANT-SPR-BLOOM-OF-THE-ETERNAL-SPIRAL-CR19`; 22 extracted child Features, the largest observed child-Feature count in the Batch 8E creature packages, plus documented inferred fields.
12. Plasma Carbine — governed Item/Weapon identity whose source row explicitly states `Original ammo-only name; full row inferred`.

## Locked test philosophy

- The real-data corpus complements rather than replaces the v0.6 synthetic contract fixtures.
- `fixtures/real/*.json` preserve actual selected source rows and related rows. They are not hand-authored A2 projections.
- Codex must run those fixtures through the same deterministic A2 adapter and v0.6 projection/service contracts used by the application.
- Golden tests must check identity, search, relationships, provenance, presentation, picker behavior, responsive overflow and accessibility without creating fixture-specific UI bypasses.
- Duplicate display names must never be merged by name.
- Unresolved relationships must remain visibly unresolved and must not fabricate clickable stable IDs.
- Source-backed corrections must affect effective projections while original frozen values remain explainable through provenance.
- `Authored Expansion` must remain visibly authored and must not be presented as verbatim source extraction.
- Inferred completion must remain provenance-distinguishable from direct source content.

## Owner-corrected real-data gap

The Batch 8E species schema explicitly permits `Owner Corrected` as an Origin/Provenance_Type value. A scan of the Batch 8E release found no actual data record using that state. The corpus therefore records `A2-RD-GAP-001` as `REAL_DATA_GAP_DO_NOT_SYNTHESIZE` rather than fabricating a test record.

`Titan's Grip` is intentionally classified as a **source-backed correction**, not an owner correction.

## Validation

- corpus validator: PASS;
- selected real cases: 12;
- blocking assertions: 55;
- Mythragara child Feature count invariant: 128;
- Iron Golem child Feature count invariant: 17;
- Bloom child Feature count invariant: 22;
- Absolute Authority duplicate stable-ID invariant: PASS;
- Titan's Grip correction invariant: PASS;
- WarDog unresolved-target invariant: PASS;
- deterministic ZIP integrity/CRC: PASS.

## Preservation boundary

This handoff does **not** change `CURRENT_WORK_POINTER.json`, does not activate A2 repository implementation, and does not alter the owner-selected Content v2 Batch 8E governed-promotion operation. It is preparatory/parallel A2 design and test evidence only.

Do not claim A2 implementation, A2 exit-gate completion, Public Canon completeness, content promotion, internal-alpha release, production release, or deployment authority from this handoff alone.

## Exact next corpus operation

Expand the real-data corpus into the second domain tranche: World/Setting, Vehicle/Mecha/Spacecraft, Environment + linked environmental Ability, Hazard/Trap, Facility/Base, Faction/Organization, Pack/Source/provenance records, cross-domain high-degree relationships, and role/redaction variants of selected real objects. Keep the owner-corrected case open until a genuine owner-corrected record is available.
