# MV-IA-F002 — Universal Object Experience

**Feature ID:** MV-IA-F002  
**Feature version:** 0.1.0  
**Classification:** entry-critical  
**Design status:** implementation-ready  
**Owner:** John Brandon Turner  
**Primary roles:** Player, Game Master, Content Creator, Owner/Admin, Assistant GM, service actor  
**Stage A mapping:** A2 — Universal Object Experience  
**Historical module mapping:** Pack Import, Validation & Registry  
**Prepared by:** Lead Documentation Architect / Product Requirements Steward  
**Reviewed by:** Architecture, Canon, UX/Accessibility, QA, Security, and Documentation roles required before implementation  
**Date:** 2026-08-05

## 1. Problem and user outcome

### Problem

Multiversal contains many governed object families—Abilities, Actions, Effects, Conditions, Resources, species, forms, items, creatures, NPCs, environments, vehicles, Worlds, Locations, factions, Scenes, rules, source records, and more. If every downstream feature creates its own browser, search, picker, inspector, relationship view, provenance display, and permission logic, the product will become inconsistent, difficult to maintain, unsafe around hidden information, and expensive to test.

Users also need to understand more than an object's display name. They must be able to determine:

- what the object is;
- which version is active;
- where it came from;
- which pack owns it;
- what it depends on;
- what it grants or affects;
- whether it is permitted and accessible in the current context;
- whether it has variants, conflicts, or incomplete source coverage;
- whether it can be selected into the current Character, Campaign, Scene, inventory, encounter, investigation, relationship, or creator workflow.

### Required outcome

A permitted user can find a real governed object, open a role-safe inspection view, understand its identity and provenance, traverse permitted relationships, compare relevant versions or variants, and select the object into another workflow without relying on a domain-specific duplicate selector.

The result must work on desktop, tablet, and mobile; through keyboard and touch; with correct permission and entitlement filtering; and with deterministic stable-ID selection.

### Why this belongs in internal alpha

The Universal Object Experience is entry-critical because it is a high-fan-out shared system consumed by Character creation, Campaign and Scene building, inventory, encounter design, investigation, relationships, World Builder, content creation, contextual help, and AI retrieval.

Without it, later vertical slices would either:

- use temporary disconnected selectors that must be replaced;
- expose hidden or restricted content;
- pass display names instead of stable IDs;
- duplicate provenance and validation behavior;
- make mobile and accessibility behavior inconsistent.

## 2. Alpha slice

### Included

- [x] Browse an approved, version-pinned internal-alpha object corpus.
- [x] Search by permitted display name, alias, stable ID, object type, source, pack, tag, and selected structured fields.
- [x] Filter by object family, pack, status, version, entitlement, Campaign compatibility, source coverage, and availability.
- [x] Open an object inspector from browse, search, relationship, and picker contexts.
- [x] Display stable ID, object family, active version, owner pack, lifecycle status, source and provenance summary, validation state, visibility, entitlement reason, and compatibility warnings.
- [x] Display role-safe original-source references and exact source coordinates when the user is authorized to view them.
- [x] Traverse permitted dependencies, grants, requirements, variants, replacements, owner-pack relationships, and selected domain relationships.
- [x] Compare two permitted versions or variants with field-level differences and source attribution.
- [x] Display unresolved conflicts and incomplete source coverage without silently resolving them.
- [x] Use a reusable constrained object picker in at least one Character workflow and one Scene workflow.
- [x] Return a stable object ID, selected version or compatibility policy, and selection context to the calling workflow.
- [x] Support single selection, bounded multi-selection, and inspect-before-select.
- [x] Support loading, empty, no-results, forbidden, restricted, stale-index, unavailable-pack, conflict, and retry states.
- [x] Provide desktop, tablet, and mobile layouts.
- [x] Provide keyboard, screen-reader, touch, high-zoom, reduced-motion, and nonvisual relationship paths.
- [x] Preserve privacy-safe telemetry and diagnostics for search, inspect, selection, denial, and failure.

### Explicitly excluded

