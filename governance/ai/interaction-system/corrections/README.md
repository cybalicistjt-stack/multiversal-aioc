# Multiversal Correction-to-Regression Intake

**Work item:** MV-CONT-004  
**Status:** governed implementation

This package converts an explicit, materially reusable owner correction into a durable minimized correction record and a deterministic proposed regression case.

## Lifecycle

1. **Immediate repair** — correct or explicitly block the current work and record evidence.
2. **Capture** — `capture` validates a minimized intake, derives a stable fingerprint, suppresses duplicates, and atomically adds one correction plus one proposed candidate.
3. **Review** — `review` requires owner authority and durable evidence before approving or rejecting the candidate.
4. **Promotion** — `promote` requires an approved candidate, an unused evaluation-case ID, and promotion evidence before adding the case to the canonical promoted-evaluation extension.
5. **Validation** — CI verifies privacy, referential integrity, status transitions, coverage closure, and that promoted cases exactly match their reviewed candidates.

## Privacy boundary

Raw messages, transcript excerpts, conversation titles, and attachment contents are prohibited. `source_ref` is opaque. Summaries and case text must be minimized paraphrases. The public repository stores no private conversation transcript.

## Idempotency and concurrency

A canonical SHA-256 fingerprint excludes capture time and evidence wording. Repeated capture of the same correction returns the existing correction and candidate IDs without mutation. Repository branches and normal pull-request review remain the concurrency boundary for remote writes.

## Commands

```bash
python tools/correction_regression.py validate
python tools/correction_regression.py capture --input correction.json
python tools/correction_regression.py review --candidate-id MV-REG-... --decision approved --reviewer john-brandon-turner --evidence "owner approval reference"
python tools/correction_regression.py promote --candidate-id MV-REG-... --case-id MV-EVAL-016 --evidence "promotion PR or decision reference"
```

Capture is automatic once a structured material correction is supplied. Canonical promotion is deliberately governed and cannot bypass owner review.
