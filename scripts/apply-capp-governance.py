#!/usr/bin/env python3
from pathlib import Path

ROADMAP = Path('governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md')
BOOTSTRAP = Path('governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md')

r = ROADMAP.read_text(encoding='utf-8')
b = BOOTSTRAP.read_text(encoding='utf-8')

assert '**Version:** 2.6.0' in r
assert '**Status:** ACTIVE — BOUNDED IMPLEMENTATION AUTHORIZED; PPIA COMPLETED_VERIFIED' in r
assert '- **PPIA final-state recovery is merged.**' in r
assert '- **PPIA:** completed parallel pre-implementation advancement program retained as implementation input and historical evidence.' in r
assert '## Design Standards Completion subproject — unfinished parallel track' in r
assert '- Preserve parallel tracks; completing PPIA does not complete or supersede A2, Design Standards, or Apple work.' in r
assert '## CAPP — Character Appearance Production Preparation' not in r

r = r.replace('**Version:** 2.6.0', '**Version:** 2.7.0', 1)
r = r.replace('**Status:** ACTIVE — BOUNDED IMPLEMENTATION AUTHORIZED; PPIA COMPLETED_VERIFIED', '**Status:** ACTIVE — BOUNDED IMPLEMENTATION AUTHORIZED; PPIA COMPLETED_VERIFIED; CAPP AUTHORIZED PARALLEL WORK', 1)

needle = '- **PPIA final-state recovery is merged.** Exact recovery head `031d4c7af10245069a5cf8bd5b2819965e338cee` passed **70/70** hosted workflows; PR #295 squash-merged as signed/verified `8357cc812436e8bbe40c214ac0ca6e44363cc1a5`. PPIA-16 remains the completed evidence anchor; no successor is selected by PPIA completion.\n'
insert = needle + '- **CAPP — Character Appearance Production Preparation is owner-approved parallel work.** CAPP inherits the completed PPIA-06 appearance architecture without reopening it. `CAPP-01 — 25-Species Appearance Choice Registry + Constraint Model` is the authorized first work item and is not yet started. CAPP does not activate A2/runtime/release/deployment/tester/paid-service/production-credential authority.\n'
assert r.count(needle) == 1
r = r.replace(needle, insert, 1)

needle = '- **PPIA:** completed parallel pre-implementation advancement program retained as implementation input and historical evidence.\n'
insert = needle + '- **CAPP:** owner-approved parallel Character Appearance production-preparation program that converts completed PPIA-06 architecture into production-ready data, tooling, renderer specifications, UX states and QA without activating application runtime.\n'
assert r.count(needle) == 1
r = r.replace(needle, insert, 1)

