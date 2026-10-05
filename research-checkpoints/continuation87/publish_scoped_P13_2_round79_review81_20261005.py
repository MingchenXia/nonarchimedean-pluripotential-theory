"""Preserve unchanged round79 paper with its actual independent round81 PASS."""
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
S = R / "root-checks/public-P13.2-round-79-final-reader"
C = R / "campaigns/round-81/P13.2-smooth-rational-quotient-actual-realization-partial-review"
D = R / "deliverables/scoped-P13.2-round79"
A = R / "root-checks/P13.2-round81-actual-partial-mathematical-review-20261005.json"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def save(p, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


expected = {
    "P13.2-argument.md": "fd6e0b515f16338a647c951c913c64acdd1e7972dee7350758ff301a3ba2d41f",
    "P13.2-paper.tex": "e68e80a54e07aa260bcb1ff4a5878df147647dc3db388d77dc6df65ed20ee23d",
    "P13.2-paper.pdf": "989bf6ebae8c16e1ffbbc8647a63371656e110d3775fee92a491d21a7e8118a7",
    "canonical-notes.json": "3c9067a4d541854da34a631ee5fb7fe97e54f2784a2d34100e1952eec80673cc",
}
assert not D.exists(), "Publication directory must be new."
for name, binding in expected.items():
    assert sha(S / name) == binding, name
assert sha(A) == "c21d2081dfbcb0e0859b2eb46aae48c3d7b0d50049e6b66281b475b74824c307"
actual = json.loads(A.read_text())
assert actual == json.loads((C / "run.json").read_text())["campaign"]["result"]
assert actual["verdict"] == "PASS"
assert actual["operationId"] == "d8aa47ff-893c-4623-81bd-dda1bd8ed0f3"
freeze = json.loads((C / "freeze.json").read_text())
for name in ["task", "argument", "settings"]:
    p = C / (name + (".md" if name == "argument" else ".json"))
    assert sha(p) == freeze[name + "_sha256"]
packet = (C / "argument.md").read_bytes()
for binding in freeze["embedded_context"]:
    p = Path(binding["path"])
    assert sha(p) == binding["sha256"]
    assert len(p.read_bytes()) == binding["bytes"]
    assert p.read_bytes() in packet, binding["label"]
premises = actual["premises"]
passages = actual["passages"]
assert len(premises) == 10 and len(passages) == 15
for passage in passages:
    i = passage["premise"]
    assert isinstance(i, int) and 0 <= i < len(premises)
    assert passage["statement"] == premises[i]
    assert passage["url"].startswith("https://")
assert {p["premise"] for p in passages} == set(range(len(premises)))
build = json.loads((S / "build-report.json").read_text())
assert all(c["returncode"] == 0 for c in build["commands"])
read = json.loads((S / "root-preservation-and-read-state-continuation85.json").read_text())
assert read["whole_argument_root_read"] is True
D.mkdir(parents=True)
for name in expected:
    dest = "P13.2-reviewed-authored-notes.json" if name == "canonical-notes.json" else name
    shutil.copyfile(S / name, D / dest)
for name in ["build-report.json", "root-preservation-and-read-state-continuation85.json", "observed-native-status.json"]:
    shutil.copyfile(S / name, D / name)
shutil.copyfile(A, D / "P13.2-correctness-review.json")
I = D / "independent-review-inputs"
I.mkdir()
for name in ["task.json", "argument.md", "settings.json", "freeze.json"]:
    shutil.copyfile(C / name, I / name)
scope = (
    "Actual finite-energy realization, uniqueness modulo constants and I-convergence of "
    "every normalized actual E1 maximizing sequence for every fixed rational or irrational "
    "Reeb field on an original normal good polarized affine cone admitting at least one "
    "smooth rational projective quotient for the specified torus; all original cones of "
    "dimension at most two. Universal supremum-test root topology, finite-energy orbit "
    "pushforwards and root-L1 transfer retain their exact stated hypotheses. Original "
    "P13.2 remains open on general higher-dimensional singular rational quotients."
)
now = datetime.now(timezone.utc).isoformat()
record = {
    "prepared_utc": now, "atom": "P13.2", "author_round": 79, "review_round": 81,
    "scope": scope, "verdict": actual["verdict"],
    "operation_id": actual["operationId"], "reported_utc": actual["reportedAt"],
    "review": str(D / "P13.2-correctness-review.json"), "review_sha256": sha(A),
    "argument": str(D / "P13.2-argument.md"), "argument_sha256": expected["P13.2-argument.md"],
    "source": str(D / "P13.2-paper.tex"), "source_sha256": expected["P13.2-paper.tex"],
    "pdf": str(D / "P13.2-paper.pdf"), "pdf_sha256": expected["P13.2-paper.pdf"],
    "pages": 8, "publication_changes": "None: argument, authored notes, TeX and PDF byte-preserved.",
    "premises": 10, "passages": 15,
    "whole_actual_report_premises_and_retained_passages_root_read": True,
    "all_zero_based_exact_statement_bindings_verified": True,
    "all_review_input_and_embedded_context_bindings_reproduced": True,
    "whole_argument_root_read": True, "whole_tex_root_read": False,
    "primary_application_observation": [
        {"url": "https://stacks.math.columbia.edu/tag/00PD", "rendered_web_lines_read": [24, 39]},
        {"url": "https://stacks.math.columbia.edu/tag/0B8X", "rendered_web_lines_read": [23, 29]},
    ],
    "local_two_pass_compilation": "SUCCESS: unchanged author build.",
    "native_compilation": "Not yet verified on publication path.",
    "original_author_native_result": None,
    "author_runtime_limit": "Round79 native author remains BLOCKED for unregistered support ID. No accepted author result or runtime handle has been fabricated.",
    "full_original_atom_solved": False,
    "review_limit": "Source-aware computational reconstruction by the requested native model; not formal proof certification, journal peer review or a priority claim.",
}
save(D / "publication-preparation.json", record)
(D / "README.md").write_text(
    "# Actual finite-energy realization from a smooth rational quotient\n\n"
    + scope + "\n\n"
    "The unchanged eight-page paper was independently reconstructed with Xean native "
    "Codex gpt-6.1-sol/xhigh. The actual round81 review returned PASS at "
    + actual["reportedAt"] + "; its complete report and exact inputs are preserved here.\n\n"
    "The historical paper metadata still says unverified draft. This wrapper records the "
    "subsequent precise-scope review without rewriting the frozen source. The historical "
    "native author support-ID failure remains preserved; the mathematical review does "
    "not create an accepted author result. General original P13.2 remains OPEN.\n\n"
    "Two author pdfTeX passes succeeded. Native editor compilation on this saved "
    "publication path is recorded separately; the existing P16.4 editor remains open.\n"
)
for name in ["active-work.json", "checklist-current.json"]:
    p = R / name
    d = json.loads(p.read_text())
    assert d["fully_solved_original_atoms"] == ["P13.1", "P15.1", "P15.2", "P16.6"]
    d["updated_utc"] = now
    d["P13.2_round79_reviewed_partial"] = record
    if name == "active-work.json":
        d["goal_state"] = "4/42 unchanged original problems solved;38 remain open;42 reviewed scoped papers. Continue until the original goal is fulfilled."
    else:
        assert d["historical_reviewed_scoped_papers"] == 41
        d["historical_reviewed_scoped_papers"] = 42
    save(p, d)
p = R / "checklist-current.tsv"
lines = p.read_text().split("\n")
for i, line in enumerate(lines):
    if line.startswith("P13.2\t"):
        columns = line.split("\t")
        assert columns[1] == "open"
        columns[2] = "actual_all_Reeb_smooth_rational_quotient_realization_reviewed_general_singular_original_open"
        columns[3] = "2"
        lines[i] = "\t".join(columns)
p.write_text("\n".join(lines))
print(json.dumps({"publication": str(D), "files": sum(p.is_file() for p in D.rglob("*")), "record_sha256": sha(D / "publication-preparation.json"), "originals_solved": 4, "originals_open": 38, "reviewed_scoped_papers": 42}))
