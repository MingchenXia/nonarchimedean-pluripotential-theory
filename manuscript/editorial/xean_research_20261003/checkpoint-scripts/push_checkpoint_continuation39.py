"""Push immutable research files with GitHub's ordinary Git object API."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import base64,datetime,hashlib,json,subprocess

ROOT=Path('/workspace/research/github-checkpoint')
MANIFEST=ROOT/'upload-manifest-continuation39.json'
manifest=json.loads(MANIFEST.read_text())
repository=manifest['repository'];branch=manifest['branch']
base='repos/'+repository+'/git/'
requests=ROOT/'api-requests-continuation39';requests.mkdir(exist_ok=True)

def api(endpoint,method='GET',payload=None,label='request'):
    cmd=['gh','api',endpoint,'--method',method]
    if payload is not None:
        p=requests/(label+'.json')
        p.write_text(json.dumps(payload,ensure_ascii=False)+'\n')
        cmd+=['--input',str(p)]
    result=subprocess.run(cmd,capture_output=True,text=True)
    if result.returncode:
        raise RuntimeError(label+': '+result.stderr[:2000])
    return json.loads(result.stdout)

head=api(base+'ref/heads/'+branch)
parent=head['object']['sha']
assert parent==manifest['expected_previous_checkpoint'], 'Remote branch moved; inspect before retrying.'
commit=api(base+'commits/'+parent)
files=list(manifest['files'])
prefix='manuscript/editorial/xean_research_20261003'
files.append({'local':str(MANIFEST),'path':prefix+'/UPLOAD_MANIFEST-continuation39.json',
              'sha256':hashlib.sha256(MANIFEST.read_bytes()).hexdigest()})

def blob(item):
    data=Path(item['local']).read_bytes()
    assert hashlib.sha256(data).hexdigest()==item['sha256']
    expected=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    result=api(base+'blobs','POST',{'content':base64.b64encode(data).decode(),
               'encoding':'base64'},'blob-'+expected)
    assert result['sha']==expected
    return {'path':item['path'],'mode':'100644','type':'blob','sha':expected}

with ThreadPoolExecutor(max_workers=6) as pool:
    entries=list(pool.map(blob,files))
print(json.dumps({'uploaded_blobs':len(entries),'parent':parent}),flush=True)
tree=api(base+'trees','POST',{'base_tree':commit['tree']['sha'],'tree':entries},'tree')
new_commit=api(base+'commits','POST',{
    'message':'Checkpoint prescribed-type source evidence and unresolved extension',
    'tree':tree['sha'],'parents':[parent],
    'author':{'name':'Codex','email':'codex@users.noreply.github.com'}},'commit')
updated=api(base+'refs/heads/'+branch,'PATCH',{'sha':new_commit['sha'],'force':False},'ref')
assert updated['object']['sha']==new_commit['sha']
verified=api(base+'ref/heads/'+branch)
assert verified['object']['sha']==new_commit['sha']
record={'verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'repository':repository,'branch':branch,'parent_sha':parent,
        'commit_sha':new_commit['sha'],'tree_sha':tree['sha'],'files':len(entries),
        'manifest_sha256':hashlib.sha256(MANIFEST.read_bytes()).hexdigest(),
        'route':'GitHub REST Git blob/tree/commit/ref API through installed gh; native Git transport HTTP401 preserved separately',
        'branch_url':'https://github.com/'+repository+'/tree/'+branch,
        'commit_url':'https://github.com/'+repository+'/commit/'+new_commit['sha'],
        'remote_ref_verified':True,'force_update':False}
(ROOT/'push-receipt-continuation39.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
