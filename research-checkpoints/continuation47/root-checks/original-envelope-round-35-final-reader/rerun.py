"""Run the existing TeX installation twice; success records no mathematical verdict."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parent
diag = root / "diagnostics"
diag.mkdir(exist_ok=True)
exe = shutil.which("pdflatex")
records = []
if not exe:
    records.append({"command": "pdflatex", "status": "unavailable", "exit_code": None})
else:
    for pass_number in (1, 2):
        cmd = [exe, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "P03.1-paper.tex"]
        proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True)
        output_file = diag / f"tex-pass-{pass_number}.txt"
        output_file.write_text("COMMAND: " + " ".join(cmd) + "\n\nSTDOUT:\n" + proc.stdout + "\nSTDERR:\n" + proc.stderr)
        records.append({"pass": pass_number, "command": cmd, "exit_code": proc.returncode,
                        "diagnostic_file": str(output_file.relative_to(root)),
                        "overfull_boxes": proc.stdout.count("Overfull "),
                        "underfull_boxes": proc.stdout.count("Underfull ")})
        print(f"pass {pass_number}: exit {proc.returncode}, overfull {records[-1]['overfull_boxes']}")
summary = {"runs": records, "mathematical_verification": False}
(diag / "build-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
a = (root / "input.json").read_bytes()
b = (root / "input-original.json").read_bytes()
(diag / "input-integrity.json").write_text(json.dumps({"byte_equal": a == b,
        "input_sha256": hashlib.sha256(a).hexdigest(),
        "input_original_sha256": hashlib.sha256(b).hexdigest(),
        "meaning": "Input preservation only; not proof certification."}, indent=2) + "\n")
sys.exit(0 if exe and all(r["exit_code"] == 0 for r in records) else 1)

