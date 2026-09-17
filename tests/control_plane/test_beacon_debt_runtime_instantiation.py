from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME = ROOT / "evidence/content-pipeline/beacon-debt-runtime-instantiation.json"
CANDIDATE = ROOT / "evidence/content-pipeline/beacon-debt-runtime-fixture-candidate.json"
CERT = ROOT / "content-db/certification.json"
VERSION_INDEX = ROOT / "content-db/version-index.json"

A5_VALIDATION_CLASSES = [
    "required-field", "stable-id-reference", "source-version", "campaign-isolation",
    "permission", "entitlement", "pack-present", "pack-version", "pack-dependency",
    "rules-profile", "schema-compatibility", "visibility-safety", "note-classification",
    "character-control", "character-lifecycle", "participant-membership", "role-scope",
    "assistant-gm-delegation", "observer-grant", "map-alternative", "media-reference",
    "objective-entry-condition", "duplicate-placement-policy", "launch-readiness",
]


def digest(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def load(path: Path):
    assert path.is_file(), f"missing required artifact: {path.relative_to(ROOT)}"
    return json.loads(path.read_text())


def test_beacon_debt_runtime_instantiation_and_snapshot():
    runtime = load(RUNTIME)
    candidate = load(CANDIDATE)
    cert = load(CERT)
    version_index = load(VERSION_INDEX)

    assert runtime["schema_version"] == "1.0.0"
    assert runtime["artifact"] == "BEACON_DEBT_GOLDEN_RUNTIME_INSTANTIATION"
    assert runtime["state"] == "IMMUTABLE_LAUNCH_SNAPSHOT_READY_NO_PLAY_EXECUTED"
    assert runtime["playSequenceExecuted"] is False
    assert runtime["playtestClaim"] is False

    campaign = runtime["campaign"]
    assert campaign["campaignId"] == candidate["campaignDraft"]["campaignId"]
    assert campaign["version"] == 1
    assert campaign["lifecycleState"] == "active"
    assert campaign["policyBinding"]["rulesProfileId"] == "mv.adventure.beacon-debt.rules.golden-test-core"
    assert campaign["policyBinding"]["rulesProfileVersion"] == "1.0.0"

    scenes = runtime["scenes"]
    maps = runtime["sceneMaps"]
    assert len(scenes) == 5
    assert len(maps) == 5
    assert [s["sortOrder"] for s in scenes] == [1, 2, 3, 4, 5]
    assert all(s["version"] == 1 and s["lifecycleState"] == "ready" for s in scenes)
    assert all(m["coordinateMode"] == "gridless" for m in maps)
    assert all(not m.get("mapMediaReferenceId") and not m.get("squareCalibration") for m in maps)
    assert all(len(m["gridlessLocations"]) == 1 for m in maps)

    placement_ids = set()
    for placement in runtime["placements"]:
        assert placement["placementId"] not in placement_ids
        placement_ids.add(placement["placementId"])
        assert placement["version"] == 1
        assert placement["semanticLocation"]["kind"] == "gridless-location"
        ref = placement["sourceDefinition"]
        assert ref["objectId"] and ref["objectVersion"]

    validation = runtime["readinessReceipt"]
    gate_scene = next(s for s in scenes if s["sceneId"] == "scene:beacon-debt:gate-pressure")
    assert validation["campaignId"] == campaign["campaignId"]
    assert validation["campaignVersion"] == campaign["version"]
    assert validation["sceneId"] == gate_scene["sceneId"]
    assert validation["sceneVersion"] == gate_scene["version"]
    assert validation["evaluatedClasses"] == A5_VALIDATION_CLASSES
    assert validation["findings"] == []
    assert validation["canLaunch"] is True
    assert validation["packLockDigest"] == cert["semanticFingerprint"]
    assert validation["inputDigest"] == digest(runtime["readinessInputs"])

    snapshot = runtime["launchSnapshot"]
    assert snapshot["immutable"] is True
    assert snapshot["campaignId"] == campaign["campaignId"]
    assert snapshot["campaignVersion"] == campaign["version"]
    assert snapshot["sceneId"] == gate_scene["sceneId"]
    assert snapshot["sceneVersion"] == gate_scene["version"]
    assert snapshot["rulesProfileId"] == validation["rulesProfileId"]
    assert snapshot["rulesProfileVersion"] == validation["rulesProfileVersion"]
    assert snapshot["packLockDigest"] == validation["packLockDigest"]
    assert snapshot["validationReceiptId"] == validation["validationReceiptId"]
    assert snapshot["mapBinding"]["coordinateMode"] == "gridless"
    assert snapshot["mapBinding"]["semanticMapVersion"] == 1
    assert snapshot["characterBindings"] == []
    assert len(snapshot["participantBindings"]) == 1
    assert snapshot["participantBindings"][0]["role"] == "gm"

    gate_placement_ids = {p["placementId"] for p in runtime["placements"] if p["sceneId"] == gate_scene["sceneId"]}
    assert {p["placementId"] for p in snapshot["placementVersions"]} == gate_placement_ids
    assert snapshot["contentDigest"] == digest(runtime["snapshotDigestInput"])

    session = runtime["session"]
    assert session["status"] == "launched"
    assert session["revision"] == 1
    assert session["lastSequence"] == 0
    assert session["campaignId"] == campaign["campaignId"]
    assert session["sceneId"] == gate_scene["sceneId"]
    assert session["launchSnapshotId"] == snapshot["snapshotId"]
    assert session["launchSnapshotChecksum"] == snapshot["contentDigest"]

    assert runtime["runtimeEffects"] == []
    assert runtime["revealedClues"] == []
    assert runtime["durableEvents"] == []

    # Exact versions referenced by the runtime fixture must remain resolvable.
    current_ids = {entry["stableId"] for entry in version_index.get("records", []) if isinstance(entry, dict) and entry.get("stableId")}
    serialized = json.dumps(runtime)
    for required in (
        "mv.adventure.beacon-debt.module",
        "mv.adventure.beacon-debt.rules.golden-test-core",
        "mv.setting.faction.administrative-syndicate",
        "mv.adventure.beacon-debt.social-situation.east-gate-priority",
    ):
        assert required in serialized
    assert cert["recordCount"] == 526
