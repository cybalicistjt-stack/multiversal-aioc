#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "evidence" / "content-pipeline" / "beacon-debt-runtime-fixture-candidate.json"
INSTANTIATED = ROOT / "evidence" / "content-pipeline" / "beacon-debt-runtime-instantiated.json"
VERSION_INDEX = ROOT / "content-db" / "version-index.json"
CERT = ROOT / "content-db" / "certification.json"
GOLDEN = ROOT / "evidence" / "content-pipeline" / "beacon-debt-golden-diagnostics.json"

SCENE_IDS = [
    "scene:beacon-debt:gate-pressure",
    "scene:beacon-debt:damaged-crossing",
    "scene:beacon-debt:beacon-restoration",
    "scene:beacon-debt:listening-market-investigation",
    "scene:beacon-debt:consequence-return",
]

A5_VALIDATION_CLASSES = [
    "required-field", "stable-id-reference", "source-version", "campaign-isolation",
    "permission", "entitlement", "pack-present", "pack-version", "pack-dependency",
    "rules-profile", "schema-compatibility", "visibility-safety", "note-classification",
    "character-control", "character-lifecycle", "participant-membership", "role-scope",
    "assistant-gm-delegation", "observer-grant", "map-alternative", "media-reference",
    "objective-entry-condition", "duplicate-placement-policy", "launch-readiness",
]

REQUIRED_PINNED_REFS = {
    "mv.adventure.beacon-debt.module@1.0.2",
    "mv.adventure.beacon-debt.investigation.maps-as-leverage@1.0.0",
    "mv.setting.faction.administrative-syndicate@1.0.0",
    "mv.setting.faction.black-feathers@1.0.0",
    "mv.faction.lantern-compact@1.0.0",
    "mv.setting.vertigon.hazard.transit-crossflow-cascade@1.0.1",
    "mv.adventure.beacon-debt.npc.mira-venn@1.0.1",
    "mv.adventure.beacon-debt.social-situation.east-gate-priority@1.0.2",
    "mv.adventure.beacon-debt.rules.golden-test-core@1.0.0",
    "mv.adventure.beacon-debt.action.navigate-crossflow@1.0.0",
    "mv.adventure.beacon-debt.action.restore-route-beacon@1.0.0",
    "mv.adventure.beacon-debt.action.request-priority-exception@1.0.0",
    "mv.adventure.beacon-debt.resource.route-deterioration@1.0.0",
    "mv.adventure.beacon-debt.resource.refugee-arrival-pressure@1.0.0",
}


