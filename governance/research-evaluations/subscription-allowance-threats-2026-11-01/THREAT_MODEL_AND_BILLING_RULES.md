# Multiversal — Subscription, Allowance, and Billing Threat Audit
**Study:** SA-BILL-01 · **Date:** 2026-11-01 · **Disposition:** security design/proposed reference semantics, NOT approved price, deployed billing, release, or new implementation authority.

## 0. Authority and evidence grades

**Established owner directive (2026-10-27 conversation):** one allowance **per Campaign per Player-user**, grantable by a GM **with a subscription**. The one allowance may unlock **one custom Setting with its governed dependencies**, or a **Species**, **item set**, **ability tree**, or another explicitly allowlisted grantable content class. It works **only for that Campaign** and the Player's participation in the game. The Player may access their Character and material they have in the Campaign under the authorized, non-transferable access-only state; they **cannot transfer restricted objects or restricted Characters out of that Campaign/Character**. These are product requirements, not a claim that a server-side implementation exists.

**Repository-derived current contracts:**
- AIOC `operations/CURRENT.json`: GPR PCV-03F service-first authoritative Session with PostgreSQL/HTTPS/WSS and A3/A5 control is **in progress**. It controls current implementation; read-only PCV-I01C local-host portability design does not override that active selection.
- App `packages/contracts/src/identity-device/entitlement-evaluator.ts`: free, subscription, sponsored-month and campaign-premium-grant; baseline official-content and a free Tier-2 Ability-tree cap. The evaluator **does not** encode the one-slot allowance, grant subject/type, dependency closure, transfer quarantine, external purchase authenticity, signed offline lease, or published price. It operates on caller-supplied records.
- App `packages/entitlements/src/entitlement-service-port.ts`: interface for grant operations; no billing provider or committed allowance ledger is established by this port.
- AIOC `governance/application-planning/internal-alpha/INTERNAL_ALPHA_SHARED_SYSTEMS.md`: SS-04 includes grants/sponsored access, expiry, reasoned decisions, offline snapshots and historical preservation.
- AIOC `governance/application-planning/internal-alpha/IA-D08-004_OFFLINE_DEFERRAL_READINESS.md`: only bounded cached reads, recoverable drafts and reauthorization; **no unrestricted offline ownership/entitlement mutation**.
- AIOC `governance/application-planning/internal-alpha/feature-packets/MV-IA-F020_PERMISSIONS_AND_HIDDEN_INFORMATION.md`: deny-by-default read/search/count/subscription/export/AI/command authorization and cache invalidation.
- App `DevelopmentBible/00-executive-overview/product-vision.md`: $4.99/month is an older entry-price *target*, explicitly not a paid-launch authorization. Subsequent informal pricing discussion must not be conflated with an adopted SKU.
- AIOC `governance/application-planning/internal-alpha/IA-D08-002_AI_PERMISSION_PROVENANCE_COST_FALLBACK_MATRIX.md`: optional AI costs are separately bounded and must not become a hidden automatic overage.

**External, time-sensitive requirements (checked 2026-11-01):**
- Google Play Payments / Subscriptions: digital in-app subscription normally uses Play Billing, subject to country-specific approved alternative billing and external link programs. United States rules changed and programs may add reporting/fees; don't assume alternative checkout is unrestricted. https://support.google.com/googleplay/android-developer/answer/9858738 and https://support.google.com/googleplay/android-developer/answer/15582165
- Google Play subscription lifecycle: query authoritative `purchases.subscriptionsv2.get` following notifications; cancellation normally leaves access through the paid term, grace retains access, account hold removes it, expiration removes it; upgraded plans can issue linked purchase tokens. https://developer.android.com/google/play/billing/lifecycle/subscriptions
- Apple App Review 3.1.1/3.1.2 (future iOS conditional): native digital goods/subscriptions usually require IAP subject to storefront exceptions, subscription value/disclosure/cross-device requirements; a campaign grant is not a substitute for a disallowed external checkout mechanism. https://developer.apple.com/app-store/review/guidelines/
- U.S. ROSCA/FTC Act: clear material terms, express consent and straightforward cancellation remain relevant. The **2024 FTC Click-to-Cancel amended rule was vacated in July 2025**, and FTC conformed its negative-option rule in February 2026; don't cite the vacated rule as current binding law. https://www.ftc.gov/legal-library/browse/statutes/restore-online-shoppers-confidence-act and https://www.ftc.gov/policy/public-comments/revision-negative-option-rule-withdrawal-cars-rule-removal-non-compete-rule-conform-these-rules-0
- Payment providers, tax jurisdictions, store territories, refunds and plan disclosures require future vendor/storefront-specific legal review. This is engineering risk analysis, not legal advice.

