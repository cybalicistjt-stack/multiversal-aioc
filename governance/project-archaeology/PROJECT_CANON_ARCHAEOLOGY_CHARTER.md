# Multiversal Project Canon Archaeology & Wiring Audit Charter

**Status:** OWNER-DIRECTED — COMPLETED VERIFIED  
**Owner/final authority:** John Brandon Turner  
**Operational implementation authority:** none  
**Purpose:** reconstruct the complete project lineage, resolve current canon, recover dropped intent, and then prove that the current project is wired to the recovered canon before ordinary product implementation resumes.

## 1. Stop-the-line rule

This work is a project-memory and integration integrity gate.

- PCV-03 remains preserved at its last exact implementation state; this archaeology does not alter its runtime code or silently restart it.
- PCV-04 and later implementation remain unauthorized while the owner-directed archaeology gate is open.
- A "complete" archaeology requires both the **Canon Reconstruction Gate** and the **Internal Wiring / Dependency / Interconnectivity Gate** below.
- No historical source regains live operational authority merely because it is rediscovered. Historical material is evidence to reconcile, not a selector.

## 2. Why this exists

Repeated implementation failures have shown that later work can rediscover or partially recreate decisions that had already been made months earlier. The project has accumulated multiple authority eras, parallel workstreams, reduced tranche families, source-recovery programs, post-Bible additions, and implementation programs. Later execution ledgers are therefore not a complete substitute for total project memory.

The correction is one durable project-wide register that answers, for every meaningful project element:

1. where it originated;
2. what it intended;
3. what it produced;
4. whether it was implemented, design-complete, planned, deferred, superseded, or abandoned;
5. what superseded or refined it;
6. what remains current;
7. which later systems depend on it;
8. whether the current implementation actually consumes it.

## 3. Required chronological reconstruction

The archaeology must begin before the modern repositories and must preserve the project's actual genealogy.

### Era A — preformal source / "Rubik's cube"

Recover the giant text-dump / Rubik's-cube source state that preceded the formal project phases. Record its source location, content families, decomposition history, and what later artifacts inherited from it.

### Era B — Phase 0

Recover the first formal source-creation / decomposition phase and its relationship to the original game corpus.

### Era C — Phase 0.5

Recover the original Project Bible / Multiversal definition layer and distinguish it from later Project Bible v2.0 editorial consolidation.

### Era D — original numbered phases

Recover each original phase independently. Do not collapse "Phases 1–7" into one summary merely because the later Bible does so. Reconstruct each phase's scope, decisions, deliverables, completion evidence, successor, and surviving authority.

Include Phase 8 canonicalization/validation and Phase 9 architecture/readiness while distinguishing later unrelated programs that also use "Phase 0–9" terminology.

### Era E — post-phase / pre-family interstitial work

Recover every named step, Stage A item, internal-alpha packet, source-recovery program, content-authoring track, repository-hardening effort, operating-package change, and other work that occurred after/between the original phases but before or alongside the family-execution era.

### Era F — tranche-family era

Recover every tranche family, including:
- families with normal work-state attempt ledgers;
- families completed through content/design governance without later work-state attempts;
- families reduced/folded by PDCP;
- parallel authoring families;
- planning-only families;
- deferred future programs;
- interstitial amendments and cross-family insertions;
- families whose capabilities were absorbed by another owner.

### Era G — OPS3 / current convergence

Recover OPS3, persistent lanes, PCV, current UI/runtime changes, packaging/validation governance, and all owner directions after the Project Bible that materially refine current product intent.

## 4. Evidence classes

The register must distinguish evidence rather than flatten it.

1. **Owner decision evidence** — explicit owner choices and approvals.
2. **Canonical governance artifacts** — current or historically controlling contracts.
3. **Implementation evidence** — merged code, exact-head validation, installed proof.
4. **Completion/closure evidence** — completion reports, handoffs, receipts.
5. **Planning evidence** — approved programs/backlogs not yet implemented.
6. **Recovered source evidence** — legacy files, archives, conversation-derived source packages.
7. **Historical/provenance-only evidence** — superseded selectors, stale handoffs, old roadmaps.
8. **Unresolved evidence** — conflicting, missing, or insufficiently sourced claims that remain genuinely indeterminate after reconstruction.

