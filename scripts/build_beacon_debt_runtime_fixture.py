#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "evidence" / "content-pipeline" / "beacon-debt-runtime-fixture-candidate.json"
CERT = ROOT / "content-db" / "certification.json"
OUT = ROOT / "evidence" / "content-pipeline" / "beacon-debt-runtime-instantiated.json"

VALIDATION_CLASSES = [
    "required-field", "stable-id-reference", "source-version", "campaign-isolation",
    "permission", "entitlement", "pack-present", "pack-version", "pack-dependency",
    "rules-profile", "schema-compatibility", "visibility-safety", "note-classification",
    "character-control", "character-lifecycle", "participant-membership", "role-scope",
    "assistant-gm-delegation", "observer-grant", "map-alternative", "media-reference",
    "objective-entry-condition", "duplicate-placement-policy", "launch-readiness",
]

AT = "2026-09-17T12:15:00Z"
OWNER = "subject:beacon-debt-golden-gm"
CAMPAIGN_ID = "campaign:beacon-debt-golden-01"
SESSION_ID = "session:beacon-debt-golden-01"
VISIBILITY_ID = "visibility:beacon-debt-golden-01"
RULES_ID = "mv.adventure.beacon-debt.rules.golden-test-core"
RULES_VERSION = "1.0.0"