def iter_refs(value):
    if isinstance(value, dict):
        if "objectId" in value and "objectVersion" in value:
            yield value
        for child in value.values():
            yield from iter_refs(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_refs(child)


def assert_refs_resolve(value, version_keys):
    unresolved = []
    pinned = set()
    for ref in iter_refs(value):
        key = f"{ref['objectId']}@{ref['objectVersion']}"
        if ref.get("referenceClass") == "MIB-11 source-only stable identity":
            if key not in {"world:havalaea@1.0.0", "setting:vertigon@1.0.0"}:
                unresolved.append(key)
            continue
        pinned.add(key)
        if key not in version_keys:
            unresolved.append(key)
    assert not unresolved, f"unresolved exact references: {sorted(set(unresolved))}"
    return pinned


def validate_pre_runtime_candidate(version_keys):
    assert FIXTURE.exists(), "Beacon Debt runtime fixture candidate is missing"
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    assert fixture["artifact"] == "BEACON_DEBT_GOLDEN_RUNTIME_FIXTURE_CANDIDATE"
    assert fixture["state"] == "PRE_RUNTIME_FIXTURE_SPEC_READY"
    assert fixture["runtimeStateCreated"] is False
    assert fixture["launchSnapshotCreated"] is False
    assert fixture["playtestClaim"] is False

    campaign = fixture["campaignDraft"]
    assert campaign["campaignId"] == "campaign-fixture:beacon-debt-golden-01"
    assert campaign["version"] == "candidate-0.1.0"
    assert campaign["adventureRef"] == {
        "ownerDomain": "D28",
        "objectId": "mv.adventure.beacon-debt.module",
        "objectVersion": "1.0.2",
    }

    scenes = fixture["sceneDrafts"]
    assert [scene["sceneId"] for scene in scenes] == SCENE_IDS
    assert [scene["order"] for scene in scenes] == [1, 2, 3, 4, 5]
    assert all(scene["coordinateMode"] == "gridless" for scene in scenes)
    assert all(scene["mapMediaReferenceId"] is None for scene in scenes)
    assert all(scene["calibrationId"] is None for scene in scenes)

    resources = fixture["initialCampaignLocalState"]["resourceValues"]
    assert resources == {
        "mv.adventure.beacon-debt.resource.route-deterioration@1.0.0": 1,
        "mv.adventure.beacon-debt.resource.refugee-arrival-pressure@1.0.0": 1,
    }
    assert fixture["initialCampaignLocalState"]["bridgeState"] == "already-damaged-synthetic-fixture"
    assert fixture["initialCampaignLocalState"]["priorRealSessionOrEventImplied"] is False

    visibility = fixture["visibilityPolicyCandidate"]
    assert visibility["truthProjection"] == "gm-only-until-solved"
    assert visibility["clueDefault"] == "hidden-until-governed-discovery-or-reveal"
    assert visibility["permissionBeforeResolutionAndAggregation"] is True

    snapshot = fixture["launchSnapshotBoundary"]
    assert snapshot["launchSnapshotId"] is None
    assert snapshot["readinessReceiptId"] is None
    assert snapshot["immutableOnceCreated"] is True
    assert snapshot["creationAuthorizedByThisArtifact"] is False
    assert snapshot["requiredActionSequence"] == ["P8-ACT-021", "P8-ACT-022"]

    pinned = assert_refs_resolve(fixture, version_keys)
    assert REQUIRED_PINNED_REFS <= pinned
    assert fixture["itemCompletionCompatibility"]["modifiesItemIdentity"] is False
    assert fixture["itemCompletionCompatibility"]["ogrGameReadyClaim"] is False


def validate_instantiated_runtime(version_keys, cert):
    assert INSTANTIATED.exists(), "instantiated Beacon Debt A5 runtime fixture is missing"
    runtime = json.loads(INSTANTIATED.read_text(encoding="utf-8"))

    assert runtime["artifact"] == "BEACON_DEBT_GOLDEN_RUNTIME_INSTANTIATED"
    assert runtime["state"] == "IMMUTABLE_LAUNCH_SNAPSHOT_CREATED"
    assert runtime["fixtureRuntimeStateCreated"] is True
    assert runtime["productionPersistentRuntimeStateCreated"] is False
    assert runtime["launchSnapshotCreated"] is True
    assert runtime["playSequenceExecuted"] is False
    assert runtime["playtestClaim"] is False
    assert runtime["authority"]["productionServiceImplementationAvailable"] is False

    surface = runtime["canonicalSurface"]
    assert surface["recordCount"] == cert["recordCount"] == 556
    assert surface["semanticFingerprint"] == cert["semanticFingerprint"]
    assert surface["sourceDigest"] == cert["sourceDigest"]

    campaign = runtime["campaign"]
    assert campaign["campaignId"] == "campaign:beacon-debt-golden-01"
    assert campaign["version"] == 1
    assert campaign["lifecycleState"] == "active"
    assert campaign["policyBinding"]["rulesProfileId"] == "mv.adventure.beacon-debt.rules.golden-test-core"
    assert campaign["policyBinding"]["rulesProfileVersion"] == "1.0.0"

    scenes = runtime["scenes"]
    maps = runtime["maps"]
    assert [scene["sceneId"] for scene in scenes] == SCENE_IDS
    assert [scene["sortOrder"] for scene in scenes] == [0, 1, 2, 3, 4]
    assert all(scene["campaignId"] == campaign["campaignId"] for scene in scenes)
    assert all(scene["lifecycleState"] == "ready" and scene["version"] == 1 for scene in scenes)
    assert len(maps) == 5
    assert all(m["coordinateMode"] == "gridless" and m["version"] == 1 for m in maps)
    assert all("mapMediaReferenceId" not in m and "squareCalibration" not in m for m in maps)
    assert {m["sceneId"] for m in maps} == set(SCENE_IDS)

    placements = runtime["placements"]
    assert len(placements) >= 25
    assert all(p["version"] == 1 for p in placements)
    assert all(p["sceneId"] in SCENE_IDS for p in placements)
    assert all(p["semanticLocation"]["kind"] == "gridless-location" for p in placements)
    pinned = assert_refs_resolve(runtime, version_keys)
    assert REQUIRED_PINNED_REFS <= pinned

    receipt = runtime["validationReceipt"]
    assert receipt["campaignId"] == campaign["campaignId"]
    assert receipt["campaignVersion"] == 1
    assert receipt["sceneId"] == SCENE_IDS[0]
    assert receipt["sceneVersion"] == 1
    assert receipt["evaluatedClasses"] == A5_VALIDATION_CLASSES
    assert receipt["findings"] == []
    assert receipt["canLaunch"] is True
    assert receipt["inputDigest"].startswith("sha256:") and len(receipt["inputDigest"]) == 71

    snapshot = runtime["launchSnapshot"]
    assert snapshot["campaignId"] == campaign["campaignId"]
    assert snapshot["campaignVersion"] == 1
    assert snapshot["sceneId"] == SCENE_IDS[0]
    assert snapshot["sceneVersion"] == 1
    assert snapshot["rulesProfileId"] == receipt["rulesProfileId"]
    assert snapshot["rulesProfileVersion"] == receipt["rulesProfileVersion"]
    assert snapshot["packLockDigest"] == receipt["packLockDigest"] == cert["semanticFingerprint"]
    assert snapshot["validationReceiptId"] == receipt["validationReceiptId"]
    assert snapshot["immutable"] is True
    assert snapshot["mapBinding"]["coordinateMode"] == "gridless"
    assert snapshot["mapBinding"]["semanticMapVersion"] == 1
    assert snapshot["characterBindings"] == []
    assert len(snapshot["participantBindings"]) == 1
    assert snapshot["participantBindings"][0]["role"] == "gm"
    assert snapshot["contentDigest"].startswith("sha256:") and len(snapshot["contentDigest"]) == 71

    gate_placement_ids = {p["placementId"] for p in placements if p["sceneId"] == SCENE_IDS[0]}
    snap_placement_ids = {p["placementId"] for p in snapshot["placementVersions"]}
    assert snap_placement_ids == gate_placement_ids

    session = runtime["session"]
    assert session["campaignId"] == campaign["campaignId"]
    assert session["sceneId"] == SCENE_IDS[0]
    assert session["launchSnapshotId"] == snapshot["snapshotId"]
    assert session["launchSnapshotChecksum"] == snapshot["contentDigest"]
    assert session["status"] == "launched"
    assert session["revision"] == 1
    assert session["lastSequence"] == 0

    state = runtime["initialCampaignLocalState"]
    assert state["resourceValues"] == {
        "mv.adventure.beacon-debt.resource.route-deterioration@1.0.0": 1,
        "mv.adventure.beacon-debt.resource.refugee-arrival-pressure@1.0.0": 1,
    }
    assert state["priorRealSessionOrEventImplied"] is False
    assert state["durableEventsCreated"] is False

    visibility = runtime["visibilityState"]
    assert visibility["truthProjection"] == "gm-only-until-solved"
    assert visibility["initiallyRevealedClues"] == []
    assert visibility["playerKnowledgeCreated"] is False

    boundary = runtime["executionBoundary"]
    assert boundary["nextAllowedOperation"] == "execute deterministic golden-test play sequence"
    assert boundary["actionResultsCreated"] is False
    assert boundary["clueDiscoveryEventsCreated"] is False
    assert boundary["postSessionEventsCreated"] is False
    assert boundary["runtimeExecutionAuthorizedByThisArtifact"] is False


def main():
    version_index = json.loads(VERSION_INDEX.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    golden = json.loads(GOLDEN.read_text(encoding="utf-8"))
    assert cert["recordCount"] == 556
    assert version_index["versionCount"] == 47
    assert golden["overall_state"] == "DETERMINISTIC_GOLDEN_LAUNCH_READY_PRE_RUNTIME"
    version_keys = {entry["key"] for entry in version_index["versions"]}

    validate_pre_runtime_candidate(version_keys)
    validate_instantiated_runtime(version_keys, cert)
    print("Beacon Debt runtime fixture + immutable launch snapshot: PASS")


if __name__ == "__main__":
    main()
