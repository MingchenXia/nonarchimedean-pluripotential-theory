"""Upload only a frozen, hash-bound research manifest; keep normal Git history."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import base64
import hashlib
import json
import subprocess

G = Path('/workspace/research/github-checkpoint')
manifest_path = G / 'upload-manifest-continuation56.json'
manifest = json.loads(manifest_path.read_text())
repository = manifest['repository']
branch = manifest['branch']
assert repository == 'MingchenXia/nonarchimedean-pluripotential-theory'
assert branch == 'codex/xean-research-20261003'
base = 'repos/' + repository + '/git/'
requests = G / 'api-requests-continuation56'
requests.mkdir(exist_ok=True)

def api(endpoint, method='GET', payload=None, label='request'):
    command = ['gh', 'api', endpoint, '--method', method]
    if payload is not None:
        path = requests / (label + '.json')
        path.write_text(json.dumps(payload, ensure_ascii=False) + '\n')
        command.extend(['--input', str(path)])
    completed = subprocess.run(command, capture_output=True, text=True)
    if completed.returncode:
        raise RuntimeError(label + ': ' + completed.stderr[:2000])
    return json.loads(completed.stdout)

head = api(base + 'ref/heads/' + branch)
parent = head['object']['sha']
assert parent == manifest['expected_previous_checkpoint'], 'Remote branch moved; inspect without force.'
commit = api(base + 'commits/' + parent)
existing = api(base + 'trees/' + commit['tree']['sha'] + '?recursive=1')
assert not existing.get('truncated'), 'Existing tree is incomplete; stop before mutation.'
existing_blobs = {item['sha'] for item in existing['tree'] if item['type'] == 'blob'}
files = list(manifest['files'])
files.append({'local':str(manifest_path),
    'path':'manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation56.json',
    'sha256':hashlib.sha256(manifest_path.read_bytes()).hexdigest()})
groups = {}
entries = []
for item in files:
    path = Path(item['local'])
    data = path.read_bytes()
    assert hashlib.sha256(data).hexdigest() == item['sha256'], str(path)
    blob_sha = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    entries.append({'path':item['path'],'mode':'100644','type':'blob','sha':blob_sha})
    if blob_sha not in existing_blobs and blob_sha not in groups:
        groups[blob_sha] = item
assert len({e['path'] for e in entries}) == len(entries)
print(json.dumps({'files':len(entries),'new_unique_blobs':len(groups),
                  'reused_existing_blobs':len({e['sha'] for e in entries} & existing_blobs)}),flush=True)

def upload(blob_sha, item):
    data = Path(item['local']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == item['sha256']
    result = api(base+'blobs','POST',{'content':base64.b64encode(data).decode(),'encoding':'base64'},'blob-'+blob_sha)
    assert result['sha'] == blob_sha
    return blob_sha

with ThreadPoolExecutor(max_workers=6) as pool:
    futures = [pool.submit(upload, blob_sha, item) for blob_sha, item in groups.items()]
    for count, future in enumerate(as_completed(futures), 1):
        future.result()
        if count % 100 == 0 or count == len(futures):
            print(json.dumps({'new_blobs_uploaded':count,'total':len(futures)}),flush=True)
tree = api(base+'trees','POST',{'base_tree':commit['tree']['sha'],'tree':entries},'tree')
new_commit = api(base+'commits','POST',{
    'message':'Checkpoint local research 44-55 and launch independent P16.6/P15.2 audits',
    'tree':tree['sha'],'parents':[parent],
    'author':{'name':'Codex','email':'codex@users.noreply.github.com'}},'commit')
updated = api(base+'refs/heads/'+branch,'PATCH',{'sha':new_commit['sha'],'force':False},'ref')
assert updated['object']['sha'] == new_commit['sha']
verified = api(base+'ref/heads/'+branch)
assert verified['object']['sha'] == new_commit['sha']
remote_tree = api(base+'trees/'+tree['sha']+'?recursive=1')
assert not remote_tree.get('truncated')
actual = {e['path']:e['sha'] for e in remote_tree['tree'] if e['type']=='blob'}
assert all(actual[e['path']]==e['sha'] for e in entries)
receipt = {'verified_utc':datetime.now(timezone.utc).isoformat(),'repository':repository,'branch':branch,
    'parent_sha':parent,'commit_sha':new_commit['sha'],'tree_sha':tree['sha'],'files':len(entries),
    'new_unique_blobs':len(groups),'all_file_blob_bindings_verified_remote':True,
    'manifest_sha256':hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
    'route':'GitHub REST Git object API through installed gh',
    'branch_url':'https://github.com/'+repository+'/tree/'+branch,
    'commit_url':'https://github.com/'+repository+'/commit/'+new_commit['sha'],
    'remote_ref_verified':True,'force_update':False}
(G/'push-receipt-continuation56.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2),flush=True)
