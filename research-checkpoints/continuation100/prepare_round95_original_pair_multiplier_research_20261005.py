"""Preserve completed93 and freeze the next original P21.3 research attempt."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
C93 = R / "campaigns/round-93/P21.3-universal-continuous-pair-current-independence"
W93 = C93 / "artifacts/codex-KzRdXb"
P = R / "root-checks/public-P21.3-round-93-final-reader"
C = R / "campaigns/round-95/P21.3-original-pair-multiplier-geometric-research"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(path, value):
    path = Path(path)
    assert not path.exists()
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not P.exists() and not C.exists()
oldprep = json.loads((R / "round93-continuous-pair-current-research-preparation-20261005.json").read_text())
assert sha(C93 / "input.json") == oldprep["input_sha256"]
for b in oldprep["embedded_context"]:
    assert sha(b["path"]) == b["sha256"]
proc = subprocess.run(
    ["bash", "scripts/cloud.sh", "xean", "--records", "status", str(C93 / "campaign.sqlite")],
    cwd="/workspace/xean", capture_output=True, text=True, check=True,
)
state = json.loads(proc.stdout)
assert state["status"] == "completed" and state["calls"]["admitted"] == 1
result = json.loads((C93 / "run.json").read_text())["campaign"]["result"]
assert result["kind"] == "notes" and result["candidate"] is False
assert result["workspace"] == str(W93) and len(result["notes"]) == 3
ids = []
for note in result["notes"]:
    assert all(v in ids for v in note["support"])
    ids.append(note["id"])
artifact = json.loads((W93 / "artifact-manifest.json").read_text())
for name, b in artifact.items():
    assert sha(W93 / name) == b["sha256"]
assert json.loads((W93 / "input-original.json").read_text()) == json.loads((C93 / "input.json").read_text())
assert (W93 / "task-original.json").read_bytes() == (C93 / "task-original.json").read_bytes()
assert (W93 / "assignment-original.txt").read_bytes() == (C93 / "assignment-original.txt").read_bytes()
source = json.loads((W93 / "source-manifest.json").read_text())
texts = {}
for key, b in source["sources"].items():
    assert sha(W93 / b["file"]) == b["sha256"]
    texts[key] = (W93 / b["file"]).read_bytes().decode("utf-8").split("\n")
for b in source["units"]:
    expected = "\n".join(texts[b["source"]][b["lf_first"] - 1:b["lf_last_inclusive"]]).encode("utf-8")
    assert (W93 / b["file"]).read_bytes() == expected
    assert sha(W93 / b["file"]) == b["sha256"]
premises = json.loads((W93 / "premises.json").read_text())
assert [b["index"] for b in premises] == list(range(8))
for b in premises:
    for q in b["passages"]:
        assert q["premise"] == b["index"] and sha(W93 / q["quote_file"]) == q["sha256"]
for f in W93.rglob("*"):
    assert not f.is_symlink()
    if f.is_file():
        assert f.suffix not in {".sqlite", ".jsonl"}
        assert not any(v in {".git", ".codex", ".aws", "auth.json", ".env", "run.json"} for v in f.relative_to(W93).parts)
shutil.copytree(W93, P)
canonical = R / "root-checks/P21.3-round93-canonical-native-result-20261005.json"
save(canonical, result)
save(P / "completed-native-status.json", state)
reading = {
    "canonical_result": str(canonical), "sha256": sha(canonical),
    "whole_canonical_notes_root_read": True, "whole_core_root_read": True,
    "all_external_premise_statements_root_read": True,
    "all_nonnegative_passage_bindings_verified": True,
    "all21_literal_primary_units_reproduced": True,
    "all21_primary_bodies_root_read": False, "whole_TeX_root_read": False,
    "independent_mathematical_review_performed": False,
    "original_task_bytes_equal": True, "original_assignment_bytes_equal": True,
    "artifact_input_json_value_equal": True, "artifact_input_bytes_equal": False,
    "frozen_input_sha256": sha(C93 / "input.json"),
    "artifact_input_sha256": sha(P / "input-original.json"),
    "input_binding_note": "Artifact JSON serializes the same values in different bytes; frozen campaign bytes remain preserved separately. The artifact audit is not a claim of byte equality with frozen input.",
    "candidate": False, "original_closed": False, "new_scoped_paper_accepted": False,
    "gaps": json.loads((P / "status.json").read_text())["concrete_gaps"],
}
reading_path = R / "root-checks/P21.3-round93-root-reading-binding-20261005.json"
save(reading_path, reading)
C.mkdir(parents=True)
(C / "artifacts").mkdir()
task = json.loads((C93 / "task-original.json").read_text())
shutil.copyfile(C93 / "task-original.json", C / "task-original.json")
context = []


def embed(label, path):
    path = Path(path)
    body = path.read_text()
    context.append({"label": label, "path": str(path), "bytes": path.stat().st_size, "sha256": sha(path)})
    return "\n\nBEGIN MATHEMATICAL DATA: " + label + "\n" + body + "\nEND MATHEMATICAL DATA\n"


focus = """
CONTINUATION95: complete ORIGINAL P21.3. Use only Xean native Codex
gpt-6.1-sol/xhigh. The unchanged task below is controlling mathematical scope.
The completed93 draft is NOT task-granted mathematics and is NOT a solution.
Reconstruct any formal reduction you use; target an actual new analytic proof
of all-curvature-relation preservation, or one genuine analytic counterexample.
Do not replace research with another paper just restating its equivalences.

First critically reconstruct the supplied new102 bounded-generated-Psh
multiplier induction. Its proposed mechanism is that a locally bounded FINAL
section bounds every decreasing predecessor from below; upper semicontinuity
bounds each from above on fixed compact coefficient-measure supports. Thus
bounded dominated convergence may prove positivity through every sheafified
ordinal without reverse CPsh recognition. Check Borel multiplication, middle
positivity, restrictions, limit ranks and the complete primary antecedents.
This is an unreviewed proof suggestion, not an accepted premise.

