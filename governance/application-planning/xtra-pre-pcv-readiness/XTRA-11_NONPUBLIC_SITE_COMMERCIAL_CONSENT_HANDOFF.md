# XTRA-11 — Nonpublic Demo, Website, Consent, Pricing and Lifecycle Preparation

**Edition:** 2026-11-02 · **Scope:** selected XTRA-11 source-only templates for future MCB-09..25. **No MCB tranche activation.** This document does not authorize a website, waitlist, advertisements, emails, paid vendor changes, customer contacts, tracking, subscription checkout, real financial claims, or public media. Companion: [the machine-readable commercial preparation matrix](XTRA-11_NONPUBLIC_COMMERCIAL_PREP_MATRIX_v1.0.0.json) and `tests/control_plane/test_xtra11_commercial_preflight.py`.

## 1. Evidence and decision boundaries

The canonical [MCB Program](../market-capture-brand-backbone/MCB_MARKET_CAPTURE_AND_BRAND_BACKBONE_PROGRAM.md) defines **17 future tranches MCB-09..25**, but their [backlog](../market-capture-brand-backbone/MCB_PROGRAM_BACKLOG.json) is entirely **planned**, not selected. This tranche prepares handoffs, **not any of those 17 implementations**.

[XTRA-10](XTRA-10_MARKET_CATEGORY_PERSONA_BRAND_CLAIMS_HANDOFF.md) provides seven self-described vendor competitors, four unvalidated audience hypotheses, eight unused interview questions, eight nonpublic audience-copy drafts and sixteen **unapproved public claims**. All planned public pages, demonstrations, price copy and outreach must depend on an independently current approval receipt rather than a draft claim. [XTRA-06](XTRA-06_PCV_ACCEPTANCE_HANDOFF.md) keeps full PCV-04..10 acceptance predecessor-blocked. [XTRA-09](XTRA-09_OPERATOR_READINESS_AND_INCIDENT_RUNBOOK.md) does not prove a live backup/restore; XTRA-02 remains externally blocked with a November 8 2026 recorded Render DB expiry.

Separate **design intent → repo/source evidence → reproducible fixture → installed real-device proof → verified consent/rights → approved public/commercial statement**. Skipping any layer creates false evidence.

## 2. Deterministic demo and media design (MCB-09/22)

The proposed demo story uses the **XTRA-04 first-party Beacon Debt five-scene fixture**, not a fabricated live session:

| Scene / script role | Intended user-visible story | Release evidence still required |
| --- | --- | --- |
| Gate Pressure / GM | Setup, permissions and hidden clue | Actual GM-only projection and rights-cleared scene media |
| Damaged Crossing / Player | Character action and GM decision | Two-human independent session action and reconnect |
| Beacon Restoration / GM | Canonical state, repair and checkpoint | Durable installed sequence and checkpoint proof |
| Listening Market Investigation / Player | Investigation without GM-only leak | Role-safe capture and correct asset licenses |
| Consequence and Return / Creator | Owned custom definition vs Campaign derivative | Actual entitlement/rights and share boundaries |

Each storyboard frame is explicitly `fixture_only=true`, `filmed=false`; neither screenshots nor fake testimonials are created. Future media capture receipts should include the exact installed app head/installer, synthetic dataset, device/role, permission projection, text alternatives, license chain, release consent, screenshot/video digest and human review. No staged UI may be presented as captured native functionality.

## 3. Site navigation and original SEO content (MCB-10/11/12)

Ten proposed unhosted paths: `/`, `/for-gms`, `/for-players`, `/for-creators`, `/how-it-works`, `/demo`, `/pricing`, `/privacy`, `/faq`, `/contact`. All are **information-architecture sketches, not working URLs**. The suggested information order is: who the game serves; accurately bounded capabilities; sample Campaign; current limitations (including no launch VTT); evidence-backed trust and privacy; only then an optional consented future action. Role pages must distinguish design/source demo from installed proof.

Eight proposed original-content search intents concern first sessions, d20 character creation, permissioned Campaigns, custom settings, local vs managed Session authority, VTT comparisons, GM allowances and Multiversal rules. They are **topic hypotheses, not observed search volumes or ranking estimates**. Google [Search Essentials/Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) encourages understandable site structure, useful accurate people-first content and descriptive URLs; no SEO guarantee follows. Preserve author, dated source, internal evidence claim IDs, review status, accessibility and rights for each content artifact.

**Sample page specification, not final website copy:** `/for-gms`: headline about preparing a Multiversal Campaign with fewer disconnected steps is only a *benefit hypothesis*; show the Beacon Debt illustrated storyboard with “source demonstration, not installed multiplayer proof”; include a bounded FAQ on GM-only notes and Campaign allowance status; no “Try Now”, “Join Waitlist” or price button until actually supported, compliant and approved. CTA remains a disabled research-design placeholder.

## 4. Pricing and GM-to-Player allowance research (MCB-19/20/21)

Five **unpriced, not configured, not available-for-sale hypotheses**:

