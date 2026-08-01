# Multiversal Forensic Audit Runner

This runner audits the complete legacy corpus without assuming that rules or game objects appear only in obvious chapters.

## Authoritative corpus

1. `fullmv062926.pdf` — every page is scanned for prose, tables, formulas, examples, sidebars, lore-defined mechanics, adventure content, and named or unnamed game objects.
2. CSV files beneath the `aaaa` source — every row is treated as independent structured evidence and compared against both the PDF findings and the current canonical database.

## Run

```bash
python -m pip install pypdf
python audit/forensic_audit.py \
  --pdf sources/fullmv062926.pdf \
  --csv-root sources/aaaa \
  --canonical content-source/phase-1-8-canonical-objects.json \
  --out audit-output
```

The page ledger is append-only and resumable. Restarting the command skips pages already marked complete.

For bounded runs:

```bash
python audit/forensic_audit.py --pdf sources/fullmv062926.pdf --out audit-output --start-page 1 --end-page 250
```

## Detection policy

The runner combines:

- broad content-family terms;
- mechanical signatures such as dice, DCs, statistics, durations, ranges, actions, and per-scene limits;
- inline CSV/header detection;
- paragraph/chunk extraction;
- exact-name comparison against canonical stable IDs.

Automatic extraction and matching create candidates only. They do not establish canon.

## Outputs

- `page-ledger.jsonl` — checkpoint and page-level extraction counts.
- `findings.jsonl` — PDF evidence with page/chunk provenance.
- `csv-findings.jsonl` — standalone CSV evidence with file/row provenance.
- `audit-summary.json` — counts by family, source kind, and match state.
- `unresolved-review-queue.json` — findings not uniquely matched to an existing canonical object.

Later review passes add canonical diffs, duplicate groups, conflict decisions, and approved object candidates.
