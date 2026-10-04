#!/usr/bin/env python3
"""Preserve input and LF source evidence; assemble the authoritative review body."""
from pathlib import Path
import hashlib
import json
import platform
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parent
SOURCE_ROOT = Path("/workspace/research/shared-sources")
FENCE = chr(96) * 3
sha = lambda b: hashlib.sha256(b).hexdigest()
raw_input = (ROOT / "input.json").read_bytes()
original = ROOT / "input-original.json"
if original.exists():
    assert original.read_bytes() == raw_input, "Original input changed"
else:
    original.write_bytes(raw_input)
obj = json.loads(raw_input)
assignment = obj["assignment"]
pattern = re.compile(
    r"## Primary unit: ([^\n]+)\n\nSource ([^,\n]+), LF(\d+)--(\d+); "
    r"raw SHA256 ([0-9a-f]{64})\.\n\n" + FENCE + r"text\n(.*?)\n" + FENCE,
    re.S,
)
units = list(pattern.finditer(assignment))
assert len(units) == 14, len(units)
source_dir = ROOT / "source-evidence"
source_dir.mkdir(exist_ok=True)
records = []
appendix = [
    "\n\n# Immutable primary evidence and source audit\n",
    "The supplied input strings remain unchanged in input.json and its byte-identical "
    "input-original.json copy. The source quotes below reproduce actual LF slices, "
    "without adding a final LF to the hashed slice. Form feeds and source defects are "
    "preserved. The supplied quotation strings are separately compared to those slices; "
    "the comparison outcome is recorded, rather than silently editing either source.\n",
]
for index, m in enumerate(units, 1):
    title, filename, first, last, expected, supplied = m.groups()
    first, last = int(first), int(last)
    raw = (SOURCE_ROOT / filename).read_bytes()
    lines = raw.split(b"\n")
    chunk = b"\n".join(lines[first - 1:last])
    observed = sha(chunk)
    assert observed == expected, (filename, first, last, observed, expected)
    local = f"unit-{index:02d}-{filename}-{first}-{last}.txt"
    (source_dir / local).write_bytes(chunk)
    supplied_equal = supplied.encode() == chunk
    records.append(dict(
        title=title, source_path=str(SOURCE_ROOT / filename),
        first_LF=first, last_LF=last, supplied_sha256=expected,
        observed_sha256=observed, matched=True,
        supplied_quote_equals_raw_slice=supplied_equal,
        supplied_quote_sha256=sha(supplied.encode()),
        artifact=str(Path("source-evidence") / local),
        full_source_sha256=sha(raw),
    ))
    appendix.append(
        f"\n## Primary unit {index}: {title}\n\n"
        f"Source: {filename}, LF{first}--{last}. Supplied and observed raw SHA256: "
        f"{observed}. Literal supplied quote equals LF slice: {supplied_equal}.\n\n"
        + FENCE + "text\n" + chunk.decode() + "\n" + FENCE + "\n"
    )
    if not supplied_equal:
        appendix.append("\nLiteral supplied quote, separately preserved:\n\n"
                        + FENCE + "text\n" + supplied + "\n" + FENCE + "\n")

extras = [
    ("BEGZ-0812.3674v2-20261004.txt", 180, 248,
     "Local nonpluripolar definition, including no pluripolar mass"),
    ("BEGZ-0812.3674v2-20261004.txt", 325, 442,
     "Proposition 1.6 and full Theorem 1.8 closedness proof"),
    ("BEGZ-0812.3674v2-20261004.txt", 525, 578,
     "Global potentials and minimal singularity reference"),
    ("Vu-2004.11111v1-20261004.txt", 273, 287,
     "Literal Condition (*) definition and constant-sequence example"),
    ("Vu-2005.13241v3-20261004.txt", 53, 78,
     "Definition of the weight family W-minus"),
]
for filename, first, last, title in extras:
    raw = (SOURCE_ROOT / filename).read_bytes()
    chunk = b"\n".join(raw.split(b"\n")[first - 1:last])
    observed = sha(chunk)
    local = f"extra-{filename}-{first}-{last}.txt"
    (source_dir / local).write_bytes(chunk)
    records.append(dict(
        title=title, source_path=str(SOURCE_ROOT / filename),
        first_LF=first, last_LF=last, observed_sha256=observed,
        artifact=str(Path("source-evidence") / local),
        full_source_sha256=sha(raw), supplied_sha256=None,
    ))
    appendix.append(
        f"\n## Additional foundation: {title}\n\n"
        f"Source: {filename}, LF{first}--{last}; observed raw SHA256: {observed}.\n\n"
        + FENCE + "text\n" + chunk.decode() + "\n" + FENCE + "\n"
    )
