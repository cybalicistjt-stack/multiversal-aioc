# Multiversal Application Implementation Roadmap — Cross-Cutting Product TODO Supplement

**Document ID:** MV-APP-ROADMAP-XCUT-001  
**Status:** OWNER-APPROVED TODO SUPPLEMENT — NOT IMPLEMENTATION-ACTIVE  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-18  
**Roadmap integration target:** next canonical `APPLICATION_IMPLEMENTATION_ROADMAP.md` reconciliation

## Purpose

This supplement preserves owner-approved product requirements that must remain visible in the application roadmap while the main roadmap is awaiting a broader canonical-state reconciliation. These requirements are cross-cutting and must not be lost merely because their detailed design/implementation tranche has not yet been activated.

This supplement does **not** change the current runtime pointer, supersede active CCTI work, authorize release/deployment, or activate either requirement for implementation. The next roadmap reconciliation must fold these TODOs into the main application roadmap and preserve their cross-cutting nature.

## TODO-UX-VOICE — Multiversal Product Personality and Assistance Standard

**Status:** TODO — canonical product-wide design standard required before product-language/UI-assistance freeze.

Multiversal is creative, broad in scope, and complex behind the scenes. Its visible personality must make that complexity approachable without diminishing the user's intelligence or creative ownership.

Canonical direction:

> **Multiversal is a knowledgeable, creative companion: warm enough to invite experimentation, confident enough to give clear guidance, and restrained enough to respect the user.**

The intended voice and interaction personality is:

- warm and welcoming;
- encouraging and quietly enthusiastic;
- curious and creatively supportive;
- comparable to a capable older brother or gentle mentor;
- clear and confident when explaining complexity, errors, limits, or consequences;
- respectful of the user's intelligence, autonomy, taste, and authorship;
- never obsequious, saccharine, infantilizing, excessively congratulatory, performatively cheerful, or evasive about problems.

This personality must be expressed consistently across, at minimum:

- onboarding and first-run guidance;
- navigation and empty states;
- tooltips, contextual help, teaching, and tutorials;
- warnings, validation, recovery, and error messages;
- Player and GM assistance;
- creator/storycraft/world/adventure authoring surfaces;
- notifications and status messages;
- optional AI-assisted features;
- accessibility/help/support language;
- future community and social surfaces.

Detailed work must define reusable voice principles, UI-copy patterns, anti-patterns, error/recovery tone, encouragement thresholds, assistance behavior, and acceptance examples. This requirement should be reconciled with the existing UI Design Bible, Screen Design Bible, onboarding/help work, APW, CSW, and future contextual-assistance design rather than creating a competing design authority.

## TODO-FSF — Family Safety / Parental Controls Framework

**Status:** TODO — future bounded architecture/design track required before broad minor-facing community, stranger-discovery, public-publishing, marketplace, or matchmaking exposure.

Multiversal should provide meaningful platform-level safety controls for parents/guardians who purchase or manage the application for children. The system must be explicit about its boundary: Multiversal can govern platform capabilities and exposure, but cannot guarantee or fully control the speech, conduct, or fictional content introduced by other human participants in tabletop play.

Canonical boundary:

> **Parental controls govern Multiversal-controlled capabilities and exposure; they do not claim to control or guarantee the conduct, speech, or fictional content introduced by other human participants.**

Family safety must be modeled as an account-policy/capability axis, **not** as a permanent gameplay role. Player, GM, Assistant GM, creator, owner, observer, and similar authorities remain contextual Campaign/resource roles. A user under a family-safety policy may still legitimately be a GM, Player, creator, or other contextual role where permitted.

Future design should cover, as applicable:

- family-linked parent/guardian and child-account relationships;
- age-appropriate safety presets plus granular controls;
- privacy-by-default and reduced discoverability for child accounts;
- public profile, stranger discovery, invitation, public Campaign, and community-content controls;
- communication controls, blocking, reporting, attachments, links, and unsolicited-contact restrictions;
- Campaign-joining approval and trusted-friend/family allowances;
- content descriptors, warnings, filtering, and maturity controls for platform-governed content;
- optional AI safeguards and child-account AI capability limits;
- purchase, subscription, marketplace, and paid-content authorization controls;
- public publishing/community-distribution controls while preserving private creation;
- safety/reporting center and clear visibility into active platform-level protections;
- separation of guardian safety authority from GM authority and from automatic surveillance of a child's private creative work;
- universal safety tools useful to all ages, including content preferences and easy exit/block/report flows;
- data minimization and privacy architecture appropriate to minor accounts;
- clear acceptance tests demonstrating what Multiversal can and cannot enforce.

Architecture that is expensive to retrofit—account/family relationships, capability-level permissions, privacy classifications, content descriptors, reporting/blocking primitives, guardian-vs-Campaign authority separation, and purchase authorization—should be established before dependent public/community systems are frozen.

This future framework should integrate with APW account/context authority, CSW private creation/publication flows, Campaign authority, future community worldbuilding/sharing, communications, commerce, discovery, optional AI, and any later social/matchmaking systems.

A bounded future track may use the provisional handle **FSF — Family Safety Framework**. Naming, tranche structure, legal/compliance review requirements, implementation sequencing, and release gates remain to be formally designed and owner-approved.

## Roadmap reconciliation requirements

At the next canonical `APPLICATION_IMPLEMENTATION_ROADMAP.md` reconciliation:

1. Add the Multiversal personality/voice standard as an explicit product-wide TODO and cross-cutting acceptance concern.
2. Add Family Safety / Parental Controls as an explicit future bounded TODO/track and preserve the human-participant enforcement boundary.
3. Place both in dependency order without interrupting the currently approved CCTI → roadmap reconciliation → tester-successor → APW/CSW sequence unless new repository evidence requires otherwise.
4. Preserve these requirements in future handoff/bootstrap/recovery projections once their execution windows become relevant.
5. Do not treat this supplement or roadmap notation as implementation completion.
