#!/usr/bin/env python3
"""Verify deliverable structure and every recorded artifact digest."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent
status = json.loads((root / "status.json").read_text())
assert set(status) == {"id", "status", "exact_result", "proof_file", "concrete_gaps"}
assert status["status"] == "partial" and status["proof_file"] == "P15.2-argument.md"
notes = json.loads((root / "native-notes.json").read_text())
assert notes["candidate"] is False
earlier = set()
for note in notes["notes"]:
    assert set(note) == {"id", "summary", "detailedSummary", "text", "support"}
    assert all(dep in earlier for dep in note["support"])
    earlier.add(note["id"])
manifest = json.loads((root / "artifact-manifest.json").read_text())
for filename, entry in manifest["files"].items():
    data = (root / filename).read_bytes()
    assert len(data) == entry["bytes"]
    assert hashlib.sha256(data).hexdigest() == entry["sha256"]
assert (root / "input.json").read_bytes() == (root / "input-original.json").read_bytes()
build = json.loads((root / "build-audit.json").read_text())
assert build["completed"] and build["successful_tex_passes"] == 2
assert build["overfull_hboxes"] == 0 and not build["undefined_control_sequences"]
main = (root / "P15.2-main.md").read_text()
assert not any(ord(c) < 32 and c != "\n" for c in main)
result = {
    "five_key_partial_status": True, "support_DAG": True,
    "recorded_artifact_hashes": True, "input_byte_preserved": True,
    "final_pdf_two_successful_passes": True, "overfull_boxes": 0,
    "analytic_correctness_established": False,
    "rerun": "python verify_artifacts.py",
}
(root / "final-check.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
