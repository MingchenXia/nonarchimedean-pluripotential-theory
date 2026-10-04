from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

R=Path('/workspace/research')
prior=R/'P03-curve-final-source-applications-root-read-20261004.json'
record=json.loads(prior.read_text())
corrected=[]
for old in record['earlier_indispensable_foundation_reads']:
    candidates=[R/'shared-sources'/Path(old).name,R/'root-checks'/Path(old).name]
    actual=[p for p in candidates if p.is_file()]
    assert len(actual)==1,(old,actual)
    p=actual[0]
    corrected.append({'recorded_path':old,'correct_path':str(p),
                      'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
out=R/'P03-curve-final-source-applications-root-read-20261004.paths-addendum.json'
assert not out.exists()
out.write_text(json.dumps({'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'prior_record':str(prior),'prior_sha256':hashlib.sha256(prior.read_bytes()).hexdigest(),
    'correction':'The four references to earlier read records omitted their shared-sources directory. The literal-unit bindings and read scopes in the prior record are unchanged. The prior record and its executed helper remain preserved.',
    'corrected_earlier_foundation_read_records':corrected,
    'mathematical_acceptance':False,'original_target_closed':False},indent=2)+'\n')
print(out)
