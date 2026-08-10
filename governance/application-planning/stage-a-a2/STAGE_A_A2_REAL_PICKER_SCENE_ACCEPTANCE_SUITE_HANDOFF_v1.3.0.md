# STAGE-A-A2 Real Picker / Scene Acceptance Suite Handoff v1.3.0

**Work item:** STAGE-A-A2 — Universal Object Experience  
**Status:** pre-implementation Picker/Scene acceptance suite complete; A2 implementation not started by this handoff  
**AIOC branch:** `governance/stage-a-a2-detailed-design`  
**Application repository:** `cybalicistjt-stack/Multiversal-app`  
**Owner/final authority:** John Brandon Turner

## Owner-visible package

`STAGE_A_A2_REAL_PICKER_SCENE_ACCEPTANCE_SUITE_v1.3.0.zip`

SHA-256:

`6231bc8d88692a4257d672cf086d563ca2e483d72c625e38d8b7efceb2489a3d`

This package is the A2-07/A2-08 execution addendum to the governed A2 pre-implementation bundle, v1.1 projection/profile mapping, and v1.2 search/filter/ranking suite. It turns the approved v0.5 Picker/Scene behavior and v0.6 Picker/receipt/Scene schemas into deterministic acceptance fixtures grounded in real Batch 8E identities.

## Verified coverage

- schema-valid Picker invocations: **8**;
- real candidate-state fixtures: **14**;
- schema-valid success receipts: **3**;
- schema-valid service-error outcomes: **8**;
- tray/recovery cases: **6**;
- schema-valid Scene placement requests: **2**;
- schema-valid Scene placement results: **2**;
- idempotency/atomicity cases: **3**;
- blocking acceptance assertions: **30**;
- explicit real-data gaps: **4**;
- package files: **25**;
- package validator: **PASS**;
- outer ZIP CRC/integrity: **PASS**.

## Real governed anchors

The suite uses real governed identities including:

- Backpack — `DEF-ITM-99A7C519C317`;
- Dagger — `DEF-WPN-68A77E852F73`;
- Plasma Rifle — `DEF-WPN-8DF4110A9CEF`;
- Iron Golem — `CONSTRUCT-GOL-IRON-GOLEM-SRC01-CR10`;
- WarDog Recruit — `NPC-WD-SRC-001`;
- Swamps — `ENVDEF-BB71C8719980`;
- Mythragara — `SPC-MYTHRAGARA` as a caller-family incompatibility case;
- Titan's Grip — `DEF-ABL-93540966BC4D` as an exact-version stale-state case.

Real source-only negative anchors include `VEH-0001` Civilian Car and `HTR-0079` Frost Wire.

## Runtime-policy boundary

Permission revocation, entitlement revocation, Campaign pack-lock changes, version advancement, caller-family incompatibility, and interrupted-request recovery are deterministic **test overlays applied to real governed objects**. They are not claims about the canonical visibility or entitlement state of those content objects.

## Version boundary

The active release registry does not provide one intrinsic version field for every governed object. For deterministic A2 acceptance only, selected governed objects use the explicit snapshot token:

`batch8e-1.6.0`

This means “resolved against the Batch 8E portable release 1.6.0 fixture snapshot.” It must not be presented as a claim that every source Definition intrinsically has object version 1.6.0.

## Locked Picker behavior

- provisional selection never performs caller mutation;
- single-select replacement is reversible and nonauthoritative;
- the A2 tray is stable-ID oriented and remains stable-ID unique in the reference fixture;
- search/filter/Inspector/relationship navigation does not clear the tray;
- recovered provisional IDs restore intent, not authorization;
- finalization revalidates permission, entitlement, pack lock, version, caller profile/family constraints, Campaign/rules compatibility and current object availability;
- multi-select receipt is atomic by default;
- source-only/noncanonical IDs cannot finalize authoritative Picker receipts;
- successful receipts contain stable IDs/resolved versions and `authoritativeMutationPerformed: false`;
- WarDog Recruit demonstrates a compatible-with-warning receipt without fabricating its unresolved `Any Race` relationship target.

## Duplicate and quantity boundary

The reference Scene fixture uses this policy:

- same Environment stable ID: one binding in the tray/reference Scene environment slot;
- Creature/NPC repeated Scene instances: caller placement semantics after receipt, not duplicate source identity;
- Item quantity: caller placement metadata after receipt;
- Dagger proves one selected source identity may become Scene placement quantity 3 without modifying the source Definition.

## Scene placement proof

The mixed real receipt selects Swamps, Iron Golem, WarDog Recruit and Dagger. The caller-owned adapter then creates four distinct Campaign-local placement IDs and increments the deterministic Scene version from 7 to 8. Placement IDs are different from source stable IDs. A separate Dagger quantity case increments the Scene from 8 to 9.

The suite also requires:

- save/reopen preserving placement IDs and source references;
- stale expected Scene version rejection;
- caller idempotency-key retry returning the same placement outcome without duplicate placements or a second version increment;
- source Definition/fixture immutability witnesses remaining unchanged after placement application.

## Real coverage gaps preserved

1. `A2-PICK-GAP-001` — current Batch 8E release has no governed Vehicle positive receipt object; real Vehicle `VEH-0001` is source-only.
2. `A2-PICK-GAP-002` — current release has no governed Hazard positive receipt object; real Frost Wire `HTR-0079` is source-only.
3. `A2-PICK-GAP-003` — current 11,861-object governed search index contains no `P-A2-EVIDENCE` Clue/Evidence object.
4. `A2-PICK-GAP-004` — no universal object-intrinsic version field exists on the active release index; use the explicit fixture snapshot token without overclaiming object version authority.

Do not synthesize positive Vehicle/Hazard/Clue receipts merely to close coverage.

## Codex integration

Transfer this suite during A2-01. Begin running it through the same deterministic application query/Picker path in A2-07 and A2-08. The v0.6 Picker invocation, Picker receipt, Scene placement request/result and service-error schemas included in the package remain the executable contract boundary.

Day-one negative tests for A2-07/A2-08 must include source-only rejection, permission revocation, entitlement revocation, pack-lock change, exact-version stale failure, atomic partial failure, recovered-tray revalidation, duplicate Environment selection, stale Scene version and idempotent caller retry.

Production code must not contain fixture-specific name/stable-ID branches. Golden outcomes change only when governed authority changes, not merely to make implementation tests pass.

## Preservation boundary

This handoff does **not** change `CURRENT_WORK_POINTER.json`, does not activate A2 application implementation, does not alter the Design Standards primary attempt, does not promote any source-only record, and does not authorize internal-alpha release, production release or deployment.

## Exact next pre-Sunday A2 operation

Build the real **version/variant/conflict + provenance acceptance suite** for A2-06/A2-09: source-backed correction comparison, duplicate-name distinct identities, parent/variant lineage, authored expansion provenance, inference-heavy records, redacted-vs-full provenance, unavailable/restricted comparison sides, semantic field alignment, conflict/read-only behavior, and deep-link/history recovery. Produce executable fixtures and expected projections suitable for direct Codex transfer.