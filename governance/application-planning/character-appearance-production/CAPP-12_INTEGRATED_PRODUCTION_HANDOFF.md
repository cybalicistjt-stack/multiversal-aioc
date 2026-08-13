# CAPP-12 Integrated Production Handoff

**State:** content built; integrated validation pending. This is not a `completed_verified` claim.

## Authority

PPIA-06 remains appearance architecture authority, PPIA-05 remains Species/Form/biology authority, and PPIA-03 remains actual equipment/inventory authority. CAPP-01 supplies stable appearance choices/constraints, CAPP-02 supplies presets/randomization/locks, and CAPP-03 supplies renderer-production metadata/topology templates.

## Implementation chain

1. **CAPP-04** — asset manifest, coverage model, contextual coverage, reference analyzer and `tools/capp04_coverage.py`.
2. **CAPP-05** — deterministic semantic render-plan contract and `tools/capp05_appearance_compiler.py`.
3. **CAPP-06** — topology-aware wardrobe/equipment visual-fit catalog.
4. **CAPP-07** — implementation-grade Appearance Studio screen/state/responsive/accessibility/recovery contract.
5. **CAPP-08** — portrait/token/export derivative identity, framing, permission filtering and invalidation contract.
6. **CAPP-09** — deterministic migration contract and `tools/capp09_migration_reference.py`; no silent substitution.
7. **CAPP-10** — structured nonvisual appearance grammar and `tools/capp10_accessibility_description.py`.
8. **CAPP-11** — large deterministic synthetic/noncanonical QA generator at `tools/capp11_generate_qa_corpus.py`.
9. **CAPP-12** — integrated build validator at `scripts/validate-capp-integrated-build.py` and this implementation handoff.

## Cross-surface invariants

A valid Character remains valid when renderer coverage is partial, unsupported or unknown. Appearance does not grant mechanics, rewrite biology/current Form, or change actual equipment ownership/equip state. Unknown anatomy stays unknown. Hidden information is filtered before rendering, diagnostics exposed to the viewer, accessibility description and export. Renderer assets, fit classes, anchors, masks, palettes, pose and view remain outside Character truth. Unsupported assets are not silently substituted or warped. Migration never silently substitutes removed/missing values. Generated QA remains synthetic/noncanonical.

Special topology regressions explicitly include Vespin four-arm/two-leg, Moravi two-arm/four-leg, Suula nested hand/claw, ManyToms composite/repeated constituents, and the unknown-topology no-synthesis boundary.

## Validation entry point

`python scripts/validate-capp-integrated-build.py`

Per the owner's current direction, the tranche is built first. The next phase is one or more integrated validation rounds: repository validator, targeted artifact review, generated-corpus inspection, exact-head hosted CI, PR/merge evidence, then and only then `completed_verified` state projection.

No application runtime, STAGE-A-A2, release, deployment, tester access, paid services, production credentials or unsupported canonical promotion is activated by this handoff.
