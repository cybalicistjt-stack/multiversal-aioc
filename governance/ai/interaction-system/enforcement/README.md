# Interaction Enforcement Controls

**Work item:** MV-CONT-003  
**Status:** Implementation candidate

This directory maps the redacted interaction audit to Project Bible and governance authority, records enforcement gaps, and supplies typed receipts for the highest-value missing controls.

## Files

- `CONTROL_COVERAGE_MATRIX.json` — all 22 patterns, authorities, existing controls, and target controls.
- `CONTROL_GAP_REGISTER.json` — prioritized gaps and residual risks.
- `EVALUATION_CONTROL_MAP.json` — all 15 evaluation cases mapped to controls.
- `CONTROL_RECEIPT.schema.json` — common receipt envelope.
- `CONTROL_RECEIPT.examples.json` — one valid example for each control type.
- `PROJECT_BIBLE_TRACEABILITY.md` — source-backed authority summary.

## Validation

```bash
python tools/interaction_enforcement.py validate
python -m unittest discover -s tests/interaction_enforcement -v
```

Policy-only coverage is not classified as enforced. Enforcement requires a deterministic representation, negative tests, and CI capable of failing.
