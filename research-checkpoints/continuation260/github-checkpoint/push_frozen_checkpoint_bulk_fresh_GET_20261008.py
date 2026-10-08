"""Upload one authorized frozen research checkpoint and verify its exact Git tree."""
from pathlib import Path
from datetime import datetime, timezone
import base64
import hashlib
import json
import os
import subprocess
import time
import sys
import re

G=Path('/workspace/research/github-checkpoint')
assert len(sys.argv)==3
M=Path(sys.argv[1]);expected_manifest_sha256=sys.argv[2]
assert M.parent==G and re.fullmatch(r'upload-manifest-continuation[0-9]+\.json',M.name)
assert re.fullmatch(r'[0-9a-f]{64}',expected_manifest_sha256)
assert hashlib.sha256(M.read_bytes()).hexdigest()==expected_manifest_sha256
label=M.stem.removeprefix('upload-manifest-')
m=json.loads(M.read_text())
repository,branch=m['repository'],m['branch']
assert repository=='MingchenXia/nonarchimedean-pluripotential-theory'
assert branch=='codex/xean-research-20261003'
base='repos/'+repository+'/git/'
R=G/('api-recovery-'+label);R.mkdir(exist_ok=True)
last_write=0.0
def api(endpoint,method='GET',payload=None,label='request'):
    global last_write
    saved=R/(label+'-response.json')
    if method=='POST' and saved.exists():return json.loads(saved.read_text())
    if method=='GET':
        endpoint += ('&' if '?' in endpoint else '?')+'checkpoint_verification='+str(time.time_ns())
    cmd=['gh','api',endpoint,'--method',method]
    if method=='GET':cmd.extend(['--header','Cache-Control: no-cache'])
    if payload is not None:
        p=R/(label+'-request.json');data=(json.dumps(payload,ensure_ascii=False)+'\n').encode()
        if p.exists():assert p.read_bytes()==data
        else:p.write_bytes(data)
        cmd.extend(['--input',str(p)])
    for attempt in range(3):
        if method!='GET':time.sleep(max(0,8-(time.monotonic()-last_write)))
        r=subprocess.run(cmd,capture_output=True,text=True)
        if method!='GET':last_write=time.monotonic()
        (R/(label+'-attempt'+str(attempt)+'.stderr.txt')).write_text(r.stderr)
        if r.returncode==0:
            value=json.loads(r.stdout)
            if method=='POST':saved.write_text(json.dumps(value,indent=2)+'\n')
            return value
        if any('HTTP '+str(c) in r.stderr for c in [502,503,504]) and attempt<2:continue
        raise RuntimeError(label+': '+r.stderr[:2000])

parent=api(base+'ref/heads/'+branch)['object']['sha'];assert parent==m['expected_previous_checkpoint']
pc=api(base+'commits/'+parent)
existing=api(base+'trees/'+pc['tree']['sha']+'?recursive=1');assert not existing.get('truncated')
available={e['sha'] for e in existing['tree'] if e['type']=='blob'}
files=m['files']+[{'local':str(M),'path':'manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-'+label+'.json','sha256':hashlib.sha256(M.read_bytes()).hexdigest()}]
entries=[];groups={}
for item in files:
    data=Path(item['local']).read_bytes();assert hashlib.sha256(data).hexdigest()==item['sha256'],item['local']
    sha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    entries.append({'path':item['path'],'mode':'100644','type':'blob','sha':sha});groups.setdefault(sha,item)
assert len(entries)==m['file_count']+1 and len({e['path'] for e in entries})==len(entries)

# Build the same tree locally from the verified parent checkpoint tree.
task_env=dict(os.environ);task_env['GIT_INDEX_FILE']=str(G/('native-'+label+'.index'))
git=['git','--git-dir='+str(G/'native-continuation56.git')]
subprocess.run(git+['read-tree',pc['tree']['sha']],env=task_env,check=True,capture_output=True)
for sha,item in groups.items():
    p=Path(item['local']);r=subprocess.run(git+['hash-object','-w',str(p)],env=task_env,capture_output=True,text=True,check=True);assert r.stdout.strip()==sha
