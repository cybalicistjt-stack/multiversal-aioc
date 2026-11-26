# MVAC-05 — Asset provenance and action-specific rights

25 November 2026. Shared design and synthetic reference validation complete. Product rights enforcement is not implemented or certified. MVAC-03/04 browser and full-workflow acceptance remain open.

## Delivered in the same single-file prototype

`Multiversal_MVAC05_Asset_Provenance_and_Rights.html` retains the MVAC-04 map editor, renderer, illustrated artwork, seven native example documents, selection controls, undo and checkpoints. The new **Asset rights** button opens a review panel with nine synthetic resources and 54 scenarios. Its code/data are embedded in the HTML; no companion file, server, asset download or service is required. The optional evidence ZIP is for inspection/reproduction only.

The panel is a contract review. It changes no actual license, map, account, asset registration or runtime permission. The original four application scripts are byte-identical to MVAC-04. Native map Save is unchanged. This avoids pretending that sample policy logic is a production authorization service.

## Existing ownership and implementation seams

The app already has ARI resource handles (ARI-01), verified original-byte bindings (ARI-02), derivative lineage (ARI-03), use-capability evidence aggregation (ARI-11) and native/generated registration (ARI-18). MVAC-05 uses those owners. It adds an action-specific reference envelope and attribution obligations rather than a second catalog, rights registry or account system.

ARI-11 aggregates evidence conservatively across `allowed`, `unknown`, `denied` and `revoked`; missing evidence remains unknown. ARI-01 uses the spelling `redistribute`, while ARI-11 uses `redistribution`; an integration adapter must map these explicitly. Registration is not a license grant: the actual ARI-18 helper can register a resource with reference permission while export remains unknown.

Existing ARI/OCS/PCA owners retain provenance/rights registration. Account/session and GATE/MCB owners retain subject access, entitlement, allowances, offline and commercial policy. This design neither changes the subscription/allowance model nor assumes a purchase permits sharing.

## Evidence envelope

`RESOURCES.json` contains synthetic examples of these fields:

| Record | Required information and meaning |
| --- | --- |
| Logical resource | Stable resource ID and revision, media kind and visibility reference; distinct from a file hash and from a gameplay item. |
| Provenance | Creator or explicit unknown; source reference; evidence ID; retained import/purchase evidence. A receipt is stored as a fact, not converted into a grant. |
| License evidence | License/terms identifier, revision, source reference, evidence ID and terms digest. `recorded` means the sample has stated evidence; it is not a legal-clearance certificate. Unknown evidence stays unknown. |
| Broad capabilities | Existing ARI-11 evidence for private use, transform, campaign use, export, redistribution and commercial use. Each result retains its source evidence IDs. |
| Action-specific evidence | Exact action, evidence ID/source, resource revision, license revision, subject, permitted audience, campaign scope where applicable, commercial scope and expiry where supplied. |
| Attribution obligations | Required/not-required/unknown; exact required fields and values such as creator, title, source, license and change notice. Requirements come from evidence rather than a hard-coded assumption about all licenses. |
| Byte identity | Actual present/reference-only state, verified original digest and length when known. Digest equality does not merge logical ownership or grants. |
| Derivative dependencies | Parent resource, resource revision and license revision. The child cannot silently broaden a parent's permissions. |

Real ingestion must verify evidence through the existing owners and preserve original source metadata. The sample strings and local policy objects in this artifact are deliberately synthetic. A client-supplied `allowed` value or copied policy receipt is not proof of authority.

## Separate operations and decisions

| Requested operation | Broad capability checks | Additional explicit conditions |
| --- | --- | --- |
| Private use | private-use | Specific subject/self use evidence; current audience-policy result. A provider reference can remain a reference without claiming possession of original bytes. |
| Modify | private-use + transform | Modification evidence, actual source bytes and lineage obligations. No newly created distribution rights. |
| Session delivery | campaign-use | Explicit delivery permission for the campaign/audience, current audience policy, source bytes and applicable attribution. A provider link is not automatically permission to extract and deliver its bytes. |
| Flattened-map export | export + transform | Explicit finished-map output evidence, audience and attribution. This action does not grant raw source redistribution. |
| Raw asset / portable-pack redistribution | export + redistribution | Explicit raw distribution evidence for every included logical resource/dependency, audience policy, actual bytes and required attribution. |
| Commercial request | commercial-use in addition to the operation above | The action's evidence must also permit commercial scope. Commercial status alone grants no other action. |

Attribution is an obligation, not a general right to use an asset. Providing credit cannot turn an unknown/denied use into an allowed one. Conversely, an explicit no-attribution obligation does not waive the other action checks. A sample export with required credit stays blocked until the request includes it, and unresolved required fields remain unresolved.

The Wonderdraft vendor license example independently illustrates why finished-work distribution and standalone asset redistribution must be separate concepts. It is one vendor's terms, not a clearance for supplied sheets or other creators' packs. No automatic license-name parser or universal legal interpretation is introduced here.

## Decision and failure contract

