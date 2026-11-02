# XTRA-08 — Subscription, Allowance, Protected-Content and Replay Threat Preflight

**Status:** source-linked 39-case synthetic/reference-only specification; not a deployed security control, production billing adapter or guarantee against leakage.  
**Companion:** [XTRA-08 Allowance Security Threat Matrix](XTRA-08_ALLOWANCE_SECURITY_THREAT_MATRIX_v1.0.0.json).  
**Executable reference:** `tests/control_plane/xtra08_reference_oracle.py`.

## Owner-approved product requirement, unaltered

Exactly **one allowance per Campaign per Player-user**, issued by a **GM with a verified active subscription**, may unlock one eligible custom Setting with dependencies, Species, item set, Ability tree or other owner-approved class **for that Campaign only**. A sponsored Character and restricted dependencies must not escape to another Campaign, account or public export. Independent user-authored raw work may be recoverable when protected projections are denied, but no access grant is synthesized by this research.

Separate current A3 Campaign role/member state, provider purchase identity/receipt truth, PostgreSQL issuance ledger, registered source/root closure, ARI rights, and each protected action-specific read/export pathway. A client boolean, UI badge or possession of encrypted bytes cannot substitute for the current server-derived trust boundary.

## Existing source evidence and its limits

| Source | What it demonstrates | What it does **not** demonstrate |
|---|---|---|
| **SA-BILL-05** | Disposable PostgreSQL 16 SERIALIZABLE fixture with uniqueness, idempotency, hostile connections, membership/GM subscription denial | Production PostgreSQL migration, live signed provider receipts or across-service atomic trust |
| **SA-BILL-08** | Historical actual app source functions: generic hidden count, generic public command payload, replay before fresh membership; safe A9 projections | A live reachable endpoint exploit or complete upstream service mitigation |
| **SA-BILL-09** | Test-first RED and proposed temporary-source repairs for replay/visibility; 15 test cases | Deployed patch, signed cryptographic command ledger or approved schema migration |
| **SA-BILL-10** | Direct generic patch conflicts with inherited P9-06 replay and hidden-count contracts; compatible *outer boundary* can deny untrusted external responses | Real deployed external gateway or replacement of production owner-specific service |
| **Threat Model** | Product requirements, provider-lifecycle considerations and priority attack matrix | Final price, trial/grace/retarget/offline lease policy or active billing/payment provider |

**Do not apply the direct SA-BILL-09 generic handler patch as-is.** The source research shows that historical validators might return green while TypeScript semantics differ. Implementing real protection requires actual A3/session/provider authoritative input, client and internal call-site migration, safe outer projections, and real end-to-end proof in PCV-03F or later owner-selected implementation.

## Reference test matrix (not executed against product)

| Group | Cases | Covered threat boundaries |
|---|---:|---|
| Issuance | 10 | GM verification, active subscription, Player membership, current epoch, registered root rights and duplicate Campaign/Player slot |
| Content use | 12 | Cross-Campaign containment, tainted Character transfers, download/export/import/share, search/AI/WSS/cache, dependency revision |
| Replay / projection | 6 | Same-actor command binding, stored original receipt, post-revocation authorization and safe external projections |
| Offline | 7 | Signed device-bound bounded read-only lease, expiry, revocation epoch, encrypted vault, prohibition on offline protected mutation |
| Owner choices | 4 | Trial/grace, GM succession, final subscription SKU and offline lease policy remain unapproved |
| **Total** | **39** | Synthetic-only assertions; all actual application results remain NOT_TESTED |

The oracle allows **only** a deliberately complete synthetic positive vector per issuance/use/replay/offline group; every missing trusted predicate is denied. Unknown domains are denied. Its positive status is explicitly `ALLOW_SYNTHETIC_ONLY`, *not* a signed real permission. A green oracle verifies the intended reference table, not the implementation.

## Scenarios and source linkage

