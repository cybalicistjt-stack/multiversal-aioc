# Application Implementation Roadmap — MAL-09 Closeout / MAL-10 Selection

**Date:** 2026-09-04  
**Status:** canonical closeout supplement

## MAL-09 completed_verified

MAL-09 — Accessibility, Mobile/Input, Performance & Nonblocking Fallbacks — completed from exact application baseline `0df7fb35b22ae6906e876a1c651a6f7e00787a20`.

- Governed start: AIOC PR `950`, candidate `e37bd99a2386c89aee4d2c9ab50dd1790b3025a0`, Repository Health run `33854622260`, job `100964942485`, merge `2744bd4d94e068c428a0e756ba3d6e1d15975beb`.
- Genuine matching acceptance RED: application head `15eed08a07206e5217b7606f714c9ca8dacb2c20`, run `33854883855`; Linux and Windows failed at the intended missing-production `client-typecheck` boundary; deterministic comparison passed with receipt `eb0d5cc211ba4c3ace22a5222c96645c4ffe6689fa7e8e17b5bf48b40c9f9580`.
- Production GREEN: exact head `d72b454c6cc8df0fe4916f374a6ebe0158121aea`, run `33855096444`; selector, Linux, Windows and deterministic comparison all passed with receipt `57769229558cac1950d8b6008bd6daa4d168b40c3f5b3d363c9541d931b80eb0`.
- Application PR `404` merged as `c8cb1bbb18def3ac8f910fc75d6d52d8181ae291`.
- Repairs: validation-contract `0`; application-feature `0`; repository-state `0`; historical predecessor fanout `0`; unchanged-evidence reruns `0`; post-merge stale-pointer incidents `0`.

MAL-09 freezes semantic-equivalent accessibility controls, device-neutral semantic input normalization, presentation-only performance degradation and deterministic visibility-conservative nonblocking fallbacks. MAL-08 owner/reward boundaries remain authoritative.

## MAL-10 selected_not_started

MAL-10 — Starter Library & Golden Microgame/Aniloop Proof — is the strict successor and is selected from exact application main `c8cb1bbb18def3ac8f910fc75d6d52d8181ae291` with branch `null` and implementation authority `false`.

A future governed start may authorize only a small original starter library and deterministic golden proof composed from frozen MAL-01..09 contracts. Starter content may demonstrate frozen MAL capabilities but must not copy proprietary game maps, encounter scripts, minigame logic, level designs or reward tables, create parallel canonical owner truth, reveal hidden state, grant rewards or bypass Permission.

Golden proof must preserve semantic results across self-hosted Linux/Windows and permitted accessibility/device/presentation variants. No durable persistence, migration `0022`, ALP-01+, provider activation, tester distribution, release or deployment authority is introduced by this selection.
