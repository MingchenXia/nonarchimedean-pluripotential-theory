"""Freeze supplementary source reads and a future-only reference proposal."""
from pathlib import Path
import datetime,hashlib,json,shutil
r=Path('/workspace/research');cp=r/'github-checkpoint'
parent='544bd6e13f1fc8fa64ae5fba30b417dcd25e2c7b'
a=json.loads((r/'active-work.json').read_text())
assert a['github_checkpoint']['commit_sha']==parent
assert a['selected_atoms']==['P15.1','P15.2'] and not a['full_solutions']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
snapshot=cp/'continuation42-uploaded-live-records';snapshot.mkdir(exist_ok=False)
prefix='manuscript/editorial/xean_research_20261003/';files=[]
def add(p,target,mutable=False):
    p=Path(p);assert p.is_file(),p
    if mutable:
        dst=snapshot/(str(len(files))+'-'+p.name);shutil.copyfile(p,dst);p=dst
    assert prefix+target not in {x['path'] for x in files}
    files.append({'local':str(p),'path':prefix+target,'sha256':sha(p)})
proposal=r/'P15-minimum-reference-compression-future-proposal-20261004.json'
assert sha(proposal)=='4fa25b688a5622335c9e7895afca7086871cd629e7b1d96e09fb8a860ebae996'
add(proposal,'proposed-inputs/minimum-reference-compression/'+proposal.name)
for name in ('prescribed-type-relative-energy-supplementary-read-20261004.json',
             'prescribed-type-relative-energy-supplementary-read-v2-20261004.json'):
    p=r/'shared-sources'/name;j=json.loads(p.read_text());src=Path(j['source_text'])
    assert sha(src)==j['source_text_sha256']
    for u in j['units']:
        raw=b'\n'.join(src.read_bytes().split(b'\n')[u['first_lf_line']-1:u['last_lf_line']])
        assert raw.decode()==u['body'] and hashlib.sha256(raw).hexdigest()==u['raw_sha256']
    add(p,'source-authentication/prescribed-type-zero-volume/'+name)
for name in ('Vu-2004.11111v1-weighted-source-34.png','Vu-2004.11111v1-weighted-source-35.png'):
    add(r/'shared-sources'/name,'source-authentication/prescribed-type-zero-volume/'+name)
add(cp/'push-receipt-continuation41.json','records/push-receipt-continuation41.json')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):
    add(r/name,name,mutable=True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name)
push=cp/'push_checkpoint_continuation42.py';assert not push.exists()
s=(cp/'push_checkpoint_continuation41.py').read_text().replace('continuation41','continuation42').replace(
 'Checkpoint prescribed-type zero-volume research and primary foundations',
 'Checkpoint relative-energy source reads and future reference compression')
push.write_text(s);add(push,'checkpoint-scripts/'+push.name)
note=snapshot/'CHECKPOINT.txt'
note.write_text('Checkpoint42: current research remains ONLY P15.1/P15.2 through '
 'native Xean gpt-6.1-sol xhigh. Results not yet committed; independent review '
 'preparers wait for full proof freeze. Extra root source reads retain complete '
 'selected relative-energy/mixed-full-mass/weighted-continuity bodies and printed '
 'defects, with actual selected page visuals. Exact minimal-current full mass '
 'versus arbitrary-reference full mass and Kahler versus pseudoeffective scopes '
 'kept distinct. Future-only finite-dimensional polynomial energy-reference '
 'compression and full-form operator-kernel proposal is UNVERIFIED and was not '
 'injected into running workers or reviews. No new theorem acceptance, no whole '
 'archival source PDF/text or private native transcript uploaded. Earlier reviewed '
 'papers remain immutable. All42originalsopen; goal ACTIVE.\n')
add(note,'CHECKPOINT.txt')
m={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'repository':'MingchenXia/nonarchimedean-pluripotential-theory','branch':'codex/xean-research-20261003',
 'expected_previous_checkpoint':parent,'files':files,'scope':'Supplementary exact primary source reads and unverified future reference proposal only; no new theorem accepted.'}
p=cp/'upload-manifest-continuation42.json';assert not p.exists()
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files':len(files),'manifest':str(p),'sha256':sha(p)}))
