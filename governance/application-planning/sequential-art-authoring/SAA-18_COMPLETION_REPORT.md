# SAA-18 Completion Report

**Status:** `completed_verified`  
**Schema:** `SAA-18.1`  
**Application PR:** #736  
**Causal RED:** run `35720861636`, head `5d4d65584819123fa5124a272caf8e1e1c38d6f9`  
**Bounded repair run:** `35721112307`, head `97ab9e6177beb485130c968b9f40f37831ba92bf`  
**Validated GREEN:** run `35721344085`, head `86f99566d64f057f1e52f43592d80dadd556ef11`  
**Application merge:** `0f03a6055bf956fbfaf993641ef8b4e38416f788`

SAA-18 delivers deterministic comic-project package manifests and import/export handoff metadata. Stable SAA project/version identity, SAA-13 history lineage and SAA-17 accessibility identity are preserved.

Dependencies explicitly distinguish reference-only resources from embedded derivatives. Reference-only dependencies never gain source bytes. Embedded derivatives require byte-present ARI identity, explicit export rights, and redistribution rights when the package declares redistribution intent. Stale resource/rights versions, unavailable or incompatible dependencies, unsupported package versions and invalid embedding permissions fail closed.

The first implementation candidate exposed only a bounded TypeScript input-container mutability defect in failure-path fixtures; the contract logic was unchanged, the input container was repaired, and the repaired exact head passed both platforms plus deterministic comparison.

Packaging performs no canonical asset registration, sharing, publication, external upload, owner-truth mutation, fabricated permission, silent compatibility repair or version migration. SAA-19 — Advisory Authoring Assistance — is selected next but not started.
