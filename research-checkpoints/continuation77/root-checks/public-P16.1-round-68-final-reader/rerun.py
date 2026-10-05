"""Reproduce provenance, finite illustrations, the two builds and verification."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

commands = []
for script in ("prepare_provenance.py", "algebra_checks.py", "build.py", "verify.py"):
    result = subprocess.run([sys.executable, script], cwd=ROOT, capture_output=True)
    (ROOT / f"rerun-{Path(script).stem}.stdout.txt").write_bytes(result.stdout)
    (ROOT / f"rerun-{Path(script).stem}.stderr.txt").write_bytes(result.stderr)
    command = {"argv": [sys.executable, script], "cwd": str(ROOT), "returncode": result.returncode}
    commands.append(command)
    print(json.dumps(command))
    (ROOT / "rerun-commands.json").write_text(json.dumps(commands, indent=2)+"\n")
    if result.returncode:
        raise SystemExit(result.returncode)
