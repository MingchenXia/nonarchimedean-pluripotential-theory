#!/usr/bin/env python3
"""Administrative checks and exactly two builds; not a mathematical verifier."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent
CHECKS = ROOT / "checks"
CHECKS.mkdir(exist_ok=True)
data = json.loads((ROOT / "input.json").read_text())
assert (ROOT / "input.json").read_bytes() == (ROOT / "input-original.json").read_bytes()
assert json.loads((ROOT / "task-original.json").read_text()) == data["task"]
assert (ROOT / "assignment-original.txt").read_text() == data["assignment"] + "\n"
status = json.loads((ROOT / "status.json").read_text())
assert set(status) == {"id", "status", "exact_result", "proof_file", "concrete_gaps"}
assert status["status"] == "partial"
assert status["concrete_gaps"]
subprocess.run(["python", "make_paper.py"], cwd=ROOT, check=True)
tex = (ROOT / "P03.3-paper.tex").read_text()
assert "\\input{" not in tex and "\\include{" not in tex
assert all(x in tex for x in ("Finite Galois", "projective", "type-4", "counterexample"))
builds = []
for pass_number in (1, 2):
    cmd = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "P03.3-paper.tex"]
    cp = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    (CHECKS / f"tex-pass-{pass_number}.stdout.txt").write_text(cp.stdout + cp.stderr)
    logpath = ROOT / "P03.3-paper.log"
    log = logpath.read_text(errors="replace") if logpath.exists() else ""
    (CHECKS / f"tex-pass-{pass_number}.log").write_text(log)
    builds.append(dict(pass_number=pass_number, command=cmd, exit_code=cp.returncode,
                       warnings=[s for s in log.splitlines()
                                 if "Warning" in s or "Overfull" in s or s.startswith("!")],
                       output=[s for s in cp.stdout.splitlines() if "Output written" in s]))
result = dict(input_original_byte_equal=True, task_object_equal=True, assignment_string_equal=True,
              status_exact_keys=True, standalone_tex=True,
              input_sha256=hashlib.sha256((ROOT / "input.json").read_bytes()).hexdigest(),
              builds=builds, mathematical_verification=False)
(CHECKS / "deliverable-checks.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
if any(b["exit_code"] for b in builds):
    raise SystemExit(1)