for entry in entries:
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',entry['sha'],entry['path']],env=task_env,check=True,capture_output=True)
expected_tree=subprocess.run(git+['write-tree'],env=task_env,check=True,capture_output=True,text=True).stdout.strip()
(R/'independent-tree-binding.json').write_text(json.dumps({'parent':parent,'base_tree':pc['tree']['sha'],'expected_tree':expected_tree,'files':len(entries)},indent=2)+'\n')
texts=[];binaries=[]
for sha,item in groups.items():
    if sha in available:continue
    data=Path(item['local']).read_bytes()
    try:content=data.decode('utf-8')
    except UnicodeDecodeError:binaries.append((sha,item))
    else:texts.append({'path':sha,'mode':'100644','type':'blob','content':content})
print(json.dumps({'files':len(entries),'new_text_blobs':len(texts),'new_binary_blobs':len(binaries),'expected_tree':expected_tree}),flush=True)
chunks=[];chunk=[];size=0
for entry in texts:
    n=len(json.dumps(entry,ensure_ascii=False).encode())
    if chunk and size+n>1000000:chunks.append(chunk);chunk=[];size=0
    chunk.append(entry);size+=n
if chunk:chunks.append(chunk)
for i,chunk in enumerate(chunks):
    result=api(base+'trees','POST',{'tree':chunk},'text-'+str(i));actual={e['path']:e['sha'] for e in result['tree'] if e['type']=='blob'}
    assert all(actual[e['path']]==e['path'] for e in chunk)
for i,(sha,item) in enumerate(binaries):
    data=Path(item['local']).read_bytes();assert hashlib.sha256(data).hexdigest()==item['sha256']
    result=api(base+'blobs','POST',{'content':base64.b64encode(data).decode(),'encoding':'base64'},'binary-'+sha);assert result['sha']==sha
    print(json.dumps({'binary_uploaded':i+1,'total':len(binaries)}),flush=True)
tree=api(base+'trees','POST',{'base_tree':pc['tree']['sha'],'tree':entries},'tree');assert tree['sha']==expected_tree
remote=api(base+'trees/'+tree['sha']+'?recursive=1');assert not remote.get('truncated')
actual={e['path']:e['sha'] for e in remote['tree'] if e['type']=='blob'};assert all(actual[e['path']]==e['sha'] for e in entries)
commit=api(base+'commits','POST',{'message':m['commit_message'],'tree':tree['sha'],'parents':[parent],'author':{'name':'Codex','email':'codex@users.noreply.github.com'}},'commit')
assert api(base+'ref/heads/'+branch)['object']['sha']==parent
updated=api(base+'refs/heads/'+branch,'PATCH',{'sha':commit['sha'],'force':False},'ref');assert updated['object']['sha']==commit['sha']
assert api(base+'ref/heads/'+branch)['object']['sha']==commit['sha']
receipt={'verified_utc':datetime.now(timezone.utc).isoformat(),'repository':repository,'branch':branch,'parent_sha':parent,'commit_sha':commit['sha'],'tree_sha':tree['sha'],'files':len(entries),'manifest_sha256':hashlib.sha256(M.read_bytes()).hexdigest(),'independent_native_git_tree_verified':True,'all_file_blob_bindings_verified_remote':True,'remote_ref_verified':True,'force_update':False,'fully_solved_original_atoms':m['fully_solved_original_atoms'],'remaining_open_atoms':m['remaining_open_atoms'],'route':'Paced documented GitHub bulk UTF8 tree-content and binary-blob REST API; preserved native authentication','commit_url':'https://github.com/'+repository+'/commit/'+commit['sha']}
(G/('push-receipt-'+label+'.json')).write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2),flush=True)
