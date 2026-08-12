# PPIA-13 — Source and Teaching-Surface Inventory

**Work item:** PPIA-13 — Onboarding, Help & In-App Teaching Content  
**Milestone:** Foundation / Source and Teaching-Surface Inventory  
**Status:** foundation candidate  
**Owner and final authority:** John Brandon Turner

## 1. Purpose

This inventory establishes the governed source basis for the later PPIA-13 teaching-content library. It does not write the full user-facing library yet and does not redefine the application, game rules, permissions, Pack lifecycle, recovery semantics, or canonical content.

The owner-approved PPIA completion gate is a **complete role-aware onboarding/help/teaching content library covering first use through troubleshooting and tutorial-Campaign flow**. The Foundation identifies what may be taught, to whom, from which authority, and where source gaps must remain visible.

## 2. Primary authority: MV-IA-F025

`MV-IA-F025_ONBOARDING_HELP_DIAGNOSTICS_AND_ISSUE_REPORTING.md` is the direct inherited feature contract. Its support matrix supplies the canonical foundation vocabulary:

- 9 roles;
- 10 onboarding stages;
- 20 help contexts;
- 16 issue categories;
- 5 severity values;
- 24 protected diagnostic surfaces;
- 26 required denied cases;
- 20 acceptance criteria;
- default Help decision `deny-unless-topic-is-public-or-context-authorized`;
- default diagnostic decision `exclude`;
- default issue decision `deny`.

PPIA-13 preserves F025's progressive/contextual guidance, safe support, diagnostic redaction, explicit issue-reporting boundaries, zero-paid-service/zero-AI viability and permission-safe help search.

## 3. Surrounding inherited contracts

### MV-IA-F003 — Identity, Dashboard, and Workspace Selection

Controls first launch, identity/subject context, role/workspace selection, dashboard/resume behavior and the safe return path into authorized work.

### MV-IA-F004 — Character Creation and Advancement

Controls Character authority and the Character-creation surface. PPIA-13 may teach the governed creation path but may not invent Character mechanics or source defaults.

### MV-IA-F006 — First Playable Action and GM Approval Loop

Controls the first complete Player-to-GM teaching loop. The critical distinction is:

`local draft → validation → submitted → pending GM decision → approved / modified-and-approved / denied → authoritative commit → role-safe projection`.

Quick rules inspection is contextual and role-filtered. A local preview is nonauthoritative. Only accepted durable decision/commit evidence changes authoritative game state.

### MV-IA-F020 — Permissions and Hidden Information

Controls deny-by-default visibility and inference safety. Filtering must occur before counts, ranking, pagination, aliases, exact-ID lookup, relationships, notifications, exports, diagnostics, AI retrieval, and teaching derivatives. A client cannot receive protected fields and merely hide them.

### MV-IA-F021 — Autosave, Reconnect, Recovery, and Bounded Offline Use

Controls teaching of interruption and recovery. PPIA-13 must distinguish local draft, local autosave, authoritative save, submitted command, accepted durable Event, realtime delivery, and displayed projection. Offline authoritative mutation is prohibited. Ambiguous network outcomes use status lookup and idempotent recovery instead of guessing.

### PPIA-08 — Campaign / Scene / Session Authoring Depth

The owner-approved PPIA dependency is completed_verified. PPIA-13 may teach the existing Campaign/Scene/Session authoring depth and tutorial flow but does not reopen its domain design.

## 4. Project-source support

The retained `SCREEN_DESIGN_BIBLE.md`, `UI_DESIGN_BIBLE.md`, and `FEATURE_BIBLE.md` support, but do not outrank, repository contracts. They add the established journey and presentation expectations for:

- new Player onboarding, returning Player, Character creation, Campaign join, GM authoring and live Session journeys;
- context-sensitive Help and Rule Inspector access;
- empty/loading/error/offline/conflict/recovery states;
- Player Dashboard first-launch and empty-account states;
- mobile single-column/single-focus behavior;
- keyboard and touch completion;
- screen-reader semantics;
- high zoom/text scaling;
- reduced motion;
- noncolor equivalents;
- return-context preservation.

