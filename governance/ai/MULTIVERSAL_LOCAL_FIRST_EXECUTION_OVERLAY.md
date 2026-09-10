# Multiversal Local-First Execution Overlay

**Document ID:** MV-AI-LOCAL-FIRST-001  
**Version:** 1.0.0  
**Status:** CURRENT — OWNER-APPROVED EXECUTION OVERLAY  
**Approved:** 2026-09-10  
**Scope:** all future implementation and production tranches unless a narrower current authority explicitly requires otherwise

## Purpose

The completed MLR-01 workstation gives Multiversal a validated local execution plane for deterministic tooling, local AI, retrieval, media, 3D, GIS, QA and production work. This overlay changes the default execution assumption without changing the roadmap order, canonical owner domains, rights rules, acceptance gates or current work selector.

The rule is:

> Do not spend frontier-model reasoning, paid-provider calls, or custom implementation effort on commodity work that an approved deterministic tool, reusable library, local model or local specialist engine can perform reliably under the tranche's governing contracts.

## Mandatory execution ladder

For each bounded task inside a selected tranche, choose the lowest layer that can satisfy correctness, rights, security, reproducibility and portability requirements:

1. **Deterministic installed tool** — exact search, parsing, conversion, hashing, media processing, SQL, validation, security scanning, benchmarking and similar mechanical work.
2. **Approved reusable/open library or reference implementation** — only after tranche-specific license/architecture review when incorporation is required.
3. **Local model or local agent** — only for bounded tasks whose outputs can be reviewed or machine-checked; local inference is not canonical authority.
4. **Locally hosted specialist engine** — e.g. Blender, QGIS, ComfyUI, Qdrant, Ollama, Piper/Whisper-class workers behind Multiversal-owned contracts.
5. **Hosted inexpensive/commodity provider** — only when local execution is materially inferior, unavailable, uneconomic or impractical.
6. **Frontier Codex/Work/high-capability reasoning** — reserve for ambiguous requirements, architecture, difficult debugging, security/rights-sensitive reasoning, cross-system design and final review where stronger capability materially changes correctness or value.
7. **Human/owner-only judgment** — canon, owner policy, rights decisions requiring owner choice, taste gates, commercial/legal choices and other nondelegable decisions.

Do not escalate merely because a lower layer is unfamiliar. Escalate when evidence shows the lower layer cannot satisfy the task.

## Commodity non-reimplementation rule

Do not build a general-purpose replacement for an established approved capability merely because Multiversal needs to use that capability. Prefer a governed adapter/worker boundary when lawful and practical.

Default non-reimplementation examples include:

- ZIP/RAR/7z codec/decompression internals;
- general image/video/audio codecs and transcoders;
- generic thumbnail/waveform/media-metadata engines;
- OCR engines;
- generic vector databases and embedding runtimes;
- generic TTS/STT engines;
- general image-generation runtimes;
- full 2D/3D DCC, CAD or GIS applications;
- generic graph-layout engines;
- general backup engines;
- vulnerability and secret scanners.

A custom implementation is justified only when shipping/runtime independence, license/distribution constraints, security isolation, deterministic semantics, offline requirements, performance, accessibility, platform support or a genuinely Multiversal-specific behavior cannot be met by an adapter around the existing capability.

## Multiversal-owned control plane

External/local workers never become canonical owner-domain authority. Multiversal continues to own:

- semantic state and domain rules;
- permissions, visibility and consent;
- recipes/manifests and typed inputs/outputs;
- provider/worker abstraction;
- provenance, rights and use capabilities;
- deterministic receipts and cache keys;
- validation and acceptance;
- review/approval/canon promotion;
- user-facing product behavior.

A local service or installed application is an execution engine, not an architecture decision.

## Reuse-before-regeneration rule

When a task succeeds and its result is expected to recur, preserve the reusable mechanism where practical: script, fixture, recipe, manifest, prompt/template, cached derivative, benchmark, conversion profile or test corpus. Successful deterministic/local work should not be rediscovered or regenerated solely because a conversation or agent session ended.

Content-addressed inputs, exact versions, hashes and receipts should be used whenever practical so caches and outputs can be invalidated deterministically.

## AI routing rule

Local models are preferred for bounded drafting, extraction, classification, transformation, search assistance and repetitive code/support work **only after task-level quality is demonstrated**. A smaller model is not automatically cheaper if its error/repair rate increases total work.

AI output remains proposal/candidate material unless an existing owner-domain path promotes it. No model—local or hosted—receives mechanical, canonical, permission, consent or adjudication authority merely because it runs locally.

## Installed workstation baseline

MLR-01 completed_verified with 45 Tier A/B/C resources: 40 newly installed/configured, 5 existing installations reused, zero blocked/deferred, loopback-only local services where applicable and final validation passed. MLR-01 itself is retired; this overlay does not reopen its machine-maintenance authority.

Future workstation acquisition/maintenance still requires then-current authority or a new owner-authorized machine-local work order.

## Tier D and external dependency rule

The Tier D registry and later resource-source catalogs are discovery/evaluation inputs, not automatic application dependencies. A selected product tranche must still justify direct incorporation, inspect current license/security/maintenance/compatibility, and preserve provider neutrality where required.

## Validation rule

Using a mature tool does not weaken Multiversal acceptance. The selected tranche must still test the Multiversal-owned boundary: hostile/error inputs, deterministic receipts, unsupported states, cancellation/recovery, rights, visibility, cross-platform behavior and exact downstream effects as applicable.

## Current-work preservation

This overlay does not select a work item, reorder the roadmap, reopen MLR-01, or grant implementation authority to future tranches. `CURRENT_WORK_POINTER.json` remains the sole current product selector.