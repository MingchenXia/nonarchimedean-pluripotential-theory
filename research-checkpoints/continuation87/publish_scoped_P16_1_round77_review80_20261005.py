"""Publish the unchanged round77 partial paper with actual round80 PASS and errata."""
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
S = R / "root-checks/public-P16.1-round-77-final-reader"
C = R / "campaigns/round-80/P16.1-compact-IBP-smooth-gate-partial-mathematical-review"
D = R / "deliverables/scoped-P16.1-round77"
A = R / "root-checks/P16.1-round80-actual-partial-mathematical-review-20261005.json"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def save(p, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


bindings = {
    "P16.1-argument.md": "6a82ecc963545cb9cc6f741e016f73ad82c8c43d9258acab9aa6431b221dba17",
    "P16.1-paper.tex": "d0fe620919f1dd6d46fd27740dd0c998448f788ba12b6eb5b57d4a7a2e57679f",
    "P16.1-paper.pdf": "07ef1129326f39993be17fabb283616b9ee5feb2db2ab85b3796200ad627559e",
    "canonical-native-result.json": "9665c02a812e1cea828cdcd61949ce484c483ce80992a8637489b859cc2d1cdf",
}
assert not D.exists()
for name, binding in bindings.items():
    assert sha(S / name) == binding, name
assert sha(A) == "342418bf7b363d708000f3f1d9d1f4cc4bb876ba4e96e78ce084c4f7a5ef4499"
actual = json.loads(A.read_text())
assert actual == json.loads((C / "run.json").read_text())["campaign"]["result"]
assert actual["verdict"] == "PASS" and actual["operationId"] == "e713d8d8-ccee-48b8-a347-4e0378a86db7"
freeze = json.loads((C / "freeze.json").read_text())
for name in ["task", "argument", "settings"]:
    p = C / (name + (".md" if name == "argument" else ".json"))
    assert sha(p) == freeze[name + "_sha256"]
packet = (C / "argument.md").read_bytes()
for binding in freeze["embedded_context"]:
    p = Path(binding["path"])
    assert sha(p) == binding["sha256"] and len(p.read_bytes()) == binding["bytes"]
    assert p.read_bytes() in packet
assert len(actual["premises"]) == len(actual["passages"]) == 15
for p in actual["passages"]:
    i = p["premise"]
    assert isinstance(i, int) and 0 <= i < 15
    assert p["statement"] == actual["premises"][i] and p["url"].startswith("https://")
assert {p["premise"] for p in actual["passages"]} == set(range(15))
assert all(p["returncode"] == 0 for p in json.loads((S / "build-report.json").read_text())["commands"])
assert json.loads((S / "root-preservation-and-read-state-continuation85.json").read_text())["whole_argument_root_read"]
D.mkdir(parents=True)
for name in bindings:
    shutil.copyfile(S / name, D / name)
for name in ["build-report.json", "root-preservation-and-read-state-continuation85.json", "observed-native-status.json"]:
    shutil.copyfile(S / name, D / name)
shutil.copyfile(A, D / "P16.1-correctness-review.json")
I = D / "independent-review-inputs"
I.mkdir()
for name in ["task.json", "argument.md", "settings.json", "freeze.json"]:
    shutil.copyfile(C / name, I / name)
errata = [
    "Section7: 'smooth projective morphism' means projective birational domination with smooth projective source, retaining the explicit original resolution-witness antecedent.",
    "Harmonic logarithms are logarithms of units on their indicated domains.",
    "The H/A naming switch in BE7.8 is a source naming typo.",
    "The weighted pairing is the test-containing pairing minus the zero-test pairing.",
    "IBP formulas are for dimension n>=1; reduced irreducible dimension-zero X is one point and its empty product has raw mass one.",
]
scope = (
    "Exact original-ring compact PL extensions and saturation partitions, algebraic-first "
    "continuous contact metric/nef bridge, common-bundle genuine FS approximation, shared "
    "collar positive and weighted products, compact signed IBP, raw mass, comparison and "
    "divisorial-atom domination. EP yields first genuine membership with explicit EP "
    "hypothesis; smooth characteristic-zero and actual-nef-reference instances follow. "
    "Smooth upper-growth regularization and principal-open removal retain the exact "
    "geometric compactification, projective birational domination and resolution-witness "
    "antecedents. Canonical nonflat norm characters and whole-base finite AFS trace formula "
    "are proved. Whole-base weak trace, Runge, singular EP and original P16.1 remain open."
)
now = datetime.now(timezone.utc).isoformat()
record = {
    "prepared_utc": now, "atom": "P16.1", "author_round": 77, "review_round": 80,
    "scope": scope, "verdict": "PASS", "operation_id": actual["operationId"],
    "reported_utc": actual["reportedAt"], "review": str(D / "P16.1-correctness-review.json"),
    "review_sha256": sha(A), "argument": str(D / "P16.1-argument.md"),
    "argument_sha256": bindings["P16.1-argument.md"], "source": str(D / "P16.1-paper.tex"),
    "source_sha256": bindings["P16.1-paper.tex"], "pdf": str(D / "P16.1-paper.pdf"),
    "pdf_sha256": bindings["P16.1-paper.pdf"], "pages": 12,
    "publication_changes": "None; frozen paper and actual native author result byte-preserved. Required harmless reading clarifications are supplied in the errata and actual review.",
    "binding_harmless_reading_clarifications": errata,
    "premises": 15, "passages": 15, "whole_actual_report_premises_and_retained_passages_root_read": True,
    "all_zero_based_exact_statement_bindings_verified": True,
    "all_review_input_and_embedded_context_bindings_reproduced": True,
    "whole_argument_root_read": True, "whole_tex_root_read": False,
    "local_two_pass_compilation": "SUCCESS: unchanged author build.",
    "native_compilation": "Not yet verified on publication path.",
    "full_original_atom_solved": False,
    "review_limit": "Source-aware computational reconstruction by requested Xean native gpt-6.1-sol/xhigh, not formal proof certification, journal peer review or a priority claim.",
}
save(D / "publication-preparation.json", record)
(D / "errata-and-reading-scope.md").write_text(
    "# Binding reading clarifications from actual round80 review\n\n"
    + "\n\n".join("- " + s for s in errata) + "\n\n"
    "These are exactly the harmless interpretations retained by the actual PASS. They do "
    "not discharge any conditional geometric antecedent or prove singular EP.\n"
)
(D / "README.md").write_text(
    "# Compact IBP and smooth conditional gates\n\n" + scope + "\n\n"
    "Actual round80 independent review: PASS at " + actual["reportedAt"] + ". The complete "
    "mathematical report, all premises/passages and exact input packet are preserved. "
    "Read the unchanged twelve-page paper together with errata-and-reading-scope.md. "
    "Historical unverified-draft metadata is preserved; this wrapper records the later "
    "mathematical review. Original P16.1 remains OPEN.\n\n"
    "Two author pdfTeX passes succeeded. Native compilation on this publication path is "
    "recorded separately. The existing P16.4 editor is kept unchanged and open.\n"
)
for name in ["active-work.json", "checklist-current.json"]:
    p = R / name
    d = json.loads(p.read_text())
    assert d["fully_solved_original_atoms"] == ["P13.1", "P15.1", "P15.2", "P16.6"]
    d["updated_utc"] = now
    d["P16.1_round77_reviewed_partial"] = record
    if name == "active-work.json":
        d["goal_state"] = "4/42 unchanged original problems solved;38 remain open;43 reviewed scoped papers. Continue until the original goal is fulfilled."
    else:
        assert d["historical_reviewed_scoped_papers"] == 42
        d["historical_reviewed_scoped_papers"] = 43
        for target in d["targets"]:
            if target["id"] in ["P13.2", "P16.1"]:
                assert target["closure"] == "open" and target["fully_solved"] is False
                rec = d["P13.2_round79_reviewed_partial"] if target["id"] == "P13.2" else record
                target.setdefault("reviewed_papers", []).append(rec)
                target["current_focus"] = rec["scope"]
    save(p, d)
p = R / "checklist-current.tsv"
lines = p.read_text().split("\n")
for i, line in enumerate(lines):
    if line.startswith("P16.1\t"):
        columns = line.split("\t")
        assert columns[1] == "open"
        columns[2] = "compact_IBP_continuous_bridge_smooth_conditional_gates_and_canonical_norm_reviewed_singular_EP_open"
        columns[3] = "1"
        lines[i] = "\t".join(columns)
p.write_text("\n".join(lines))
print(json.dumps({"publication": str(D), "files": sum(p.is_file() for p in D.rglob("*")), "record_sha256": sha(D / "publication-preparation.json"), "originals_solved": 4, "originals_open": 38, "reviewed_scoped_papers": 43}))
