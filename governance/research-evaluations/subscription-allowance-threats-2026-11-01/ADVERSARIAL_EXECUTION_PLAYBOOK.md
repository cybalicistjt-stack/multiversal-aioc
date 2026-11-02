# SA-BILL-01 — Adversarial Execution Playbook
**Status:** staged test plan. **No actual paid transactions, API abuse, deployed service probes or installed-device evidence have been executed.** Use disposable provider sandbox identities, a fully isolated test backend, synthetic registered content and no real protected/third-party assets.

## Harness data set

Create **GM-A** (verified subscribed), **GM-B** (expired), **PLAYER-1** (free), **PLAYER-2** (free), **PLAYER-3** (subscribed), **ATTACKER** (not a Campaign member); **CAMPAIGN-X**, **CAMPAIGN-Y**; **DEV-WIN-1**, **DEV-ANDROID-1**, **DEV-ANDROID-2** bound to separate installation/device IDs. Give GM-A GM role only in X; GM-B GM in Y. Use one registered custom Setting S with dependencies Species-D, Itemset-D, AbilityTree-D, and an unrelated premium root U. Create one Character linked to S, one unrelated Character, public and GM-only fields, and an authorization-scoped query/search/AI index. Test with valid and revoked A3 sessions, controlled network cutoff, replayable provider sandbox events and actual native encrypted-store artifacts.

### Chain P0-1: One-slot double issuance / TOCTOU
**Fixtures:** one untouched `(X,PLAYER-1,gm-sponsored-premium)` slot; a subscribed GM-A and two different target roots.
**Actions:** send 100 grant mutations concurrently from separate authenticated devices, 50 for S and 50 for U, with unique request IDs; repeat the winning ID 20 times after timeouts; run the same test while the GM's subscription or Campaign role is revoked midflight.
**Oracle:** exactly one live row at the unique slot key, one canonical target and dependency closure; losing requests return conflict (or same cached result for identical idempotency); no extra subscription, charge, or object grant. Either authority epoch change rejects committing new grants. Database transaction/isolation receipt required. The test passes **only** if both database uniqueness and API authorization are demonstrated, not if a frontend hides the grant button.

### Chain P0-2: Dependency laundering across Campaign/Character/exports
**Fixtures:** PLAYER-1 granted S in X, PLAYER-2 in X without grant; S -> Species-D -> Itemset-D -> AbilityTree-D; Character CX references all.
**Actions:** try direct object export, whole Setting export, species library import, local Character duplication, new Campaign Y import, copied save file, deep link, printable sheet, REST list/detail, batch export, cached search ID, GM sharing link, and sub-account subscription upgrade for PLAYER-1.
**Oracle:** never output protected pack bytes or authorized-use capability outside X; no transfer of restricted Character or dependent objects. Return safe redacted user-owned metadata/drafts where independently authorized; original owner/campaign/source provenance remains attached. Paying for an unrelated personal tier does not erase dependencies. Independently inspect serialized bytes, screenshots, search counts and log archives.

### Chain P0-3: Provider webhook and cancel/refund state forgery
**Fixtures:** one sandbox active subscription with `entitled_until=T`, provider confirmed purchase token and stable canonical payer.
**Actions:** replay purchase and renewal events; deliver refund before the older renewal; try invalid signature, wrong application package, swapped customer, duplicated checkout, voluntary cancellation before T, grace, account hold, expired period, then successful recovery; simulate provider GET timeouts.
**Oracle:** verified provider truth and correct entitled intervals win. Cancel auto-renew before T does not prematurely revoke a paid interval. Grace/hold behavior follows actual provider; no premium on unknown or unverifiable source. No duplicate bill or grant and no charge created by retry. Preserve immutable event/consent/transaction refs. Owner decisions on *GM allowance issuance during trial or grace* remain explicitly pending.

### Chain P0-4: Offline copy + stale keys + clock rollback
**Fixtures:** authenticated Player on Win and Android; bounded per-device signed lease for X; encrypted protected S on both, GM revoke while Android disconnected.
**Actions:** disconnect, copy cache to second Android, change device clock and timezone, restore old signed lease, replace local database, sign out and sign in as a second subject, reconnect after GM revoke, attempt offline authorized mutation, dump logs/backups.
**Oracle:** no cross-device/user decryption; no unbounded lease extension or offline grant/transfer; online reconnect fences old epoch and cache/search/AI. A truly disconnected previously authorized reader may retain access until its lease ends; this is a quantified residual risk, not a claim of immediate remote erasure. Capture installed key-store/SQLite/network trace; tests on Node mocks are insufficient.

