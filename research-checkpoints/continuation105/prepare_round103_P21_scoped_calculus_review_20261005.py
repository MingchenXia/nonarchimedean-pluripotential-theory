"""Preserve incomplete100 and freeze a source-contained scoped mathematical audit."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil

R = Path("/workspace/research")
A = R / "campaigns/round-100/P21.3-original-mixed-symmetry-and-arbitrary-current-research"
W = A / "artifacts/codex-RcZhes"
P = R / "root-checks/public-P21.3-round-100-final-reader"
C = R / "campaigns/round-103/P21.3-bounded-generated-mixed-symmetry-scoped-review"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not P.exists() and not C.exists()
f = json.loads((A / "freeze.json").read_text())
assert sha(A / "input.json") == f["input_sha256"]
result = json.loads((A / "run.json").read_text())["campaign"]["result"]
assert result["candidate"] is False and result["workspace"] == str(W) and len(result["notes"]) == 4
seen = []
for n in result["notes"]:
    assert n["id"] not in seen and all(s in seen for s in n["support"])
    seen.append(n["id"])
assert json.loads((W / "input-original.json").read_text()) == json.loads((A / "input.json").read_text())
assert (W / "task-original.json").read_bytes() == (A / "task-original.json").read_bytes()
assert (W / "assignment-original.txt").read_bytes() == (A / "assignment-original.txt").read_bytes()
status = json.loads((W / "status.json").read_text())
assert set(status) == {"id", "status", "exact_result", "proof_file", "concrete_gaps"}
assert status["status"] == "partial"
source = json.loads((W / "source-manifest.json").read_text())
s = source["source"]
assert sha(W / s["path"]) == s["sha256"] == sha(s["read_only_origin"])
lines = (W / s["path"]).read_bytes().decode().split("\n")
units = {}
for u in source["units"]:
    a, z = u["inclusive_one_based_LF"]
    literal = "\n".join(lines[a - 1:z]) + "\n"
    assert (W / u["path"]).read_bytes() == literal.encode()
    assert sha(W / u["path"]) == u["sha256"]
    assert u["source_sha256"] == s["sha256"] and u["url"].startswith("https://")
    units[u["id"]] = u
assert len(units) == 27
bound = source["bound_primary_units"][0]
assert sha(W / bound["path"]) == bound["sha256"] == sha(bound["read_only_origin"])
assert (W / units["weak-multiplier"]["path"]).read_bytes() == (W / bound["path"]).read_bytes() + b"\n"
premises = json.loads((W / "premises.json").read_text())
assert [p["id"] for p in premises] == ["P" + str(i) for i in range(9)]
for p in premises:
    assert p["evidence"] and p["primary_url"].startswith("https://")
    for q in p["evidence"]:
        assert q == units[q["id"]]
artifacts = []
for p in sorted(W.rglob("*")):
    assert not p.is_symlink()
    if p.is_file():
        assert p.suffix not in {".sqlite", ".jsonl"}
        assert not any(x in {".git", ".codex", ".aws", ".env", "auth.json", "run.json"} for x in p.relative_to(W).parts)
        artifacts.append({"path": str(p.relative_to(W)), "bytes": p.stat().st_size, "sha256": sha(p)})
shutil.copytree(W, P)
save(P / "root-independent-artifact-manifest.json", {
    "original_workspace": str(W), "artifacts": artifacts,
    "source_units_reproduced": 27, "mathematical_acceptance_asserted": False,
})
canonical = R / "root-checks/P21.3-round100-canonical-native-result-20261005.json"
reading = R / "root-checks/P21.3-round100-root-reading-binding-20261005.json"
save(canonical, result)
save(reading, {
    "canonical_result": str(canonical), "sha256": sha(canonical),
    "whole_canonical_notes_root_read": True, "whole254_LF_core_root_read": True,
    "all9_standalone_external_premise_records_root_read": True,
    "all27_literal_source_unit_bindings_reproduced": True,
    "all27_primary_bodies_root_read": False, "whole_TeX_root_read": False,
    "original_task_and_assignment_bytes_equal": True,
    "artifact_input_json_values_equal": True, "artifact_input_bytes_equal": False,
    "frozen_input_sha256": sha(A / "input.json"), "artifact_input_sha256": sha(P / "input-original.json"),
    "bound_weak_multiplier_and_single_newline_difference_verified": True,
    "independent_mathematical_review_performed": False,
    "candidate": False, "original_closed": False, "new_scoped_paper_accepted": False,
})
C.mkdir(parents=True)
(C / "artifacts").mkdir()
shutil.copyfile(A / "task-original.json", C / "task-original.json")
task = json.loads((C / "task-original.json").read_text())
original_criteria = task["completionCriteria"]
task["completionCriteria"] = """
Independently reconstruct this new100 PARTIAL mathematical packet only.
Requested verified scope: ordinary middle-positive Borel multiplication and
its limits, all locally bounded generated-Psh ordinal stages and positivity,
one-continuous-factor mixed symmetry and permutation independence with at most
one discontinuous factor, compatible-current closure including differentiation
by locally bounded possibly discontinuous generated potentials, smooth
positive closed decorations and weak positive limits, and the elementary
fixed-kernel monomial-shear diagnostic. Retain every original ambient field,
ordinary open, degree, singularity and multiplicity within those statements.
Do not require or infer arbitrary-current exhaustion or original P21.3 closure.
The exact original task wording remains in problem and is embedded below.

