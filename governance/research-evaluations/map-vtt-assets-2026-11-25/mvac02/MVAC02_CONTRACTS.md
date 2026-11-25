# MVAC-02 — Shared spatial and media integration contracts

25 November 2026. Completed for shared design and reference validation. Product implementation remains incomplete. Next recommendation: MVAC-03, the Author / Prepare / Play interaction shell.

The existing native Map Maker document remains the authoring authority. MVAC-02 adds a proposed versioned integration sidecar and explicit mappings into existing app contracts. It creates no replacement document system, second asset registry, combat ledger, inventory ledger, or account authority. The UHT28 application and seven MVAC-01 fixtures remain unchanged.

## What is already present and what this cycle adds

At pinned app commit `db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f`, ARI already describes resource handles, original-byte identity, use capabilities and the visual bridge to MAI. MAI already describes asset packages and placeables, coordinate projection, geometry candidates and owner integration plans/acknowledgements. These are useful contracts and pure helpers; their presence does not establish installed runtime integration. The shared-assets port is for gameplay items/vehicles and their ownership/custody/equipment, not a media catalog. Its directory README is stale relative to the actual port; this study uses the source file.

This cycle specifies the compatibility boundary between those owners and UHT28: stable native references, coordinate calibration, version pins, separate audience and license decisions, explicit failure states and recovery. A small executable reference oracle demonstrates expected outcomes. It is a design test, not a new production resolver or authorization service.

| Record | Authority / existing contract | Required separation |
| --- | --- | --- |
| Native map document | Native editor; map ID, revision, draft and source geometry | Save author intent; do not embed live encounter truth or assume viewport state grants access. |
| Prepared/live scene binding | Existing scene/session and account owners; MAI-09 integration intent | Pin native document revision, floor and owner references; draft and live scene revisions are independent. |
| Logical media resource | ARI-01 handle and existing ARI/PCA registration | Stable resource ID, source/provenance and capability evidence; distinct from a gameplay item. |
| Source bytes | ARI-02 original-byte SHA-256 binding | Identical bytes may serve several logical resources without merging rights. Reference-only has no fabricated digest. Storage locator remains owner-managed. |
| Representation / rendition | Existing media derivative lineage and MAI variants | Immutable byte digest, dimensions, alpha/color profile, recipe version and source identity. Do not overwrite the original or silently repoint a pinned rendition. Detailed manifest belongs to MVAC-06. |
| Placed artwork instance | Native feature/showcase element; MAI-02 placeable | Per-instance transform and visibility reference; no actor, door state, collision, world topology or vision truth inferred from artwork. |
| Gameplay object | Existing A5/A6/A7/D17 and shared asset owners where applicable | Bind existing stable identity/version; a token image does not create an NPC, item or vehicle. |
| Rights / audience policy | ARI capability evidence; account/session/GATE owners where applicable | License permission and audience authorization are separate necessary checks. A valid hash, purchase, import or local role switch grants neither. |

## Proposed extension envelope

`OBJECT_TRACES.json` contains four concrete design-sidecar records. The sidecar is separately versioned (`mvac02.design-sidecar.v1`) and keyed by native document ID/revision plus stable object identity and source pointer. It pins media resource, representation, pack version, rights evidence, coordinate space and floor, and references a gameplay owner only when needed. Source geometry is copied only as test evidence; an eventual runtime sidecar must reference the native owner and avoid a competing editable geometry copy.

A saved sidecar transaction must record native checkpoint identity and content digest, schema/features and dependency pins. A mismatching source revision cannot be silently rebound by array position. Resolve stable ID first, verify the pointer/identity, then require an explicit reviewed rebase if author changes invalidate the reference. Unknown optional metadata round-trips; unknown required features block activation. This cycle specifies these requirements; it does not implement transactional storage, automatic rebasing or schema migration.

No product code may take the design oracle's default `policyReceipt: true` as permission. The oracle uses synthetic inputs only. A real adapter requires a verified current owner policy result scoped to subject, campaign, scene, action, resource revision and audience, before any private payload or dependency metadata is emitted. A string supplied by a client is not a policy receipt.

## Coordinates, units and floors

Every spatial binding declares its coordinate-space ID and source basis. Native author units, map pixels, asset-local pixels, grid coordinates, normalized coordinates and physical units are different spaces. The MAI-03 helper uses explicit map dimensions and origins; this design chooses top-left origin, +x right and +y down for presentation pixels. Positive presentation rotation follows the existing transform math (clockwise on a downward-y canvas). This convention is not a world-coordinate authority.

For a chosen export frame, record `(minX,minY,width,height)`, output pixel dimensions and the exact affine transform. Mapping to pixels uses `(nativeX-minX)*outputWidth/width` and the equivalent y expression; it must remain independent of viewport zoom/pan and device-pixel ratio. Nonuniform scaling must be explicit; use an aspect-preserving frame for physical-distance exports. Grid rotation and a placeable's rotation are independent transforms and must not be copied into each other. Existing MAI grid projection descriptors do not contain a grid rotation field: use a separately declared outer affine transform and its inverse, or reject that unsupported rotated-grid export; never silently drop rotation.

