from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation189.json';F=G/'continuation189-publication-records';S=K/'small-batch180181-public-status-20261007-continuation189'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation188.json').read_text())
assert prior['commit_sha']=='39c534adc1d24561176384e7b727785b710e0c99'
assert all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
F.mkdir();S.mkdir();items=[]
for n in (179,180,181):
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[x for x in items if x['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),items=items,active_items=active,maximum_concurrent_campaigns=2,
    focus='Whole217 general E1 mixed operator independentlyPASS179, exact complete native/frozen/source bindings verified, accepted supporting paper69. Original full equation author180 continues its unchanged frozen input. Whole218 independent181 reviews every new locality/comparison proof using only entire accepted217 caller grant O with harmless normalization clarifications. Original atoms9/42 unchanged.')
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==69 and j['remaining_open_original_atoms']==33
    j.update(updated_utc=datetime.now(timezone.utc).isoformat(),current_small_batch=batch,
        github_pending_checkpoint=dict(manifest=str(M),continuation=189,status='prepared_for_authorized_push'))
    if name=='checklist-current.json':
        for t in j['targets']:
            if t['id']=='P16.4':
                assert not t['fully_solved'] and t['closure']=='open'
                t['current_focus']='Whole217 arbitrary-dimensional all-complete-field genuine E1 mixed operator independentlyPASS179 and accepted as supporting paper69. Whole218 strict Borel locality/open locality/mixed and pure comparison independently181 active; only complete accepted217 O and source-preserving normalization clarifications granted. Original-equation author180 continues with its unchanged full171/214/216 grants and frozen unreviewed217/218 data; no new feedback supplied. Compactness/EP/outer derivative/target characterization/attainment/every-solution uniqueness remain open.'
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=datetime.now(timezone.utc).isoformat(),originals_solved=9,originals_open=33,
    cumulative_independently_accepted_research_papers=69,new_original_closure=None,new_accepted_partial_review=179,
    active_batch=[x['round'] for x in active],new_unreviewed_target_observation=219,no_hot_feedback=True,protected_editor_unchanged_open=True),indent=2)+'\n')
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py')
    files.append(dict(local=str(p),path=remote or 'research-checkpoints/continuation189/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in (F,S,K/'public-P16.4-continuation217-general-E1-mixed-operator'):
    for p in sorted(folder.iterdir()):
        if p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf'):add(p)
for label in ('actual-canonical-independent-review','native-model-final-review','whole-partial-review-binding'):add(K/f'P16.4-round179-{label}-20261007.json')
add(K/'public-P16.4-continuation218-strict-locality-comparison/accepted-prerequisite-O-binding181-20261007.json')
add(K/'P16.4-continuation219-target-integrability-working-observation-20261007.json')
C=next((R/'campaigns/round-181').iterdir())
for name in ('task.json','argument.md','settings.json','freeze.json','original-task.json','mathematical-data-bindings.json','launch-record.json'):add(C/name)
for name in ('bind_completed_review179_20261007.py','accept_general_operator217_review179_20261007.py','prepare_locality218_review181_20261007.py','launch_frozen_partial_review181_20261007.py','record_verified188_20261007.py'):add(R/name)
add(G/'push-receipt-continuation188.json');add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=datetime.now(timezone.utc).isoformat(),repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],
    files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=69,
    commit_message='Accept all-field general E1 mixed operator and launch locality comparison review',
    scope='Whole2178-page general E1 mixed operator independentlyPASS179, complete report/all8premises/14passages ROOT read, exact native/frozen/source bindings verified; accepted supporting paper69 with source-preserving epsilon-normalization clarification. Publish immutable full181 review input/launch: sole accepted whole217 O grant, whole2186-page locality/comparison manuscript and source ledger. Author180 retains unchanged frozen task with no hot feedback. Publish219 target-integrability working observation explicitly unreviewed, lacking coercivity/compactness and not granted. Originals9/42 unchanged; two active campaigns. No private active outputs, runtime/account/editor changes or full third-party source PDFs uploaded.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[x['round'] for x in active],accepted_papers=69,originals_solved=9),indent=2))
