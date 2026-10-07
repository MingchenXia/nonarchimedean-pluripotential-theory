from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
M=G/'upload-manifest-continuation199.json'; F=G/'continuation199-publication-records'
S=K/'small-batch189193-public-status-20261007-continuation199'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation198.json').read_text())
assert prior['commit_sha']=='828595b1d038e32523cf6bf7257bd05577aa4637' and prior['files']==64 and not prior['force_update']
assert all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
C193=next((R/'campaigns/round-193').iterdir());assert (C193/'launch-record.json').exists()
cf=json.loads((C193/'freeze.json').read_text())
for n,k in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:assert sha(C193/n)==cf[k]
now=datetime.now(timezone.utc).isoformat(); F.mkdir(); S.mkdir(); items=[]
for n in (189,192,193):
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P05.2' if n==192 else 'P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
assert next(i for i in items if i['round']==192)['observed_status']=='completed'
active=[i for i in items if i['unsettled_calls']>0]; assert len(active)<=2
D=K/'public-P05.2-continuation230-continuous-completion-and-envelope'
acceptance=json.loads((D/'whole-partial-paper-acceptance192-20261007.json').read_text())
assert acceptance['cumulative_accepted_paper_number']==75 and acceptance['verdict']=='PASS' and not acceptance['original_closed']
route=K/'P16.4-continuation238-flat-polarized-formal-algebraization-working-route-20261007.json'
assert sha(route)=='657286e5aa68564ad29d5b6ae054a845a1696338ff519bb9edbc0a1ce39135f2'
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,prepared_next_round=None,focus='Whole independent189 genus-zero equation audit and unchanged full originalP16.4 native193 author. Review192 PASS for entire230 continuous completion and all-continuous-obstacle envelope manuscript; full P05 PA regularization/contact classification remains open. Newly reconstructed model-algebraization route238 is unreviewed data and was not hot-sent to immutable193.')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==75 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(manifest=str(M),continuation=199,status='prepared_for_authorized_push'))
    j['prepared_next_original_campaign'].update(prepared_only=False,launched=True,launch_record=str(C193/'launch-record.json'),launch_record_sha256=sha(C193/'launch-record.json'))
    j['P16_4_formal_algebraization_route238']=dict(record=str(route),record_sha256=sha(route),new_accepted_paper=False,original_closed=False,source_units_whole_printed_read=24,working_application_steps=10,actual_model_premises_still_required=True,all_recursive_generated_dependencies_read=False,sent_to_active193=False)
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for n in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/n,F/n)
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=now,originals_solved=9,originals_open=33,cumulative_accepted_papers=75,new_accepted_whole_scoped_paper=230,independent_review_round=192,verdict='PASS',review_premises=7,review_passages=33,complete_report_root_read=True,exact_native_final_and_whole_frozen_inputs_bound=True,new_original_closure=None,active_batch=[i['round'] for i in active],launched_original_author193=True,unreviewed_working_route238=True,protected_editor_unchanged_open=True),indent=2)+'\n')
files=[];seen=set()
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and 'frozen-primary-data-LOCALONLY' not in p.parts
    remote=remote or 'research-checkpoints/continuation199/'+str(p.relative_to(R));assert remote not in seen;seen.add(remote)
    files.append(dict(local=str(p),path=remote,bytes=p.stat().st_size,sha256=sha(p)))
for d in (F,S):
    for p in sorted(d.iterdir()):add(p)
for n in ('P05.2-paper.tex','P05.2-paper.pdf','whole-partial-paper-acceptance192-20261007.json','harmless-reader-clarifications192-20261007.json','root-reproduction-binding-20261007.json','native-compiler-success-final-source-addendum-20261007.json','root-limited-pdf-visual-addendum-20261007.json'):add(D/n)
for n in ('P05.2-round192-actual-canonical-independent-review-20261007.json','P05.2-round192-native-model-final-review-20261007.json','P05.2-round192-whole-partial-review-binding-20261007.json'):add(K/n)
add(route);add(C193/'launch-record.json')
for n in ('bind_and_accept_continuous_completion230_review192_20261007.py','write_formal_algebraization238_stacks_working_route_20261007.py','launch_frozen_original_field_equation193_20261007.py','record_verified198_20261007.py'):add(R/n)
add(G/'push-receipt-continuation198.json');add(Path(__file__))
for n in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/n,'manuscript/editorial/xean_research_20261003/'+n)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=75,commit_message='Accept continuous envelope theorem and continue actual curve model proof',scope='Independent native192 PASS for entire unchanged thirteen-page230 manuscript: rational-endpoint PCC continuous dominating completion without continuity or boundedness assumptions, all real-endpoint completion inequalities, every continuous-obstacle actual envelope continuity and nonexpansiveness, sharp fan diagnostics, separate compact chart PA/raw-zero cases and exact entire-class density gap. Whole report7premises33passages read and bound exactly to native final, full frozen203478-byte argument, nine data bodies and only completeA224/B225 grants. Accepted supporting paper75; general PA regularization, operator/contact classification and original P05 remain open. Launch193 originalP16.4 only after192 settled, at most2campaigns with189; unchanged frozen original373771-byte input/private16source packet. New unreviewed238 Stacks formal-effectiveness route, complete printed24units read, explicit local inverse-projective construction and Noetherian Serre descent, preserves compatible original bundle; actual formal curve/Cartier/slope-degree/frame/orbit premises and higher-dimensional original equation remain unproved. No238 hotfeedback, no active private outputs, no full third-party source uploads, no auth/runtime/editor change.9/42 originals solved33open75accepted.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[i['round'] for i in active],accepted_papers=75),indent=2))
