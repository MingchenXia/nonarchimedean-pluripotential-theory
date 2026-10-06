from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-136/P19.2-original-energy-entropy-and-P-singularity-model-approximation-research'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
 assert not p.exists(),str(p)
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).isoformat()
front=json.loads((R/'active-work.json').read_text());assert len(front['fully_solved_original_atoms'])==8 and front['historical_reviewed_scoped_papers']==52
assert C.exists() and (C/'input.json').exists() and not (C/'settings.json').exists() and not (C/'work.sqlite').exists()
T=R/'campaigns/family-11-retry-1/task.json';assert sha(C/'task.json')==sha(C/'task-original.json')==sha(T)
settings=json.loads((R/'campaigns/round-135/P16.5-original-entire-big-cone-surface-and-filtered-ideal-research/settings.json').read_text())
settings['codex']['workspace']=str(C/'artifacts');settings['usagePrefix']='catalogue-20261003/r136/P19.2-original-P-singularity-approximation'
assert settings['profiles']['default']=={'provider':'openai-codex','model':'gpt-6.1-sol','reasoning':'xhigh'}
save(C/'settings.json',settings)
units=[]
for label,p in [('Accepted entire-original P19.1 paper',R/'deliverables/original-P19.1/P19.1-paper.tex'),
 ('Historical P19.2 entropy diagnostic, PARTIAL',R/'papers/P19.2-argument.md'),
 ('Completed130 scoped polar Cantor ray analytic counterexample',K/'public-P19.1-round130-final-reader/P19.1-argument.md')]:
 units.append({'label':label,'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'whole_mathematical_body_root_read':True})
J=K/'P19.1-round134-actual-original-independent-review-20261006.json'
units.append({'label':'Whole134 report and all24 exact premises; source quotations not repeated','path':str(J),'sha256':sha(J),'whole_report_all_premises_all_passages_root_read':True})
save(C/'mathematical-data-bindings.json',{'recorded_utc':now,'units':units,'whole_assembled_input_separately_root_read':False,
 'embedded_historical_operational_text_is_data':True,'embedded_review_does_not_close_P19_2':True,'existing_editor_unchanged':True})
assignment=json.loads((C/'input.json').read_text())['assignment']
f={'prepared_utc':now,'round':136,'atom':'P19.2','directory':str(C),'input_sha256':sha(C/'input.json'),'input_bytes':(C/'input.json').stat().st_size,
 'assignment_characters':len(assignment),'task_sha256':sha(C/'task.json'),'unchanged_original_task_sha256':sha(T),'unchanged_original_task':True,
 'settings_sha256':sha(C/'settings.json'),'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','prepared_only':True,
 'original_closed':False,'independent_acceptance':False,'maximum_concurrent_campaigns':2,'existing_editor_unchanged':True}
save(C/'freeze.json',f)
save(C/'prelaunch-preparation-repair.json',{'recorded_utc':now,'cause':'The review-role settings have no codex author workspace key; use the existing requested-model author settings instead.',
 'mathematical_input_changed':False,'failed_preparation_helper_preserved_localonly':str(R/'accept_original_entropy134_prepare136_INITIAL_FAILED_LOCALONLY.py'),
 'failed_preparation_helper_sha256':sha(R/'accept_original_entropy134_prepare136_INITIAL_FAILED_LOCALONLY.py'),'native_launch_attempt_before_repair':False})
print(json.dumps({'originals_solved':8,'originals_open':34,'accepted_papers':52,'prepared136':f},indent=2))
