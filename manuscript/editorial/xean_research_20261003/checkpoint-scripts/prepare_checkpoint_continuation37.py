"""Freeze accepted arbitrary-field intrinsic curve recognition paper."""
from pathlib import Path
import datetime,hashlib,json,shutil
r=Path('/workspace/research');c=r/'github-checkpoint';parent='c0345ae7ee8b30bbbd4bb429fc3fe141e8cf57f6'
a=json.loads((r/'active-work.json').read_text());assert a['github_checkpoint']['commit_sha']==parent and not a['full_solutions']
snapshot=c/'continuation37-uploaded-live-records';snapshot.mkdir(exist_ok=False)
prefix='manuscript/editorial/xean_research_20261003/';files=[];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def add(path,target,mutable=False):
    p=Path(path);assert p.is_file(),p
    if mutable:
        q=snapshot/(str(len(files))+'-'+p.name);shutil.copyfile(p,q);p=q
    assert prefix+target not in {x['path'] for x in files}
    files.append({'local':str(p),'path':prefix+target,'sha256':sha(p)})
m=json.loads((r/'deliverables/round-26-bundle-manifest.json').read_text())
for name,digest in m['entries'].items():
    p=r/'deliverables/round-26'/name;assert sha(p)==digest;add(p,'deliverables/round-26/'+name)
assert sha(Path(m['bundle']))==m['sha256'];add(m['bundle'],'deliverables/reviewed-papers-round-26.zip')
for n in ('round-26-bundle-manifest.json','round-26-source-preparation.json','round-26-native-verification.json','round-26-visual-check.json'):
    add(r/'deliverables'/n,'deliverables/'+n)
for n in ('record_round26_curve_review.py','prepare_round26_curve_source.py','export_round26_curve.py','publish_round26_curve.py'):
    add(r/n,'checkpoint-scripts/'+n)
v=r/'campaigns/round-26/P06.2-arbitrary-field-curve-recognition-integration-v2-review'
for n in ('review-read-attestation.json','root-draft-read-record.json','publication-edits.json'):
    add(v/n,'accepted-reviews/round26-arbitrary-field-curve/'+n)
for p in sorted((r/'root-checks/arbitrary-field-curve-integration-phase2').iterdir()):
    if p.is_file():add(p,'root-checks/arbitrary-field-curve-integration-phase2/'+p.name)
add(c/'push-receipt-continuation36.json','records/push-receipt-continuation36.json')
for n in ('active-work.json','checklist-current.json','checklist-current.tsv','refresh_checklist.py'):add(r/n,n,True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name)
p=c/'push_checkpoint_continuation37.py';assert not p.exists()
s=(c/'push_checkpoint_continuation36.py').read_text().replace('continuation36','continuation37').replace('Publish reviewed supplied-tree regularization and checkpoint curve recognition','Publish reviewed arbitrary-field pure-curve recognition')
p.write_text(s);add(p,'checkpoint-scripts/'+p.name)
p=snapshot/'CHECKPOINT.txt';p.write_text('Checkpoint37: Arbitrary-field intrinsicPUREcurve ordinaryzero-Hessian recognition independently reviewedPASS43/75. Full report/allpremises/allpassages read, exact0basedstatementlinks andimmutablebindings checked. Allnew1232LFmain/all3actualcanonicalnotes/all16newprimarybodies read;23source/supportcopies rebound; full previously reviewed gates reusedatidenticalexactscope and mathematicalbodies embedded. ANYcomplete nontrivK, actualgoodsepstrictboundarylessPUREcurve, singular/nil/imperfect/positivechar/unequalactualArtinianlengths; fullALLextensions/ALLcurvemaps classicalPH andG-localREALPL/GJRharmonic, allordinaryopens. No arbitrarytranc currentascent orordinarysmoothapprox theorem. Published10page paper nativecompilerSUCCESS unchangedfinalsource,2cleanPDFexports andfirstpagevisual. ExactGJRversion/closedsubspace terminology clarificationsonly; originalquotationsunchanged. Originalarbitrary-dimensionalP06.2open; all42originalsopen, goalactive. Nextsmallbatchselectedafterthischeckpoint.\n');add(p,'CHECKPOINT.txt')
m={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':'MingchenXia/nonarchimedean-pluripotential-theory',
 'branch':'codex/xean-research-20261003','expected_previous_checkpoint':parent,'files':files,
 'scope':'Accepted arbitrary-field pure-curve recognition paper and exact full proof/review evidence. Original all-dimensional problem and all42originalsopen.'}
p=c/'upload-manifest-continuation37.json';assert not p.exists();p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files':len(files),'manifest':str(p),'sha256':sha(p)}))
