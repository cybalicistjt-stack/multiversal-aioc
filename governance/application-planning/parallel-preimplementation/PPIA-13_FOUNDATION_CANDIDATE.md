# PPIA-13 Foundation Candidate — Onboarding, Help & In-App Teaching Content

**Work item:** PPIA-13  
**Milestone:** Foundation / Source and Teaching-Surface Inventory  
**Version:** 0.1.0  
**Status:** candidate — not complete until this exact milestone head passes required hosted validation and merges  
**Owner and final authority:** John Brandon Turner

## Foundation decision

PPIA-13 is a **teaching-content layer over existing governed behavior**, not a new authority layer.

The direct inherited authority is MV-IA-F025 — Onboarding, Help, Diagnostics, and Issue Reporting. PPIA-13 extends that implementation-ready feature design into the owner-approved complete role-aware teaching library while preserving MV-IA-F003 identity/workspace behavior, MV-IA-F004 Character authority, MV-IA-F006 first Action/GM approval, MV-IA-F020 permission/hidden-information filtering, MV-IA-F021 recovery/offline semantics, and completed PPIA-08 Campaign/Scene/Session authoring depth.

## Locked Foundation surface

This candidate defines:

- 6 evidence/provenance classes;
- 12 teaching-content types;
- 12 contextual trigger classes;
- 18 stable teaching surfaces;
- all 9 F025 roles, with Player, Game Master and Content Creator as primary human teaching audiences;
- 5 foundation journey contracts: Player first use, GM first use, Creator first use, reconnect/recovery teaching, and tutorial-Campaign flow;
- one permission-safe teaching pipeline that filters before every derivative;
- one explicit PPIA-14 microcopy handoff;
- one explicit unresolved F024 Pack-lifecycle source gap;
- 30 deterministic, synthetic, noncanonical Foundation reference cases.

## What the Foundation protects

### Authority

Teaching explains the user's current authorized projection. It cannot widen permission, create entitlement, invent game rules, alter Character/Campaign/Session truth, approve a proposal, commit a result, manufacture Pack lifecycle semantics, or promote content.

### Hidden information

Help search, topic counts, examples, tutorials, screenshots, empty states, diagnostics, exports, notifications and AI context are all derived only after server-authorized projection/filtering. Protected existence cannot be inferred from omissions, disabled options, counts or diagnostics.

### Recovery truth

The teaching model preserves the distinctions required by MV-IA-F021 and MV-IA-F006: local draft, local autosave, authoritative save, submitted command, pending decision, accepted durable Event and displayed projection are not interchangeable.

### Accessibility parity

A required teaching path cannot depend on desktop geometry, color, hover, animation or vision. Mobile, keyboard, touch, screen-reader, high-zoom, reduced-motion and semantic nonvisual delivery preserve the same required meaning and actions.

### Source provenance

Every later authored teaching object must identify its governing sources and provenance class. Unsupported behavior remains an unresolved gap rather than being filled from generic software conventions.

## Pack boundary

MV-IA-F020 and MV-IA-F021 name MV-IA-F024 as a Pack dependency, but a completed F024 feature packet is absent from the canonical feature-packet directory at this milestone. The Foundation therefore permits teaching only already-evidenced Pack facts such as source pack/version, installed-pack context, pack lock/digest, entitlement and compatibility references. F024-specific lifecycle UI/actions remain unresolved.

## PPIA-14 boundary

PPIA-13 owns conceptual explanation and teaching of what a state means, what evidence is authoritative, and which safe action category follows. PPIA-14 owns the later complete, final, permission-safe state-by-state error/recovery/denial microcopy library. Foundation examples must not masquerade as approved final PPIA-14 copy.

## Tutorial-Campaign boundary

Tutorial-Campaign material is synthetic teaching content. It is noncanonical, permission-safe, replayable, and must not duplicate authoritative effects when replayed. Any future canonical promotion requires its own governed source/canonical-content process.

## Milestone gate

This Foundation milestone may merge only when:

1. `scripts/validate-ppia13-foundation.py` passes;
2. the PPIA-06→PPIA-13 transition regression passes;
3. generalized PPIA continuity passes;
4. conversation continuity passes;
5. every applicable hosted repository workflow passes on one exact head.

Merging this milestone does not complete PPIA-13. It establishes the source and semantic architecture for the next bounded teaching-library contract milestone.

No application runtime, STAGE-A-A2, release, deployment, tester access, paid service, production credential, or public/internal-alpha release is authorized by this candidate.
