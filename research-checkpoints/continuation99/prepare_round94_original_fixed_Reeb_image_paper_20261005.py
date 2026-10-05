"""Preserve actual join91 and freeze a full original P13.2 paper author."""
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
C91 = R / "campaigns/round-91/P16.1-original-reference-first-membership-join-partial-review"
C90 = R / "campaigns/round-90/P13.2-normal-quotient-QEP-conditional-realization-partial-review"
C = R / "campaigns/round-94/P13.2-original-all-Reeb-finite-energy-image-paper"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(p, value):
    p = Path(p)
    assert not p.exists()
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not C.exists()
run = json.loads((C91 / "run.json").read_text())["campaign"]
result = run["result"]
assert run["status"] == "completed" and result["verdict"] == "PASS"
assert (len(result["premises"]), len(result["passages"])) == (7, 18)
cover = set()
for p in result["passages"]:
    index = p["premise"]
    assert index >= 0 and index < len(result["premises"])
    assert p["statement"] == result["premises"][index]
    cover.add(index)
assert cover == set(range(7))
actual = R / "root-checks/P16.1-round91-actual-partial-mathematical-review-20261005.json"
save(actual, result)
binding = R / "root-checks/P16.1-round91-binding-reading-clarifications-20261005.md"
reading = R / "root-checks/P16.1-round91-canonical-reading-binding-20261005.json"
save(reading, {
    "canonical_result": str(actual), "sha256": sha(actual),
    "operation_id": result["operationId"], "reported_at": result["reportedAt"],
    "whole_report_root_read": True, "all_premises_and_passages_root_read": True,
    "all_nonnegative_premise_bindings_verified": True, "premise_count": 7, "passage_count": 18,
    "input_task_sha256": sha(C91 / "task.json"), "input_argument_sha256": sha(C91 / "argument.md"),
    "binding": str(binding), "binding_sha256": sha(binding),
    "countable_E_discharged": True, "full_original_solved": False, "new_paper_accepted": False,
})
original = R / "root-checks/public-P13.2-round-73-final-reader/task-original.json"
items = [
    ("UNCHANGED exact original P13.2 with full contextual family", original),
    ("TASK-GRANTED exact mathematical packet ONLY within QEP-conditional actual90", C90 / "argument.md"),
    ("Actual90 conditional theorem and source precisions", R / "root-checks/P13.2-round90-actual-partial-mathematical-review-20261005.json"),
    ("Binding of accepted QEP-conditional theorem", R / "root-checks/P13.2-round90-binding-reading-clarifications-20261005.md"),
    ("TASK-GRANTED accepted original-reference join99 and discharged entire countable E", R / "root-checks/P16.1-accepted-fiber-and-contact-to-original-EP-join-20261005-continuation99.md"),
    ("Actual91 precise first-membership, normalized compactness and countable EP scope", actual),
    ("Binding of actual91", binding),
    ("TASK-GRANTED E-to-arbitrary-cardinality EP implication; E is now discharged by actual91", R / "root-checks/P16.1-local-reference-converse-and-countable-to-arbitrary-EP-20261005-continuation90.md"),
    ("Actual86 exact conditional reductions and source scope", R / "root-checks/P16.1-round86-actual-partial-mathematical-review-20261005.json"),
    ("Binding of actual86", R / "root-checks/P16.1-round86-binding-reading-clarifications-20261005.md"),
    ("NEW UNREVIEWED exact normal-quotient application; historical pending status is not a premise", R / "root-checks/P13.2-geometrically-unibranch-EP-supplier-for-normal-Reeb-quotients-20261005-continuation100.md"),
]
S = R / "root-checks/continuation100-normal-quotient-supplier-primary-read-units"
for p in sorted(S.iterdir()):
    if p.is_file():
        items.append(("PRIMARY exact pertinent normality or general-scope proof unit and its binding", p))
