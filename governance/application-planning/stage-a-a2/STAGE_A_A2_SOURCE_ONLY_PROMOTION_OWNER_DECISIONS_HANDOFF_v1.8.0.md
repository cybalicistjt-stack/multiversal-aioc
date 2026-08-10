# STAGE-A-A2 Source-Only Promotion Owner Decisions Handoff v1.8.0

**Work item:** STAGE-A-A2 — Universal Object Experience  
**Status:** owner decisions resolved; bounded 16-record promotion pilot prepared; promotion not executed  
**Owner/final authority:** John Brandon Turner  
**AIOC branch:** `governance/stage-a-a2-detailed-design`

## Owner-approved decisions

1. **Logical catalog keys approved**
   - `Vehicles.csv` → `VEH`
   - `Mecha.csv` → `MCH`
   - `Spacecraft.csv` → `SCF`
   - `Hazards_Traps.csv` → `HTR`

2. **Semantic routing approved**
   - Vehicle is a distinct canonical semantic kind.
   - Mecha is a distinct canonical semantic kind and may reuse the A2 Vehicle presentation system.
   - Spacecraft is a distinct canonical semantic kind and may reuse the A2 Vehicle presentation system.
   - Hazard is canonical; Trap is a Hazard subtype.
   - Vehicle/Mecha/Ship components/modules route as Item/component objects with host compatibility relationships.
   - Service Facility remains Facility.
   - Framework records are not vehicle/hazard instances.

3. **All eight exact-name collisions are KEEP_DISTINCT**

   The source-side future canonical Definitions receive unique display names while the existing governed counterparts remain unchanged. Original source names remain provenance evidence and are not promoted as authoritative aliases merely to preserve the duplicate name.

   | Catalog | Original source name | Approved future canonical display name |
   |---|---|---|
   | Mecha.csv | Antimatter Reactor | Mecha Antimatter Reactor |
   | Mecha.csv | Solar Array | Mecha Solar Array |
   | Mecha.csv | Turbine Generator | Mecha Turbine Generator |
   | Mecha.csv | Energy Shield Generator | Mecha Energy Shield Generator |
   | Mecha.csv | Sensor Array | Mecha Sensor Array |
   | Mecha.csv | Aquatic Adaptation | Mecha Aquatic Adaptation System |
   | Spacecraft.csv | Vanguard Repair Fabricator | Vanguard Ship Repair Fabricator |
   | Spacecraft.csv | Paragon Repair Fabricator | Paragon Ship Repair Fabricator |

4. **Authored-expansion policy approved — Option A**

   Authored/original expansion records may become ordinary governed usable content. Their provenance must permanently state `Authored Expansion`; they may not masquerade as direct source extraction.

5. **Framework routing approved**

   Mecha/Spacecraft/Hazard-Trap `Rules Framework` / `Ship Class Framework` records route to **Rule / Rules Profile** objects rather than to Vehicle, Mecha, Spacecraft or Hazard object instances.

## Package

Owner-visible package:

`STAGE_A_A2_SOURCE_ONLY_PROMOTION_DECISION_AND_PILOT_WORK_ORDER_v1.8.0.zip`

SHA-256:

`bf9f65b11a9f704c8dcec889f2b6183f4c15179afa0a71ab9b189973f79e6f2d`

Package validator: **PASS**.

Verified package boundary:

- owner decisions resolved: **5/5**;
- collision rows resolved: **8/8**;
- unique future canonical display names assigned: **8**;
- bounded promotion pilot rows prepared: **16**;
- Source_Record_IDs minted: **0**;
- Definition_IDs minted: **0**;
- promotion executed: **false**;
- release authorized: **false**;
- deployment authorized: **false**.

## Promotion boundary

The owner decisions remove the policy/identity ambiguity identified by v1.7.0, but this handoff does not itself promote content. A separately executed bounded pilot must still:

1. re-verify the current identity contract and source snapshot;
2. freeze exact source-row receipts for the 16 approved pilot records;
3. mint/freeze deterministic Source_Record_IDs under the approved logical catalog keys;
4. mint governed Definition IDs under the approved semantic family routing;
5. preserve source-local IDs as provenance coordinates only;
6. update the governed release registry and regenerate affected A2 fixtures;
7. rerun affected v1.1–v1.6 validators;
8. record exact before/after registry counts and rollback mappings.

## Sunday A2 boundary

The existing `STAGE_A_A2_SUNDAY_CODEX_MASTER_EXECUTION_v2.0.0` remains valid unless this 16-record promotion pilot is actually completed before A2 application implementation begins. Do not make Sunday A2 wait merely because the promotion work order is prepared.

If the promotion pilot is completed before Sunday, regenerate the affected v1.1–v1.6 fixtures and rebuild the Sunday master archive before handing it to Codex.

This handoff does not alter `CURRENT_WORK_POINTER.json`, does not complete or modify the parallel Design Standards primary attempt, does not activate A2 application implementation, and does not authorize release/deployment.