No lower evidence class may silently override a higher one.

### 4A. Completion-first reconstruction rule

The archaeology is a **reconstruction project, not merely an extraction project**. Missing verbatim source does not by itself justify leaving a hole in project memory.

For every gap, first attempt to reconstruct the missing fact, decision, scope, dependency, deliverable, successor relationship, or intended behavior from the strongest combination of:

- explicit owner decisions;
- surviving source fragments and archive material;
- chronological predecessor/successor relationships;
- Git history and imported repository state;
- later artifacts that demonstrably inherited or depended on the missing element;
- schemas, tests, contracts, manifests, UI/runtime behavior, and data shapes that encode the earlier decision;
- supersession and migration chains;
- independent project records that converge on the same interpretation.

Reconstruction must choose the **most evidence-consistent complete interpretation**, not the most conservative empty interpretation.

Every reconstructed assertion must carry an evidence-quality label:

- `verbatim_source` — directly present in the original source;
- `directly_supported` — explicitly established by surviving authoritative evidence;
- `reconstructed_high_confidence` — not preserved verbatim, but the surviving evidence and downstream dependencies strongly determine one interpretation;
- `reconstructed_medium_confidence` — the best-supported interpretation with limited residual ambiguity;
- `reconstructed_low_confidence` — a necessary completion with meaningful uncertainty that does not justify leaving the system structurally incomplete;
- `indeterminate` — two or more materially different interpretations remain plausible and available evidence cannot responsibly choose among them.

Rules:

1. Do **not** leave a field, phase, dependency, or intent blank merely because no single surviving document states it verbatim.
2. Do **not** fabricate arbitrary detail. Reconstruction must be traceable to evidence, inherited behavior, chronology, or necessary system structure.
3. When one interpretation explains all surviving evidence substantially better than alternatives, record it as the reconstruction and preserve the reasoning/provenance.
4. When a lower-confidence reconstruction is needed for completeness, mark the uncertainty explicitly and route later contradictory evidence to supersession/revision rather than deleting the reconstruction silently.
5. Use `indeterminate` / `unresolved_archaeology` only after active reconstruction fails to select a responsible best-supported answer.
6. Owner ratification may promote or correct a reconstruction at any confidence level.

## 5. Canon Register disposition vocabulary

Every recovered item must receive one explicit disposition:

- current_canon
- current_intent_not_yet_implemented
- implemented_and_current
- implemented_but_superseded
- design_complete_consumed_by_later_owner
- completed_parallel_content_or_governance
- owner_approved_planned
- deferred_future
- superseded_provenance_only
- rejected_or_retired
- unresolved_archaeology
- missing_orphaned_intent

"Not present in the current work-state ledger" is never itself a retirement decision.

## 6. Canon Reconstruction Gate

This gate passes only when:

- the preformal Rubik's-cube source layer is accounted for;
- Phase 0 and Phase 0.5 are independently accounted for;
- every original numbered phase is independently accounted for;
- every Stage A / Internal Alpha / interstitial program is accounted for;
- every discovered application-planning family is dispositioned;
- every discovered work-state family/work item is dispositioned;
- parallel content/design programs are included;
- planning-only and deferred programs are included;
- later owner decisions after the Project Bible are incorporated;
- all explicit supersession chains are recorded;
- conflicts and gaps are actively reconstructed to the best-supported complete answer; only genuinely indeterminate alternatives remain unresolved;
- forgotten/orphaned intentions are surfaced explicitly and reconstructed into a usable intended state wherever the evidence permits;
- the result is available in one machine-readable register plus a human-readable guide.

## 7. Internal Wiring / Dependency / Interconnectivity Gate

After canon reconstruction, perform a separate comprehensive implementation audit.

The question is not only "do we possess this design?" but "is every system that should know about it actually connected to it?"

For every current-canon or current-intent item, audit:

- canonical owner and stable identity;
- upstream requirements;
- downstream consumers;
- runtime/API/package bindings;
- data/schema/storage/migration bindings;
- Action/Event/authority/permission bindings;
- content/provenance/rights bindings;
- UI/navigation/search/discoverability bindings;
- phone/desktop/accessibility projections;
- offline/local-first and online/session behavior;
- reconnect/recovery/idempotency behavior where applicable;
- asset/presentation dependencies;
- creator/GM/player projections;
- validation and regression coverage;
- packaging/install/update implications;
- export/backup/provider-exit implications;
- cross-family late-bind and golden-proof dependencies;
- documentation/help/reference exposure where applicable.

