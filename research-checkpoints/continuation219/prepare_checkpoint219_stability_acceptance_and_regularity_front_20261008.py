from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
D=K/'public-P16.4-continuation279-higher-dimensional-stability-and-maximizing-output-limits'
M=G/'upload-manifest-continuation219.json';F=G/'continuation219-publication-records';S=K/'small-batch215216-public-status-20261008-continuation219'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,v):Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation218.json').read_text())
assert prior['commit_sha']=='b125e92eae324285e5d582b88ca17c194fa3fcc2' and not prior['force_update']
assert all(prior[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
accept=D/'whole-mathematical-paper-acceptance-after-audit214-20261008.json';a=json.loads(accept.read_text())
assert a['cumulative_accepted_paper_number']==81 and not a['original_closed'] and not a['automatic_acceptance'] and not a['canonical_xean_review_role']
assert a['native_mathematical_verdict']==a['ROOT_mathematical_verdict']=='PASS'
for key in ['source','argument','pdf']:assert sha(a[key])==a[key+'_sha256']
binding=Path(a['review_binding']);assert sha(binding)==a['review_binding_sha256']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in [214,215,216]:
    c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';write(p,st)
    items.append(dict(round=n,atom='P16.4' if n==214 else 'P05.2' if n==215 else 'P05.1',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,accepted_paper_number=81,original_closed=False,focus='Independent215 whole unchanged all-continuous-affine282 audit plus original216 full coefficient-separated P05.1 regularity classification. S279 is accepted only in its full stability/maximizing-output scope; general equation stays open.')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==81 and j['github_pending_checkpoint'] is None and j['github_checkpoint']['commit_sha']==prior['commit_sha']
    j.update(updated_utc=now,current_small_batch=batch,P05_1_original_continuation216=dict(directory=items[2]['directory'],whole_math_files=33,whole_math_bytes=687766,only_grants=['A224','B225','R230','S262','S272'],all_clarifications_retained=True,working_ROOT276277278281283284285_and_NEW282_not_grants=True,full_original_family_dossier_preserved=True,source_typography_controls_replaced=0,model='gpt-6.1-sol',reasoning='xhigh',new_accepted_paper=False,original_closed=False),next_work='Continue215 whole independent282 audit and216 ORIGINAL P05.1 classification. ROOT can progress independent mathematics without third campaign or private ACTIVE output/hotfeedback. S279 whole stability/output-limit theorem is accepted with all source-preserving clarifications, while originalP16.4 inverse/attainment/allpointuniqueness remain open. All33 original goals persist; regular verified pushes.',github_pending_checkpoint=dict(continuation=219,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    write(p,j);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint219: higher-dimensional stability accepted; original regularity classification resumed\n\n9/42 original problems solved;33 open;81 accepted scoped/supporting mathematical papers. S279 now has whole independent214 mathematical PASS plus complete ROOT mathematical/source/evidence review and exact reproduction. Its unchanged588-line9-page paper establishes signed nonordered singular Dirichlet/PL stability, exact all-dimension energy-defect coefficients, mixed-measure fibre rigidity, known-output dual stability, and a canonical intrinsic positive Radon limit for ALL maximizing nets and mixed tuples. Quantitative intrinsic test bounds precede applying M to the limit. Reference covariance retains the selected-reference moment boundary. The competitor-only Euler statement is an inequality criterion. General originalP16.4 still lacks actual potential attainment, lambda=every target, and every-point finite-constant uniqueness; it remains open.\n\nROOT read all four EXACT214 FINAL notes and the separate saved draft, entire mathematical/report unique contents and all5named/15equation/64proof-and-scope/41unnumbered groups,9grant scopes/allclarifications,4ordinary foundation groups,10granted and4original BE applications. Repeated master-report sections were verified against the complete read separate reports; master decisive reasoning equals SAVED draft, not FINAL. All31math87ownhistory62primary bindings and184auditor inventory entries match actual unchanged bytes. ROOT reproduced the inspected own528-coefficient checker exactly; previous136/1089 formal checks, exact conversion and localbuilds remain. Historical initial unusable conversion and intermediate warning remain; two ROOT passes succeeded, first with a rerun warning and final clean. No universal historical negative-operation authentication is claimed. Ordinary nativeWORKER review is not canonical Xean review or automatic acceptance.\n\nCurrent two-campaign batch is independent215 unchanged282 all-C_b affine/contact audit and original216 ENTIRE P05.1 coefficient-separated regularity classification, both native61xhigh.216 has exactly5whole grants/allclarifications,33wholemath files687766bytes,4original primaries, unchanged full44807-character family dossier and older/current working proofs only as DATA to reconstruct. Its original source contains zero disallowed control characters; no normalization change was made. The full compact-local-chart literal, general singular higher-dimensional real, and arbitrary nonseparable obstacle scope remains required; partial sectors cannot close the original. No third campaign, private ACTIVE read or hot feedback.\n\nProtected editor stays open unchanged. Existing builtin204/249 pending observations are preserved without claiming compiler success/failure; local builds are separate evidence. Original full primaries/long quotations/pixels/private streams/databases/auth are excluded. No-force update independently verifies the remote tree, every blob and branch reference.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation219/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
    for p in sorted(folder.iterdir()):add(p)
for p in [accept,D/'harmless-reader-clarifications-after-audit214-20261008.json',binding,K/'P16.4-round214-exact-native-model-final-whole-stability279-local-audit-20261008.json']:add(p)
for p in sorted((D/'evidence/independent-local-audit214').rglob('*')):
    if p.is_file() and 'LOCALONLY' not in str(p.relative_to(D)):add(p)
c=next((R/'campaigns/round-216').iterdir())
for name in ['task.json','original-task.json','original-family-task.json','normalization-data.json','freeze.json','input.json','settings.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json','launch-record.json']:add(c/name)
for name in ['bind_and_accept_stability279_after_local_audit214_20261008.py','prepare_original_regularity_campaign216_20261008.py','launch_original_regularity_campaign216_20261008.py','record_verified218_20261008.py']:add(R/name)
add(G/'push-receipt-continuation218.json');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=81,commit_message='Accept whole higher-dimensional stability paper and resume original regularity classification',scope='S279 wholemath accepted after independent214 and ROOT fullproof/source/evidence/exact528repro; nativeFINAL distinctsaveddraft retained, sourceunchanged; no inverse/attainment/allpointuniqueness/originalclosure.215 whole282audit and216 ORIGINALP05.1author native61xhigh exactlytwo;33math4primary fullfamily DATA scope.9solved33open81accepted; protectededitor/auth/runtimeunchanged thirdparty/privateexcluded noforceverify.'))
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],originals_solved=9,accepted_papers=81),indent=2))