- [x] Full canonical content editing and publication.
- [x] Owner approval or canonical promotion from the object browser.
- [x] Installation, update, migration, or removal of packs from the browser itself.
- [x] Public marketplace, purchasing, creator payouts, ratings, or public reviews.
- [x] Unbounded graph visualization of the complete corpus.
- [x] Semantic or vector search that requires a paid or hosted provider.
- [x] AI-generated object summaries as a dependency for normal use.
- [x] Bulk destructive object mutation.
- [x] Direct editing of historical source artifacts.
- [x] Exposure of hidden result counts, GM-only relationships, restricted metadata, or inaccessible source details.

### Full long-term scope deferred

Later expansion may include richer authoring, batch operations, pack management entry points, saved searches, user collections, advanced graph analysis, localization-aware search ranking, media comparison, public content discovery, creator submissions, and optional governed AI assistance.

Those expansions must reuse this packet's stable-ID, permission, entitlement, provenance, comparison, accessibility, and selection contracts rather than replacing them.

## 3. Roles and authority

| Role | Allowed actions | Hidden information | Approval required |
|---|---|---|---|
| Player | Browse and inspect Player-visible, entitled, installed objects; compare permitted variants; select compatible objects into allowed Character or Scene actions | Cannot see GM-only fields, unrevealed objects, hidden relationships, private notes, restricted counts, or inaccessible provenance | Selection may require downstream Character or GM approval; browsing does not |
| Game Master | Browse Campaign-permitted content; inspect GM fields; select objects into Campaign, Scene, encounter, NPC, or reward workflows | Cannot see another Campaign's private content, another user's private notes, or owner-only governance records | Destructive or canonical operations remain outside this packet |
| Owner/Admin | Inspect all authorized project and Campaign objects; view governance and validation metadata; diagnose conflicts | Access remains bounded by environment and explicit administrative authority | Canon, release, and destructive actions require their existing owner gates |
| Content Creator | Browse canonical and permitted draft objects; inspect provenance; compare variants; select references into a draft | Cannot see unauthorized Campaign secrets or other creators' private drafts | Submission or promotion is handled by separate approval workflows |
| Assistant GM/Observer | Browse and inspect only capabilities granted by Campaign role | May receive narrower projection than primary GM; no implicit access to all GM fields | Elevated access requires Campaign-role change |
| Service actor or AI | Query only through scoped service contracts; return permitted stable IDs and source-linked fields | No hidden or restricted retrieval outside the resolved subject and Campaign context | Mutation is prohibited here; optional AI output remains read-only or proposed elsewhere |

## 4. Dependencies

### Feature dependencies

- MV-IA-F001 — Application Shell and Workspace Navigation.
- MV-IA-F024 — Pack Lifecycle and Canonical Content Registry.

### Cross-cutting features required before alpha-ready status

- MV-IA-F019 — Content Library and Entitlements.
- MV-IA-F020 — Permissions and Hidden Information.
- MV-IA-F022 — Accessibility and Adaptive Interface.
- MV-IA-F021 — Autosave, Reconnect, Recovery, and Bounded Offline Use for saved picker state, stale recovery, and reconnect behavior where the caller is live.

These cross-cutting features do not block completion of this design packet. They block a claim that the implemented feature is alpha-ready.

### Shared systems

- SS-01 — Application shell.
- SS-03 — Authorization and visibility.
- SS-04 — Entitlement evaluation.
- SS-05 — Universal object experience; this packet is the controlling feature design for SS-05.
- SS-07 — Persistence, drafts, and state versions.
- SS-09 — Relationship and graph model.
- SS-14 — Validation and issue presentation.
- SS-15 — Accessibility behavior.
- SS-16 — Responsive information hierarchy.
- SS-17 — Content pack lifecycle.
- SS-18 — Telemetry and diagnostics.
- SS-19 — Help and source-grounded explanation.

### Service ports and adapters

The implementation should consume provider-neutral ports or application-owned interfaces for object catalog query, object retrieval, relationship traversal, provenance retrieval, source-fragment retrieval, entitlement decision, authorization and projection, pack and installation registry, validation findings, search-index status, telemetry, and diagnostics.

