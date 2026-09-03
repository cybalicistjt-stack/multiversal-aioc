# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-07; SCL-08 IN_PROGRESS  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner

## Current state

SCL-01 through SCL-07 are `completed_verified`. Owner `Continue` governed-started SCL-08 — Vehicle, Mecha, Ship & Fleet Integration — from exact application main `154a72bbcabfe6fe21a99e219ef1afe1863bb061`. Application implementation authority is limited to branch `integration/scl-08-vehicle-mecha-ship-fleet-integration` and the sealed read-only integration contract below.

## Governed SCL-08 contract

SCL-08 integrates explicit canonical references; it does not create a second vehicle runtime. Canonical F008 Asset identity/ownership/custody/control/access and F014 Vehicle Operation state remain authoritative. SCL-02 remains authoritative for squad/fleet profile and membership identity. SCL-03/04 retain command/order authority, SCL-06 retains logistics/readiness evidence, SCL-07/World retain semantic position/environment truth, SCL-09 retains casualty/damage/recovery reconciliation, and SCL-10 retains strategic consequences.

Retained source `Vehicles & Operations.PDF` SHA-256 `8eac372414eb74efa19ebfdfd954762cdd82f01a71c7563335c0c0f4998ba219` provides vehicle/mecha/starship operational abilities and piloting/crew context. Retained `Squad & Fleet.PDF` SHA-256 `20d7a5bbeafb7fccf2213aee5470741cb35760270907ff56e075f86ee83ae8da` describes a source-specific squad as 1-5 ships and a fleet as multiple squads led by a flagship or command ship. That source-specific squad-size statement is preserved as evidence only; it does not replace the frozen SCL-01/SCL-02 scale taxonomy or become a universal numeric cap. A flagship/command-ship leader is projected only from an explicit canonical reference and is never inferred.

Canonical F014 operational classes are `ground`, `water`, `air`, `space`, `submersible`, `walker`, `mecha`, `mount`, `hybrid`, `abstract`. Canonical stations are `pilot`, `commander`, `navigator`, `gunner`, `engineer`, `sensor`, `communications`, `defense`, `medical`, `cargo`, `passenger`, `remote-operator`. Canonical vehicle states are `idle`, `crewed`, `active`, `docked`, `disabled`, `immobilized`, `uncontrolled`, `adrift`, `breached`, `destroyed`, `abandoned`, `captured`, `salvaged`.

SCL-08 may project visible `vehicle`, `mecha`, and `ship` integration rows linking SCL-02 profile/membership IDs to explicit F008 Asset Instance and F014 Vehicle Operation references, plus explicit crew/station actor refs and command/resource/position/handoff references. Ownership or custody never implies station authority. Pilot/crew identity remains distinct from machine identity; SCL-08 never merges actor and machine state or infers pilot damage from machine damage.

Carried craft, cargo, passengers and nested Assets remain separate identities. Carrier damage, fleet membership, boarding or docking references never implicitly mutate children. Unknown/source-unspecified evidence is not zero, absent, available, compatible, full or unlimited.

Visibility filters before platform rows, crew/station rosters, fleet bindings, counts, classes, states, source-rule references, summaries, search, provenance, handoffs, deterministic receipts or AI context. Hidden existence/cardinality is undisclosed. Stable integration-ID ordering exists only for deterministic output and never creates authority or priority.

No vehicle movement, Action/Combat result, Resource consumption, repair, damage/casualty propagation, ownership/control transfer, position mutation, command issuance/resolution, autonomous AI command/adjudication, duplicate ledger, durable persistence or migration `0022` is authorized by SCL-08.

## Tranches

1. SCL-01 — Source Inventory, Scale Taxonomy & Authority Map — completed_verified.
2. SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model — completed_verified.
3. SCL-03 — Command Hierarchy, Roles, Orders & Communication — completed_verified.
4. SCL-04 — Command Phases & Deterministic Order Resolution — completed_verified.
5. SCL-05 — Morale, Cohesion, Leadership & Discipline — completed_verified.
6. SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness — completed_verified.
7. SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position — completed_verified.
8. SCL-08 — Vehicle, Mecha, Ship & Fleet Integration — in_progress.
9. SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery — planned.
10. SCL-10 — Faction, Settlement, World & Campaign Consequence Integration — planned.
11. SCL-11 — Workbench, Scenario Packs, Balance & Cross-Scale Golden Proof — planned.

## Current invariant

Acceptance-first application evidence must establish genuine matching self-hosted Linux/Windows RED before SCL-08 production contract/panel mutation. Final exact-head GREEN must run exactly one SCL-08 current-family profile with zero historical predecessor fanout and deterministic comparison.
