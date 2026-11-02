#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures/session/p9-06-018-hidden-information-response-filter.json"
SOURCE = ROOT / "packages/contracts/src/session/hidden-information-response-filter.ts"
WORKFLOW = ROOT / ".github/workflows/validate-p9-06-018.yml"


def need(ok, msg):
    if not ok:
        raise SystemExit(msg)


def authorize(viewer, campaign, membership):
    if viewer == campaign["ownerSubjectId"]:
        return "owner"
    if not membership:
        return None
    if membership["subjectId"] != viewer or membership["campaignId"] != campaign["campaignId"]:
        return None
    return membership["role"]


def project(events, session_id, viewer, campaign, membership):
    role = authorize(viewer, campaign, membership)
    if role is None:
        return {"error": "unauthorized"}
    if any(event["sessionId"] != session_id for event in events):
        return {"error": "not_found"}
    visible = []
    for event in events:
        scope = event["visibility"]
        if scope["kind"] == "public":
            visible.append(event["eventId"])
        elif scope["kind"] == "gm_only" and role in {"owner", "gm"}:
            visible.append(event["eventId"])
        elif scope["kind"] == "participants" and viewer in scope["participantIds"]:
            visible.append(event["eventId"])
    return {"visible": visible, "hidden": len(events) - len(visible)}


data = json.loads(FIXTURE.read_text())
need(data["schema_version"] == "1.0.0", "bad fixture schema")
need(data["work_item_id"] == "P9-06-018", "wrong work item")
need(len(data["cases"]) >= 6, "insufficient deterministic coverage")

for case in data["cases"]:
    result = project(data["events"], data["session_id"], case["viewerSubjectId"], data["campaign"], case.get("membership"))
    if "expectedError" in case:
        need(result == {"error": case["expectedError"]}, f"fixture failed: {case['id']}")
    else:
        need(result["visible"] == case["expectedVisibleEventIds"], f"visibility mismatch: {case['id']}")
        need(result["hidden"] == case["expectedHiddenCount"], f"hidden count mismatch: {case['id']}")

cross = data["cross_session_case"]
result = project(data["events"] + [cross["event"]], data["session_id"], cross["viewerSubjectId"], data["campaign"], cross["membership"])
need(result == {"error": cross["expectedError"]}, "cross-session leakage was not rejected")

text = SOURCE.read_text()
for token in ["session.read", "gm_only", "participantIds", "hiddenEventCount", "unauthorized", "event.sessionId !== context.sessionId"]:
    need(token in text, f"source contract missing {token}")
need("authorizeCampaignRequest" in text.split("visibleEvents = events.filter")[0], "projection must authorize before visibility filtering")

workflow = WORKFLOW.read_text()
need("python tools/verify_p9_06_018.py" in workflow, "workflow does not run focused validator")
need("p9-06-018-hidden-information-response-filter.json" in workflow, "workflow path filter missing fixture")
print("P9-06-018 verification passed")
