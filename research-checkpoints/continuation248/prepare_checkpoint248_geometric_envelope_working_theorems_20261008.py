from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation248.json';F=G/'continuation248-publication-records';S=K/'small-batch242-244-public-status-20261008-continuation248'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not M.exists() and not F.exists() and not S.exists()
prior=json.loads((G/'push-receipt-continuation247.json').read_text())
assert prior['commit_sha']=='7d01ac5ddcb21c2d3dcbaa2c21a9b7e41fcc9a00' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
P=K/'P12.3-continuation335-continuous-obstacle-geometric-envelope-failure-on-double-plane-working-proof-20261008.md'
B=K/'P12.3-continuation335-ROOT-whole-working-proof-source-scope-and-binding-20261008.json'
binding=json.loads(B.read_text());assert sha(P)==binding['proof']['sha256']=='443585a7f043e428ec9b41422913547a18385cf4589a6898f182c6f1dc59083c'
assert not binding['original_closed'] and not binding['paper_accepted'] and not binding['hot_feedback_sent']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat();F.mkdir();S.mkdir();items=[]
for n,atom in [(242,'P12.3'),(244,'P03.1')]:
    c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';write(p,st)
    items.append(dict(round=n,atom=atom,status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],public_status=str(p),original_closed=False,private_active_output_read=False,hot_feedback_sent=False))
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==91 and x['github_pending_checkpoint'] is None
    x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=248,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Continue native242 P12.3 and native244 P03.1 max2; ROOT335 actual geometric envelope counterexample, conductor criterion and exact BFJ smooth continuity await independent proof/source/scope review after current frozen calls settle;13solved29OPEN91accepted unchanged; verify248.')
    x['P12_3_ROOT335_unreviewed_working_result']=dict(proof=str(P),binding=str(B),proof_sha256=sha(P),original_closed=False,paper_accepted=False,active_campaigns_not_given_proof=[242,244])
    write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint248: actual geometric envelope obstruction and precise conductor reduction, UNREVIEWED\n\n13/42 originals solved,29OPEN,91 accepted papers UNCHANGED. This checkpoint publishes a substantive ROOT working proof for originalP12.3, not a closure or accepted paper. Native242 P12.3 and244 P03.1 remain a max2 small batch; neither frozen campaign has received this later work or hot feedback. Native auth/runtime and protectedP16.4 editor are preserved.\n\nThe working proof computes the FULL completed geometric raw envelope and its regularization for a finite continuous obstacle on the excellent double-plane ring k[x,y,z]/xy localized at its origin, in EVERY characteristic and with ALL semivaluation supports. Regularization violates a necessary geometric-positivity inequality, so the blanket excellent-nonnormal envelope theorem is false. This uses actual primary blowups and the whole qualified accepted G331 geometric comparison, not a radial analytic substitute.\n\nActual PRIMARY conductor masks give equality with the separated normalization raw envelope on the dense finite-conductor locus. Consequently downstairs regularized positivity is equivalent to continuity and fibre-constancy of the full normalized raw envelope, including every infinite-conductor fibre. Any conductor fibre joining distinct normal centres obstructs the universal property, without granting normal-envelope positivity. Curves retain min(obstacle,0).\n\nThe exact published BFJ smooth affine CLOSED-germ algebraically closed characteristic-zero scope is treated positively: complete3.18 yields uniform CM/l primary approximation for dual-complex/PA obstacles,1.15 and raw sup-norm contraction then give every finite continuous obstacle, ALL supports and every primary gauge. This does NOT prove the envelope property for every excellent singular normal germ or transfer SNC/multiplier methods to arbitrary characteristic. Primary source bodies/pixels and private active native outputs remain LOCALONLY. Current source-unit metadata and the complete G331 mandatory qualification/source ledger accompany the proof. Independent mathematical, primary-source and whole-original-scope review is still required.\n')
files=[];seen=set()
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    target=target or 'research-checkpoints/continuation248/'+str(p.relative_to(R));assert target not in seen;seen.add(target)
    files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]:
    for p in sorted(folder.rglob('*')):
        if p.is_file():add(p)
for p in [P,B,R/'record_ROOT335_working_source_and_scope_20261008.py',R/'record_verified247_20261008.py',G/'push-receipt-continuation247.json',Path(__file__)]:add(p)
for e in binding['grant_import_requires_all']:add(e['path'])
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
x=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=29,historical_reviewed_scoped_papers=91,commit_message='Record geometric envelope counterexample, exact conductor criterion and smooth working proof',scope='UNREVIEWED ROOT335; counts13solved29OPEN91accepted unchanged; max2 frozen native242244; qualified G331; exact BFJ scope; private sources/active outputs excluded.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active),indent=2))
