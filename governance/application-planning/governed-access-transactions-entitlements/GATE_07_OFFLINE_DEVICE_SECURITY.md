# GATE-07 — Offline signed authorization, device key custody and replay safety

**Scope:** source-only threat model and implementation specification for Multiversal Windows+Android clients; no actual key issue, cryptographic verification, native install, external payment or signed payload has been executed. **Authority:** Owner-approved UADS Oct 27 verified-then-offline continuity, subscriber security extension, GATE-02/GATE-05/GATE-06 published designs. Preserve user-owned data and known denial independently of current paid runtime.

## Approved offline UX and non-negotiable constraints

A signed-in, unchanged account on an enrolled installation may continue using **previously verified protected cached content/actions while offline** until the finite verified entitlement or narrower authorization expires. Ordinary app restart may retain an intentionally remembered account. Token refresh expiry does **not** itself invalidate an otherwise valid distinct offline authorization. A different device/installation must enroll online independently; using another username, subscriber download, copied ciphertext or same recovery email conveys no rights.

An online first verification checks subject, account-device credential binding, verified subscription (or narrow Campaign Allowance, Sponsored Month, or retained character projection), pack/resource action scope, provenance, time and policy epoch. A separate server-signed *offline lease* only records those established facts. It is not an access token and cannot call online APIs, mint checkout, issue allowance, generate rights, enroll a device, or extend itself.

Lease has a **finite, trusted** `validUntil <= last verified paid-through` or for allowance runtime the applicable GM qualifying paid-through and any narrower grant/membership/resource cap. Undefined billing end means no offline lease, not an unlimited lifetime. No extra fixed maximum offline check-in TTL is approved; a shorter policy requires explicit owner decision. Server-required collaborative commands and current remote data remain unavailable offline.

## Proposed signed envelope (not app code)

```ts
interface OfflineAuthorizationEnvelope {
 schema: 1; issuer: 'multiversal-entitlement-server'; audience: 'offline-content';
 leaseId: string; subjectId: string; installationId: string;
 devicePublicKeyThumbprint: string; loginSessionFamilyId: string;
 securityEpoch: number; policyVersion: string; grantVersion: number;
 entitlementSource: 'subscription'|'sponsored-month'|'campaign-premium-grant'|'retained-character-view';
 contentRootRef: string; manifestDigest: string; resourceVersion: string;
 campaignId?: string; beneficiarySubjectId?: string;
 selectedActions: string[]; contentKeyEnvelopeRefs: string[];
 issuedAtTrusted: number; notBeforeTrusted: number; expiresAtTrusted: number;
 confirmedPaidThroughTrusted?: number; // no undefined limit on subscribed runtime
}
interface ProtectedContentCacheEnvelope {
 contentDigest: string; subjectId: string; installationId: string;
 deviceKeyRef: string; policyVersion: string; leaseId: string;
 sourceRootRef: string; campaignId?: string;
 purpose: 'runtime'|'restricted-character-view'|'independent-authored-draft';
 encryptionAlgorithm: 'authenticated-encryption-vetted-library';
}
```

Cryptographic signatures must cover canonical bytes, all policy/scope metadata, issuer/audience and version; maintain public key verification and rotation with legitimate backward compatibility only for still-valid, non-revoked leases. The client does not generate trusted server signatures. Do not reuse an API bearer token, a content manifest signature or a mutable Boolean as a lease. Explicit login-session-family continuity allows rotating network access tokens without invalidating verified offline rights.

## Key hierarchy and per-platform boundaries

- Server signing private keys and provider secrets stay server-side, inaccessible from app bundles, native bridges and exports. Publish only issuer public verification keys with tracked key IDs and verification policy.
- Use a **distinct account-device secret/key** per installation and subject; a device ID string is a routing label, not possession proof. Server registration proves possession of its enrolled key. Protect each content decryption key via an authenticated account/device/scope-bound envelope; authenticated metadata covers content hash, subject, device, manifest and policy epoch. Separate restricted-character projection keys from Campaign runtime and general subscriber source keys.
- Android: use maintained Android Keystore APIs and hardware-backed key protection *where actually available*. Hardware attestation, if relied on, requires full certificate-chain, root, security level and revocation verification; optional hardware support and OS diversity prevent unconditional hardware-backed claims. Software-only Keystore still needs a measured threat model.
- Windows: use appropriate per-user DPAPI/CNG protection or verified native solution, not `CRYPTPROTECT_LOCAL_MACHINE` as cross-account isolation. DPAPI's normal protection is for a Windows OS user/profile and can have roaming/recovery exceptions; **two Multiversal accounts on one Windows login remain separate app secrets and locks by policy**, not guaranteed by DPAPI alone. Test profile reset/roaming and native secret-store restore cases.
- Browser/Electron Web Crypto `CryptoKey.extractable=false` blocks API export/wrapping, but is **not** proof of hardware isolation, secure execution in a compromised process or OS-user separation. Do not claim that encrypted files or nonexportable keys defeat an app-instrumenting device owner.
- No subscriber plaintext/content keys, tokens, signature secrets or account passwords in crash logs, screenshots, diagnostics, exported repository reports, notifications, shared files or backups. Back up account-owned data **without** copying an active offline license/device credential; restore it through fresh online enrollment.

## Account switching, known denial and trusted time

