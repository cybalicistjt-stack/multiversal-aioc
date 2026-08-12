# PPIA-10 — Relationship, Social & Faction Inspector, Action & Reference Candidate

**Work item:** PPIA-10 — Relationship, Social & Faction Content Framework  
**Version:** 0.1.0  
**State:** INSPECTOR / ACTION / REFERENCE CANDIDATE — NOT PPIA-10 COMPLETE  
**Foundation merge:** `0c0b8ce17cd80e47b7b12285a2bd8278e58a732e`

## 1. Purpose

Convert the verified PPIA-10 source/design foundation into deterministic inspector, mutation, recovery and reference-case contracts without reopening source authority or claiming final PPIA-10 completion.

This milestone integrates, rather than replaces, the verified F009 Relationship Tracker, F010 Social Interaction Mode and F016 Factions/Reputation/Organizations contracts. It supplies implementation-ready integration semantics where the retained sources leave gaps, with every such addition labeled as governed PPIA-10 design rather than recovered source canon.

## 2. Preserved source and design authority

This candidate retains the verified foundation boundary:

- 5 directly relevant PDFs / 44 visually reviewed pages;
- 2 structured CSVs / 1,374 rows;
- 94 structurally explicit social/faction rows: 82 Social & Influence plus 12 faction-linked;
- the two ten-page social-status PDFs as near-duplicate variants, not independent corroboration;
- F009's 14 directional relationship dimensions, four scale-profile kinds, seven reveal layers and 24 deterministic fixtures;
- F010's three interaction modes, fourteen action categories, seven alpha Actions, six resolution methods, seven degree outcomes, 29 outcome Event draft types and 24 deterministic fixtures;
- F016's sixteen faction contract families, nine visibility layers, profile-defined standing/influence, seven converted organizations, 956-record progression corpus and 24 deterministic fixtures;
- all 18 PPIA-10 semantic layers;
- all 14 PPIA-10 presentation profiles;
- all 15 explicit domain handoffs.

The retained sources do not authorize a universal relationship scale, standing scale, influence scale, social DC table, automatic reciprocal relationship mutation, progression-derived faction authority, rank-derived permission or AI decision/reveal authority.

## 3. Inspector projection contract

The matrix defines exactly **18 projection groups**, one for each verified PPIA-10 semantic layer. Every group declares the presentation profiles that consume it, and together the groups cover all **14** verified presentation profiles.

Permission filtering occurs before hidden endpoint resolution and before topology, counts, search, suggestions, export, realtime, notifications, diagnostics or AI context. A graph or canvas is never authoritative; semantic list, table and linear projections retain the same authorized meaning and actions.

## 4. Governed action surface

The matrix defines exactly **34 actions**:

- **10 reads** for relationship, relationship history/reveal, Social Mode, truth/belief state, faction detail, standing/influence, faction network/operations, reveal preview, history/recovery/accessibility and provenance;
- **24 authoritative mutations** for directional relationship state, Bonds/obligations, reveal/revocation, Social Mode lifecycle/proposal/review/resolution, temporary state, social-status binding, faction placement/membership/rank/office/standing/influence/operations/services/external bindings, faction relationships, secret/claim/rumor/knowledge records, reveal commits, compensating Events, explicit generated-proposal acceptance and revocation/purge requests.

Every authoritative mutation requires authorization, `expected_version` and a stable `operation_id`. Cross-domain atomic consequences additionally revalidate the relevant owning-domain versions.

An ambiguous response is never retried blindly. The client first queries operation status and current version. Compatible duplicate operations converge on the prior result/status; conflicting reuse of an operation ID fails safely.

## 5. Relationship semantics

Relationship state remains directional. A source-to-target edge does not create target-to-source state. Explicit mutuality is represented by two independently versioned edges or an explicit paired-edge contract.

The fourteen F009 dimensions remain independent. Scale meaning comes from a bound numeric, ordered-enum, band-only or validated-custom-scalar profile. PPIA-10 defines no universal conversion.

Bonds, leverage, favors, promises, debts, oaths and obligations remain typed persistent instruments. `Social Gameplay.PDF` names Kindred, Blood, Rivalry, Romantic and Mentor as Bond examples; their source-specific XP examples remain examples and are not promoted into universal thresholds.

## 6. Social interaction, truth and temporary state

F010's three Social Mode forms remain freeform, assisted and structured-challenge.

Objective truth, NPC belief, Player belief, claim/lie, rumor, knowledge, motive and secret remain independently governed. Deception may change belief without changing truth. Persuasion may obtain the best plausible authorized outcome but is not mind control. Insight does not reveal an exact hidden motive merely because a check succeeds.

