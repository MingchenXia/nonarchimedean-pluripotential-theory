from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
D=K/'public-P05.2-continuation282-all-continuous-affine-spaces-and-affine-arrangements'
M=G/'upload-manifest-continuation218.json';F=G/'continuation218-publication-records';S=K/'small-batch215-public-status-20261008-continuation218'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,v):Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation217.json').read_text())
assert prior['commit_sha']=='f400ddc7034cf68bf6d737b83e849e908a412727' and not prior['force_update']
assert all(prior[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
rep=json.loads((D/'root-reproduction-binding-20261008.json').read_text())
assert not rep['mathematical_acceptance'] and not rep['original_closed'] and rep['finite_output_exact'] and rep['latex_to_markdown_exact']
for key in ['source','argument','pdf']:assert sha(rep[key])==rep[key+'_sha256']
working=[next(K.glob('P05.2-continuation284-*.json')),next(K.glob('P05.2-continuation285-*.json'))]
for p in working:
    j=json.loads(p.read_text());assert not j['new_mathematical_grant'] and not j['original_closed']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in [213,214,215]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';write(p,st)
    items.append(dict(round=n,atom='P16.4' if n==214 else 'P05.2',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False,new_accepted_paper=False))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2
write(D/'builtin-compile-pending-addendum-20261008.json',dict(recorded_utc=now,source_sha256=rep['source_sha256'],unchanged=True,builtin_compile_request=dict(cell_id='249',path=rep['source'],pending=True,last_wait_no_result=True,no_success_or_failure_claimed=True),local_build_exit_codes=[0,0],local_final_diagnostics=[],protected_editor_unchanged_open=True,no_new_tab=True,mathematical_acceptance=False,original_closed=False))
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,accepted_paper_number=80,original_closed=False,focus='Independent215 whole unchanged all-continuous-affine282 mathematical/local-source audit active;214 completed scopedPASS assertion awaits full ROOT review. NewROOT284285 unreviewed DATA excluded from215.')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==80 and j['github_pending_checkpoint'] is None and j['github_checkpoint']['commit_sha']==prior['commit_sha']
    j.update(updated_utc=now,current_small_batch=batch,P05_2_affine_arrangement282=dict(source=rep['source'],source_sha256=rep['source_sha256'],argument=rep['argument'],argument_sha256=rep['argument_sha256'],pdf=rep['pdf'],pdf_sha256=rep['pdf_sha256'],root_reproduction=str(D/'root-reproduction-binding-20261008.json'),full_ROOT_source_argument_ledger_scope_exact_FINAL_and_saved_draft_read=True,saved_notes_differ_from_FINAL=True,source_to_markdown_and_finite_reproduction_exact=True,local_clean_final_build=True,independent_local_source_review_round=215,whole_immutable_math_files=27,whole_math_bytes=596991,own_historical_files=46,only_grants=['A224','B225','R230','S262','S272'],new_accepted_paper=False,original_closed=False),P05_2_new_working284285=[dict(path=str(p),sha256=sha(p),new_mathematical_grant=False,new_accepted_paper=False,original_closed=False,not_supplied_to_active215_or_old213214=True) for p in working],next_work='Continue215 full unchanged282 independent audit and ROOT read ENTIRE settled214 report/exactFINAL/wholeproof/source premises/reproduction before any279 acceptance. At most two61xhigh campaigns. ROOT284 actualREALfull-affine alternative and285 fixed-fan exactpolynomial facetests are UNREVIEWED, not grants or fullclassification. GeneralP16.4 inverse/attainment/allpointuniqueness and generalP05.2 remain open. Continue all33 originals and regular verified pushes.',github_pending_checkpoint=dict(continuation=218,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    write(p,j);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint218: all-continuous affine-space contact and affine-arrangement draft\n\n9/42 original problems solved;33 open;80 accepted scoped/supporting mathematical papers. New UNREVIEWED282 proposes global real-PA regularization for every continuous convex function bounded relative to any actual real PA positive-growth reference on complete rational affine support. It proves all-bounded-continuous-obstacle contact in that sector and classifies finite positive affine-plane arrangements by pairwise disjointness. Intersections give a positive complete tangent-plane subcycle and transverse two-sided line, an explicitly calibrated primitive raw atom, and an actual-reference finite-PA negative-contact witness. General singular and abstract/glued categories remain open. ROOT read the whole source, argument, ledger, scope, four exact FINAL notes and separate saved draft; saved draft differs in all four notes. Reproduction retains exact finite arithmetic, exact LaTeX-to-Markdown conversion, and two successful local passes with a clean final build. Whole independent215 native61xhigh ordinaryWORKER audit freezes27wholemath bodies with all5grants/allclarifications,4original primaries and46ownhistorical files. It is not canonical review or automatic acceptance.\n\nSettled214 asserts a scoped mathematical PASS for279, but its whole report/exact FINAL/evidence is still awaiting ROOT review; no paper is accepted by this checkpoint. NewROOT284 independently extends an alternative full-affine approximation/contact route to actual REAL references by exact cone-face decomposition and bounded clipped support-plane estimates; ROOT285 gives a finite polynomial-identity criterion on marked faces for ONE fixed rational tangent fan, and an actual-reference obstruction when the granted global jet/roof hypotheses hold. Both are complete UNREVIEWED working data, not grants, not supplied to213214215, and not full structural classifications.\n\nBuilt-in282 compiler request249 remains pending with no returned diagnostics; local compilation is separate evidence. Protected editor stays open unchanged, no new tab. Original thirdparty full texts/long quotations/pixels/private active outputs/databases/auth are excluded. No-force update with independent tree/blob/ref verification.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation218/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
    for p in sorted(folder.iterdir()):add(p)
for p in sorted(D.rglob('*')):
    if p.is_file() and p.suffix not in ['.aux','.out'] and 'LOCALONLY' not in str(p.relative_to(D)):add(p)
for p in working:add(p)
c=next((R/'campaigns/round-215').iterdir())
for name in ['task.json','original-task.json','freeze.json','input.json','settings.json','mathematical-packet-bindings.json','historical-own-evidence-bindings.json','private-primary-packet-bindings.json','launch-record.json']:add(c/name)
for name in ['reproduce_affine_arrangements282_20261008.py','prepare_affine_arrangements_audit215_20261008.py','launch_affine_arrangements_audit215_20261008.py','write_real_reference_full_space_contact284_20261007.py','write_fixed_fan_algebraic_contact_test285_20261007.py','record_verified217_20261007.py']:add(R/name)
add(G/'push-receipt-continuation217.json');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=80,commit_message='Retain full all-continuous affine contact and arrangement draft for independent review',scope='UNREVIEWED282 wholeROOTread exactFINAL distinct saveddraft, exactfinite/sourceMD and11p localbuild;215 independentWHOLEaudit27math4primary46ownevidence.214 settled awaitsROOTfullread noaccept. New284actualREALfullaffine and285fixedfanpolynomialface workingDATA notgrants/nohotfeedback.9originals33open80accepted. Builtin249pending/editorunchanged. Thirdparty/privateexcluded/noforceverify.'))
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],originals_solved=9,accepted_papers=80),indent=2))
