from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation246.json';F=G/'continuation246-publication-records'
S=K/'small-batch-public-status-20261008-continuation246'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists()for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation245.json').read_text())
assert prior['commit_sha']=='cad9792fb7df5fc81ed452198e46eeadc15c88d6' and not prior['force_update']
assert all(prior[k]for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n,atom in [(240,'P12.2'),(241,'P05.2')]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';write(p,st)
    items.append(dict(round=n,atom=atom,status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],public_status=str(p),original_closed=(n==241),private_active_output_read=False,hot_feedback_sent=False))
assert items[1]['status']=='completed' and items[1]['unsettled_calls']==0
active=[e['round']for e in items if e['unsettled_calls']];assert len(active)<=2
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text())
    assert len(x['fully_solved_original_atoms'])==12 and x['remaining_open_original_atoms']==30 and x['historical_reviewed_scoped_papers']==90 and x['github_pending_checkpoint']is None
    x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=246,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Continue remaining30 original problems in at most2 native gpt-6.1-sol xhigh campaigns; P12.2 whole review240 ongoing; prepare next original P12.3. Verify checkpoint246 before marking publication complete.')
    write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint246: complete original P05.2 accepted after independent241 and ROOT whole reconstruction\n\n12/42 original problems solved;30 OPEN;90 accepted papers. Native239 continuation332 supplies the unchanged14-page complete coefficient-separated orthogonality classification. All five actual author proof notes and all eight actual independent241 review notes were ROOT read, with complete independent proof/source/scope/noncircularity/evidence records. Mathematics, new source applications and whole original scope PASS at the exact globally embedded all-face balanced category. Real pairs iff explicit infinite carrier/tree/primitive-polynomial criterion, equivalently genuine domain and exact contact for ALL bounded continuous obstacles. Every positive-dimensional admitted literal pair fails its admitted-obstacle domain; d0/empty cases direct; compact positive-dimensional objects absent by divergence. No terminating algorithm or universal real orthogonality claimed.\n\nO332 imports MUST retain the entire mandatory evidence/reader qualification and all underlying qualified assumptions. ROOT independently confirms the previously asserted controller/native assignment difference was false: full decoded inputs, including task, notes AND assignment, are equal; raw serialization bytes differ. Historical erroneous binding and frozen/published records remain unchanged and are explicitly corrected. Review saved expanded prose differs from actual FINAL and is not presented as the actual result. Source/PDF unchanged; builtin compilation succeeded. Hashes and finite diagnostics are not proofs.\n\nROOT328 is a separately reviewed optional finite-vertex consequence with smaller-tolerance strict-margin precision, not author239 input or an essential rescue. Later ROOT333334 countable rational witnesses and explicit F_sigma_delta working proofs remain UNREVIEWED, NOT supplied to either frozen author239 or reviewer241, and NOT acceptance premises. Current exact BBGS source-reading metadata added; primary bodies/images/excerpts, private provider/controller logs remain LOCALONLY. Native240 independent whole originalP12.2 review remains separate and grants no P12.2 closure until its actual completed proof/source/scope result is checked. At most2 native campaigns; signed-in authentication/environment and protected P16.4 editor preserved.\n\nPublication follows verified245 by nonforce update and independent exact Git file/blob/tree/ref verification. Historical FAIL/INCONCLUSIVE retained.\n')
files=[];seen=set()
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY'not in str(p.relative_to(R))
    target=target or 'research-checkpoints/continuation246/'+str(p.relative_to(R));assert target not in seen;seen.add(target)
    files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
D=K/'public-P05.2-continuation332-carrier-tree-primitive-polynomial-whole-original-candidate'
for folder in [F,S,D]:
    for p in sorted(folder.rglob('*')):
        if p.is_file():add(p)
for p in [K/'P05.2-round241-whole-original-carrier-tree-classification332-ROOT-binding-20261008.json',K/'round241-actual-native-final.json',K/'P05.2-continuation333-countable-rational-obstacles-finite-rational-forests-and-polynomial-feasibility-working-proof-20261008.md',K/'P05.2-continuation334-rational-relative-witnesses-and-explicit-F-sigma-delta-pair-classification-working-proof-20261008.md',K/'P05.2-additional-BBGS-real-signed-recursion-and-normalization-ROOT-reading-20261008.json',G/'push-receipt-continuation245.json',R/'record_verified245_and_BBGS_current_application_reads_20261008.py',R/'capture_completed_whole_contact_review241_20261008.py',R/'accept_whole_original_P05_2_after_review241_20261008.py',R/'accept_whole_original_P05_2_after_review241_v2_20261008.py',Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
x=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=30,historical_reviewed_scoped_papers=90,commit_message='Accept complete original P05.2 after whole independent review and preserve explicit evidence correction',scope='12solved30 OPEN90accepted; unchanged14p originalP05.2 and all proof/source/scope reviews; mandatory assignment-equality correction; ROOT333334 remain unreviewed; P12.2 review240 separate.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active),indent=2))
