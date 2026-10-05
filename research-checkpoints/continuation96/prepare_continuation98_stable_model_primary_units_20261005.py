"""Extract exact rendered primary bodies and record honest reading limits."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

R = Path("/workspace/research")
S = R / "root-checks/continuation98-stable-model-primary-read-units"
live = R / "root-checks/continuation98-live-stable-modification-primary-observation.json"
F = R / "root-checks/P16.1-stable-domination-of-the-specified-curve-graph-model-20261005-continuation98.md"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not S.exists()
S.mkdir()
units = []
block = json.loads(live.read_text())["content"][0]["text"]
old = R / "root-checks/public-P16.1-round-84-final-reader/source-extracts/e010-web-1-280.txt"
for label, source, text, first, last in [
    ("Temkin-0707.3953v3-definitions-and-projectivity",old,old.read_text(),61,201),
    ("Temkin-0707.3953v3-complete-valuation-ring-gluing",live,block,2506,2592),
]:
    selected = []
    seen = []
    for line in text.split("\n"):
        m = re.match(r"^L(\d+)@P[\d-]+:",line)
        if m and first <= int(m[1]) <= last:
            selected.append(line)
            seen.append(int(m[1]))
    assert seen == list(range(first,last+1))
    p = S / f"{label}-rendered{first}-{last}.txt"
    p.write_text("\n".join(selected))
    units.append({"source":str(source),"source_sha256":sha(source),
                  "url":"https://arxiv.org/pdf/0707.3953v3","renderer_zero_based_inclusive":[first,last],
                  "literal_file":str(p),"literal_sha256":sha(p),
                  "whole_pertinent_literal_body_root_read":True,
                  "whole_source_paper_root_read":False,"all_recursive_primary_proofs_root_read":False})
record = {
    "recorded_utc":datetime.now(timezone.utc).isoformat(),"proposal":str(F),"proposal_sha256":sha(F),
    "whole_current_proposal_root_read":True,"units":units,"mathematics_accepted":False,
    "original_closed":False,"pending_review88_hot_feedback_sent":False,
    "completed_author84_literal_e010_and_e011_whole_root_read":True,
    "completed_author84_e012_entire_literal_root_read":True,
    "all_70_author84_primary_bodies_root_read":False,
    "source_body_correction":"Frozen e012 has rendered77-156, not the claimed valuation-ring gluing proof; e011 has only the2506-2512 beginning before its disjoint excerpts. Actual complete gluing2506-2592 is freshly supplied; old snapshots/provenance are unchanged.",
    "edition":"Explicitly pinnedv3,14April2010. Latest-version status is not claimed.",
}
(S / "source-read-record.json").write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"directory":str(S),"units":len(units),"proposal_sha256":sha(F)},indent=2))
