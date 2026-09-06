# Application Implementation Roadmap — VTI-06 Governed Start

**Work item:** VTI-06 — Scene, Map, Token & MAI Bridge  
**State of this commit:** acceptance-only governed-start contract; production mutation remains locked pending genuine matching application RED.  
**Application baseline:** `e9ddbf9c763faca74689cb3776ad21501c341ba5`  
**Implementation branch after this exact-head reconciliation validates and merges:** `integration/vti-06-scene-map-token-mai-bridge`

## Exact-head baseline reconciliation

The governed start was validated while application `main` was `4bd061a87852f4bb4b17f5d500ae6ab85081c72b`, tree `8e9942b47cb5231816d4584397d460eaec522846`. Before the VTI-06 application branch was created, `main` advanced through `973490e8358fe0a48dad43933ac3675acd188303`, which added only a one-character `placeholder` file, and `e9ddbf9c763faca74689cb3776ad21501c341ba5`, which removed only that file. The current `e9ddbf9c...` tree is again exactly `8e9942b47cb5231816d4584397d460eaec522846`. This is therefore an exact-head reconciliation only, with no semantic, authority or scope change. IC-13 remains historically anchored to `4bd061a...`.

## Bounded objective

VTI-06 projects existing canonical Multiversal Scene, map-version, placement, MAI/ISE/SSA asset and semantic-spatial state into provider-neutral external VTT scene/map/token presentation semantics. It does not create a second spatial model and does not make an external VTT authoritative for rules, assets, visibility or canonical game state.

## Acceptance-only authority opened by this governed start

- create the registered VTI-06 application branch from the exact application baseline only after this AIOC exact-head reconciliation merges;
- add the bounded VTI-06 acceptance profile, fixtures, invariant verifier and tests;
- define provider-neutral acceptance envelopes for canonical Scene, map-version and placement projection;
- prove expected absence of the VTI-06 production bridge by genuine matching Linux and Windows RED before production mutation authority opens.

## Production authority remains locked until matching RED

The following remain unauthorized before matching RED is sealed:
- production scene/map/token/MAI bridge implementation;
- new or replacement canonical scene/spatial/map/token/wall/door/lighting/grid/elevation/asset semantics;
- provider-specific schemas, vendor selection/ranking, credentials, external accounts or adapter implementation;
- live external synchronization mutation or canonical game-state mutation;
- hidden-information bypass or permission weakening;
- durable VTI persistence or a new migration;
- provider activation, tester distribution, release or deployment;
- VTI-07+ and SGC-01+ implementation.

## Native-authority reuse requirement

VTI-06 must reuse the application's existing Scene, SceneMapVersion, ScenePlacementRecord, launch-snapshot/map-binding, visibility/authorization projection and MAI/ISE/SSA semantic-asset/construction-role authorities where applicable. Unsupported target-VTT fidelity must remain explicit rather than being invented.

## Exact next action after this reconciliation merges

Create `integration/vti-06-scene-map-token-mai-bridge` from exact application main `e9ddbf9c763faca74689cb3776ad21501c341ba5`, add acceptance-only VTI-06 validation, and obtain genuine matching self-hosted Linux/Windows RED before any production bridge code is authorized.
