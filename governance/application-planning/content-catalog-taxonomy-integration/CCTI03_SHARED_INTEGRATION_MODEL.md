# CCTI-03 — Shared Integration Model

**Mode:** read-only analytical contract. Persistent taxonomy writes remain owner-gated.

## Analytical routing classes

- `ITEM_SHADOW_PROJECTION` — current Item-corpus definition/reference work prepared for Item v0.12.0 shadow projection. A8 owns live Asset Instance state.
- `PLATFORM_MODEL` — reusable Vehicle/Mecha/Spacecraft model prepared for Platform v0.11.0. A model is not an individual asset.
- `PLATFORM_COMPONENT_OR_MODULE` — reusable component/module. PPIA-04 owns explicit parent/component semantics; PPIA-03 generic Asset semantics are reused only where appropriate. Actual installation is runtime state.
- `PLATFORM_RULE_FRAMEWORK` — rules/class/framework content, never a platform asset merely because it is stored in a platform CSV.
- `SUPPORT_EQUIPMENT_OR_SUPPLY` — support equipment, consumable, ammunition/charge/power/support content routed to the owning Item/Resource domain after evidence review.
- `SERVICE_OR_FACILITY` — service/facility/package content routed to Economy/Base/Crafting/Vehicle handoffs as applicable.
- `LEGACY_REFERENCE` — supersession/provenance evidence; does not create a duplicate current Definition.
- `REVIEW_REQUIRED` — evidence insufficient or conflicting; unknown remains unknown.

These route labels are CCTI analysis labels, not new canonical taxonomy IDs.

## Initial deterministic routing

Item v0.12.0 scopes the 5,389-row Item corpus. Content V2 separately proves `Weapons_Ammo.csv` is reference-only, so CCTI preserves 5,353 non-legacy Item rows for direct Item shadow projection plus 36 legacy-reference rows. Thirty of the 36 reference rows point to existing current Definitions; six remain reference identities without a current target.

Platform catalogs split as:

- 2,984 `PLATFORM_MODEL` rows: Vehicles 953; Mecha 930; Spacecraft 1,101.
- 2,644 non-model rows requiring component/module/rules/support/service routing.

Component parentage or compatibility must use explicit structured/source evidence. Name similarity or document grouping is insufficient.

## Definition versus instance

Item catalog identity may describe concept/family/line/model/variant/configuration, creator/origin, compatibility and provenance. It does not own live ownership, custody, quantity, equipped state, condition, damage, repair, or runtime modification.

Platform catalog identity may describe creator/manufacturer, family/platform/model/variant/trim, factory configuration, compatibility, support/parts, production history and provenance. Serial/callsign/ownership/service/damage/repair/capture/destruction history belongs only to an individual asset.

## Cross-domain analysis families

CCTI may identify candidate relationships read-only, but persistent adoption must map them to existing governed registries or present an owner-reviewed extension proposal. Analysis families include component compatibility/parentage, factory configuration, ammunition/charge, power/resource requirements, host/interface/mount requirements, cargo/support/EVA equipment, repair materials/components, reusable upgrades, creator/manufacturer, product lineage, and setting/context compatibility.

Definition relationships never imply that an individual runtime asset currently has a component installed, fuel loaded, cargo present, or ownership assigned.

## Shared context boundary

Reality/shared context may describe presence, affinity, requirements, availability, or compatibility. It does not duplicate Item/Platform mechanics or Campaign/runtime state. Intrinsic requirement, affinity, compatibility, availability, legality, rarity, and price remain distinct concepts.

## Evidence precedence

1. governed stable identity / explicit cross-catalog identity decision;
2. source/master row plus typed normalization/provenance evidence;
3. explicit relationship, parentage, or supersession evidence;
4. exact later taxonomy/catalog registry and crosswalk authority;
5. review-required where evidence remains insufficient.

Display-name similarity is never authority.
