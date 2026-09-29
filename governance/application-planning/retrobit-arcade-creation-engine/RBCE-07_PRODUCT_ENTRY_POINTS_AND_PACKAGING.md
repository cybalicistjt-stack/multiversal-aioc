# RBCE-07 — Product Entry Points & Packaging

**Program:** Retrobit Arcade & Creation Engine (RBCE)  
**Work item:** RBCE-07  
**Status:** OWNER-DIRECTED DESIGN BASELINE  
**Operational authority:** none; this artifact does not select implementation and cannot override OPS3  
**Consumes:** RBCE-01 through RBCE-06, Multiversal Pack List architecture, GPR delivery/roster semantics, MAI rights/provenance, canonical owner permissions

## 1. Purpose

RBCE-07 completes the first Retrobit productization sequence by defining the product entry points through which people create, discover, play, embed and roster a Retrobit project, plus the governed path from a publishable Retrobit Game Project to a portable Multiversal `.pack`.

RBCE-07 is a product-routing and package-candidate contract. It does not create a second gameplay runtime, content authority, asset authority, campaign authority or archive/compiler format.

## 2. Authority

Authority remains outside RBCE-07:

- **GPR** owns gameplay execution, delivery-mode readiness and roster-injection runtime semantics.
- **MRCS/canonical owners** own governed definitions and canonical mutations.
- **MAI / ARI / PCA** own asset provenance, rights and redistribution capability.
- **RBCE-01** owns the Retrobit Game Project format and playable/publishable lifecycle.
- **RBCE-02** owns Retrobit 2D projection profiles.
- **RBCE-03** owns creator-facing Studio authoring.
- **RBCE-04** owns Retro Asset Workbench preparation/handoff.
- **RBCE-05** owns the creator-facing Gameplay Parts projection.
- **RBCE-06** owns golden-game conformance proof.
- The **canonical Multiversal `.pack` compiler/installer contract** owns final archive layout, stable package paths, archive encoding, installation/uninstallation mechanics and final schema compliance.

RBCE-07 may build and validate a package candidate, request canonical compilation, inspect/import a final `.pack`, and expose the resulting project through product entry points. It may not silently invent compiler internals.

## 3. Required product entry points

The first product surface exposes exactly these owner-approved intents.

### `entry:create-retrobit-game`
Starts or resumes a Retrobit project in RBCE-03 Studio. Creation does not imply campaign or canonical owner mutation.

### `entry:play-arcade`
Opens a playable Retrobit project from local/installed Arcade library context and starts an allowed GPR delivery mode. `playable` is sufficient for local play when local-use rights are satisfied; `publishable` is not required.

### `entry:add-campaign-minigame`
Creates a governed campaign attachment proposal for a project that declares `embedded-minigame`. The owning campaign must accept the attachment and all returned outcomes remain typed owner proposals/receipts.

### `entry:attach-scene-object`
Creates a governed reference/attachment proposal from a Scene/Object host to a Retrobit project. The host owner remains authoritative and gameplay state is referenced rather than cloned.

### `entry:use-existing-character-roster`
Projects existing canonical Character/Roster identities into supported Retrobit roles. Canonical Character identity/state remains owner-held.

### `entry:standalone-roster`
Provides a non-campaign roster flow for direct Arcade play. Project/run-local actors are allowed and remain clearly non-canonical.

## 4. Arcade library and launch behavior

The Arcade library is a product projection over available Retrobit projects/packages. It may expose title, presentation metadata, version, lifecycle/readiness, supported delivery modes, roster requirements, accessibility summary, provenance/publication status and install/update state.

Library indexing, search order, favorites, recents and visual merchandising are presentation state only.

A launch request resolves:

`entry point -> project/package identity -> lifecycle -> dependencies -> rights for requested use -> delivery mode -> roster/context requirements -> GPR launch`

Any unresolved required gate fails closed with an actionable diagnostic.

## 5. Package lifecycle

RBCE-07 aligns with the existing Multiversal Pack List lifecycle:

`Retrobit authoring project -> validation -> package candidate -> cross-object/dependency review -> canonical pack compilation -> final .pack`

The package candidate is not a final `.pack`. A final `.pack` can be claimed only after the canonical compiler returns successful compilation evidence.

## 6. Package-candidate logical contents

A Retrobit package candidate carries these logical content roles without fixing archive paths:

1. normalized `retrobit.project.json` project payload;
2. package identity and project/schema versions;
3. dependency manifest;
4. embedded asset manifest;
5. provenance/rights manifest;
6. integrity manifest and deterministic semantic fingerprint;
7. accessibility/presentation discovery metadata;
8. migration metadata;
9. validation receipt set.

Exact archive filenames/directories, compression, signing, binary layout and installer database representation remain canonical compiler/installer decisions.

## 7. Embedded versus referenced content

The RBCE-01 policy remains controlling: embedded assets are `redistributable-only`.

A dependency may be embedded only with explicit redistribution capability, referenced only through an allowed governed dependency model, or blocked when rights/version/dependency resolution is missing.

Transform permission does not imply redistribution permission. Local-use permission does not imply redistribution permission. Rights silence is never permission. Protected study/reference expression may remain in research provenance, never as a production dependency.

## 8. Package validation gates

A package candidate must fail closed unless all applicable gates pass:

1. supported schema and explicit migration state;
2. publishability for the selected distribution target;
3. deterministic normalized project fingerprint;
4. dependency closure;
5. no ambiguous/conflicting required versions;
6. required runtime/definition/capability references resolve;
7. redistribution rights for every embedded asset;
8. zero protected production dependencies;
9. no local absolute paths or path traversal;
10. integrity coverage for candidate payloads;
11. required blocking-test/conformance receipts;
12. explicit install-conflict policy;
13. canonical compiler compatibility.

