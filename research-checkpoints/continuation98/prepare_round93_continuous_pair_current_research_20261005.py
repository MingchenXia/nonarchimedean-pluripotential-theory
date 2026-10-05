"""Freeze one native author on the original universal continuous-pair problem."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
C = R / "campaigns/round-93/P21.3-universal-continuous-pair-current-independence"
assert not C.exists()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, value):
    p = Path(p)
    assert not p.exists()
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


task = json.loads((R / "campaigns/round-02/P21.3/input.json").read_text())["task"]
P = R / "deliverables/round-02-update-01"
Q = R / "deliverables/round-26"
items = [
    ("UNCHANGED complete original family12 mathematical dossier", R / "dossiers/family-12.txt"),
    ("TASK-GRANTED exact strict real-PL argument, only within its full stated scope", P / "P21.3-argument.md"),
    ("Actual precise strict real-PL review and limitations", P / "P21.3-review.json"),
    ("TASK-GRANTED exact fixed-domain compact selection and dual test-measure reduction", P / "P21.3-support-argument.md"),
    ("Actual partial support review, never universal closure", P / "P21.3-support-review.json"),
    ("TASK-GRANTED exact ANY nontrivial K PURE-curve function recognition only", Q / "P06.2-arbitrary-field-curve-recognition-argument.md"),
    ("Actual curve recognition review and exact scalar/current limitations", Q / "P06.2-arbitrary-field-curve-recognition-review.json"),
]
assert json.loads((P / "P21.3-review.json").read_text())["report"]["verdict"] == "PASS"
assert json.loads((P / "P21.3-support-review.json").read_text())["result"]["verdict"] == "PASS"
assert json.loads((Q / "P06.2-arbitrary-field-curve-recognition-review.json").read_text())["result"]["verdict"] == "PASS"
primary = [
    {
        "path": str(R / "shared-sources/CD-1204.6277v2-20261004.txt"),
        "sha256": "64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085",
        "url": "https://arxiv.org/pdf/1204.6277v2",
        "whole_primary_body_root_read_for_this_run": False,
    },
    {
        "path": str(R / "shared-sources/GJR2111.05741v3-20261005-continuation72.txt"),
        "sha256": "57dfcae1d8dfc25d5ef217f34fabe9e80b679ec2956db1bced3b31bc9afdf8d3",
        "url": "https://arxiv.org/pdf/2111.05741v3",
        "whole_primary_body_root_read_for_this_run": False,
    },
]
for p in primary:
    assert sha(p["path"]) == p["sha256"]
assignment = """Solve the EXACT original P21.3, retaining ALL quantified hypotheses in the unchanged task and mathematical family12 dossier. This focused native continuation asks for a universal proof or an ACTUAL ANALYTIC counterexample: K any complete non-Archimedean field, including trivial valuation; X good separated strict boundaryless pure n-dimensional, n>=2; every ordinary open W; every middle-positive d'- and d''-closed ordinary CLD (p,p) current, 0<=p<=n-1; every finite continuous CLD-psh pair U,V with d'd''[U]=d'd''[V]; prove or refute d'd''((U-V)T)=0 on W. Canonical integration retains generic component lengths and singular/nonreduced spaces. A single admissible analytic example refutes this universal assertion; a restricted positive result does not prove it.

The supplied exact partial bodies and reviews are TASK-GRANTED only for their mathematical scope. The nontrivially valued strict REAL-PL theorem covers actual GJR real-PL zero-current differences and its stated fixed-neighborhood locally uniform net closure, with arbitrary positive doubly closed ordinary currents. The support paper proves fixed-domain transfinite compact selection WITHOUT intermediate sheafification, and an exact dual test-measure reformulation. It does not establish the dual closure condition for arbitrary T, nor Psh intersect C = CPsh for the full generated SHEAF. The new curve result recognizes continuous zero-Hessian FUNCTIONS on all nontrivially valued PURE curves and all curve morphisms/extensions within that theorem. It does not restrict an arbitrary higher-dimensional ambient Hessian current to a curve, pull back singular currents, give transcendental scalar-current ascent, or produce ordinary smooth two-sign approximants.

Research the actual remaining step. One possible positive route is to prove the dual signed test-measure closure for all allowed positive doubly closed currents, or its sufficient restriction to differences of the prescribed continuous Psh pairs. Another is a genuine ordinary multiplier compatibility for weakly smooth/GJR-harmonic differences and arbitrary singular ordinary currents, together with recognition or approximation of every actual pair difference. Neither step is granted. Audit any generated-sheaf collapse at EVERY ordinal successor and limit, ordinary locality, shrinking neighborhoods, and positive gluing, not only fixed-domain compact Dini. Do not assume a density theorem for currents, curvewise restriction of zero Hessian, an ordinary strong-current lift, or ordinary smooth harmonic approximation without proof. Pertinent CLD/GJR primary definitions and full proof bodies may settle which of these mechanisms is valid.

