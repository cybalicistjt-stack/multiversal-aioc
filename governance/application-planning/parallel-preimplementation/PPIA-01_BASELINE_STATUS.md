# PPIA-01 Corrected Baseline Status

- PPIA-01 content authority is the later 8E-009 CSV-first registry, not the earlier 487-object semantic-parse database.
- Repository `Csv.zip` contains the governed 20-dataset / 19,199-row source set and is the executable audit authority.
- `MV_Master_01_Core.zip` retains supporting copies of all twenty CSV datasets with matching row and column counts.
- Final 8E-009 reconciliation records 19,199 promoted rows, zero unprocessed rows, and zero partial datasets.
- A deterministic PPIA-01 scanner is now present at `scripts/audit-ppia01-csv-content-quality.py`.
- The first scanner pass is designed to distinguish source-unspecified fields, governed inference/estimates, explicit missing definitions, missing effect text, omitted quantitative values, structural blanks, and same-name groups without auto-merging them.
- The earlier 487-object semantic database is excluded from PPIA-01 quality counts and is documented as a retirement candidate whose current AIOC consumers must be migrated before deletion.

The next evidence step is exact GitHub CI execution against repository `Csv.zip`, followed by preservation of the generated high-priority source-gap register and source-backed repair work.
