# STAGE-A-A2 Performance / Scale / Privacy Acceptance Handoff v1.6.0

**Work item:** STAGE-A-A2 — Universal Object Experience  
**Status:** pre-implementation performance/scale/privacy acceptance package complete; A2 implementation not started by this handoff  
**AIOC branch:** `governance/stage-a-a2-detailed-design`  
**Application repository:** `cybalicistjt-stack/Multiversal-app`  
**Owner/final authority:** John Brandon Turner

## Owner-visible package

`STAGE_A_A2_PERFORMANCE_SCALE_PRIVACY_ACCEPTANCE_v1.6.0.zip`

SHA-256:

`46da6983be93fa0ec7fc51e862e1eee2b38e90084078a4fe2021ba7b70613935`

This package is the A2-02 through A2-10 performance/scale/privacy execution addendum to the governed A2 pre-implementation package and v1.1–v1.5 acceptance packages. It turns the existing authorization-first behavior, the real 11,861-object search corpus and the approved visual/accessibility stress cases into explicit deterministic local budgets and leakage gates.

## Verified coverage

- governed search corpus: **11,861 objects**;
- blocking performance budgets: **18**;
- collection/pagination/virtualization bounds: **14**;
- privacy/authorization leakage surfaces: **40**;
- deterministic revocation/leakage transition scenarios: **16**;
- cache/recovery security rules: **14**;
- telemetry privacy rows: **15**;
- combined blocking acceptance assertions: **72**;
- package files: **16**;
- package validator: **PASS**;
- internal SHA-256 receipt verification: **PASS**;
- outer ZIP CRC/integrity: **PASS**.

## Performance boundary

The timing values in this package are **local deterministic A2 acceptance budgets, not production SLAs**. They do not claim performance for a hosted provider, internet connection, production database, production device class or deployment.

A construction-time naive Python full-corpus scanner was measured only as calibration evidence on the current execution environment. Across representative real query cases its observation was approximately **57.243 ms median / 79.112 ms p95 / 90.410 ms max**. This is not the application implementation and is not a completion criterion by itself.

The implementation budgets intentionally include substantial headroom, including:

- cold fixture catalog parse/local index readiness: `<= 1500 ms`;
- warm exact stable-ID lookup: `p95 <= 25 ms`;
- warm full-corpus text search/ranking: `p95 <= 250 ms`;
- filter + authorized facet projection: `p95 <= 250 ms`;
- suggestions: `p95 <= 150 ms` service compute after the UI debounce;
- first 50 result rows/cards: `p95 <= 400 ms` headless render;
- max schema page of 100 results: `p95 <= 650 ms`;
- high-density Mythragara Inspector: `p95 <= 600 ms` to usable heading/first meaningful section;
- Dagger 35-edge relationship group: `p95 <= 300 ms`;
- two-side compare: `p95 <= 450 ms`;
- Picker final revalidation for the typical <=20-selection reference case: `p95 <= 300 ms`.

Security correctness always overrides latency. A slow safe projection is an optimization failure; a fast leaking projection is a blocking security failure.

## Scale/collection locks

The package preserves the v0.6 query `pageSize` maximum of 100 and establishes bounded rendering behavior rather than unbounded DOM growth.

Key bounds include:

- default search page 50, schema maximum 100;
- result virtualization/windowing or progressive paging when >100 results are loaded or authorized result count exceeds 200;
- at most 10 visible suggestions;
- large Feature/property collections above 80 rows use virtualization/progressive batches <=50;
- relationship group batches are <=25 rows, with an auto-visible maximum of 50;
- visible relationship breadcrumb depth remains three;
- provenance level 4 renders one authorized source fragment/coordinate payload at a time;
- Vertigon's 69 source sections remain on-demand rather than eager-expanded;
- compare remains exactly two sides;
- Picker tray may support the v0.6 schema maximum 100, but lists above 20 entries must remain bounded/virtualized while the caller action stays reachable.

Virtualization may not weaken semantic order, keyboard navigation, focus restoration, selected-state continuity or authorized accessibility counts.

## Privacy/authorization surface rule

Authorization/entitlement projection must occur before matching, ranking, counting, faceting, suggestions, relationship grouping, provenance, compare or Picker eligibility.

