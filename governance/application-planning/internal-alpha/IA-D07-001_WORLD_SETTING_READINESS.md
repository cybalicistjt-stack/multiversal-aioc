# IA-D07-001 — World and Setting Management Readiness

**Decision:** IMPLEMENTATION-READY DESIGN  
**Owner:** John Brandon Turner

## Gate results

- Scope bounded to internal-alpha World and Setting Management.
- Stable identity, lifecycle, versioning, authority, and provenance are explicit.
- Hidden-information filtering precedes search, aggregation, export, diagnostics, notifications, and optional-AI context.
- Campaign-local overlays preserve source identity and require reviewed migration.
- Import/export, pack lifecycle, dependency, tombstone, concurrency, and recovery behavior are defined.
- Accessible list, tree, table, detail, timeline, semantic outline, keyboard, touch, screen-reader, responsive, high-contrast, reduced-motion, and nonvisual parity are required.
- Twenty-four deterministic fixtures and twenty-eight blocking acceptance criteria are present.
- Seven findings are resolved; zero blocking findings remain.
- `P9-06-008-attempt-002` remains unfinished and unmodified.

## Blocking acceptance criteria

WSM-AC-001 through WSM-AC-028 require, respectively: stable IDs; lifecycle enforcement; immutable published versions; expected-version writes; idempotency; role-separated authority; hidden-search protection; hidden-count protection; filtered exports; filtered diagnostics; filtered AI context; typed relations; acyclic hierarchy; semantic geography; Campaign version pinning; overlay/source separation; reviewed migration; import collision handling; dependency preview; pack disablement preservation; tombstones; autosave drafts; status lookup; Event-gap repair; keyboard parity; screen-reader parity; responsive parity; provenance and checksum preservation.

## Next

IA-D07-002 — MV-IA-F017 Adventure and Module Management.