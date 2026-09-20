# OARC-01 — Authority & Handoff Contract

**Work item:** OARC-01  
**Contract:** `OARC01.AUTHORITY_HANDOFF.v1`  
**Status:** implementation candidate  
**Scope:** owner boundaries and handoff semantics only

## Result

OARC is a **readiness bridge, validation and certification lane**. It is not a new canonical owner runtime.

The operational-asset ownership graph is frozen as a graph of explicit handoffs, not a transfer of authority:

`MRCS-13 definitions → MIB-14 configuration foundation → D17/PPIA-03 live Asset truth ↔ PPIA-04/F014 operational semantics`

MERA and MBES remain future orchestration families that consume those owners after their own governed starts. They are **not** downstream ledgers that OARC may implement early.

## Frozen owner matrix

| Concern | Primary owner | OARC treatment |
| --- | --- | --- |
| reusable item/equipment/vehicle/construct/component definitions, slots and versioned compatibility | MRCS-13 | consume/bridge only |
| vehicle/platform/base configuration foundation, module/facility compatibility, governed capacities and crew bounds | MIB-14 | consume/validate only |
| live Asset identity, ownership/custody, location, containment/cargo placement, condition and history | D17/PPIA-03/shared-assets | live truth; OARC never duplicates |
| vehicle/mecha/starship stations, control, movement/deployment, operational systems and docking/boarding semantics | PPIA-04/F014 | consume/validate only |
| repair/crafting/refurbishment/fabrication transactions | MIB-12 | handoff only |
| salvage/decomposition/extraction/donor lineage | LSS | handoff only |
| price/market/scarcity/economic truth | MIB-13/Economy | reference only |
| Project/task/campaign-time truth | APW/D26 | reference only |
| engineering topology, diagnosis, disassembly/refit, network/failure, calibration and acceptance | MERA | **reserved; no implementation authority yet** |
| construction, built-environment topology, functional spaces/facility networks and settlement development | MBES | **reserved; no implementation authority yet** |
| canonical world/environment/reality state | World/Environment/Reality | reference/owner response only |
| action/combat/strategic outcomes | Action/Event/Combat/SCL | accepted result only |

## Handoff rules

MRCS hands MIB-14 definition identity/version, explicit slots/components, compatibility rules and owner references. It does not hand over a live Asset.

MIB-14 validates/plans operational configurations and bounded mutation intents. D17/shared Asset authority commits and owns the live instance state.

PPIA-04/F014 consumes stable live Asset identity while retaining domain-specific vehicle/mecha/starship semantics. Crew/station assignment, deployment, installation and containment never imply ownership transfer or identity collapse.

Future MERA receives accepted Asset/configuration/component/interface evidence plus owner references. It will own engineering orchestration only after a MERA governed start; repair transactions remain MIB-12, salvage remains LSS, Asset truth remains D17 and Project/time remains APW/D26.

Future MBES receives accepted base/facility/site and owner-backed engineering/project/economy/world references. It will own construction/built-environment/settlement orchestration only after an MBES governed start.

## Later-OARC admission gate

Before OARC-02 through OARC-07 add any field or capability, the work must identify:
1. one existing primary truth owner;
2. whether the representation is a definition, reference, live-owner state, projection, receipt or coverage gap;
3. the source-truth state;
4. the authorized mutation/handoff path;
5. provenance.

If no primary owner exists, the result is an **unresolved owner gap** and OARC does not implement it. If the source does not specify a fact, OARC records it as unresolved and does not default or infer it.

## Explicit prohibitions

OARC may not create a second modular-definition grammar, Asset/inventory/cargo ledger, vehicle operations engine, MERA engineering topology/network runtime, MBES construction/room/facility-network runtime, crafting/repair ledger, salvage ledger, economy ledger, Project/time ledger, combat outcome runtime or World/Environment truth store.

This keeps OARC-02 through OARC-07 focused on the actual closure problem: making existing operational-asset content traverse the existing owners correctly and proving where it cannot yet do so.

## Source basis

This contract is grounded in the completed MRCS-13 work state; MIB program/MIB-14 foundation boundaries; PPIA-04 vehicle/mecha/starship specification and source inventory; completed SMB-05/06 base/vehicle boundary proofs; LSS ownership rules; and the owner-approved but not-yet-authorized MERA and MBES programs/backlogs.
