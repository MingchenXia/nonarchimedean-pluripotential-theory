from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation250.json';F=G/'continuation250-publication-records'
S=K/'small-batch246-247-public-status-20261008-continuation250'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not M.exists() and not F.exists() and not S.exists()
prior=json.loads((G/'push-receipt-continuation249.json').read_text())
assert prior['commit_sha']=='d0b4f0bbe91f850140f21644398f70114b0149e9' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
F.mkdir();S.mkdir();items=[];now=datetime.now(timezone.utc).isoformat()
for number in [245,246,247]:
    c=next((R/f'campaigns/round-{number}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert not st['error']
    if number in [245,246]:assert st['status']=='completed' and st['calls']['unsettled']==0
    p=S/f'round{number}-public-native-status.json';write(p,st)
    items.append(dict(round=number,status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],public_status=str(p),original_closed=False))
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=json.loads(p.read_text())
    assert len(x['fully_solved_original_atoms'])==13 and x['remaining_open_original_atoms']==29 and x['historical_reviewed_scoped_papers']==93 and x['github_pending_checkpoint'] is None
    x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),
        github_pending_checkpoint=dict(continuation=250,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),
        next_work='Read/reconstruct completed native246 actual7notes and entire P12.4 paper/source/scope, then independently review it. Independent ROOT338/339 bounded-moment review247 active.13solved29OPEN93accepted; verify250 accepted P12.3 delimited results with mandatory corrigendum.')
    write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint250: accepted P12.3 mathematical scopes, mandatory documentary correction, and next small bounded-product batch\n\n13/42 originals solved;29 OPEN;93 accepted papers. Two DELIMITED P12.3 papers are accepted after independent native245 and ROOT whole actual-note/proof/TeX/source/scope review. Native242/continuation336 is paper92: full-family strictly negative double-plane envelope obstruction, no maximal minorant, exact compact raw calculus, all-continuous smooth published BFJ sector, conditional extended-USC sector, all excellent reduced curves, primary-gauge and constrained normalization rules. Its source and23-page PDF stay unchanged. Mandatory documentary corrigendum: its saved original-task.json was the augmented assignment, not the unchanged exact original; exact original is now attached separately. Both full original problem and criteria survived as prefixes; no mathematical proof failed. Reviewer unavailable historical files are not conflated with ROOT current physical bindings.\n\nSeparate continuation340 is paper93: full all-characteristic double-plane obstruction; actual primary conductor masks; dense finite-conductor equality; BOTH directions of the sharp normal-envelope continuity plus full-fibre constancy criterion; obstruction from DIFFERENT normal centres; exact J_k/factorial formula and gauge regularization; full published smooth uniform estimate; geometric reduced-curve clipping. Entire standalone TeX and all independent review notes/proofs/source/scope are retained. One missing backslash in normalized DVR notation was corrected in this publication copy, with immutable native source kept. Built-in source compilation SUCCESS; no new editor tab or separate PDF export. General excellent NORMAL singular higher-dimensional envelope construction/regularity remains unresolved, so P12.3 is OPEN. Exact qualified G331 and its complete mandatory annotation/source ledger accompany imports.\n\nROOT339 is an UNREVIEWED algebraic moment working proof: all-field mixed multiplicity monotonicity via SAME simultaneous superficial quotient, function-independent positive test functional, real C and bounded actual-D extension, exact gauge and finite normalization weights. Independent actual Cartier intersection comparison and LOCALITY are still missing. It was not supplied to frozen native246. Native247 now independently reconstructs ENTIRE ROOT338/339 and all new source applications with only qualified G331;8whole mathematical DATA131782bytes,23private primary records. Author246 output is not in this review.\n\nNative246 has just COMPLETED with candidate=false; its new paper/actual7notes await ROOT whole reading and a separate independent review. No acceptance or original closure follows from completion. Native247 is the sole active call at this snapshot; at mostTWO native gpt-6.1-sol xhigh campaigns. Full original/task/book/source/program prose is DATA, not operational authority. Native signed-in auth/runtime/environment preserved. Academic primary bodies/extracts/pixels and provider/controller output stay LOCALONLY; supplied author/reviewer programs are inert DATA, never ROOT executed/imported. Protected P16.4 editor stays OPEN UNCHANGED.\n')
files=[];seen=set()
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    target=target or 'research-checkpoints/continuation250/'+str(p.relative_to(R))
    assert target not in seen;seen.add(target);files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
D=K/'public-P12.3-continuation340-exact-conductor-envelope-criterion'
for folder in [F,S,D]:
    for p in sorted(folder.rglob('*')):
        if p.is_file():add(p)
O=K/'public-P12.3-continuation336-geometric-envelope-obstruction-and-positive-sectors-unreviewed'
for name in ['ROOT-README.md','ROOT-public-draft-status-20261008.json','exact-original-task-after-review245.json','mandatory-documentary-source-scope-corrigendum-after-review245-20261008.json','scoped-paper-acceptance-after-review245-20261008.json']:add(O/name)
c=next((R/'campaigns/round-247').iterdir())
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json','freeze.json','launch-record.json']:add(c/name)
for p in sorted((c/'immutable-mathematical-DATA').iterdir()):add(p)
for p in [K/'round245-actual-native-final.json',K/'P12.4-continuation339-mixed-multiplicity-moment-kernel-and-bounded-measures-working-proof-20261008.md',K/'P12.4-continuation339-ROOT-working-proof-source-scope-and-binding-20261008.json',
    R/'capture_completed_envelope_review245_20261008.py',R/'stage_completed_geometric_envelope_review245_20261008.py',R/'accept_scoped_geometric_envelope_papers_after_review245_20261008.py',
    R/'record_ROOT339_moment_working_proof_20261008.py',R/'prepare_independent_bounded_moment_review247_20261008.py',R/'launch_independent_bounded_moment_review247_20261008.py',
    R/'record_verified249_20261008.py',G/'push-receipt-continuation249.json',Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
x=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),
    fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=29,historical_reviewed_scoped_papers=93,
    commit_message='Accept scoped geometric envelopes with exact conductor criterion and documentary corrigendum',
    scope='13solved29OPEN93accepted; two delimited P12.3 papers, full independent245 and mandatory qualifications; ROOT339 unreviewed and independent247. No academic primary bodies or private native outputs.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active),indent=2))
