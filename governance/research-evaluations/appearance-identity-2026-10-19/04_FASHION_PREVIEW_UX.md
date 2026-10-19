# 04 — UX-01 Fashion Scene Context and Effect Preview Study

## Verified starting point
The inspected FDE workspace mounts FDE-02 selectors, FDE-03 SVG/asset preview, FDE-04 persistent library, FDE-05 intake, FDE-06 asset realization and FGA-04 session actions. FGA-04 exposes full-body/portrait/token views; FDE-03 draws the garment using a local semantic projection and supported primitive coverage checks. The inspected modules do not offer contextual lighting or scene preview controls. **Do not claim global absence** until shared scene and renderer capabilities are audited.

External example: Infinity Nikki v2.8 provides current-location scene preview, four selectable lighting states, effect visibility toggles, and missing-piece reports on scheme import (official v2.8 notes: https://infinitynikki.infoldgames.com/en/news/560).

## Proposed limited MVP
1. Add a **noncanonical Preview Context** control to the existing Fashion workspace: `neutral`, `daylight`, `low_light`, `interior_warm`, `high_contrast_magic` (names/values provisional; select bounded context variants based on actual rendering capabilities).
2. Reuse the *same* FGA semantic garment state, topology/fit output, material/palette and exact resource coverage across all contexts.
3. Keep fixed CAPP/PPIA 3/4 master instead of copying unrestricted camera rotation. For token and portrait use existing derivative profiles.
4. Effect visibility toggle is per authorized visual effect; view-only changes cannot mute an active mechanical ability or alter equipment ownership.
5. Show `renderable | partial | unsupported | unknown` alongside a deterministic nonvisual explanation. No hidden body/GM-only evidence emerges through preview context.
6. If real lighting shader is unavailable, allow a **clearly labeled illustrative context simulator**; don't claim it accurately predicts a game renderer.
7. Responsive use: inspector controls remain first, preview may collapse at high zoom; keyboard navigation, screen-reader labels, reduced-motion mode, high contrast. No color-only compatibility indication.
8. Save preset associations separately from transient preview camera or environmental selection; exporting scene context never asserts world-weather truth.

## UX interaction flow
Open FDE > choose existing design from FDE-04 > choose compatible topology > choose existing full-body/portrait/token > choose scene context > optional authorized cosmetic effect toggles > inspect fit/coverage > save visual presentation preference (optional) > export after scoped compatibility review.

**Unhappy paths:** unknown topology; invalid asset license; missing contextual background; missing effect asset; changed garment checksum; no network; unsupported phone GPU; reduced-motion preference; imported recipe references unavailable garment; stale session/version. Each has a visible explanation and allows continued semantic editing where safe.

## Test plan
- [ ] Same canonical garment checksum across all contexts and outputs.
- [ ] Unsupported contexts show fallback as explicit illustrative preview (never silently substitute).
- [ ] Same fit/occlusion across context choices; wing/tail clearance invariant.
- [ ] No dice/ability/inventory/equipment changes from effect visibility setting.
- [ ] Existing FDE save/import/reopen survives style switch, stale asset and cold start.
- [ ] Three derivatives preserve semantic identity.
- [ ] Nonvisual summary and keyboard-only controls match GUI choices.
- [ ] Device-specific performance recorded with explicit platform, build and renderer evidence.

## Explicit non-goals
No world simulation, no live scene weather, no unlimited 3D orbit, no new lighting engine implied by a dropdown, no AI image generation dependency, no fashion implementation without a newly selected governed task.
