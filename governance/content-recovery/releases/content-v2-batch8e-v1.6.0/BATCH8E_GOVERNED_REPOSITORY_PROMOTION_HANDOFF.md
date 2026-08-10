# Content v2 Batch 8E — Governed Repository Promotion Handoff

**Work item:** `CONTENT-V2-BATCH8E-PROMOTION`  
**Attempt:** `CONTENT-V2-BATCH8E-PROMOTION-attempt-001`  
**Repository:** `cybalicistjt-stack/multiversal-aioc`  
**Branch:** `content-recovery/batch8e-governed-promotion`  
**Owner authorization:** Explicitly approved 2026-08-10.

## Promotion input

Full portable release candidate:

- `MULTIVERSAL_CONTENT_V2_CROSS_DOMAIN_CLOSURE_PORTABLE_RELEASE_BATCH8E_PACKAGE_v1.6.0.zip`
- SHA-256: `f9d0d04334ae0c4ef75bbe8ceb466a468a77a88aed54849db697965bec331d3e`
- Size: 18562968 bytes
- Portable validation: 22/22 blocking gates PASS

Repository promotion projection prepared from exact-copy release files:

- `CONTENT_V2_BATCH8E_GOVERNED_PROMOTION_COLLECTION_v1.0.0.zip`
- SHA-256: `660a2a7b2ca8301e64d992bcf759b8ca29e7b4a52f09c681ed5ae2c58a1733c0`
- Size: 1026921 bytes
- 50 exact-copy files covering canonical identities/Ability registries, World/Setting content, Environment, Branch, Empire, relationship ledgers, unresolved/deferred boundary, and release receipts.

## Governing constraints

1. Preserve the existing 487-record certified canonical collection; do not overwrite it.
2. Promote Batch 8E as a separately governed recovered-content collection.
3. Preserve stable IDs and exact source evidence; do not silently rewrite IDs or source bytes.
4. Preserve all explicit unresolved states.
5. The 1,671 R1 candidates remain an open owner-decision queue; this promotion does not disposition them.
6. This promotion does not claim Public Canon 1.0 completeness.
7. This promotion does not authorize production/public deployment.

## Exact repository target

`governance/content-recovery/releases/content-v2-batch8e-v1.6.0/`

Required repository files:

- the exact governed promotion ZIP above;
- this handoff;
- `BATCH8E_PROMOTION_INPUT_MANIFEST.json`;
- `BATCH8E_CROSS_DOMAIN_CONTENT_CLOSURE_REPORT_v1.6.0.md`;
- `BATCH8E_CROSS_DOMAIN_METRICS_v1.0.0.json`;
- `BATCH8E_CROSS_DOMAIN_VALIDATION_v1.0.0.csv`;
- `UNRESOLVED_DEFERRED_QUEUE_SUMMARY_v1.0.0.csv`;
- `PACKAGE_MANIFEST.json`;
- `SHA256SUMS.txt`.

## Current execution boundary

The current ChatGPT GitHub connector can commit UTF-8 repository text but does not expose a file parameter that can consume the mounted local ZIP bytes. The exact-byte promotion ZIP therefore must be copied using Codex or another real repository checkout/file-capable execution surface.

Do not mark this attempt complete until the ZIP exists at the target path, SHA-256 `660a2a7b2ca8301e64d992bcf759b8ca29e7b4a52f09c681ed5ae2c58a1733c0` is verified on the exact PR head, targeted validation passes, and the PR is merged.

## Exact continuation

1. Copy the promotion ZIP byte-for-byte to the target directory.
2. Verify SHA-256 `660a2a7b2ca8301e64d992bcf759b8ca29e7b4a52f09c681ed5ae2c58a1733c0`.
3. Reconstruct/inspect the 50 exact-copy files and run the packaged Batch 8E portable validator against the full release source when available.
4. Add/run targeted CI that verifies the promotion ZIP hash plus the committed manifest/report/validation boundaries.
5. Merge only after exact-head validation passes.
6. After merge, treat Batch 7A→8E content consolidation as governed repository-promoted. Production Content Library migration remains separately gated.
