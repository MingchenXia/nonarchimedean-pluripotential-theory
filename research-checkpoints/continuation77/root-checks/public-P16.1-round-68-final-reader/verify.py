"""Verify preservation, provenance, output schema and successful document builds."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
checks = []

def check(label, predicate):
    checks.append({"check": label, "passed": bool(predicate)})
    if not predicate:
        raise AssertionError(label)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    source = ROOT / "input.json"
    original = ROOT / "input-original.json"
    check("input byte identity", source.read_bytes() == original.read_bytes())
    data = json.loads(source.read_text())
    check("assignment value identity", (ROOT / "assignment-original.txt").read_text() == data["assignment"])
    check("task value identity", json.loads((ROOT / "task-original.json").read_text()) == data["task"])
    status = json.loads((ROOT / "status.json").read_text())
    check("exact five-key status schema", set(status) == {"id", "status", "exact_result", "proof_file", "concrete_gaps"})
    check("partial disposition", status["id"] == "P16.1" and status["status"] == "partial" and len(status["concrete_gaps"]) == 4)
    check("proof exists", (ROOT / status["proof_file"]).is_file())
    provenance = json.loads((ROOT / "source-extracts/source-provenance.json").read_text())
    check("ten permitted primary sources", len(provenance["sources"]) == 10)
    excerpt_count = 0
    for record in provenance["sources"]:
        sid = record["id"]
        for kind, item in record["files"].items():
            check(f"{sid}:{kind} hash", digest(ROOT/item["local_copy"]) == item["sha256"])
            check(f"{sid}:{kind} supplied match", item["matches_supplied"])
        literal_file = ROOT / record["files"]["literal_extract"]["local_copy"]
        lines = literal_file.read_text().split("\n")
        check(f"{sid} LF split count", len(lines) == record["LF_split_count"])
        for e in record["literal_statements_and_proof_bodies"]:
            lo, hi = e["start_LF"], e["end_LF"]
            expected = "\n".join(lines[lo-1:hi])
            check(f"{sid} LF{lo}-{hi} literal", e["literal"] == expected)
            check(f"{sid} LF{lo}-{hi} file", (ROOT/e["artifact"]).read_text() == expected)
            check(f"{sid} LF{lo}-{hi} hash", hashlib.sha256(expected.encode()).hexdigest() == e["literal_sha256"])
            check(f"{sid} LF{lo}-{hi} scope", bool(e["application_scope"]["checked_applications"]) and bool(e["application_scope"]["concrete_limits"]))
            excerpt_count += 1
    check("excerpt count", excerpt_count == provenance["excerpt_count"])
    notes = json.loads((ROOT / "notes.json").read_text())
    check("canonical output keys", set(notes) == {"notes", "candidate"})
    check("candidate false", notes["candidate"] is False)
    check("at most four nonempty notes", 1 <= len(notes["notes"]) <= 4)
    earlier = set()
    for i, note in enumerate(notes["notes"], 1):
        check(f"note n{i} id", note["id"] == f"n{i}")
        check(f"note n{i} schema", set(note) == {"id", "summary", "detailedSummary", "text", "support"})
        check(f"note n{i} earlier-only support", set(note["support"]) <= earlier)
        check(f"note n{i} prose", all(isinstance(note[k], str) and note[k] for k in ("summary", "detailedSummary", "text")))
        earlier.add(note["id"])
    build = json.loads((ROOT/"build-results.json").read_text())
    check("Pandoc and two TeX builds", len(build["commands"]) == 3 and build["success"])
    for command in build["commands"]:
        label = command["label"]
        check(f"{label} return code", command["returncode"] == 0)
        check(f"{label} stdout exists", (ROOT/command["stdout"]).is_file())
        check(f"{label} stderr exists", (ROOT/command["stderr"]).is_file())
    for number in (1, 2):
        log = ROOT/f"tex-run-{number}.log"
        check(f"TeX separate log {number}", log.is_file() and "Output written on" in log.read_text())
    check("standalone TeX", "\\documentclass" in (ROOT/"P16.1-paper.tex").read_text() and "\\begin{document}" in (ROOT/"P16.1-paper.tex").read_text())
    check("PDF build hash", digest(ROOT/"P16.1-paper.pdf") == build["pdf_sha256"])
    check("finite illustration checks", json.loads((ROOT/"algebra-checks.json").read_text())["passed"])
    result = {
        "all_passed": True, "check_count": len(checks), "checks": checks,
        "input_sha256": digest(source), "argument_sha256": digest(ROOT/"P16.1-argument.md"),
        "tex_sha256": digest(ROOT/"P16.1-paper.tex"), "pdf_sha256": digest(ROOT/"P16.1-paper.pdf"),
        "source_files_verified": sum(len(s["files"]) for s in provenance["sources"]), "literal_excerpts": excerpt_count,
        "scope": "Integrity, schema, finite illustrations and execution only. This is not an independent mathematical correctness or novelty check."
    }
    (ROOT/"verification.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: result[k] for k in ("all_passed", "check_count", "input_sha256", "literal_excerpts", "source_files_verified")}))

if __name__ == "__main__":
    main()
