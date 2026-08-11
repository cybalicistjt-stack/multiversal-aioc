# PPIA-01 — CSV-First Content Quality & Missing-Information Closure Audit

**Work item:** PPIA-01  
**Program:** PPIA — Parallel Pre-Implementation Advancement  
**Status:** ACTIVE  
**Owner/final authority:** John Brandon Turner

## Correction of audit authority

PPIA-01 does **not** use the earlier 487-object semantic-parse database as its content authority.

That database came from an earlier unsuccessful semantic parsing/recovery path and remains in the repository only because several AIOC operational surfaces still consume it. It is a compatibility/retirement concern, not the source set PPIA-01 is trying to improve.

The primary PPIA-01 content authority is the later CSV-first program completed under 8E-009.

## Primary audit source

Repository sources:

- `Csv.zip`
- `governance/object-system/csv-intake/CSV_INTAKE_AUDIT_SNAPSHOT.json`
- `governance/object-system/csv-intake/CSV_SOURCE_REGISTRY.json`
- `governance/object-system/csv-intake/OWNER_RECOMMENDATION_DELEGATION.json`
- consolidated P0/P1 tranche contracts and runners
- `governance/object-system/csv-intake/FULL_REGISTRY_RECONCILIATION_CONTRACT.json`
- `scripts/run-full-csv-registry-reconciliation.py`

Governed baseline:

- 20 CSV datasets
- 19,199 structured records
- exact duplicate rows: 0 at intake
- final registry reconciliation: 19,199 promoted rows
- unprocessed rows: 0
- partial datasets: 0
- deterministic canonical identities assigned through the governed tranche/reconciliation process
- raw CSV retained in the generated canonical records
- same-name rows preserved separately rather than auto-merged
- install/uninstall validation retained in the reconciliation process

The owner recommendation delegation remains active and permits bounded evidence-based recommendations where source values are incomplete, while forbidding fabricated source facts, citations, identifiers, relationships, or unsupported scope changes.

## Retained source copy

`MV_Master_01_Core.zip` preserves the same twenty CSV catalogs individually under `03_CSV_Sources/`. Their current retained copies reproduce the governed dataset row counts and column counts exactly, totaling 19,199 rows. They are supporting reference copies; repository `Csv.zip` remains the authoritative executable source.

## What “incomplete” means for PPIA-01

The later CSV work intentionally distinguished several states that must remain separate:

1. **Direct source fact** — explicit in the source and preserved.
2. **Governed inference/estimate** — an evidence-based reversible recommendation adopted under the owner delegation because the source omitted a value.
3. **Explicit source absence** — fields marked `Not specified in source`, `not specified in the PDF`, or equivalent.
4. **Published name/heading without definition** — the source names a mechanic or ability but does not provide its full definition.
5. **Published pricing/listing without effect text** — an identity exists but usable mechanics are absent.
6. **Unknown quantitative value** — source states an effect but omits the amount/value.
7. **Intentional not-applicable state** — `N/A`, `Not applicable`, `None`, or equivalent where the field does not apply; this is not automatically a gap.
8. **Distinct same-name source records** — possible variants/duplicates that remain separate until evidence supports reconciliation.

PPIA-01 prioritizes categories 3–6 for source recovery and categories 2 and 8 for review. Category 7 is not treated as missing information without field-specific evidence.

## Audit outputs

The deterministic scanner produces, per dataset:

- exact row and column verification;
- actual blank-cell count;
- explicit `Not specified in source` cell count;
- rows containing governed inference/estimate language;
- rows with explicit missing-definition status;
- rows whose source provides no effect text;
- rows whose source explicitly omits an amount/value;
- duplicate-name group count without automatic merge;
- a high-priority source-gap queue with exact dataset row, record ID, name, source PDF/page/section when available, and reason.

The scanner does not change content or decide that every source-unspecified field is required.

## First repair priority

The first source-recovery pass should begin with **explicitly incomplete published mechanics**, because those can often be resolved without redesigning systems:

- published abilities whose standalone definition/XP price is missing;
- published proficiency headings with missing definitions;
- published ability names with omitted cost/description;
- published ability listings whose source provides no effect text;
- explicit quantitative omissions such as “amount not specified.”

Only after that queue is resolved should PPIA-01 spend time replacing governed estimates or reviewing same-name records.

## Obsolete semantic database boundary

The repository `content-db/` 487-object database and its materialization/certification pipeline are **excluded from PPIA-01 content-quality counts**.

They are not deleted in this tranche merely because they are obsolete as content authority. Current AIOC consumers still reference them directly, including:

- `content-database.js`, which hard-codes the 487-record certified count;
- `bridge/mcp-server/src/server-v3.mjs`, which fetches `content-db/index.json`;
- content-database build/certification/promotion workflows;
- operational/development-brain surfaces that consume the repository content database.

Retirement therefore requires a bounded migration: replace those consumers with the current CSV-first registry or an appropriate compiled projection, validate AIOC behavior, then delete the obsolete semantic database and its dead pipeline in a separate cleanup operation.

## Completion gate

PPIA-01 is complete only when the repository contains:

- a deterministic 19,199-row quality baseline;
- a source-grounded cross-domain gap register;
- a prioritized repair backlog;
- source-backed repairs where evidence is sufficient;
- an unresolved-source register for gaps the retained sources truly do not answer;
- duplicate/variant review dispositions where needed;
- traceability from remaining gaps to the later PPIA/Stage A surfaces they affect;
- a final deterministic re-audit.

PPIA-01 does not activate A2, deploy/release the application, authorize tester access, or silently promote unsupported authored content.