### Wiring defect classes

- **orphaned_canon** — canonical capability has no required consumer path.
- **stale_binding** — consumer points at superseded authority.
- **duplicate_owner** — a later subsystem recreated truth owned elsewhere.
- **missing_dependency** — required predecessor/capability is absent from the graph or implementation.
- **missing_consumer** — dependency exists but the expected downstream feature never consumes it.
- **partial_projection** — runtime exists but one or more required user/role/device surfaces do not expose it.
- **authority_bypass** — integration skips the governing owner/permission/event boundary.
- **persistence_gap** — UI/runtime path does not preserve required durable state.
- **recovery_gap** — reconnect/restart/migration path loses or duplicates governed state.
- **test_blind_spot** — wiring exists without a regression/acceptance proof capable of detecting its loss.
- **dead_planned_intent** — owner-approved current intent has no implementation destination.
- **implicit_only_wiring** — connection exists only by convention/prose rather than a durable contract/reference.

Every defect must name the producer, expected consumer, current evidence, impact, and repair destination.

## 8. Relationship to existing dependency artifacts

Existing artifacts are inputs, not proof of completeness:

- ROADMAP_DEPENDENCY_GRAPH.json covers cross-program activation semantics but is not a total project knowledge graph.
- PDCP_CROSS_FAMILY_OVERLAP_REGISTER.md records important owner/folding decisions but only for its reviewed family scope.
- PCV convergence ledgers detect stranded user-facing implementation but do not reconstruct the whole historical canon.
- Project Bible v2.0 is a major authority snapshot but predates many later owner decisions and compresses parts of the early phase history.
- OPS3 CURRENT/BOOTSTRAP control live execution only; they intentionally do not contain total project memory.

The new register must link these rather than replacing their specialized purposes.

## 9. Repair rule after audit

The wiring audit must first produce findings. Repairs happen only after the defect inventory is complete enough to avoid locally fixing one seam while contradicting another.

Repairs should prefer:
1. binding existing owners together;
2. restoring missing references/projections;
3. routing stranded capabilities into existing product paths;
4. deleting duplicate authority only after migration/supersession is explicit;
5. adding tests that fail if the recovered wire is lost again.

Do not solve missing integration by creating another parallel system.

## 10. Completion standard

This project-wide gate is complete only when all of the following exist and reconcile:

- Project Canon Register;
- chronology and supersession guide;
- source/provenance inventory;
- family/tranche inventory;
- orphaned-intent register;
- current-canon index;
- wiring/dependency/interconnectivity matrix;
- wiring defect register;
- repair routing plan;
- validation proving register coverage and referential integrity;
- bootstrap pointer telling future conversations where to read the register without making the register a competing live work selector.

Until then, archaeology status remains **IN PROGRESS**.


## 11. Completion-candidate artifact set

The reconstruction and wiring inventory are materialized in the sibling artifacts named by `PROJECT_CANON_REGISTER.json#artifact_set`. This candidate becomes `COMPLETED_VERIFIED` only after `scripts/validate_project_canon_archaeology.py` and the Operations V3 repository-health gate pass on the exact candidate head and protected-main publication is verified. Routed future PCV work is not authorized by archaeology.


## 12. Verified closeout

The completion candidate merged to `main` as `c03aae1112810ef8bafdb6a7aca8bfc430d7deaf`. GitHub Actions run `36080361805`, job `107900750519`, passed the project-canon archaeology validator, the OPS3 single-door/semantic-retirement checks, and the existing Operations V3 regression suite on the exact candidate head.

The Canon Reconstruction Gate and the Internal Wiring / Dependency / Interconnectivity Gate are therefore **completed_verified**. Known future product-convergence gaps remain explicitly routed to their owning PCV tranches; this closeout grants no successor authority and does not claim those future repairs are already implemented.

The preserved product lane resumes at PCV-03's existing installed Windows + Android physical two-device proof. PCV-04 remains unauthorized until PCV-03 itself closes.
