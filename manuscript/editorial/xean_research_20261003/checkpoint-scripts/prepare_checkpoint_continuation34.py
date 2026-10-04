"""Freeze a pending graph proof and the new recognition-only curve integration."""
from pathlib import Path
import datetime,hashlib,json,shutil
r=Path('/workspace/research');c=r/'github-checkpoint'
parent='a797862a48a9c5c637b37ba388cda2f76affeaf4'
a=json.loads((r/'active-work.json').read_text());assert a['github_checkpoint']['commit_sha']==parent and not a['full_solutions']
snapshot=c/'continuation34-uploaded-live-records';snapshot.mkdir(exist_ok=False)
prefix='manuscript/editorial/xean_research_20261003/';files=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def add(path,target,mutable=False):
 p=Path(path);assert p.is_file(),p
 if mutable:
  q=snapshot/(str(len(files))+'-'+p.name);shutil.copyfile(p,q);p=q
 assert prefix+target not in {x['path'] for x in files}
 files.append({'local':str(p),'path':prefix+target,'sha256':sha(p)})

d=r/'campaigns/round-26/P06.2-arbitrary-field-curve-recognition-integration-v2'
for n in ('input.json','settings.json','input-manifest.json','integration-evidence-manifest.json','root-primary-read-and-bindings.json'):
 add(d/n,'continuation-inputs/arbitrary-field-curve-recognition-integration-v2/'+n)
for n in ('prepare_arbitrary_field_curve_recognition_integration.py','prepare_arbitrary_field_curve_recognition_integration_v2.py','review_arbitrary_field_curve_recognition_integration_after_completion.py'):
 add(r/n,'checkpoint-scripts/'+n)
add(r/'campaigns/round-26/P06.2-arbitrary-field-curve-recognition-integration/preparation-failure.json','continuation-inputs/arbitrary-field-curve-recognition-integration/preparation-failure.json')
add(r/'P06.2-arbitrary-field-curve-recognition-integration-evidence.md','root-proposals/P06.2-arbitrary-field-curve-recognition-integration-evidence.md')

w=r/'campaigns/round-24/P05.2-finitely-many-graph-products/artifacts/codex-BufmAZ'
claim=json.loads((w/'status.json').read_text());assert claim['status']=='partial' and claim['id']=='P05.2'
for n in ('P05.2-argument.md','P05.2-partial.tex','P05.2-partial.pdf','product-main.md','status.json','author-self-audit.md','research-notes.md','source-authentication.json','source-hashes.json','source-excerpts.json','snapshot_sources.py','compose_argument.py','diagnostics.py','diagnostic-input.json','diagnostic-output.json','diagnostic-stdout.txt','build.py','build-header.tex','make_notes.py','final_checks.py','artifact-hashes.json','checks.json','environment.json','commands.txt','build-evidence.json','initial-failed-build-evidence.json','second-failed-build-evidence.json','initial-failed-build-compile-1.log','second-failed-build-compile-1.log','layout-warning-compile.log','build-compile-1.log','build-compile-2.log'):
 add(w/n,'unaccepted/round24-many-graph-products/'+n)
v=r/'campaigns/round-24/P05.2-finitely-many-graph-products-review'
binding=json.loads((v/'source-artifact-binding.json').read_text())
assert binding['main_argument_sha256']==sha(w/'P05.2-argument.md')
assert binding['source_tex_sha256']==sha(w/'P05.2-partial.tex')
assert binding['source_status_sha256']==sha(w/'status.json')
for n in ('task.json','settings.json','argument.md','freeze.json','source-artifact-binding.json'):
 add(v/n,'pending-reviews/round24-many-graph-products/'+n)
root=r/'root-checks/many-graph-product-draft-phase1'
for n in ('canonical-result-record.json','read-in-progress.json'):
 add(root/n,'root-checks/many-graph-product-draft-phase1/'+n)
add(c/'push-receipt-continuation33.json','records/push-receipt-continuation33.json')
for n in ('active-work.json','checklist-current.json','checklist-current.tsv','refresh_checklist.py'):
 add(r/n,n,True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name)
p=c/'push_checkpoint_continuation34.py';assert not p.exists()
s=(c/'push_checkpoint_continuation33.py').read_text().replace('continuation33','continuation34').replace('Record exact saturated-quotient diagnostic and research checkpoint','Checkpoint many-factor graph draft and curve recognition integration')
p.write_text(s);add(p,'checkpoint-scripts/'+p.name)
p=snapshot/'CHECKPOINT.txt';p.write_text('Checkpoint34: Many-factor graph classification draft committed,45-page authorPDF and complete2478LF-line argument; independently reviewed exact finite-product scope is PENDING, no acceptance. All3canonical native notes/full audits read and mainLF1-268 read; remaining proof/diagnostics/rootread and full review/bindings required. Fresh all-K PURE-curve recognition-only integration running through native6.1xhigh with queued independent review, full exact previously reviewed transport/ALGClrecognition gates imported, authentic complete selected GR scalar-descent proof units supplied. First-stage ordinary-smooth psh approximation is a stronger separate curve campaign. Initial preparation wrapper/main hash mismatch preserved before native admission; freshv2 uses exact underlying main and receipt binding. Only2selectedatomsP05.2/P06.2, all42originalsopen, goalactive. No new accepted theorem or paper in this checkpoint.\n');add(p,'CHECKPOINT.txt')
m={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':'MingchenXia/nonarchimedean-pluripotential-theory','branch':'codex/xean-research-20261003','expected_previous_checkpoint':parent,'files':files,'scope':'Unaccepted many-factor graph proof/diagnostics and frozen pending review, new recognition-only all-K curve integration. Original42atomsopen.'}
p=c/'upload-manifest-continuation34.json';assert not p.exists();p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'files':len(files),'manifest':str(p),'sha256':sha(p)}))