- Free baseline Player access; capabilities derived from verified actual entitlement rules, not unlimited promises.
- GM subscription supporting Campaign/session preparation; one allowance per Player per Campaign **only under a verified currently subscribing GM** if the actual backend implements it.
- Campaign-scoped Player allowance for one custom setting and dependencies **or** a species/item set/ability tree; cannot transfer dependent content or character out.
- Creator/workshop add-on hypothesis, with nonportable/third-party rights explicitly preserved.
- Family/hybrid use concept, requiring additional minors, consent, product and accessibility review.

No dollar price, free trial length, payment plan, vendor merchant ID, billing API or refund policy is authorized. The historical $4.99/month idea must not be printed as a binding price. Evaluate future pricing against observed GM-to-Player invitations, consented conversion, entitlement denial/support load, churn and real invoice/refund costs, not arbitrarily invented CAC, LTV or ARPU. The machine-readable unit-economics fields are intentionally `null`.

Before any live subscription, independently approve accurate terms, consent, cancellation and authority, with legal review of **currently applicable** consumer rules. The [FTC Negative Option Rule page](https://www.ftc.gov/legal-library/browse/rules/negative-option-rule) is a legal-research starting point, **not proof that a particular old rule applies in 2026**; recheck any changes and state-specific obligations before release.

## 5. Consent-safe audience development (MCB-13..18)

**There is no live waitlist**. The optional future interest form may include separate affirmative choices for **alpha research invitations** and **product updates**. Defaults are unchecked. Submission stays disabled until owner-approved purpose, privacy notice, eligibility/age review, storage encryption, retention/deletion, consent receipts, suppression and tested access controls exist. Do not collect contacts, run interviews, log browser identifiers or send a single email in XTRA-11.

Lifecycle **concepts**, not actual customers: discovery → reading → interest draft → pending opt-in → verified opt-in → invited → first Campaign → retention → unsubscribed. Event definitions such as `page_view`, `opt_in_confirm`, `invite_accepted`, `subscription_started`, and `unsubscribe_confirm` exist **only** in a synthetic taxonomy; `enabled=false`, `observed_count=0`, and no private payload is allowed.

For future promotional email, [FTC CAN-SPAM guidance](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) explains sender identity, truthful subject, address and working opt-out practices. Transactional/account emails require distinct classification; do not treat an account invite as blanket consent to marketing. Current jurisdiction, minors and privacy laws require independent review. A future opt-out should remain effective even if a Campaign account is restored or source identity changes.

Partner/creator CRM is a schema only; not scraped people or contact records. Community design must allocate spoiler, harassment, ownership, moderation and family safeguards *before* the first public recruitment or official community launch.

## 6. Trust, analytics, simulated launch and expansion (MCB-18/23/24/25)

Avoid “AI solves your problems”, “guaranteed private”, “100% encrypted”, “all settings included”, “all devices sync now” or market-share assertions. Trust language must explain **GM vs Player visible data**, earned Campaign allowance, owned vs permissioned derivative content, actual offline lease limitations, support/privacy request paths, and honest status of protections.

Every future analytics event needs a legitimate measurement purpose, owner and consent assessment, data minimization, actor/Campaign privacy, retention, tested redaction, access controls and exact source signal. The eight event names are design identifiers only. Do not turn an imagined Campaign or on-branch test into a real conversion.

**Simulation:** The matrix includes **59 explicit negative vectors** across real public-site, media, signup, email, billing, interviews, analytics, paid campaigns, partner outreach and synthetic-launch gates. Only one assumption-complete, entirely isolated **synthetic tabletop** may result in `SIMULATION_ONLY`. Every attempted *real* operation is DENY by the reference oracle, even when caller-provided flags are true. Any actual approval must come from a separate governing process with real evidence; this test cannot confer it.

**Expansion hypothesis:** Start with Multiversal GM-first workflow research → invite-driven Player validation → Creator rights/authoring feedback → hybrid/remote, families and publishers only after real consented observations. That is a proposed study sequence, not a forecast, customer list or growth plan approved for deployment.

## 7. Open owner/runtime gates

| Required future decision or proof | Present state |
| --- | --- |
| Actual authenticated cross-device PCV-03F and human MTLC-14 experience | Not certified by XTRA |
| Real Render archive and independent restore or explicit expendability decision | XTRA-02 `blocked_external`; November 8 expiry on existing record |
| Demo rights, independent screenshot and real app role-specific source receipt | Not performed |
| Public site, brand visuals, privacy/cookie policy, approved legal claims | Not approved |
| Specific data inventory, consent, eligibility, age/family checks, storage, opt-out | Not approved; **zero contacts** |
| Final price/SKU/merchant, accurate renewal/cancellation/refund and paid launch | Not approved |
| Marketing email, campaign spend, live analytics, community and partner contact | Not approved; **zero outreach** |
| MCB tranche implementation or commercial readiness completion | **All MCB-01..25 remain planned** |

**XTRA-11 acceptance** requires the source-only registry, operator handoff and Python reference regression to pass exact-head validation and protected-main publication. It does not complete, activate or authorize any MCB tranche. Handoff to XTRA-12 may reference these templates while retaining every live/owner-only blocker.