## 1. System assets, adversaries and trust boundaries

**Assets:** money/ledger, subscribed subject capability, active Campaign GM mandate, each Player's one Campaign allowance slot, registered content release + dependency graph, Character/Setting/Species/item ownership and provenance, encrypted protected packs and derived content, permission-safe search and exports, A3 sessions and bound device keys, audit/event ledger, platform purchase receipts, AI/provider budget.

**Adversaries:** unsubscribed Player requesting elevated content, formerly subscribed GM, subscriber sharing login across devices, player abusing shared link/import/export, malicious/compromised local client, stolen/offline device or copied install directory, replayed/refunded purchase receipt, malicious GM/account manager, compromised partner webhook, concurrency races, and honest users exposed to confusing billing states.

**Trust boundaries, all separate:** payment processor/store -> verified billing ingestion -> owner-side subscription ledger -> versioned entitlement decision -> Campaign role and one allowance slot -> registered content dependency/right projection -> Character operations -> transport/cache/export/AI. **Money paid does not grant GM role. GM role does not create subscription. Campaign membership does not make protected dependencies owned, transferable or globally available.** Source authority remains with A3/A4/A5/A9/A10/Species/Form and content/rights owners; the entitlement service evaluates permission, not authors those domains.

## 2. High-priority findings and risks

| ID | Priority | Finding and concrete exploit | Required control / evidence |
|---|---|---|---|
| SA-01 | Critical | A GM or Player forges a premium grant via client API/fixture/grant record | Server-issued grant mutation behind verified payment, GM authority, Campaign membership, subject/version/nonce checks; no client-trusted booleans |
| SA-02 | Critical | Two simultaneous grants both pass the one-slot count check | Database uniqueness on `(campaign_id,player_subject_id,slot_kind)` + serializable/atomic CAS, persistent slot history, retry-safe idempotency |
| SA-03 | Critical | Granted Setting dependencies escape to another Campaign through export, character copy, import or search | Recursive dependency/provenance taint closure; authorize every edge and derived object; deny restricted cross-Campaign transfer and protected bytes in exports |
| SA-04 | Critical | A GM cancels/refunds, is removed or loses subscription; grants remain usable indefinitely | Derived effective entitlement must depend on current GM subscription + current GM authority + Campaign/Player membership + active allowance; event-driven invalidation; record preserved |
| SA-05 | Critical | Old phone reuses premium keys/cache after remote revoke | Short bounded verified offline read-only leases with trusted-clock/monotonic antirollback, per-device keys, remote invalidation on reconnect, key rotation; never promise immediate offline erasure |
| SA-06 | Critical | Direct API, search count, autocomplete, websocket, AI prompts or backups leak restricted dependencies | Enforce row/field/graph authorization before query, indexing, projection, subscriptions, exports, telemetry, retrieval and AI; negative exfil tests |
| SA-07 | High | Cancellation status switches to "cancelled" immediately and wrongly strips still-paid access | Model `auto_renew=false` separately from entitlement `entitled_until` and revocation; verify with store/processor, preserve access through paid term |
| SA-08 | High | Refund/chargeback arrives late or duplicate/out-of-order webhooks change paid state | Verify signature and provider app/product/account, fetch current provider truth, idempotency keys, monotonic versions, event ledger, reconciliation; no webhook-order entitlement |
| SA-09 | High | Device-local time or malformed timestamp extends grant / bypasses expiry | Server UTC temporal validation + signed bounded lease; never compare untrusted arbitrary ISO strings lexicographically |
| SA-10 | High | User with separate accounts/linked email/device shares entitlement or receives duplicate allowances | Canonical A3 subject key, verified identity binding, unique purchase ownership and transfer dispute workflow; device ID not account ID |
| SA-11 | High | Old owned Character references subscriber-only object and transfers through "plain Character export" | Persistent source/digest lineage on Character, inventory, ability, derived stat, saves, assets; protected quarantine/authorized in-Campaign use only, even after copying |
| SA-12 | High | GM uses one allowance to install multiple independently premium packs by labeling all as dependencies | Trusted dependency graph from registered release, exact version, cycle and size caps, no arbitrary user-claimed transitive dependencies, provenance record |
| SA-13 | High | Allowance withdrawn, target changed and old capability still works due to stale session | Versioned decision containing `allowance_id`, target, campaign, subject and epoch; evaluate on command and new projections; atomic revoke/replace |
| SA-14 | High | A Player owns sub and uses a Campaign allowance to export GM-owned content | Subscription is not ownership or a transfer license; independent source/right permission and destination policy always enforced |
| SA-15 | High | Payment dispute / grant restoration unwittingly deletes or unlocks author-created data | Preserve authored raw data under source ownership; quarantine dependent projections and restricted derivatives; never delete on simple nonrenewal |
| SA-16 | High | Subscription appears active while invoice unpaid/plan changed/charge not acknowledged | Provider-confirmed state machine, correct grace/hold handling, plan and product mapping, revocation/recovery audit |
| SA-17 | High | Refund or cancellation retries create duplicate invoices or double AI usage charges | Provider idempotency, exactly-once internal ledger application, separate optional-AI metering and user budget caps |
| SA-18 | High | Subscription rule migration changes entitlement unexpectedly or breaks older snapshots | Version ruleset/decision, durable migration, replay and rollback tests, invalidation on version drift |
| SA-19 | Medium | Shared Campaign leaves no clear message on which content is unavailable | Visible "available only in Campaign X" status, accessible denial reasons, saved source references and export warnings |
| SA-20 | Medium | App Store/Play store use wrong checkout route, disclosures or cancellation endpoint | Storefront-specific adapter and compliance tests; no price publication until owner approvals and current legal policy checks |

