# PCM — Proprietary Capability Mining Clean-Room & Rights Rules

**Status:** OWNER-APPROVED PLANNING CONTROL  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-09-09  
**Implementation authority:** none

## Purpose

PCM may study proprietary products to identify useful problem definitions, workflows, user-facing affordances, interoperability patterns and measurable production outcomes that Multiversal can independently implement. PCM is not authorization to clone proprietary software.

## Mandatory clean-room boundary

1. Study public product documentation, public demos, lawful ordinary-use behavior, published APIs/SDKs and licensing terms.
2. Extract **capability descriptions and workflow requirements**, not proprietary implementation details.
3. Do not decompile, disassemble, bypass access controls, scrape protected services, recover private protocols, copy proprietary source, copy protected assets/content, or use confidential/leaked material.
4. Do not reproduce distinctive copyrighted text, art, sample projects, branded content, proprietary datasets or vendor-specific protected expression.
5. Do not treat trial/evaluation access as permission to reverse engineer or redistribute.
6. Any third-party code, model, SDK, asset or dataset proposed for direct incorporation receives its own ARI rights/license/provenance review. Public availability alone is insufficient.
7. Multiversal-native implementations must be designed from Multiversal requirements and owner-domain contracts. Vendor names may remain in planning provenance but must not become product-facing identity unless separately licensed.
8. Where a product's value depends on a network, marketplace, recruited human panel, proprietary training corpus or licensed runtime that would be irrational to recreate, prefer `USE_AS_IS` or `LICENSE_TEMPORARILY` rather than pretending the surrounding business/infrastructure is a small software feature.
9. A native implementation may use open-source components discovered by the separate resource survey only when their licenses and provenance permit the intended use.
10. No PCM finding may silently change canonical game rules, story truth, Character truth, World truth, asset rights, AI authority, audio semantics, localization authority or release authority.

## Classification vocabulary

- `USE_AS_IS` — external product provides high value and rebuilding it is not economically sensible.
- `LICENSE_TEMPORARILY` — use during production/prototyping while keeping an exit path.
- `STUDY_PATTERNS` — useful workflow lessons; no direct dependency intended.
- `BUILD_MULTIVERSAL_NATIVE` — independently implement a bounded Multiversal-specific capability because recurring value/cost/control justify ownership.
- `IGNORE` — insufficient current value, obsolete/unavailable, redundant, or strategically poor fit.

A catalog entry may carry a primary classification plus secondary notes, but only `BUILD_MULTIVERSAL_NATIVE` may create PCA scope.

## Native-build test

Before a PCA tranche implements a vendor-derived capability, it must answer yes to all of the following:

- Is the capability useful to Multiversal independent of the vendor?
- Can the useful subset be described without vendor-specific protected implementation details?
- Does an existing Multiversal owner not already provide the same capability?
- Can the new tool consume existing owner truth rather than creating parallel canonical state?
- Is there meaningful leverage in reduced recurring cost, faster content production, local/offline operation, deterministic reuse, provider independence, or lower AI-credit usage?
- Is the proposed tranche narrow enough for the governed family execution method, or split before start?

## Provider and paid-service boundary

This planning approval creates no paid subscription, procurement, credential, provider activation, public upload, data-sharing or production-service authority. Any later external-service use must be approved and reverified against then-current pricing, terms, privacy, data retention, rights and export behavior.

## Provenance rule

Every PCM product entry records the public source used for capability study and the date checked. PCA design artifacts must cite PCM capability IDs rather than presenting vendor behavior as Multiversal source authority.
