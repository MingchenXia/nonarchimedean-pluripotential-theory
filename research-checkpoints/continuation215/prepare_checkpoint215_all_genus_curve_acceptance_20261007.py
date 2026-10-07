from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation215.json';F=G/'continuation215-publication-records'
S=K/'small-batch210211-public-status-20261007-continuation215'
D=K/'public-P16.4-continuation269-all-genus-original-field-curve-equation'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,d:Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation214.json').read_text())
assert prior['commit_sha']=='835717b537956ae065c671fb700e39ce51eba43a' and not prior['force_update']
assert all(prior[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
accept=json.loads((D/'whole-partial-paper-acceptance209-local-source-audit-20261007.json').read_text())
assert accept['verdict']=='PASS' and accept['cumulative_accepted_paper_number']==79 and not accept['original_closed']
assert sha(accept['source'])==accept['source_sha256'] and sha(accept['review_binding'])==accept['review_binding_sha256']
working=next(K.glob('P05.2-continuation278-*.json'));w=json.loads(working.read_text());assert not w['new_mathematical_grant'] and not w['original_closed']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in [209,210,211]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';write(p,st)
    items.append(dict(round=n,atom='P05.2' if n==210 else 'P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2
assert items[0]['unsettled_calls']==items[1]['unsettled_calls']==0
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,accepted_paper_number=79,original_closed=False,focus='S269 all-genus original-field curve theorem accepted after complete local-source worker209 plus ROOT whole audit/bindings/finite and original-pixel reproduction. Original211 general nontrivial n>=2 equation active. Worker210 whole evidence INCONCLUSIVE/mathematics reconstructed; ROOT audit still in progress, no S272 acceptance at this snapshot.')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==79 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,current_small_batch=batch,P05_2_PCC_tree_working278=dict(path=str(working),sha256=sha(working),new_mathematical_grant=False,original_closed=False),P05_2_local_audit210_scope=dict(settled=True,whole_evidence_verdict='INCONCLUSIVE',mathematical_reconstruction='No concrete material defect in all13units; historical input/checker/build/artifact availability limits',ROOT_binding_in_progress=True,new_accepted_paper=False,original_closed=False),P16_4_original_higher_dim211=dict(directory=items[2]['directory'],only_grants=['O217','D214','N220','T171','Q222','C218','G227','M257','S269'],whole_math_files=26,complete_math_bytes=474079,compact_native_input_bytes=15984,original_closed=False,new_accepted_paper=False),next_work='Finish ROOT whole210 mathematical/evidence audit preserving actual INCONCLUSIVE; continue original211 general higher-dimensional equation. At most two61xhigh campaigns. S269 curves do not close originalP16.4. Continue all33originals and regular verified pushes.',github_pending_checkpoint=dict(continuation=215,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    write(p,j);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint215: all-genus original-field curve theorem accepted; general higher-dimensional equation continues\n\n9/42 originals solved;33 open;79 accepted scoped/supporting papers. S269 is the complete all-genus curve theorem over ALL original fields: genuine original-bundle FS recognition and raw signed/zero curvature, arbitrary-support intrinsic finite-energy inverse, dual attainment afterward, and EVERYsolution EVERYpoint uniqueness/descent. Its source and scopes are unchanged. Independent209 is an ordinary native Codex WORKER local-source audit, not the canonical Xean research review role or automatic acceptance. ROOT read the whole report,26ordinary premises,52proof units,26equations,25applications and three exact FINAL notes; verified all33whole math bodies,8grants/all clarifications,62originals,40own artifacts,44passage bindings and35long original units. ROOT independently reran150rational graph targets/36tree pairs and rerendered18original scanned pages with exact byte matches. Finite checks/bindings do not certify analytic mathematics; ordinary recursive source foundations are explicitly disclosed and not all freshly reconstructed. Prior207whole INCONCLUSIVE remains unchanged. General n>=2 nontrivial P16.4 remains OPEN.\n\nNew native211 gpt-6.1-sol xhigh continues the full remaining original P16.4, with NINEwhole O/D/N/T/Q/C/G/M/S269 grants and ALL clarifications. A compact15,984-byte assignment references26immutable complete math files containing474,079bytes, rather than embedding a huge argument preview. The supported native worker reads the whole files and unchanged62primary packet, writes only own fresh artifacts, and keeps source/editor/runtime/auth unchanged. Maximum two campaigns.\n\nWorker210 is settled: its full local-source reconstruction reports no concrete material defect in all13P05.2 mathematical units, but its overall whole-evidence verdict is INCONCLUSIVE because the explicitly supplied packet lacks earlier checker/input/grid/build/log/artifact files. ROOT is still binding the whole report and those evidence claims; no new P05.2 acceptance at this snapshot. No INCONCLUSIVE is relabeled PASS. New ROOT278 proves a legal-PCC-tree formula for the actual unrestricted envelope, proper-height control of near-optimal tree leaf probabilities, bounded local-uniform obstacle continuity, and conditional localized continuity/contact bridges on the EXISTING genuine completion. It gives no all-obstacle domain membership or all-refinement structural classification. ROOT276/277/278 remain unreviewed future data.\n\nCompiler tracking addenda disclose environment-transition loss of old265/269wait handles53/113, which is NOT a compiler failure/success. Actual272request27 remains pending without returned diagnostics. Existing local builds/sources are preserved; current editor stays open unchanged. Long original source bytes/pixels/quotations, active private streams, databases and authentication are excluded. Publication uses no-force updates with independent tree/blob/ref verification.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation215/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
    for p in sorted(folder.iterdir()):add(p)
for p in [Path(accept['review_binding']),D/'whole-partial-paper-acceptance209-local-source-audit-20261007.json',D/'harmless-reader-clarifications209-local-source-audit-20261007.json',K/'P16.4-round209-exact-native-model-final-independent-local-audit-20261007.json',K/'P16.4-round209-actual-registered-native-worker-independent-local-audit-20261007.json',working]:add(p)
for p in sorted((D/'evidence/independent-local-audit209').iterdir()):add(p)
for dirname in ['public-P16.4-continuation265-actual-formal-FS-curve-equation','public-P16.4-continuation269-all-genus-original-field-curve-equation','public-P05.2-continuation272-arbitrary-real-reference-completion-and-flat-jet-contact']:
    folder=K/dirname
    if not folder.exists() and '265' in dirname:folder=next(K.glob('public-P16.4-continuation265-*'))
    add(folder/'builtin-request-tracking-addendum-after-environment-transition-20261007.json')
c=next((R/'campaigns/round-211').iterdir())
for name in ['task.json','original-task.json','freeze.json','input.json','settings.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json','launch-record.json']:add(c/name)
for name in ['bind_and_accept_curve269_local_audit209_20261007.py','prepare_higher_dimensional_equation211_20261007.py','launch_higher_dimensional_equation211_20261007.py','write_PCC_tree_envelope278_20261007.py','record_builtin_request_tracking_after_transition_20261007.py','record_verified214_20261007.py']:add(R/name)
add(G/'push-receipt-continuation214.json');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=79,commit_message='Accept all-genus curve equation after whole local-source audit and continue higher dimensions',scope='Whole S269 curves accepted after independently ROOT-read native209 worker local-source audit, exact bindings and finite/pixel reproduction;ordinary worker NOT canonicalreview/automaticaccept. Nineoriginals33open79supporting. Original211generalhigherdimwith9wholegrants26immutablefilesandcompactassignment.210settledwholeevidenceINCONCLUSIVE/mathematics reconstructed;ROOTbindingpending,noS272acceptance at snapshot.ROOT278newunreviewedPCCtree/localuniform envelope proof conditionalcontact,noallobstacleclassification. Compiler old53/113trackinglossnotfailure/success,27pending;source/editor unchanged. Originalprimaries/longquotes/pixels/privateactive/auth/databasesexcluded. Verified noforcepush.'))
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],originals_solved=9,accepted_papers=79),indent=2))
