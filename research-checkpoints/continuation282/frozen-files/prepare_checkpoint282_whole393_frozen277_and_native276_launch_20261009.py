from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation282-publication-records';M=G/'upload-manifest-continuation282.json'
C=R/'campaigns/round-277/P16.7-whole393-intrinsic-compactness-and-equation'
C276=R/'campaigns/round-276/P12.3-whole391392-formal-BIG-diagonal-and-original-residual'
B=K/'P16.7-round275-whole-draft393-ROOT-proof-source-scope-and-binding-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists() and not (C/'work.sqlite').exists()
prior=load(G/'push-receipt-continuation281.json');assert prior['commit_sha']=='cabfc4424dc1902e79ac61b3993409e5fd818a58'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(B)=='c67890a5c79291cb33da77aa2ef749282753877fff02a89568957bb2c4b12d74';b=load(B)
for e in b['public_files']:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
f=load(C/'freeze.json');assert f['input_sha256']=='dd50b01adf7dbd181765b9128d6f16e04545df85b96fc291bdb689ef125f83b7'
for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
    for e in load(C/name):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
launch=load(C276/'launch-record.json');assert launch['frozen_input_sha256']=='05af7054d111391f5347d1201ae85ba734edfcb4ce0f24d3eb77238267745bc5'
st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C276/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert st['status'] in ['running','completed'] and not st['error'] and st['calls']['admitted']==1
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name);assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==281 and x['current_active_batch']==[276]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
F.mkdir()
def freeze(p):
    p=Path(p);rel=p.relative_to(R);assert p.is_file() and 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    assert p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst);assert sha(dst)==sha(p)
paths=[B,C276/'launch-record.json',R/'record_verified_checkpoint281_20261009.py',R/'launch_frozen_native276_whole391392_checked_20261009.py',R/'prepare_native277_whole393_intrinsic_equation_gates_20261009.py',G/'push-receipt-continuation281.json',Path(__file__)]+[Path(e['path']) for e in b['public_files']]+[C/n for n in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','freeze.json']]
assert len(paths)==len(set(map(str,paths)))
for p in paths:freeze(p)
write(F/'native276-public-status.json',st);now=datetime.now(timezone.utc).isoformat()
write(F/'publication-qualification.json',dict(recorded_utc=now,status='Whole393 support-rejected DATA UNREVIEWED, frozen277 and onecall276 launch; no original closure/acceptance',whole393_scope=b['whole_reading_and_scope'],binding393_sha256=sha(B),native277=f,wholemath='All257 complete native277 mathematical copies retained locally and fully SHA-bound; preceding full lineage + newwhole393 public. Never publish fullprivate primary/book bodies.',all_full_primary_bodies_literal_units_pixels_and_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,no_ACTIVE_math_read_or_hot_feedback=True,compiler_UNVERIFIED=True,protected_editor_OPEN_UNCHANGED=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97)))
(F/'README.md').write_text('Checkpoint282: whole generated operator draft393, corrected primary-unit evidence, frozen native277\n\nEntire native275 raw FINAL remains Xean support-rejected DATA. Whole five mathematical notes,46943-byte companion,48600-byte standalone TeX and4964-byte ledger are published with whole-content/scope/source corrections; no note import, acceptance or correctness grant. The claimed all-direction GENERATED analytic operator, mixed products, first variation/comparison/locality/clamps require independent verification. Intrinsic compactness/envelopes/arbitrary-measure existence/full uniqueness remain OPEN.\n\nThe old ROOT388 extractor counted PDF FF separators through splitlines and produced source bodies inconsistent with literal-LF descriptors. Own correction identifies the cause; five correct full actual source ranges have now been physically read and retained LOCALONLY. No full source reproduction, pixels or book bodies are uploaded.\n\nNative276 runs one existing signed-in gpt-6.1-sol xhigh call for actual formal BIGdiagonal/subadditivity/envelopes. Frozen277 independently reviews whole393 and pursues full intrinsic equation gates with STRICT valid earlier-own-note support identifiers and zero imported grants. All257 whole mathematical files are locally frozen with full binding metadata; preceding lineage and new whole393 are publicly retained. At most TWO campaigns; no hot feedback or active mathematics read.\n\n16solved26OPEN97accepted unchanged. Compiler diagnostics unverified; protected P16.4 editor OPEN UNCHANGED. NONFORCE publication verifies exact native Git tree, remote file blobs and branch.\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=282,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),native277_intrinsic_equation_frozen=f,next_work='Verify282 whole393/sourcecorrection/frozen277/276launch before starting277. Then TWO independent calls formalBIG and intrinsicE1 equation. ROOT prove remaining genuine gates, no acceptance/closure/countchange.');write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv');files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation282/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/name;files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+name,bytes=p.stat().st_size,sha256=sha(p)))
assert len({e['path'] for e in files})==len(files)
x=load(R/'active-work.json');write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint whole generated analytic operator draft and independent equation research',scope='Entire393 support-rejected DATA UNREVIEWED/source correction/frozen277/native276launch; no closure/acceptance/fullprimary/book publication/editorchange.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),native276_status=st['status'],solved=16,open=26,papers=97),indent=2))
