# MERA — Multiversal Engineering, Refit & Assembly

**Program ID:** MERA  
**Status:** ACTIVE — MERA-07 IN_PROGRESS; PDCP-REDUCED  
**Activation:** after GPR effective golden gate under `ROADMAP_DEPENDENCY_GRAPH.json`  
**Successor:** MBES-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-09-11  
**Implementation authority:** MERA-07 only on `work/mera-07-repair-wear-maintenance-emergency`

## Purpose

MERA is the governed player/GM engineering orchestration layer for inspecting, diagnosing, proposing, disassembling, repairing, refitting, calibrating, testing and returning complex Assets to service. It composes existing Item/Asset, salvage, crafting, vehicle/mecha/starship, Project, Profession, economy, rules/content and built-environment owners; it does not replace them.

The core gameplay loop remains:

`inspect → diagnose → propose → source/recover → isolate/disassemble → repair/replace/modify → install/reassemble → calibrate → test/accept → return to service`

MERA does not require 3D rendering or a physics sandbox. Schematic and semantic operation is the blocking baseline.

## PDCP reduction

Historical baseline: **24** planned tranches.  
Effective implementation/proof plan: **10** tranches.  
Standalone future tranches removed: **14**.  
Capability loss detected: **no**.

Authoritative reduction artifacts:

- `governance/application-planning/preimplementation-design-closure/PDCP_MERA_FAMILY_DESIGN_CLOSURE.md`
- `governance/application-planning/preimplementation-design-closure/PDCP_MERA_REDUCTION_RECEIPT.json`

The historical baseline remains provenance. Future governed execution uses only the reduced strict order in `MERA_PROGRAM_BACKLOG.json`.

## Engineering-resolution ladder

`Asset → system → assembly → subassembly → component → interface/connection → governed network`

Definitions may stop at any supported level. Unknown lower-level detail is never invented to satisfy UI, diagnostics, compatibility or simulation.

## Existing authorities consumed

- **PPIA-03 / D17:** Item/Asset identity, ownership, condition, installation/modification and history.
- **LSS:** decomposition, salvage, partial stripping, donor components and cannibalization lineage.
- **MIB-12:** repair/refurbishment/remanufacture/fabrication/transformation transactions.
- **MIB-13:** prices, markets, trade and services.
- **MIB-14 + PPIA-04/F014:** vehicle/platform/base/mecha/starship definitions, configuration and operational foundations.
- **APW/D26:** Project/task/participant/prerequisite/time/cancellation truth.
- **DPL/Profession:** Character engineering/mechanic capability and profession truth.
- **MRCS:** reusable engineering/component/interface/compatibility/work-recipe definitions.
- **GPR + Action/Event:** reusable gameplay execution, authoritative receipts and replay.
- **ARI/PCA:** common identity, rights, provenance, review/version/import/export infrastructure.
- **PCA-12 + PDCP Packet 08:** generic analysis/formal-validation machinery.
- **PDCP Packet 07:** shared proposal/preview/dry-run/commit/explanation/intervention/recovery semantics.
- **Reduced MBES:** workshop/garage/hangar/built-facility/infrastructure context.

## Reduced implementation order

### MERA-01 — Engineering Workspace, Topology, Authority & Resolution Core

Absorbs historical `01+02`. Implements the engineering workspace, stable topology projections, resolution-depth behavior, permissions, proposal/live distinctions and owner-binding shell.

### MERA-03 — Configuration Proposal, Compatibility, Blueprint & Interchange Adapters

Absorbs historical `03+04+23`. Implements engineering-specific configuration diff/proposal, compatibility/interface/adapter/substitution evaluation, reusable blueprint/preset/loadout references and domain serializers over Packet-07 and ARI/PCA common infrastructure.

### MERA-05 — Diagnostics, Calibration, Test & Acceptance Runtime

Absorbs historical `05+09+22`. Implements permission-safe inspection/fault isolation, calibration/tuning, engineering test/shakedown/acceptance evidence and MERA interpretation of PCA-12/Packet-08 analyses.

### MERA-06 — Isolation, Access, Safe Disassembly & Recovery Handoff

Retains historical `06` and residual integration from `17/18/19`. Implements owner-defined access/isolation/de-energization/depressurization/support prerequisites, disassembly sequencing and typed handoff to LSS/MIB-12. MERA never invents salvage output.

### MERA-07 — Repair, Wear, Maintenance & Emergency Engineering

