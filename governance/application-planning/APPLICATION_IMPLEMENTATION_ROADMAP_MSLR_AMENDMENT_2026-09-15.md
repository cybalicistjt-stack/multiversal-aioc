# Application Implementation Roadmap — MSLR Amendment

**Date:** 2026-09-15  
**Program:** MSLR — Multiversal Spatial Law Runtime  
**Status:** owner-approved planned; future interstitial  
**Operational authority:** none

## OPS3 reconciliation

This amendment was created through the OPS3 canonical door. `operations/CURRENT.json` remains the only live selector and was not changed by this planning amendment.

At registration time, OPS3 state revision 47 selects **MAS-03 — Adventure, Scene, Encounter & Set-Piece Assembly** as `selected_not_started`, with no implementation branch and no implementation authority until a future owner `Continue` governed-starts MAS-03. MSLR does not change that selection and has no current implementation authority.

`governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json` remains the current cross-program planning authority.

## Placement decision

MSLR is inserted between MBES and MSWI:

`GPR → MERA → MBES → MSLR → MSWI → SMB-08`

This placement is dependency-driven rather than merely thematic:

- SSA already supplies completed semantic spatial topology and authoring foundations.
- ENV already supplies completed multiversal environment contexts such as Reality Instability, Dimensional Bleed, Portal Activity, Temporal Instability and Dream Influence.
- MCS will supply cartographic/interior/topology projections.
- GPR will supply generic gameplay execution and composition.
- MERA and MBES complete engineering, built-environment and settlement substrates that anomalous spatial laws may affect.
- MSLR then supplies specialized player-facing spatial-law runtime behavior.
- MSWI consumes MSLR's typed spatial observations/events/deltas for broader systemic consequences.

Placing MSLR before MERA would create an artificial dependency because MERA can validly operate without impossible-space gameplay. Placing MSLR after MSWI would force MSWI to close without the specialist spatial runtime it should integrate. The MBES → MSLR → MSWI seam is therefore the narrowest causal placement.

## Roadmap registration

The authoritative dependency graph is amended so that:

- node `MSLR` exists with `implementation_authority=false`;
- `MSLR.hard_requires=["MBES"]`;
- MSLR governed start requires `MBES-24`, `GPR-16`, `MCS-21`, `SSA-10`, `ENV-16` and the relevant World/Reality/Scene/Transition/Portal/Visibility/Knowledge/Action/Event owner contracts;
- `MSLR.golden_proof_requires=["MSLR-18"]`;
- the rotation gate for `MSLR-01` requires `MBES-24`, `GPR-16`, and `MCS-21` (SSA/ENV are already completed foundations and remain explicit start prerequisites);
- MSWI now hard-requires MSLR and requires `MSLR-18` at its start gate;
- MBES compatibility successor becomes `MSLR-01`;
- MSLR compatibility successor is `MSWI-01`;
- MSWI compatibility activation becomes `MSLR-18` and its upstream list includes MSLR completion.

## Program scope

MSLR contains 18 bounded tranches covering:

1. authority/crosswalk/runtime contract;
2. spatial-law profiles and composition;
3. dynamic topology state/replay/recovery;
4. true/observable/known/suspected topology projections;
5. observation/hypothesis/experiment/law discovery;
6. governed topology-changing operations;
7. fuzzy Reality boundaries/seams/bleed with traversability separation;
8. metric geometry profiles;
9. recursive scale and bigger-inside containment transforms;
10. orientation/gravity frames;
11. observer/knowledge/memory/perception-dependent connectivity;
12. temporal/dream/causal/looping spatial laws;
13. anchors/mapping/stabilization/counterplay;
14. constraint-driven procedural impossible-space generation and solvability proof;
15. liminal sensory anomaly grammar with accessible equivalents;
16. multi-resolution and cross-system spatial execution;
17. GM/Creator spatial-law studio and diagnostics;
18. golden impossible-space proof and MSWI handoff.

## Execution discipline

MSLR uses a 24-minute tranche target with at least 8 minutes reserved for closeout. A tranche is split before governed start if its implementation scope cannot credibly leave the closeout reserve intact. Once governed-started, one owner `Continue` carries the bounded tranche through implementation, required validation, verified closeout and next selection unless an OPS3 owner-only boundary or genuine external blocker is reached.

## Non-authorization

This amendment does not:

- start MSLR;
- grant an MSLR implementation branch;
- alter the live MAS-03 selection;
- start MSWI or SMB-08;
- promote recovered/pending source rules into canon;
- authorize paid/cloud dependencies, deployment or release.