The main target remains equality, not positivity of two separate products.
Try to derive the missing preservation of exact signed curvature relations
using actual analytic geometry and doubly closedness. Options to examine are
local positive-current regularization respecting all analytic refinements;
an actual two-sign generating construction for a continuous pair difference
with zero canonical Hessian; or an explicit higher-dimensional analytic
current and admissible pair violating equality. Prove every such mechanism.
No current-density theorem, strong lift/product compatibility, fixed-domain
positive gluing, higher-dimensional curve restriction, or preservation under
transcendental scalar extension is an assumption.

The following new primary GR reading is diagnostic, not recognition:
GR arXiv2506.13548v2 §§1.2,7.1--7.8, primary
https://arxiv.org/pdf/2506.13548v2. Classically pluriharmonic functions have
finite-dimensional Shilov evaluation spaces on compact affinoids; real-PL
recognition7.8 assumes an actual strictly semistable formal model. Equality
of ordinary Hessian currents for U,V does not yet make ±(U-V) classically
psh; neither semistable models nor descent of arbitrary currents is assumed.
If using these tools supply the missing implications, not a conditional
reformulation. Residual Picard/nonordinary-smooth curve examples are already
covered by the precisely granted real-PL multiplier theorem.

Retain every complete K including trivial valuation, every original good
separated strict boundaryless pure n>=2 analytic X, every ordinary open,
middle positivity and all degrees0<=p<=n-1, singularities, nilpotents and
actual generic multiplicities. A negative result needs one ACTUAL analytic
space, both finite continuous generated-Psh potentials separately, upstairs
Hessian equality, one positive doubly closed ordinary current and a compact
smooth test giving a nonzero product difference. A coarse cross-fan with
unequal upstairs curvatures, a topological example or a continuous harmonic
function with no admissible pair is insufficient.

The old exact accepted backgrounds and restrictions remain as stated in
the inherited assignment. A new102 lemma, formal source repair, conditional
density route or a narrower positive range alone must have candidate=false.
If the full original is proved, produce a readable standalone paper with
complete new proofs, exact primary premises and all applicability checks.
If it is still open, identify the genuinely new proved step and the concrete
unproved analytic statement; do not count an equivalent restatement as progress.
Use only supplied mathematical data and exact read-only primary paths or
public primary sources, and your fresh workspace. Do not inspect active92/94
or other private state. Do not alter editor, book, repository, runtime, auth,
source caches or sandbox; no other models, workers, installs or external
messages. There is no supplied time cutoff. Preserve task/assignment.
Provide P21.3-argument.md, P21.3-paper.tex/PDF using existing tools if available,
source provenance, build logs and status.json with exactly id,status,
exact_result,proof_file,concrete_gaps. Return at most four canonical notes
with backwards-only supports and candidate=true only for the full original.
"""
assignment = focus + "\nINHERITED EXACT BACKGROUND AND ITS SCOPES:\n" + (C93 / "assignment-original.txt").read_text()
for label, path in [
    ("UNREVIEWED completed93 formal core and precise gaps", P / "P21.3-core.md"),
    ("Literal primary premises for93, not independent review", P / "premises.json"),
    ("Completed93 literal primary bodies, only their precise statements", P / "P21.3-primary-evidence.md"),
    ("UNREVIEWED new102 locally bounded multiplier induction", R / "root-checks/P21.3-bounded-generated-Psh-multiplier-induction-20261005-continuation102.md"),
]:
    assignment += embed(label, path)
assignment += "\nCONTROLLING FINAL FOCUS: solve original pair equality or give an actual analytic counterexample; separate-product positivity and formal equivalences are not full coverage.\n"
(C / "assignment-original.txt").write_text(assignment)
save(C / "input.json", {"task": task, "notes": [], "assignment": assignment})
settings = json.loads((C93 / "settings.json").read_text())
settings["codex"]["workspace"] = str(C / "artifacts")
settings["usagePrefix"] = "catalogue-20261003/r95/P21.3-original-pair-multiplier"
assert len(settings["usagePrefix"]) <= 91
save(C / "settings.json", settings)
save(C / "freeze.json", {
    "input_sha256": sha(C / "input.json"), "task_sha256": sha(C / "task-original.json"),
    "assignment_sha256": sha(C / "assignment-original.txt"), "settings_sha256": sha(C / "settings.json"),
    "embedded_context": context, "inherited_context": oldprep["embedded_context"],
    "new102_granted": False, "completed93_granted": False, "original_closed": False,
})
prep = {
    "prepared_utc": datetime.now(timezone.utc).isoformat(), "round": 95, "atom": "P21.3",
    "directory": str(C), "public_reader93": str(P), "canonical93": str(canonical),
    "reading93": str(reading_path), "input_sha256": sha(C / "input.json"),
    "input_bytes": (C / "input.json").stat().st_size, "task_sha256": sha(C / "task-original.json"),
    "assignment_sha256": sha(C / "assignment-original.txt"), "settings_sha256": sha(C / "settings.json"),
    "embedded_context": context, "route": "Xean native Codex", "model": "gpt-6.1-sol",
    "reasoning": "xhigh", "submission_attempted": False, "original_closed": False,
    "no_hot_feedback_to92_or94": True, "new_mathematics_granted": False,
}
save(R / "round95-original-pair-multiplier-research-preparation-20261005.json", prep)
print(json.dumps({k: prep[k] for k in ["directory", "input_sha256", "input_bytes", "task_sha256", "settings_sha256"]}, indent=2))
