"""Preserve completed author84 and prepare a fresh exact Rossi/C1 repair review."""
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, value):
    Path(p).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


now = datetime.now(timezone.utc).isoformat()
A84 = R / "root-checks/P16.1-round84-canonical-native-result-20261005.json"
V85 = R / "root-checks/P16.1-round85-actual-partial-mathematical-review-20261005.json"
assert sha(A84) == "939f274e0ee284c1bd5c4fd99a7dfbe60d3392daeba3068eb04e929de82d9158"
assert sha(V85) == "a3540b6d2d3fc7845ca896b559abbdc477633afbe9fbab2e4682723d241a5c9c"
a84, v85 = json.loads(A84.read_text()), json.loads(V85.read_text())
assert a84["candidate"] is False and len(a84["notes"]) == 4
assert v85["verdict"] == "FAIL"
assert {p["premise"] for p in v85["passages"]} == set(range(28))
assert all(p["premise"] >= 0 and p["statement"] == v85["premises"][p["premise"]]
           for p in v85["passages"])
C84 = R / "campaigns/round-84/P16.1-fiber-reference-and-finite-data-descent"
W = Path(a84["workspace"])
assert W == C84 / "artifacts/codex-jOwhg8"
D = R / "root-checks/public-P16.1-round-84-final-reader"
assert D.is_dir()
for p in W.rglob("*"):
    if p.is_file():
        assert sha(p) == sha(D / p.relative_to(W))
assert sha(D / "canonical-native-result.json") == sha(A84)
assert json.loads((D / "input.json").read_text()) == json.loads((C84 / "input.json").read_text())
assert (D / "input.json").read_bytes() == (D / "input-original.json").read_bytes()
prov = json.loads((D / "source-extracts/source-provenance.json").read_text())
assert len(prov["units"]) == 70
for unit in prov["units"]:
    source = D / unit["source_file"]
    assert sha(source) == unit["source_text_sha256"]
    first, last = unit["inclusive_LF"]
    literal = "\n".join(source.read_bytes().decode().split("\n")[first-1:last]).encode()
    assert literal.decode() == unit["literal"]
    assert (D / unit["artifact"]).read_bytes() == literal
    assert sha(D / unit["artifact"]) == unit["sha256"]
prem = json.loads((D / "premises.json").read_text())
assert len(prem["premises"]) == 27 and len(prem["passages"]) == 70
assert {p["premise"] for p in prem["passages"]} == set(range(27))
assert all(isinstance(p["premise"], int) and p["premise"] >= 0
           and p["statement"] == prem["premises"][p["premise"]]["statement"] for p in prem["passages"])
