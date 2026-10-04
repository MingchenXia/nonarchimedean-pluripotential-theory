"""Freeze reviewed completed-algebraic transport paper and new source evidence."""
from pathlib import Path
import datetime,hashlib,json,shutil
root=Path('/workspace/research');checkpoint=root/'github-checkpoint'
parent='21b7cdb13d61ce6ddbbd0296e346b9cf7c2c155b'
active=json.loads((root/'active-work.json').read_text())
assert active['github_checkpoint']['commit_sha']==parent
assert active['selected_atoms']==['P06.2','P05.2'] and not active['full_solutions']
assert active['latest_checkpoint']==str(root/'deliverables/reviewed-papers-round-22.zip')
snapshot=checkpoint/'continuation28-uploaded-live-records';snapshot.mkdir(exist_ok=False)
prefix='manuscript/editorial/xean_research_20261003/';files=[]
def add(path,target,mutable=False):
    path=Path(path);assert path.is_file(),path
    if mutable:
        copy=snapshot/(str(len(files))+'-'+path.name);shutil.copyfile(path,copy);path=copy
    assert prefix+target not in {f['path'] for f in files}
    files.append({'local':str(path),'path':prefix+target,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
manifest=json.loads((root/'deliverables/round-22-bundle-manifest.json').read_text())
assert manifest['entry_count']==9 and not manifest['fully_solved_original_atoms']
for name,digest in manifest['entries'].items():
    p=root/'deliverables/round-22'/name
    assert hashlib.sha256(p.read_bytes()).hexdigest()==digest
    add(p,'round-22/'+name)
for name in ('reviewed-papers-round-22.zip','round-22-bundle-manifest.json','round-22-native-compile.json','round-22-source-preparation.json','round-22-visual-check.json','round-22-pre-layout-export.log'):
    add(root/'deliverables'/name,name)
review=root/'campaigns/round-21/P06.2-all-dimensional-completed-algebraic-review'
run=json.loads((review/'run.json').read_text())['campaign']
assert run['status']=='completed' and run['result']['verdict']=='PASS'
att=json.loads((review/'review-read-attestation.json').read_text())
assert att['publish_exact_scope'] and att['full_report_read'] and att['all_premises_read'] and att['all_passages_read']
for name in ('run.json','task.json','settings.json','argument.md','freeze.json','source-artifact-binding.json','root-draft-read-record.json','review-read-attestation.json','publication-edits.json'):
    add(review/name,'reviews/round-22/'+name)
for name in ('prepare_round22_completed_algebraic_source.py','publish_round22.py','prepare_curve_source_repair_evidence_v2.py'):
    add(root/name,'checkpoint-scripts/'+name)
auth=root/'shared-sources/curve-source-authentication-20261004'
for name in ('hal-api.json','hal-api-retrieval.json','hal-record-retrieval.json','numdam-record-retrieval.json','Thuillier-official-document-retrieval.json','root-source-authentication.json','repair-evidence-manifest.json','evidence-preparation-failure.json'):
    add(auth/name,'source-authentication/curve-20261004/'+name)
add(root/'shared-sources/P06.2-curve-two-sign-primary-source-repair-evidence.md','source-authentication/P06.2-curve-two-sign-primary-source-repair-evidence.md')
add(checkpoint/'push-receipt-continuation27.json','records/push-receipt-continuation27.json')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv','refresh_checklist.py'):
    add(root/name,name,mutable=True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name)
push=checkpoint/'push_checkpoint_continuation28.py';assert not push.exists()
s=(checkpoint/'push_checkpoint_continuation27.py').read_text().replace('continuation27','continuation28')
s=s.replace('Checkpoint arbitrary graph research and algebraic completion draft','Publish reviewed completed-algebraic transport and curve source evidence')
push.write_text(s);add(push,'checkpoint-scripts/'+push.name)
summary=snapshot/'CHECKPOINT.txt'
summary.write_text('Checkpoint28: New13-page exact partial theorem: every compact ordinary form descends through one finite algebraic stage, every bidegree; completed-algebraic ordinary zero-Hessian transport on actual boundaryless pure analytic spaces, every dimension, with nilpotents and all component lengths. Independent review PASS23premises/32passages fully read and bound. Native compile SUCCESS; two unchanged-source exports clean; first page visually inspected only. All33primary units retained in frozen argument, exact previously fully read source-body reuse disclosed; no full-new-appendix-fresh-read claim. New official curve-source authentication and selected complete primary proof evidence supports a FUTURE fresh repair, not a regularization theorem. Existing INCONCLUSIVE/incomplete records preserved. P05 arbitrary graph-product research continues. All42 originals remain open; only P05.2/P06.2 selected; goal active. No archival full scan/OCR or full thesis PDF redistributed.\n')
add(summary,'CHECKPOINT.txt')
m={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':'MingchenXia/nonarchimedean-pluripotential-theory','branch':'codex/xean-research-20261003','expected_previous_checkpoint':parent,'files':files,'scope':'Reviewed exact partial completed-algebraic transport paper; future curve source evidence. All42 originals open.'}
p=checkpoint/'upload-manifest-continuation28.json';assert not p.exists();p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files':len(files),'manifest':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
