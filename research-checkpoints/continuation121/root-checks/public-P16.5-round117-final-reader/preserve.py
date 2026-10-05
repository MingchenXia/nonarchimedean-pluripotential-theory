#!/usr/bin/env python3
"""Extract only the supplied input. Historical paths are never dereferenced."""
from pathlib import Path
import hashlib
import json
import platform
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parent

def save_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def main():
    raw = (ROOT / "input.json").read_bytes()
    data = json.loads(raw)
    original = ROOT / "input-original.json"
    if original.exists() and original.read_bytes() != raw:
        raise RuntimeError("The original input and current input differ")
    original.write_bytes(raw)
    assignment = data["assignment"]
    (ROOT / "assignment-original.txt").write_text(assignment, encoding="utf-8")
    save_json(ROOT / "task-original.json", data["task"])
    evidence = ROOT / "evidence"
    evidence.mkdir(exist_ok=True)
    index = []
    pattern = r"BEGIN MATHEMATICAL DATA: ([^\n]*)\n(.*?)\nEND MATHEMATICAL DATA"
    for i, match in enumerate(re.finditer(pattern, assignment, re.S)):
        body = match.group(2)
        path = evidence / f"block-{i:03d}.txt"
        path.write_text(body, encoding="utf-8")
        index.append({"index": i, "label": match.group(1), "path": str(path.relative_to(ROOT)),
                      "assignment_character_start": match.start(2),
                      "assignment_character_end": match.end(2),
                      "sha256": hashlib.sha256(body.encode()).hexdigest(), "characters": len(body)})
    save_json(evidence / "block-index.json", index)
    heading = "## Actual completed full-original independent review114\n"
    start = assignment.index(heading) + len(heading)
    review = json.JSONDecoder().raw_decode(assignment[start:])[0]
    save_json(evidence / "review114.json", review)
    save_json(evidence / "review-discrepancy.json", {
        "review_verdict": review["verdict"], "passage_count": len(review["passages"]),
        "premise_count": len(review["premises"]),
        "actual_passage_premise_indices": sorted({x["premise"] for x in review["passages"]}),
        "report_mentions_minus_one": "−1" in review["report"] or "-1" in review["report"],
        "minus_one_actual_passages": [x for x in review["passages"] if x["premise"] == -1],
        "rule": "Preserve actual objects; do not create a missing task quotation."})
    dictionary_record = next(x for x in index if x["label"] == "Whole68 primary proof-body dictionary of G0")
    dictionary = json.loads((ROOT / dictionary_record["path"]).read_text())
    unit_dir = evidence / "G0-dictionary"
    unit_dir.mkdir(exist_ok=True)
    units = []
    for i, (key, body) in enumerate(dictionary.items()):
        path = unit_dir / f"unit-{i:03d}.txt"
        path.write_text(body, encoding="utf-8")
        units.append({"index": i, "supplied_key": key, "path": str(path.relative_to(ROOT)),
                      "sha256": hashlib.sha256(body.encode()).hexdigest(), "characters": len(body)})
    save_json(unit_dir / "index.json", units)
    save_json(ROOT / "preservation.json", {
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "input_original_sha256": hashlib.sha256(original.read_bytes()).hexdigest(),
        "byte_identical": original.read_bytes() == raw,
        "assignment_utf8_roundtrip": (ROOT / "assignment-original.txt").read_text() == assignment,
        "task_value_identical": json.loads((ROOT / "task-original.json").read_text()) == data["task"]})
    save_json(ROOT / "environment.json", {
        "python": sys.version, "platform": platform.platform(), "cwd": str(ROOT),
        "source_access": "Frozen input only; no historical paths dereferenced",
        "supervised_compute": "No facility supplied; no resource-heavy computation used",
        "executables": {x: shutil.which(x) for x in ("python3", "pdflatex", "pandoc", "latexmk")}})
    print(json.dumps({"preserved_input_bytes": len(raw), "extracted_blocks": len(index),
                      "dictionary_units": len(units), "verdict": review["verdict"]}))

if __name__ == "__main__":
    main()