The 40-surface leakage matrix explicitly covers:

- result rows;
- `authorizedResultCount`;
- facet bucket counts and bucket existence;
- suggestions/autocomplete;
- exact stable-ID lookup;
- source-only IDs;
- Inspector body/fields/hidden sections;
- relationship counts/rows/breadcrumbs;
- all four provenance levels;
- compare sides/diffs/conflict evidence;
- Picker results/tray/count/receipt;
- URL state;
- browser history;
- local/session recovery;
- object/query/suggestion caches;
- hidden DOM nodes and data attributes;
- ARIA labels/descriptions;
- live regions;
- document title/breadcrumb chrome;
- loading/skeleton cardinality;
- copy/share surfaces;
- telemetry and performance metrics.

Protected content must be absent from unauthorized DOM/accessibility state. `display:none`, disabled controls or locked placeholders are not acceptable substitutes when their existence would disclose hidden identity/cardinality.

## Revocation/cache transition tests

The 16 privacy scenarios apply deterministic test overlays to real governed identities; they are **not canonical visibility claims**.

Required transitions include:

- hidden `Absolute Authority` excluded from search/count/facets/suggestions;
- forbidden exact ID indistinguishable from nonexistent ID;
- Mythragara open under broader authority, then revoked while Inspector/provenance/history state exists;
- browser Back/Forward after revocation requiring fresh authorization;
- redacted provenance containing no source title/path/coordinate/fragment;
- denied relationship targets excluded from permitted counts;
- compare side restriction preventing inaccessible diff computation;
- Picker item revoked after provisional selection, causing atomic revalidation failure/no partial receipt;
- recovery rehydrating only IDs still permitted;
- logout clearing protected A2 detail/provenance/compare caches;
- ARIA/live regions/document title following the same redaction boundary;
- auth-scoped suggestion caches unable to replay broader-authority results;
- loading/skeleton states not leaking preauthorization cardinality.

## Cache/recovery rule

A cache hit is never authority. Search, suggestion, Inspector, relationship, provenance, compare and Picker caches must either include the relevant authorization/entitlement/corpus/caller projection version in the cache scope or be invalidated before use.

Recovery records remain stable-ID/view-intent records only. They do not store rendered protected payloads, source fragments, authorization decisions, full selection receipts or entitlement tokens as current authority.

## Telemetry boundary

Telemetry uses bounded categorical/count/latency buckets. Hidden names, restricted stable IDs, source fragments, entitlement tokens, auth payloads and sensitive raw query text are forbidden where the v0.5 event matrix marks them protected.

Performance instrumentation itself is treated as a privacy surface: it may emit operation and bucketed latency/result count, not hidden identities.

## Codex integration

Transfer this suite during A2-01 with the other A2 addenda and apply it progressively:

- A2-02/A2-03: full 11,861-object search/filter/facet/suggestion budgets and leakage gates;
- A2-04/A2-05: result/Inspector render budgets plus DOM/accessibility redaction;
- A2-06: relationship/provenance bounds and revocation leakage;
- A2-07/A2-08: Picker cache/recovery/revalidation leakage and atomic receipts;
- A2-09: compare/history/cache revocation tests;
- A2-10: run all 72 blocking performance/scale/privacy assertions and capture raw measurement/security evidence.

Do not add a hosted search provider or new runtime dependency merely to satisfy these budgets. That remains a governed A2 stop condition.

## Preservation boundary

This handoff does **not** change `CURRENT_WORK_POINTER.json`, does not activate A2 application implementation, does not alter the owner-selected Design Standards primary attempt, does not create production performance guarantees, does not change canonical content visibility, and does not authorize internal-alpha release, production release or deployment.

## Exact next pre-Sunday A2 operation

Create one **consolidated Sunday Codex master execution bundle** that supersedes the earlier scattered transfer burden without superseding their authority: include/reference the governed v1.0 work order package plus v1.1 profile/source mapping, v1.2 search suite, v1.3 Picker/Scene suite, v1.4 compare/provenance suite, v1.5 visual/accessibility reference and this v1.6 performance/privacy package. Update the one-pass Sunday instructions, dependency/transfer manifest, expected test/evidence counts, checksum inventory and exact day-one execution order so the owner can hand Codex one archive and one start instruction.