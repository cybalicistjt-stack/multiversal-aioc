#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
handler = ROOT / "packages/contracts/src/session/authoritative-session-command-handler.ts"
fixture_path = ROOT / "fixtures/session/p9-06-016-authoritative-command-handler.json"
workflow = ROOT / ".github/workflows/validate-p9-06-016.yml"

for path in (handler, fixture_path, workflow):
    if not path.is_file():
        raise SystemExit(f"missing required path: {path.relative_to(ROOT)}")

text = handler.read_text(encoding="utf-8")
required_tokens = [
    "handleAuthoritativeSessionCommand",
    "authorizeCampaignRequest",
    'action: "session.command"',
    '"stale-revision"',
    '"duplicate-without-receipt"',
    "processedCommandIds",
    "expectedRevision !== state.revision",
    "lastSequence + 1",
    "replayed: true",
]
for token in required_tokens:
    if token not in text:
        raise SystemExit(f"handler missing required token: {token}")

fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
if fixture.get("workItem") != "P9-06-016":
    raise SystemExit("fixture work item mismatch")
cases = {case["id"]: case for case in fixture.get("cases", [])}
required_cases = {
    "owner-accepted",
    "player-accepted",
    "observer-denied",
    "cross-campaign-denied",
    "stale-revision-denied",
    "duplicate-replayed",
    "wrong-session-denied",
}
missing = sorted(required_cases - set(cases))
if missing:
    raise SystemExit(f"missing deterministic cases: {missing}")
if cases["observer-denied"]["expected"].get("reason") != "unauthorized":
    raise SystemExit("observer must be denied command authority")
if cases["cross-campaign-denied"]["expected"].get("accepted") is not False:
    raise SystemExit("cross-campaign membership must not authorize")
if cases["stale-revision-denied"]["expected"].get("reason") != "stale-revision":
    raise SystemExit("stale revision semantics missing")
if cases["duplicate-replayed"]["expected"].get("replayed") is not True:
    raise SystemExit("duplicate replay semantics missing")

wtext = workflow.read_text(encoding="utf-8")
if "python tools/verify_p9_06_016.py" not in wtext:
    raise SystemExit("workflow does not invoke focused validator")

print("P9-06-016 authoritative session command handler validation passed")
