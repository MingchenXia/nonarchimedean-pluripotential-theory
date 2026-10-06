from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research')
G = R / 'github-checkpoint'
d = json.loads((G / 'push-receipt-continuation158.json').read_text())
assert d['commit_sha'] == 'cfefa17e769d0677d99121ee3a77bad90d8f90db'
assert d['parent_sha'] == 'be571302976172a5418ae92ce1afbb2309799600'
assert d['tree_sha'] == 'bc9e22ce0850de8f4abd8c3fae6e96da51df1804'
assert d['manifest_sha256'] == hashlib.sha256((G / 'upload-manifest-continuation158.json').read_bytes()).hexdigest()
assert all(d[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
assert d['files'] == 21 and d['force_update'] is False
for name in ('active-work.json','checklist-current.json'):
    p = R / name
    a = json.loads(p.read_text())
    assert len(a['fully_solved_original_atoms']) == 8 and a['remaining_open_original_atoms'] == 34
    assert a['historical_reviewed_scoped_papers'] == 57
    a.update({'github_checkpoint':d,'github_pending_checkpoint':None,
              'updated_utc':datetime.now(timezone.utc).isoformat()})
    p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verified_checkpoint':158,'commit_sha':d['commit_sha'],
                  'originals_solved':8,'accepted_papers':57},indent=2))
