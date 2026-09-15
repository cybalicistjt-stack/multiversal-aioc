# ChatGPT Project Source Cutover — Operations V3

The Multiversal Project Source entry files must not contain independent execution rules or current-state claims. Their only operational job is to route a new GPT conversation to the canonical AIOC operations door.

## Replace these Project Source files

### `START_HERE.md`

Use the replacement maintained in the cutover bundle. Its only authority statement is:

- canonical repository: `cybalicistjt-stack/multiversal-aioc`
- canonical door: `operations/BOOTSTRAP.md`
- GitHub current `main` wins for technical implementation facts
- every other Project Source is reference/evidence only

### `NEW_CHAT_PROMPT.txt`

Use exactly:

`Open cybalicistjt-stack/multiversal-aioc/operations/BOOTSTRAP.md from current main and follow it. Use no other bootstrap or behavior source.`

### `SOURCE_MAP.md`

Keep source classifications and provenance guidance, but remove any implication that it can route current execution. It is source discovery only.

### `PROJECT_SOURCE_MANIFEST.md`

Keep inventory/checksum information, but make the authority note explicit: it cannot select current work or define agent behavior.

## Preserve without operational authority

Keep the Feature/UI/Screen Bibles, game-framework packages, provenance packages, source archives, continuity snapshots and historical conversation exports. These remain valuable content/provenance/recovery sources and are not deleted.

## Required Project setting

Replace the ChatGPT Project custom instructions with `operations/adapters/GPT_PROJECT_INSTRUCTIONS.md`.

## Tool limitation

The available Project Files API can read Project-backed files but cannot replace the Project attachment or custom-instruction surfaces in place. Repository-side cutover therefore prepares verified replacement files; the Project surface must be replaced through the ChatGPT Project UI or another future API that explicitly supports Project-source mutation.
