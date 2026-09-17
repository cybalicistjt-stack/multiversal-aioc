#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_RECORD_COUNT = 526
REQUIRED_IDS = {
    "mv.setting.faction.administrative-syndicate",
    "mv.setting.faction.black-feathers",
    "mv.adventure.beacon-debt.module",
    "mv.adventure.beacon-debt.investigation.maps-as-leverage",
    "mv.adventure.beacon-debt.clue.cf06-black-feathers-association-evidence",
    "mv.adventure.beacon-debt.rules.golden-test-core",
    "mv.adventure.beacon-debt.action.navigate-crossflow",
    "mv.adventure.beacon-debt.action.restore-route-beacon",
    "mv.adventure.beacon-debt.action.request-priority-exception",
}


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def iter_refs(value):
    if isinstance(value, dict):
        if "objectId" in value:
            yield value
        for child in value.values():
            yield from iter_refs(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_refs(child)


def main() -> None:
    run("node", "scripts/materialize-content-source.mjs")
    run("node", "scripts/build-canonical-content-database.mjs")
    run("node", "scripts/certify-canonical-content-pipeline.mjs")

    index = json.loads((ROOT / "content-db" / "index.json").read_text(encoding="utf-8"))
    certificate = json.loads((ROOT / "content-db" / "certification.json").read_text(encoding="utf-8"))

    assert index["recordCount"] == EXPECTED_RECORD_COUNT, (
        f"expected {EXPECTED_RECORD_COUNT} effective canonical records; found {index['recordCount']}"
    )
    assert certificate["recordCount"] == EXPECTED_RECORD_COUNT
    assert certificate["baselineRecordCount"] == 487
    assert certificate["appendedRecordCount"] == 39
    assert certificate["replacementRecordCount"] == 8
    assert certificate["supplementalInputRecordCount"] == 47
    assert certificate["gameReadiness"]["assessed"] is False
    assert "not-game-readiness" in certificate["certificationScope"]
    assert (ROOT / "content-db" / "content-record.schema.json").exists(), "clean rebuild must preserve the record schema"

    by_id = {record["stableId"]: record for record in index["records"]}
    missing = sorted(REQUIRED_IDS - set(by_id))
    assert not missing, f"required canonical records missing from generated database: {missing}"

    admin = by_id["mv.setting.faction.administrative-syndicate"]
    assert admin["contentVersion"] == "1.0.0"

    expected_versions = {
        "mv.setting.faction-relationship.administrative-syndicate-east-gate": "1.0.1",
        "mv.setting.faction-relationship.lantern-compact-administrative-syndicate": "1.0.1",
        "mv.setting.vertigon.hazard.transit-crossflow-cascade": "1.0.1",
        "mv.adventure.beacon-debt.npc.mira-venn": "1.0.1",
        "mv.adventure.beacon-debt.social-situation.east-gate-priority": "1.0.2",
        "mv.adventure.beacon-debt.module": "1.0.2",
    }
    for stable_id, version in expected_versions.items():
        assert by_id[stable_id]["contentVersion"] == version, f"{stable_id} must resolve at {version}"
        assert by_id[stable_id]["provenance"]["sourceClass"] == "replacement"

    assert by_id["mv.setting.faction-relationship.administrative-syndicate-east-gate"]["provenance"]["replaces"]["contentVersion"] == "1.0.0"
    assert by_id["mv.setting.faction-relationship.lantern-compact-administrative-syndicate"]["provenance"]["replaces"]["contentVersion"] == "1.0.0"
    assert by_id["mv.setting.vertigon.hazard.transit-crossflow-cascade"]["provenance"]["replaces"]["contentVersion"] == "1.0.0"
    assert by_id["mv.adventure.beacon-debt.npc.mira-venn"]["provenance"]["replaces"]["contentVersion"] == "1.0.0"
    assert by_id["mv.adventure.beacon-debt.social-situation.east-gate-priority"]["provenance"]["replaces"]["contentVersion"] == "1.0.1"
    assert by_id["mv.adventure.beacon-debt.module"]["provenance"]["replaces"]["contentVersion"] == "1.0.1"

    beacon_ids = [sid for sid in by_id if sid.startswith("mv.adventure.beacon-debt") or sid.startswith("mv.setting.vertigon") or sid.startswith("mv.setting.faction-relationship") or sid in {"mv.faction.lantern-compact", "mv.setting.faction.black-feathers"}]
    unresolved_admin_refs = []
    for stable_id in beacon_ids:
        for ref in iter_refs(by_id[stable_id]["gameObject"]):
            if ref.get("objectId") == "mv.setting.faction.administrative-syndicate" and ref.get("objectVersion") != "1.0.0":
                unresolved_admin_refs.append((stable_id, ref))
    assert not unresolved_admin_refs, f"Administrative Syndicate references remain unresolved: {unresolved_admin_refs}"

    print(
        "Canonical content pipeline reconciliation PASS: "
        f"{index['recordCount']} effective records; 39 appends + 8 governed replacements; Beacon Debt mechanics and exact references resolve."
    )


if __name__ == "__main__":
    main()
