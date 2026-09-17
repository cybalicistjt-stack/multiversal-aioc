#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "evidence" / "content-pipeline" / "beacon-debt-runtime-fixture-candidate.json"
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


def main():
    assert FIXTURE.exists(), "Beacon Debt runtime fixture candidate is missing"
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    version_index = json.loads(VERSION_INDEX.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    golden = json.loads(GOLDEN.read_text(encoding="utf-8"))

    assert cert["recordCount"] == 526
    assert version_index["versionCount"] == 47
    assert golden["overall_state"] == "DETERMINISTIC_GOLDEN_LAUNCH_READY_PRE_RUNTIME"

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
    assert visibility["policyVersion"] == "candidate-0.1.0"
    assert visibility["truthProjection"] == "gm-only-until-solved"
    assert visibility["clueDefault"] == "hidden-until-governed-discovery-or-reveal"
    assert visibility["permissionBeforeResolutionAndAggregation"] is True
    assert "CF-05" in visibility["initiallyHiddenClueIds"]
    assert "CF-06" in visibility["initiallyHiddenClueIds"]

    snapshot = fixture["launchSnapshotBoundary"]
    assert snapshot["launchSnapshotId"] is None
    assert snapshot["readinessReceiptId"] is None
    assert snapshot["immutableOnceCreated"] is True
    assert snapshot["creationAuthorizedByThisArtifact"] is False
    assert snapshot["requiredActionSequence"] == ["P8-ACT-021", "P8-ACT-022"]
    assert snapshot["blockingFindings"] == [
        "authoritative Campaign/Scene/Session aggregate versions do not yet exist",
        "P8-ACT-021 launch-readiness receipt has not yet been created",
    ]

    version_keys = {entry["key"] for entry in version_index["versions"]}
    pinned = set()
    unresolved = []
    for ref in iter_refs(fixture):
        key = f"{ref['objectId']}@{ref['objectVersion']}"
        if ref.get("referenceClass") == "MIB-11 source-only stable identity":
            if key not in {"world:havalaea@1.0.0", "setting:vertigon@1.0.0"}:
                unresolved.append(key)
            continue
        pinned.add(key)
        if key not in version_keys:
            unresolved.append(key)
    assert not unresolved, f"fixture has unresolved exact references: {sorted(set(unresolved))}"
    assert REQUIRED_PINNED_REFS <= pinned, f"fixture is missing required exact pins: {sorted(REQUIRED_PINNED_REFS - pinned)}"

    assert fixture["itemCompletionCompatibility"]["modifiesItemIdentity"] is False
    assert fixture["itemCompletionCompatibility"]["ogrGameReadyClaim"] is False
    assert fixture["itemCompletionCompatibility"]["replacementPathPreserved"] is True

    print("Beacon Debt pre-runtime fixture candidate: PASS")


if __name__ == "__main__":
    main()