def digest(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def placement_kind(object_id):
    if ".item." in object_id:
        return "item"
    if ".npc." in object_id or ".group." in object_id:
        return "creature-npc"
    if ".hazard." in object_id:
        return "hazard"
    if ".location." in object_id:
        return "environment-feature"
    return "other-governed-scene-content"


def main():
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    assert cert["recordCount"] == 556

    campaign = {
        "campaignId": CAMPAIGN_ID,
        "ownerSubjectId": OWNER,
        "title": "Beacon Debt — Deterministic Golden Test",
        "summary": "Governed A5 golden-test fixture for The Beacon Debt; no play sequence executed.",
        "lifecycleState": "active",
        "policyBinding": {
            "rulesProfileId": RULES_ID,
            "rulesProfileVersion": RULES_VERSION,
            "permissionPolicyVersion": "fixture-1",
            "visibilityPolicyVersion": "1",
        },
        "packLockId": cert["semanticFingerprint"],
        "version": 1,
        "createdAt": AT,
        "updatedAt": AT,
    }

    scenes = []
    maps = []
    placements = []
    for i, draft in enumerate(candidate["sceneDrafts"]):
        map_id = f"mapv:beacon-debt:{i+1}"
        location_id = f"location:beacon-debt:{i+1}"
        scenes.append({
            "sceneId": draft["sceneId"],
            "campaignId": CAMPAIGN_ID,
            "title": draft["title"],
            "sceneType": ["social", "exploration", "technical", "investigation", "consequence"][i],
            "lifecycleState": "ready",
            "sortOrder": i,
            "templateReferenceIds": [],
            "branchTargetSceneIds": [candidate["sceneDrafts"][i+1]["sceneId"]] if i < 4 else [],
            "activeMapVersionId": map_id,
            "version": 1,
            "createdAt": AT,
            "updatedAt": AT,
        })
        maps.append({
            "mapVersionId": map_id,
            "sceneId": draft["sceneId"],
            "version": 1,
            "coordinateMode": "gridless",
            "namedZones": [],
            "gridlessLocations": [{
                "locationId": location_id,
                "label": draft["title"],
                "description": draft["semanticLocation"],
            }],
            "dungeonPrimitives": [],
            "nonvisualAlternative": draft["semanticLocation"],
            "createdAt": AT,
        })
        refs = [draft["primaryLocationRef"], *draft["contentRefs"]]
        for j, ref in enumerate(refs):
            placements.append({
                "placementId": f"placement:beacon-debt:{i+1}:{j+1}",
                "sceneId": draft["sceneId"],
                "placementKind": placement_kind(ref["objectId"]),
                "sourceDefinition": {
                    "ownerDomain": ref["ownerDomain"],
                    "objectId": ref["objectId"],
                    "objectVersion": ref["objectVersion"],
                },
                "semanticLocation": {
                    "kind": "gridless-location",
                    "locationId": location_id,
                    "label": draft["title"],
                    "description": draft["semanticLocation"],
                },
                "layerId": "governed-content",
                "zOrder": j,
                "label": ref["objectId"],
                "visibilityPolicyReference": VISIBILITY_ID,
                "localState": {},
                "version": 1,
            })

    gate_scene = scenes[0]
    gate_map = maps[0]
    gate_placements = [p for p in placements if p["sceneId"] == gate_scene["sceneId"]]
    readiness_input = {
        "campaignId": CAMPAIGN_ID,
        "campaignVersion": 1,
        "sceneId": gate_scene["sceneId"],
        "sceneVersion": 1,
        "rulesProfileId": RULES_ID,
        "rulesProfileVersion": RULES_VERSION,
        "packLockDigest": cert["semanticFingerprint"],
        "viewerSubjectId": OWNER,
        "workspaceEntryAuthorizationId": "workspace-entry:beacon-debt-golden-01",
        "permissionDecisionReference": "permission:beacon-debt-golden-01",
        "entitlementDecisionReferences": [],
        "online": True,
        "at": AT,
    }
    receipt = {
        "validationReceiptId": "validation:beacon-debt-golden-01",
        **{k: readiness_input[k] for k in ["campaignId", "campaignVersion", "sceneId", "sceneVersion", "rulesProfileId", "rulesProfileVersion", "packLockDigest"]},
        "evaluatedClasses": VALIDATION_CLASSES,
        "findings": [],
        "permissionBeforeAggregationEvidenceReference": "permission:beacon-debt-golden-01",
        "semanticMapEvidenceReference": "semantic-map:beacon-debt-gate-pressure:v1",
        "inputDigest": digest(readiness_input),
        "validatedAt": AT,
        "canLaunch": True,
    }

    snapshot_core = {
        "snapshotId": "snapshot:beacon-debt-golden-01",
        "campaignId": CAMPAIGN_ID,
        "campaignVersion": 1,
        "sceneId": gate_scene["sceneId"],
        "sceneVersion": 1,
        "rulesProfileId": RULES_ID,
        "rulesProfileVersion": RULES_VERSION,
        "packLockDigest": cert["semanticFingerprint"],
        "schemaVersions": {"a5": "0.3.0", "content-db": "3.0.0", "beacon-debt-runtime-fixture": "1.0.0"},
        "participantBindings": [{
            "subjectId": OWNER,
            "membershipId": "membership:beacon-debt-golden-gm",
            "role": "gm",
            "membershipVersion": 1,
        }],
        "characterBindings": [],
        "placementVersions": [{
            "placementId": p["placementId"],
            "placementVersion": p["version"],
            **p["sourceDefinition"],
        } for p in gate_placements],
        "mapBinding": {
            "coordinateMode": "gridless",
            "mapVersionId": gate_map["mapVersionId"],
            "semanticMapVersion": gate_map["version"],
        },
        "visibilityPolicyVersion": "1",
        "validationReceiptId": receipt["validationReceiptId"],
        "createdBy": OWNER,
        "createdAt": AT,
        "immutable": True,
    }
    snapshot = dict(snapshot_core)
    snapshot["contentDigest"] = digest(snapshot_core)

    session = {
        "sessionId": SESSION_ID,
        "campaignId": CAMPAIGN_ID,
        "sceneId": gate_scene["sceneId"],
        "launchSnapshotId": snapshot["snapshotId"],
        "launchSnapshotChecksum": snapshot["contentDigest"],
        "status": "launched",
        "revision": 1,
        "lastSequence": 0,
        "createdBySubjectId": OWNER,
        "createdAt": AT,
        "updatedAt": AT,
    }

    runtime = {
        "schemaVersion": "1.0.0",
        "artifact": "BEACON_DEBT_GOLDEN_RUNTIME_INSTANTIATED",
        "state": "IMMUTABLE_LAUNCH_SNAPSHOT_CREATED",
        "fixtureRuntimeStateCreated": True,
        "productionPersistentRuntimeStateCreated": False,
        "launchSnapshotCreated": True,
        "playSequenceExecuted": False,
        "playtestClaim": False,
        "authority": {
            "owner": "PPIA-08 / Stage-A A5 contract fixture authority",
            "productionServiceImplementationAvailable": False,
            "implementationBasis": "Multiversal-app A5 contracts and fixture-backed integration surface",
            "explicitNonClaim": "No production persistence write occurred; this is deterministic governed fixture state.",
        },
        "canonicalSurface": {
            "recordCount": cert["recordCount"],
            "semanticFingerprint": cert["semanticFingerprint"],
            "sourceDigest": cert["sourceDigest"],
        },
        "rulesProfileRef": {
            "ownerDomain": "MRCS/D28",
            "objectId": RULES_ID,
            "objectVersion": RULES_VERSION,
        },
        "campaign": campaign,
        "scenes": scenes,
        "maps": maps,
        "placements": placements,
        "validationReceipt": receipt,
        "launchSnapshot": snapshot,
        "session": session,
        "initialCampaignLocalState": candidate["initialCampaignLocalState"],
        "visibilityState": {
            "policyId": VISIBILITY_ID,
            "policyVersion": "1",
            "truthProjection": candidate["visibilityPolicyCandidate"]["truthProjection"],
            "clueDefault": candidate["visibilityPolicyCandidate"]["clueDefault"],
            "initiallyRevealedClues": [],
            "playerKnowledgeCreated": False,
        },
        "executionBoundary": {
            "nextAllowedOperation": "execute deterministic golden-test play sequence",
            "actionResultsCreated": False,
            "clueDiscoveryEventsCreated": False,
            "postSessionEventsCreated": False,
            "runtimeExecutionAuthorizedByThisArtifact": False,
        },
        "itemCompletionCompatibility": candidate["itemCompletionCompatibility"],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(runtime, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Beacon Debt A5 runtime fixture written: {OUT}")
    print(f"placements={len(placements)} snapshotPlacements={len(gate_placements)}")
    print(f"snapshot={snapshot['snapshotId']} digest={snapshot['contentDigest']}")


if __name__ == "__main__":
    main()
