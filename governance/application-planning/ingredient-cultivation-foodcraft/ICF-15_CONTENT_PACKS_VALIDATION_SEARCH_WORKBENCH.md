# ICF-15 — Content Packs, Validation, Search & Workbench

**Status:** implementation candidate  
**Authority:** ICF-15 only  
**Upstream:** ICF-02 through ICF-14 completed foundations  
**Downstream:** MIB-14 resumes only after ICF-15 closeout

## Decision

ICF-15 publishes the completed Ingredient, Cultivation & Foodcraft foundation as a deterministic, provider-neutral content/search/inspection package. It does **not** create another content authority, search truth, inventory ledger, economy, scheduler, recipe engine, creature-harvest engine, or Cozy automation path.

Canonical ICF source/rule/crosswalk artifacts remain authoritative. ICF-15 outputs are compiled packs, validation evidence, search projections and read-only inspector/workbench contracts.

## Compiled foundation

The registry accounts for **971 primary ingredient definitions** (964 from ICF-03..06 plus 7 ICF-09 signature ingredients), **400 ICF-10 derived preparations**, **319 ICF-14 recipes/templates/source formulas**, and **27 ICF-09 canonical creature-harvest crosswalk records**: **1,717 searchable projected records** total. Six governing rule sets remain owned by ICF-07/08/11/12/13/14.

Existing tranche materializers remain the deterministic source of expanded ingredient/preparation/recipe packs. The ICF-15 compiler orchestrates them, copies the governed ICF-09 crosswalk/signature packs, emits SHA-256 pack receipts, and builds a stable-sorted provider-neutral search projection.

## Validation

Validation is fail-closed for duplicate stable identities; alias shape and ambiguity without alias-as-identity; reference resolution; property/effect authority; typed quantities/units/ranges; template executability and compatibility; creature-harvest coverage; provenance and unresolved-gap preservation; Downtime/Project and Cozy boundaries; and D17/MIB-13 owner-domain boundaries.

## Harvest coverage

ICF-09 gives exact catalog crosswalk coverage for 27 canonical creatures, but catalog coverage is not executable harvest coverage. At ICF-15 closeout, 27/27 creature definitions are represented exactly once, 27/27 retain `harvestProfile.evidenceStatus = gap`, and **0** have a fully executable harvest profile because authored harvest mode/yield evidence is absent. Six creatures link to seven canonical signature ingredients; seven creatures have some authored anatomy evidence; two have an explicit body-plan profile; five have an explicit trait-affinity profile; and the seven unresolved ICF-06 creature-derived bindings remain unresolved.

ICF-15 exposes these facts instead of inventing anatomy, yield, edibility, safety, legality, tools, preservation, or contamination rules.

## Search and facets

ICF-15 reuses **MV-IA-F002 Universal Object Experience** and the PPIA-02 inspector/projection principles. Search is a derived index, never a replacement registry. Authorization and field filtering occur **before** suggestions, counts, facets, relationships, provenance, or comparison are computed. Unauthorized object existence cannot leak through hidden counts or facet cardinality.

Supported projections are Ingredient, Derived Preparation, Recipe/Recipe Template/source formula, and Creature Harvest crosswalk. Facets cover taxonomy, nature/origin, rarity, availability, acquisition, edibility, perishability, production eligibility, transformation lineage, recipe family/kind/authorship/output form, harvest evidence/body-plan/trait/signature state, and source-coverage gaps. Display names, aliases, filenames, and provider IDs never replace stable identity.

## Inspectors and workbench

The **Ingredient Inspector** shows identity, taxonomy, physical/unit/storage data, ecology/production eligibility, culinary/magical/alchemical profiles, quality-condition authority, linked processing/recipes, coverage, and provenance. It cannot set live quantity/quality, price, or automation authority.

The **Recipe Inspector** shows family/authorship, exact inputs or unresolved template slots, process/output, owning outcome authority, generation/template state, validation, and provenance. Template instantiation creates a proposal only; it cannot invent an effect, silently bind an unresolved template, or directly commit live output.

The **Creature Harvest Inspector** shows creature identity, source evidence, authored anatomy/traits, harvest profile, signature ingredients, edibility/safety/legality assertions, coverage gaps, and provenance. It cannot infer anatomy, harvest yield, or edibility from names/type and cannot directly create loot/inventory.

The workbench is a read-only/diagnostic composition surface for search/filter/compare, ingredient → preparation → recipe tracing, creature → signature ingredient tracing, unresolved reference/alias/gap findings, template proposals, and launching separately authorized Project/Downtime or Asset workflows. It is not a second authoring/publication or live-state system.

## Downtime and Cozy validation

ICF metadata may say an operation is **eligible to be considered** for bounded Cozy automation. That is metadata only. It never means unattended progress, automatic spending/sales, automatic human/GM decisions, wall-clock elapsed time becoming Campaign time, or bypassing Project/Downtime, D17, MIB-13, or other owner-domain checks. APM/CEL remains the automation authority after fresh authorization.

## Deterministic evidence

ICF-15 adds JSON/Markdown and Python-standard-library compiler/validator artifacts only. There is no platform-specific application/runtime delta and no migration `0022`. The compiler normalizes emitted paths, explicitly sorts projected records, serializes deterministic JSON, and SHA-256 hashes emitted bytes. Final AIOC acceptance therefore uses the registered governance-only repository-health exception; application Windows/Linux runtime validation is not triggered by this content/compiler tranche.

## Completion invariants

- 1,717 governed searchable projections are accounted for by the pack registry;
- identity remains stable-ID based;
- prior ICF authority boundaries remain intact;
- all 27 canonical creature crosswalk gaps remain visible and fail-closed;
- unresolved source/template/harvest gaps remain first-class diagnostics;
- universal search/inspector permission and accessibility contracts are reused rather than forked;
- D17 owns live Asset state; MIB-13 owns current price/scarcity; APW-03/existing Project owns long-running activity orchestration; APM/CEL owns Cozy automation authorization;
- no provider-dependent authority, real-money behavior, or migration `0022`.
