# Project Feature / Family / App Dependency Map

**Status:** completion candidate

The machine-readable map is `PROJECT_FEATURE_FAMILY_APP_DEPENDENCY_MAP.json`.

## Layers

1. **Chronology/source layer** — preformal corpus, Phase 0/0.5, original Phases 1–9, Stage A/Internal Alpha/recovery lineages, OPS3/current convergence.
2. **Planning-group layer** — all 83 discovered `governance/application-planning/*` groups.
3. **Work-state family layer** — all 73 family prefixes recovered from 667 attempt files.
4. **Work-item layer** — all 662 unique historical/current work items.
5. **Canon/current-intent layer** — the 71 current canon/current-intent nodes from project archaeology.
6. **Application layer** — one Multiversal application root plus the 56 PCV-01 capability-surface rows and their explicit product-convergence targets.

## Edge semantics

- `member_of` — work item belongs to a work-state family.
- `lineage_parent` — family is documented by a planning group or non-application lineage.
- `contributes_to_app` — structural contribution only; not a runtime dependency claim.
- `product_convergence_target` — PCV-01 ledger explicitly assigns a capability family to a PCV target.
- `documented_downstream_consumer` — project archaeology/current canon explicitly names the consumer.
- `chronology_predecessor`, `stage_a_predecessor`, `strict_predecessor` — sequencing evidence.

A missing runtime-dependency edge is never silently inferred. It remains a gap to investigate if the owning work requires it.

## Coverage guarantee

The validator requires exact set equality with the frozen archaeology inventory for:
- 83 planning groups;
- 73 work-state families;
- 662 unique work items;
- 667 attempt files / 5 duplicate-attempt extras;
- 71 canon/current-intent entries;
- 56 PCV-01 capability rows.

This map is therefore an integrity index over existing authority, not a replacement roadmap.

## Attempt-record evidence

Every one of the 662 frozen work-item identities carries the exact current Git blob reference(s) for its historical `governance/ai/work-state/*-attempt-*.json` evidence. The registry verifies 667 frozen attempt records with exactly five duplicate-attempt extras and zero work items missing an attempt record. New PIM/PCV interstitial attempts live in the append-only current overlay and do not alter the frozen 662/667 archaeology counts.
