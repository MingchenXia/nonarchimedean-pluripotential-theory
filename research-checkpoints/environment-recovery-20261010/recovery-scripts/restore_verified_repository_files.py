from pathlib import Path
import json, hashlib, shutil
repo = Path('/workspace/recovered-research-repository')
root = Path('/workspace/research')
base = repo / 'manuscript/editorial/xean_research_20261003'
records, errors, verified = [], [], {}
def digest(b):
    return hashlib.sha256(b).hexdigest()
def retain(entry, payload, source):
    local = entry.get('local')
    expected = entry.get('sha256')
    if not local or not expected or not local.startswith('/workspace/research/'):
        return
    target = Path(local)
    if root not in target.parents or '..' in target.parts:
        raise ValueError('unsafe recovery path')
    if digest(payload) != expected or len(payload) != entry.get('bytes', len(payload)):
        errors.append({'source': source, 'local': local, 'error': 'hash or length mismatch'})
        return
    if target.exists() and digest(target.read_bytes()) != expected:
        records.append({'local': local, 'sha256': expected, 'status': 'historical revision retained only in repository', 'source': source})
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        target.write_bytes(payload)
    verified[expected] = local
    records.append({'local': local, 'sha256': expected, 'bytes': len(payload), 'status': 'byte-exact recovered', 'source': source})
manifests = list(base.glob('UPLOAD_MANIFEST*.json'))
def order(p):
    import re
    m = re.search(r'continuation(\d+)', p.name)
    return (int(m.group(1)) if m else -1, p.name)
for path in sorted(manifests, key=order, reverse=True):
    data = json.loads(path.read_text())
    entries = data.get('files', [])
    for e in entries:
        if not isinstance(e, dict) or not isinstance(e.get('path'), str):
            continue
        source = repo / e['path']
        if repo not in source.parents or not source.is_file():
            errors.append({'manifest': path.name, 'path': e.get('path'), 'error': 'payload absent'})
            continue
        retain(e, source.read_bytes(), str(source))
    for binding in data.get('whole_body_binding', []):
        original = binding.get('original', {})
        indices = binding.get('ordered_file_indices', [])
        if not indices:
            continue
        try:
            parts = [repo / entries[i]['path'] for i in indices]
            payload = b''.join(p.read_bytes() for p in parts)
            retain(original, payload, path.name + ':ordered-parts')
        except (KeyError, IndexError, OSError) as exc:
            errors.append({'manifest': path.name, 'error': str(exc)})
report = {'manifests': len(manifests), 'verified_unique_hashes': len(verified), 'records': records, 'errors': errors, 'mathematical_reading_or_acceptance_credit': False, 'supplied_programs_executed': False}
out = root / 'recovery-LOCALONLY/verified-file-recovery.json'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'manifests':len(manifests), 'verified_unique_hashes':len(verified), 'recovered_records':len(records), 'errors':len(errors), 'report':str(out)}))
