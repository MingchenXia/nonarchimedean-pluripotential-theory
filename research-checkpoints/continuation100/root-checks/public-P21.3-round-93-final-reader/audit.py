"""Reproducibility checks, not a mathematical verifier."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def main():
    inp = (ROOT / "input.json").read_bytes()
    assert inp == (ROOT / "input-original.json").read_bytes()
    obj = json.loads(inp)
    assert json.loads((ROOT / "task-original.json").read_text(encoding="utf-8")) == obj["task"]
    assert (ROOT / "assignment-original.txt").read_bytes() == obj["assignment"].encode("utf-8")
    manifest = json.loads((ROOT / "source-manifest.json").read_text(encoding="utf-8"))
    for source in manifest["sources"].values():
        assert sha((ROOT / source["file"]).read_bytes()) == source["sha256"]
        assert source["entire_primary_read"] is False
    for unit in manifest["units"]:
        source = manifest["sources"][unit["source"]]
        lines = (ROOT / source["file"]).read_bytes().decode("utf-8").split("\n")
        raw = "\n".join(lines[unit["lf_first"]-1:unit["lf_last_inclusive"]]).encode("utf-8")
        assert raw == (ROOT / unit["file"]).read_bytes()
        assert sha(raw) == unit["sha256"]
    premises = json.loads((ROOT / "premises.json").read_text(encoding="utf-8"))
    assert [p["index"] for p in premises] == list(range(len(premises)))
    for p in premises:
        assert p["passages"]
        for q in p["passages"]:
            assert q["premise"] == p["index"] >= 0
            assert q["url"].startswith("https://arxiv.org/pdf/")
            assert q["lf_first"] <= q["lf_last_inclusive"]
    status = json.loads((ROOT / "status.json").read_text(encoding="utf-8"))
    assert set(status) == {"id", "status", "exact_result", "proof_file", "concrete_gaps"}
    assert status["id"] == "P21.3" and status["status"] == "partial"
    assert (ROOT / status["proof_file"]).exists() and status["concrete_gaps"]
    response = json.loads((ROOT / "notes.json").read_text(encoding="utf-8"))
    assert response["candidate"] is False and len(response["notes"]) <= 4
    seen = set()
    for n in response["notes"]:
        assert set(n) == {"id", "summary", "detailedSummary", "text", "support"}
        assert re.fullmatch(r"n[1-9][0-9]*", n["id"])
        assert all(x in seen for x in n["support"])
        assert all(n[k] for k in ["summary", "detailedSummary", "text"])
        seen.add(n["id"])
    pdf = (ROOT / "P21.3-paper.pdf").read_bytes()
    assert pdf.startswith(b"%PDF-")
    log = (ROOT / "logs/pdflatex-pass2.log").read_text(encoding="utf-8", errors="replace")
    assert "Output written on" in log and "Fatal error" not in log
    notices = [line for line in log.splitlines() if any(x in line for x in ["Overfull", "Underfull", "Warning", "Missing character", "undefined"])]
    files = ["input-original.json", "task-original.json", "assignment-original.txt", "P21.3-core.md", "P21.3-argument.md", "P21.3-paper.tex", "P21.3-paper.pdf", "premises.json", "source-manifest.json", "status.json", "notes.json"]
    hashes = {f: {"bytes": (ROOT/f).stat().st_size, "sha256": sha((ROOT/f).read_bytes())} for f in files}
    (ROOT / "artifact-manifest.json").write_text(json.dumps(hashes, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    result = {"originals_preserved": True, "primary_units_exact": len(manifest["units"]),
              "premise_indices_complete": len(premises), "backward_note_supports_valid": True,
              "status_schema_exact": True, "pdf_compiled": True,
              "compiler_notices": notices, "candidate": False,
              "mathematical_verification": "Not performed by this program; proofs are unverified drafts."}
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
