"""Freeze next small-batch inputs without certifying the proposed mathematics."""
from pathlib import Path
import datetime,hashlib,json,shutil
r=Path('/workspace/research');c=r/'github-checkpoint';parent='39ada688fec003a2e9485124ea3ea036d631ff93'
a=json.loads((r/'active-work.json').read_text());assert a['github_checkpoint']['commit_sha']==parent and a['selected_atoms']==['P15.1','P15.2'] and not a['full_solutions']
snapshot=c/'continuation38-uploaded-live-records';snapshot.mkdir(exist_ok=False)
prefix='manuscript/editorial/xean_research_20261003/';files=[];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def add(path,target,mutable=False):
    p=Path(path);assert p.is_file(),p
    if mutable:
        q=snapshot/(str(len(files))+'-'+p.name);shutil.copyfile(p,q);p=q
    assert prefix+target not in {x['path'] for x in files}
    files.append({'local':str(p),'path':prefix+target,'sha256':sha(p)})
for n in ('prepare_zero_volume_fibration_batch.py','review_zero_volume_fibration_after_completion.py'):
    add(r/n,'checkpoint-scripts/'+n)
for n in ('P15-zero-volume-fibration-proposal.md','zero-volume-fibration-batch-manifest.json'):
    add(r/n,'proposed-inputs/zero-volume-fibration/'+n)
for n in ('BEGZ-0812.3674v2-20261004-provenance.json','zero-volume-fibration-primary-read-20261004.json'):
    add(r/'shared-sources'/n,'source-authentication/zero-volume-fibration/'+n)
batch=json.loads((r/'zero-volume-fibration-batch-manifest.json').read_text())
for item in batch['campaigns']:
    p=Path(item['directory']);target='proposed-inputs/zero-volume-fibration/'+item['atom']+'/'
    for n in ('input.json','settings.json','input-manifest.json'):
        if n in item['inputs']:assert sha(p/n)==item['inputs'][n]
        add(p/n,target+n)
add(c/'push-receipt-continuation37.json','records/push-receipt-continuation37.json')
for n in ('active-work.json','checklist-current.json','checklist-current.tsv','refresh_checklist.py'):add(r/n,n,True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name)
p=c/'push_checkpoint_continuation38.py';assert not p.exists()
s=(c/'push_checkpoint_continuation37.py').read_text().replace('continuation37','continuation38').replace('Publish reviewed arbitrary-field pure-curve recognition','Checkpoint two zero-volume fibration research inputs')
p.write_text(s);add(p,'checkpoint-scripts/'+p.name)
p=snapshot/'CHECKPOINT.txt';p.write_text('Checkpoint38: Next small batch ONLYP15.1/P15.2 launched usingXean nativeCodex gpt-6.1-sol xhigh, one admittedresearchcall each. Independentreviewpreparers waiting forcommittedfrozenproofs; no newtheoremadmitted oraccepted. Originalgeneralpseudoeffective zero-volume energy/operator problemsunchanged. UNVERIFIEDproposed relativebase construction: suppliedsurjectiveholomorphicfibration ofsmoothcompactKahlermanifolds, boundedbase potentials, arbitrarynon-descending boundedperturbativepotentials approachingpullbackuniformlywithout epsilon-rate, critical/singularfibres retained, auxiliaryKahlerclass independenceonlyafterexplicittransversecoefficient. Carrier/base dimension/rawmass/reference/minimalboundedtype explicit. Old smoothfixedclassenergy/P1xP1counterexample arecomparisononly. Fresh primaryBEGZ0812.3674v2 retrieved/hashbound; sixexactselectedbodies fullyrootread, sourcequotes retainedwith visibletranscription/omittedproofs; noarchivalPDF orwholemonographuploaded. Priorreviewedfinitegraph28page, suppliedtree10page andall-Kcurve10page papersremainimmutableandpushed. All42originalsopen; goalactive; regularGitHubcheckpointscontinue.\n');add(p,'CHECKPOINT.txt')
m={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':'MingchenXia/nonarchimedean-pluripotential-theory',
 'branch':'codex/xean-research-20261003','expected_previous_checkpoint':parent,'files':files,
 'scope':'Immutable next-batch P15.1/P15.2 unverified fibration proposals, native research inputs, primary evidence and current active goal. No new theorem acceptance.'}
p=c/'upload-manifest-continuation38.json';assert not p.exists();p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files':len(files),'manifest':str(p),'sha256':sha(p)}))