### Chain P0-5: Search, WebSocket, AI and side-channel leaks
**Fixtures:** deny PLAYER-2 S, allow PLAYER-1 only in X; GM hidden sections attached to S; connected A9/A5 realtime and rules/lore search context.
**Actions:** enumerate exact IDs and aliases, facet counts, name completion, vector/hybrid search, reverse links, cached thumbnails, event subscriptions, notifications, AI summary retrieval, export and diagnostics; revoke PLAYER-1 while a response is in flight.
**Oracle:** filtering before ranking/search/index projection and every event; count and embeddings leak nothing, including hidden topology. Revoke removes newly unauthorized cached facets and AI context. Source authorization must win over model-context convenience. Use explicit negative snapshots of all returned payloads and raw bytes.

### Chain P1-6: GM leaves, re-subscribes, Player leaves
**Fixtures:** one effective allowance with issuer GM-A, recipient PLAYER-1.
**Actions:** revoke GM role, expire GM subscription, replace GM, end Campaign, remove Player, restore subscriber entitlement and reenter Campaign with new epoch.
**Oracle:** no permission merely because historical grant exists. Keep persistent slot and lineage but suspend premium use; do not silently reassign GM sponsorship or restore without source-owner policy. Owner must select whether new GM may take over the slot or whether a new GM grant is required.

### Chain P1-7: Legitimate entitlement + user recovery
**Fixtures:** Player-authored Character with independently created biography, and premium-dependent visual/mechanics references from S.
**Actions:** expire GM entitlement, enter denied state, request account data export and own drafted content, renew paid issuer, authorize X again.
**Oracle:** own raw drafts/bio remain recoverable when separate rights allow; restricted render/data/export remain quarantined, not deleted or falsely licensed. On legitimate recovery, re-evaluate current registered releases and versions, never replay obsolete abilities/Items automatically.

### Chain P1-8: Accessibility and consumer-billing compliance
**Fixtures:** Google Play Android sandbox and later iOS (only if shipped); Windows merchant subscription prototype; canceled and account-hold conditions.
**Actions:** keyboard, touch and screen-reader walkthrough of price/period/renewal terms, trial-to-paid, cancellation and restore, correct store management links, external checkout eligibility, consent and error screens; use three regional storefront profiles including US and another country.
**Oracle:** accessible material disclosures before confirmation, no double subscription or forced retention friction, cancellation halts future renewals per provider, and no storefront-specific billing restriction is bypassed. Actual UI and provider review evidence required.

## Test coverage matrix and evidence

| Layer | Minimum proof | What it does not prove |
|---|---|---|
| Reference state model | Deterministic subscription transitions, one-slot invariant, denial predicates and all 60 scenario identifiers | Actual database race resistance or money movement |
| Source-owner transactional integration | DB unique index, simultaneous grants, source GM subscription revocation, query permission fencing, idempotency | Real store signatures or installed encryption |
| Provider sandbox + hostile API | Real provider JWS/HMAC signatures and reconciliation, forged client/webhook rejections, cancellation/grace/hold/refund | Real paid launch permission |
| Browser/renderer/search/AI negative integration | Actual response bytes and caches before/after revocation | OS key-store/hardware backed isolation |
| Native Windows + Android two-device | Isolated installs with A3 same subject and separate device IDs, offline key binding, backup/clock rollback and cross-device recovery | Instant remote revocation when completely disconnected |
| Independent rights/content review | Exact registered release, source/asset license, dependency closure and reviewer proof | Authorization to sell or release |

**Exit criteria:** all Critical scenarios and P0 chains independently green with exact-head provenance, zero unapproved cross-Campaign transfers, zero duplicate effective allowance slots, no client-origin subscription minting, provider-correct entitlement terms, no hidden data exfiltration, and explicit bounded offline exposure measurement. Any external owner service or actual native device unavailable is a **blocker**, not a green fixture.

**Test order:** reference/negative fixtures -> transactional concurrency -> hostile API/provider sandbox -> index/export/AI leakage -> installed-device/offline -> independent owner/rights/UX review. Preserve GPR PCV-03F and MTLC-14 selectors; these tests cannot overtake their authorized work without a new selected implementation scope.
