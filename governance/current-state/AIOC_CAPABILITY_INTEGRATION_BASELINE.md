# AIOC Capability Integration Baseline

**Status:** IMPLEMENTED — CI verification pending  
**Batch:** AIOC-CI-001 — Preserved COS Capability Workbench  
**Public default:** `/operational/`  
**Source policy:** reuse preserved recent COS work in place; do not revive the obsolete migration entry shell

## Integrated public capabilities

The operational AIOC command center now exposes these preserved COS surfaces:

1. `development-os.html` — Development OS
2. `aioc-core.html` — AIOC Core
3. `studio.html` — Content Studio
4. `balance.html` — Balance Lab
5. `testing-suite.html` — Testing Suite
6. `feature-modules.html` — Feature Modules
7. `diagnostics.html` — Diagnostics
8. `refresh.html` — Refresh and Recovery

## Boundaries

- Existing COS source files and shared assets remain authoritative; they were not copied into a second source tree or rewritten.
- The Pages artifact publishes the approved capability surfaces and their root-level shared static assets.
- `/operational/` remains the public root target.
- The obsolete `/v2/` migration entry shell remains excluded.
- The certified 487-object database, implementation documentation, governance state, and deployment health contracts remain unchanged in authority.

## Deployment evidence

- Operational page integration commit: `45abaf694f33ee59245f72584a14b8d5bc5db3cb`
- Workbench wiring commit: `ea666dc089ebea6c5d765a6f89d9efff714ad50b`
- Unified Pages publication commit: `1685056d2ea1b1c20cbbb1bea17c1cadbc967cc1`

The deployment workflow must verify all eight approved surfaces, operational health, deployment manifest, and certified content database before this batch is considered closed.