**Evidence caveat:** These are attack hypotheses and design risks. A source port or passing fixture test is *not* a demonstrated exploit, deployed mitigation, billing integration, or security certification. The current evaluator's deliberate simplicity explains part of the gap; no assertion of a production breach is made.

## 3. Proposed billing and entitlement rule model

### 3A. Separate ledgers (PROPOSED, not automatically authorized)

1. **BillingAgreement** `billing_agreement_id,canonical_payer_subject_id,provider,storefront,country,product_id,plan_version,currency,amount_minor_units,period_start,period_end,auto_renew,provider_reference,verified_at,provider_revision,status,consent_receipt_id`. A provider receipt alone never assigns to an arbitrary subject.
2. **PaymentEvent** immutable provider notification and reconciliation receipt: `provider_event_id,signature_verification,provider_transaction_id,original_purchase_id,observed_at,provider_effective_at,event_type,raw_digest,normalization_id,ledger_revision`. Unique `provider_event_id` and unique provider purchase ownership.
3. **EntitlementGrant** `subject_id,grant_origin,capabilities,starts_at,entitled_until,revoked_at,ruleset_version,source_revision`. Paid subscriber entitlement follows provider-confirmed entitlement period. Distinguish a cancellation *instruction* from access loss.
4. **CampaignAllowanceSlot** unique `(campaign_id,player_subject_id,"GM-sponsored-premium")`, `slot_id,issuer_gm_subject_id,target_kind,target_release_id,target_version,dependency_closure_digest,state,grant_epoch,issued_at,revoked_at,eligibility_decision_ref`. Exactly one live grant configuration per slot; historical replacements remain ledger events, not a second simultaneous allowance.
5. **RestrictedDependencyEdge / provenance** `source_release,source_digest,allowed_campaign,allowed_character,grant_id,owner_rights,derivation_kind,downstream_subject`. Taint is monotone for campaign-private derivatives until a source owner authorizes an explicit independent transformation.
6. **AuthorizedOfflineLease** `subject_id,device_id,campaign_id,resource_set_digest,entitlement_epoch,permissions_epoch,issued_at,expires_at,max_offline_elapsed,signature,lease_key_id` and separate encrypted cache key binding. Cache is not canonical authority.
7. **OptionalAIBudgetLedger** separate opt-in token/payment budget by user/Campaign/provider/period; subscription and allowance do not imply unlimited generative calls or accidental paid provider execution.

