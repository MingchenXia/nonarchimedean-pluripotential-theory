#!/usr/bin/env python3
"""Reproduce source copies and LF slices from the recorded read-only inputs."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EVIDENCE = ROOT / "evidence"


def main():
    provenance = json.loads((EVIDENCE / "source-provenance.json").read_text())
    for key, entry in provenance.items():
        if key.startswith("LF") or "source" not in entry:
            continue
        source = Path(entry["source"])
        data = source.read_bytes()
        if hashlib.sha256(data).hexdigest() != entry["sha256"]:
            raise RuntimeError(f"Recorded source changed: {key}")
        (ROOT / entry["copy"]).write_bytes(data)
    lines = (EVIDENCE / "BEGZ-primary-original.txt").read_text().split("\n")
    for key, entry in provenance.items():
        if key.startswith("LF"):
            a, z = map(int, key[2:].split("-"))
            data = "\n".join(lines[a - 1:z]).encode()
            assert hashlib.sha256(data).hexdigest() == entry["sha256"]
            (ROOT / entry["copy"]).write_bytes(data)
    original = json.loads((ROOT / "original-input/input.json").read_text())
    strings = {"task.problem": original["task"]["problem"],
               "task.completionCriteria": original["task"]["completionCriteria"],
               "assignment": original["assignment"]}
    (ROOT / "original-input/strings.json").write_text(json.dumps(strings, ensure_ascii=False, indent=2) + "\n")
    for key, value in strings.items():
        (ROOT / "original-input" / (key.replace(".", "-") + ".txt")).write_text(value)
    print("Recorded source hashes and LF slices reproduced; original decoded strings preserved.")


if __name__ == "__main__":
    main()
