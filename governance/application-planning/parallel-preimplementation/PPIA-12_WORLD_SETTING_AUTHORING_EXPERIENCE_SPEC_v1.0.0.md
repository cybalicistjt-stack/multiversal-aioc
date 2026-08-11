# PPIA-12 — World & Setting Authoring Experience Specification v1.0.0

**Work item:** PPIA-12 — World & Setting Authoring System  
**Status:** IMPLEMENTATION-READY DESIGN SPECIFICATION  
**Owner:** John Brandon Turner  
**Primary repository:** `cybalicistjt-stack/multiversal-aioc`  
**Application runtime mutation authorized by this document:** No  
**STAGE-A-A2 activation authorized by this document:** No

## 1. Purpose

PPIA-12 defines the implementation-ready World & Setting Authoring experience without reopening completed Internal Alpha design or absorbing Campaign/Scene authoring. It binds reusable Setting Definitions, cosmology and branch placement, typed region/location/site hierarchy, environment profiles, settlements/infrastructure/landmarks, factions/institutions/governance, culture/society/economy, history/eras/timelines, world-local content extensions, setting-local rules, routes/portals/connectivity, Campaign instantiation handoff, reveal/knowledge state, source/conflict/provenance, recovery and accessible operation into one governed contract.

PPIA-12 owns reusable setting structure, setting-scoped extensions and authoring contracts. **PPIA-08 owns Campaign/Scene instantiation and live Campaign-local state.** MV-IA-F002 owns universal browse/inspect/compare surfaces. PPIA-02/03/04/05 retain Creature/NPC, Item, Vehicle and Species/Form core Definitions. Owning Ability/rules domains retain universal Ability and rule semantics. PPIA-11 retains encounter/balance calibration. MV-IA-F020/F021 retain permission-safe projection and recovery. MV-IA-F022 retains accessibility/adaptive-interface authority.

PPIA-12 does not authorize application implementation, release, deployment, tester access, paid services, credentials, production activation or unsupported canonical promotion.

## 2. Authority and retained source basis

### 2.1 Primary setting/cosmology/location sources

The verified primary source basis contains **22 primary setting/cosmology/location PDFs / 693 pages**. These sources include named worlds and cities, multiversal locations, branches, layers, planes, cross-reality infrastructure and setting-local mechanics. Exact filenames, page counts and hashes remain governed in `PPIA-12_SOURCE_AND_DESIGN_INVENTORY.md`.

Source documents can mix identity, geography, governance, culture, history, rules, Creatures, Species, Items, Vehicles and other facets. Document membership does not collapse those meanings into one World record.

### 2.2 Reusable environment templates

The verified environment source basis contains **8 reusable environment-template PDFs / 238 pages**. These are reusable archetype/template evidence. They do not instantiate a named World, Region, Location or Campaign by themselves.

An environment template becomes setting-attached only through explicit source-backed attachment or governed authoring. A Campaign-local environment state remains PPIA-08-owned and does not rewrite the reusable template or Setting Definition.

### 2.3 Worldbuilding authoring guidance

The verified authoring-guidance basis contains **2 authoring-guidance PDFs / 30 pages**. `Worldbuilding.PDF` and `World Creation tables.PDF` are authoring aids. Random-table results, generated suggestions, AI assistance and inferred cross-references remain proposals until explicit governed acceptance.

### 2.4 Aggregate retained boundary

The final verified source boundary is **32 retained PDFs / 961 pages total**. **No dedicated World/Setting CSV catalog is present.** Structured setting relationships therefore require explicit source evidence or governed authoring provenance rather than inference from a nonexistent structured world-membership table.

## 3. Source-truth and scope states

Source fact, source absence, source-unspecified state, conflict, revision, inference, recommendation/proposal, accepted authored fact, Campaign-local state, reveal state and runtime state remain distinguishable.

**Unknown stays unknown.** Missing geography, population, parentage, chronology, connectivity, compatibility, mechanics, faction presence, environment membership or route access is not silently replaced with a default.

**World-local stays world-local.** A rule, mechanic, Ability, Species, Creature, Item, Vehicle, environment, faction, culture, calendar or historical claim found in a setting source remains setting-scoped unless separate authority explicitly promotes broader scope.

## 4. Fourteen semantic identity/state layers

PPIA-12 preserves fourteen semantic layers:

1. **World / Setting Definition** — reusable source-backed identity, type, names, premise and stable setting metadata.
2. **Cosmology / Branch / Reality Placement** — explicit placement in branches, planes, layers, realities, eras or other cosmological containers.
3. **Region / Location / Site Hierarchy** — typed containment and location relations among worlds, realms, regions, zones, settlements, districts, stations, ships, routes, landmarks and sites.
4. **Environment / Biome / Hazard Profile** — setting-attached or reusable environment, hazard, resource and traversal context with provenance.
5. **Settlement / Infrastructure / Landmark** — source-backed settlements, structures, infrastructure, landmarks, portals, roads and hubs.
6. **Faction / Institution / Governance** — setting-scoped factions, governments, corporations, institutions, jurisdictions and authority relations.
7. **Culture / Society / Economy** — setting-scoped cultures, religions, languages, calendars, customs, economies and social structures.
8. **History / Era / Event / Timeline** — source-backed eras, historical events, chronology, causal relations and unresolved chronology conflicts.
9. **World-local Content Extension** — setting availability, membership, provenance and extension metadata for governed objects while their core Definitions remain with owning domains.
10. **World-local Rule / Mechanic Extension** — rules or mechanics explicitly scoped to a world, reality, branch, plane, zone or setting context.
11. **Transit / Portal / Route / Connectivity** — explicit roads, portals, routes, adjacency, access rules and inter-setting connectivity.
12. **Campaign Instantiation / Current Setting State** — Campaign-local instance, destruction/occupation/control/discovery/current-timeline state referencing reusable Definitions.
13. **Knowledge / Visibility / Secret State** — role- and Campaign-scoped reveal, discovery, secret, rumor and GM-only projection state.
14. **Provenance / Conflict / Recovery** — source references, assertions, conflicts, revisions, authoring decisions, history, operation IDs, expected versions and recovery receipts.

Implementations may package these layers differently internally but may not collapse their meaning.

## 5. Typed hierarchy and nonplanetary settings

World/Setting hierarchy is typed rather than planet-only. Valid source-supported entities can include worlds, realms, branches, layers, planes, cities, city-stations, generation ships, routes, districts, zones, regions, settlements, landmarks and other setting entities.

`Black Vegas.PDF` anchors a spaceborne city-station pattern. `The Antiquaria.PDF` anchors a semi-transdimensional generation-ship setting. `The Rakuuta Road.PDF` anchors cross-reality route/infrastructure rather than a World. Cosmology sources anchor branches, layers and planes.

Hierarchy, membership and placement require explicit source evidence or governed authoring provenance. Same document, name similarity, theme, proximity, shared faction or AI inference are insufficient.

`Havalaea.PDF` and `Vertigon.PDF` provide explicit reciprocal evidence for a Havalaea → Vertigon world-to-city relation. That evidence authorizes that bounded relation only; it does not generalize unsupported neighboring hierarchy.

## 6. World/Setting Inspector and projection model

`PPIA-12_WORLD_SETTING_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json` defines **14 Inspector projection groups** aligned one-to-one with the fourteen semantic layers and **16 governed action contracts**:

- `inspect_compare`;
- `author_setting_definition`;
- `author_hierarchy_relation`;
- `attach_environment_profile`;
- `author_infrastructure_landmark`;
- `author_faction_governance`;
- `author_culture_society_economy`;
- `author_history_timeline`;
- `scope_content_extension`;
- `scope_local_rule_extension`;
- `author_route_connectivity`;
- `campaign_scene_handoff`;
- `reveal_hide_setting_fact`;
- `generate_authoring_proposal`;
- `source_conflict_resolution_candidate`;
- `history_export_recovery`.

Exactly **12 action contracts are authoritative mutation paths**. Mutation paths require explicit authority, expected-version/revalidation boundaries and operation-ID/idempotency or equivalent recovery semantics.

## 7. Permission-safe projection

Authorization and filtering occur before hidden settings, locations, routes, factions, history, secrets, counts, search facets, hierarchy nodes, map labels, summaries, warnings, exports, diagnostics, notifications, pathfinding or AI/service context are serialized or aggregated.

An unauthorized viewer must not infer a hidden location or route from changed counts, unavailable path length, missing capacity, search facets, map gaps, error strings, route-validation behavior, exports, diagnostics or assistant summaries.

GM authority is Campaign-scoped rather than universal source-governance authority. Assistant GM and service/AI roles receive minimum delegated projections and do not independently author, reveal, resolve conflicts or promote local mechanics.

## 8. Environment attachment

Reusable environment templates remain distinct from setting-attached environment state. Explicit attachment preserves template provenance, setting scope and specialization state.

