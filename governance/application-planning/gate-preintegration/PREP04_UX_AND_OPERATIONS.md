# GATE-PREP-04 — Nonproduction subscription UX and operator readiness

**Authority:** approved GATE-PREP-04 isolated preparation (2026-11-02), not a consumer-facing release. **NO owner-approved price, tax, merchant, purchase terms, refund/grace policy or retail store.** The UI model in tests/gate_prep is an in-memory state-only fixture and does not charge.

## Screen behavior and accessible flows

| Journey | Presentation and required proof | No silent inference |
| --- | --- | --- |
| New account | Verified email + chosen username, one subject across Windows/Android; fetch current rights before purchase | Display username is not payment owner |
| Pricing/disclosure | Show merchant, price, currency, interval, scope/limitations, auto-renew, trial/refund rules, tax, cancellation and contact in approved localized copy; affirmative opt-in | Historical $4.99 is not an active SKU |
| Checkout processing | Pending state, provider channel; customer/customer-id binding verified server-side | Checkout redirect never grants access |
| Active subscription | Status, exact paid-through date/time, source channel, eligible benefits and management path | Provider "active" alone isn't finite coverage |
| Cancel-at-period-end | Auto-renew off, retain legitimately verified paid-through, show ending date and provider-specific cancellation management | Do not revoke early on cancellation |
| Failed renewal | Status/retry notice and preserved still-valid prior period; owner-approved grace pending | No invented extra grace |
| Sponsored Month | Named beneficiary account-scoped finite source and correct redemption; separate from Campaign Allowance | No sharing subscriber tier with GM |
| Campaign Allowance | Campaign, selected root/dependencies, issuing GM and constrained actions; retained character view without reusable package | One slot does not unlock library |
| Device/offline | Show last verified scope, finite end, failed recheck, locked account switch and local draft preservation | Offline key ≠ online login |
| Ownership lapse | Preserve safe authored exports and drafts while protected runtime locked | No deletion of personal text |
| Refund/dispute | Show pending status + support; do not invent permanent revocation policy | Commercial decision outstanding |

Accessibility acceptance: keyboard traversal for all major routes, clear focus, descriptive error text (not color-only), reduced motion, actionable recovery and screen-reader labels. A mock screen does not establish installed Windows/Android accessibility.

## Operational exercises, no real customer records

1. **Reconciliation dry run:** import synthetic event IDs, provider/environment/customer mapping and current snapshot; detect duplicate/conflicting/out-of-order deliveries; compare trusted invoice/paid-through to derived subject grants; produce immutable incident timeline and outbox retry receipt.
2. **Charge dispute/refund tabletop:** confirm source revision and owner policy; place unresolved amount/access policy on hold; preserve authored materials. An operations agent cannot improvise a refund rule from a webhook hint.
3. **Account mismatch:** payment proof for subject A received under subject B; quarantine the attempt, do not bind receipt or refund blindly; log audit without secrets; security escalation.
4. **GM allowance lapse:** show member's restricted character-view projection, no unconditional root swap, preserve data; pending decision determines future runtime after GM eligibility changes.
5. **Provider outage:** new subscriptions not activated by failed fetch, existing finite paid-through remains independently considered, no client-side receipt acceptance.
6. **Key/cache incident:** known denial monotonic, isolate credential, block scope renewal; preserve encrypted user drafts; do not include content keys or plaintext in support diagnostics.
7. **Recovery:** user obtains fresh account authentication and device binding; old offline lease and copied cache cannot become bearer rights on replacement device.
8. **Storefront rejection:** route to actual charging rail (direct/Play/IAP/US alternative); do not assert all countries allow external checkout.

## Audit artifact contract

Every tabletop evidence row should identify: test ID, fake subject, fake transaction/event id, provider env, recorded source version, operator action, privacy-redacted diagnostic, expected result, actual result, UTC timestamp, reviewer and unresolved owner policy. Never put customer email, card number, private keys, signed purchase tokens or actual user data in fixtures.

## Open decision packets (owner to resolve independently)

- Retail offer price and inclusive vs exclusive taxes; geographic sales scope, merchant/tax responsibility and all-in costs.
- Trial/free tier, renewal grace, delinquency, refunds and disputes, cancellation effective moment, complaint handling.
- Sponsored Month eligibility, recipient acceptance, gifting/GM access, inability to transfer to shared mailbox account.
- Ongoing subscribed-GM obligation and one-slot replacement after issuer lapse; restricted-character continuity.
- Offline license max time (bounded by verified paid-through), key rotation/clock/recovery; privacy/retention and AI optional usage.
- Google Play opt-in/reporting and Apple future storefront, current terms at actual launch date.

## Integration handoff

PREP-04 ends with state-only UI code and these scenarios. GATE-09 requires separate owner-selected backend authority and verified PCV-03F account/Campaign/Session boundary; GATE-10 provider test credentials require independent approval; GATE-11 installed journeys; GATE-12 independent security; GATE-13 real support/restore; GATE-14 owner release. No one should connect this mock UI to a live provider without those gates.
