# MTLC-05 — Original Consent/Veils source-recovery receipt

**Classification:** genuine original-canon provenance gap, not a product compilation or CI failure.  
**Operational authority:** `operations/CURRENT.json`; this report is evidence only and cannot grant permissions, redefine canon, or select successor work.  
**Current implementing artifact:** Multiversal-app draft PR #851 at exact head `ff7f45c998f1a34a53a7704caab7269fb7cbab8d`, validated by GitHub run `38749897894` (focused feedback, Linux, Windows and cross-platform comparison green). **Draft/unmerged** by deliberate source gate.

## Canon that requires proof

The owner corrected MTLC-01 to recognize that Multiversal already had original tabletop *Consent and Veils* material, likely in older original PDF sources. That fact is an original-source **recovery instruction**, not permission to write remembered or third-party equivalent rules. The approved MTLC-05 exit criterion requires both source traceability and product-visible Consent/Veils; newly-authored participant table agreements do not satisfy it.

## Recovery sources examined

1. **Current governed sources**: MTLC-01 Section 5A source gap and MTLC-01 70-item traceability matrix; neither contains original passage or an extractable original page identity. The AIOC current full Project Bible and reference Bibles contain no original tabletop Consent/Veils wording.
2. **ChatGPT Project Sources (October 15, 2026)**: `PROJECT_BIBLE_OPS3_REFERENCE.md`, `FEATURE_BIBLE.md`, `SCREEN_DESIGN_BIBLE.md`, `UI_DESIGN_BIBLE.md`, sanitized `DB-004` reference ZIP, and 8E-008G source-provenance audit ZIP. Text searches distinguish unrelated spell/setting uses of “Veil” and account/privacy consent. No tabletop safety passage found in those available readable items.
3. **Connected personal Library/Project search**: topical and original-package name queries surfaced current reference artifacts and feature manifests, not original Consent/Veils rules text.
4. **Preserved Google Drive `98_CURATED_MULTIVERSAL_ARCHIVE`**: directly inspected its governed-source / extraction / legacy-conversation inventories and downloaded `PROJECT_CONVERSATIONS_01.zip` through `_06.zip`, `GENRE_EXPANSION_CONVERSATION.zip`, and `NOW_THIS_GOVERNED_SOURCE_EXACT.zip`. Searched their readable MHT entries (30 project-conversation captures, one genre capture and 24 governed-source captures) for `Consent and Veils`, `Veils`, `Lines and Veils`, `Session Zero` and `player consent`. Found later Session Zero/planning mentions, but **no exact original tabletop rules passage**. The result is bounded to the readable contents inspected; nested/missing original PDFs are not claimed absent from the entire archive.
5. **Google Drive filename search** for `MV_Master`, `DB-004`, `Project Bible`, and Consent/Veils plus folder inventory did not identify an accessible original tabletop Consent/Veils source PDF. Several matches were unrelated novels, third-party tabletop guides, and later project policy material; none can be promoted to original canon.
6. **Current NCG TGCP-16** makes the same distinction: third-party Script Change and Consent in Gaming are comparisons and cannot be treated as recovered Multiversal canon.

## Product implementation already verified, but not original canon

PR #851 includes an A3/Group/A5-gated Session Zero workspace, revisioned table-authored expectations, self-authored privacy-separated boundaries with explicit organizer-sharing opt-in, agreement acknowledgment/withdrawal, session-scoped recording/streaming opt-in preflight, persisted HTTP/SQLite acceptance, and hash-only idempotency receipts. Its `consentVeilsProvenance` is explicitly `unresolved-original-source`. Validation does **not** certify original wording, device permission enforcement, production recording/streaming integration, or production privacy/regulatory posture.

## First unresolved dependency and owner action

**External original source needed:** original PDF/source passage for Multiversal's tabletop Consent and Veils mechanism (or the source bundle containing it) with file and page/section context. Only the owner can supply/link that preserved original if inaccessible here, or explicitly authorize a different canon design. Until then:

- Keep PR #851 **draft and unmerged**, with successful exact-head candidate preserved.
- Keep MTLC-05 `in_progress`, with source recovery as an **owner-only dependency**, not `completed_verified`.
- Do not claim MTLC-06 authorization, invent new safety-tool text or substitute unrelated/third-party consent mechanisms.
- When the source is provided, quote and trace original terminology, reconcile additive UI to the verified source, revalidate any changed candidate head, then follow the ordinary OPS5 publication/closeout sequence.