save(D / "root-preservation-and-reading-limits-20261005.json", {
    "recorded_utc": now, "canonical_notes_whole_root_read": True,
    "canonical_sha256": sha(A84), "candidate": False, "original_closed": False,
    "semantic_campaign_input_reproduced": True, "worker_original_input_bytes_preserved": True,
    "campaign_input_sha256": sha(C84 / "input.json"),
    "worker_input_sha256": sha(D / "input.json"),
    "serialization_bytes_identical_campaign_worker": (C84 / "input.json").read_bytes() == (D / "input.json").read_bytes(),
    "worker_assignment_and_task_exact": True, "literal_units_reproduced": 70,
    "premise_passage_bindings_nonnegative_complete": True,
    "whole_argument_root_read": False, "whole_tex_root_read": False,
    "all_primary_literal_units_root_read": False, "whole_primary_files_root_read": False,
    "mathematics_accepted": False,
    "scope": "Completed public conditional author draft. C1 is unproved; all new combined mathematics remains unreviewed. Documentary observations do not certify correctness.",
})
record = R / "root-checks/P16.1-round85-actual-review-root-reading-20261005.json"
assert not record.exists()
save(record, {
    "recorded_utc": now, "canonical": str(V85), "canonical_sha256": sha(V85),
    "actual_verdict": "FAIL", "operation_id": v85["operationId"], "reported_at": v85["reportedAt"],
    "whole_actual_report_root_read": True, "all_28_premises_root_read": True,
    "all_36_passages_root_read": True, "all_nonnegative_bindings_verified": True,
    "whole_recursive_primary_proofs_root_read": False, "original_closed": False,
    "unreviewed_repair_pending": True,
    "failure": "The unchanged Rossi assertion omitted z in V. Both downstream applications choose V around their tested point, but this is an essential restriction requiring a fresh review.",
})
old = R / "root-checks/public-P16.1-round-83-final-reader/P16.1-argument.md"
sentence = "Let z belong to hull(L)\\L and let V be relatively compact open, with compact closure disjoint from L."
corrected = "Let z belong to hull(L)\\L and let V be a relatively compact open NEIGHBORHOOD OF z, with compact closure disjoint from L."
text = old.read_text()
assert text.count(sentence) == 1
fixed = R / "root-checks/P16.1-round83-Rossi-neighborhood-repaired-argument-20261005-continuation96.md"
assert not fixed.exists()
fixed.write_text(text.replace(sentence, corrected))
binding = R / "root-checks/P16.1-round85-Rossi-repair-binding-20261005-continuation96.md"
assert not binding.exists()
binding.write_text("""# Exact Rossi neighborhood repair; independently unreviewed

The actual round85 report is FAIL. No portion of author83 is promoted to an accepted theorem by that report. The new retained argument is the entire author83 argument with exactly one sentence changed: V is now explicitly a relatively compact open neighborhood of the tested z. Its old canonical notes, old paper and failed proof remain historical unchanged data, not assertions of the new retained body.

The missing condition is necessary. For trivially valued Qbar, L={the radius-one Gauss point at zero}, z=0 and V={|T-1|<1/2}, z lies in the original k[T] hull of L but outside V. Its boundary hull has |T-1| at most 1/2, whereas |T-1|(z)=1. Therefore the old conclusion is false. The repair excludes this counterexample by the essential antecedent z in V.

In the repaired proof, the glued maximum equals max(Cg0,log|f|-t) at z because z lies in V. The controlled g0 vanishes on a neighborhood of hull(L), so its value at z is zero. Strict separation gives log|f(z)|-t>0, while the glued function is zero on L because the compact closure of V is disjoint from L. The whole reference-winning boundary collar and all original-ring regularization inputs still require the precise accepted background; the added condition alone does not grant their mathematics.

Both uses retain the new antecedent. The off-bad-set proof chooses V around its finite maximum y; its boundary hull K_V is contained in hull(L), and Rossi is applied with tested y. The split-piece proof chooses V around x, with controlled compact closure inside pi^{-1}(N) intersect W_1 and disjoint from L; it applies Rossi with tested x. The original polynomial hull and compact controlled closures are kept.

Two binding clarifications apply throughout this new review. In a positive weighted sum, padding generator branches keeps their scaled positive logarithmic slopes: multiplying a log branch by positive c scales its slope by c; lowering a rational constant does not restore unit slope. Finite maxima/products still preserve the original generator data. Where a real additive normalization is used while the local contact convention requires rational constants, take decreasing rational shifts converging to that real value and flatten with rational shifts. Limits, same constants in equality contacts, original references and all minus-infinity values remain unchanged.

The full n1/n2/n3 chain and its projective canonical-reference consequence must be independently reconstructed again. Actual round87 provides only its exact geometric witness construction and countable net-to-sequence scope with its binding clarification; its application to every witness here must be checked. Actual round80 grants only the precise round77 partial background and errata. Resolved-nef all-point fiber descent, first target membership, target EP and the original equation are not granted. This fresh repair is not hot feedback to pending review88, does not alter any prior frozen input, and does not close original P16.1.
""")
C = R / "campaigns/round-89/P16.1-Rossi-neighborhood-repaired-countable-global-review"
assert not C.exists()
C.mkdir(parents=True)
oldC = R / "campaigns/round-85/P16.1-whole-base-trace-and-countable-Runge-partial-review"
task = json.loads((oldC / "task.json").read_text())
task["problem"] = """Independently assess the ENTIRE newly retained author83 argument with the essential Rossi antecedent z in V repaired, and the two explicit slope/rational-shift binding clarifications. Reconstruct n1 whole-base trace on the one original proper birational contact witness; n2 original-reference controlled regularization of already genuine affine FS limits, uniform pole multiplier, countable barrier, Rossi and original-u off-bad-set control; n3 countable split-piece/descending-Z/product Runge-Hartogs/singular-stratum/final GLOBAL empty-Z chain and its ORIGINAL projective canonical ample-reference weak-to-genuine consequence; audit n4's precise remaining gaps. The old actual85 FAIL is unchanged diagnostic data and grants none of author83's mathematics. The new retained body is the repaired full argument and repair binding only; old canonical notes and paper are historical data, not reviewed assertions. The exact accepted round77/actual80 and exact GEO/countable extraction root91/actual87 plus binding are granted only for their stated partial scope. Verify GEO applications to the SAME original witnesses in the new chain rather than treating a scope label as an antecedent check. No resolved-nef all-point fiber descent, singular EP, arbitrary-cardinality existence or original equation is granted."""
task["completionCriteria"] += """ The essential repair changes the mathematical assertion; independently prove its neighborhood version and confirm EVERY use has tested point inside V. Do not grant the remaining chain because the failed report found only this defect. Check weighted generator padding retains positive scaled slopes, and rational shifts implement real normalizations without invalid contacts or changing minus-infinity values. Assess the exact projective first-membership consequence on countable original reduced irreducible geometrically unibranch projective X with actual ample Q L, GIVEN the precise local contact-witness hypothesis; prove the global varying-class closure. The premise that a descended resolved potential has those contacts is conditional and outside this review. The output remains a partial review, never original closure."""
save(C / "task.json", task)
contexts = []


