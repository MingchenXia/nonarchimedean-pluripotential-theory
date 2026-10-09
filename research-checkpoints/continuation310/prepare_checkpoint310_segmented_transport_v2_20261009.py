"""Preserve frozen310 mathematics; split only oversized transport, never alter source."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,subprocess,os

R=Path('/workspace/research');G=R/'github-checkpoint'
V=G/'continuation310-segmented-transport-v2';D=G/'api-recovery-continuation310-v2'
M=G/'upload-manifest-continuation310-v2.json'
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
old=load(G/'upload-manifest-continuation310.json');prior=load(G/'api-recovery-continuation310/connector-plan.json')
assert not V.exists() and not D.exists() and not M.exists()
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for n in ['active-work.json','checklist-current.json']:
 y=load(R/n);assert y['github_pending_checkpoint']['continuation']==310 and y['latest_verified_github_checkpoint']['continuation']==309
 assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
V.mkdir();D.mkdir()
files=[];split=[]
for e in old['files']:
 p=Path(e['local']);assert sha(p)==e['sha256'] and p.stat().st_size==e['bytes']
 assert 'LOCALONLY' not in e['path'] and 'primary-data' not in e['path']
 if e['bytes']<=1000000:
  files.append(e);continue
 assert p.name=='proof-companion.txt'
 data=p.read_bytes();off=0;parts=[]
 folder=V/'proof-companion.txt.parts';folder.mkdir()
 while off<len(data):
  end=min(off+180000,len(data))
  while end<len(data) and data[end]&192==128:end-=1
  body=data[off:end];body.decode('utf-8')
  q=folder/f'part-{len(parts)+1:03d}.txt';q.write_bytes(body)
  f=dict(local=str(q),path=e['path']+'.parts/'+q.name,bytes=len(body),sha256=sha(q))
  files.append(f);parts.append(f);off=end
 assert b''.join(Path(f['local']).read_bytes() for f in parts)==data
 split.append(dict(original=e,ordered_parts=parts,reconstruction='Concatenate UTF-8 bytes in exact ordered_parts order with NO added separators or newlines.',whole_sha256=e['sha256'],whole_bytes=e['bytes'],whole_body_locally_retained=True,whole_body_present_across_all_public_parts=True,mathematical_reading_credit=False))
assert len(split)==1
now=datetime.now(timezone.utc).isoformat()
write(V/'whole-companion-reconstruction.json',dict(recorded_utc=now,split_files=split,reason='Single oversized connector requests repeatedly interrupted; exact byte-preserving bounded transport.',original_frozen_manifest_sha256=sha(G/'upload-manifest-continuation310.json'),original_frozen_packet_unchanged=True,accepted=False,original_closed=False))
(V/'README.md').write_text('Checkpoint310 transport v2\n\nThe complete working papers431432433 and frozen299 metadata are unchanged. The 7,084,039-byte ROOT432 proof companion is transported as ordered UTF-8 parts, concatenated without added separators. whole-companion-reconstruction.json binds EVERYpart and the exact original whole SHA256. The original frozen manifest and all original bodies remain retained. Earlier oversized connector requests were interrupted; no successful branch update was inferred. Source claims/counts/primary exclusions/protected editor remain unchanged. This transport record gives NO mathematical reading, acceptance, closure or compilation credit. Native298 and299 mathematics remain uninspected by ROOT at this freeze. NONFORCE publication still requires native Git root, all remote paths and final ref verification.\n')
extra=[(V/'whole-companion-reconstruction.json','whole-companion-reconstruction.json'),(V/'README.md','transport-v2-README.md'),(G/'upload-manifest-continuation310.json','transport-v1-frozen-manifest.json'),(Path(__file__),'prepare_checkpoint310_segmented_transport_v2_20261009.py')]
for p,n in extra:files.append(dict(local=str(p),path='research-checkpoints/continuation310/'+n,bytes=p.stat().st_size,sha256=sha(p)))
write(M,dict(generated_utc=now,repository=old['repository'],branch=old['branch'],expected_previous_checkpoint=prior['parent'],files=files,file_count=len(files),transport_version=2,whole_companion_binding=split,original_frozen_manifest_sha256=sha(G/'upload-manifest-continuation310.json'),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message=old['commit_message'],scope=old['scope'],oversized_single_blob_not_required=True,exact_whole_body_reconstructible=True))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation310.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')];env=dict(os.environ);env['GIT_INDEX_FILE']=str(G/'native-continuation310-v2.index')
subprocess.run(git+['read-tree',prior['base_tree']],env=env,capture_output=True,check=True)
entries=[];groups={}
for e in items:
 body=Path(e['local']).read_bytes();body.decode();assert hashlib.sha256(body).hexdigest()==e['sha256']
 h=hashlib.sha1(b'blob '+str(len(body)).encode()+b'\0'+body).hexdigest()
 assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
 entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h));groups.setdefault(h,e)
 subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=env,capture_output=True,text=True,check=True).stdout.strip()
already={x['path'] for i in range(prior['content_chunks']) if i!=7 for x in load(G/f'api-recovery-continuation310/content-chunk-{i}.json')['tree']}
chunks=[];batch=[];size=0
for h,e in groups.items():
 if h in already:continue
 x=dict(path=h,mode='100644',type='blob',content=Path(e['local']).read_text());n=len(json.dumps(x,ensure_ascii=True).encode())
 if batch and size+n>230000:chunks.append(batch);batch=[];size=0
 batch.append(x);size+=n
if batch:chunks.append(batch)
sizes=[]
for i,ch in enumerate(chunks):
 p=D/f'content-chunk-{i}.json';p.write_text(json.dumps(dict(tree=ch),ensure_ascii=True,indent=2)+'\n');sizes.append(p.stat().st_size)
write(D/'connector-plan.json',dict(repository=old['repository'],branch=old['branch'],parent=prior['parent'],base_tree=prior['base_tree'],expected_tree=expected,manifest_sha256=sha(M),entries=entries,content_chunks=len(chunks),content_chunk_bytes=sizes,existing_content_chunks=[dict(directory=str(G/'api-recovery-continuation310'),chunk=i) for i in range(prior['content_chunks']) if i!=7],unique_blobs=len(groups),commit_message=old['commit_message'],force=False,transport_version=2))
for n in ['active-work.json','checklist-current.json']:
 p=R/n;y=load(p);y['github_pending_checkpoint'].update(transport_version=2,manifest=str(M),expected_tree=expected,oversized_single_blob_not_required=True);y['updated_utc']=now;write(p,y)
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),actual_files=len(items),unique_blobs=len(groups),new_content_chunks=len(chunks),max_chunk_bytes=max(sizes),split_parts=len(split[0]['ordered_parts']),expected_tree=expected,counts_unchanged=True),indent=2))
