# 05 — Research-to-Implementation Roadmap and Acceptance Matrix

## Scope and status
Owner approved the **research/design directions** on 2026-10-19. This is a scoped recommendation, **not** a CURRENT-selected implementation item. Start development only after a follow-on OPS5 selector/work item explicitly grants an implementation lane, branch and acceptance profile. No current GPR/MTLC state is changed.

## Five proposed tranches (not selected work items)
| ID | Research outcome | Minimal adoption path | Exit proof |
|---|---|---|---|
| UX-01 | FDE scene/context preview UX and gap closure | extend existing FDE projection/UI only | deterministic invariance, real renderer preview if claimed, accessibility and cross-platform evidence |
| COMP-01 | Cross-owner recipe and compatibility manifest | adapters around FDE-04/CAPP-07, no duplicate preset owner | round trip, checksum/version/rights, authorization/visibility negative proofs |
| FORM-01 | Modular form/augmentation **proposal** design | read-only topology map + action routed to actual owner | anatomical immutability until authorized owner acceptance; nonhuman and secret tests |
| SOC-01 | GM-authored presentation challenges | social runtime projection and existing adjudication | fairness/usability study; GM secrecy; no free modifiers |
| PORT-01 | Creator API, portability and optional AI proposal path | provider-off contract first, optional bounded AI later | reproducible import/export, entitlement/provenance, multi-device proof only where executed |

## Dependency order
1. **Existing owner contracts review:** CASI, CAPP/PPIA, FGA/FDE, equipment/abilities, social action authority, ARI permissions. Confirm semantic terms and current API before shipping interfaces.
2. UX-01 and COMP-01 may each begin after the fit/preset review; COMP-01 must not replace CAPP-07 presets.
3. FORM-01 depends on Species/Form & actual augmentation rule ownership. Its cosmetic part can be designed without authorizing functional limbs.
4. SOC-01 depends on accepted social mechanics and GM visibility conventions. Evaluation must not hardcode rules the user has not approved.
5. PORT-01 consumes stable schemas and real importer diagnostics; AI is optional, never provider-mandatory.

## Acceptance classes
- **R: research evidence**: confirm source text, date, feature status, licensing context, no contradictory caveats.
- **D: design review**: domain-owners/owner approve exact IDs, schema and interfaces, no unauthorized domains.
- **F: focused deterministic proof**: compile/types/semantic validators, representative fixtures for permitted/partial/unresolved/forbidden.
- **I: independent integration**: full Creator session and real local storage; explicit cross-app/device if claimed.
- **P: publication**: exact-head PR, target-main integration, required validation, OPS5 reconciliation. A draft PR or local test does not grant P.

## Negative tests that must always pass
1. Fashion dye/preview/ability cosmetic does not change mana cost, attack bonus, spell DC, damage or ability availability.
2. Cosmetic wing/tail/extra limb cannot grant anatomy, flight, carrying capacity or movement modes.
3. Same appearance recipe cannot insert actual item into inventory or equip slot.
4. Hidden NPC state cannot appear in player preview, error messages, portable export or AI suggestion prompt.
5. Unsupported/nonhuman topology yields explicit unresolved/incompatible receipt, no default humanoid.
6. Import with stale owner ref/version cannot silently overwrite new data; requires review.
7. Export/import with missing copyrighted or unavailable assets retains semantics and reports missing visuals, not silently downloads content.
8. Same recipe and registry versions give same checksum regardless of client device/renderer.
9. Unknown fields cannot trigger executable actions or network calls.
10. Optional AI cannot submit owner action or spend credits without explicit configured permission.
11. Offline/provider-off FDE path remains usable.
12. GM social criteria remain filtered from unauthorized player views.

## Five evaluation questions for owner usability playtests
- How many interactions until a saved design can be previewed in another context?
- Can a player distinguish **appearance** from functionality without tutorial intervention?
- Are import failures actionable: *what* is missing, *why*, and *how to repair*?
- Can a GM adjudicate presentation challenges using current rules without unplanned extra bookkeeping?
- Does the player see one consistent design across full-body, portrait and token modes with clear degradation when an asset is missing?

Collect measured time, counts and errors; do not assign invented performance targets or completion scores.

## Proposed first implementation slice
One context-preview selector on existing FDE, one portable presentation-only appearance recipe, one validator/compatibility report covering human + Vespin + Moravi + Mythragara + ManyToms. Gate behind domain review first; do not begin a second fashion engine.

## Risks/decisions
- Is **environmental contextual preview** merely an illustrative compositor or actual target-renderer parity? Must label truthfully.
- Does a universal appearance recipe add any value beyond existing CAPP/FDE preset contracts? Implement only the missing orchestration seam.
- Which owner governs functional prosthetics/cybernetics? Do not invent.
- Which exact social mechanic may be modified by wardrobe? No default automatic modifiers.
- Do we have user-approved sharing/public collection/licensing/monetization policy? Not yet established by this study.
- Platform limitations, performance, and user benefits remain *untested*; external sources are inspiration, not acceptance evidence.

## Prototype/checking evidence in this research package
Static source comparison and structured example authored. No application change, automated test run, live UI review, playtest, or CI required/claimed. Review/merge of research docs must still obey protected-main policy; research PR can remain draft.
