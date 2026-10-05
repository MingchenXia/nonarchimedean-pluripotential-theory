"""Use existing Pandoc and pdfLaTeX, preserving each build stream and log."""
import hashlib
import json
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def run(command, label):
    result = subprocess.run(command, cwd=ROOT, capture_output=True)
    (ROOT / f"{label}.stdout.txt").write_bytes(result.stdout)
    (ROOT / f"{label}.stderr.txt").write_bytes(result.stderr)
    record = {"label": label, "argv": command, "cwd": str(ROOT), "returncode": result.returncode, "stdout": f"{label}.stdout.txt", "stderr": f"{label}.stderr.txt"}
    print(json.dumps({"label": label, "returncode": result.returncode}))
    return record

def main():
    commands = []
    pandoc, latex = shutil.which("pandoc"), shutil.which("pdflatex")
    assert pandoc and latex, "Existing document tools required; no installation attempted."
    commands.append(run([pandoc, "P16.1-argument.md", "--standalone", "--from=markdown+tex_math_dollars", "--to=latex", "--include-in-header=tex-header.tex", "-V", "documentclass=article", "-V", "fontsize=11pt", "-o", "P16.1-paper.tex"], "pandoc"))
    if commands[-1]["returncode"] == 0:
        for number in (1, 2):
            label = f"tex-run-{number}"
            commands.append(run([latex, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "P16.1-paper.tex"], label))
            generated = ROOT / "P16.1-paper.log"
            if generated.exists():
                shutil.copyfile(generated, ROOT / f"{label}.log")
            if commands[-1]["returncode"] != 0:
                break
    success = len(commands) == 3 and all(c["returncode"] == 0 for c in commands)
    result = {"commands": commands, "success": success}
    pdf = ROOT / "P16.1-paper.pdf"
    if pdf.exists():
        result["pdf_sha256"] = hashlib.sha256(pdf.read_bytes()).hexdigest()
        result["pdf_bytes"] = pdf.stat().st_size
    (ROOT / "build-results.json").write_text(json.dumps(result, indent=2)+"\n")
    environment = json.loads((ROOT / "environment.json").read_text())
    environment.update({"python": sys.version, "platform": platform.platform(), "tool_versions": {}})
    for name in ("pandoc", "pdflatex", "pdftotext", "pdfinfo"):
        tool = shutil.which(name)
        environment["tools"][name] = tool
        if tool:
            option = "--version" if name in ("pandoc", "pdflatex") else "-v"
            r = subprocess.run([tool, option], capture_output=True)
            environment["tool_versions"][name] = (r.stdout+r.stderr).decode(errors="replace").split("\n")[0]
    (ROOT / "environment.json").write_text(json.dumps(environment, indent=2)+"\n")
    final_log = ROOT / "tex-run-2.log"
    review = {"scope": "Typesetting observations only, not mathematical verification."}
    if final_log.exists():
        content = final_log.read_text(errors="replace")
        review.update({"overfull_boxes": content.count("Overfull "), "underfull_boxes": content.count("Underfull "), "warnings": content.count("Warning"), "undefined_control_sequence": "Undefined control sequence" in content, "output_summary": re.findall(r"Output written on[^\n]+",content)})
    if pdf.exists() and success:
        info = run([shutil.which("pdfinfo"), "P16.1-paper.pdf"], "pdfinfo")
        review["pdfinfo_command"] = info
    (ROOT / "build-review.json").write_text(json.dumps(review, indent=2)+"\n")
    if not success:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
