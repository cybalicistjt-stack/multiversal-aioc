# CAB-13 — High-Risk Review Queue

## P0 — data/source integrity

- `Abilities_Core.csv + ABLREC-00483` Rain of Arrows — Mechanics field visibly contains unrelated Blood Weapons material; recover source boundary before balance repair.
- Any additional field-boundary contamination must be source-confirmed before promotion to P0.

## P1 — throughput / multiplier review

- Countermastery — extra Reaction generation and expansion.
- Master of War Mounts — persistent extra mount Action each turn.
- Personal Time Dilation — full extra Action for one minute at source 2,000 XP.
- Perfect Timing (Counteroffensive) — additional Reaction even if already used.
- Supreme Rider’s Reflexes — additional Reaction/round.

## P1 — multi-axis bundle review

- Avatar of Glory — +5 attacks, nonmagical immunity, extra attack, one-minute transformation; source 5,000 XP.
- Ethereal Overdrive — all-damage resistance, +2 attacks/saves, 10 HP/turn regeneration, mana resource, one-minute state.
- Regenerative Shift — recurring transformed-state healing, counter condition.

## Corpus queues

All records matching consequential action multipliers, autonomous ally actions, immunity/resistance bundles, regeneration, transformations, multipliers, auto-success/bypass, resource generation, unbounded per-each scaling, or persistent global effects enter CAB-22 repair triage. Records with missing action/frequency/resource/interaction semantics are reviewed before deterministic repricing.

Queue identity uses `source_dataset + Record_ID` per CAB-11 until globally unique stable IDs are assigned.