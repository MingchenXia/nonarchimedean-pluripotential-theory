#!/usr/bin/env python3
"""Preserve the frozen packet, run small diagnostics, and compile exactly twice."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
BUILD = ROOT / "build"

def save_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def main():
    BUILD.mkdir(exist_ok=True)
    log = []
    def run(argv, label):
        result = subprocess.run(argv, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (BUILD / f"{label}.stdout.txt").write_text(result.stdout)
        (BUILD / f"{label}.stderr.txt").write_text(result.stderr)
        log.append({"label": label, "argv": argv, "cwd": str(ROOT), "returncode": result.returncode,
                    "stdout": f"build/{label}.stdout.txt", "stderr": f"build/{label}.stderr.txt"})
        save_json(ROOT / "run-log.json", log)
        if result.returncode:
            print(result.stdout[-6000:])
            print(result.stderr[-3000:], file=sys.stderr)
            raise RuntimeError(f"{label} failed: {result.returncode}")
        return result
    run([sys.executable, "preserve.py"], "preserve")
    status = json.loads((ROOT / "status.json").read_text())
    assert set(status) == {"id", "status", "exact_result", "proof_file", "concrete_gaps"}
    assert status["status"] == "PARTIAL" and len(status["concrete_gaps"]) == 3
    result_path = ROOT / "result.json"
    if result_path.exists():
        result = json.loads(result_path.read_text())
        earlier = set()
        for note in result["notes"]:
            assert set(note) == {"id", "summary", "detailedSummary", "text", "support"}
            assert set(note["support"]) <= earlier
            assert note["id"] not in earlier
            earlier.add(note["id"])
        assert result["candidate"] is False
    run([sys.executable, "checks.py"], "checks")
    for executable in ("pdflatex", "pandoc"):
        run([executable, "--version"], f"{executable}-version")
    run(["pandoc", "P16.5-argument.md", "--standalone", "--to=latex",
         "--output=P16.5-paper.tex"], "pandoc")
    for pass_number in (1, 2):
        run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
             "-output-directory=build", "P16.5-paper.tex"], f"pdflatex-pass-{pass_number}")
        for extension in ("log", "aux", "out"):
            source = BUILD / f"P16.5-paper.{extension}"
            if source.exists():
                (BUILD / f"pdflatex-pass-{pass_number}.{extension}").write_bytes(source.read_bytes())
    diagnostics = {}
    for pass_number in (1, 2):
        lines = (BUILD / f"pdflatex-pass-{pass_number}.log").read_text(errors="replace").splitlines()
        diagnostics[str(pass_number)] = {"warnings": [line for line in lines if any(x in line for x in
                                                  ("Warning", "Overfull", "Underfull", "Undefined", "Error"))],
                                         "output": [line for line in lines if "Output written" in line]}
    save_json(BUILD / "diagnostics.json", diagnostics)
    hashes = {}
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and path.name != "artifact-hashes.json":
            hashes[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    save_json(ROOT / "artifact-hashes.json", hashes)
    print(json.dumps({"status": "rerun completed", "candidate": False,
                      "pdf": "build/P16.5-paper.pdf", "tex_passes": 2,
                      "diagnostics": diagnostics}, ensure_ascii=False))

if __name__ == "__main__":
    main()
