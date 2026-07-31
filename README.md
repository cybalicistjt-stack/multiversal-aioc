# Multiversal AIOC Standalone PWA v0.2.0

A free, local-first Android-installable Progressive Web App for operating the Multiversal AI development project. It has no Base44 dependency, no subscription, and no required backend.

## Added in v0.2.0

The app now includes the original operations tools plus:

- Executive intelligence dashboard and local conversational command layer
- Project-wide search, knowledge graph, decision provenance, living documentation, and digital twin impact simulation
- Agent workload, quality, routing, conflict detection, credit efficiency, and bottleneck analysis
- Repository health, dependency mapping, release notes, migrations, artifacts, approvals, analytics, estimates, heatmaps, and critical-path records
- World timeline, species, item, vehicle, quest, dialogue, story-flow, relationship, rule, and pack-authoring tools
- Voice capture, photo/file capture, daily planning, calendar export, focus timer, version checkpoints, backup testing, and emergency recovery

All records are stored in the browser's local storage and can be exported as a complete JSON backup. Photos are referenced by metadata rather than permanently embedded to avoid filling phone storage. Small text, Markdown, and JSON files can be imported into notes.

## Run locally

From the extracted directory:

```bash
python3 -m http.server 8080
```

Open `http://localhost:8080` in a browser on the same device. For Android installation, host this folder over HTTPS using any free static host, then open it in Chrome and choose **Install app** or **Add to Home screen**.

## No paid services required

Core features run entirely on-device. Optional future live GitHub, Codex, AI, calendar, and notification synchronization would require their respective credentials or services, but none are required for this release.