### 3B. Subscription lifecycle model

`pending_purchase` -> `verified_active` (paid/trial policy) -> `cancel_scheduled` (still entitled until paid term) -> `expired`. Payment failure may enter `grace_entitled`, then `account_hold_denied`, then `recovered` or `expired`. `revoked_or_refunded` can terminate earlier according to verified provider event/terms. `paused` is explicitly mapped to no premium access unless current provider status and product policy say otherwise. `disputed` triggers provider reconciliation (not auto payment or grant). Unknown, pending, or unverifiable purchase must not mint premium. **Store-specific states are normalized but not invented.**

| Subscription/billing condition | Premium access | Renewal charge | GM can issue/keep effective allowance |
|---|---|---|---|
| Verified active, in paid interval | Yes | Per verified plan | Yes if current GM/Campaign eligibility |
| Cancel scheduled, paid interval unexpired | Yes | No future renewal unless resubscribed | Yes until entitlement expiry (proposed) |
| Verified trial entitlement | According to explicit trial SKU | As disclosed at conversion | **Owner decision**: allow grant during trial? Default deny issuance |
| Verified billing grace | Yes when provider grants grace | Provider manages retries | **Owner decision**: existing allowance reads continue, prohibit new grants |
| Account hold / paused non-entitled | No premium | Provider-specific | No new grants; existing premium privileges suspended |
| Expired | No premium | No charge without new consent | Suspended; provenance remains |
| Reversed/refunded/revoked | Deny affected grant promptly | Refund reconciled separately | Suspend affected grants (provider truth required) |
| Provider unavailable | No *new* premium or allowance authority | Never invent charge | Previously verified current leases may read safe cached material, never mint/transfer |

**Owner decision required** for trial grants, grace issuance, refund revocation effective time, and exceptional appeals; proposed conservative defaults are *not final commercial policy*.

### 3C. Allowance decision model

Allow only if **ALL** are true: (a) canonical Player subject and Campaign membership; (b) current issuer is authorized GM of same Campaign; (c) issuer's subscription is provider verified and effective under approved grace policy; (d) exactly one enforced slot for `(campaign,player)` and request uses valid idempotent issuance/authorized replacement; (e) allowed grantable target type and registered immutable release+version; (f) dependency closure computed on trusted owner graph, checked for rights, cycles, incompatible constraints and campaign license; (g) persistent transaction writes slot, dependency digest, audit, source references and entitlement revision; (h) evaluation rechecks current membership, GM authority, grant epoch and source rights on every protected use.

Effective usage: `subject_is_current_member && campaign_matches && slot_active && gm_still_eligible && source_release_active && entitlement_epoch_current && owner_rights_allow_action`. It gives **access only**, never ownership, canonical publication, free equipment/mechanics, transferable Character control, other-Campaign rights or generic subscription. A self-paid subscriber's global capabilities are a separate union, and do not remove the scoped lineage on GM-sponsored assets.

**Dependency handling:** a custom Setting gets its proven dependency closure as **one root allowance**, not separate grants per child. A selected Species, item set, ability tree or future owner-allowlisted root likewise consumes exactly one slot; a bundle of unrelated roots is not an implicit dependency. Linked Character references must retain the originating Campaign scope. GM revocation, player removal or Campaign closure suspends premium projections, but retains source IDs, audit, and permitted user drafts.

### 3D. Billing amount and store rules (NO PRICE SELECTED)

Amount = `currency_minor_units` of a validated `(storefront,territory,SKU,plan_version,term)`; never calculate an invoice from the client entitlement tier. Provider adjudicates taxes, refunds, proration and billing retry according to route. Proposed pure reconciliation steps: validate provider-signed event -> pull latest authoritative purchase -> bind purchase to canonical payer with anti-reassignment -> normalize lifecycle and effective interval -> atomically append deduplicated ledger and recompute grants -> invalidate session/cache/exports -> notify in accessible format. Every state change has exact source and timestamp; no user double-charge on retry. Purchaser and allowance recipient are separate subjects. The **GM's subscription is not a per-Player charge** and one allowance is not purchasable currency unless owner explicitly approves a separate commercial SKU (currently not approved).