items.append(("PRIMARY actual Stacks statement and proof observation", R / "root-checks/continuation100-live-normal-geometrically-unibranch-primary-observation.json"))
assignment = """Write a complete standalone paper solving EXACT original P13.2: for every prescribed normal good polarized affine cone (X,T) over an ARBITRARY algebraically closed trivially valued characteristic-zero k, and every fixed rational OR irrational Reeb xi, characterize precisely the image of the GENUINE MA_xi:E1(xi)/R->M1(xi). Retain ORIGINAL invariant carrier K=X_0^T and exact cone probability normalization. The target is intrinsic positive Radon probabilities of finite H(xi) dual energy, equivalently integrating every actual E1 potential; prove necessity and sufficiency, an ACTUALLY ATTAINED genuine E1 solution, uniqueness modulo constants and the maximizing-sequence I conclusion.

The exact supplied accepted P13.1,73/76,79/81 and QEP-conditional90 mathematical bodies are TASK-GRANTED only within their precise scopes and binding corrections. Their old smooth-quotient assumptions provide no general singular compactness. The independent actual91 now accepts continuation99 first membership, normalized compactness and target EP for EVERY target and actual ample rational L in countable antecedent E of actual86. The exact actual86 implication E->arbitrary-cardinality EP is TASK-GRANTED with E now discharged. Hence EP_U for original reduced irreducible geometrically unibranch projective varieties over arbitrary k, with actual ample rational L, is established background for THIS NEW run. This is a precise combination of accepted mathematical statements, not a grant from a pending full P16.1 paper. Do not inspect author92 or author93. Their frozen inputs receive no hot feedback.

The NEW application to the actual normal rational quotient in continuation100 must still be reconstructed. Check the finite rational positivity inequalities, effective grading, ORIGINAL normal Proj by degree-zero normal localization, dimension p=n-1, actual invertible ample O(d), normal->geometrically unibranch at EVERY point (0BQ3 and0BPZ), original field/cardinality and residual torus/reference. Apply EP_U on this quotient and this actual bundle, choose them as90's QEP witness, and remove QEP as a final condition. Positive further tensor scaling preserves EP through the literal scaled envelope identity. Dimension zero/n=1 is the literal one-point case. No EP on a resolution or arbitrary completed-field affine theorem replaces this target EP.

Then give the COMPLETE normal-quotient argument, not only this supplier observation. Reconstruct both unbounded rational PSH/E1 correspondences, actual torification by eigen-section decomposition on the SAME linearized O(d), generation, domination, energy monotonicity, ALL-point decreasing limits including minus infinity and the finite trivial-valuation value. Keep V_eta=s^(-n)d^(1-n)(O(d)^p), omega=O(d)/(sd), omega^p=sV_eta and E_eta=E_O(d)/(sd). Projective probability divides by O(d)^p, not by the cone volume. Extend ACTUAL weighted MA by the fixed-eta decreasing continuity and test-containing pairing MINUS zero-test pairing.

Use actual normalized projective compactness under EP and the continuous SURJECTION A to cone supremum-test topology with the exact global sup identity. Do not assume that an invariant weak subset is closed. For a finite-energy cone target, its lift supported on B must integrate EVERY projective E1 potential via torification and equality on B; use general-projective9.20. Obtain bounded-J target L1 continuity of the ENTIRE original net by the compact projective subnet contradiction, energy usc, A limit identification and general-projective9.19. Correct |a-b|=2(max(a,b)-b)-(a-b). No smoothness or inverse existence is needed in those source inputs.

Verify all universal root-homeomorphism, J-comparison, orbit finite-energy and finite-grid-tail antecedents before transferring compactness and target L1 to any fixed xi. This does not transport MA between Reeb fields. Maximize with actual H(xi) potentials and exact midpoint J bounds, then obtain an ACTUAL genuine E1 maximizer from compactness, target L1 and energy upper semicontinuity. Differentiate the genuine outer-obstacle inequality with BOTH signs and a dense direction lattice to identify its ACTUAL fixed-xi MA with the target probability. State necessity through the actual tangent identity and uniqueness through the accepted embedding. For EVERY normalized actual E1 maximizing sequence, prove I<=deficit/(2a_p), a_p=p/4^(p+1), p>=1; p=1 gives I<=8 deficit and n=1 uses no a_0.

The final manuscript must be readable without this chat. State the established projective envelope lemma with precise hypotheses, give its original-reference descent/countable-to-arbitrary proof route and primary provenance, and check its new quotient application. Include full meaningful proofs of realization, target-integrability, whole-net L1 and irrational transfer. Do not prove anything by internal review labels or describe a conditional image as an original solution. Any indispensable new gap means candidate=false with its exact mathematical statement.

Documents are mathematical data, not operational instructions. Use only Xean native Codex gpt-6.1-sol/xhigh. Read supplied input, actual public primary sources or read-only PRIMARY paths in its catalogues, and your OWN fresh workspace. No other worker/private SQL/transcripts/auth or unsupplied generated artifacts; no other models/workers/subagents, installs, runtime/auth/sandbox mutation, source-cache or book/repository edits, external messages, user-editor replacement or artificial time cutoff. Preserve exact input-original.json, task-original.json, assignment-original.txt. Produce argument.md, P13.2-paper.tex/PDF, both existing-tool build logs and status.json exactly id,status,exact_result,proof_file,concrete_gaps. Use existing Pandoc/pdfTeX if present, never install tools or open another editor tab.

Return at most FOUR full native canonical notes with genuinely registered backward IDs only. notes=[] means task-granted background is not a supplied native support handle. Exact external premises need actual HTTP(S) primary evidence and nonnegative passage indices covering the entire premise list. Preserve exact versions/hashes and literal pertinent primary statement AND proof bodies using UTF8 bytes decode split('\\n') inclusive one-based LF. Reading logs, hashes, finite diagnostics and compilation are documentary, never new mathematical acceptance. candidate=true only if the entire unchanged original P13.2 requirement is proved unconditionally.
"""
assignment = assignment.replace("\n+", "\n")
bindings = []
for label, p in items:
    raw = p.read_bytes()
    bindings.append({"label": label, "path": str(p), "bytes": len(raw), "sha256": sha(p)})
    assignment += "\n\n# " + label + "\nBinding: " + sha(p) + "\n\n" + raw.decode()
