from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation281-publication-records'; M=G/'upload-manifest-continuation281.json'
C=R/'campaigns/round-276/P12.3-whole391392-formal-BIG-diagonal-and-original-residual'
B=K/'P12.3-continuation392-ROOT-whole-proof-source-scope-and-binding-20261009.json'
P=K/'P12.3-continuation392-Noether-different-and-completed-Cartier-products-working-paper-20261009.tex'
Q=K/'P12.3-Wang1994-formal-normalization-ROOT-primary-pixel-reading-scope-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists() and not (C/'work.sqlite').exists()
prior=load(G/'push-receipt-continuation280.json'); assert prior['commit_sha']=='09ff974b780030295a4642131d6095cfcc39d73e'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(B)=='33b851cc423d8024e2d2e45259f0ffbaebdf17935950c7b88d117b7b22750bdb' and sha(P)=='d39862c9a6c128d93f02a0843aaa15593252affc159ebafcda8b51e1cb6fcd5a'
assert sha(Q)=='6263fec57890d8d26aa031de9002bb58fee1a159710bb26886056ad5a5217d2d'
f=load(C/'freeze.json'); assert f['input_sha256']=='05af7054d111391f5347d1201ae85ba734edfcb4ce0f24d3eb77238267745bc5'
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:
    assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    for e in load(C/name):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(R/'campaigns/round-275/P16.7-whole390388389-general-E1-operator/work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert st['status']=='blocked' and st['calls']['admitted']==st['calls']['settled']==1 and st['calls']['unsettled']==0
assert st['error'].startswith('Unknown, dead, or forward support:')
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name); assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==280
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
F.mkdir()
def freeze(p):
    p=Path(p); rel=p.relative_to(R)
    assert p.is_file() and 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    assert p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    dst=F/'frozen-files'/rel; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,dst); assert sha(dst)==sha(p)
paths=[P,B,Q,R/'bind_ROOT392_Noether_different_and_completed_Cartier_products_20261009.py',R/'record_ROOT392_Wang_pixel_scope_and_rebind_20261009.py',R/'prepare_native276_whole391392_formal_BIG_diagonal_20261009.py',R/'record_verified_checkpoint280_20261009.py',G/'push-receipt-continuation280.json',Path(__file__)]+[C/n for n in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json','freeze.json']]
paths += [R/'capture_terminal_native275_support_rejection_20261009.py',K/'P16.7-native275-terminal-support-rejection-and-data-retention-20261009.json']
assert len(paths)==len(set(map(str,paths)))
for p in paths:freeze(p)
write(F/'native275-public-status.json',st); now=datetime.now(timezone.utc).isoformat()
write(F/'publication-qualification.json',dict(recorded_utc=now,status='Whole amended ROOT392 and frozen native276 UNREVIEWED; no original closure/acceptance',counts=dict(solved=16,open=26,accepted_scoped_papers=97),paper392_sha256=sha(P),binding392_sha256=sha(B),Wang_pixel_scope_record_sha256=sha(Q),native276=f,whole_math_policy='Native276 full312-file mathematical copies retained locally and wholly SHA-bound here. Old full mathematical material already retained in preceding checkpoints; new entireROOT392 is included. Do not redundantly republish private source/wholebook bodies.',new_scope='Every Noetherdifferent gives uniform root containment and full compatible completed-diagonal maps; fixed-coefficient-field sum matches actual Wang4.3; completed Hom factorization; BIGproduct inclusion expressly conditional.',remaining='Actual BIG framework/restriction/subadditivity and entire formal CE; original generalP12.3 and all-directionE1 stillOPEN',all_full_primary_bodies_literal_units_pixels_and_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,no_ACTIVE_math_read_or_hot_feedback=True,compiler_UNVERIFIED=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint281: entire ROOT392 formal Noether-different draft and frozen native276\n\nThe complete amended22408-byte paper gives direct q-independent Noether-different root containment, full compatible completed-diagonal lifting, and finite-module completed Hom factorization. Its primary corollary retains exact named published formal Jacobian foundations; the normalization sum now exactly matches Wang fixed-coefficient-field Definition4.1/Lemma4.3. Actual official pixels597--602 were read for the recorded units. Full scannedPDF/OCR/pixels and other full primary bodies remainLOCALONLY; retention is not whole-paper reading. The BIG product proposition is explicitly conditional. No actual BIG restriction/subadditivity or full original closure is claimed.\n\nFrozen native276 will independently inspect whole391392 and pursue actual formal BIG restriction/subadditivity and isolated formal envelope continuity, with only entire qualifiedG331/B341/E350 grants. All312 full mathematical input files are retained locally and wholly bound by metadata; prior whole mathematical versions are retained in preceding checkpoints, while the new wholeROOT392 is included here. The three whole book contexts and1231 private primary/evidence items remainLOCALONLY. Native275 generalE1 remains independent; at mostTWO native campaigns, existing signed-in gpt-6.1-sol xhigh.\n\n16/42 original problems solved,26 OPEN,97 accepted scoped papers unchanged. Drafts unreviewed and compiler diagnostics pending. Protected P16.4 editor OPEN UNCHANGED. NONFORCE publication verifies nativeGit tree, remote blobs and branch.\n')
with (F/'README.md').open('a') as out:out.write('\nNative275 terminal correction: one call settled, but Xean BLOCKED its result for unknown support identifiers referencing ungranted whole390/source prose. Raw FINAL retained as DATA, not imported or accepted; math not yet ROOT read, no original closure and no automatic retry. Frozen276 predates terminal mathematics and receives no hot feedback.\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=281,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),native276_formal_BIG_frozen=f,next_work='Verify281 wholeROOT392/Wang reading qualification/frozen276 beforelaunch. Then native276 actual formalBIG diagonal; independently whole-read terminal275 rejected raw DATA and paper. At mostTWO; no automatic275 retry/counts/acceptance/editorchange.');write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv'); files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation281/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/name; files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+name,bytes=p.stat().st_size,sha256=sha(p)))
assert len({e['path'] for e in files})==len(files)
x=load(R/'active-work.json');write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint formal Noether-different draft and frozen completed-diagonal research',scope='WholeROOT392 UNREVIEWED, exactWang source scope and frozennative276; no closure/acceptance/fullprimary/book publication/editorchange.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),native275_status=st['status'],solved=16,open=26,papers=97),indent=2))
