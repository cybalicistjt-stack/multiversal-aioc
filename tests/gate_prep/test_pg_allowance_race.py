#!/usr/bin/env python3
"""GATE-PREP-01: real disposable PG transaction race; seeded fake facts only.
Reuses SA-BILL-05 PostgreSQL fixture rather than duplicating A3 service.
100 competing attempts, at most 24 simultaneous database workers.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "control_plane"))
from test_sa_bill05_postgres import prepare, seed_campaign, issue, count, connect


class GatePrepIsolatedPostgres(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        prepare()
        with connect() as conn:
            version = int(conn.execute("SHOW server_version_num").fetchone()[0])
            assert version >= 150000
            print(f"GATE-PREP-01 real disposable PostgreSQL {version} (not PCV)")

    def test_100_competing_attempts_only_one_durable_allowance(self):
        seed_campaign("gate-prep-campaign", "Raven2")
        def worker(i):
            return issue(campaign="gate-prep-campaign", player="Raven2",
                         command_id=f"gate-prep-unique-{i}")
        with ThreadPoolExecutor(max_workers=24) as pool:
            results = list(pool.map(worker, range(100)))
        self.assertEqual(results.count("ISSUED"), 1, results)
        self.assertEqual(results.count("SLOT_CONFLICT"), 99, results)
        self.assertEqual(count("campaign_allowance_slot",
            "campaign_id='gate-prep-campaign' AND player_subject_id='Raven2'"), 1)
        self.assertEqual(count("allowance_command_receipt",
            "campaign_id='gate-prep-campaign'"), 1)
        self.assertEqual(count("allowance_immutable_event",
            "campaign_id='gate-prep-campaign'"), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
