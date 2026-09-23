# BIP — Beta Installation Packaging

**Status:** in progress  
**Lane:** gpr  
**Owner selection:** 2026-09-23

BIP is the owner-canonicalized post-SMB packaging program for turning the `RELEASE_CANDIDATE_READY` Multiversal beta into tester-installable artifacts without authorizing public release or app-store publication.

## BIP-01 — Beta Installation Packaging — Windows + Android

Package the real `apps/client-ui` application through the existing Tauri shell.

Required artifacts:

- Windows x64 NSIS current-user setup executable;
- Android ARM64 directly installable APK;
- SHA-256 checksum manifest tied to version and source head.

Android beta signing must be stable across beta builds but remain distinct from any future production/store signing identity. Windows production Authenticode signing, Microsoft Store publication, Google Play publication and public launch remain separate owner/provider gates.