A local deterministic adapter is required for development and CI. A named hosted search provider is not required for the alpha slice.

### Canonical objects and packs

Representative alpha support must include Ability, Action, Effect, Condition, Resource, species or form, item or equipment, creature or NPC, environment, vehicle or operational Asset, World or Location content, faction or relationship content, Scene content, rules, source and provenance records, and pack versions.

### Schemas and migrations

Required contracts include universal summary and detail projections, query and filter request, paginated results, relationship edge projection, provenance and source-coordinate projection, version or variant comparison, picker constraints, selection receipt, entitlement and authorization decisions, index status, stale-cursor error, and reference migration or supersession mapping.

### Decisions and gates

- Stage A A2 exit condition.
- MV-IA-001 entry-critical feature gate.
- AG-02 provider-neutral boundaries.
- AG-03 data foundation before trusted alpha data.
- AG-04 identity and entitlements before alpha-ready status.
- Security and hidden-information review before Campaign-data integration.
- Owner review before alpha-ready status.

## 5. Object and state model

### Reusable Definitions

The browser and inspector operate primarily on reusable governed Definitions and their role-safe projections.

Minimum summary fields are stable ID, object family, display name, permitted aliases, short description, active or selected version, owner pack, lifecycle status, source-coverage status, validation state, permission state, entitlement state and reason, compatibility indicators, and permitted preview media.

### Campaign placements or bindings

The inspector may show Campaign placement ID, Campaign-local label or notes, rules-profile compatibility, installed-pack binding, visibility or reveal state, Scene or Character references, and house-rule markers. A placement must never be presented as if it changed the reusable Definition.

### Live instances and state

Live instances are displayed only when the calling workflow requests them and the user is authorized. The default catalog view must distinguish a Definition from an item, creature, Condition, vehicle, or other live instance.

### Events and history

Permitted history may include version release, supersession, pack update, Campaign placement, validation finding, reveal-state change, and selection receipt. History remains role-filtered and source-linked.

### Projections and indexes

Required projections are ObjectSummaryProjection, ObjectDetailProjection, ObjectRelationshipProjection, ObjectProvenanceProjection, ObjectComparisonProjection, and PickerSelectionProjection. Search indexes are derived; the canonical registry remains authoritative.

### Stable IDs

Display names, aliases, filenames, and provider IDs are never used as the selected identity. Picker output includes stable ID and, where required, version or compatibility policy. Superseded IDs return an explicit mapping, warning, or block rather than silent substitution.

### Provenance

The inspector displays authorized source ID, title, status, authority, coordinate, normalized target, owner pack, transformation summary, coverage state, conflict state, and validation evidence. Original text remains source evidence rather than editable canonical data.

## 6. Primary user flow

1. The user enters a Character, Campaign, Scene, inventory, encounter, or creator workflow.
2. The caller opens the universal picker with typed constraints.
3. The picker resolves identity, Campaign, role, installed packs, permissions, entitlements, rules profile, and calling context.
4. The initial result set contains only permitted and compatible summaries.
5. The user searches, filters, sorts, or enters an exact stable ID.
6. The user opens an inspector without losing caller context.
7. The inspector shows identity, relevant content or mechanics, source, provenance, relationships, compatibility, permission, entitlement, and validation state.
8. The user may compare a permitted version or variant.
9. The user selects the object.
10. The service revalidates permission, entitlement, installation, compatibility, and version.
11. The picker returns a receipt containing stable ID, resolved version or policy, calling context, and warnings.
12. The caller performs domain validation before authoritative save or submission.

## 7. Alternate and secondary flows

### Exact stable-ID lookup

Resolve the ID without exposing unrelated results. A superseded ID shows its mapping. A forbidden or absent ID follows the non-disclosure error policy.

### Compare versions or variants

Offer only permitted comparisons. Align meaningful fields, show additions, removals, and changes, and attribute every difference to a source or version.

