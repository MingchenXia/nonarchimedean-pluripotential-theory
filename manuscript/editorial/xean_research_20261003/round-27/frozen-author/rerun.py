#!/usr/bin/env python3
"""Small exact diagnostics and a two-pass, wholly local document build."""
from __future__ import annotations

import hashlib
import json
import math
import platform
import shutil
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EVIDENCE = ROOT / "evidence"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    EVIDENCE.mkdir(exist_ok=True)
    start = time.time()
    report = {"kind": "exhaustive finite arithmetic diagnostics, not proof of analytic claims"}
    vandermonde = 0
    exponent_checks = 0
    telescoping_checks = 0
    def choose(n: int, k: int) -> int:
        return math.comb(n, k) if 0 <= k <= n else 0

    for n in range(2, 33):
        for nu in range(1, n):
            m = n - nu
            assert min(n - k for k in range(nu + 1)) == m
            assert min(n - 1 - k for k in range(nu)) == m
            assert min(n - k for k in range(nu)) == m + 1
            exponent_checks += 1
            for a in range(nu + 1):
                observed = sum(choose(j, a) * choose(n - j, nu - a) for j in range(n + 1))
                expected = math.comb(n + 1, nu + 1)
                assert observed == expected, (n, nu, a, observed, expected)
                assert Fraction(observed, n + 1) == Fraction(math.comb(n, nu), nu + 1)
                vandermonde += 1
    for d in range(1, 33):
        coeff = [1] * (d + 1)
        for j in range(1, d + 1):
            coeff[j] += j
            coeff[j - 1] -= j
        assert coeff == [0] * d + [d + 1]
        for a in range(d + 1):
            integral = Fraction(math.comb(d, a) * math.factorial(a) * math.factorial(d - a), math.factorial(d + 1))
            assert integral == Fraction(1, d + 1)
        telescoping_checks += 1
    report.update(vandermonde_cases=vandermonde, exponent_cases=exponent_checks,
                  telescoping_dimensions=telescoping_checks, maximum_n=32, arithmetic_pass=True)

    prov = json.loads((EVIDENCE / "source-provenance.json").read_text())
    hash_checks = 0
    for entry in prov.values():
        if "copy" in entry and "sha256" in entry:
            assert sha256(ROOT / entry["copy"]) == entry["sha256"]
            hash_checks += 1
    original = json.loads((ROOT / "original-input/input.json").read_text())
    strings = json.loads((ROOT / "original-input/strings.json").read_text())
    assert strings["task.problem"] == original["task"]["problem"]
    assert strings["task.completionCriteria"] == original["task"]["completionCriteria"]
    assert strings["assignment"] == original["assignment"]
    report.update(provenance_hash_checks=hash_checks, original_string_checks=3)

    argument = (ROOT / "P15.2-argument.md").read_text()
    core = argument.split("<!-- END THEOREM PAPER -->", 1)[0].split("\n", 1)[1]
    (EVIDENCE / "theorem-paper-input.md").write_text(core)
    header = EVIDENCE / "latex-header.tex"
    header.write_text("\\usepackage{amsmath,amssymb}\n\\setlength{\\emergencystretch}{2em}\n")
    commands = []
    def run(command: list[str], log: str, input_text: str | None = None) -> subprocess.CompletedProcess:
        begun = time.time()
        result = subprocess.run(command, cwd=ROOT, input=input_text, capture_output=True, text=True)
        (EVIDENCE / log).write_text(result.stdout + result.stderr)
        commands.append({"argv": command, "cwd": str(ROOT), "returncode": result.returncode,
                         "log": "evidence/" + log, "seconds": round(time.time() - begun, 4)})
        if result.returncode:
            (EVIDENCE / "commands.json").write_text(json.dumps(commands, indent=2) + "\n")
            raise RuntimeError(f"Command failed; see evidence/{log}")
        return result

    run(["pandoc", "--from=markdown+tex_math_dollars", "--to=latex", "--standalone", "--wrap=none", "--shift-heading-level-by=-1",
         "--metadata=title:A relative base Monge--Ampère operator for bounded potentials",
         "--metadata=author:Xean research author draft",
         "--metadata=date:4 October 2026; partial result for P15.2",
         "-V", "documentclass=article", "-V", "fontsize=11pt", "-V", "geometry=margin=1in",
         "--include-in-header=" + str(header), "--output=P15.2-partial.tex"], "pandoc.log", core)
    compile_command = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "P15.2-partial.tex"]
    for pass_number in (1, 2):
        run(compile_command, f"build-pass-{pass_number}.stdout.txt")
        shutil.copyfile(ROOT / "P15.2-partial.log", EVIDENCE / f"build-pass-{pass_number}.log")
    run(["pdftotext", "-layout", "P15.2-partial.pdf", "evidence/P15.2-partial-extracted.txt"], "pdf-extraction.log")
    info = run(["pdfinfo", "P15.2-partial.pdf"], "pdfinfo.txt")
    extracted = (EVIDENCE / "P15.2-partial-extracted.txt").read_text()
    normalized_extracted = " ".join(extracted.split())
    for required in ["Exact scope and statement", "Operator estimate", "Bibliography", "original atom remains open"]:
        assert required in normalized_extracted, required
    warnings = {}
    for pass_number in (1, 2):
        text = (EVIDENCE / f"build-pass-{pass_number}.log").read_text()
        warnings[str(pass_number)] = [line for line in text.split("\n") if any(k in line for k in ["Warning", "Overfull", "Underfull", "Error"])]
    report.update(build_passes=2, pdf_sha256=sha256(ROOT / "P15.2-partial.pdf"),
                  tex_sha256=sha256(ROOT / "P15.2-partial.tex"), warnings=warnings,
                  elapsed_seconds=round(time.time() - start, 4), pdf_text_required_checks=4,
                  environment={"python": sys.version, "platform": platform.platform()})
    (EVIDENCE / "commands.json").write_text(json.dumps(commands, ensure_ascii=False, indent=2) + "\n")
    (EVIDENCE / "diagnostics.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print(info.stdout)


if __name__ == "__main__":
    main()