`playable`, `publishable`, `package-ready` and `compiled` remain distinct states.

## 9. Compile/export/share

Normal export flow:

`Validate publishability -> Build candidate -> Preview manifest/dependencies/rights -> Request canonical compile -> Verify compiler result -> Save/share .pack`

Rules:

- `.pack` is the only portable package extension for this program;
- a candidate/review JSON is never mislabeled as a final pack;
- compiler errors block final export;
- local file export/share does not require a marketplace or cloud provider;
- no Retrobit v1 pack may introduce arbitrary executable scripting.

## 10. Import/install

Import is inspection-first:

`Select .pack -> Read manifest safely -> Validate schema/integrity -> Resolve dependencies/compatibility -> Preview install -> Explicit install -> Index in Arcade`

Before explicit install, import may not execute gameplay, mutate campaign state, fetch arbitrary network dependencies or overwrite installed content.

Hash mismatch, unsupported schema, path escape/traversal, unresolved required dependency or forbidden content blocks installation. Version collisions never silently replace installed content; resolution is explicit and installer-governed.

## 11. Campaign and Scene attachment records

Campaign-minigame and Scene/Object integration use owner-governed attachment/reference records containing stable project/package identity, version requirement, requested launch mode, optional host reference, optional governed roster mapping, typed outcome channel and owner permission/receipt metadata.

Attachments never embed duplicate Character, Scene, campaign objective, inventory or other canonical owner state.

## 12. Roster projection

Existing-character use follows:

`canonical identity -> authorized projection -> Retrobit participant role -> typed outcomes back to owners`

Retrobit may retain only the governed reference/projection needed by the run. Standalone Retrobit-local actors cannot be mistaken for canonical Characters.

## 13. Save, replay and package identity

Packaging does not merge authoring state, runtime save state and canonical owner state.

Package updates/reinstalls may not silently reinterpret incompatible saves; explicit migration/compatibility evidence is required.

## 14. Accessibility

All six entry points, package validation, manifest/dependency review, import/install conflict resolution and roster selection require keyboard-operable, screen-reader-usable paths. Critical readiness/rights/dependency states cannot rely on color alone.

## 15. Local-first and provider independence

The required path works with AI and paid cloud disabled: create/resume locally, discover local projects, play with installed dependencies, build/inspect candidates, compile/export when the canonical compiler is installed, inspect/install local `.pack` files, and use standalone roster flows.

Optional AI may explain problems or suggest metadata. It cannot grant rights, resolve missing dependencies, change permissions, mark content publishable or synthesize compiler success.

## 16. Security and trust boundaries

A Retrobit `.pack` is data, not an arbitrary code/plugin channel. Import fails closed on arbitrary executable/script payloads outside approved contracts, path traversal/absolute-path writes, integrity mismatch, unsupported schema, undeclared dependencies, protected production dependencies, malformed identity or unresolved installation conflict.

External references do not authorize automatic network download.

## 17. Diagnostics

Reserved diagnostics include:

`entry-point-unsupported`, `entry-point-permission-denied`, `project-not-playable`, `project-not-publishable`, `delivery-mode-not-declared`, `delivery-capability-unavailable`, `roster-injection-not-supported`, `roster-owner-capability-unavailable`, `attachment-owner-receipt-required`, `package-candidate-invalid`, `package-dependency-unresolved`, `package-dependency-version-conflict`, `package-embedded-rights-missing`, `package-protected-production-dependency`, `package-integrity-mismatch`, `package-local-path-forbidden`, `package-path-traversal-forbidden`, `package-schema-unsupported`, `package-migration-required`, `package-install-conflict`, `canonical-pack-compiler-unavailable`, `canonical-pack-compilation-failed`.

Diagnostics normalize by code, semantic path and stable reference.

## 18. Four-Engine Test Chamber acceptance use

Once implementation is authorized, the golden project must demonstrate: Play Arcade launch, direct-play completion, campaign-minigame attachment proposal, Scene/Object attachment proposal, existing-character projection, standalone roster launch, package-candidate construction, redistribution-only embedding, dependency/provenance/integrity review, canonical compile result handling, safe import/install round trip, identical semantic project fingerprint after round trip, and fail-closed bad-hash/missing-rights/unresolved-dependency/version-conflict cases.

RBCE-07 design evidence does not claim those executions have occurred.

## 19. Machine identifiers

- schema ID: `RBCE07.PRODUCT_PACKAGING.v1`
- semantic version: `1.0.0`
- package extension: `.pack`
- project payload filename: `retrobit.project.json`
- embedded asset policy: `redistributable-only`
- package authority: `canonical-multiversal-pack-compiler`
- installer authority: `canonical-multiversal-pack-installer`
- default presentation skin: `retrobit-classic-arcade`

## 20. Explicit non-decisions

RBCE-07 does not decide final archive path layout, compression/container algorithm, signing/trust-store technology, marketplace/community policy, cloud sync, installer side-by-side/update implementation, exact size caps or platform-store rules.

## 21. Activation boundary

This is durable content/design only. Product implementation begins only when OPS3 explicitly selects and authorizes RBCE-07 or equivalent governed implementation work.

Completing this design tranche completes the owner-approved **RBCE-01 through RBCE-07 planning sequence**. It does not authorize implementation, alter the live PCV-03F work item, or claim that the Four-Engine game/runtime/package has been executed in the application.
