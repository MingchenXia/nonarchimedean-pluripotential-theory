"""Preserve an incomplete curve result and freeze its narrow causal continuation."""
from pathlib import Path
import datetime, hashlib, json, shutil

r=Path('/workspace/research'); c=r/'github-checkpoint'
parent='857c356c62a6e557d951d7f2eafcbe9999ebf2aa'
a=json.loads((r/'active-work.json').read_text())
assert a['github_checkpoint']['commit_sha']==parent and not a['full_solutions']
snapshot=c/'continuation32-uploaded-live-records'; snapshot.mkdir(exist_ok=False)
prefix='manuscript/editorial/xean_research_20261003/'; files=[]
def add(path,target,mutable=False):
    p=Path(path); assert p.is_file(),p
    if mutable:
        cp=snapshot/(str(len(files))+'-'+p.name); shutil.copyfile(p,cp); p=cp
    assert prefix+target not in {x['path'] for x in files}
    files.append({'local':str(p),'path':prefix+target,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})

w=r/'campaigns/round-23/P06.2-curve-two-sign-source-repair/artifacts/codex-b6Tb1c'
claim=json.loads((w/'status.json').read_text())
assert claim['id']=='P06.2' and claim['status']=='incomplete' and claim['proof_file'] is None
for n in ('P06.2-argument.md','argument-core.md','status.json','notes.json','self-audit.md','research-evidence.md','source-evidence.md','build-evidence.md','prepare_evidence.py','assemble_and_validate.py','reproduce.sh','diagnostics/finite_checks.py','diagnostics/output.json','evidence/artifact-hashes.json','evidence/cache-comparisons.json','evidence/complete-read-inputs.json','evidence/input-inventory.json','evidence/environment.json','evidence/extraction-output.json','evidence/failed-extraction-attempt.txt','evidence/source-selections.json','evidence/validation-output.json','evidence/review-origin.json'):
    add(w/n,'unaccepted/round23-curve-source-repair/'+n)
root=r/'root-checks/curve-source-repair-incomplete'
for p in sorted(root.iterdir()):
    if p.is_file(): add(p,'root-checks/curve-source-repair-incomplete/'+p.name)
d=r/'campaigns/round-25/P06.2-specified-semistable-tree-regularization'
for n in ('input.json','settings.json','input-manifest.json'):
    add(d/n,'continuation-inputs/specified-semistable-tree-regularization/'+n)
for n in ('prepare_specified_tree_regularization.py','review_specified_tree_regularization_after_completion.py'):
    add(r/n,'checkpoint-scripts/'+n)
add(r/'P06.2-specified-semistable-tree-regularization-proposal.md','root-proposals/P06.2-specified-semistable-tree-regularization-proposal.md')
add(c/'push-receipt-continuation31.json','records/push-receipt-continuation31.json')
for n in ('active-work.json','checklist-current.json','checklist-current.tsv','refresh_checklist.py'):
    add(r/n,n,mutable=True)
add(Path(__file__),'checkpoint-scripts/'+Path(__file__).name)
p=c/'push_checkpoint_continuation32.py'; assert not p.exists()
s=(c/'push_checkpoint_continuation31.py').read_text().replace('continuation31','continuation32').replace('Record native compiler success for unchanged graph paper','Preserve incomplete curve repair and launch specified-tree construction')
p.write_text(s); add(p,'checkpoint-scripts/'+p.name)
p=snapshot/'CHECKPOINT.txt'
p.write_text('Checkpoint32: Full-curve two-sign source/scope repair completed INCOMPLETE with exact id P06.2 and null proof pointer. No independent theorem review was admitted and no analytic paper accepted. Full core/all3 canonical notes read; finite diagnostics independently rerun with no analytic inference. Diagnostic dossier and exact missing applications retained. Fresh specified actual semistable TREE regularization campaign launched, arbitrary residual genus and fixed compact Y; model/tree/factorization are input hypotheses. New residual Riemann--Roch/unit-lift/all-direction/whole-annulus proposal remains fallible. Many-factor graph classification continues. Only P05.2/P06.2 active, all42 original atoms open, goalactive. Previously accepted papers and native compilation records remain unchanged.\n')
add(p,'CHECKPOINT.txt')
m={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':'MingchenXia/nonarchimedean-pluripotential-theory','branch':'codex/xean-research-20261003','expected_previous_checkpoint':parent,'files':files,'scope':'Incomplete curve source repair preserved without acceptance; fresh specified-tree analytic construction and many-factor graph research running. All42 originals open.'}
p=c/'upload-manifest-continuation32.json'; assert not p.exists()
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files':len(files),'manifest':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
