"""Finish existing blob upload using small deterministic tree patches and normal Git history."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time

G = Path('/workspace/research/github-checkpoint')
M = G / 'upload-manifest-continuation56.json'
assert hashlib.sha256(M.read_bytes()).hexdigest() == '4aabe1b32f84b320a45e88f224ec0d160b4b42f3d5d81c7fdf6a985d9d70b953'
m = json.loads(M.read_text())
repository, branch = m['repository'], m['branch']
base = 'repos/' + repository + '/git/'
R = G / 'chunked-tree-recovery-continuation56'
R.mkdir(exist_ok=True)
last_write = 0.0

def api(endpoint, method='GET', payload=None, label='request'):
    global last_write
    response = R / (label + '-response.json')
    if method == 'POST' and response.exists():
        return json.loads(response.read_text())
    cmd = ['gh', 'api', endpoint, '--method', method]
    if payload is not None:
        p = R / (label + '-request.json')
        data = (json.dumps(payload, ensure_ascii=False) + '\n').encode()
        if p.exists():
            assert p.read_bytes() == data
        else:
            p.write_bytes(data)
        cmd.extend(['--input', str(p)])
    for attempt in range(3):
        if method != 'GET':
            time.sleep(max(0, 8 - (time.monotonic() - last_write)))
        result = subprocess.run(cmd, capture_output=True, text=True)
        if method != 'GET':
            last_write = time.monotonic()
        (R / (label + '-attempt' + str(attempt) + '.stderr.txt')).write_text(result.stderr)
        if result.returncode == 0:
            value = json.loads(result.stdout)
            if method == 'POST':
                response.write_text(json.dumps(value, indent=2) + '\n')
            return value
        if any('HTTP ' + str(code) in result.stderr for code in (502,503,504)) and attempt < 2:
            print(json.dumps({'transient_server_error': label, 'attempt': attempt}), flush=True)
            continue
        raise RuntimeError(label + ': ' + result.stderr[:2000])

parent = api(base + 'ref/heads/' + branch)['object']['sha']
assert parent == m['expected_previous_checkpoint']
parent_commit = api(base + 'commits/' + parent)
entries = json.loads((G / 'bulk-recovery-continuation56/final-tree-request.json').read_text())['tree']
files = m['files'] + [{'local': str(M), 'path': 'manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation56.json', 'sha256': hashlib.sha256(M.read_bytes()).hexdigest()}]
expected = {}
for f in files:
    data = Path(f['local']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == f['sha256'], f['local']
    expected[f['path']] = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
assert len(entries) == len(expected) == 2476
assert all(expected[e['path']] == e['sha'] for e in entries)
tree_sha = parent_commit['tree']['sha']
chunks = [entries[i:i+250] for i in range(0,len(entries),250)]
for index, chunk in enumerate(chunks):
    result = api(base + 'trees', 'POST', {'base_tree': tree_sha, 'tree': chunk}, 'tree-stage-' + str(index))
    tree_sha = result['sha']
    print(json.dumps({'tree_stage': index+1, 'stages': len(chunks), 'tree_sha': tree_sha}), flush=True)
assert tree_sha == '6fcdab8f7c749197532813b3bb6abfd86e0118f9'
remote = api(base + 'trees/' + tree_sha + '?recursive=1')
assert not remote.get('truncated')
actual = {e['path']: e['sha'] for e in remote['tree'] if e['type'] == 'blob'}
assert all(actual[p] == s for p,s in expected.items())
commit = api(base + 'commits', 'POST', {'message': 'Checkpoint frozen research 44-55 and independent audit launches', 'tree': tree_sha, 'parents': [parent], 'author': {'name':'Codex','email':'codex@users.noreply.github.com'}}, 'commit')
assert api(base + 'ref/heads/' + branch)['object']['sha'] == parent
updated = api(base + 'refs/heads/' + branch, 'PATCH', {'sha': commit['sha'], 'force': False}, 'ref')
assert updated['object']['sha'] == commit['sha']
assert api(base + 'ref/heads/' + branch)['object']['sha'] == commit['sha']
receipt = {'verified_utc': datetime.now(timezone.utc).isoformat(), 'repository': repository, 'branch': branch, 'parent_sha': parent, 'commit_sha': commit['sha'], 'tree_sha': tree_sha, 'files': len(entries), 'all_file_blob_bindings_verified_remote': True, 'manifest_sha256': hashlib.sha256(M.read_bytes()).hexdigest(), 'route': 'Documented bulk UTF8 blob creation, existing binary blob verification, small sequential tree patches; preserved native authentication', 'remote_ref_verified': True, 'force_update': False, 'commit_url': 'https://github.com/' + repository + '/commit/' + commit['sha']}
(G / 'push-receipt-continuation56.json').write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps(receipt, indent=2), flush=True)
