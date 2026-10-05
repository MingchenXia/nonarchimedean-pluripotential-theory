"""Complete103 after a local preparation KeyError; preserve all written inputs."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

R = Path("/workspace/research")
P = R / "root-checks/public-P21.3-round-100-final-reader"
C = R / "campaigns/round-103/P21.3-bounded-generated-mixed-symmetry-scoped-review"
canonical = R / "root-checks/P21.3-round100-canonical-native-result-20261005.json"
reading = R / "root-checks/P21.3-round100-root-reading-binding-20261005.json"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert C.exists() and not (C / "settings.json").exists() and not (C / "review.sqlite").exists()
v = json.loads(canonical.read_text())
assert v["candidate"] is False and len(v["notes"]) == 4
assert json.loads(reading.read_text())["sha256"] == sha(canonical)
manifest = json.loads((P / "root-independent-artifact-manifest.json").read_text())
for a in manifest["artifacts"]:
    assert sha(P / a["path"]) == a["sha256"]
items = [
    ("Complete NEW unreviewed proof100", P / "P21.3-core.md"),
    ("Exact unchanged original P21.3 and original completion criteria", C / "task-original.json"),
    ("All nine precise external primary premises and literal bindings", P / "premises.json"),
    ("All27 literal pertinent CLD primary statement and proof units", P / "P21.3-primary-evidence.md"),
    ("Original source versions and exact coordinates", P / "source-manifest.json"),
    ("Complete canonical new100 notes, not grants", canonical),
    ("Documentary reading boundaries, not grants", reading),
]
expected = "Source-contained audit packet for new100 only. No current research102 output is supplied.\n"
context = []
for label, path in items:
    context.append({"label": label, "path": str(path), "bytes": path.stat().st_size, "sha256": sha(path)})
    expected += "\n\nBEGIN MATHEMATICAL DATA: " + label + "\n" + path.read_text() + "\nEND MATHEMATICAL DATA\n"
assert (C / "argument.md").read_text() == expected
assert isinstance(json.loads((C / "task.json").read_text())["completionCriteria"], str)
settings = json.loads((R / "campaigns/round-99/P16.1-original-self-contained-full-review/settings.json").read_text())
assert "codex" not in settings
settings["usagePrefix"] = "catalogue-20261003/r103/P21.3-scoped-generated-calculus"
save(C / "settings.json", settings)
freeze = {
    "prepared_utc": datetime.now(timezone.utc).isoformat(), "round": 103, "atom": "P21.3",
    "directory": str(C), "public_reader100": str(P),
    "canonical100": str(canonical), "reading100": str(reading),
    "task_sha256": sha(C / "task.json"), "original_task_sha256": sha(C / "task-original.json"),
    "argument_sha256": sha(C / "argument.md"), "argument_bytes": (C / "argument.md").stat().st_size,
    "settings_sha256": sha(C / "settings.json"), "embedded_context": context,
    "prior_preparation_error": "KeyError codex: the known-working REVIEW profile has no author-workspace codex section; no native call was made. Preserved partial inputs verified, missing settings/freeze completed only.",
    "prior_preparation_helper": str(R / "prepare_round103_P21_scoped_calculus_review_20261005.py"),
    "new_paper_granted": False, "full_original_review": False, "original_closed": False,
    "submission_attempted": False, "route": "Xean native Codex",
    "model": "gpt-6.1-sol", "reasoning": "xhigh",
}
save(C / "freeze.json", freeze)
save(R / "round103-P21-scoped-calculus-review-preparation-20261005.json", freeze)
print(json.dumps({k: x for k, x in freeze.items() if k != "embedded_context"}, indent=2))