### Relationship traversal

Show a bounded permitted list or graph, support type and direction filters, preserve focus and back-navigation context, and provide an equivalent nonvisual representation.

### Browse without a calling workflow

Allow browse and inspection without selection controls. The user may copy a permitted stable ID or open an authorized workflow.

### Incomplete or conflicted object

Display affected fields and evidence. The record may be inspectable but not selectable when the caller requires complete compatible data.

## 8. Failure, empty, and recovery states

| State | User sees | Allowed action | Preserved data | Evidence |
|---|---|---|---|---|
| Loading | Progress with active context | Cancel, close, wait | Query, filters, caller | Duration and operation ID |
| Empty corpus | No approved corpus or pack available | Return or inspect pack status | Caller draft | Registry status |
| No results | No-match state without hidden counts | Edit query, clear filters, exact lookup | Query and filters | Redacted search event |
| Validation error | Affected filter, constraint, or field | Correct input or inspect issue | Query and draft | Finding ID |
| Forbidden | Generic access denial | Return or use separate role request | Draft | Stable denial code |
| Restricted entitlement | Omitted or deliberately limited preview | Choose permitted alternative | Draft | Entitlement decision |
| Offline | Read-only cache when permitted; authoritative selection blocked unless caller supports snapshot | Retry, read, close | Query, cache, draft | Snapshot version |
| Stale index | Search may be incomplete | Refresh or exact lookup | Query and filters | Index version |
| Stale object | Record changed | Refresh, compare, cancel | Draft and prior reference | Expected/current version |
| Conflict | Conflict and affected fields | Inspect, choose resolved variant, cancel | Query and draft | Conflict ID |
| Unavailable pack | Reference unavailable or blocked | Inspect dependency or choose alternative | Draft and reference | Pack IDs |
| Failed selection | No caller mutation | Retry or cancel | Full picker state | Operation ID |
| Recovery required | Restored picker revalidates access | Resume, refresh, discard | Local picker state | Recovery receipt |

## 9. Permissions and hidden information

Authorization occurs before results, facets, counts, suggestions, relationships, previews, exports, and AI retrieval. Services return role-safe projections; clients do not receive hidden fields and merely hide them.

Required denied cases include unrevealed clue lookup through every channel, GM-only field retrieval, cross-Campaign isolation, revoked-user cache reuse, private creator draft access, AI over-retrieval, restricted preview leakage, and exact-ID existence inference.

## 10. Entitlements

Access may come from free policy, approved ownership, Campaign grant, sponsored access, administration, or test fixtures. Campaign grants remain scoped. Expiry blocks new use according to policy but preserves historical Character and Campaign state. Cached decisions are bounded and revalidated before authoritative selection.

## 11. Persistence and history

Picker state is a nonauthoritative convenience draft. Selection becomes authoritative only through the caller. Repeated selection operations are idempotent. Saved references use stable ID and version or policy, survive display-name changes, and use explicit migration maps for supersession. Exports remain permission-safe and source-linked.

## 12. Realtime, interruption, and reconnect

Before submission only local state exists. A selection request may retry with the same operation ID. Accepted receipts recover through the operation or caller draft. Pack, entitlement, permission, or object-version events invalidate affected cache. Second-device unsaved picker state remains local unless a later draft-sync feature is approved.

## 13. Interface and information hierarchy

Desktop uses result and inspector regions with preserved list position. Tablet adapts split view to full-height panels. Mobile uses a single-focus search → filter → inspector → detail subview → select sequence. No required action depends on hover, drag, or a wide graph.

Player hierarchy emphasizes compatibility, requirements, costs or grants, availability, and Select. GM hierarchy emphasizes Campaign compatibility, Player-safe versus GM-only fields, dependencies, warnings, and selection controls. Provenance and advanced validation remain available but secondary.

## 14. Accessibility

Use semantic results and headings, complete keyboard operation, predictable focus restoration, screen-reader state announcements, high-zoom support, noncolor statuses, reduced motion, adequate touch targets, nondrag alternatives, equivalent relationship list/table views, and actionable error recovery.

