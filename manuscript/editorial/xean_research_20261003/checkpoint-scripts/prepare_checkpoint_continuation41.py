"""Checkpoint the immutable prescribed-type research inputs and source checks."""
from pathlib import Path
import datetime, hashlib, json, shutil

r=Path('/workspace/research');cp=r/'github-checkpoint'
parent='fe9b915882f5191fe0b048f26ad8e9bdde432c0c'
active=json.loads((r/'active-work.json').read_text())
assert active['github_checkpoint']['commit_sha']==parent
assert active['selected_atoms']==['P15.1','P15.2'] and not active['full_solutions']
snapshot=cp/'continuation41-uploaded-live-records';snapshot.mkdir(exist_ok=False)
prefix='manuscript/editorial/xean_research_20261003/';files=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def add(path,target,mutable=False):
    path=Path(path);assert path.is_file(),path
    if mutable:
        copy=snapshot/(str(len(files))+'-'+path.name);shutil.copyfile(path,copy);path=copy
    assert prefix+target not in {x['path'] for x in files}
    files.append({'local':str(path),'path':prefix+target,'sha256':sha(path)})

batch_path=r/'prescribed-type-zero-volume-batch-manifest.json'
batch=json.loads(batch_path.read_text());proposal=Path(batch['proposal']);evidence=Path(batch['primary_read_record'])
assert sha(proposal)==batch['proposal_sha256']
assert sha(evidence)==batch['primary_read_record_sha256']
read=json.loads(evidence.read_text());assert len(read['primary_units'])==14
for unit in read['primary_units']:
    src=Path(unit['source_text']);assert sha(src)==unit['source_text_sha256']
    raw=b'\n'.join(src.read_bytes().split(b'\n')[unit['first_lf_line']-1:unit['last_lf_line']])
    assert raw.decode()==unit['body'] and hashlib.sha256(raw).hexdigest()==unit['raw_sha256']
    assert unit['body'] in proposal.read_text()
for path in (batch_path,proposal,evidence):
    add(path,'proposed-inputs/prescribed-type-zero-volume/'+path.name)
for c in batch['campaigns']:
    d=Path(c['directory']);n=d.parent.name
    for name in ('input.json','settings.json','input-manifest.json'):
        if name in c['inputs']:assert sha(d/name)==c['inputs'][name]
        add(d/name,n+'/research-inputs/'+name)
for name in ('Vu-2004.11111v1-20261004-provenance.json','Vu-2005.13241v1-20261004-provenance.json',
             'Vu-2005.13241v3-20261004-provenance.json','Vu-2004.11111-abstract-20261004.html',
             'Vu-2005.13241-abstract-20261004.html','Vu-2005.13241v3-page4.png',
             'Vu-2005.13241v3-page6.png','Vu-2004.11111v1-page4.png'):
    add(r/'shared-sources'/name,'source-authentication/prescribed-type-zero-volume/'+name)
for name in ('prepare_prescribed_type_zero_volume_batch.py','review_prescribed_type_zero_volume_after_completion.py','refresh_checklist.py'):
    add(r/name,'reproduction-scripts/'+name,mutable=name=='refresh_checklist.py')
add(cp/'push-receipt-continuation40.json','records/push-receipt-continuation40.json')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):
    add(r/name,name,mutable=True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name)
push=cp/'push_checkpoint_continuation41.py';assert not push.exists()
s=(cp/'push_checkpoint_continuation40.py').read_text().replace('continuation40','continuation41').replace(
    'Publish reviewed relative zero-volume fibration operator and energy papers',
    'Checkpoint prescribed-type zero-volume research and primary foundations')
push.write_text(s);add(push,'checkpoint-scripts/'+push.name)
note=snapshot/'CHECKPOINT.txt'
note.write_text('Checkpoint41: ONLY P15.1/P15.2 fresh native Xean gpt-6.1-sol xhigh '
    'research running, with complete independent reviews queued after proof freeze. '
    'General pseudoeffective prescribed-type energy/operator proposal UNVERIFIED. '
    'Fourteen exact selected primary units retained in full, with direct new Vu reads '
    'and unchanged earlier BEGZ/DDNL/Xia complete-read reuse disclosed. Vu v3 Eq2.3 '
    'has correct intrinsic half-factor; repeated printed defects and actual page visuals '
    'preserved, not silently corrected. Exact T-admissibility, positivity and source '
    'normalization are proof obligations for new applications. Finite-energy, carrier '
    'and minimum-reference requirements remain unresolved. No complete archival PDF/text '
    'or private native transcript uploaded. Previous two fibration papers remain immutable '
    'and pushed. All42originalsopen; goal ACTIVE.\n')
add(note,'CHECKPOINT.txt')
manifest={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'repository':'MingchenXia/nonarchimedean-pluripotential-theory','branch':'codex/xean-research-20261003',
    'expected_previous_checkpoint':parent,'files':files,'scope':'Frozen unverified next two-problem research inputs and complete selected primary evidence; no new theorem accepted.'}
p=cp/'upload-manifest-continuation41.json';assert not p.exists()
p.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files':len(files),'manifest':str(p),'sha256':sha(p)}))
