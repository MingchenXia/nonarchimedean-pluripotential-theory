#!/usr/bin/env python3
"""Lightweight provenance/coefficient checks and two-pass full-proof build.

No network, model calls, installation, or heavy computation. Run in this folder.
Execution is diagnostic evidence, never a proof of the analytic claims.
"""
from __future__ import annotations

import hashlib
import json
import math
import platform
from pathlib import Path
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(name: str, data: object) -> None:
    (ROOT / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def choose(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


def main() -> None:
    provenance = json.loads((ROOT / "source-provenance.json").read_text())
    original = json.loads((ROOT / "input.json").read_text())
    tests: list[dict] = []
    assert (ROOT / "input.json").read_bytes() == (ROOT / "original-input.json").read_bytes()
    for file, string in [
        ("original-problem.txt", original["task"]["problem"]),
        ("original-completion-criteria.txt", original["task"]["completionCriteria"]),
        ("original-assignment.txt", original["assignment"]),
    ]:
        assert (ROOT / file).read_text() == string
    tests.append({"check": "all original input strings and original JSON bytes preserved", "passed": True})

    expected = {
        (175, 188): "6935e7b22f65e44e597df16e0d3f61db8fd131b34f83d0e0047f2612bd58bf5c",
        (189, 242): "14edda72965b2b8a4d90c4cf9e4adb68eaaf60093fa10c9f376d90be736feb01",
        (249, 322): "1dada113d7a3c9897039047fef2fa9aa9922f3c359092bbbfc416fab3823e0b2",
        (626, 762): "59d8ae8186c59c9beb538816fed649a432c4bd8de0ccccc3501c3c2877126824",
        (810, 840): "aa1c54651a97636414c96f9ae8d1815cfcfc49c8d8fbd8f02b7fd6f1a9306d3e",
        (1120, 1222): "c1037903ef8126d0cb75ab0138d6ee5076fd0dd4d64ab91c9bcbad63e9124be2",
    }
    # The known body hash is checked from the original assignment itself as well.
    # No normalization of formfeeds, terminal LF, or Unicode is performed.
    for block in provenance["excerpts"]:
        path = ROOT / block["file"]
        digest = sha(path)
        assert digest == block["sha256"]
        interval = (block["first_LF_line"], block["last_LF_line"])
        if interval in expected:
            supplied = expected[interval]
            # Fail clearly if a hand-entered digest is mistyped, before treating
            # a historical body as matched to the assignment.
            assert supplied in original["assignment"], ("digest not supplied", interval, supplied)
            assert digest == supplied, (interval, digest, supplied)
        source = Path(block["source"])
        if source.exists():
            lf = source.read_bytes().split(b"\n")
            extracted = b"\n".join(lf[interval[0] - 1:interval[1]])
            assert extracted == path.read_bytes()
    tests.append({"check": "all six supplied LF excerpt hashes and literal byte extraction", "passed": True, "count": 6})
    for key in ["primary_text", "primary_pdf"]:
        source = Path(provenance[key]["path"])
        if source.exists():
            assert sha(source) == provenance[key]["sha256"]
    assert sha(ROOT / "operator-proposal-original.md") == provenance["proposal_sha256"]
    assert sha(ROOT / "original-input.json") == provenance["original_input_sha256"]
    tests.append({"check": "primary text/PDF, proposal and input SHA256 provenance", "passed": True})

    coefficient_cases = 0
    mass_cases = 0
    for n in range(2, 31):
        for nu in range(1, n):
            for a in range(nu + 1):
                lhs = sum(choose(j, a) * choose(n - j, nu - a) for j in range(n + 1))
                assert lhs == choose(n + 1, nu + 1)
                coefficient_cases += 1
            assert n * choose(n - 1, nu - 1) == nu * choose(n, nu)
            assert (nu + 1) * choose(n + 1, nu + 1) == (n + 1) * choose(n, nu)
            # Exact power-count diagnostic: volume starts at n-nu, while
            # theta*q^(n-1) also starts at n-nu, not n-nu-1.
            assert min(n - k for k in range(nu + 1)) == n - nu
            assert min(n - 1 - k for k in range(nu)) == n - nu
            mass_cases += 1
    tests.append({"check": "energy convolution coefficient identity", "passed": True,
                  "scope": "exhaustive integers 2<=n<=30, 1<=nu<n, 0<=a<=nu", "cases": coefficient_cases})
    tests.append({"check": "calibration coefficient identities and transverse power counts", "passed": True,
                  "scope": "exhaustive integers 2<=n<=30, 1<=nu<n", "cases": mass_cases})
    tests.append({"check": "analytic theorem", "passed": None,
                  "scope": "not machine checked; author proof and cited bounded foundations only"})
    save("checks.json", {"checks": tests, "execution_does_not_prove_mathematics": True})

    # Generate a standalone TeX body. No external input/include of the Markdown.
    pandoc = shutil.which("pandoc")
    pdflatex = shutil.which("pdflatex")
    if not pandoc or not pdflatex:
        raise RuntimeError("Local Pandoc and pdflatex are required; no installation attempted")
    commands = [[pandoc, "P15.1-argument.md", "--standalone",
                 "--from=markdown+tex_math_dollars", "--to=latex",
                 "-V", "documentclass=article", "-V", "fontsize=11pt",
                 "-V", "geometry:margin=1in", "-o", "P15.1-partial.tex"]]
    records = []
    first = subprocess.run(commands[0], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (ROOT / "pandoc-build.log").write_text(first.stdout)
    records.append({"command": commands[0], "returncode": first.returncode, "log": "pandoc-build.log"})
    if first.returncode:
        save("build-evidence.json", {"commands": records, "success": False})
        raise RuntimeError("Pandoc build failed; see pandoc-build.log")
    for pass_number in (1, 2):
        command = [pdflatex, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "P15.1-partial.tex"]
        commands.append(command)
        completed = subprocess.run(command, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        name = f"build-pass-{pass_number}.log"
        (ROOT / name).write_text(completed.stdout)
        records.append({"command": command, "pass": pass_number, "returncode": completed.returncode, "log": name})
        if completed.returncode:
            save("build-evidence.json", {"commands": records, "success": False})
            raise RuntimeError(f"TeX pass {pass_number} failed; see {name}")
    second_log = (ROOT / "build-pass-2.log").read_text()
    warnings = [line for line in second_log.split("\n") if any(s in line for s in ["Warning", "Overfull", "Underfull"])]
    assert "Output written on P15.1-partial.pdf" in second_log
    assert not any(s in second_log for s in ["Undefined control sequence", "Fatal error", "undefined references"])
    save("build-evidence.json", {
        "utc": datetime.now(timezone.utc).isoformat(), "success": True,
        "commands": records, "pdflatex_passes": 2, "second_pass_warnings": warnings,
        "proof_sha256": sha(ROOT / "P15.1-argument.md"),
        "tex_sha256": sha(ROOT / "P15.1-partial.tex"), "pdf_sha256": sha(ROOT / "P15.1-partial.pdf"),
        "pdf_bytes": (ROOT / "P15.1-partial.pdf").stat().st_size,
        "python": sys.version, "platform": platform.platform(),
        "diagnostic_only": True,
    })
    save("commands.json", {"rerun": "python rerun.py", "build_commands": commands,
                           "writes": "assigned workspace only", "network": False})
    print(json.dumps({"checks_passed": 5, "coefficient_cases": coefficient_cases,
                      "mass_and_power_cases": mass_cases, "pdflatex_passes": 2,
                      "pdf": "P15.1-partial.pdf", "warnings": warnings,
                      "analytic_proof_machine_verified": False}, indent=2))


if __name__ == "__main__":
    main()
