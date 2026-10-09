from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation279-publication-records'; M=G/'upload-manifest-continuation279.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation278.json'); assert prior['commit_sha']=='e9593cf1a49f8d9aca8cdd2e7add95a4ba192041'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
P389=K/'P16.7-continuation389-canonical-generated-energy-and-finite-dual-integrability-working-paper-20261009.tex'
B389=K/'P16.7-continuation389-ROOT-whole-proof-source-scope-and-binding-20261009.json'
B390=K/'P16.7-round273-whole-candidate390-ROOT-proof-source-scope-and-binding-20261009.json'; b390=load(B390)
assert sha(P389)=='735e4c6cd92a4a70bc551d74863704463a16cedd2486b54b8a31abbd5ff328b0'
assert sha(B389)=='afb7e156e78ddd5b0f679b738361473e6c2cb8564a7161e2873fa44941b20a97'
assert sha(B390)=='03d216d2f59ba1df77af2560051a5d2cd95ff4cd602bc85721fa9bb8c76dd0e5'
for e in b390['public_files']:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
C=R/'campaigns/round-275/P16.7-whole390388389-general-E1-operator'; f=load(C/'freeze.json')
assert not (C/'work.sqlite').exists() and f['input_sha256']=='36d6d13f18dcf92d18faa9e8cc1c371acb80841cdd45ee661d7dab4e51ca6141'
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    for e in load(C/name):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name); assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==278
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
states={}
for n,dirname in [(273,'P16.7-whole385387-full-bounded-dual-and-intrinsic-E1'),(274,'P12.3-whole386-Jensen-completion-and-original-residual')]:
    c=R/'campaigns'/('round-%d'%n)/dirname
    states[n]=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert states[n]['status']=='completed' and states[n]['error'] is None and states[n]['calls']['unsettled']==0
F.mkdir()
def freeze(p):
    p=Path(p); rel=p.relative_to(R)
    assert p.is_file() and 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel) and 'immutable-book-context' not in str(rel)
    assert p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    dst=F/'frozen-files'/rel; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,dst); assert sha(dst)==sha(p)
paths=[P389,B389,B390,K/'P12.3-G331-existing-completion-and-envelope-transfer-ROOT-scope-correction-20261009.json',R/'bind_ROOT389_generated_energy_and_full_dual_integrability_20261009.py',R/'record_G331_existing_completion_and_envelope_transfer_ROOT_20261009.py',R/'capture_completed_native273_actual_FINAL_20261009.py',R/'read_completed_native273_whole_fields_20261009.py',R/'audit_native273_whole_proof_and_literal_TeX_identity_20261009.py',R/'stage_completed_native273_whole390_ROOT_20261009.py',R/'capture_completed_native274_actual_FINAL_20261009.py',R/'prepare_native275_whole390388389_general_E1_20261009.py',R/'record_verified_checkpoint278_20261009.py',G/'push-receipt-continuation278.json',G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py',Path(__file__)]
paths += [Path(e['path']) for e in b390['public_files']]
paths += [p for p in sorted(C.rglob('*')) if p.is_file()]
assert len(paths)==len(set(map(str,paths)))
for p in paths:freeze(p)
for n,s in states.items():write(F/('native%d-public-status.json'%n),s)
now=datetime.now(timezone.utc).isoformat()
write(F/'publication-qualification.json',dict(recorded_utc=now,status='Whole ROOT389 and native273 whole390 UNREVIEWED, native275 frozen UNLAUNCHED; no original closure or acceptance',counts=dict(solved=16,open=26,accepted_scoped_papers=97),paper389_sha256=sha(P389),binding389_sha256=sha(B389),binding390_sha256=sha(B390),native273_current_version_evidence_correction=b390['qualified_whole_reading']['native_version_evidence_correction'],bounded_class_definition_boundary=b390['qualified_whole_reading']['class_definition_boundary'],native274_exact_FINAL_captured_whole_review_pending=True,completion_scope_correction='G331 already proves completion boundary/C/D; envelope/Jensen transport is a corollary, not a new completion theorem or general CE proof.',frozen275=f,all_full_primary_bodies_literal_units_pixels_and_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,no_ACTIVE_math_read_or_feedback=True,compilation_UNVERIFIED=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint279: canonical generated energy and full bounded dual drafts\n\nWhole ROOT389 proves canonical energy independent of bounded continuous decreasing presentations and integrability/L1 convergence against every finite FULL bounded-dual measure, under its explicit unreviewed bounded foundation388. It does not construct an all-direction unbounded analytic operator. Whole native273 draft390 supplies actual continuous/discrete radial nonpluripolar equations and exact full dual1/6+2Z/3 for its DECLARED locally smooth-approximable bounded class. ROOT records the distinct smallest continuous-psh-sheaf definition in388, and corrects native version evidence concerning incoming387 rather than current390. All proofs and exact residuals are included UNREVIEWED.\n\nG331 completion invariance was already accepted; the new scope record gives envelope/Jensen transfer as a corollary and preserves general CE as OPEN. Native274 completed; its settled FINAL is captured but whole review is pending. Native275 is frozen and UNLAUNCHED pending this verified NONFORCE checkpoint, with whole390388389 and fresh Ducros source evidence for a general E1 operator advance.\n\n16/42 original problems solved,26 OPEN,97 accepted scoped papers unchanged. No full primary bodies, literal units, pixels or whole book context published. No supplied/native program executed, protected editor OPEN UNCHANGED. Compiler requests unverified. Independent native Git tree, all remote blob bindings and branch are verified for the nonforce push.\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); x.update(updated_utc=now,current_active_batch=[],github_pending_checkpoint=dict(continuation=279,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),native275_frozen=dict(directory=str(C),input_sha256=f['input_sha256'],status='FROZEN UNLAUNCHED; verify279 beforelaunch'),next_work='Verify279 then launch frozen native275 generalE1 operator, at mostTWO. Whole native274 proof review then prepare nextP12.3 residual campaign. Entire389390 UNREVIEWED; no originalclosure/acceptance/countincrease; protected editor unchanged.'); write(p,x); shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv'); files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation279/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/name; files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+name,bytes=p.stat().st_size,sha256=sha(p)))
assert len({e['path'] for e in files})==len(files)
x=load(R/'active-work.json')
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint canonical generated energy, full bounded dual drafts and frozen general E1 audit',scope='Entire389390 UNREVIEWED and frozen275; exact class/source/version/completion boundaries; no closure/acceptance/fullprimary/book publication/editorchange.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),native275_frozen_unlaunched=True,solved=16,open=26,papers=97),indent=2))
