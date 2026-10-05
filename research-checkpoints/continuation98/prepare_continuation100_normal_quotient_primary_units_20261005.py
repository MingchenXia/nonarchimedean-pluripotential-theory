"""Preserve exact pertinent BGM proof units and the actual normality source."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
S = R / "root-checks/continuation100-normal-quotient-supplier-primary-read-units"
F = R / "root-checks/P13.2-geometrically-unibranch-EP-supplier-for-normal-Reeb-quotients-20261005-continuation100.md"
source = R / "shared-sources/BGM-2004.03847v1-20261005-continuation69.txt"
obs = R / "root-checks/continuation100-live-normal-geometrically-unibranch-primary-observation.json"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not S.exists()
assert sha(source) == "e32b491f36d88217a8f89d156490382aa8b610b89dbbf5f645cb502dcf36f535"
lines = source.read_bytes().decode().split("\n")
S.mkdir()
units = []
for first, last in [(325, 440), (446, 512), (550, 633), (637, 783), (785, 790)]:
    p = S / f"BGM-2004.03847v1-LF{first}-{last}.txt"
    p.write_text("\n".join(lines[first - 1:last]))
    assert p.read_text() == "\n".join(lines[first - 1:last])
    units.append({
        "source": str(source), "source_sha256": sha(source),
        "primary_url": "https://arxiv.org/pdf/2004.03847v1",
        "inclusive_one_based_LF": [first, last], "literal_file": str(p),
        "literal_sha256": sha(p), "whole_pertinent_literal_body_root_read": True,
        "whole_primary_paper_root_read": False, "all_recursive_primary_proofs_root_read": False,
    })
j = json.loads(obs.read_text())
body = "\n".join(c["text"] for c in j["content"] if c["type"] == "text")
parts = body.split("--------------------------------------------------------------------------------")
assert len(parts) == 2
for part, tag, first, last in [(parts[0], "0BQ3", 24, 25), (parts[1], "0BPZ", 24, 24)]:
    found = re.findall(r"^L(\d+):.*$", part, re.M)
    assert len(found) == len(set(found))
    kept = [line for line in part.split("\n") if (m := re.match(r"^L(\d+):", line)) and first <= int(m[1]) <= last]
    assert len(kept) == last - first + 1
    p = S / f"Stacks-{tag}-rendered{first}-{last}.txt"
    p.write_text("\n".join(kept))
    units.append({
        "source": str(obs), "source_sha256": sha(obs),
        "primary_url": "https://stacks.math.columbia.edu/tag/" + tag,
        "zero_based_rendered_inclusive": [first, last], "literal_file": str(p),
        "literal_sha256": sha(p), "whole_pertinent_literal_body_root_read": True,
        "all_recursive_primary_proofs_root_read": False,
    })
(S / "source-read-record.json").write_text(json.dumps({
    "recorded_utc": datetime.now(timezone.utc).isoformat(),
    "proposal": str(F), "proposal_sha256": sha(F), "whole_current_proposal_root_read": True,
    "units": units, "mathematics_accepted": False, "original_closed": False,
    "EP_U_established": False, "QEP_supplier_pending_review91": True,
    "no_hot_feedback_to91_or92": True,
    "source_scope": "BGM estimate and derivative proof retain general geometrically reduced scope. Section3.2 imposes an additional envelope-continuity premise. Normal implies geometrically unibranch by complete Stacks statement/proof and definition.",
}, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"directory": str(S), "units": len(units),
                  "proposal_sha256": sha(F), "record_sha256": sha(S / "source-read-record.json")}, indent=2))
