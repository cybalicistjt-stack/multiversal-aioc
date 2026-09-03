# APPLICATION IMPLEMENTATION ROADMAP — SCL-08 CLOSEOUT — 2026-09-03

## Canonical result

SCL-08 — Vehicle, Mecha, Ship & Fleet Integration — is `completed_verified` on application merge `1de481381d0d65d3a88d0e1cdc1af77ebe73dfb6`.

The tranche implements a visibility-first deterministic read-only integration projection over explicit canonical SCL profile/membership, F008 Asset Instance, F014 Vehicle Operation, actor/station and owner-domain handoff references. It does not copy or replace vehicle/Asset truth, infer flagship authority, impose a universal fleet-size cap, execute movement or Resource mutation, propagate damage/casualties, or mutate owner domains.

## Governed-start evidence

- AIOC PR: `897`
- validated head: `46f6124ed8502067129b2c5b017fa7e034556389`
- Repository Health run/job: `33751788835` / `100636762296`
- governed-start merge: `84ba98673cfb3e853dd3789bf1fce0f753450157`
- validation-contract repairs: `0`

## Acceptance-first RED

- head: `3c988221d684094946d9fc73a77d8ab3ecd37e24`
- run: `33752103675`
- selector: `100637776879`
- Linux: `100637813669`
- Windows: `100637813587`
- comparator: `100637978759`
- Linux artifact: `9891950822`
- Windows artifact: `9891954694`
- comparison artifact: `9891964212`
- deterministic receipt: `ced84fabe9a801e001ed09193bb9ac6a05858f926191b35003f3c8b7b305062a`

Both self-hosted lanes passed the governed invariant/install path and reached the intended missing-production `client-typecheck` RED before the production contract and panel were added.

## Final exact-head validation

- validated head: `16f4b1eded3ae90c577184b2dc84cce9feff67bd`
- run: `33752347595`
- selector/repository health: `100638564408`
- Linux: `100638603430`
- Windows: `100638603596`
- comparator: `100638773125`
- Linux artifact: `9892043491`
- Windows artifact: `9892047548`
- comparison artifact: `9892054711`
- deterministic receipt: `d0defc9bfd6f544cd0b2e69d0d7ac1bd13d93d103977297223cf5a8f1460d7be`
- historical predecessor profile fanout: `0`
- application feature repairs: `0`
- validation-contract repairs: `0`
- unchanged-evidence reruns: `0`

Application PR `392` merged as `1de481381d0d65d3a88d0e1cdc1af77ebe73dfb6`.

## Frozen SCL-08 boundaries

- SCL-01..07 remain completed and frozen.
- F008 remains canonical for Asset identity, ownership, custody, control, access, containment and lineage.
- F014 remains canonical for Vehicle Operations, crew/stations, movement, Resources, systems and operational state.
- SCL-03/04 retain command/order contracts and deterministic handoff planning.
- SCL-06 retains logistics/readiness evidence and support handoffs.
- SCL-07/World retain terrain/location/position truth.
- SCL-09 retains individual-to-unit casualty, damage and recovery reconciliation.
- SCL-10 retains faction, settlement, World and Campaign consequences.
- Source-specific squad-size and flagship/command-ship language remains source evidence only; it is not a universal scale cap and does not infer command authority.
- No autonomous AI command/adjudication, hidden-data reveal, owner mutation, duplicate ledger, durable SCL persistence or migration `0022` is authorized.

## Strict successor

SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery — is `selected_not_started` from exact application baseline `1de481381d0d65d3a88d0e1cdc1af77ebe73dfb6`, with `implementation_branch: null` and `implementation_authority: false`.

A future owner `Continue` must perform the bounded SCL-09 governed start before any application mutation.
