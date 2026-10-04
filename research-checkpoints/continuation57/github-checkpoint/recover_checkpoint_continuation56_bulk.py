"""Recover frozen checkpoint56 with documented bulk text-tree writes and paced API calls."""
from pathlib import Path
from datetime import datetime, timezone
import base64
import hashlib
import json
import subprocess
import time

G = Path('/workspace/research/github-checkpoint')
M = G / 'upload-manifest-continuation56.json'
assert hashlib.sha256(M.read_bytes()).hexdigest() == '4aabe1b32f84b320a45e88f224ec0d160b4b42f3d5d81c7fdf6a985d9d70b953'
manifest = json.loads(M.read_text())
repository = manifest['repository']
branch = manifest['branch']
assert repository == 'MingchenXia/nonarchimedean-pluripotential-theory'
assert branch == 'codex/xean-research-20261003'
base = 'repos/' + repository + '/git/'
R = G / 'bulk-recovery-continuation56'
R.mkdir(exist_ok=True)
last_write = 0.0

def event(value):
    value['utc'] = datetime.now(timezone.utc).isoformat()
    with (R / 'events.jsonl').open('a') as f:
        f.write(json.dumps(value) + '\n')
    print(json.dumps(value), flush=True)

def api(endpoint, method='GET', payload=None, label='request', scalar=False):
    global last_write
    response_file = R / (label + '-response.json')
    if method == 'POST' and response_file.exists():
        return json.loads(response_file.read_text())
    command = ['gh', 'api', endpoint, '--method', method]
    if payload is not None:
        request_file = R / (label + '-request.json')
        request_bytes = (json.dumps(payload, ensure_ascii=False) + '\n').encode()
        if request_file.exists():
            assert request_file.read_bytes() == request_bytes
        else:
            request_file.write_bytes(request_bytes)
        command.extend(['--input', str(request_file)])
    if scalar:
        command.extend(['--jq', '.sha'])
    for attempt in range(3):
        if method != 'GET':
            time.sleep(max(0, 8 - (time.monotonic() - last_write)))
        result = subprocess.run(command, capture_output=True, text=True)
        if method != 'GET':
            last_write = time.monotonic()
        (R / (label + '-attempt' + str(attempt) + '.stderr.txt')).write_text(result.stderr)
        if result.returncode == 0:
            if scalar:
                return result.stdout.strip()
            value = json.loads(result.stdout)
            if method == 'POST':
                response_file.write_text(json.dumps(value, indent=2) + '\n')
            return value
        if scalar and 'HTTP 404' in result.stderr:
            return None
        if 'HTTP 403' in result.stderr and ('rate limit' in result.stderr.lower()) and attempt < 2:
            event({'state': 'GitHub rate limit; respecting cooldown', 'label': label, 'attempt': attempt})
            for _ in range(5):
                time.sleep(60)
            continue
        raise RuntimeError(label + ': ' + result.stderr[:2000])

