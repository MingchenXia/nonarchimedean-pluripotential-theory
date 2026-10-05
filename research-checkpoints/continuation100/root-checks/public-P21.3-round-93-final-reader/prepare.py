from pathlib import Path
import hashlib
import json
import platform
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def main():
    core = (ROOT / "P21.3-core.md").read_bytes()
    evidence = (ROOT / "P21.3-primary-evidence.md").read_bytes()
    (ROOT / "P21.3-argument.md").write_bytes(core+b"\n\n---\n\n"+evidence)
    status = {
        "id": "P21.3",
        "status": "partial",
        "exact_result": "Exact original-pair dual criterion for every target field, space, ordinary open and current degree: continuous generated-Psh cone operations are justified at every sheafified ordinal; the target on a fixed W,T is equivalent to weak closure tested only on Psh-continuous differences, exact finite interpolation against actual psh potentials, and preservation of their signed curvature relations. Failure of the pair-class closure would give admissible analytic psh potentials by coefficient splitting. No universal closure proof or actual analytic counterexample is supplied. The generated-sheaf successor gap in the printed recognition proof is documented without claiming the theorem false.",
        "proof_file": "P21.3-argument.md",
        "concrete_gaps": [
            "For arbitrary allowed positive doubly closed singular ordinary T, prove that every signed relation sum c_i d'd''[u_i]=0 among finite continuous generated-Psh functions on every ordinary W satisfies sum c_i <d'd''(u_i T),alpha>=0 for all compact ordinary symmetric alpha; equivalently prove the exact finite interpolation condition in Theorem 1.",
            "Alternatively exhibit an actual admissible W,T,alpha and finite actual continuous generated-Psh tuple with a relation violating the displayed multiplier equation. None is constructed; failure of the stronger all-continuous-kernel criterion alone would not supply the required psh pair.",
            "A full Psh-continuous to CPsh recognition proof must handle arbitrary discontinuous predecessor approximants and intermediate ordinary sheafification at every successor, with justified positive gluing on fixed neighbourhoods. The printed proof treats continuous predecessor approximants instead. Even repaired recognition of U,V individually would need a separate two-sign or multiplier argument for U-V.",
            "No new current density theorem, higher-dimensional curve restriction, arbitrary closed positive strong lift with ordinary product compatibility, or trivial-valuation regularization theorem is established."
        ]
    }
    (ROOT / "status.json").write_text(json.dumps(status, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    versions = {}
    for command in [("pandoc", "--version"), ("pdflatex", "--version"), ("pdftotext", "-v")]:
        exe = shutil.which(command[0])
        if exe:
            run = subprocess.run(command, capture_output=True, text=True, check=False)
            versions[command[0]] = {"path": exe, "version": (run.stdout or run.stderr).splitlines()[0], "exit_code": run.returncode}
    originals = {}
    for name in ["input-original.json", "task-original.json", "assignment-original.txt"]:
        raw = (ROOT / name).read_bytes()
        originals[name] = {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}
    environment = {"working_directory": str(ROOT), "python": sys.version,
                   "python_executable": sys.executable, "platform": platform.platform(),
                   "tools": versions, "originals": originals,
                   "reading": "Selected supplied primary LF bodies only; not the entire primary sources.",
                   "subagents": 0, "installations": 0, "external_reviews": 0,
                   "resource_heavy_work": False, "supervised_compute_facility": "None supplied; none needed or launched.",
                   "model_configuration": "User requested native gpt-6.1-sol/xhigh; no model-switch or delegation tools used. Runtime identity not separately inspected."}
    (ROOT / "environment.json").write_text(json.dumps(environment, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"argument_bytes": len(core)+len(evidence)+9, "status": "partial", "pdf_tools_present": all(k in versions for k in ("pandoc", "pdflatex"))}))

if __name__ == "__main__":
    main()
