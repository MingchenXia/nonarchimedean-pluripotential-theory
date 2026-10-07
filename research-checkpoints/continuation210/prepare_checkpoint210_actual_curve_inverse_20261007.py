from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation210.json';F=G/'continuation210-publication-records';S=K/'small-batch204205-public-status-20261007-continuation210'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation209.json').read_text())
assert prior['commit_sha']=='adf55f9f5908e565e6dc4b3f9fae46a33f80511f' and not prior['force_update']
assert all(prior[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
D=K/'public-P16.4-continuation265-actual-positive-curve-models-and-raw-formal-curvature'
b=json.loads((D/'root-reproduction-binding-20261007.json').read_text())
assert b['own_finite_checker_reproduced'] and b['root_local_build_exit_codes']==[0,0] and b['independent_mathematical_verdict'] is None
assert sha(D/'P16.4-paper.tex')==b['source_sha256']=='c7c1aaaa93e0417b67caec30b1fb80fbe2c4708dc3d40b2f5ac6040385a154e6'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in [203,204,205]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P05.2' if n==204 else 'P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],
                 public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2 and items[0]['unsettled_calls']==0
working=next(K.glob('P16.4-continuation268-*.json'));w=json.loads(working.read_text());assert not w['new_mathematical_grant'] and not w['original_closed']
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,
           focus='WHOLE27-page P05.2 graph/topology review204 and original P16.4 author205: actual formal FS recognition, non-atomic target approximation, full actual all-genus curve inverse/EVERYsolution EVERYpoint uniqueness/invariant descent; general dimension scope unchanged.',
           new_accepted_paper=False,original_closed=False)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==77 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,current_small_batch=batch,
             P16_4_actual_positive_curve_paper=dict(directory=str(D),source_sha256=b['source_sha256'],author_round=203,status='ENTIRE12-page907TeX/304MD/47ledger/13scope/SIX exact FINAL notes ROOT-read,44math13artifact42primary bindings valid, exact finite checker/Pandoc reproduced, two local builds successful with disclosed reference-list warnings. Actual visual pages1/6/9/12. Unconditional same-original FS application absent from203 and supplied newly as267 with complete literal Stacks packet270; entire265 remains UNREVIEWED.',new_mathematical_grant=False,original_closed=False),
             P16_4_actual_curve_inverse_working_proof=dict(path=str(working),sha256=sha(working),status='UNREVIEWED12-step actual all-genus inverse/EVERYpoint route: corrected non-atomic projected measures, actual FS approximation, finite-dual raw energy bound, concrete single decreasing-FS net, actual weighted-FS carrier/trace and radial double-inf proof, invariant singular descent BEFOREdescent.',new_mathematical_grant=False,original_closed=False),
             compiler_availability=dict(P05_2_continuation262='Builtin request23 returned No handler registered; immutable unavailable addendum, two prior local builds clean. No builtin SUCCESS.',P16_4_continuation265='Builtin request53 pending at snapshot without SUCCESS; local builds successful with four disclosed warnings.'),
             next_work='Continue actual original equations and classifications, whole independent review only on settled full sources; few campaigns at a time, regular verified no-force GitHub checkpoints. Do not count scoped papers as original closures.',
             github_pending_checkpoint=dict(continuation=210,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n');shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint210: actual all-genus curve inversion and same-original formal FS\n\n9/42 original problems solved;33 open;77 accepted scoped/supporting papers. New12-page265/native203 is UNREVIEWED, with entire907TeX/304Markdown/47ledger/13scope/SIX EXACT final notes ROOT-read and all44frozen math/42private primary/13artifact bindings verified. Independent exact Q(sqrt2) checks reproduce1188 positive-degree interpolation/3996 orientation/35kernel/19attached-tree cases; finite algebra is not analytic proof. Exact Pandoc conversion and two local builds reproduced. Four reference-list layout warnings disclosed; actual visual pages1/6/9/12 legible. Builtin53 pending without SUCCESS; current protected editor unchanged. Conditional formal FS antecedents, prescribed-target inverse and full original remain OPEN. Failed250/198 unchanged.\n\nNew UNREVIEWED ROOT268 gives an actual all-genus inverse and every-solution all-point working route: cofinal actual graph retractions retaining cycles; projected target can be NONATOMIC, so finite typeII atomic/epsilon approximations precede actual positive original-bundle FS realization; true raw energy/finite-J bound; concrete single decreasing-FS net before E1; true weighted-FS finite carriers and trace laws; radial monotonicity and double infimum include poles and IV/typeI endpoints. Actual normalized singular invariance is proved before original-field descent. This is a reconstruction obligation, not accepted mathematics or original closure.\n\nNext native205 gpt-6.1-sol xhigh now reconstructs those applications and the actual original equation using eight COMPLETE O/D/N/T/Q/C/G/M grants/all clarifications only, whole265/exact203/267/268 and whole250/198 FAIL as DATA. New original Stacks packet270 supplies ten COMPLETE immediate descent/Serre/generation/horizontal/properness units privately, including whole01Q3 generation proof missing from203. No fresh-all-recursive-foundation claim. WHOLE27-page P05.2 independent reader204 continues; at most two campaigns.\n\nP05.2 builtin262 request returned No handler registered; its source and successful separate local compilation retained in a NEW immutable addendum, without changing frozen204 inputs. Only public/settled evidence and original-source metadata published; third-party original full texts/images, active private streams/databases/accounts remain local. Regular verified no-force GitHub publication.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation210/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
    for p in sorted(folder.iterdir()):add(p)
for name in ['P16.4-paper.tex','P16.4-paper.pdf','P16.4-argument.md','source-application-ledger.md','scope-and-gaps.md','finite_checks.py','finite-inputs.json','finite-output.json','root-reproduction-binding-20261007.json','root-visual-and-builtin-request-scope-addendum-20261007.json','README.md']:add(D/name)
for p in sorted((D/'evidence').iterdir()):add(p)
for name in ['P16.4-round203-actual-registered-partial-author-result-20261007.json','P16.4-round203-exact-native-model-final-partial-author-20261007.json','P16.4-round203-whole-actual-positive-curve-author-binding-20261007.json']:add(K/name)
add(working)
add(K/'continuation270-actual-formal-FS-primary-LOCALONLY/retrieval-binding.json')
add(K/'public-P05.2-continuation262-corrected-raw-uniformities-and-all-continuous-graph-contact/root-builtin-unavailable-addendum-20261007.json')
C=next((R/'campaigns/round-205').iterdir())
for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json']:add(C/name)
for name in ['bind_and_reproduce_actual_positive_curve265_20261007.py','record_builtin262_unavailable_20261007.py','retrieve_actual_formal_FS_primary270_20261007.py','write_actual_curve_inverse268_20261007.py','prepare_original_curve_equation205_20261007.py','launch_frozen_original_curve_equation205_20261007.py','record_verified209_20261007.py']:add(R/name)
add(G/'push-receipt-continuation209.json');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),
       fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=77,
       commit_message='Advance actual all-genus curve inversion and same-original formal FS; preserve complete positive-model draft',
       scope='Entire12page265907TeX304MD47ledger6EXACTFINALs ROOTread,44math42primary13artifacts verified/checker+Pandoc/two local builds successful; reference-list warnings/partialvisual scope disclosed. UNREVIEWED268 actual inverse/everypoint route including NONATOMIC projected measure correction, genuine FS approximation, finite-J rawenergy, concrete decreasing-FS net, true graphtrace/radial doubleinf/allpoint/invariant singular descent. Original205 active61xhigh8wholegrants/allclarifs,46wholemath/62literalprivateprimaryfiles; whole250-198FAIL unchanged. WHOLE204graphreview active.9originals33open77accepted. Builtin262 unavailable/265pending noSUCCESS, protectededitor unchanged, no fullthirdparty/activeprivate/databases/accounts. Verified noforce checkpoint.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],originals_solved=9,accepted_papers=77),indent=2))
