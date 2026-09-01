from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import check_packet as packet  # noqa: E402


class RepairedPacketTests(unittest.TestCase):
    def test_exact_target_and_mathematical_partition(self) -> None:
        packet.check_semantics()
        self.assertEqual(packet.sha256(ROOT / "STATEMENT.tex"), packet.PINS["STATEMENT.tex"])
        self.assertEqual(packet.sha256(ROOT / "PROOF.tex"), packet.PINS["PROOF.tex"])

    def test_pdf_derivatives_routes_and_anchor_lines(self) -> None:
        packet.check_routes()

    def test_lf_only_decoder_retains_form_feed_inside_a_line(self) -> None:
        path = ROOT / "source_pins/BT82_A_new_capacity.txt"
        rows = packet.lf_only_lines_bytes(path)
        self.assertEqual(len(rows), path.read_bytes().count(b"\x0a"))
        self.assertGreater(sum(row.count(b"\x0c") for row in rows), 0)
        self.assertTrue(rows[1107 - 1].startswith(b"    THEOREM 6.9."))

    def test_metadata_has_one_line_numbering_domain(self) -> None:
        blob = (ROOT / "SOURCE_ROUTES.json").read_bytes().lower()
        self.assertNotIn(b"runtime_line", blob)
        self.assertNotIn(b"split" + b"lines", blob)
        checker_blob = (ROOT / "check_packet.py").read_bytes()
        self.assertNotIn(b".split" + b"lines(", checker_blob)

    def test_repair_ledger_and_failed_audit_provenance(self) -> None:
        packet.check_repair_ledger()
        packet.check_nested_sha_ledger(
            ROOT / "audit/PACKET_STAGE_FAIL_AUDIT_v1_20260901",
            packet.PINS["audit/PACKET_STAGE_FAIL_AUDIT_v1_20260901/SHA256SUMS"],
        )


if __name__ == "__main__":
    unittest.main()
