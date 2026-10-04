"""Freeze reviewed finite graph-product paper and pending conditional curve draft."""
from pathlib import Path
import datetime,hashlib,json,shutil
r=Path('/workspace/research');c=r/'github-checkpoint';parent='0ec9f757a4b461718b2d999b5f0ba26da9ffd0ca'
a=json.loads((r/'active-work.json').read_text());assert a['github_checkpoint']['commit_sha']==parent and not a['full_solutions']
snapshot=c/'continuation35-uploaded-live-records';snapshot.mkdir(exist_ok=False)
prefix='manuscript/editorial/xean_research_20261003/';files=[];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def add(path,target,mutable=False):
    p=Path(path);assert p.is_file(),p
    if mutable:
        q=snapshot/(str(len(files))+'-'+p.name);shutil.copyfile(p,q);p=q
    assert prefix+target not in {x['path'] for x in files}
    files.append({'local':str(p),'path':prefix+target,'sha256':sha(p)})
m=json.loads((r/'deliverables/round-24-bundle-manifest.json').read_text())
for name,digest in m['entries'].items():
    p=r/'deliverables/round-24'/name;assert sha(p)==digest;add(p,'deliverables/round-24/'+name)
assert sha(Path(m['bundle']))==m['sha256'];add(m['bundle'],'deliverables/reviewed-papers-round-24.zip')
for n in ('round-24-bundle-manifest.json','round-24-source-preparation.json','round-24-native-verification.json','round-24-visual-check.json'):
    add(r/'deliverables'/n,'deliverables/'+n)
for n in ('prepare_round24_many_graph_source.py','publish_round24_many_graph.py','record_round24_graph_read.py','record_round24_graph_read_v2.py','record_round24_graph_read_v3.py'):
    add(r/n,'checkpoint-scripts/'+n)
v=r/'campaigns/round-24/P05.2-finitely-many-graph-products-review'
for n in ('review-read-attestation.json','root-draft-read-record.json','publication-edits.json'):
    add(v/n,'accepted-reviews/round24-many-graph-products/'+n)
for dirname in ('many-graph-product-draft-phase2','many-graph-product-draft-phase3','many-graph-product-draft-phase3-v2','many-graph-product-draft-phase3-v3','specified-tree-regularization-phase1'):
    for p in sorted((r/'root-checks'/dirname).iterdir()):
        if p.is_file():add(p,'root-checks/'+dirname+'/'+p.name)
w=r/'campaigns/round-25/P06.2-specified-semistable-tree-regularization/artifacts/codex-luvloj'
assert json.loads((w/'status.json').read_text())['status']=='partial'
for n in ('P06.2-argument.md','P06.2-partial.tex','P06.2-partial.pdf','status.json','self-audit.md','source-evidence.md','research-evidence.md','build-evidence.md','reproduce.sh','assemble_evidence.py','validate_artifacts.py'):
    add(w/n,'unaccepted/round25-specified-tree/'+n)
for p in sorted((w/'evidence').iterdir()):
    if p.is_file():add(p,'unaccepted/round25-specified-tree/evidence/'+p.name)
v=r/'campaigns/round-25/P06.2-specified-semistable-tree-regularization-review'
for n in ('task.json','settings.json','argument.md','freeze.json','source-artifact-binding.json'):
    add(v/n,'pending-reviews/round25-specified-tree/'+n)
add(c/'push-receipt-continuation34.json','records/push-receipt-continuation34.json')
for n in ('active-work.json','checklist-current.json','checklist-current.tsv','refresh_checklist.py'):add(r/n,n,True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name)
p=c/'push_checkpoint_continuation35.py';assert not p.exists()
s=(c/'push_checkpoint_continuation34.py').read_text().replace('continuation34','continuation35').replace('Checkpoint many-factor graph draft and curve recognition integration','Publish reviewed finite graph-product classification and preserve curve draft')
p.write_text(s);add(p,'checkpoint-scripts/'+p.name)
p=snapshot/'CHECKPOINT.txt';p.write_text('Checkpoint35: Exact finite graph-product partial classification independently reviewedPASS0/0, full report and all main/supporting proofs/canonicalnotes read, immutable binding checked; published28page paper with native desktop compilerSUCCESS on unchangedsource,2cleanPDFexports and firstpagevisual. Criterion all localrelationconesrankone and atmostONEbranchedfactor; actualrawPAPC/regularization/fullcontact or complete negative integral for EACHfixedREALreference. Original arbitrary balanced-carrier problemopen. Full proof/support/sourcequotes/review/diagnostic packet retained. Metadata ledger failures preserved: trailing LF count and author-local/canonical-note distinction; no math or worker changes. Conditional actual specified semistableTREE ordinary smoothing9page author draft committed as UNACCEPTED; supplied model/tree/factorization inputs, independent reviewpending, all3canonicalnotes read but main/sources not yet fully rootread. All-K pure-curve recognition integration running separately. Only2selectedatomsP05.2/P06.2, all42originalsopen, goalactive.\n');add(p,'CHECKPOINT.txt')
m={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':'MingchenXia/nonarchimedean-pluripotential-theory','branch':'codex/xean-research-20261003','expected_previous_checkpoint':parent,'files':files,'scope':'Reviewed any-finite-number graph-product partial classification paper; pending conditional tree regularization draft; all-K curve recognition integration continues. All42originalsopen.'}
p=c/'upload-manifest-continuation35.json';assert not p.exists();p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'files':len(files),'manifest':str(p),'sha256':sha(p)}))