Asset anchor is a fraction of asset dimensions. Transform order follows MAI-03: subtract anchor, apply scale/flip, rotate, then translate. Widths and heights must be positive and finite; singular transforms reject. A native point is not an asset anchor ratio. Distinct floors have explicit IDs and their own coordinate/calibration context. Local elevation offsets and meter-valued elevation metadata remain separate from feet/pixels; floor IDs imply no physical height, adjacency or travel permission. Non-Euclidean portal/topology relationships stay under their existing owners.

| Example | Native source | Calibration / allowed claim |
| --- | --- | --- |
| Archive door, F03 | `tidewatch:level:0-south-door-0`, point (6,8), `level:0` | `/draft/interiorFeetPerUnit` explicitly says 5 ft per native unit. This is author calibration, not gameplay distance authority. |
| Harbor City tree, F02 | `urban:1:5`, (7.61,4.201), size .296, cluster count 5 | Urban sketch units have no verified physical calibration here. Preserve count/seed/rotation; render preview, block physical-distance claims until calibrated. |
| NPC token, F04 | Synthetic binding at (4,3); no existing authoritative actor in frozen fixture | Synthetic placement only. Do not infer which of the fixture's square/hex/gridless definitions is active. Require explicit selected grid, calibration and existing actor-owner reference. |
| GM handout | Synthetic nonspatial private document media | No spatial transform or map distance; retain GM-only audience and separate reveal operation. |

The regional fixture's scale/sketch metadata is not automatically an affine physical calibration. Importing a pixel image cannot establish world distance or correct a floor mismatch. Before UVTT or another physical export, record selected grid, units, origin, transform and floor profile explicitly and validate the receiving tool in MVAC-17.

## Rights mapping and export decisions

| Source concept | Destination / required rule |
| --- | --- |
| ARI-01 `redistribute` | ARI-11 `redistribution`; explicit spelling adapter, never blind key copying. |
| ARI `allowed` | MAI permission `granted`, only for the corresponding action with retained evidence. |
| ARI `denied` or `revoked` | MAI `denied`; retain original revoked reason/evidence in the sidecar so revocation is not forgotten. |
| ARI `unknown` or absent | MAI `unknown`; block the affected operation. |
| ARI reference/private/campaign capabilities | MAI permissions have different granularity. No universal one-to-one mapping. Keep the original action-specific capability check and policy gate; broad `useInExperience` cannot grant session delivery on its own. |
| Flattened map export | Check map-output permission and audience, attribution and dependencies. It grants no permission to export raw source assets or packs. |
| Original/portable asset export | Require the applicable export and redistribution capability, authorized audience and actual verified bytes. Provider reference remains a reference unless its owner permits byte acquisition. |

The reference tests deliberately show a reference-only resource can be eligible for reference use while still lacking bytes for raw export. Equal byte digests never merge license provenance, account ownership or private delivery scope. ARI-11 restricts conflicting evidence; a revoked result wins over an allowed one. Session reveal policy and license grants remain independent.

GM-only records are excluded before a player projection is constructed, including labels, thumbnails, search results, counts, dependency names and URLs. A cosmetic hide flag or local role switch is insufficient. This is a required contract, not a privacy result proved by these local tests; MVAC-18/21 require actual authenticated delivery-boundary tests.

## Six-stage object traces

The HTML inspector and JSON contain all 24 object/stage explanations. The native door and tree are exact source references. The NPC and handout are clearly marked synthetic design examples, because the frozen maps provide no authoritative actor or handout records.

| Object | Create / save | Prepare / play | Export / recovery |
| --- | --- | --- | --- |
| Door | Keep native point/material/width/ID; save the sidecar reference separately. | Prepare an interaction candidate; existing scene owner validates an open/close request. Door drawing cannot change visibility/collision rules. | Export only authorized representation/profile; recovery queries ambiguous operation status before retry. |
| Tree cluster | Retain native `urban:1:5`, count 5, seed and per-instance overrides. | Resolve exact presentation/pack; missing physical scale permits artwork only. No implied blocker or harvested inventory. | Flattened output and source asset redistribution have separate rights. Reopen the same pinned version or show missing content. |
| NPC token | Bind an existing actor stable ID/version; synthetic reference stays explicitly synthetic. | Unresolved actor blocks gameplay. Existing owner accepts/rejects moves/actions and returns a versioned receipt. | Art export does not export private actor statistics. Restore presentation and resync authoritative actor state separately. |
| GM handout | Retain media/document owner, provenance and GM-only policy. | Preparation never reveals it. Reveal requires an explicit authorized owner operation and allowed media delivery. | Player exports omit private record and metadata. Recovery does not broaden audience or infer a reveal from local cache. |

## Revisions, updates and failure behavior

There are separate native document revision, scene preparation/live revision, owner object version, immutable representation version/digest and rights/policy evidence revision. One counter cannot substitute for the others. Pin expected versions on requests, and invalidate only affected bindings when a map or pack changes. Updates stage a candidate dependency closure; existing scenes continue on their last complete approved pins until reviewed activation. Unknown or incompatible mandatory features stop activation rather than partially upgrading.