capp_section = '''## CAPP — Character Appearance Production Preparation — authorized parallel track

Governing documents:
- `governance/application-planning/character-appearance-production/CAPP_CHARACTER_APPEARANCE_PRODUCTION_PREPARATION_PROGRAM.md`
- `governance/application-planning/character-appearance-production/CAPP_PROGRAM_BACKLOG.json`

**Status:** OWNER-APPROVED — AUTHORIZED PARALLEL WORK; NOT YET STARTED.

CAPP inherits and extends the completed PPIA-06 Character Appearance Creator architecture into production preparation. It does not reopen PPIA-06. PPIA-05 remains Species/Form biology authority and PPIA-03 remains actual Asset/equipment authority.

Approved execution order:
1. **CAPP-01 — 25-Species Appearance Choice Registry + Constraint Model** — AUTHORIZED NEXT / NOT STARTED
2. **CAPP-02 — Preset, Randomization and Lock Libraries** — PLANNED
3. **CAPP-03 — Pixel-Art Asset Production Standard** — PLANNED
4. **CAPP-04 — Asset Manifest and Coverage Analyzer Contract** — PLANNED
5. **CAPP-05 — Deterministic Appearance Compiler / Reference Engine** — PLANNED
6. **CAPP-06 — Wardrobe and Equipment-Fit Compatibility Catalog** — PLANNED
7. **CAPP-07 — Full Appearance Studio Screen and State Specification** — PLANNED
8. **CAPP-08 — Portrait, Token and Export Production Contract** — PLANNED
9. **CAPP-09 — Appearance Versioning and Migration Engine Contract** — PLANNED
10. **CAPP-10 — Accessibility Description Grammar** — PLANNED
11. **CAPP-11 — Expanded Generated QA and Coverage Corpus** — PLANNED
12. **CAPP-12 — Integrated Production Handoff and Completion Gate** — PLANNED

Dependency-optimized order: `CAPP-01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11 → 12`.

CAPP-01 is first because later presets, randomization, asset production, coverage analysis, renderer tooling, UI controls and QA must derive from one stable machine-readable choice/constraint authority.

CAPP may be selected as the conversational primary while STAGE-A-A2 remains the authorized current application item. CAPP selection does not activate A2 or alter the application work order. CAPP also does not complete/supersede DS-008 or WP-011 / Apple work.

No CAPP item authorizes application runtime mutation, release, deployment, tester access, paid services, production credentials, or unsupported canonical-content promotion.

'''
marker = '## Design Standards Completion subproject — unfinished parallel track\n'
assert r.count(marker) == 1
r = r.replace(marker, capp_section + marker, 1)
r = r.replace('- Preserve parallel tracks; completing PPIA does not complete or supersede A2, Design Standards, or Apple work.', '- Preserve parallel tracks; completing PPIA or working CAPP does not complete or supersede A2, Design Standards, Apple work, or other retained tracks.', 1)

assert '**Version:** 5.4.0' in b
assert '**Last updated:** 2026-08-11' in b
assert '9. Read `governance/ai/runtime/ROADMAP_INDEX.json` and only the governing roadmap section for the primary work item.' in b
assert '## Parallel-track safety' in b
assert 'CAPP — Character Appearance Production Preparation' not in b

b = b.replace('**Version:** 5.4.0', '**Version:** 5.5.0', 1)
b = b.replace('**Last updated:** 2026-08-11', '**Last updated:** 2026-08-13', 1)
b = b.replace('9. Read `governance/ai/runtime/ROADMAP_INDEX.json` and only the governing roadmap section for the primary work item.', '9. Read `governance/ai/runtime/ROADMAP_INDEX.json` and only the governing roadmap section for the primary work item. If the primary work item is in CAPP, also read `governance/application-planning/character-appearance-production/CAPP_CHARACTER_APPEARANCE_PRODUCTION_PREPARATION_PROGRAM.md` and `CAPP_PROGRAM_BACKLOG.json` before execution.', 1)

needle = 'Application implementation authority may also be recorded canonically inside `cybalicistjt-stack/Multiversal-app` even while the AIOC conversational primary points to a governance/design side mission. A selected AIOC primary attempt does not by itself supersede the application repository\'s authorized current work order, and an application work order does not silently complete or discard the AIOC primary attempt.\n'
addition = needle + '\nCAPP — Character Appearance Production Preparation is an owner-approved parallel track that inherits completed PPIA-06 without reopening it. When CAPP is selected, recover its active work from `governance/application-planning/character-appearance-production/CAPP_PROGRAM_BACKLOG.json`, the CAPP checkpoint, exact branch/PR/CI evidence and the CAPP program document. Selecting CAPP does not activate or supersede STAGE-A-A2, DS-008, WP-011 / Apple work or any other retained track.\n\nCAPP work is repository/governance production preparation unless a specific item explicitly requires a checkout or external exact bytes. Do not invent an A2-style checkout blocker for CAPP merely because A2 itself is checkout-blocked; evaluate the actual CAPP work item and available connector/source surface.\n'
assert b.count(needle) == 1
b = b.replace(needle, addition, 1)

ROADMAP.write_text(r, encoding='utf-8')
BOOTSTRAP.write_text(b, encoding='utf-8')

# Self-remove one-time patch machinery from the branch before committing.
Path('scripts/apply-capp-governance.py').unlink(missing_ok=True)
Path('.github/workflows/apply-capp-governance.yml').unlink(missing_ok=True)