Absorbs historical `07+08+20` plus residuals from `17/18/19/21`. Implements profile-driven repair classes, wear/service interpretation, maintenance, field patches, bypasses, substitutes and jury-rigs without universal penalties or bonuses.

### MERA-10 — Dependency, Network, Failure & Graceful-Degradation Runtime

Absorbs historical `10+11`. Implements engineering-domain dependency/network/failure semantics for accepted power/fuel/heat/fluid/ammunition/data/control/magical interfaces. Generic graph/constraint machinery comes from PCA-12.

### MERA-12 — Item, Weapon, Armor, Tool & Equipment Engineering Adapters

Retains historical `12`. Implements Item/equipment engineering over PPIA-03/D17/MIB-12/MRCS without a second Item or crafting engine.

### MERA-13 — Vehicle, Mecha & Starship Engineering Adapter Pack

Absorbs historical `13+14+15`. PPIA-04 already governs Vehicle/Mecha/Starship as one semantic experience family; MERA supplies one engineering adapter substrate with target-specific profile packs rather than three engines.

### MERA-16 — Machinery, Robotics, Constructs & Industrial-System Engineering Adapters

Retains historical `16`. This stays distinct because machinery/robotics/construct/industrial systems may bind owner, autonomy/control and facility contexts that are not PPIA-04 Vehicle semantics.

### MERA-24 — Golden Cross-Domain Engineering Proof & MBES Handoff

Retains historical `24` and all removed-tranche proof obligations.

## Removed standalone runtimes

### Historical MERA-17 / MERA-18

Canonical salvageability, decomposition, donor lineage and cannibalization remain LSS responsibilities; refurbishment/remanufacture/fabrication/repair transactions remain MIB-12 responsibilities. MERA keeps only planning, compatibility, sequencing, handoff and proof in `06/07/24`.

### Historical MERA-19 / MERA-21

Worker capability remains DPL/Profession; work Projects/time remain APW/D26; garage/hangar/fleet and vehicle/platform context remains MIB-14/PPIA-04; built workshop/facility context remains reduced MBES. MERA consumes these as prerequisites and work-order bindings in `06/07/13/16/24`.

## Engineering invariants

- Definition, blueprint/proposal, Asset instance, installed configuration, operational state, diagnostics, analysis and presentation remain distinct.
- Unknown is not zero, absent, unlimited, compatible, safe or available.
- Preview/simulation is not mutation.
- A successful repair transaction does not automatically satisfy required acceptance testing.
- LSS remains salvage/decomposition authority.
- MIB-12 remains repair/refurbishment/remanufacture/fabrication authority.
- PPIA-03/D17 remain Item/Asset identity and condition authority.
- MIB-14/PPIA-04/F014 remain Vehicle/Mecha/Starship definition and live-operation authority.
- APW/D26 remains Project/time authority.
- DPL remains Character work/profession authority.
- MRCS remains reusable engineering-definition authority.
- PCA-12/Packet-08 own generic analysis machinery.
- Packet-07 owns generic preview/dry-run/explanation/recovery semantics.
- ARI/PCA own common provenance/version/review/interchange infrastructure.
- No universal compatibility, reliability, wear, salvage-yield, repair-quality, jury-rig, failure or tuning formula may be invented.
- No real-world engineering or safety claim is implied by game-rule simulation.
- No 3D renderer or paid/cloud provider is required for blocking workflows.
- Optional AI is advisory only.
- No MERA implementation authority exists until OPS3 governed-start selects a surviving MERA work item.

## Golden proof

`MERA-24` must prove at minimum:

- a damaged ordinary Item inspected, diagnosed, repaired, tested and returned to use;
- a weapon/armor proposal saved before commit and revalidated at commit;
- a compatible donor component recovered through LSS and installed without duplicating provenance;
- a vehicle/mecha/starship engineering flow over the shared PPIA-04 adapter family;
- a machinery/robotics/construct flow proving the separate non-PPIA-04 adapter seam;
- a temporary/jury-rigged repair whose effects come only from governed definitions;
- partial teardown preserving unrecovered components and exact history;
- incompatible and unknown-source configurations failing closed without fabricated facts;
- DPL/Project/tool/workstation/facility prerequisites routed through their owners;
- network/dependency/failure analysis bounded to declared topology;
- PCA-12 analysis remaining noncanonical;
- lost-response/idempotent recovery without duplicate consumption or installation;
- provider-off local operation and equivalent nonvisual operation;
- handoff into reduced MBES without MBES rebuilding the MERA engineering kernel.

The family DCP records **48 golden validation vectors** (`MERA-PDCP-001..048`).