| Failure / event | Required response |
| --- | --- |
| Missing pack/representation/source bytes | Keep source geometry and stable IDs; show a visible unresolved marker. Do not silently replace with a similarly named asset. Reference-only does not become byte-present. |
| Stale native/owner revision | Explain expected/current revision, refresh or explicitly rebase. No last-writer-wins gameplay overwrite. |
| Wrong floor/basis/unknown calibration | Block affected interaction or measured export. Cosmetic preview may continue only with the limitation visible. |
| Unsupported feature / variant version | Reject activation or export profile with a named reason and retain last-good pins. |
| Denied/unknown/revoked capability or missing audience policy | Block operation before delivery; preserve provenance. Cached bytes confer no new rights. |
| Owner action pending / ambiguous | Preserve operation ID and payload binding. Query authoritative status; do not issue a new operation ID as an automatic retry. |
| Accepted duplicate operation | Reuse the owner receipt for that same operation and payload; reject conflicting payload reuse. Idempotency belongs to the owner, not a second renderer journal. |
| Reordered event / reconnect | Verify owner sequence/revision, resync gaps and project only accepted events. Local author undo cannot undo committed gameplay. |
| Restore / relink | Restore native checkpoint and pinned references, then resolve dependencies and reconcile owner state. Content digest verifies bytes, not license or entitlement. Review substitutions. |

Detailed transactional ingestion, crash-safe pack activation, cache eviction/offline policy and portable restore remain MVAC-07/11/12/13; live action/reconnect proof remains MVAC-18/19/20/21. The reference oracle returns failure statuses only. It performs no mutation, authorization, storage transaction, download, owner request or network retry.

## Evidence and remaining work

71 checks passed with zero failures: seven pinned source-integrity checks, 26 executions of existing ARI/MAI helpers, 29 design-oracle/mapping cases and nine native-fixture/source-pointer integrity checks. The exact classification is recorded per check in `VERIFICATION.json`. The design oracle covers four ready examples and 20 negative/recovery examples. The seven original native fixture hashes remain unchanged; UHT28 is unchanged.

Pinned-contract execution covers ARI-01 handles/availability, ARI-11 conflicting and unknown rights, ARI-02 original byte deduplication/reference-only behavior, MAI-03 coordinate/anchor/flip/rotation round trips and singular input rejection, and ARI-16 presentation bridging without coordinate synthesis. Node strips TypeScript types from unchanged pinned source into test-only modules. This is executable pure-function evidence, not an installed-app build or a browser workflow test.

The HTML has a self-contained trace/case inspector; controlled DOM checks cover all object/stage/case selections and textual rendering. Actual browser layout/device/keyboard/accessibility acceptance remains open. All 40 broader MVAC-01 workflow/device tasks remain NOT_RUN. Creator visual review, real authenticated privacy, storage/network recovery, runtime owner receipts, physical devices, receiving-VTT imports and performance remain unproven.

MVAC-02 closes the shared design/reference-validation step only. No persistent lane, CURRENT selector or product implementation state changes. MVAC-03 is the next recommendation: build one canvas-first Author / Prepare / Play shell using these contracts, showing the selected object, scene revision, unresolved dependencies and local-preview role clearly.

## Pinned source references

These sources are repository evidence, not claims about released behavior:

- [ARI resource handles](https://github.com/cybalicistjt-stack/Multiversal-app/blob/db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f/packages/contracts/src/asset-resource-ingestion-reuse/universal-resource-handle-capability-contract.ts)
- [ARI byte identity](https://github.com/cybalicistjt-stack/Multiversal-app/blob/db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f/packages/contracts/src/asset-resource-ingestion-reuse/content-addressed-byte-identity-deduplication.ts)
- [ARI rights evidence](https://github.com/cybalicistjt-stack/Multiversal-app/blob/db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f/packages/contracts/src/asset-resource-ingestion-reuse/rights-license-use-capability-matrix.ts)
- [MAI asset/placeable contracts](https://github.com/cybalicistjt-stack/Multiversal-app/blob/db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f/packages/contracts/src/map-asset-interoperability/canonical-map-asset-placeable-package-contracts.ts)
- [MAI projection](https://github.com/cybalicistjt-stack/Multiversal-app/blob/db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f/packages/contracts/src/map-asset-interoperability/grid-coordinate-scale-projection-contracts.ts)
- [MAI geometry candidates](https://github.com/cybalicistjt-stack/Multiversal-app/blob/db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f/packages/contracts/src/map-asset-interoperability/layers-objects-overhead-occlusion-interactive-geometry-contracts.ts)
- [ARI/MAI bridge](https://github.com/cybalicistjt-stack/Multiversal-app/blob/db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f/packages/contracts/src/asset-resource-ingestion-reuse/mai-bridge.ts)
- [MAI owner integration](https://github.com/cybalicistjt-stack/Multiversal-app/blob/db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f/packages/contracts/src/map-asset-interoperability/world-scene-combat-exploration-creator-integration-contracts.ts)
- [Gameplay shared-asset port](https://github.com/cybalicistjt-stack/Multiversal-app/blob/db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f/packages/contracts/src/shared-assets/shared-asset-port.ts)
