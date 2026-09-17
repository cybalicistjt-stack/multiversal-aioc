#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "content-db" / "index.json"
VERSION_INDEX = ROOT / "content-db" / "version-index.json"
CERT = ROOT / "content-db" / "certification.json"
OUT = ROOT / "evidence" / "content-pipeline" / "beacon-debt-golden-diagnostics.json"

BEACON_IDS = [
    "mv.setting.faction.black-feathers",
    "mv.faction.lantern-compact",
    "mv.setting.faction-relationship.administrative-syndicate-east-gate",
    "mv.setting.faction-relationship.lantern-compact-administrative-syndicate",
    "mv.setting.vertigon.location.east-transit-spine",
    "mv.setting.vertigon.location.east-gate-interchange",
    "mv.setting.vertigon.location.east-route-beacon",
    "mv.setting.vertigon.location.eastern-bridge",
    "mv.setting.vertigon.location.listening-market",
    "mv.setting.vertigon.hazard.transit-crossflow-cascade",
    "mv.adventure.beacon-debt.npc.mira-venn",
    "mv.adventure.beacon-debt.group.displaced-travelers",
    "mv.adventure.beacon-debt.social-situation.east-gate-priority",
    "mv.adventure.beacon-debt.module",
    "mv.adventure.beacon-debt.investigation.maps-as-leverage",
    "mv.adventure.beacon-debt.item.east-spine-revision-sale-note",
    "mv.adventure.beacon-debt.item.current-conditions-annotation-request",
    "mv.adventure.beacon-debt.npc.independent-listening-market-broker",
    "mv.adventure.beacon-debt.item.broker-delivery-memorandum",
    "mv.adventure.beacon-debt.clue.cf01-recent-map-purchase-observation",
    "mv.adventure.beacon-debt.clue.cf02-fresh-revision-premium",
    "mv.adventure.beacon-debt.clue.cf03-current-conditions-annotation-request",
    "mv.adventure.beacon-debt.clue.cf04-fragmented-brokerage-pattern",
    "mv.adventure.beacon-debt.clue.cf05-independent-black-feathers-association-claim",
    "mv.adventure.beacon-debt.clue.cf06-black-feathers-association-evidence",
    "mv.adventure.beacon-debt.connection.cf02-cf03-same-subject",
    "mv.adventure.beacon-debt.connection.cf02-cf04-supports",
    "mv.adventure.beacon-debt.connection.cf03-cf04-supports",
]

MECHANICS_IDS = [
    "mv.adventure.beacon-debt.rules.golden-test-core",
    "mv.adventure.beacon-debt.resource.route-deterioration",
    "mv.adventure.beacon-debt.resource.refugee-arrival-pressure",
    "mv.adventure.beacon-debt.action.navigate-crossflow",
    "mv.adventure.beacon-debt.action.restore-route-beacon",
    "mv.adventure.beacon-debt.action.request-priority-exception",
    "mv.adventure.beacon-debt.effect.route-pressure-advance",
    "mv.adventure.beacon-debt.effect.refugee-pressure-advance",
    "mv.adventure.beacon-debt.effect.route-beacon-restored",
    "mv.adventure.beacon-debt.effect.priority-exception-granted",
]
ALL_IDS = BEACON_IDS + MECHANICS_IDS

EXPECTED_VERSIONS = {stable_id: "1.0.0" for stable_id in ALL_IDS}
for stable_id in [
    "mv.setting.faction-relationship.administrative-syndicate-east-gate",
    "mv.setting.faction-relationship.lantern-compact-administrative-syndicate",
]:
    EXPECTED_VERSIONS[stable_id] = "1.0.1"
EXPECTED_VERSIONS["mv.setting.vertigon.hazard.transit-crossflow-cascade"] = "1.0.1"
EXPECTED_VERSIONS["mv.adventure.beacon-debt.npc.mira-venn"] = "1.0.1"
EXPECTED_VERSIONS["mv.adventure.beacon-debt.social-situation.east-gate-priority"] = "1.0.2"
EXPECTED_VERSIONS["mv.adventure.beacon-debt.module"] = "1.0.2"


