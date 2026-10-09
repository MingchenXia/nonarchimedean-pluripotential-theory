from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation276-publication-records'; M=G/'upload-manifest-continuation276.json'
C=R/'campaigns/round-274/P12.3-whole386-Jensen-completion-and-original-residual'
A=R/'campaigns/round-273/P16.7-whole385387-full-bounded-dual-and-intrinsic-E1'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation275.json'); assert prior['commit_sha']=='1fcb952cc79d605ab2bde0ecb714354b9d9980dd'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name); assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==275
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
fr=load(C/'freeze.json'); assert fr['input_sha256']=='6d0d003dc2d964a9154146398ac8b10a9a7f8940ccbfd0539c104cb8d97126b3'
assert not (C/'work.sqlite').exists() and fr['whole_math_files']==259
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:
    assert sha(C/name)==fr[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    for e in load(C/name):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
la=load(A/'launch-record.json'); assert la['round']==273 and la['frozen_input_sha256']=='f730f0a2b17a5bb4eb18307e8ed48b8121c183c70775ce7016f546f73c5e6ad3'
st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(A/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert not st['error'] and st['status'] in ['running','completed']; active=[273] if st['calls']['unsettled'] else []
F.mkdir(); S=F/'frozen-status-only'; S.mkdir(); write(S/'round273-public-native-status.json',st)
def freeze(p):
    p=Path(p); rel=p.relative_to(R)
    assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    assert 'primary-data' not in str(rel) and 'immutable-book-context' not in str(rel)
    dst=F/'frozen-files'/rel; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,dst); assert sha(dst)==sha(p)
for p in [A/'launch-record.json',R/'launch_frozen_native273_whole385387_checked_20261009.py',R/'prepare_native274_whole386_Jensen_and_completion_20261009.py',R/'record_verified_checkpoint275_20261009.py',G/'push-receipt-continuation275.json',G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py',Path(__file__)]:freeze(p)
for p in sorted((C/'immutable-mathematical-DATA').rglob('*')):
    if p.is_file():freeze(p)
for p in sorted(C.glob('*.json')):freeze(p)
now=datetime.now(timezone.utc).isoformat()
write(F/'publication-qualification.json',dict(recorded_utc=now,solved=16,open=26,accepted_papers=97,status='Frozen native274 and launched native273; all draft385386387 UNREVIEWED; no countincrease/originalclosure',native273=dict(status=st['status'],pid=la['pid'],model='gpt-6.1-sol',reasoning='xhigh',only_grants=[],whole_math_files=183,target='Whole384385387383 independent proof; fullbounded Ctheta variation/concavity/exactradialdual thenfulloriginalE1'),native274=dict(status='FROZEN NOT LAUNCHED',model='gpt-6.1-sol',reasoning='xhigh',only_grants=['G331','B341','E350'],whole_math_files=259,whole_math_bytes=8654708,private_primary_files=730,whole_context_files=3,target='IndependentWHOLE386 repairedHH/Jensen chain; proveactual completion-invariance offullnormalizedsemivaluations/primary/modelcone/rawenvelopes, thenformalcharp/generaloriginalscope'),completion_route_is_UNPROVED_and_not_a_correctness_grant=True,maximum_concurrent_campaigns=2,no_active_native273_math_read_or_hot_feedback=True,all_full_primary_bodies_literal_units_pixels_and_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,compiler='385/386/387 native requests pending, no diagnostics or verified PDF. Protected editor OPEN UNCHANGED; no newtabs.'))
(F/'README.md').write_text('Checkpoint276: formal completion route and full bounded analytic dual\n\n16/42 original problems solved;26 OPEN;97 accepted scoped papers unchanged. Native273 is running with the complete P16.7 drafts and no incoming correctness grants. Native274 is frozen, not launched, with the complete P12.3 repaired proof and exactly the entire qualifiedG331/B341/E350. It will independently verify that proof and investigate actual completion-invariance of the full normalized valuative link, primary/model-nef cones and raw envelopes, then the remaining original scope. The proposed completion mechanism is UNPROVED, not an assumed theorem.\n\nAll full primary/source/pixel/book-context bodies remain LOCALONLY. No active mathematics feedback, supplied-program execution, new editor tab, acceptance or original closure. Maximum TWO native gpt-6.1-sol xhigh campaigns. NONFORCE upload independently verifies the native Git tree, all remote file bindings and the fresh branch reference before launch.\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,maximum_concurrent_campaigns=2,items=[dict(round=273,status=st['status'],unsettled_calls=st['calls']['unsettled'])],next_frozen_rounds=[274]),github_pending_checkpoint=dict(continuation=276,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify276 frozen274 and273launch, then launchnative274. Native273 fullboundedCtheta dual andintrinsicE1; native274 whole386/Jensen/completion/originalP12.3; at mostTWO. No active feedback/countincrease;16solved26OPEN97accepted unchanged; protected editor unchanged.'); write(p,x); shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv'); files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation276/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/name; files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+name,bytes=p.stat().st_size,sha256=sha(p)))
assert len({e['path'] for e in files})==len(files)
x=load(R/'active-work.json')
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint frozen formal completion research and native analytic dual launch',scope='Entirefrozen274/P12.3 whole386 and native273launch/P16.7. Completion and fullboundeddual routes UNPROVED.16solved26OPEN97accepted unchanged; no fullprimary/bookpublication or activefeedback/editorchange.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,next_frozen_round=274,solved=16,open=26,papers=97),indent=2))
