from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
M=G/'upload-manifest-continuation192.json'; F=G/'continuation192-publication-records'; S=K/'small-batch186187-public-status-20261007-continuation192'
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation191.json').read_text()); assert prior['commit_sha']=='b4d5f1bf0def87cc283a6a3546e025796be3f1e4'
assert all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
accept=json.loads((K/'public-P16.4-continuation222-projective-line-kernel-equation/whole-partial-paper-acceptance185-20261007.json').read_text()); assert accept['verdict']=='PASS' and accept['cumulative_accepted_paper_number']==72
now=datetime.now(timezone.utc).isoformat(); F.mkdir(); S.mkdir(); items=[]
for n in (184,185,186,187):
    c=next((R/f'campaigns/round-{n}').iterdir()); st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json'; p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P05.2' if n in (184,187) else 'P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[x for x in items if x['unsettled_calls']>0]; assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,
    focus='Whole222 split projective-line equation independently PASS185, accepted paper72 with exact native/frozen bindings. Full originalP16.4 author186 uses six complete accepted grants and unproved general-curve observation223. Full originalP05.2 author184 candidate=false produces whole224 strict-growth Bergman-fan obstruction/literal regularity failure, under independent187 review with no caller grants. Originals9/42 unchanged.')
for name in ('active-work.json','checklist-current.json'):
    p=R/name; j=json.loads(p.read_text()); assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==72 and j['remaining_open_original_atoms']==33
    j.update(updated_utc=now,current_small_batch=batch,github_pending_checkpoint=dict(manifest=str(M),continuation=192,status='prepared_for_authorized_push'))
    if name=='checklist-current.json':
        for t in j['targets']:
            if t['id']=='P05.2':
                assert not t['fully_solved'] and t['closure']=='open'
                t['current_focus']='Completed184 candidate=false: nine-page strict positive-growth U(3,4) fan contact obstruction with genuine finite PA endpoint and separate literal regularity failure. Entire224 under independent187 review with no mathematical grants; full general structural classification remains open.'
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'): shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=now,originals_solved=9,originals_open=33,cumulative_independently_accepted_research_papers=72,new_original_closure=None,new_accepted_partial_review=185,active_batch=[x['round'] for x in active],new_unreviewed_polyhedral_obstruction=224,unproved_general_curve_plan=223,no_hot_feedback=True,protected_editor_unchanged_open=True),indent=2)+'\n')
D=K/'public-P05.2-continuation224-strict-growth-obstruction'; addendum=D/'native-compiler-and-limited-visual-addendum-20261007.json'; assert not addendum.exists()
addendum.write_text(json.dumps(dict(recorded_utc=now,path=str(D/'P05.2-paper.tex'),source_sha256=sha(D/'P05.2-paper.tex'),native_result=dict(path=str(D/'P05.2-paper.tex'),kind='success',message="The current source compiled successfully with the desktop editor's compiler."),native_compiler_success=True,source_unchanged_since_applicable_compile_request=True,root_visual_pages_read=[1,9],all_pdf_pages_visually_root_read=False,pdf_pages=9,pdf_sha256=sha(D/'P05.2-paper.pdf'),mathematical_acceptance_implied=False,protected_editor_unchanged_open=True),indent=2)+'\n')
files=[]
def add(p,remote=None):
    p=Path(p); assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py')
    files.append(dict(local=str(p),path=remote or 'research-checkpoints/continuation192/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in (F,S,K/'public-P16.4-continuation222-projective-line-kernel-equation',D):
    for p in sorted(folder.iterdir()):
        if p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py'): add(p)
for p in sorted((D/'evidence').glob('*.json')): add(p)
for label in ('actual-canonical-independent-review','native-model-final-review','whole-partial-review-binding'): add(K/f'P16.4-round185-{label}-20261007.json')
for label in ('completed-actual-author-result','native-model-final-partial-author','settled-partial-author-binding'): add(K/f'P05.2-round184-{label}-20261007.json')
add(K/'P16.4-continuation223-general-curve-kernel-working-observation-20261007.json')
A=Path(json.loads((K/'P05.2-round184-completed-actual-author-result-20261007.json').read_text())['workspace']); add(A/'P05.2-paper.pdf'); add(A/'P05.2-paper.tex')
for n in (186,187):
    c=next((R/f'campaigns/round-{n}').iterdir())
    for name in ('task.json','input.json' if n==186 else 'argument.md','settings.json','freeze.json','original-task.json','mathematical-data-bindings.json','launch-record.json'): add(c/name)
for name in ('bind_completed_review185_20261007.py','accept_projective_line222_review185_20261007.py','prepare_original_field_equation186_after_projective_line_20261007.py','launch_frozen_original_field_equation186_20261007.py','bind_completed_partial_author184_20261007.py','reproduce_polyhedral_obstruction224_20261007.py','prepare_polyhedral_obstruction224_review187_20261007.py','launch_frozen_partial_review187_20261007.py','record_verified191_20261007.py'): add(R/name)
add(G/'push-receipt-continuation191.json'); add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'): add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=72,
    commit_message='Accept all-field projective-line equation and audit strict-growth polyhedral obstruction',
    scope='Entire222 seven-page split P^1_K actual equation independentlyPASS185, full14245-char report/1premise/4passages ROOT read and exact native/frozen/source bindings verified. Accepted supporting paper72, intrinsic target/existence/every-solution allpoint uniqueness/variational value over all complete char0 fields and actual ample rational bundles. Whole224 nine-page strict-growth U(3,4) contact obstruction and separate literal regularity failure remain unreviewed under frozen187 no-grant independent review; ROOT read all241 saved source lines, whole argument/source ledger/all3notes, reproduced finite checks/two warning-free local builds/exact native compiler SUCCESS/first+last PDF pages only. Completed184 actual/native/frozen proof binding published. Full originalP16.4 author186 proceeds with complete acceptedO217/D214/N220/T171/Q222/C218 and unproved graph working observation223. No new original closure:9/42 solved,33 open,max2 campaigns. No private active streams, full third-party sources, auth/runtime/protected editor changes.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[x['round'] for x in active],accepted_papers=72,originals_solved=9),indent=2))
