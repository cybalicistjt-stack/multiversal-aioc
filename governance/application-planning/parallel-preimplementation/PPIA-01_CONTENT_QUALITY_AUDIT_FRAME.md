# PPIA-01 — Content Quality & Missing-Information Closure Audit Frame

**Work item:** PPIA-01  
**Program:** PPIA — Parallel Pre-Implementation Advancement  
**Status:** ACTIVE — AUDIT BASELINE IN CONSTRUCTION  
**Owner/final authority:** John Brandon Turner  
**Application runtime mutation authorized:** false  
**A2 activation authorized:** false  
**Unsupported canonical promotion authorized:** false

## Purpose

PPIA-01 determines where Multiversal content is complete enough to support later application experiences and where content is structurally present but semantically thin, source-unresolved, provenance-incomplete, duplicated/ambiguous, or still absent from the current operational source set.

The audit is evidence-first. It must never fill a gap from general RPG knowledge, infer a missing rule because it seems obvious, merge same-name records automatically, or promote playtest/source-only material into canon without governing evidence.

## Authority surfaces

PPIA-01 keeps the following surfaces separate instead of treating their record counts as interchangeable.

### A. Current certified operational content database — primary PPIA-01 scan surface

- Repository surface: `content-db/`
- Database version: `3.0.0`
- Current certified full-object count: **487**
- Source digest: `sha256:11d3e26161a6ea1acbe8847d7c01c5f6fb09a9525dc2e2eba557d41b4c612fbb`
- Legacy inventory status: `QUARANTINED_CORRUPTED_SOURCE`
- Source transport retained in repository: `content-source/phase-1-8-canonical-objects.json.gz.b64`

These 487 records are the current operational canonical-object set. PPIA-01 audits their actual object bodies rather than assuming that certification means semantic completeness.

### B. Canonical schema registry — structural expectation surface

- Repository surface: `canonical-schema-registry.json`
- Registry ID: `mv.aioc.canonical-schema-registry.8d003`
- Base required fields: `id`, `objectType`, `recordLayer`, `schemaVersion`, `contentVersion`, `name`, `status`, `createdAt`, `updatedAt`, `spec`
- Object-type contracts include explicit required `spec` fields where defined.

The registry is used to identify structural incompleteness. PPIA-01 does not silently expand a schema contract beyond what the registry declares.

### C. Historical structured CSV corpus — source/recovery surface, not present operational canon

The governed CSV intake audit records **20 CSV datasets / 19,199 rows**. The CSV source registry explicitly states that structured rows are not canonical by themselves and require source verification, cross-file identity reconciliation, and governed promotion.

PPIA-01 may use these rows to recover evidence-supported missing information, but their existence does not make them current canonical records.

### D. 8E-008G source-coverage/provenance audit — source-boundary evidence surface

The retained 8E-008G audit established:

- 158,189 authoritative records provenance-accounted;
- 1,347 foundational inventory identities accounted for;
- 596 playtest-only identities intentionally outside the authoritative baseline;
- 168 source identifier dialects classified;
- **2,766 / 7,144 page-primary structural candidates lacked a formal disposition binding at that audit boundary.**

The 2,766 count means **unbound source sections**, not proven missing mechanics. A candidate may ultimately bind to a canonical record, duplicate/superseded source, intentional exclusion, supporting prose/example, or approved deferral.

### E. Original PDFs and retained structured catalogs — source-truth evidence

Original legacy PDFs and CSV catalogs retained in `MV_Master_01_Core.zip` remain supporting source evidence. Repository state controls current status; retained originals are consulted when a record-level repair needs exact source truth.

## Important certification finding

The current canonical content certification proves a bounded set of things: 487 records exist, IDs are unique, each record contains a `gameObject`, source digests match, and the legacy inventory remains quarantined.

It does **not** validate each `gameObject` against `canonical-schema-registry.json` or prove that the object contains the substantive fields needed by its domain contract. PPIA-01 therefore adds a quality/completeness audit without redefining canonical identity or bypassing the existing promotion pipeline.

## Gap taxonomy