## Roadmap placement

Cross-program activation remains governed by `ROADMAP_DEPENDENCY_GRAPH.json`. `MERA-01` remains the family start/rotation milestone and `MERA-24` remains the golden/MBES handoff milestone. Historical roadmap prose remains provenance only where it disagrees with the current DAG or PDCP-reduced strict order.


## MERA-01 completed workspace/topology result

MERA-01 completed_verified with published contract `MERA-01.1`. The engineering workspace grants no mutation authority, preserves D17/PPIA-03 Asset identity, projects only source-supported topology depth, retains unknown/conflict explicitly, filters visibility before counts/graph construction, keeps proposal state noncanonical, and pins owner versions without creating a second Asset/component ledger.

Causal RED run `35556187396` at `7638813e26be8ec5399c99ef97cd957275e56d40`; first implementation-head exact GREEN run `35556316867` at `e8ecbb1ceee8f37b3f7cfd6f50e6b193fa0fed77`; application publication PR #675 as `6c64b6f94c63061f6a5f582dd949a1c6d2d3d690`.

MERA-03 is selected_not_started. Its closeout must reconsult the cross-program DAG because MBES-01 rotation becomes eligible once MERA-03 joins already-completed MRCS-14.


## MERA-03 completed configuration/interchange result

MERA-03 completed_verified with published contract `MERA-03.1`. Configuration proposals remain noncanonical; compatibility is explicit/versioned and never inferred from names; unknown/conflict fails closed; explicit adapter rules are bounded; blueprints require target-specific permission/version/compatibility revalidation; ARI/PCA retain generic interchange/provenance/rights/version/review authority; optional AI has no commit/publication/owner authority.

Causal RED: run `35556956815` at `3705158ef40abc1c832d4bb5aa3b14517f9c4c51`. Exact-head GREEN: run `35557070342` at `0236803753934d6516b9800bf3cb66c82736ca3b`. Published application: PR #676 as `a5c31694b58e010241e636be76aaf0d97b007fbf`.

Fresh roadmap reconciliation found the MBES-01 rotation milestone is satisfied, but MBES remains blocked by authoritative `hard_requires: ["MERA"]` until the MERA program completes and by MBES `activation_after: MERA-24`. MERA-05 is therefore selected_not_started.


## MERA-05 completed diagnostics/calibration/acceptance result

MERA-05 completed_verified with published contract `MERA-05.1`. Diagnostic evidence preserves symptom/suspected/isolated/identified distinctions and filters hidden fault truth before projection. Calibration/tuning is restricted to authored adjustable state and cannot invent unsupported capability. PCA-12/Packet-08 results remain noncanonical analysis evidence; unknown, timeout and unsupported results stay inconclusive.

Repair receipts remain owner history rather than acceptance. Acceptance is separately governed by explicit test definitions and owner-authored certification requirements; failed acceptance preserves prior successful owner receipts. Provider-off semantic/nonvisual and keyboard-capable operation remains blocking baseline.

Causal RED: run `35557606982` at `357b77882a49cd29e7b9dbb4e0880b38d94f86c8`. Exact-head GREEN: run `35557691915` at `f2a5969e38b894855b0d442873477c94e2dd1912`. Published application: PR #677 as `13dafa2a92aab021e74f9a92b7743534ccc667fa`.

Fresh roadmap reconciliation supplies no interstitial successor override. MERA-06 is selected_not_started. MBES remains blocked until MERA completes at MERA-24.


## MERA-06 completed isolation/disassembly/recovery result

MERA-06 completed_verified with published contract `MERA-06.1`. Owner-authored access/isolation prerequisites are revalidated against permission and D17 owner version; hidden requirements are filtered before aggregation and missing authored rules remain unresolved. Ordered disassembly stays noncanonical. Partial completion preserves exact owner receipts and pending steps without invented rollback.

LSS retains recoverability/decomposition/salvage/donor-lineage authority, and MIB-12 retains repair/refabrication transaction authority. MERA-06 emits typed handoffs only and performs no canonical owner mutation.

Causal RED: run `35558237964` at `7caddf40804673d9e75b60f75c7e2ea518a83b01`. Exact-head GREEN: run `35558334892` at `2af0d9302253bcdd96398e77b35da7f1ba022a6a`. Published application: PR #678 as `312b35e5a3dbd268611c46e3572afda550104477`.

Fresh roadmap reconciliation supplies no interstitial successor override. MERA-07 is selected_not_started. MBES remains blocked until MERA completes at MERA-24.
