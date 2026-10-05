"""Record the verified remote head in mutable local research fronts."""
from pathlib import Path
from datetime import datetime, timezone
import json

R = Path('/workspace/research')
receipt = json.loads((R / 'github-checkpoint/push-receipt-continuation72.json').read_text())
assert receipt['commit_sha'] == 'a4f8146014a6d2b07756dfe5ce38a66721650800'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
now = datetime.now(timezone.utc).isoformat()
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    d = json.loads(p.read_text())
    d['updated_utc'] = now
    if name == 'active-work.json':
        d['github_checkpoint'] = receipt
        d['github_pending_checkpoint'] = None
    else:
        d['latest_verified_github_checkpoint'] = receipt
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'verified_head': receipt['commit_sha'], 'fronts_updated': True}))
