from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
M=G/'upload-manifest-continuation204.json'; F=G/'continuation204-publication-records'
S=K/'small-batch197199-public-status-20261007-continuation204'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation203.json').read_text())
assert prior['commit_sha']=='854df68ff97ae97f74a45f8f7d7e56143196eb9d' and not prior['force_update']
assert all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
fail=K/'P16.4-round198-whole-direct-formal-FAIL-review-binding-20261007.json'
assert json.loads(fail.read_text())['verdict']=='FAIL'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat(); F.mkdir(); S.mkdir(); items=[]
for n in (195,196,197,198,199):
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json'; p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P05.2' if n in (196,197) else 'P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0]; assert len(active)<=2
assert all(e['unsettled_calls']==0 for e in items if e['round'] in (195,196,198))
working=[K/'P16.4-continuation251-original-FS-reference-and-maximal-residual-coordinate-application-working-proof-20261007.json',K/'P16.4-continuation252-general-reference-moment-and-intrinsic-dual-working-proof-20261007.json']
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,focus='197 original P05.2 whole classification after material contact hypothesis and coupled endpoint repair;199 original P16.4 with seven whole grants including accepted genus-zero theorem, explicit material coercivity repair and new general reference-moment/target-criterion route252. Whole198 FAIL preserved; no new acceptance.',completed198_verdict='FAIL',new_accepted_paper=False,original_closed=False)
for name in ('active-work.json','checklist-current.json'):
    p=R/name; j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==76 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,current_small_batch=batch,P16_4_latest_reference_moment_working252=dict(records=[dict(path=str(p),sha256=sha(p)) for p in working],status='Unreviewed full initial-reference application251 and general-dimensional uniform reference moment/intrinsic dual/coercivity proof252. Actual common curve preserves original section values; degree controls annular slopes; CLD support alone suffices. Original inverse existence/attainment/every-point uniqueness remains open.',mathematical_grant=False,new_accepted_paper=False,original_closed=False,author_round=199),next_work='Continue original native197 and199 with at most two active campaigns, read settled results completely, reconstruct and independently review new mathematics, and keep regular verified GitHub checkpoints. No original closure from criteria alone.',github_pending_checkpoint=dict(continuation=204,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n'); shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint204: general reference-moment work and material coercivity failure\n\n9/42 originals solved,33 open,76 independently accepted scoped/supporting papers. Whole198 independently returned FAIL on unchanged18-page250: M0 alone does not imply coercivity; finite U_mu is necessary. The actual P1 Gauss/delta-at-zero counterexample is preserved in the full report. All16 premises and47 zero-based passages were read; external premise coverage0-13, missing original-primary bindings14/15 expressly retained. No new acceptance or silent source repair.\n\nROOT251 supplies an unreviewed initial-reference/maximal-residual coordinate application. ROOT252 supplies a full proposed general-dimensional uniform reference moment and intrinsic dual criterion: one actual common generic-incidence curve, original section-map degree and annular slope bounds, and genuine CLD atomic support without the coefficient formula. This is not general prescribed-target existence or every-point uniqueness.\n\nOriginal author199 launched with seven WHOLE accepted grants, now including whole genus-zero G227 and all unchanged clarifications,43 complete mathematical data units and26 private read-only primary files. Author197 continues full P05.2 classification; max two native61xhigh campaigns. Source250 and frozen198 inputs remain unchanged; built-in250 request remains unverified as recorded at checkpoint203, two clean local builds remain evidence. Native authentication/runtime and protected editor preserved. Full third-party sources, original dossiers, private inspection/stdout/SQLite and active streams excluded.\n')
files=[]
def add(p,target=None):
    p=Path(p); assert p.is_file() and 'LOCALONLY' not in p.name
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation204/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in (F,S):
    for p in sorted(folder.iterdir()):add(p)
for p in working:add(p)
for name in ('P16.4-round198-actual-canonical-independent-FAIL-review-20261007.json','P16.4-round198-native-model-final-FAIL-review-20261007.json','P16.4-round198-whole-direct-formal-FAIL-review-binding-20261007.json'):add(K/name)
add(K/'public-P16.4-continuation250-direct-formal-recognition-and-target-bounds/independent-whole-paper-FAIL198-20261007.json')
C=next((R/'campaigns/round-199').iterdir())
for name in ('freeze.json','mathematical-data-bindings.json','launch-record.json'):add(C/name)
for name in ('bind_whole_direct_formal_FAIL198_20261007.py','write_initial_coordinate_application251_20261007.py','write_general_reference_moment252_working_proof_20261007.py','prepare_original_equation199_after_reference_moment_and_FAIL198_20261007.py','launch_frozen_original_equation199_after_reference_moment_20261007.py','record_verified203_20261007.py'):add(R/name)
add(G/'push-receipt-continuation203.json'); add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=76,commit_message='Preserve coercivity counterexample and advance general reference-moment criterion',scope='Whole198 independent FAIL and exact native/canonical/frozen bindings; actual P1 counterexample refutes unqualified coercivity despite M0=0. Correct finite-target hypothesis requires new mathematics; old250 source untouched. Unreviewed251 initial-reference and252 all-dimensional M0/intrinsic dual/coercivity proof, with remaining original inverse existence/attainment/every-point uniqueness explicit. Original199 launched with seven WHOLE grants including genus-zero227/all clarifications,43 whole math units and26 private original primary files.197 full original classification continues.9/42 originals solved33open76accepted; no new acceptance or original closure. Native61xhigh max2; no hot feedback/auth/runtime/editor changes. Full third-party/source dossier/private inspection/stdout/SQLite/active streams excluded.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],accepted_papers=76),indent=2))
