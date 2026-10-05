"""Preserve input-too-large96 and resubmit the same full review with less duplication."""
import hashlib
import json
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
O = R / "campaigns/round-96/P16.1-original-singular-unibranch-paper-full-review"
C = R / "campaigns/round-97/P16.1-original-full-review-length-recovery"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def save(path, value):
    path = Path(path)
    assert not path.exists()
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


assert not C.exists()
freeze = json.loads((O / "freeze.json").read_text())
assert sha(O / "argument.md") == freeze["argument_sha256"]
for b in freeze["embedded_context"]:
    assert sha(b["path"]) == b["sha256"]
state = json.loads(subprocess.run(
    ["bash", "scripts/cloud.sh", "xean", "--records", "status", str(O / "review.sqlite")],
    cwd="/workspace/xean", capture_output=True, text=True, check=True,
).stdout)
assert state["status"] == "blocked" and "input_too_large" in state["error"]
C.mkdir(parents=True)
save(C / "previous96-input-length-failure.json", state)
shutil.copyfile(O / "task.json", C / "task.json")
shutil.copyfile(O / "task-original.json", C / "task-original.json")
shutil.copyfile(O / "primary-catalogue.json", C / "primary-catalogue.json")
included, referenced = [], []
parts = [
    "# SAME FULL ORIGINAL P16.1 review, with duplicate primary material referenced\n",
    "The full paper, every external premise, and every exact granted mathematical proof and scope remain supplied below. Six duplicate primary evidence/catalogue entries are referenced at their preserved read-only public paths. No mathematical scope, acceptance criterion or model is changed.\n",
]
for b in freeze["embedded_context"]:
    if re.match(r"Originally supplied context 2[0-5]:", b["label"]):
        referenced.append(b)
        continue
    included.append(b)
    parts.append("\n\nBEGIN MATHEMATICAL DATA: " + b["label"] + "\n" + Path(b["path"]).read_text() + "\nEND MATHEMATICAL DATA\n")
parts.append("\n\n# Referenced duplicate primary entries, explicitly available for read-only review\n")
parts.append(json.dumps(referenced, ensure_ascii=False, indent=2))
argument = "\n".join(parts)
assert len(argument) < 900000
(C / "argument.md").write_text(argument)
settings = json.loads((O / "settings.json").read_text())
settings["usagePrefix"] = "catalogue-20261003/r97/P16.1-original-full-review-recovery"
save(C / "settings.json", settings)
save(C / "freeze.json", {
    "task_sha256": sha(C / "task.json"), "original_task_sha256": sha(C / "task-original.json"),
    "argument_sha256": sha(C / "argument.md"), "settings_sha256": sha(C / "settings.json"),
    "embedded_context": included, "referenced_read_only_context": referenced,
    "original_task_unchanged": True, "full_original_review_scope_unchanged": True,
    "original_closed": False, "previous96_rewritten_or_rerun": False,
})
prep = {
    "prepared_utc": datetime.now(timezone.utc).isoformat(), "round": 97, "atom": "P16.1",
    "directory": str(C), "previous96": str(O), "previous_failure": str(C / "previous96-input-length-failure.json"),
    "task_sha256": sha(C / "task.json"), "original_task_sha256": sha(C / "task-original.json"),
    "argument_sha256": sha(C / "argument.md"), "argument_characters": len(argument),
    "argument_bytes": (C / "argument.md").stat().st_size, "settings_sha256": sha(C / "settings.json"),
    "embedded_context": included, "referenced_read_only_context": referenced,
    "route": "Xean native Codex", "model": "gpt-6.1-sol", "reasoning": "xhigh",
    "full_original_review": True, "original_closed": False, "no_scope_reduction": True,
    "no_hot_feedback_to94_or95": True,
}
save(R / "round97-P16-full-review-length-recovery-preparation-20261005.json", prep)
print(json.dumps({k: prep[k] for k in ["directory", "task_sha256", "argument_sha256", "argument_characters", "argument_bytes", "settings_sha256"]}, indent=2))