A template does not prove that a named setting contains that environment. A setting attachment does not rewrite the reusable template. Campaign-local environment changes remain PPIA-08-owned.

## 9. Infrastructure, landmarks and routes

Settlements, infrastructure and landmarks remain typed setting structures with attributable placement relations. Generic Items or Vehicles do not become setting infrastructure merely because they are mentioned nearby.

Routes, portals and connectivity are distinct from containment hierarchy. Explicit endpoints, route type, access semantics and provenance are required. Shared multiversal context does not imply connectivity.

Hidden routes are filtered before pathfinding, search and counts. Maps are supplemental and never the sole authority for route or hierarchy state.

## 10. Factions, governance, culture, society and economy

Faction/institution/governance facts remain distinct from location identity. Jurisdiction, presence and authority relations require explicit source or governed authoring evidence.

Culture, society, religion, language, calendar, customs and economy remain setting-scoped facets. They do not become Species biology or immutable Character traits merely because a Species and culture co-occur in a world source.

`The Empire.PDF` demonstrates mixed governance/economy/law/institution facets. `Noir City(1).PDF` demonstrates districts, landmarks and factions in the same source. These are routed into distinct semantic groups rather than flattened into one record.

## 11. History, chronology and revision conflicts

Historical events, eras, chronology and causal relations require source evidence or explicit authored decisions. Document order, paragraph order, co-occurrence and file naming do not create chronology.

`Stratebrait.PDF` is a governing reference case for older/current/new revision material. Conflicting assertions remain separately attributable until a governed resolution is accepted. Resolution candidates do not rewrite retained raw source.

## 12. World-local content extensions

PPIA-12 may store setting availability, membership, provenance, local variant metadata and setting-specific extension metadata for Species, Creatures/NPCs, Items, Vehicles, Abilities and other governed objects.

Core Definitions and universal mechanics remain owned by PPIA-02, PPIA-03, PPIA-04, PPIA-05 and the relevant Ability/rules domains. A world-local extension does not silently fork, overwrite or replace those Definitions.

## 13. Setting-local rule and mechanic extensions

Musical Reality mechanics, branch-specific gameplay and unusual local physics remain explicitly scoped to their source-supported setting context.

Setting-local mechanics do not become universal/core rules automatically. Broader promotion requires separate authority, provenance and validation outside this completion contract.

## 14. Campaign/Scene handoff

PPIA-08 owns Campaign and Scene instantiation. PPIA-12 hands stable Setting Definition references and the minimum authorized reusable setting context into PPIA-08.

Campaign destruction, occupation, renaming, discovery, current control and current timeline state mutate only the Campaign instance. They never rewrite reusable Setting Definitions or other Campaigns.

## 15. Authoring proposals and governed acceptance

Worldbuilding guidance, random tables, templates, AI assistance and inferred cross-references create proposals only. A proposal carries provenance, scope and review state but is not canonical source truth.

Acceptance occurs through the specific owning authoring workflow. Rejection or abandonment leaves existing Definitions unchanged. Proposal-generation authority does not imply acceptance authority.

## 16. Integrated workflow set

`PPIA-12_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json` defines **16 integrated World/Setting workflows** (`WS-WF-001` through `WS-WF-016`). They cover:

1. Library / World / Setting reference and comparison;
2. Setting Definition creation and governed editing;
3. typed cosmology and location hierarchy authoring;
4. environment profile attachment and specialization;
5. infrastructure and landmark authoring;
6. faction, institution and governance authoring;
7. culture, society and economy authoring;
8. history, era and timeline authoring;
9. world-local content extension scoping;
10. setting-local rule/mechanic extension scoping;
11. transit, portal and route authoring;
12. Campaign/Scene instantiation handoff;
13. Campaign reveal / hidden setting knowledge;
14. authoring proposal generation and acceptance routing;
15. source conflict / revision / provenance review;
16. history / export / reconnect / ambiguous-network recovery.

Exactly **12 authoritative mutation workflows** contain revalidation/expected-version and operation-ID/idempotency recovery boundaries.

## 17. Cross-domain handoffs

The workflow matrix defines **10 cross-domain handoff contracts** (`WS-HO-001` through `WS-HO-010`). These preserve ownership for:

- MV-IA-F002 Universal Object browse/inspect/compare;
- PPIA-08 Campaign & Scene authoring;
- PPIA-02 Creature & NPC Definitions;
- PPIA-03 Item & Inventory Definitions;
- PPIA-04 Vehicle/Mecha/Starship Definitions;
- PPIA-05 Species/Form/Biology Definitions;
- owning Ability/rules execution and promotion domains;
- PPIA-11 encounter/balance calibration;
- MV-IA-F020/F021 permission/reveal/recovery;
- MV-IA-F022 accessibility/adaptive interface.

A receiving workflow does not inherit canonical mutation authority merely because a source surface authorized inspection.

## 18. Recovery and concurrency

Every authoritative mutation is expected-version checked and idempotent or governed by an equivalent concurrency contract. Ambiguous network outcomes query operation status using the original operation ID before retry and reuse the same idempotency identity.

Reconnect reauthorizes role, Campaign scope, authoring scope, visible settings/routes/secrets, rules/pack state and relevant versions. Cached hidden or revoked state cannot restore authority.

**No broad offline authoritative World/Setting mutation is permitted.** Offline drafts may exist as non-authoritative proposals, but authoritative Definition, relation, route, reveal or Campaign-instantiation state requires governed synchronization and validation.

## 19. Accessibility and responsive behavior

World/Setting authoring and inspection must support expanded desktop, medium, compact/mobile, keyboard-only, screen-reader, high-zoom/reflow and reduced-motion operation.

No required workflow may depend solely on map geometry, color, drag, hover, animation, node placement or visual route tracing. Hierarchy levels, relation types, route endpoints, reveal state, local-rule scope, source/conflict status, validation and authoritative results require semantic textual/nonvisual equivalents.

Maps may visualize governed setting data, but map geometry is supplemental rather than authoritative.

## 20. Reference corpus

`PPIA-12_REFERENCE_CASES_v0.1.0.json` contains **20 reference cases**: **13 contract-grounded, 4 synthetic QA and 3 guardrails**.

The corpus covers Definition-versus-Campaign state, Havalaea→Vertigon explicit hierarchy, no hierarchy by co-occurrence, Black Vegas and Antiquaria nonplanetary settings, Rakuuta Road connectivity, cosmology branches/layers/planes, Musical Reality and branch-local mechanics, unusual local physics, environment templates, authoring proposals, Empire and Noir City mixed facets, Stratebrait revision conflicts, owning-domain extensions, Campaign-local changes, hidden facts/pathfinding, ambiguous-network recovery and accessible nonvisual authoring.

Synthetic QA cases are validation fixtures, not canonical setting records.

## 21. Acceptance contract

`PPIA-12_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.0.json` defines **48 acceptance requirements across 16 categories**. The matrix traces all:

- 14 identity/state layers and 14 Inspector projection groups;
- 16 governed action contracts;
- 16 integrated workflows;
- 10 cross-domain handoffs;
- 20 reference cases.

All acceptance categories preserve source scope, typed hierarchy, environment-template separation, world-local non-universalization, owning-domain boundaries, Definition-versus-Campaign-state separation, permission-before-aggregation/pathfinding, explicit unknown/conflict/proposal provenance, expected-version/idempotent recovery and accessible nonvisual operation.

## 22. Non-goals and forbidden promotion

PPIA-12 completion does **not**:

- mutate retained raw PDFs or invent a World/Setting CSV authority;
- create hierarchy, membership, routes, chronology or compatibility from co-occurrence, name similarity, theme, proximity, document order or AI inference;
- force all settings into planet/continent/country/city geography;
- instantiate environment templates automatically;
- universalize Musical Reality, branch-local or other setting-local mechanics;
- replace PPIA-02/03/04/05 or Ability/rules owning Definitions;
- mutate reusable Definitions from Campaign-local destruction, occupation, discovery or Scene state;
- silently reconcile Stratebrait-style conflicts or overwrite raw source;
- treat proposals from random tables, templates or AI assistance as accepted canon;
- expose hidden locations, routes, factions, history or secrets through aggregates, pathfinding, errors, exports, diagnostics or AI context;
- permit broad offline authoritative World/Setting mutation;
- activate STAGE-A-A2;
- mutate application runtime;
- authorize release, deployment, tester access, paid services, production credentials or unsupported canonical promotion.

## 23. Completion condition

PPIA-12 may become `completed_verified` only when the exact completion-candidate head passes the deterministic PPIA-12 completion validator and every applicable repository regression gate, the candidate PR merges into canonical `main`, and the post-merge continuity checkpoint records the exact validated head, PR, merge SHA, `completed_verified` state and next dependency-optimized PPIA tranche.