### 3E. Offline security reality

Offline **protected view** may use a narrowly scoped cryptographically verified lease, bounded lifetime and encryption-at-rest plus device key/OS-keystore binding where supported; UI must identify stale state and block unsupported action. **Offline premium grant issuance, subscription validation, transfer, cross-Campaign export, owner publication, or canonical Session mutation is denied.** Offline clients cannot learn a remote revoke before contact; therefore instantaneous remote erasure of already-decrypted data is impossible. Minimize prefetch, limit lease duration, rotate keys on rejoin, and invalidate on all known local epoch changes. Screenshots and memory capture remain residual risks. Save user-authored recoverable drafts separately, but never silently export protected dependent pack bytes or grant privileged campaign use outside scope.

## 4. Acceptance criteria and release gates

- **P0** formal database uniqueness and concurrent grant race test; signed source trust, duplicate/refund webhook replay, GM role/subscription revocation, grant target and recursive dependency export quarantine; assert no premium via direct endpoint, search, AI, websocket, cache.
- **P0** truth-table state machine for paid-but-canceled, grace, hold, refund, two-device stale auth, three concurrent account/device identities, clock rollback and replay; exact timestamps and idempotency.
- **P1** Character/Species/Ability Tree/Setting/item set nested provenance tests across copy, derived objects, backup/import, authored draft and Campaign transfer; no loss of recoverable user-authored raw work.
- **P1** accessibility/screen-reader and cancellation/restore purchase flows; appropriate platform payment-disclosure test and store redirect/alternative-billing enrollment checks.
- **P1** signed, bounded offline leases on Android/Windows, encryption/key rotation and absence of protected bytes from logs; physically installed tests, not only mocked crypto.
- **P2** periodic reconciliation, unusual volume alerts, account-linkage disputes, chargeback handling, support-facing diagnostics with redacted provenance.
- **No-go:** no paid activation, entitlement billing claims, permanent offline protected access, allowance transfer or production security certification based only on these plans or fixtures.

## 5. Decision register (owner approval required BEFORE product policy finalization)

| Decision | Current status | Conservative proposal |
|---|---|---|
| Published monthly price/tier/SKUs | NOT APPROVED; $4.99 legacy target only | Do not enable charges |
| Whether allowance stays effective through paid-but-canceled term | Not explicitly selected | Yes until provider-confirmed expiry |
| Trial GM can issue allowance | Unspecified | No new issuance |
| Grace-state GM can issue new allowance | Unspecified | No new issuance; existing read until provider grace end |
| GM subscription lapses: revoke vs suspend | Grant depends on subscribed GM; exact UX not selected | Suspend access, preserve slot and provenance; recover only on verified restoration |
| Replacement/retargeting of used allowance | One active allowance fixed; replacement process unspecified | One atomic GM-authorized replacement; deny instant oscillation abuse and log history |
| User-owned dependent creations during lapse | Recoverable Character/access-only rule; export-right detail unspecified | Preserve source, quarantine restricted projections; permit raw-only export only after owner rights review |
| Maximum dependency closure and authorized root catalog | Not specified | Exact allowlist plus cycle/size bounds, no arbitrary root bundling |
| Sponsored months vs campaign allowance | Existing evaluator treats them as different sources; detailed semantics unselected | Maintain distinct grants; no cross-Campaign subscriber bleed |
| Optional AI billing in subscription | Not approved as inclusive or metered | Opt-in with separate hard budgets; no hidden charge |
| Offline maximum read lease duration | No approved time period | Choose only after measured installed revocation/security tests |
| Apple iOS/App Store distribution | Future conditional | Require storefront-specific compliance before launch |

## 6. Adversarial scenario corpus

See `ADVERSARIAL_SCENARIOS.json` (structured IDs, severity, preconditions, adversarial event, expected permitted/denied outcome and evidence type) and `SCENARIO_INDEX.md`. These are *proposed test fixtures*, not tests already executed against the running Multiversal app. An `expected` outcome is a specification obligation; it does not assert current implementation passes it.

**Scope guard:** this study does not change `operations/CURRENT.json`, GPR PCV-03F, MTLC-14, AXI-01, prices, live subscriptions or production permissions.