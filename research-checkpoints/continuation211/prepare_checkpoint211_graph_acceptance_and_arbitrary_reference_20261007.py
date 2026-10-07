from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation211.json';F=G/'continuation211-publication-records';S=K/'small-batch205206-public-status-20261007-continuation211'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation210.json').read_text())
assert prior['commit_sha']=='bad032b33e33ec83ad47239f2fcdc00557457275' and not prior['force_update']
assert all(prior[q] for q in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
D=K/'public-P05.2-continuation262-corrected-raw-uniformities-and-all-continuous-graph-contact'
a=json.loads((D/'whole-partial-paper-acceptance204-20261007.json').read_text())
assert a['verdict']=='PASS' and a['cumulative_accepted_paper_number']==78
assert sha(D/'P05.2-paper.tex')==a['source_sha256']=='b756af20301a93fba71af139b24b5bc8fd264b57a54a1d941aa05392d97f33f7'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n in [204,205,206]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
    items.append(dict(round=n,atom='P16.4' if n==205 else 'P05.2',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],
                 public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2 and items[0]['unsettled_calls']==0
working=next(K.glob('P05.2-continuation271-*.json'));w=json.loads(working.read_text());assert not w['new_mathematical_grant'] and not w['original_closed']
batch=dict(recorded_utc=now,items=items,active_items=active,maximum_concurrent_campaigns=2,
           focus='Original P16.4 author205 actual original-bundle all-genus inverse/everypoint equation; original P05.2 author206 new arbitrary-real-reference mixed-completion route and full higher-dimensional all-obstacle contact classification. Entire27page S262 accepted204, no original closure.',
           new_accepted_paper=True,accepted_paper_number=78,original_closed=False)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['historical_reviewed_scoped_papers']==78 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,current_small_batch=batch,
             P05_2_arbitrary_reference_working271=dict(path=str(working),sha256=sha(working),status='UNREVIEWED rational positive PC component in minimal active face, true same-reference compact-test auxiliaries/rational cutoffs, exact proper-height bound for ALL fixed-C mixed tuples; no arbitrary-reference bad-jet gluing or allCONTPC regularization grant.',new_mathematical_grant=False,original_closed=False),
             next_work='Continue unchanged original P16.4/P05.2 with at most two native61xhigh campaigns; settled sources receive full ROOT reads/reproduction/independent whole review. Regular verified GitHub pushes, all scopes/failures/current editor preserved.',
             github_pending_checkpoint=dict(continuation=211,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n');shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint211: whole all-continuous real graph paper accepted; arbitrary-reference route\n\n9/42 originals solved;33 open;78 accepted scoped/supporting papers. ENTIRE27page262 independently PASS204: all19proofunits/unnumbered constructions/EIGHT exact notes reconstructed, three COMPLETE A/B/R grants/all clarifications only. Full25562-character report,3premises and14passages ROOT-read; exact native/canonical/task/argument/20whole frozen units/zero-based premise bindings verified. Thirteen external passages cover every premise; the separate task grant-authorization passage is excluded from source evidence.\n\nS262 now grants complete all-C_b REAL graph regularization/raw primitive-Stieltjes operator/contact iff local relation cone equals actual weight ray, arbitrary actual real reference coefficients and positive weights on rational geometry. It also grants corrected finite PA contact/raw examples, actual quadratic nonPA endpoint/literal gap, and material ordinary-weak/global-vague/fixed-C-weak-BL mixed completion. Actual common K_C quantifier includes ALL completed tuples. All source/body/ledger/material/exact notes previously whole ROOT-read; checker/Pandoc/two local builds reproduced clean. Only pages1/14/21/24/27 visually checked; builtin23 unavailable, no SUCCESS. Original higher-dimensional all-obstacle/nonPA/arbitrary-reference classification OPEN; old247/196 and255/200 remain FAIL. Exact accepted source unchanged, all harmless clarifications supplied.\n\nNEW UNREVIEWED ROOT271 rational positive PC component route: finite-carrier rational support/circuit cone and minimal active face yield exact original gamma=gamma-prime+epsilon gamma0 with gamma0 rational positive-growth and gamma-prime PC. Same-reference sums transfer actual compact-test auxiliaries without irrational maximum walls; rational gamma0 cutoffs give proper H0 moment K_C,0=(2d/epsilon)CM+J0 for ALL tuples in each fixed-C family. This would extend REAL genuine mixed completion to arbitrary actual real coefficients on rational geometry. It does NOT grant allCONTPC regularization, arbitrary-reference bad-jet gluing or the full contact classification.\n\nOriginal206 now reconstructs that NEW proof and seeks full higher-dimensional classification with FOUR complete A/B/R/S262 grants/all clarifications, whole old FAILs as data;22whole units/4bound original BMPSv1 and BBGS publisher files,61xhigh. Original205 continues actual all-genus/general-dimensional equation,46whole units/62literal original files/eight grants,61xhigh. At most two campaigns, no active private output/hot feedback.\n\nVerified no-force publication; only settled/public research and source metadata uploaded. No third-party full texts/images, active private streams/databases/accounts. Protected editor unchanged and open.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation211/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
    for p in sorted(folder.iterdir()):add(p)
for name in ['whole-partial-paper-acceptance204-20261007.json','harmless-reader-clarifications204-20261007.json']:add(D/name)
for name in ['P05.2-round204-actual-canonical-independent-review-20261007.json','P05.2-round204-native-model-final-review-20261007.json','P05.2-round204-whole-graph-contact-review-binding-20261007.json']:add(K/name)
add(working)
C=next((R/'campaigns/round-206').iterdir())
for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json']:add(C/name)
for name in ['bind_and_accept_graph_contact262_review204_20261007.py','write_arbitrary_reference_completion271_20261007.py','prepare_original_polyhedral206_after_graph_acceptance_20261007.py','launch_frozen_original_polyhedral206_20261007.py','record_verified210_20261007.py']:add(R/name)
add(G/'push-receipt-continuation210.json');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),
       fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=78,
       commit_message='Accept entire corrected raw and all-continuous graph paper; advance arbitrary-real-reference mixed completion',
       scope='Whole27page262 PASS204 all19results/eight exactnotes/three whole A-B-R grants+allclarifs; full report3premises14passages ROOTread exactnativecanonical20wholeunits/zero-basedcoverage verified, task-only authorization excluded. S262 fourth grant,78accepted9originals33open. NEW271 unreviewed rational PC summand at activeface, true same-reference irrational-coefficient mixedcompletion/properheight commonALLfixedCmoment; no allCONTPC/badjet/fullclassification closure. Original205/20661xhigh atmosttwo frozen campaigns. Old196/200FAIL unchanged; exact accepted source/editor preserved; builtin262 unavailable/265pending withoutSUCCESS. No fullthirdparty/activeprivate/databases/accounts; verified noforce checkpoint.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],originals_solved=9,accepted_papers=78),indent=2))