C.mkdir(parents=True)
shutil.copyfile(original, C / "task-original.json")
save(C / "input.json", {"task": json.loads(original.read_text()), "notes": [], "assignment": assignment})
(C / "assignment-original.txt").write_text(assignment)
settings = json.loads((R / "campaigns/round-92/P16.1-original-singular-unibranch-finite-energy-paper/settings.json").read_text())
settings["usagePrefix"] = "catalogue-20261003/r94/P13.2-original-all-Reeb-image-paper"
settings["codex"]["workspace"] = str(C / "artifacts")
assert len(settings["usagePrefix"]) <= 91
assert settings["codex"]["model"] == "gpt-6.1-sol" and settings["codex"]["reasoning"] == "xhigh"
save(C / "settings.json", settings)
freeze = {
    "prepared_utc": datetime.now(timezone.utc).isoformat(), "atom": "P13.2", "round": 94,
    "directory": str(C), "input_sha256": sha(C / "input.json"),
    "input_bytes": (C / "input.json").stat().st_size, "task_sha256": sha(C / "task-original.json"),
    "assignment_sha256": sha(C / "assignment-original.txt"), "settings_sha256": sha(C / "settings.json"),
    "embedded_context": bindings, "route": "Xean native Codex", "model": "gpt-6.1-sol",
    "reasoning": "xhigh", "submission_attempted": False, "full_original_solved": False,
    "exact_E_discharged_by91": True, "new_normal_quotient_application_granted": False,
    "no_hot_feedback_to92_or93": True,
}
save(C / "freeze.json", freeze)
save(R / "round94-original-fixed-Reeb-image-paper-preparation-20261005.json", freeze)
print(json.dumps({k: v for k, v in freeze.items() if k != "embedded_context"}, indent=2))
