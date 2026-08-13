# CAPP-01 Completion Report
## 25-Species Appearance Choice Registry + Constraint Model

**Work item:** CAPP-01  
**State:** READY-FOR-REVIEW CANDIDATE — NOT COMPLETED_VERIFIED  
**Owner:** John Brandon Turner

CAPP-01 converts the completed PPIA-05/PPIA-06 appearance authorities into a deterministic production-preparation registry and executable constraint contract. The substantive artifacts are generated from current canonical PPIA-06 morphology, semantic-taxonomy, Appearance Studio and owner-visual-decision files, with PPIA-05 retained as Species/Form biology truth and PPIA-03 retained as actual equipment authority.

The current canonical appearance set contains exactly 25 profiles in PPIA-06 order. The registry inherits 10 canonical Appearance Studio surfaces (P06-UI-002 through P06-UI-011), preserves their semantic-layer references and mutation modes, and currently produces 180 unique stable source-derived IDs across required features, bounded variation and explicit owner-resolved contracts.

Key source-controlled cases include Giantkin's valid Grendelkin/Surtrborn/Daityr lineages only; Stygian optional horns/wings with no appearance-granted flight and no pointed ears; Vespin four-arm topology; Moravi two-arm/four-leg topology; Rakuuta facial feathers/no-horn identity; Traiga's base no-extra-wing rule; Furashin dynamic fur phenotype; Kola-Ha Form separation; Toba-Madra fur/dye and actual-cybernetics separation; Arborae linked seasonal profiles; Mythragara derived hybrid; Suula persistent and active Adaptation boundaries; Nekron one-time ascension-derived customization; ManyToms replicated constituent identity; and The Free's broad humanoid android topology boundary.

The constraint model evaluates permission first, then upstream biology/current Form, topology, required features, profile state/behavior, authored dependencies, renderer compatibility and actual equipment projection. It preserves explicit unknown/unavailable/read-only states, prohibits silent substitution, prohibits implicit humanoid limb counts, and requires authoritative-state inspection before retry after ambiguous mutation outcomes. Renderer support never determines identity validity. Presentation wardrobe never grants mechanics or Asset ownership; actual equipment remains a permission-safe PPIA-03 projection. Randomization remains downstream CAPP-02 work and may not mutate source-owned biology/history/current Form/equipment.

A source-integrity failure occurred during foundation construction: an earlier legacy profile reconstruction beginning with Antyrri/Brambleborn did not match current PPIA-06 authority. Hosted run `31702343075` exposed the defect. The substantive package was replaced—not grandfathered—with deterministic generation from the canonical authority in run `31703091730`, whose regeneration and embedded validation passed. The corrected owner-authored foundation head `f460761d323af7c10f54ff85faec553163aa29e9` then passed dedicated run `31703316324`, reporting `canonical_profiles=25 choice_surfaces=10 stable_choice_ids=180`.

CAPP recovery indexing was also repaired: `scripts/sync-capp-roadmap-index.py` derives all 12 CAPP roadmap-index entries from the canonical CAPP backlog, and run `31703569637` passed generation/check/commit. This prevents the new parallel track from being omitted by normal indexed session recovery.

The attached acceptance matrix contains 20 candidate checks. CAPP-01 may become `completed_verified` only after the completion validator passes on the exact PR head, all applicable hosted checks are green, the PR is merged, and the merge signature is verified. Until then this report is explicitly not a completion claim.

No application runtime, STAGE-A-A2 activation, release, deployment, tester access, paid service, production credential, or unsupported canonical-content promotion is authorized by CAPP-01.