| Code | Class | Meaning | Default handling |
|---|---|---|---|
| `PPIA01-Q0` | Integrity contradiction | Wrapper/object identity mismatch, duplicate stable identity, malformed record, manifest-count contradiction, or invalid source digest | BLOCK audit progression for affected record until repository evidence is reconciled |
| `PPIA01-Q1` | Schema structural gap | A current canonical object lacks fields required by the canonical schema registry, including required `spec` members where declared | Source-backed repair candidate; do not invent values |
| `PPIA01-Q2` | Semantic thinness | Object exists but carries little or no domain payload beyond identity/provenance | Compare against exact source/package evidence before repair |
| `PPIA01-Q3` | Provenance/binding gap | Source locator, page/anchor, archive/member, candidate disposition, or provenance chain cannot be resolved strongly enough to support a repair | Add to unresolved-source register; no authored fill |
| `PPIA01-Q4` | Identity/duplicate ambiguity | Same/similar names, overlapping sources, aliases, or conflicting IDs require reconciliation | Preserve variants/conflicts; never auto-merge by name |
| `PPIA01-Q5` | Source absence | The desired field/content is not supported by retained authoritative source evidence | Record as unresolved source absence; owner-authored proposal must remain explicitly noncanonical until approved |
| `PPIA01-Q6` | Support/readiness gap | Validation, balance, testing, presentation/profile, accessibility, or downstream feature support is absent or thin | Queue for the owning later tranche; absence does not by itself invalidate source content |
| `PPIA01-Q7` | Intentional exclusion/deferment | Playtest-only, source-only, duplicate, superseded, example/prose, intentionally excluded, or separately deferred material | Preserve disposition; do not “repair” into canon |

## Repair evidence classes

A content repair may be applied only when it is supported by one or more of these evidence classes and the chosen class is recorded:

1. **Exact current canonical package member** — strongest direct recovery source when a fuller object exists in a governed package.
2. **Exact original source citation** — PDF/page/section or structured-source coordinate that unambiguously supports the field.
3. **Existing canonical cross-record relationship** — another governed record explicitly provides the same stable fact and the relationship is nonconflicting.
4. **Owner-approved authored correction** — must be identified as owner-authored/owner-corrected and must not be fabricated by the audit.

Fuzzy heading similarity, generic genre knowledge, assumed defaults, or same-name matching are review evidence only and cannot independently satisfy a repair.

## Audit sequence

1. **Operational baseline scan** — scan all 487 current `content-db/objects/**` records against manifest identity, canonical base fields, registered object-type requirements, semantic payload depth, name collisions, and source-locator status.
2. **Domain prioritization** — rank current gaps by downstream leverage for PPIA-02 through PPIA-12 and Stage A work.
3. **Source binding** — for high-priority thin records, locate exact package/PDF/CSV evidence and assign Q3/Q5/Q7 dispositions where a repair cannot be proven.
4. **Source-backed repair batches** — apply only evidence-supported corrections, preserving stable IDs and provenance.
5. **Re-audit** — rerun the deterministic scan after each repair batch; report improved coverage without treating unresolved source absence as failure.
6. **Closure** — publish cross-domain gap register, prioritized repair backlog, unresolved-source register, source-backed completed repairs, and feature-surface traceability.

## Domain audit order

The first audit pass uses the following groups because they feed the approved PPIA sequence:

1. Abilities, progression, spells/powers, traits and Adaptations.
2. Character foundations, Species, forms and biology.
3. Items, weapons, armor, ammunition, tools, wearables and asset support definitions.
4. Vehicles, mecha, spacecraft and component systems.
5. Creatures, NPCs, hazards and encounters.
6. Conditions, resources, effects, action/range/target/duration profiles and shared mechanics.
7. Settings, worlds, environments, factions, clues, adventures, routes and locations.
8. Unclassified/legacy/source-only material requiring source-boundary disposition.

## Current evidence-backed starting observations

These are observations, not completed audit results:

- The current operational database contains 487 certified records, while the old structured CSV corpus contains 19,199 rows. These are different authority surfaces.
- Representative current canonical records such as `mv.core.species.elf`, `mv.core.item.weapon.longsword`, `mv.setting.havalaea.creature.rootstalker`, and `mv.setting.havalaea.creature.rootstalker.action.root-whip` contain identity and provenance but no substantive `spec` payload in their current `gameObject` body.
- The canonical schema registry requires `recordLayer`, `schemaVersion`, `contentVersion`, `status`, timestamps, and `spec` at the base object level, with additional type-specific required fields for several object families.
- The current certification script does not validate those schema requirements; it validates set size, identity uniqueness, game-object presence, source digest, quarantine state and semantic fingerprint.

These observations justify the deterministic baseline scanner. They do not authorize automatic field generation.

## Completion boundary

PPIA-01 is complete only when the repository contains all of the following with evidence:

- source-grounded cross-domain gap register;
- prioritized repair backlog;
- completed source-backed repairs where evidence is sufficient;
- unresolved-source/source-absence register;
- explicit duplicate/alias/intentional-exclusion dispositions where applicable;
- traceability to affected PPIA and Stage A feature surfaces;
- deterministic re-audit results showing the final state of the tranche.

PPIA-01 completion does not activate A2, authorize release/deployment, authorize tester access, or promote unsupported content.