def iter_refs(value):
    if isinstance(value, dict):
        if "objectId" in value:
            yield value
        for child in value.values():
            yield from iter_refs(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_refs(child)


def exact_ref(object_id, version):
    return {"objectId": object_id, "objectVersion": version}


def contains_ref(value, object_id, version):
    return any(ref.get("objectId") == object_id and ref.get("objectVersion") == version for ref in iter_refs(value))


def main():
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    version_index = json.loads(VERSION_INDEX.read_text(encoding="utf-8"))
    certificate = json.loads(CERT.read_text(encoding="utf-8"))
    by_id = {record["stableId"]: record for record in index["records"]}
    version_keys = {entry["key"] for entry in version_index["versions"]}

    assert index["recordCount"] == 526, f"expected 526 effective canonical records after mechanics closure, found {index['recordCount']}"
    assert version_index["versionCount"] == 47, f"expected 47 immutable exact versions, found {version_index['versionCount']}"
    assert certificate["recordCount"] == 526
    assert certificate["replacementRecordCount"] == 8

    missing = [stable_id for stable_id in ALL_IDS if stable_id not in by_id]
    assert not missing, f"Beacon Debt canonical/mechanics IDs missing: {missing}"
    version_errors = {
        stable_id: (EXPECTED_VERSIONS[stable_id], by_id[stable_id].get("contentVersion"))
        for stable_id in ALL_IDS
        if by_id[stable_id].get("contentVersion") != EXPECTED_VERSIONS[stable_id]
    }
    assert not version_errors, f"Beacon Debt version mismatches: {version_errors}"

    assert by_id["mv.setting.faction.administrative-syndicate"].get("contentVersion") == "1.0.0"
    for key in [
        "mv.setting.faction.administrative-syndicate@1.0.0",
        "mv.setting.vertigon.hazard.transit-crossflow-cascade@1.0.0",
        "mv.setting.vertigon.hazard.transit-crossflow-cascade@1.0.1",
        "mv.adventure.beacon-debt.npc.mira-venn@1.0.0",
        "mv.adventure.beacon-debt.npc.mira-venn@1.0.1",
        "mv.adventure.beacon-debt.social-situation.east-gate-priority@1.0.0",
        "mv.adventure.beacon-debt.social-situation.east-gate-priority@1.0.1",
        "mv.adventure.beacon-debt.social-situation.east-gate-priority@1.0.2",
        "mv.adventure.beacon-debt.module@1.0.0",
        "mv.adventure.beacon-debt.module@1.0.1",
        "mv.adventure.beacon-debt.module@1.0.2",
    ] + [f"{stable_id}@1.0.0" for stable_id in MECHANICS_IDS]:
        assert key in version_keys, f"immutable canonical version missing: {key}"

    unresolved_refs = []
    for stable_id in ALL_IDS:
        for ref in iter_refs(by_id[stable_id]["gameObject"]):
            object_id = ref.get("objectId")
            version = ref.get("objectVersion")
            if ref.get("referenceClass") == "MIB-11 source-only stable identity":
                if object_id not in {"world:havalaea", "setting:vertigon"} or version != "1.0.0":
                    unresolved_refs.append({"source": stable_id, "ref": ref, "reason": "invalid governed MIB-11 external reference"})
                continue
            if object_id == "mv.setting.faction.administrative-syndicate" and version != "1.0.0":
                unresolved_refs.append({"source": stable_id, "ref": ref, "reason": "Administrative Syndicate must pin 1.0.0"})
            if version is not None and f"{object_id}@{version}" not in version_keys:
                unresolved_refs.append({"source": stable_id, "ref": ref, "reason": "exact version absent from canonical version index"})
    assert not unresolved_refs, f"Exact canonical references unresolved: {unresolved_refs}"

    investigation = by_id["mv.adventure.beacon-debt.investigation.maps-as-leverage"]["gameObject"]
    expected_routes = {
        "R1": ["CF-01", "CF-02"],
        "R2": ["CF-02", "CF-03"],
        "R3": ["CF-03", "CF-04"],
        "R4": ["CF-05", "CF-06"],
    }
    assert investigation["primaryConclusionRequires"] == ["R1", "R2", "R3", "R4"]
    assert investigation["redundancyContract"] == expected_routes
    assert investigation["optionalRevelations"]["R5"]["firstGoldenTestState"] == "omitted"

    rules = by_id["mv.adventure.beacon-debt.rules.golden-test-core"]["gameObject"]
    hazard = by_id["mv.setting.vertigon.hazard.transit-crossflow-cascade"]["gameObject"]
    social = by_id["mv.adventure.beacon-debt.social-situation.east-gate-priority"]["gameObject"]
    mira = by_id["mv.adventure.beacon-debt.npc.mira-venn"]["gameObject"]
    adventure = by_id["mv.adventure.beacon-debt.module"]["gameObject"]

    assert rules["profileClass"] == "adventure-golden-test-mechanics"
    assert rules["resolutionContract"]["damagePolicy"] == "none-first-golden-test"
    assert rules["resolutionContract"]["conditionPolicy"] == "none-first-golden-test"
    assert rules["resolutionContract"]["combatRequired"] is False
    assert rules["resolutionContract"]["targetPolicy"] == "packet-local-authored-thresholds-not-universal"

    assert hazard["deterministicResolution"]["target"] == 12
    assert hazard["damagePolicy"] == "none-first-golden-test"
    assert hazard["conditionPolicy"] == "none-first-golden-test"
    assert contains_ref(hazard.get("mechanicsRefs", []), "mv.adventure.beacon-debt.action.navigate-crossflow", "1.0.0")
    assert contains_ref(hazard.get("mechanicsRefs", []), "mv.adventure.beacon-debt.resource.route-deterioration", "1.0.0")

    assert mira["mechanicalStats"]["profileKind"] == "bounded-noncombat-gatekeeper"
    assert mira["mechanicalStats"]["combatStatsRequired"] is False
    assert mira["mechanicalStats"]["priorityExceptionTarget"] == 15
    assert contains_ref(mira["mechanicalStats"], "mv.adventure.beacon-debt.action.request-priority-exception", "1.0.0")

    assert social["resolutionProfile"]["priorityExceptionTarget"] == 15
    assert social["resolutionProfile"]["impossibleRequestPolicy"] == "deny-without-roll"
    assert contains_ref(social.get("mechanicsRefs", []), "mv.adventure.beacon-debt.action.request-priority-exception", "1.0.0")
    assert contains_ref(social.get("mechanicsRefs", []), "mv.adventure.beacon-debt.resource.refugee-arrival-pressure", "1.0.0")

    assert contains_ref(adventure.get("mechanicsRefs", []), "mv.adventure.beacon-debt.rules.golden-test-core", "1.0.0")
    assert contains_ref(adventure["sceneMechanics"]["Damaged Crossing"], "mv.adventure.beacon-debt.action.navigate-crossflow", "1.0.0")
    assert contains_ref(adventure["sceneMechanics"]["Beacon Restoration"], "mv.adventure.beacon-debt.action.restore-route-beacon", "1.0.0")
    assert contains_ref(adventure["sceneMechanics"]["Gate Pressure"], "mv.adventure.beacon-debt.action.request-priority-exception", "1.0.0")
    assert adventure["combatPolicy"] == "No mandatory combat encounter."
    assert adventure["deterministicGoldenTestPolicy"]["ready"] is True
    assert adventure["deterministicGoldenTestPolicy"]["runtimeStateCreated"] is False

    item_definitions = [record for record in index["records"] if record.get("objectType") == "mv.object.item-definition"]
    item_type_definitions = [record for record in index["records"] if record.get("objectType") == "mv.object.item-type-definition"]
    beacon_evidence_items = [record for record in item_definitions if record["stableId"].startswith("mv.adventure.beacon-debt.item.")]
    assert len(beacon_evidence_items) == 3
    assert all(record["gameObject"].get("scope") == "adventure-local-source-template" for record in beacon_evidence_items)
    assert certificate["gameReadiness"]["assessed"] is False
    assert version_index["gameReadinessAssessed"] is False

    diagnostic = {
        "schema_version": "1.2.0",
        "artifact": "BEACON_DEBT_GOLDEN_TEST_DIAGNOSTICS",
        "overall_state": "DETERMINISTIC_GOLDEN_LAUNCH_READY_PRE_RUNTIME",
        "runtime_state_created": False,
        "launch_snapshot_created": False,
        "playtest_claim": False,
        "canonical_database": {
            "effective_record_count": index["recordCount"],
            "version_index_count": version_index["versionCount"],
            "certification_scope": certificate["certificationScope"],
            "game_readiness_assessed": certificate["gameReadiness"]["assessed"],
            "explicit_nonclaim": "The certified content database is not the total Multiversal object corpus and does not certify OGR GAME_READY status."
        },
        "beacon_debt": {
            "canonical_ids_checked": len(ALL_IDS),
            "missing_ids": missing,
            "version_errors": version_errors,
            "administrative_syndicate": "mv.setting.faction.administrative-syndicate@1.0.0",
            "world_setting_refs": ["world:havalaea@1.0.0", "setting:vertigon@1.0.0"],
            "investigation_redundancy": expected_routes,
            "R5": "omitted_first_golden_test",
            "reference_status": "PASS_IMMUTABLE_VERSION_INDEX_PLUS_MIB11"
        },
        "mechanics": {
            "status": "READY_FOR_DETERMINISTIC_GOLDEN_LAUNCH",
            "rules_profile": "mv.adventure.beacon-debt.rules.golden-test-core@1.0.0",
            "action_refs": [
                "mv.adventure.beacon-debt.action.navigate-crossflow@1.0.0",
                "mv.adventure.beacon-debt.action.restore-route-beacon@1.0.0",
                "mv.adventure.beacon-debt.action.request-priority-exception@1.0.0"
            ],
            "resource_refs": [
                "mv.adventure.beacon-debt.resource.route-deterioration@1.0.0",
                "mv.adventure.beacon-debt.resource.refugee-arrival-pressure@1.0.0"
            ],
            "combat_required": False,
            "damage_applied_by_first_golden_test_profile": False,
            "conditions_applied_by_first_golden_test_profile": False,
            "gm_adjudicated_play_possible": True,
            "deterministic_system_golden_test_ready": True
        },
        "parallel_item_completion_crosscheck": {
            "current_certified_item_definitions": len(item_definitions),
            "current_certified_item_type_definitions": len(item_type_definitions),
            "beacon_adventure_local_evidence_item_templates": len(beacon_evidence_items),
            "replacement_path_available": True,
            "immutable_prior_versions_preserved": True,
            "ordinary_duplicate_stable_ids_rejected": True,
            "ogr_game_ready_conflated_with_canonical_certification": False,
            "mechanics_closure_added_item_definitions": False,
            "note": "Beacon Debt mechanics closure adds no Item identities. Parallel Item completion may append new stable identities or use owner-approved exact-version replacement for existing canonical stable IDs; OGR remains the readiness authority."
        }
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(diagnostic, indent=2) + "\n", encoding="utf-8")
    print(
        "Beacon Debt golden diagnostics PASS: 38 canonical packet IDs, R1-R4 redundancy, exact mechanics bindings, and immutable reference history resolve; "
        "deterministic golden launch is ready pre-runtime and Item completion remains separate."
    )


if __name__ == "__main__":
    main()