The new proof100 and proposed predecessors95/103 are NOT granted. No earlier
strict-PL or curve theorem is needed as a premise of this new argument; if used,
its precise supplied scope must be kept. Check every indispensable primary
statement and pertinent proof. All27 exact primary units and nine premise
records are supplied inline; no indispensable local file access is needed.
Do not treat historical acceptance, reading statements, hashes or builds as
mathematical evidence. Return actual canonical premises with nonnegative
zero-based statement-exact HTTP passage bindings.

Check the signed coefficient construction, support, ordinary chart topology,
middle-cone exterior-power domination, finite moments, sheafification and
cardinal stabilization, both differential equations, bounded predecessor
selection, fixed-measure sequential limits versus continuous multiplication
on varying positive nets, and correct orientation of symmetry in closure.
The complete original remains explicitly open. A scoped PASS never closes it.

One possible harmless ambiguity is singled out for assessment, not assumed
correct: Lemma2 says 'The limit is positive.' The proof proves positivity of
S, not of vS for arbitrary signed continuous v. Reconstruct the precise true
statement and determine whether this is solely a wording clarification or a
substantive defect anywhere in the proof. No edit is made to the frozen paper.
Check every other scope qualification and identify any mathematical defect.
"""
assert isinstance(original_criteria, str) and isinstance(task["completionCriteria"], str)
save(C / "task.json", task)
items = [
    ("Complete NEW unreviewed proof100", P / "P21.3-core.md"),
    ("Exact unchanged original P21.3 and original completion criteria", C / "task-original.json"),
    ("All nine precise external primary premises and literal bindings", P / "premises.json"),
    ("All27 literal pertinent CLD primary statement and proof units", P / "P21.3-primary-evidence.md"),
    ("Original source versions and exact coordinates", P / "source-manifest.json"),
    ("Complete canonical new100 notes, not grants", canonical),
    ("Documentary reading boundaries, not grants", reading),
]
argument = "Source-contained audit packet for new100 only. No current research102 output is supplied.\n"
context = []
for label, path in items:
    context.append({"label": label, "path": str(path), "bytes": path.stat().st_size, "sha256": sha(path)})
    argument += "\n\nBEGIN MATHEMATICAL DATA: " + label + "\n" + path.read_text() + "\nEND MATHEMATICAL DATA\n"
(C / "argument.md").write_text(argument)
settings = json.loads((R / "campaigns/round-99/P16.1-original-self-contained-full-review/settings.json").read_text())
settings["usagePrefix"] = "catalogue-20261003/r103/P21.3-scoped-generated-calculus"
settings["codex"]["workspace"] = str(C / "artifacts")
save(C / "settings.json", settings)
freeze = {
    "prepared_utc": datetime.now(timezone.utc).isoformat(), "round": 103, "atom": "P21.3",
    "directory": str(C), "public_reader100": str(P),
    "canonical100": str(canonical), "reading100": str(reading),
    "task_sha256": sha(C / "task.json"), "original_task_sha256": sha(C / "task-original.json"),
    "argument_sha256": sha(C / "argument.md"), "argument_bytes": (C / "argument.md").stat().st_size,
    "settings_sha256": sha(C / "settings.json"), "embedded_context": context,
    "new_paper_granted": False, "full_original_review": False, "original_closed": False,
    "submission_attempted": False, "route": "Xean native Codex",
    "model": "gpt-6.1-sol", "reasoning": "xhigh",
}
save(C / "freeze.json", freeze)
save(R / "round103-P21-scoped-calculus-review-preparation-20261005.json", freeze)
print(json.dumps({k: x for k, x in freeze.items() if k != "embedded_context"}, indent=2))