## 5. Teaching surfaces

The Foundation locks 18 stable teaching surfaces:

1. first launch and release identification;
2. identity, role and workspace entry;
3. dashboard and resume;
4. Campaign join;
5. Character creation;
6. Library / Universal Object Inspector;
7. Campaign / Scene / Session authoring;
8. first playable Action;
9. GM approval loop;
10. permissions and hidden information;
11. offline, reconnect and recovery;
12. content and Pack context;
13. contextual Help and known limitations;
14. empty states;
15. glossary and source-grounded reference;
16. diagnostics and issue-report introduction;
17. tutorial-Campaign;
18. completion, resume and Help rediscovery.

## 6. Teaching-content model

The Foundation defines 12 teaching-content types and 12 trigger classes. Every later authored teaching object must carry a stable ID, version, audience, surface, trigger, governing source references, provenance class, permission context, semantic body, nonvisual equivalent, dismissal/replay behavior, known limitations, PPIA-14 handoff and status.

Teaching content is a projection of governed behavior. It is never a new source of gameplay truth.

## 7. Audience model

All nine F025 roles remain represented. PPIA-13's primary human teaching roles are Player, Game Master and Content Creator. Assistant GM, observer, invited tester and Owner/Admin receive narrower context-specific guidance. Service actors do not receive a human tutorial UI. Optional AI can explain only the already-filtered teaching projection and a zero-AI path remains mandatory.

## 8. Hidden-information and inference boundary

Permission filtering occurs before:

- Help topic discovery and search;
- teaching-topic counts and ranking;
- examples and tutorial prerequisites;
- empty-state explanations;
- screenshots or diagrams;
- diagnostics and issue-report previews;
- exports and notifications;
- optional AI context.

Protected existence cannot leak through disabled controls, missing-topic wording, counts, autocomplete, ranking, relationship examples, tutorial branches, diagnostics, or fallback behavior.

## 9. Recovery teaching boundary

PPIA-13 teaches what recovery states mean and what category of action is safe. It does not replace the later PPIA-14 complete error/recovery/permission microcopy library.

The Foundation therefore records conceptual teaching such as “status unknown; query authoritative status using the existing operation identity,” while PPIA-14 owns final user-facing wording for every state and denial class.

## 10. Tutorial-Campaign boundary

Tutorial-Campaign lessons are synthetic, explicitly noncanonical teaching fixtures. They may demonstrate Player, GM and Creator flows using governed contracts. Replaying a lesson cannot replay authoritative game Effects or automatically promote fixture content to canonical content.

## 11. Pack source gap

F020 and F021 reference **MV-IA-F024 — Pack Lifecycle and Canonical Content Registry** as a dependency, but no completed F024 feature packet was found in the canonical internal-alpha feature-packet directory during this Foundation inventory.

Therefore PPIA-13 may teach only Pack facts already evidenced elsewhere: source pack/version, installed-pack context, pack lock/digest, entitlement and compatibility references. It may not invent F024-specific lifecycle commands, screens, policies, migration behavior, or final wording. This remains `P13-GAP-001` until a stronger canonical source exists.

## 12. Accessibility and responsive parity

Teaching is not complete if only a visual desktop walkthrough works. Required semantics, order, warnings, actions, current state, progress and completion must survive mobile single-focus layouts, keyboard-only use, touch, screen readers, high zoom, reduced motion and noncolor presentation.

## 13. Foundation acceptance position

The Foundation is ready for hosted review when its source manifest, taxonomy, authority/boundary matrix, audience/context/delivery matrix and 30 deterministic noncanonical reference cases validate together, while the PPIA-06→PPIA-13 transition, generalized PPIA program and conversation continuity regressions remain green.

This milestone does **not** claim PPIA-13 completion. **No application runtime** activation, STAGE-A-A2 activation, release, deployment, tester access, paid services or production credentials are authorized.