def body(label, path):
    p = Path(path)
    contexts.append({"label": label, "path": str(p), "sha256": sha(p), "bytes": p.stat().st_size})
    return "\n\n# " + label + "\n\n" + p.read_text()


packet = "# Fresh independent review of the complete repaired conditional C1 chain\n"
packet += body("NEW RETAINED full argument; independently unreviewed", fixed)
packet += body("NEW RETAINED essential repair and binding clarification; independently unreviewed", binding)
packet += body("UNCHANGED actual85 FAIL; diagnostic only, NO mathematical grant", V85)
freeze85 = json.loads((oldC / "freeze.json").read_text())
for entry in freeze85["embedded_context"]:
    p = Path(entry["path"])
    assert sha(p) == entry["sha256"]
    if p.name in {"P16.1-argument.md", "canonical-native-result.json"} and p.parent.name == "public-P16.1-round-83-final-reader":
        continue
    packet += body(entry["label"], p)
for label, name in [
    ("TASK-GRANTED exact geometric witness/countable extraction construction", "P16.1-geometric-witness-construction-and-countable-local-sequences-20261005-continuation91.md"),
    ("TASK-GRANTED actual87 PASS ONLY its precise partial scope", "P16.1-round87-actual-partial-mathematical-review-20261005.json"),
    ("TASK-GRANTED exact87 binding and reading limits", "P16.1-round87-binding-reading-clarifications-20261005.md"),
]:
    packet += body(label, R / "root-checks" / name)
packet += body("Exact partial review87 task limits the accepted grant",
               R / "campaigns/round-87/P16.1-geometric-witness-and-countable-sequence-partial-review/task.json")
(C / "argument.md").write_text(packet)
settings = json.loads((oldC / "settings.json").read_text())
settings["usagePrefix"] = "catalogue-20261003/r89/P16.1-Rossi-repaired-countable-global-review"
assert len(settings["usagePrefix"]) <= 91
save(C / "settings.json", settings)
save(C / "freeze.json", {
    "prepared_utc": now, "atom": "P16.1", "round": 89, "directory": str(C),
    "task_sha256": sha(C / "task.json"), "argument_sha256": sha(C / "argument.md"),
    "settings_sha256": sha(C / "settings.json"), "embedded_context": contexts,
    "argument_bytes": (C / "argument.md").stat().st_size, "original_closed": False,
    "author83_new_mathematics_granted": False, "actual85_verdict": "FAIL",
    "essential_new_Rossi_antecedent": "z in V", "input_hot_feedback": False,
    "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
})
save(R / "round89-Rossi-repair-and-round84-reader-preparation-20261005.json", {
    "prepared_utc": now, "reader84": str(D), "reader84_unreviewed": True,
    "review89": str(C), "repaired_argument": str(fixed), "repaired_argument_sha256": sha(fixed),
    "repair_binding": str(binding), "repair_binding_sha256": sha(binding),
    "whole_new_retained_body_root_read": False, "submission_attempted": False,
    "fully_solved_original_atoms": ["P13.1", "P15.1", "P15.2", "P16.6"],
    "remaining_open_atoms": 38, "original_closed": False,
})
print(json.dumps({"reader84": str(D), "review89": str(C), "contexts": len(contexts),
                  "task_sha256": sha(C / "task.json"), "argument_sha256": sha(C / "argument.md"),
                  "settings_sha256": sha(C / "settings.json"), "repaired_argument_sha256": sha(fixed),
                  "repair_binding_sha256": sha(binding)}, indent=2))