1. **Ordinary restart:** intentionally remembered current account may continue with a still-valid signed lease, intact local session family and trusted time anchor.
2. **Switch/sign-out:** persist a durable locked state and advance an account generation fence, cancel or fence late callbacks, remove decrypted runtime handles and lock source keys. Switching away **and back** requires fresh online authentication/authorization. A device biometric or remembered username alone is not a new account login.
3. **Known denial:** persist server-verified revocation, suspension, reduced scope, grant version and monotonic epoch **before** allowing any fallback. Later timeouts/airplane mode/replayed cache must not reverse it. Account or grant security events cannot be downgraded by older signed scopes.
4. **Transient network failure:** absence of response is not denial; an existing finite verified lease may continue inside exact scope until its own expiry and cannot gain new content or extend time.
5. **Trusted time:** sign server-origin issued, not-before and finite end; track server time anchor plus monotonic elapsed-time and platform uncertainty. Detected backward wall-clock rollback, device snapshot restore or loss of trustworthy temporal continuity locks protected runtime until online recheck, preserving drafts. A hostile device owner can still forge local clocks; no absolute guarantee while offline.
6. **Reconnect:** refresh authoritative subject/device/entitlement/role/content versions first; reconcile ambiguous prior idempotency commands before retries; validate every queued edit's source and destination, Campaign membership and restriction, and server acceptance. Preserve rejected/unsynced drafts with conflict state; neither auto-drop nor auto-promote them to shared truth.
7. **Bounded residual risk:** remote refund, revocation, GM lapse or suspension occurring after disconnect is unknowable until the client reconnects or lease expires. Already viewed plaintext can be captured. Security is best effort across supported clients, not unbreakable DRM.

## Request and cache access matrix

| Operation | Connected session | Unchanged offline lease | Account switched/signed-out | Retained character view |
|---|---|---|---|---|
| Protected runtime of exact authorized pack | Current server decision required | Prior authorized scope/time only | Deny | Not granted |
| New premium download, new root, GM issuance, server command | Auth and current entitlement required | Never | Deny | Never |
| Browse full premium source library | Scoped personal subscriber rights only | Only prelicensed cached sources, if leased | Deny | Not granted |
| View own restricted Campaign character | Owner, privacy filtered | Separately scoped view-only key and continuity | Deny until reauth | Allowed narrow projection |
| Transfer restricted character/item to another context | Deny absent separate owner-approved operation | Deny, pending edits remain local only | Deny | Deny |
| Sync conflict/queued edit | Server revalidates before commit | Local draft provisional | Isolate pending drafts | View-only projections do not confer sync acceptance |

All other signed manifest, source pack rights, GM-hidden visibility and user ownership controls still apply. No universal offline plan flag or installer-bundled decryption key.

## Adversarial acceptance plan (not executed)

Use **real Windows and Android installed builds**, two subjects sharing recovery mailbox (Raven1/Raven2), cross-device same subject (Raven1 Windows+Android), independent Zak1, separate enrolled device keys and server/clock/DB fixtures.

- Valid offline restart and online access-token expiry preserve prior finite rights. Device loss/reinstall requires re-enrollment.
- Account switch to Raven2 and back does not resurrect Raven1 offline; stolen copied cache / license / device string or subscriber package cannot authorize Raven2.
- Known server revocation persists after loss of network; mere transport outage retains still-valid scope. Test queued server result arriving after account generation changes.
- Wrong issuer, audience, signature, key ID, scope, Campaign, root hash, device thumbprint, subject, past end and invalid future period fail closed; no local renewal.
- Dependency package, image thumbnail, search index, notification and diagnostics cannot leak protected assets, keys or GM-hidden material. Export independent data without protected mixed material.
- Spoof/rollback local clock and backup snapshot restoration; detect where possible and disclose residual impossibility on compromised device.
- Simultaneous offline grant and independent personal subscription; one revocation must not delete the other. GM loss may be recommended lifecycle but pending owner resolution.
- Reconnect accepts idempotent queued work only after source/target rights and current membership/allowance, rejects revoked/out-of-scope edits while preserving authored drafts.

The [GATE-07 fixtures](GATE_07_OFFLINE_FIXTURES.json) with `scripts/gate07_reference_oracle.mjs` cover **68 source-only decision cases plus 12 time boundary cases**. This oracle treats signature/key/time validity as pre-verified inputs; it **does not verify a real digital signature, detect actual time tampering, or test OS keystores**.

## Evidence and limits (verified research vs source-only proposal)
- [Android hardware key attestation](https://developer.android.com/privacy-and-security/security-key-attestation): Google documentation on attestation chain/root/security-level/revocation; Android capabilities vary.
- [Windows CryptProtectData DPAPI](https://learn.microsoft.com/en-us/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata): normal OS user credential protection; machine scope permits other users on that computer and roaming cases exist.
- [MDN CryptoKey extractable](https://developer.mozilla.org/en-US/docs/Web/API/CryptoKey/extractable): only export/wrap API semantics.
- [OWASP MASVS Resilience](https://mas.owasp.org/MASVS/11-MASVS-RESILIENCE/): anti-tamper and obfuscation are defense in depth, not a substitute for server authorization.
- Owner-approved NCG UADS Account/Device/Entitlement and Subscriber Content Security Oct 27; published OPS5 GATE-02 and GATE-06 policy. This document makes no provider, OS security certification or runtime implementation claim.
