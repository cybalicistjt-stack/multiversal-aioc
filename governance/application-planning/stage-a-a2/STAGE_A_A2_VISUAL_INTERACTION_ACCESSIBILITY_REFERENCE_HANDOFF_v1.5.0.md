# STAGE-A-A2 Visual / Interaction / Accessibility Reference Handoff v1.5.0

**Work item:** STAGE-A-A2 — Universal Object Experience  
**Status:** pre-implementation visual/interaction/accessibility acceptance reference complete; A2 implementation not started by this handoff  
**AIOC branch:** `governance/stage-a-a2-detailed-design`  
**Application repository:** `cybalicistjt-stack/Multiversal-app`  
**Owner/final authority:** John Brandon Turner

## Owner-visible package

`STAGE_A_A2_VISUAL_INTERACTION_ACCESSIBILITY_REFERENCE_v1.5.0.zip`

SHA-256:

`cc19f15d2d4a5ada8bae5dca78f3067bc582915c9787e6a7767d31c43544b9eb`

This package is the A2-04 through A2-10 execution addendum to the governed A2 pre-implementation bundle and v1.1–v1.4 acceptance addenda. It converts the approved UI Bible, Screen Design Bible, A2 v0.3 responsive architecture and A2 v0.5 keyboard/Picker/compare/provenance behavior into fixed machine-readable evidence checkpoints before implementation begins.

## Verified coverage

- viewport/reference fixtures: **10**;
- named visual/interaction states: **34**;
- keyboard/focus sequence steps: **40** across six required flows;
- blocking accessibility/responsive checks: **24**;
- required evidence items: **42**;
- real large-data stress cases: **6**;
- live-region announcement classes: **9**;
- package files: **16**;
- package validator: **PASS**;
- internal SHA receipt verification: **PASS**;
- outer ZIP CRC/integrity: **PASS**.

## Locked responsive behavior

- Compact `<600` logical px: one primary column, list-first results, full-screen Inspector, compact filter/sort toolbar, removable active chips, sticky caller action and no hover dependency.
- Medium `600–1023`: filters drawer/sheet, list preferred, full-height Inspector drawer or readable landscape split.
- Large `1024–1439`: optional filter rail `240–272px`, result region minimum `520px`, Inspector `400px` default and resizable `360–520px`.
- Expanded `1440+`: optional filter rail `264–288px`, Inspector `440px` default and up to `560px`; spare space may not be filled with passive noise.
- Comfortable/Compact/Touch density changes spacing/truncation only; accessibility semantics and identity/permission content do not change.

The package includes `640px` and `320px` logical **reflow proxies** for 200%/400% pressure. These are explicitly not allowed to masquerade as actual browser zoom evidence. Actual zoom evidence remains required where the execution environment permits it.

## Accessibility/focus locks

- every A2 function keyboard operable;
- visible focus and no keyboard traps;
- skip target to Results and Selection tray where appropriate;
- closing Inspector/relationship/provenance/compare returns focus to the exact invoking result/row/field/action;
- Escape closes suggestions/popovers, true dialogs, mobile drawers/sheets and auxiliary subviews in the approved hierarchy without clearing query or selection by default;
- primary touch targets at least `44×44` logical px;
- no core workflow depends on hover or precision drag;
- required polite/assertive live-region announcements fixed before implementation;
- compare remains semantic/non-color-only and stacks left/right values per field on compact/high zoom;
- reduced motion removes parallax, large zoom transitions and animated reordering while preserving meaningful state feedback;
- hidden sections/counts/source controls are absent rather than leaking through disabled placeholders.

## Real-data visual stress anchors

1. Mythragara — 128 Features; long FeatureList/focus/section-navigation stress.
2. Vertigon — 24 places, 51 hooks and 69 source sections; long World/full-page reading stress.
3. Dagger — 35 relationship edges; grouped relationship navigation and exact focus-return stress.
4. Iron Golem — 17 Features; Creature metrics + structured Feature rows.
5. Acid Grenade — two competing source candidates; conflict compare/provenance and compact stacked-diff stress.
6. Plasma Rifle — dense ranged-weapon metrics/rules; side-Inspector overflow/readability stress.

## Evidence gate

`A2_EVIDENCE_CAPTURE_MANIFEST_v1.5.0.csv` names every required evidence checkpoint and expected filename. Screenshots prove layout/state only; DOM/test/transcript evidence remains mandatory for focus, live regions, hidden-information safety, target size, receipt parity and authorization semantics.

The final A2 evidence set must include actual desktop/tablet/compact states, Picker tray/error states, compare/provenance states, reduced-motion evidence, accessibility/focus/live-region reports, and actual 200%/400% zoom evidence when technically available. Reflow proxy screenshots must be labeled as proxies.

## Codex integration

Transfer this suite during A2-01 with the other A2 addenda. Apply it progressively:

- A2-04: Library/Inspector layouts and screen-state references;
- A2-06: relationship/provenance visual + focus checkpoints;
- A2-07/A2-08: Picker tray, mobile sticky action, atomic-error focus and desktop/mobile receipt parity;
- A2-09: compare/provenance compact/reflow/history checkpoints;
- A2-10: all 24 blocking accessibility checks and all 42 required evidence items.

Do not add a new runtime dependency merely to satisfy screenshot/a11y tooling without following the governed A2 stop-condition process.

## Preservation boundary

This handoff does **not** change `CURRENT_WORK_POINTER.json`, does not activate A2 implementation, does not alter the owner-selected Design Standards primary attempt, does not redesign the approved visual language, and does not authorize internal-alpha release, production release or deployment.

## Exact next pre-Sunday A2 operation

Build the A2 **performance/scale and privacy/authorization leakage acceptance package** using the real 11,861-object search index and high-density real objects. Lock explicit response/render budgets, virtualization/pagination thresholds, bounded relationship/provenance expansion behavior, cache/recovery rules, and a surface-by-surface leakage matrix for results, counts, facets, suggestions, exact-ID lookup, Inspector fields, relationships, provenance, compare, Picker, URL/history and accessibility text. Keep provider-neutral/local deterministic execution and do not invent production performance guarantees unsupported by the current platform.
