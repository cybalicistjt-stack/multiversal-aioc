# RSR-01 — Archive Preservation, Extraction, Provenance & Disposition Completion Report

**Work item:** RSR-01  
**Archive:** `Now this.zip`  
**Archive SHA-256:** `2a5eae712f483d1fb33ff9fb0087e96c4eb8b71b287cc707c196a4c17a2f78f4`  
**Constituent MHTs:** 24  
**Visible extracted turns:** 102 (47 owner/user; 55 assistant)  
**Unique embedded media objects excluding auth avatars:** 12  
**Substantive unique embedded media:** 11  

## Result

RSR-01 preserves the exact archive identity and creates durable extraction, attribution, media-provenance and disposition indexes without promoting recovered assistant output to canon. Every one of the 24 MHT files has an exact checksum, a source-level disposition, a downstream route, and message-level attribution.

- `14` sources are `existing-needs-reconciliation`: current AIOC search found older recovery/content evidence outside the new RSR manifest, so later tranches must link/reuse rather than duplicate.
- `10` sources are `new-candidate`: current title/topic searches did not produce pre-existing evidence outside the newly registered RSR material. This is a review priority, not automatic canon.
- Assistant turns are always `assistant-generated-proposal` until independently supported or later owner-approved.
- User turns remain `owner-authored`; explicit corrections/constraints and owner-source-statement candidates carry additional flags.
- No user turn is asserted to be verbatim quoted pre-existing source unless that can be independently established.
- The repeated 7,929-byte JPEG found in all 24 exports is classified as a UI/non-substantive profile thumbnail; it is not counted among substantive media.

## Durable artifacts

- `RSR-01_EXTRACTION_RECEIPT.json` — exact archive/constituent checksums and extraction counts.
- `RSR-01_MESSAGE_PROVENANCE_INDEX.json` — all 102 visible turns with role/attribution flags and exact normalized-text hashes; owner text is retained in full while assistant proposal text is represented by a bounded excerpt plus exact hash/length, with full proposal text recoverable from the checksum-bound MHT.
- `RSR-01_MEDIA_PROVENANCE_INDEX.json` — unique embedded media checksums, sizes, MIME types, source occurrences and substantive/UI classification.
- `RSR-01_DISPOSITION_REGISTRY.json` — one explicit disposition and route per source, with representative pre-existing evidence paths where found.

## Authority boundaries

The original MHT/media bytes remain retained in Project Sources and are not reconstructed from these indexes. Existing canonical IDs must be reused when later reconciliation confirms a semantic match. Conflicts remain explicit. RSR-02 is next and owns World/Reality/Timeline reconciliation; no RSR-02 implementation begins inside RSR-01.