## 15. Notifications and queues

Notify only for actionable state changes such as selected-object unavailability, pack-version change, permission revocation, entitlement expiry affecting new use, blocking validation findings, or degraded index state. Normal browsing does not create persistent notification noise.

## 16. AI involvement

**AI mode:** optional read-only only. AI may explain permitted fields or provenance and suggest search refinements using the same projections. No AI call is required for browse, inspect, compare, traverse, or select. AI cannot retrieve hidden data, select silently, mutate caller state, or promote canon.

## 17. Telemetry and diagnostics

Record operation and correlation IDs, release identity, query and inspector latency, index freshness, stable errors, permission denial categories, cache invalidation, recovery events, and privacy-safe issue attachments. Private narrative text and protected payloads are not logged by default.

## 18. Test scenarios

### Unit

- [x] Query and filter normalization.
- [x] Stable-ID lookup state distinctions.
- [x] Picker constraint validation.
- [x] Unauthorized-field omission.
- [x] Deterministic comparison alignment.
- [x] Relationship direction and type.

### Contract

- [x] Provider-neutral local and future adapters.
- [x] Stable authorization and entitlement decisions.
- [x] Pack, provenance, relationship, and validation contracts.
- [x] Versioned selection receipt round-trip.

### Integration

- [x] Installed pack objects appear correctly.
- [x] Detail projection safely combines all sources.
- [x] Character and Scene callers use one contract.
- [x] Supersession preserves unrelated history.

### End-to-end

- [x] Player selects a permitted Ability into Character flow.
- [x] GM selects a creature and environment into Scene flow.
- [x] Desktop inspect, provenance, relationship, comparison, and select path.
- [x] Equivalent mobile path without context loss.

### Permission and hidden information

- [x] Search, facets, counts, autocomplete, aliases, relationships, comparison, direct URL, and revocation tests.

### Entitlement

- [x] Free, granted, sponsored, restricted, expired, and historical cases.

### Persistence and migration

- [x] Stable references survive save, reload, rename, compatible update, export, and explicit supersession.

### Reconnect and recovery

- [x] Picker state recovery, idempotent retry, stale revalidation, and cache invalidation.

### Accessibility

- [x] Keyboard, screen reader, high zoom, mobile, relationship alternative, reduced motion, and touch.

### Performance

- [x] Bounded and representative corpus, pagination or virtualization, bounded relationships, and no full-corpus client download.

### Golden or deterministic regression

- [x] 8D-007J applies when changes affect governed rules, schemas, stable IDs, pack lifecycle, or deterministic baselines.

## 19. Acceptance criteria

1. **UOX-AC-001:** A permitted real object is found by browse, search, and exact ID. **Blocking:** yes.
2. **UOX-AC-002:** Inspector presents identity, version, owner pack, role-safe detail, provenance, validation, entitlement, and compatibility. **Blocking:** yes.
3. **UOX-AC-003:** Hidden content cannot leak through any retrieval or inference channel. **Blocking:** yes.
4. **UOX-AC-004:** One Character caller and one Scene caller use the same picker contract. **Blocking:** yes.
5. **UOX-AC-005:** Selection uses stable ID plus explicit version or policy. **Blocking:** yes.
6. **UOX-AC-006:** Access, installation, compatibility, and version are revalidated before return. **Blocking:** yes.
7. **UOX-AC-007:** Provenance and source coordinates are accurate and permission-safe. **Blocking:** yes.
8. **UOX-AC-008:** Relationships are bounded, directional, source-linked, permission-safe, and available visually and nonvisually. **Blocking:** yes.
9. **UOX-AC-009:** Versions, variants, supersession, incomplete coverage, and conflicts are not silently resolved. **Blocking:** yes.
10. **UOX-AC-010:** All required failure and recovery states preserve caller draft and provide a permitted next action. **Blocking:** yes.
11. **UOX-AC-011:** Desktop, tablet, mobile, keyboard, touch, screen reader, high zoom, reduced motion, and noncolor paths pass. **Blocking:** yes.
12. **UOX-AC-012:** Queries are bounded and the client does not require the entire corpus. **Blocking:** yes.
13. **UOX-AC-013:** Diagnostics are privacy-safe and attributable. **Blocking:** yes.
14. **UOX-AC-014:** Core use works with zero AI and zero paid search services. **Blocking:** yes.
15. **UOX-AC-015:** Required automated and manual gates pass with exact evidence. **Blocking:** yes.

