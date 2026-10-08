from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation222.json';F=G/'continuation222-publication-records';S=K/'small-batch218219-public-status-20261008-continuation222'
D=K/'public-P05.1-continuation291-compact-balanced-charts-and-independent-affine-branches'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,v:Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation221.json').read_text())
assert prior['commit_sha']=='49a125d7d90ae302a4e57295bc514550511a7a41' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
rep=json.loads((D/'root-reproduction-binding-20261008.json').read_text())
assert not rep['mathematical_acceptance'] and not rep['original_closed'] and rep['ROOT_finite_output_exact'] and rep['latex_to_markdown_exact']
for key in ['source','argument','pdf']:assert sha(rep[key])==rep[key+'_sha256']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in [217,218,219]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';write(p,st)
    items.append(dict(round=n,atom='P05.1',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
assert items[0]['observed_status']=='completed';active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,accepted_paper_number=82,original_closed=False,focus='218 independent WHOLE unchanged291 compact/affine/independent-bouquet/literal paper audit;219 new positive-dimensional common-subspace trace-synchronization paper author.217 isolated-crossing author settled, all6 actualFINAL ROOT-read; unchanged whole paper being read/reproduced next.')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text())
    assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==82 and j['github_pending_checkpoint'] is None and j['github_checkpoint']['commit_sha']==prior['commit_sha']
    j.update(updated_utc=now,current_small_batch=batch,new291_unreviewed_paper=dict(path=str(D),source_sha256=rep['source_sha256'],argument_sha256=rep['argument_sha256'],ROOT_exact_finite_assertions=1945,ROOT_finite_output_exact=True,ROOT_latex_to_markdown_exact=True,ROOT_local_build_exit_codes=[0,0],initial_reference_warnings_retained=True,final_disabled_shell_package_warning_retained=True,builtin_compile_requested_cell62=True,builtin_compile_result_pending=True,new_accepted_paper=False,original_closed=False),settled217_status=dict(actual_FINAL_all6_whole_ROOT_read=True,candidate=False,whole_source_read_in_progress=True,new_accepted_paper=False,original_closed=False),next_work='Complete independent218 unchanged whole291 proof/source audit, new219 exact common-subspace convex trace extension and allcontinuous same-reference global rational-geometry PA regularization. At mosttwo native61solxhigh, nohotfeedback/privateACTIVE; ROOT continues whole217 isolated-crossing manuscript/source/exactFINAL/reproduction. Original33 open goals and verified regular pushes persist.',github_pending_checkpoint=dict(continuation=222,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    write(p,j);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint222: compact chart paper, independent audit, and shared-subspace research\n\n9/42 originals solved;33 open;82 accepted scoped/supporting mathematical papers, unchanged. Unchanged291 is an UNREVIEWED complete scoped author paper, not a grant or original closure. Its compact theorem is restricted to boundaryless positive balanced rational local embedding atlases with compatible integral-affine transitions. The complete affine and independent-bouquet real theorem retains the actual reference/recession, global decreasing approximation and arbitrary bounded continuous actual envelopes. The finite noncompact literal obstruction is explicit. Broader abstract compact categories, dependent/positive-dimensional intersections and general singular classes are not silently covered.\n\nROOT read the whole source, ledger/scope/build and all6 actualFINAL notes. Saved note text differs only by one terminal newline each. All49 own artifact identities,33 math and4 original primary bindings are verified. Only the wholly inspected bounded Fraction checker was copied and executed in ROOT scratch: exact1945-assertion output matches. The source-to-Markdown conversion exactly matches, two no-shell-escape local passes succeed, initial reference/rerun warnings and final disabled-shell package warning are preserved. These reproducibility acts are not proof acceptance. A single built-in compile request for291 remains pending; no duplicate request or editor/tab action.\n\nNative218 independently audits the ENTIRE unchanged291 paper, ALL6 exactFINAL notes, full original source applications and historical evidence; exactly5whole old grants/allclarifications. New289/290 and newS282 acceptance are excluded from its inputs. Native219 authors the exact common-subspace book theorem using6whole grants/allclarifications including accepted WHOLE S282 mathematics; native215 historicalINCONCLUSIVE remains. New289 is unreviewed DATA reconstructed from scratch: one dual fiber-minimum extension, genuine rational-PA extension exact on ALLH, synchronized global decreasing approximation before MA. This includes any TWO complete rational planes with a proper positive-dimensional overlap and independent-normal books, without a several-overlap theorem. No private ACTIVE outputs or hotfeedback.\n\nNative217 settled, candidatefalse; all6 actualFINAL notes were ROOT-read. Its full unchanged isolated-crossing paper is still being read/reproduced and is not accepted or uploaded here. Long original primaries/quotes/pixels, private streams/controller output/databases and authentication remain excluded. Protected original editor stays open unchanged. No-force push independently checks every remote blob, native Git tree and branch ref.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation222/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
    for p in sorted(folder.iterdir()):add(p)
for p in sorted(D.rglob('*')):
    if not p.is_file() or 'LOCALONLY' in str(p.relative_to(D)):continue
    if p.suffix in ['.pdf','.aux','.out','.log'] and p!=D/'P05.1-paper.pdf':continue
    add(p)
for n in [218,219]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    for name in ['task.json','input.json','settings.json','freeze.json','launch-record.json','original-task.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json']:add(c/name)
    if n==218:add(c/'historical-own-evidence-bindings.json')
for name in ['reproduce_compact_and_bouquet291_20261008.py','prepare_compact_bouquet_audit218_20261008.py','launch_compact_bouquet_audit218_20261008.py','prepare_common_subspace_book_paper219_20261008.py','launch_common_subspace_book_paper219_20261008.py','record_verified221_20261008.py']:add(R/name)
add(G/'push-receipt-continuation221.json');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=82,commit_message='Preserve compact balanced-chart paper and continue exact shared-subspace approximation',scope='UNREVIEWED291 full compact/affine/independent-bouquet/literal paper, ROOT exact finite/source-conversion/local-build reproduction, independent218 whole unchanged audit and new219 common-subspace author frozen inputs.9solved33open82accepted unchanged. No privateACTIVE/hotfeedback or extra campaign, protectededitor unchanged, primaryquotes/pixels/private streams excluded, noforce remote/blob/nativeGitverify.'))
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],originals_solved=9,accepted_papers=82),indent=2))
