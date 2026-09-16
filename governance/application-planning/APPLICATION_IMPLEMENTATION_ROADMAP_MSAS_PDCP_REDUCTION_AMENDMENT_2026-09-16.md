# Application Implementation Roadmap — MSAS PDCP Reduction Amendment — 2026-09-16

**Status:** OWNER-APPROVED PLANNING RECONCILIATION  
**Program:** MSAS — Multiversal Sound & Audio Studio  
**Implementation authority:** none

## Decision

Replace the historical 21-tranche MSAS planning split with the PDCP-reduced 11-tranche implementation/proof order:

`MSAS-01 → MSAS-03 → MSAS-04 → MSAS-05 → MSAS-07 → MSAS-09 → MSAS-12 → MSAS-14 → MSAS-15 → MSAS-18 → MSAS-21`

Historical IDs remain provenance through `PDCP_MSAS_REDUCTION_RECEIPT.json`.

## Fold summary

- `01+02 → 01`
- `03` retained
- `04+16 → 04`
- `05+06 → 05`
- `07+08 → 07`
- `09+10+11 → 09`
- `12+13 → 12`
- `14` retained
- `15` retained
- historical `17` absorbed to PCA-09/PCA-08 generic generation/production owners plus domain adapters in `05/07/12/18`
- `18+19+20 → 18`
- `21` retained as golden proof

## Cross-family ownership

AAI remains audio semantic/runtime/interoperability authority. PCA-07/08/09/13 own reusable audio authoring, voice/SFX production, generic generation and localization primitives. ARI/PCA own generic rights/provenance/version/review/import-export. Packet 07 owns generic preview/live-GM control/debug semantics. MSAS owns the integrated audio-domain production, direction, voice, spatial and live-session UX over those substrates.

## DAG preservation

No `ROADMAP_DEPENDENCY_GRAPH.json` mutation is required. `MSAS-01` remains the family start milestone and `MSAS-21` remains the completion/golden gate consumed by MRCS and other roadmap surfaces. Sparse IDs are intentional.

## Cumulative PDCP effect

Historical PDCP baseline remains **208**. After this seventh complete family receipt the effective future count is **135**, with **73** standalone future tranches removed. No capability loss is recorded.

## Non-activation boundary

This amendment does not start MSAS, alter `operations/CURRENT.json`, activate paid providers, grant recording/streaming/publication rights, or change any canonical gameplay/audio state.

Next PDCP family review: **MNCS**.