## 20. Fixtures and approved alpha content

Use the MV-IA-001 identity, Campaign, Character, pack, permission, and failure fixtures. Add permitted and restricted representative records from every alpha object family; aliases; long text; dense relationships; two versions or variants; one conflict; one incomplete source record; one superseded ID; GM-only extension fields; Campaign-granted content; missing dependency; stale index; revoked permission; expired entitlement; interrupted selection; and corrupt local picker state.

## 21. Security, privacy, cost, and risk

Security requires service-filtered projections, safe query handling, identical controls across every retrieval path, and no direct-URL bypass. Privacy requires Campaign isolation, no private-text logging by default, redacted issue attachments, and source-rights enforcement. Core implementation must be local-first and require no paid provider.

Stop work for any hidden-information inference, access-bypass selection, display-name identity, provider leakage, paid or production dependency, inaccessible replacement architecture, or silent conflict resolution.

## 22. Owner review points

Owner review is required before alpha-ready status and before paid providers, public previews, marketplace behavior, broad editing, or material canon policy. No new canon decision is required for normal browsing and selection. Silence is not approval.

## 23. Implementation handoff

**Target repository:** `cybalicistjt-stack/Multiversal-app`  
**Registered work type:** feature implementation plus schema-contract change as needed  
**Decision level:** A2 bounded provider-neutral implementation; A3 for paid provider, production, public preview, or material canon policy  
**Risk class:** material — permission, entitlement, provenance, identity, and high fan-out  
**Suggested title:** `Stage A A2 — Implement Universal Object Experience vertical slice`  
**Required reviewers:** System Architect, Canon and Rules Steward, frontend, backend, UX/accessibility, QA, security/privacy, documentation/provenance  
**Required gates:** repository safety, provider-neutral contracts, schemas and fixtures, denied cases, responsive/accessibility, zero-service E2E, applicable 8D-007J, CI, and owner alpha review  
**Rollback:** disable bounded route or feature while preserving caller references and contracts; retain evidence; no destructive content migration  
**Evidence:** implementation receipt, changed files and IDs, contracts, fixtures, query and selection receipts, tests, security and accessibility reviews, performance evidence, preview, PR, and merge commit

### Suggested implementation decomposition

1. Define query, summary, detail, relationship, provenance, comparison, and selection contracts.
2. Add approved deterministic corpus fixtures and local adapter.
3. Integrate service-level authorization and entitlement boundaries.
4. Implement browser, search, filters, exact lookup, and state components.
5. Implement inspector, provenance, relationships, validation, conflict, and comparison.
6. Implement constrained picker and receipt.
7. Integrate one Character and one Scene caller.
8. Add responsive, accessibility, diagnostics, performance, denied-case, recovery, and migration evidence.
9. Run gates and produce reproducible preview.

### Dependency hold

The design packet is implementation-ready. Trusted alpha durability depends on P9-06-008 and later data-foundation work. Alpha-ready permission and entitlement claims depend on MV-IA-F019 and MV-IA-F020. Character and Scene E2E selection depends on caller workflows. This packet does not bypass the active P9-06 sequence.

## 24. Readiness decision

- [x] All required sections complete.
- [x] Dependencies and shared-system impacts identified.
- [x] Permissions, persistence, recovery, accessibility, tests, exclusions, owner decisions, and implementation handoff complete at design level.

**Final design status:** implementation-ready; implementation remains dependency-gated  
**Reviewer:** independent specialist review required in implementation work order  
**Date:** 2026-08-05  
**Packet digest:** generated and recorded by repository commit and CI artifact
