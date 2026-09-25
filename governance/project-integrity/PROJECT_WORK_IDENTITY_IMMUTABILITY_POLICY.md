# Project Work Identity Immutability Policy

**Status:** completion candidate  
**Operational authority:** none; OPS3 `operations/CURRENT.json` remains the only live selector.

## Purpose

This policy prevents completed, historical, planned, superseded, deferred, or current work from disappearing or silently changing meaning as later maintenance rewrites roadmaps and governance.

## Immutable identity rules

1. A recorded era ID, planning-group ID/path, work-state family ID, or work-item ID is immutable once it appears in the Project Work History Registry.
2. Historical records are never deleted because their implementation was superseded, folded, reduced, or consumed by later work.
3. A rename is represented as an alias/supersession edge. The prior ID remains present.
4. A disposition change is represented by a new explicit revision/history record with evidence. It may not silently overwrite the fact that the prior disposition existed.
5. PDCP reductions/folds preserve both historical and effective tranche counts.
6. Multiple attempts remain distinct historical evidence; the unique work-item identity remains singular.
7. Current execution authority is never inferred from history, dependency maps, archived checkpoints, or Project Sources.
8. New work groups are appended. They must not reuse an existing ID for a different purpose.

## Dependency-map rules

- Structural containment/lineage is not runtime authority.
- Runtime/consumer dependency edges require source evidence.
- Unknown dependency is written as unknown/unresolved, never guessed.
- A downstream implementation may consume an older owner contract without renaming itself as that owner.
- Cross-family reuse must preserve one canonical owner per fact/state/mutation.

## Required change ceremony

Any legitimate change to a frozen identity or lineage requires:
- prior identity retained;
- new identity/revision stated explicitly;
- `supersedes`, `aliases`, or `reclassified_from` relationship;
- source/evidence reference;
- owner/authorized work item;
- validator update where the schema changes.

Git history is evidence, but this policy makes the preservation requirement machine-testable in the current tree.