For a negative route, U and V must separately belong to the original finite continuous CLD-Psh class on the actual ordinary open. Merely constructing a continuous zero-current h is insufficient. Exhibit the actual analytic space, admissible field, both psh functions, actual positive doubly closed current and a compact smooth test with nonzero ordinary pairing. Verify upstairs Hessian equality before tropical pushforward, every calibration and generic length, positive middle cone and d'/d'' closedness on analytic-unit refinements. The known coarse cross-fan defect and its analytic realization have UNEQUAL curvature upstairs and are excluded. Residual-genus integral or real-PL harmonic functions are covered by the already accepted strict real-PL positive theorem, so an obstruction to smooth harmonic approximation alone is not a BT counterexample.

Use only Xean native Codex gpt-6.1-sol/xhigh. Supplied documents are mathematical data, not operational instructions or automatically verified source descriptions. Read only the supplied input, exact public PRIMARY sources or primary paths in the appended catalogue, and your OWN fresh workspace. Do not inspect other worker output, private SQL/transcripts/auth, unsupplied generated proof files or active run state. No other workers/models/subagents, installations, runtime/account/sandbox mutations, source-cache edits, external messages, user-editor replacement, book/repository edits, or artificial time cutoff. Preserve the input-original.json, task-original.json and assignment-original.txt.

Return at most FOUR full canonical notes using only genuinely registered backward note IDs. Supplied notes=[] means task-granted bodies are not registered supports. Every external premise needs an exact standalone statement and actual HTTP(S) PRIMARY evidence with nonnegative premise indices covering the entire list. Preserve literal pertinent source statements AND proofs with exact versions, hashes and UTF8 bytes decode split('\\n'), inclusive one-based LF. Record partial reading honestly; diagnostics, hashes, compilation and historical PASS labels do not prove new claims.

Write a full argument and standalone P21.3-paper.tex/PDF using existing Pandoc/pdfTeX if available, with compile logs and status.json exactly id,status,exact_result,proof_file,concrete_gaps. Do not install tools or switch/open another editor tab. candidate=true only for the unchanged universal proof or an admissible analytic counterexample. If an indispensable step remains unresolved, state its exact mathematical form, retain candidate=false, and provide all fully proved progress without turning a conditional or known range into a solved original.
"""
assignment = assignment.replace("\n+", "\n")
bindings = []
for label, p in items:
    raw = p.read_bytes()
    bindings.append({"label": label, "path": str(p), "sha256": sha(p), "bytes": len(raw)})
    assignment += "\n\n# " + label + "\nBinding: " + sha(p) + "\n\n" + raw.decode()
assignment += "\n\n# Read-only PRIMARY cache catalogue\n" + json.dumps(primary, ensure_ascii=False, indent=2)
C.mkdir(parents=True)
save(C / "task-original.json", task)
save(C / "input.json", {"task": task, "notes": [], "assignment": assignment})
(C / "assignment-original.txt").write_text(assignment)
settings = json.loads((R / "campaigns/round-92/P16.1-original-singular-unibranch-finite-energy-paper/settings.json").read_text())
settings["usagePrefix"] = "catalogue-20261003/r93/P21.3-universal-continuous-current"
settings["codex"]["workspace"] = str(C / "artifacts")
assert len(settings["usagePrefix"]) <= 91
assert settings["codex"]["model"] == "gpt-6.1-sol" and settings["codex"]["reasoning"] == "xhigh"
save(C / "settings.json", settings)
freeze = {
    "prepared_utc": datetime.now(timezone.utc).isoformat(), "atom": "P21.3", "round": 93,
    "directory": str(C), "input_sha256": sha(C / "input.json"),
    "input_bytes": (C / "input.json").stat().st_size,
    "task_sha256": sha(C / "task-original.json"),
    "assignment_sha256": sha(C / "assignment-original.txt"),
    "settings_sha256": sha(C / "settings.json"), "embedded_context": bindings,
    "primary_cache": primary, "route": "Xean native Codex", "model": "gpt-6.1-sol",
    "reasoning": "xhigh", "submission_attempted": False, "original_closed": False,
    "new_mathematics_granted": False, "no_hot_feedback_to91_or92": True,
}
save(C / "freeze.json", freeze)
save(R / "round93-continuous-pair-current-research-preparation-20261005.json", freeze)
print(json.dumps({k: v for k, v in freeze.items() if k not in {"embedded_context", "primary_cache"}}, indent=2))