The reference evaluator returns `permitted-by-sample-evidence`, `blocked` or `unresolved`, along with reasons, evidence traces and attribution output. Every result explicitly has `runtimeAuthorizationProved:false`, `ownerMutationPerformed:false` and `licenseInferred:false`.

Before evaluating license actions, the sample requires a separate audience-policy result scoped to subject, action, resource revision and campaign. GM-only sample media stays excluded from a player request. This models a necessary boundary; it does not authenticate the sample result or prove private delivery in a live system.

Unknown license/provenance, missing capabilities, stale license revisions, stale parent pins, missing bytes, missing parent records and unknown attribution produce an explicit unresolved outcome. Denied/revoked evidence, wrong subject/campaign/audience, missing audience policy, expired evidence and cyclic lineage block the affected request. No fallback to filename, purchase, prior import, similar artwork, matching bytes or an old grant makes the operation allowed.

Parent evidence is checked for the same output operation across the dependency closure, with cycle/depth bounds. A child carrying broad reuse evidence cannot export a private-only parent. This is a deliberately conservative reference contract. Real media workers and exporters must resolve the actual used dependency closure and owner evidence; they must not infer a legal grant from this test model.

Grant updates pin resource/license revisions. A derivative or prepared export must be reevaluated against current applicable evidence before delivery. Revocation blocks future modeled actions; this design does not claim to recall already exported files, encrypted/offline content or cached provider copies. Actual revocation, storage, authentication and offline behavior remain separate later acceptance surfaces.

## What is still unknown about the supplied asset sheets

The existing optional sheet manifest says no license document was supplied in that archive. MVAC-05 does not invent creator grants, apply a sample license to those images or authorize their raw redistribution. Their original bytes and provenance remain available for review, and the missing license evidence remains a fact to resolve before affected production uses.

This does not make any part of the HTML unavailable: its existing embedded data remains present. It distinguishes application packaging from evidence about which actions a production asset system may permit.

## Reference fixtures and proof

Nine resources cover private artwork, finished-map-only output, campaign-scoped delivery, attributed reuse, an unknown imported sheet, a provider reference without original bytes, a GM handout, a derivative with a private-only parent and revoked rights. Fifty-four declared scenarios have independently written expected outcomes across operations and negative cases.

127 reference/helper checks passed. They include the 54 decisions, negative attribution/scope/revision/expiry/lineage cases, actual pinned ARI-02 identical-byte bindings, ARI-03 source lineage, ARI-18 registration without inferred export rights and ARI-11 unknown/conflicting evidence. The original source-blob integrity check caught an extra trailing newline in a local copied contract; exact pinned bytes were restored and the final suite passed. The app contract source itself was unchanged.

66 review-interface checks passed, exercising every declared scenario against the delivered HTML script in a controlled DOM. All 33 MVAC-04 and 48 MVAC-03 regression checks passed against this HTML: 274 passing local checks in total. They validate local source/logic/native rendering only. Actual browser layout, keyboard/focus acceptance, authenticated users, storage/network delivery, provider extraction/entitlement, installed builds, legal clearance and physical devices are not certified.

`SOURCE_PINS.json` preserves exact app commit/blob/digest evidence. `DECISION_RESULTS.json`, `DECISION_MATRIX.csv`, `VERIFICATION.json`, `REVIEW_CHECKS.json` and prior-flow regression records preserve the decision and test boundaries. No private data or original third-party asset bytes are added by this study.

## Status and next step

MVAC-05 is complete for shared design and synthetic reference validation; `implementation_complete` remains false. The updated single HTML includes the review alongside all previous prototype behavior. Existing native documents, original asset data, CURRENT and persistent lane state are unchanged.

Next: MVAC-06, versioned asset/pack manifests with stable logical IDs, immutable representation digests, dependencies, anchors/scale, license/provenance references and explicit version compatibility. The HTML stays self-contained; this next design must not convert its existing embedded resources into required companion downloads without owner authorization.

## Source references

- [ARI-11 rights evidence aggregation](https://github.com/cybalicistjt-stack/Multiversal-app/blob/db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f/packages/contracts/src/asset-resource-ingestion-reuse/rights-license-use-capability-matrix.ts), blob `d16ac93f5f0086658c5093545f02eba44d9a425f`.
- [ARI-18 registration bridge](https://github.com/cybalicistjt-stack/Multiversal-app/blob/db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f/packages/contracts/src/asset-resource-ingestion-reuse/native-asset-registration-bridge.ts), blob `2a2a171f54b8299a48df8f57ccd3613724b23f58`.
- [Wonderdraft PACK_LICENSE.txt](https://github.com/Megasploot/Wonderdraft/blob/master/PACK_LICENSE.txt), observed blob `d6aa6646efae78b9805d24502be8352428495fe7`; vendor example only, not a grant for our supplied sheets.
- [Pinned NCG DAMC29 handbook](https://github.com/cybalicistjt-stack/NCG/blob/8f5baac1b5e7d273b23fde52c7122c9138b2b15d/docs/damc/handbook/DAMC29_PRACTITIONER_HANDBOOK.md), blob `d00c39dec087269b0804e585b0d3b61a9a0c5e4b`; research design, not product acceptance.
