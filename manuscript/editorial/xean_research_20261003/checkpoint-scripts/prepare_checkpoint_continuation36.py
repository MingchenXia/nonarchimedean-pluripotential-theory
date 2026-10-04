"""Freeze accepted supplied-tree paper and unaccepted curve-integration draft."""
from pathlib import Path
import datetime,hashlib,json,shutil
r=Path('/workspace/research');c=r/'github-checkpoint'
parent='f33e3e550a9ac5185a6c6fcd19297903d80dca86'
a=json.loads((r/'active-work.json').read_text());assert a['github_checkpoint']['commit_sha']==parent and not a['full_solutions']
snapshot=c/'continuation36-uploaded-live-records';snapshot.mkdir(exist_ok=False)
prefix='manuscript/editorial/xean_research_20261003/';files=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def add(path,target,mutable=False):
    p=Path(path);assert p.is_file(),p
    if mutable:
        q=snapshot/(str(len(files))+'-'+p.name);shutil.copyfile(p,q);p=q
    assert prefix+target not in {x['path'] for x in files}
    files.append({'local':str(p),'path':prefix+target,'sha256':sha(p)})
m=json.loads((r/'deliverables/round-25-bundle-manifest.json').read_text())
for name,digest in m['entries'].items():
    p=r/'deliverables/round-25'/name;assert sha(p)==digest;add(p,'deliverables/round-25/'+name)
assert sha(Path(m['bundle']))==m['sha256'];add(m['bundle'],'deliverables/reviewed-papers-round-25.zip')
for n in ('round-25-bundle-manifest.json','round-25-source-preparation.json','round-25-source-preparation-v3.json',
 'round-25-source-preparation-failure.json','round-25-native-verification.json','round-25-native-verification-v3.json','round-25-visual-check.json'):
    add(r/'deliverables'/n,'deliverables/'+n)
for p in sorted((r/'deliverables/round-25/preparation-v2-evidence').iterdir()):
    add(p,'deliverables/round-25/preparation-v2-evidence/'+p.name)
for n in ('record_round25_tree_and_round26_curve_read.py','prepare_round25_tree_source.py','prepare_round25_tree_source_v2.py',
 'repair_round25_tree_typesetting.py','export_round25_tree.py','export_round25_tree_v3.py','publish_round25_tree.py'):
    add(r/n,'checkpoint-scripts/'+n)
v=r/'campaigns/round-25/P06.2-specified-semistable-tree-regularization-review'
for n in ('review-read-attestation.json','root-draft-read-record.json','publication-edits.json','publication-edits-v3.json'):
    add(v/n,'accepted-reviews/round25-specified-tree/'+n)
for dirname in ('specified-tree-regularization-phase2','specified-tree-regularization-phase3','arbitrary-field-curve-integration-phase1'):
    for p in sorted((r/'root-checks'/dirname).iterdir()):
        if p.is_file():add(p,'root-checks/'+dirname+'/'+p.name)
w=r/'campaigns/round-26/P06.2-arbitrary-field-curve-recognition-integration-v2/artifacts/codex-V8ZFSU'
assert json.loads((w/'status.json').read_text())['status']=='partial'
for n in ('P06.2-argument.md','P06.2-partial.tex','P06.2-partial.pdf','status.json','author-audit.md','research-notes.md',
 'reproduce.sh','prepare.py','build-and-check.py','finalize-manifest.py'):
    add(w/n,'unaccepted/round26-arbitrary-field-curve/'+n)
for p in sorted((w/'evidence').iterdir()):
    if p.is_file():add(p,'unaccepted/round26-arbitrary-field-curve/evidence/'+p.name)
for n in ('manifest.json','primary-units.json','primary-bodies.md'):
    add(w/'sources'/n,'unaccepted/round26-arbitrary-field-curve/sources/'+n)
for p in sorted((w/'sources').glob('primary-*.txt')):
    add(p,'unaccepted/round26-arbitrary-field-curve/sources/'+p.name)
v=r/'campaigns/round-26/P06.2-arbitrary-field-curve-recognition-integration-v2-review'
for n in ('task.json','settings.json','argument.md','freeze.json','source-artifact-binding.json'):
    add(v/n,'pending-reviews/round26-arbitrary-field-curve/'+n)
add(c/'push-receipt-continuation35.json','records/push-receipt-continuation35.json')
for n in ('active-work.json','checklist-current.json','checklist-current.tsv','refresh_checklist.py'):add(r/n,n,True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name)
p=c/'push_checkpoint_continuation36.py';assert not p.exists()
s=(c/'push_checkpoint_continuation35.py').read_text().replace('continuation35','continuation36').replace('Publish reviewed finite graph-product classification and preserve curve draft','Publish reviewed supplied-tree regularization and checkpoint curve recognition')
p.write_text(s);add(p,'checkpoint-scripts/'+p.name)
p=snapshot/'CHECKPOINT.txt'
p.write_text('Checkpoint36: Conditional supplied semistableTREE ordinary two-sign regularization independently reviewedPASS16/26. Full report/premises/passages read, exact zero-based links and immutable main/TEX/status/freeze checked; fullnewproof/all3actualcanonicalnotes/all17primarybodies read and fresh copiedreproduction byteidentical. Published10page paper: native compilerSUCCESS on finalsource,2cleanPDFexports,firstpagevisual. Same entireactualIntZ ordinarysmoothpsh and continuous uniformlydecreasingallZ; model/tree/harmonicfactorizationSUPPLIEDINPUTS. Exactcitation/scalarclarifications and layoutonly edits logged; preparation count failure/firstoverflowrender preserved. All-K PUREcurve recognition integration completed10page draft under independentreview, UNACCEPTED; full1232LFmain/all3canonicalnotes/all16newprimarybodies read,23copies andfullreviewedpriorgates rebound. No arbitrarytranc currentascent orordinarysmoothing theorem fromintegration. Only2selectedatomsP05.2/P06.2; all42originalproblemsopen, goalactive.\n')
add(p,'CHECKPOINT.txt')
m={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':'MingchenXia/nonarchimedean-pluripotential-theory',
 'branch':'codex/xean-research-20261003','expected_previous_checkpoint':parent,'files':files,
 'scope':'Accepted conditional supplied-tree regularization paper; unaccepted all-K pure-curve recognition integration and full source/read bindings. All42originalsopen.'}
p=c/'upload-manifest-continuation36.json';assert not p.exists();p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files':len(files),'manifest':str(p),'sha256':sha(p)}))