parent = api(base + 'ref/heads/' + branch)['object']['sha']
assert parent == manifest['expected_previous_checkpoint'], 'Remote moved; inspect without force.'
parent_commit = api(base + 'commits/' + parent)
existing = api(base + 'trees/' + parent_commit['tree']['sha'] + '?recursive=1')
assert not existing.get('truncated')
available = {e['sha'] for e in existing['tree'] if e['type'] == 'blob'}
files = manifest['files'] + [{'local': str(M), 'path': 'manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation56.json', 'sha256': hashlib.sha256(M.read_bytes()).hexdigest()}]
entries = []
groups = {}
for item in files:
    data = Path(item['local']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == item['sha256'], item['local']
    sha = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    entries.append({'path': item['path'], 'mode': '100644', 'type': 'blob', 'sha': sha})
    groups.setdefault(sha, item)
assert len(entries) == 2476 and len({e['path'] for e in entries}) == len(entries)
text_entries = []
binary = []
for sha, item in groups.items():
    if sha in available:
        continue
    data = Path(item['local']).read_bytes()
    try:
        content = data.decode('utf-8')
    except UnicodeDecodeError:
        binary.append((sha, item))
    else:
        text_entries.append({'path': sha, 'mode': '100644', 'type': 'blob', 'content': content})
event({'state': 'validated', 'files': len(entries), 'unique_text_blobs': len(text_entries), 'unique_binary_blobs': len(binary)})

chunks = []
chunk = []
size = 0
for entry in text_entries:
    entry_size = len(json.dumps(entry, ensure_ascii=False).encode())
    if chunk and size + entry_size > 1000000:
        chunks.append(chunk)
        chunk, size = [], 0
    chunk.append(entry)
    size += entry_size
if chunk:
    chunks.append(chunk)
for index, chunk in enumerate(chunks):
    value = api(base + 'trees', 'POST', {'tree': chunk}, 'text-stage-' + str(index))
    actual = {e['path']: e['sha'] for e in value['tree'] if e['type'] == 'blob'}
    assert all(actual[e['path']] == e['path'] for e in chunk)
    available.update(actual.values())
    event({'state': 'text stage verified', 'stage': index + 1, 'stages': len(chunks), 'blobs': len(chunk)})
for index, (sha, item) in enumerate(binary):
    found = api(base + 'blobs/' + sha, label='binary-exists-' + sha, scalar=True)
    if found is None:
        data = Path(item['local']).read_bytes()
        assert hashlib.sha256(data).hexdigest() == item['sha256']
        value = api(base + 'blobs', 'POST', {'content': base64.b64encode(data).decode(), 'encoding': 'base64'}, 'binary-' + sha)
        assert value['sha'] == sha
    else:
        assert found == sha
    available.add(sha)
    if (index + 1) % 10 == 0 or index + 1 == len(binary):
        event({'state': 'binary objects verified', 'verified': index + 1, 'total': len(binary)})
assert all(e['sha'] in available for e in entries)
tree = api(base + 'trees', 'POST', {'base_tree': parent_commit['tree']['sha'], 'tree': entries}, 'final-tree')
assert tree['sha'] == '6fcdab8f7c749197532813b3bb6abfd86e0118f9', 'API tree differs from independently built native Git tree.'
commit = api(base + 'commits', 'POST', {'message': 'Checkpoint frozen research 44-55 and independent audit launches', 'tree': tree['sha'], 'parents': [parent], 'author': {'name': 'Codex', 'email': 'codex@users.noreply.github.com'}}, 'final-commit')
assert api(base + 'ref/heads/' + branch)['object']['sha'] == parent, 'Remote moved; inspect without force.'
updated = api(base + 'refs/heads/' + branch, 'PATCH', {'sha': commit['sha'], 'force': False}, 'final-ref')
assert updated['object']['sha'] == commit['sha']
assert api(base + 'ref/heads/' + branch)['object']['sha'] == commit['sha']
remote = api(base + 'trees/' + tree['sha'] + '?recursive=1')
assert not remote.get('truncated')
actual = {e['path']: e['sha'] for e in remote['tree'] if e['type'] == 'blob'}
assert all(actual[e['path']] == e['sha'] for e in entries)
receipt = {'verified_utc': datetime.now(timezone.utc).isoformat(), 'repository': repository, 'branch': branch, 'parent_sha': parent, 'commit_sha': commit['sha'], 'tree_sha': tree['sha'], 'files': len(entries), 'all_file_blob_bindings_verified_remote': True, 'manifest_sha256': hashlib.sha256(M.read_bytes()).hexdigest(), 'route': 'Documented GitHub REST bulk UTF8 tree content and paced binary blob API, preserving native authentication', 'remote_ref_verified': True, 'force_update': False, 'commit_url': 'https://github.com/' + repository + '/commit/' + commit['sha']}
(G / 'push-receipt-continuation56.json').write_text(json.dumps(receipt, indent=2) + '\n')
event(receipt)
