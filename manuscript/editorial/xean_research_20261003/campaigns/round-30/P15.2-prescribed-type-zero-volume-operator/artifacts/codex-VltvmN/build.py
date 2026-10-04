#!/usr/bin/env python3
"""Rerun the source audit, coefficient diagnostic, and two TeX compilation passes."""
from pathlib import Path
import hashlib
import json
import subprocess
import time

ROOT = Path(__file__).resolve().parent
steps = [
    ["python", "audit_and_assemble.py"],
    ["python", "coefficient_check.py"],
    ["pandoc", "P15.2-main.md", "-f",
     "markdown+tex_math_single_backslash+tex_math_dollars", "-t", "latex", "-s",
     "-V", "geometry:margin=24mm", "-V", "fontsize=10pt", "-o", "P15.2-partial.tex"],
    ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "P15.2-partial.tex"],
    ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "P15.2-partial.tex"],
    ["pdftotext", "-layout", "P15.2-partial.pdf", "P15.2-pdf-text.txt"],
    ["pdfinfo", "P15.2-partial.pdf"],
]
records = []
for index, command in enumerate(steps, 1):
    started = time.monotonic()
    run = subprocess.run(command, cwd=ROOT, text=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    filename = f"build-step-{index:02d}.txt"
    (ROOT / filename).write_text(run.stdout)
    record = {
        "command": command, "exit_code": run.returncode,
        "seconds": round(time.monotonic() - started, 3), "output_file": filename,
    }
    records.append(record)
    if run.returncode:
        (ROOT / "build-audit.json").write_text(json.dumps(
            {"completed": False, "steps": records}, indent=2) + "\n")
        print(run.stdout[-6000:])
        raise SystemExit(run.returncode)
    print(json.dumps(record))
log = (ROOT / "P15.2-partial.log").read_text(errors="replace")
audit = {
    "completed": True, "steps": records,
    "successful_tex_passes": 2,
    "overfull_hboxes": log.count("Overfull \\hbox"),
    "underfull_hboxes": log.count("Underfull \\hbox"),
    "undefined_control_sequences": "Undefined control sequence" in log,
    "latex_warnings": [line for line in log.splitlines() if "Warning" in line],
    "analytic_correctness_established": False,
    "rerun_command": "python build.py",
    "hashes": {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in
               ["input.json", "input-original.json", "P15.2-main.md",
                "P15.2-argument.md", "P15.2-partial.tex", "P15.2-partial.pdf",
                "source-audit.json", "coefficient-check.json"]},
}
(ROOT / "build-audit.json").write_text(json.dumps(audit, indent=2) + "\n")
print(json.dumps({k: audit[k] for k in
                  ["completed", "successful_tex_passes", "overfull_hboxes",
                   "undefined_control_sequences"]}))
