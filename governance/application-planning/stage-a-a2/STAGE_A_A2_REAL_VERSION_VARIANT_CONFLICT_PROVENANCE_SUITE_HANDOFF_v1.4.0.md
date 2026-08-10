# STAGE-A-A2 Real Version / Variant / Conflict + Provenance Suite Handoff v1.4.0

**Work item:** STAGE-A-A2 — Universal Object Experience  
**Status:** pre-implementation version/variant/conflict + provenance acceptance suite complete; A2 implementation not started by this handoff  
**AIOC branch:** `governance/stage-a-a2-detailed-design`  
**Application repository:** `cybalicistjt-stack/Multiversal-app`  
**Owner/final authority:** John Brandon Turner

## Owner-visible package

`STAGE_A_A2_REAL_VERSION_VARIANT_CONFLICT_PROVENANCE_SUITE_v1.4.0.zip`

SHA-256:

`ddf4060db826707cdd3b1c52322a3dc56a6ef3b0e86e8056c9f605766411e597`

This package is the A2-06/A2-09 execution addendum to the governed A2 pre-implementation bundle, v1.1 projection/profile mapping, v1.2 search/filter/ranking suite, and v1.3 Picker/Scene suite. It turns the approved v0.5 comparison/provenance behavior and v0.6 comparison/provenance/error schemas into deterministic real-data acceptance fixtures.

## Verified coverage

- positive comparison projections: **3**;
- negative comparison outcomes: **3**;
- provenance projections: **7**;
- compare/provenance deep-link states: **4**;
- history/focus recovery cases: **4**;
- blocking acceptance assertions: **32**;
- package files: **20**;
- package validator: **PASS**;
- v0.6 comparison/provenance/error schema conformance: **PASS**;
- v0.5 URL-state schema conformance: **PASS**;
- outer ZIP CRC/integrity: **PASS**.

## Real comparison anchors

### Titan's Grip — source-backed correction

`DEF-ABL-93540966BC4D` compares the preserved frozen extraction against the effective source-backed correction. The changed semantic fields are Tier `2 → 1` and Tier_Name `Tier 2 Abilities → Tier 1 Abilities`. Original frozen values remain provenance evidence and are never overwritten or relabeled as owner correction.

### Giantkin → Grendelkin — declared variant lineage

`SPC-GIANTKIN-GRENDELKIN` explicitly records `Parent_Species_ID=SPC-GIANTKIN` and `Variant_Type=Subspecies`. The compare fixture therefore labels Giantkin as the base Definition and Grendelkin as a Variant-layer side while preserving their distinct stable IDs.

### Acid Grenade — real multi-source mechanic conflict

`DEF-WPN-2EEF55CD816E` is governed by identity decision `CVID-02379DD29BE1`, which merges two source rows into one Definition while explicitly preserving conflicting mechanic/source provenance.

The real source candidates differ on fields including cost, weight, damage/effect representation and range/area:

- `Items.csv`: 200 credits, 2 lbs., ongoing-corrosion effect, 15-ft radius inferred;
- `Ranged_Weapons.csv`: 140 credits, 1 lb., 2d6 Acid explosion, 30/90 ft.

The governing conflict rule says identity resolution never silently chooses a mechanic. A2 therefore presents this comparison as read-only explanatory conflict evidence. No `Use left` / `Use right` mutation is permitted.

## Negative comparison boundaries

- the two governed `Absolute Authority` records share a display name but have distinct identities and no declared version/variant relationship; same-name equality must not create compare authority;
- a restricted comparison side returns the safe `not_found_or_forbidden` family without leaking its identity;
- an unavailable comparison version/pack returns `unavailable_pack` and must not mutate current inspection or provisional selection state.

## Real provenance anchors

The suite covers:

1. Titan's Grip source-backed correction evidence;
2. Grendelkin parent/variant source evidence;
3. Acid Grenade competing-source conflict evidence plus governance identity decision;
4. Mythragara Runebound Castellan explicitly labelled `authored_expansion`, preserving Design-judgment semantics;
5. Plasma Carbine inference-heavy normalization explicitly remaining partial/provenance-distinguishable from direct extraction;
6. Mythragara full-authority source title/coordinate/fragment projection;
7. Mythragara source-redacted projection containing no source title, coordinate, fragment or field evidence.

## Authorization, URL and recovery rules

- each compare side is independently authorization/entitlement/availability projected;
- every provenance level is independently authorization projected;
- URL state serializes safe view intent only and never grants comparison or source access;
- cached browser/history state must not resurrect previously permitted source text after permission loss;
- Back returns to the exact originating Inspector section/field/focus target;
- compact/mobile compare must remain semantically understandable without horizontal-only layout or color-only change meaning.

## Preserved gaps

- no genuine `Owner Corrected` Batch 8E record has been found; do not synthesize one;
- the active release does not provide a universal intrinsic semantic version for every object; labels such as `frozen-extracted`, `corrected-effective`, `candidate-items` and `candidate-ranged` are acceptance-side candidate labels rather than claims of canonical object versions;
- A2 conflict comparison is explanatory/read-only; conflict resolution remains outside A2 unless a separately governed workflow authorizes it.

## Codex integration

Transfer this suite during A2-01. Execute provenance fixtures during A2-06 and comparison/history fixtures during A2-09 through the same generic application projection paths used by the UI.

Day-one assertions include:

1. original correction evidence remains visible after effective-value correction;
2. true parent/variant lineage uses stable IDs and explicit record-layer labels;
3. same display names do not merge identities or create compare eligibility;
4. Acid Grenade identity merge does not choose conflicting mechanics;
5. restricted sides/source evidence do not leak through compare, deep links, back navigation or cached state;
6. authored expansions remain visibly authored;
7. inferred completion remains distinguishable from direct extraction;
8. redacted provenance contains no hidden source metadata/text;
9. compare/provenance UI remains read-only, keyboard reachable and mobile understandable.

Production code must not contain fixture-specific object-name or stable-ID branches. Golden outcomes change only when governed authority or source evidence changes, not merely to make tests pass.

## Preservation boundary

This handoff does **not** change `CURRENT_WORK_POINTER.json`, does not activate A2 application implementation, does not alter the Design Standards primary attempt, does not resolve content conflicts, does not synthesize owner-corrected evidence, and does not authorize internal-alpha release, production release or deployment.

## Exact next pre-Sunday A2 operation

Build the A2 **visual/interaction acceptance reference + accessibility/responsive executable checklist** for A2-04 through A2-10: desktop/tablet/mobile Library and Inspector states, Picker tray/sheet states, compare/provenance compact layouts, focus order, keyboard behavior, reduced motion, 200%/400% zoom-reflow expectations, large-feature/relationship collection behavior, and exact screenshot/evidence checkpoints. Use the already-approved UI/Screen Design Bibles and A2 screen specifications; do not redesign the visual language.
