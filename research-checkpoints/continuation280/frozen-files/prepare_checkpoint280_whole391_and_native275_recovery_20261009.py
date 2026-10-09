from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation280-publication-records'; M=G/'upload-manifest-continuation280.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation279.json'); assert prior['commit_sha']=='d638f663706a2d640cdf9e2ce8f32ce20a2ab127'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
B=K/'P12.3-round274-whole-candidate391-ROOT-proof-source-scope-and-binding-20261009.json'; b=load(B)
assert sha(B)=='750c08fd2ef169a0ec5baa73937ec0a3bd5797b73eb5155780396c90c99e629b'
for e in b['public_files']:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
C=R/'campaigns/round-275/P16.7-whole390388389-general-E1-operator'
f=load(C/'freeze.json'); launch=load(C/'launch-record.json')
assert f['input_sha256']==launch['frozen_input_sha256']=='36d6d13f18dcf92d18faa9e8cc1c371acb80841cdd45ee661d7dab4e51ca6141'
st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert st['status'] in ['running','completed'] and not st['error'] and st['calls']['admitted']==1
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name); assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==279
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
F.mkdir()
def freeze(p):
    p=Path(p); rel=p.relative_to(R)
    assert p.is_file() and 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    assert p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    dst=F/'frozen-files'/rel; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,dst); assert sha(dst)==sha(p)
paths=[B,C/'launch-record.json',R/'capture_completed_native274_actual_FINAL_20261009.py',R/'read_completed_native274_whole_fields_20261009.py',R/'audit_native274_whole_proof_and_literal_TeX_identity_20261009.py',R/'stage_completed_native274_whole391_ROOT_20261009.py',R/'launch_frozen_native275_whole390388389_checked_20261009.py',R/'resume_initialized_native275_socket_permission_20261009.py',R/'record_verified_checkpoint279_20261009.py',R/'fetch_formal_Noether_different_primary_20261009.py',R/'fetch_formal_Jacobian_normalization_dependencies_20261009.py',R/'ocr_Wang1994_official_primary_20261009.py',G/'push-receipt-continuation279.json',G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py',Path(__file__)]+[Path(e['path']) for e in b['public_files']]
assert len(paths)==len(set(map(str,paths)))
for p in paths:freeze(p)
write(F/'native275-public-status.json',st); now=datetime.now(timezone.utc).isoformat()
write(F/'publication-qualification.json',dict(recorded_utc=now,status='Whole native274391 UNREVIEWED; native275 one call resumed after socketEPERM before any admission; no original closure/acceptance',counts=dict(solved=16,open=26,accepted_scoped_papers=97),binding391_sha256=sha(B),whole391_scope=b['qualified_whole_reading']['scope'],completion_novelty_correction=b['qualified_whole_reading']['completion_novelty_correction'],formal_remaining=b['qualified_whole_reading']['formal_remaining'],native275_recovery=launch['recovery'],sources='Fresh formal Noetherdifferent published/author primary PDFs retained LOCALONLY; OCR and retention do not imply whole-reading/correctness. New own proof pending.',all_full_primary_bodies_literal_units_pixels_and_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,no_ACTIVE_math_read_or_hot_feedback=True,compiler_UNVERIFIED=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint280: whole391 Jensen and formal Frobenius lifting draft\n\nEntire completed native274 actualFINAL, different expanded notes,43457-byte full proof,13801-byte ledger and686035-byte literal mathematical TeX are retained with ROOT whole-reading/encoding/scope qualifications. The formal trace-discriminant lift has actual generically separable normalization/perfect coefficient-field hypotheses. The missing compatible PRIMARY multiplier ideal and BIG completed-diagonal subadditivity remain explicit. Completion/C/D invariance was already inG331; its envelope/Jensen consequences are corollaries, not a new generalCE theorem. OriginalP12.3 OPEN; all judgments UNREVIEWED.\n\nNative275 now runs one admitted gpt-6.1-sol xhigh call through signed-in Xean. Initial sandbox socketEPERM occurred before admission; SAME initialized database resumed, with no duplicate model call, frozen input change or auth/proxy/CA change. It independently reviews390388389 and targets generalE1 operator convergence. Fresh formal Noetherdifferent primary source bodies/pixels remainLOCALONLY.\n\n16/42 original problems solved,26 OPEN,97 accepted scoped papers unchanged. Compiler requests unverified; protected editor OPEN UNCHANGED. NONFORCE publication independently verifies nativeGit tree, remote blobs and branch.\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=280,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify280 whole391+native275 launch/recovery. Native275 generalE1 remains independent. ROOT formal Noetherdifferent exact source proof and new392 primary multiplier then nextP12.3 native276, at mostTWO. No counts changed; protected editor unchanged.'); write(p,x); shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv'); files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation280/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/name; files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+name,bytes=p.stat().st_size,sha256=sha(p)))
assert len({e['path'] for e in files})==len(files)
x=load(R/'active-work.json'); write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint whole Jensen and formal Frobenius lifting draft with native general E1 launch',scope='Entire391 UNREVIEWED; completed-scope novelty correction, one-call275 socketrecovery; no closure/acceptance/fullprimary/book publication/editorchange.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),native275_status=st['status'],solved=16,open=26,papers=97),indent=2))