Mood, intent and stance are temporary social state. They do not silently become persistent relationship, social status or faction standing.

## 7. Social-status scope

The retained social-status sources distinguish broad area/community status from interpersonal status. PPIA-10 therefore requires an explicit scope for any social-status binding and delegates mechanical application to the owning Condition/status contract.

The twenty artisan/craftsman/performer examples remain source examples. They do not establish a mandatory global status registry or automatic canonical Condition mapping.

## 8. Faction semantics

Faction live state keeps membership, rank, office, standing/reputation, influence, ownership, equipment, permission and progression separate.

The seven verified converted organization profiles are retained by name:

- Warden Faction;
- McBride Agency;
- Blackburn & Briar;
- Katica Graduate;
- Karma Ceutrica;
- Sacred Order;
- WarDogs.

These are provenance-backed design inputs, not automatic live Campaign factions or membership grants. The 11 Sacred Order high-ranking-agent capability records and the Warden source-reference-only tree do not grant membership, rank, office, equipment, ownership or permission.

Standing changes require an attributable source Event and a plausible information path. Influence uses its own scoped profile and history and does not rewrite standing.

## 9. Cross-domain consequences

Persistent Social Mode consequences are one accepted atomic Event group. Relationship, standing, influence, access, inventory, Condition, Project, Contract, Asset, Resource, Location and other domain changes remain owned by their authoritative domains.

All delegated Event writes commit or none commit. A failed partial write cannot be presented as an accepted social result.

Reversible effects use compensating Events. History is not deleted or rewritten.

## 10. Secrets, role projections and revocation

Hidden faction existence, relationship endpoints, exact values, membership, leaders, operations, agendas, resources, territory, motives and other protected fields are filtered before derivative computation.

Reveal preview is read-only. Reveal, withhold and revoke transitions require explicit authorization and version/idempotency controls.

Revocation invalidates protected cached, realtime, export/diagnostic and AI-context projections before the next role-safe projection. Durable history retains only authorized audit evidence for that audience.

## 11. Recovery and accessibility

All authoritative writes follow expected-version plus operation-id recovery. Lost responses use operation-status/current-version lookup before retry.

The `accessible-semantic-linear-view` is a first-class projection, not a reduced fallback. It preserves authorized entities, directional semantics, typed state, history and available actions without requiring graph/canvas interaction.

## 12. AI boundary

AI and development tooling may validate, summarize and propose only from role-safe projections. Generated output changes no social, relationship, faction, reveal, NPC-truth or canonical state by itself.

The `accept_generated_social_faction_proposal` action represents explicit authorized acceptance into the ordinary governed mutation flow; it does not grant AI independent authority.

## 13. Deterministic reference corpus

The companion corpus defines exactly **90 deterministic cases**.

- `PPIA10-RC-001` through `PPIA10-RC-024` preserve all 24 F009 fixtures one-to-one.
- `PPIA10-RC-025` through `PPIA10-RC-048` preserve all 24 F010 fixtures one-to-one.
- `PPIA10-RC-049` through `PPIA10-RC-072` preserve all 24 F016 fixtures one-to-one.
- `PPIA10-RC-073` through `PPIA10-RC-090` add PPIA-10 source/integration coverage.

The added cases cover directional relationships; the five Bond examples; area/community versus interpersonal status; the 20 artisan/craftsman/performer examples; all seven converted organization names; Sacred Order and Warden progression boundaries; standing information paths; influence separation; membership/rank/office/permission separation; Persuasion and Deception boundaries; atomic Social Mode consequences; hidden derivative filtering; revocation; lost-response recovery; semantic nonvisual parity; and proposal-only AI.

All 34 actions and all 18 projection groups are exercised by the corpus.

## 14. Ownership boundary

PPIA-10 may integrate and reference, but does not take ownership from:

- MV-IA-F009 Relationship Tracker;
- MV-IA-F010 Social Interaction Mode;
- MV-IA-F016 Factions/Reputation/Organizations;
- PPIA-08 Campaign/Scene/Session;
- PPIA-09 Investigation/Mystery;
- PPIA-12 World/Setting;
- PPIA-02 Creature/NPC;
- PPIA-03 Items/Inventory;
- Condition/Status;
- Project/Contract;
- Asset/Resource/Location;
- Permissions/Hidden Information;
- Recovery/History/Realtime;
- Proposal/Approval shared components;
- PPIA-11 Encounter/Balance authority.

## 15. Milestone boundary

This is the detailed inspector/action/reference-fixture milestone only. It does not complete PPIA-10.

Integrated authoring/workflow contracts and final PPIA-10 completion evidence remain later milestones. No application runtime, STAGE-A-A2 activation, release, deployment, tester access, paid service or production credential is authorized here.
