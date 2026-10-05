"""Record the verified checkpoint74 receipt in the mutable research fronts."""
from pathlib import Path
from datetime import datetime, timezone
import json

R = Path('/workspace/research')
receipt = json.loads((R / 'github-checkpoint/push-receipt-continuation74.json').read_text())
assert receipt['commit_sha'] == '9e0b62dbeefedaafd53a4ff8600641bf4590d6da'
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
