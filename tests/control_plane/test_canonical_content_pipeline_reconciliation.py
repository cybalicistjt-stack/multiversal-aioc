#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_RECORD_COUNT = 516
REQUIRED_IDS = {
    "mv.setting.faction.administrative-syndicate",
    "mv.setting.faction.black-feathers",
    "mv.adventure.beacon-debt.module",
    "mv.adventure.beacon-debt.investigation.maps-as-leverage",
    "mv.adventure.beacon-debt.clue.cf06-black-feathers-association-evidence",
}


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def main() -> None:
    run("node", "scripts/materialize-content-source.mjs")
    run("node", "scripts/build-canonical-content-database.mjs")
    run("node", "scripts/certify-canonical-content-pipeline.mjs")

    index = json.loads((ROOT / "content-db" / "index.json").read_text(encoding="utf-8"))
    certificate = json.loads((ROOT / "content-db" / "certification.json").read_text(encoding="utf-8"))

    assert index["recordCount"] == EXPECTED_RECORD_COUNT, (
        f"expected {EXPECTED_RECORD_COUNT} canonical records after baseline + supplemental ingestion; "
        f"found {index['recordCount']}"
    )
    assert certificate["recordCount"] == EXPECTED_RECORD_COUNT, (
        f"certificate must cover all {EXPECTED_RECORD_COUNT} canonical records; "
        f"found {certificate['recordCount']}"
    )

    by_id = {record["stableId"]: record for record in index["records"]}
    missing = sorted(REQUIRED_IDS - set(by_id))
    assert not missing, f"required canonical records missing from generated database: {missing}"

    admin = by_id["mv.setting.faction.administrative-syndicate"]
    assert admin["contentVersion"] == "1.0.0", "Administrative Syndicate must expose objectVersion/contentVersion 1.0.0"
    assert admin["gameObject"]["id"] == "mv.setting.faction.administrative-syndicate"

    beacon = by_id["mv.adventure.beacon-debt.module"]
    assert beacon["contentVersion"] == "1.0.0"

    print(
        "Canonical content pipeline reconciliation PASS: "
        f"{index['recordCount']} records; Administrative Syndicate and Beacon Debt resolve."
    )


if __name__ == "__main__":
    main()
