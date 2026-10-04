"""Append native compilation success without modifying the historical paper bundle."""
from pathlib import Path
import datetime,hashlib,json,shutil
r=Path('/workspace/research');c=r/'github-checkpoint';parent='8927fe7b717dbe47f431fd2a537c40e171419931';a=json.loads((r/'active-work.json').read_text());assert a['github_checkpoint']['commit_sha']==parent and not a['full_solutions']
snap=c/'continuation31-uploaded-live-records';snap.mkdir(exist_ok=False);prefix='manuscript/editorial/xean_research_20261003/';files=[]
def add(p,target,mutable=False):
 p=Path(p);assert p.is_file()
 if mutable:
  cp=snap/(str(len(files))+'-'+p.name);shutil.copyfile(p,cp);p=cp
 files.append({'local':str(p),'path':prefix+target,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
p=r/'deliverables/round-23-native-verification-addendum.json';j=json.loads(p.read_text());assert j['native_result']['kind']=='success' and not j['source_changed_after_publication'];add(p,p.name)
add(c/'push-receipt-continuation30.json','records/push-receipt-continuation30.json')
for n in ('active-work.json','checklist-current.json','checklist-current.tsv','refresh_checklist.py'):add(r/n,n,True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name)
p=c/'push_checkpoint_continuation31.py';assert not p.exists();s=(c/'push_checkpoint_continuation30.py').read_text().replace('continuation30','continuation31').replace('Publish reviewed arbitrary two-graph contact classification','Record native compiler success for unchanged graph paper');p.write_text(s);add(p,'checkpoint-scripts/'+p.name)
p=snap/'CHECKPOINT.txt';p.write_text('Checkpoint31: Native editor compiler now returnedSUCCESS for exact unchanged final25-page graphpaper23 source. Addendum binds source/PDF/review/historicalbundle; earlier pending verification remains preserved as an accurate record at packaging time. No mathematical/source/PDF change. All42originals remain open, curve source repair and many-factor graph research running, goalactive.\n');add(p,'CHECKPOINT.txt')
m={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':'MingchenXia/nonarchimedean-pluripotential-theory','branch':'codex/xean-research-20261003','expected_previous_checkpoint':parent,'files':files,'scope':'NativeSUCCESS addendum for unchanged reviewed graphpaper23; historicalpendingrecordpreserved, all42originalopen.'};p=c/'upload-manifest-continuation31.json';assert not p.exists();p.write_text(json.dumps(m,indent=2)+'\n');print(json.dumps({'files':len(files),'manifest':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
