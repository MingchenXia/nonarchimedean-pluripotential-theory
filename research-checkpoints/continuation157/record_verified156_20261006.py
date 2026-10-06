from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
G = R / 'github-checkpoint'
d = json.loads((G / 'push-receipt-continuation156.json').read_text())
assert d['commit_sha'] == '64491545045cb58f7764b1f03d160f2e1e90c620'
assert d['parent_sha'] == 'd48fe25583fe15dd80b2fb673211a54752fec541'
assert d['tree_sha'] == 'f23ae5127ee3f94a3d395ad516e9a4d25d1a97da'
assert d['manifest_sha256'] == hashlib.sha256((G / 'upload-manifest-continuation156.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
assert d['files'] == 47 and d['force_update'] is False
for name in ('active-work.json','checklist-current.json'):
    p = R / name
    a = json.loads(p.read_text())
    assert len(a['fully_solved_original_atoms']) == 8 and a['remaining_open_original_atoms'] == 34
    assert a['historical_reviewed_scoped_papers'] == 56
    a.update({'github_checkpoint':d,'github_pending_checkpoint':None,
              'updated_utc':datetime.now(timezone.utc).isoformat()})
    p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':156,'commit_sha':d['commit_sha'],
                  'originals_solved':8,'accepted_papers':56},indent=2))