| ID | Threat | Expected reference decision |
|---|---|---|
| XTRA08-I01 | One valid GM-approved grant | `ALLOW_SYNTHETIC_ONLY` |
| XTRA08-I02 | GM no longer active | `DENY` |
| XTRA08-I03 | GM subscription expired | `DENY` |
| XTRA08-I04 | Player removed from Campaign | `DENY` |
| XTRA08-I05 | Client spoofed subscription truth | `DENY` |
| XTRA08-I06 | Concurrent duplicate Campaign-Player slot | `DENY` |
| XTRA08-I07 | Current trusted owner revision missing | `DENY` |
| XTRA08-I08 | Unauthorized root class or incomplete rights | `DENY` |
| XTRA08-I09 | Unknown registered content-rights revision | `DENY` |
| XTRA08-I10 | Unverified actor subject | `DENY` |
| XTRA08-U01 | Authorized current Campaign read | `ALLOW_SYNTHETIC_ONLY` |
| XTRA08-U02 | Cross-Campaign protected object | `DENY` |
| XTRA08-U03 | Transfer protected Character outside Campaign | `DENY` |
| XTRA08-U04 | Export sponsored Species/item/tree | `DENY` |
| XTRA08-U05 | Search/count metadata after GM role revoked | `DENY` |
| XTRA08-U06 | AI prompt/retrieval of denied dependency | `DENY` |
| XTRA08-U07 | WSS after Player membership removed | `DENY` |
| XTRA08-U08 | CDN/download with stale rights | `DENY` |
| XTRA08-U09 | Import restricted derivative to another Campaign | `DENY` |
| XTRA08-U10 | Campaign protected cache after revocation | `DENY` |
| XTRA08-U11 | Nested dependency/version mismatch | `DENY` |
| XTRA08-U12 | Public sharing despite separate personal paid subscription | `DENY` |
| XTRA08-R01 | Trusted same-actor bound replay through safe projection | `ALLOW_SYNTHETIC_ONLY` |
| XTRA08-R02 | Revoked membership before replay | `DENY` |
| XTRA08-R03 | Substituted actor claims prior receipt | `DENY` |
| XTRA08-R04 | Changed command payload with same command ID | `DENY` |
| XTRA08-R05 | Client fabricated cached receipt | `DENY` |
| XTRA08-R06 | Unsafe generic public payload/count projection | `DENY` |
| XTRA08-O01 | Signed bounded read-only lease | `ALLOW_SYNTHETIC_ONLY` |
| XTRA08-O02 | Forged lease signature | `DENY` |
| XTRA08-O03 | License copied to another installation | `DENY` |
| XTRA08-O04 | Lease expired or clock manipulation detected | `DENY` |
| XTRA08-O05 | Epoch stale after revocation | `DENY` |
| XTRA08-O06 | Unencrypted private protected vault | `DENY` |
| XTRA08-O07 | Protected offline allowance mutation | `DENY` |
| XTRA08-P01 | Unapproved grace/trial grant policy | `OWNER_DECISION_REQUIRED` |
| XTRA08-P02 | Unapproved GM succession/retarget after allowance use | `OWNER_DECISION_REQUIRED` |
| XTRA08-P03 | Final price/SKU/merchant/store selection not approved | `OWNER_DECISION_REQUIRED` |
| XTRA08-P04 | Unapproved offline lease duration or automatic billing | `OWNER_DECISION_REQUIRED` |

## Essential real-product acceptance gates

1. **Transactional atomicity:** one current Campaign/Player allowance row and original command receipt/event, idempotent duplicate handling, 40+ real concurrent PostgreSQL connections, safe conflict rollback, no guessed cross-database transaction.
2. **Billing authenticity:** signed purchase-to-account binding, replay-safe provider updates, verified GM subscription/role revision and cancellation/refund/hold/grace policy selected by owner. No current production SKU or charge is authorized.
3. **Source provenance:** recursive dependency and Character taint across nested Settings/Species/items/Ability trees, exact versions, revisions, cycles and nontransferable Campaign derivatives; preserve independently authored raw notes.
4. **Every exposure surface:** REST/action, Rules/Lore direct/search/count/vector, AI prompts and retrieval, WSS, CDN, export/import/backup, diagnostics, caches and errors. Test bytes *and metadata* after grant/revocation, not just the frontend.
5. **Replay and hidden information:** server-bound actor/session/command digest/receipt, current authorization before duplicate replay, minimal A9-safe external projections; do not silently change inherited generic TypeScript contracts without producer/consumer migrations.
6. **Offline and native protections:** install Windows and Android clients, signed encrypted device-bound lease, monotonic revocation/expiry, no rights bypass on clock rollback or copied vault; real tests on two independent devices.
7. **Owner policy:** finalize trial/grace, GM succession/retarget, refund, provider transitions, offline lease term and SKU/pricing through separately authorized decisions. Negative-option/payment/store rules need current legal/platform verification before commerce.

## Interface with OPS5 and follow-on XTRA work

- **XTRA-08** owns this source-linked risk list and synthetic oracle only. It cannot change PCV-03F implementation or claim that the vulnerabilities are fixed.
- **PCV-03F** owns the current live service/account/Campaign gate; downstream PCV-04..10 remain blocked by their own predecessors, not activated here.
- **XTRA-07** provides role and tester guidance for eventual permission-safe real-world checks; no hidden notes or secrets in reports.
- **XTRA-02** remains externally blocked on the November 8 Render certification PostgreSQL expiration and unverified real backup/restore.
- No subscription price, payment collection, trial policy or commercial release has been approved by this document.

No production secrets, personal data, billing credentials, or protected game assets are included. No live read/write, payment event, Native keychain or real offline attack was exercised.