audit = {
    "input_sha256": sha(raw_input),
    "input_original_sha256": sha(original.read_bytes()),
    "input_byte_identical": True,
    "LF_slice_rule": "join raw.split(b'\\n')[first-1:last] without final LF",
    "supplied_units": len(units),
    "source_units": records,
    "visual_checks": [
        "Vu-2004.11111v1-page4.png: source dc=i/(2pi), ddc=i/pi.",
        "Vu-2005.13241v3-page4.png: Eq(2.3) has factor 1/2.",
        "Vu-2005.13241v3-page6.png: repeated Q_k expansions omit factor 1/2.",
    ],
    "source_proofs_by_reference": [
        "BEGZ Proposition 1.4 leaves positive multilinearity proof to the reader.",
        "Vu v3 Theorem 3.1 and Theorem 3.4 invoke earlier printed proofs.",
        "Scoped statements are used as standard foundations, not reconstructed new lemmas.",
    ],
    "unused_units": [
        "Xia Theorem 2.7 and Corollary 2.15 are preserved but not essential.",
        "Vu v1 Proposition 4.2 and Theorem 4.4 are not applied.",
    ],
    "external_standard_foundation_without_local_primary_copy":
        "Smooth compact-Kahler ddc lemma, exact statement and citation in Section 6; "
        "not a new theorem, and not independently source-verified from a local DGMS copy.",
}
(ROOT / "source-audit.json").write_text(json.dumps(audit, indent=2) + "\n")
(ROOT / "P15.2-argument.md").write_text(
    (ROOT / "P15.2-main.md").read_text() + "".join(appendix))
(ROOT / "author-audit.json").write_text(json.dumps({
    "author": "native Codex assistant in assigned workspace",
    "requested_execution": "Xean native Codex gpt-6.1-sol xhigh",
    "model_identity_verification": "No callable identity attestation exposed; no additional model invoked.",
    "subagents": 0, "network_requests": 0, "installs": 0,
    "external_messages": 0, "auth_proxy_CA_HOME_CODEX_HOME_changes": 0,
    "SQL_runtime_edits": 0, "old_artifact_writes": 0,
    "observed_workspace": str(ROOT),
    "instructions_source": "Unchanged input.json assignment and task",
    "catalogue_claims_used_as_theorems": [],
    "independent_review": "None; this is an unverified draft.",
    "skill": "/run/codex-environment/codex-home/plugins/cache/openai-curated-remote/"
             "cloud-environment/0.1.2/skills/runtime/SKILL.md",
    "runtime_skill_execution": "Read-only skill inspection; environment_status tool unavailable.",
}, indent=2) + "\n")
(ROOT / "environment.json").write_text(json.dumps({
    "platform": platform.platform(), "python": sys.version,
    "tools": {t: shutil.which(t) for t in
              ["python", "pandoc", "pdflatex", "pdfinfo", "pdftotext"]},
    "supervised_heavy_compute": "No facility used or needed for this analytic assignment.",
    "workload": "Light source hashing, exact finite coefficient diagnostics, two TeX passes.",
}, indent=2) + "\n")
print(json.dumps({"input_preserved": True, "supplied_hashes_verified": len(units),
                  "additional_units": len(extras),
                  "argument_bytes": (ROOT / "P15.2-argument.md").stat().st_size}))
