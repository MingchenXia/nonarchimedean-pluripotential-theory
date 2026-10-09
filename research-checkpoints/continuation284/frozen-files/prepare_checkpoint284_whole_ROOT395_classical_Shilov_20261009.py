from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation284-publication-records';M=G/'upload-manifest-continuation284.json'
B=K/'P16.7-continuation395-ROOT-whole-proof-source-scope-and-binding-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def status(n):
    rel={276:'P12.3-whole391392-formal-BIG-diagonal-and-original-residual',277:'P16.7-whole393-intrinsic-compactness-and-equation'}[n]
    p=R/f'campaigns/round-{n}'/rel/'work.sqlite'
    return json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(p)],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation283.json');assert prior['commit_sha']=='1771c0c5bdd98de2bb4ffc03f381b3f3de94f3fa'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(B)=='d0c82c74bc90ff0f0d8fb588baa3b1ff05e520a58c0c1f1546f8451a6343e8af';b=load(B);P=Path(b['paper']['path'])
assert sha(P)==b['paper']['sha256']=='5d7a379a3ff80c241441d6f01c93193a142e6ba89ebc5b1a955e9ed0e10173b2' and P.stat().st_size==15547
assert not b['accepted'] and not b['original_closed']
Q=Path(b['retention_record']['path']);W=Path(b['source_reading_record']['path'])
assert sha(Q)==b['retention_record']['sha256'] and sha(W)==b['source_reading_record']['sha256']
q=load(Q)
for e in [q['full_pdf'],q['full_extract']]+q['actual_units']+q['rendered_original_pages']:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name);assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==283
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
statuses={str(n):status(n) for n in [276,277]};assert all(x['calls']['admitted']==1 for x in statuses.values())
F.mkdir()
paths=[P,B,Q,W,R/'retain_GR2506_v2_primary_units_for_ROOT395_20261009.py',R/'bind_ROOT395_classical_recognition_Shilov_20261009.py',G/'push-receipt-continuation283.json',R/'record_verified_checkpoint283_20261009.py',Path(__file__)]
assert len(paths)==len(set(map(str,paths)))
for p in paths:
    rel=p.relative_to(R);assert p.is_file() and 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    assert p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst);assert sha(dst)==sha(p)
now=datetime.now(timezone.utc).isoformat();write(F/'native276277-public-status.json',statuses)
write(F/'publication-qualification.json',dict(recorded_utc=now,status='Entire ROOT395 source-qualified classical recognition/Shilov reconstruction/upper control UNREVIEWED; no closure or acceptance',paper=b['paper'],binding_sha256=sha(B),direct_scope=b['direct_scope'],named_source_foundations=b['named_foundations'],unproved=b['unproved'],reading_scope=b['reading_scope'],all_full_primary_units_pixels_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,ROOT395_NOT_in_active276277_frozeninputs=True,no_ACTIVE_math_read_or_hot_feedback=True,compiler_UNVERIFIED=True,protected_editor_OPEN_UNCHANGED=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97)))
(F/'README.md').write_text('Checkpoint284: whole classical-psh and Shilov-control working paper ROOT395\n\nEntire15547-byte paper and exact qualified proof/source bindings are retained. The source-stated GRv2 smooth-psh bridge, all-curve/all-extension classical definition, decreasing/sheaf closure and local/affinoid maximum principles apply to the ALL-stage minimal continuous CLD sheaf and its decreasing generated weights. This source bridge and maximum principles are not claimed novel. Proposed applications prove arbitrarily small finite Shilov-boundary reconstruction, boundary-value order determination including poles, and eventual uniform UPPER control against a continuous candidate. No fixed skeleton or measure-support restriction is imposed.\n\nThe exact complete applied statement/immediate-proof units and actual original PDFpages3,33,34 were ROOT physically read. Printed proof6.4 says continuous for closedness of its maximum set; the stated USC hypothesis already suffices and own proofs useUSC. Full sources/literal units/pixels/book contexts remain LOCALONLY. No entire source or deep recursive proof-tree reading claim.\n\nAll results UNREVIEWED. Arbitrary boundary-value limits need not be realized by generated psh weights; no surface compactness, envelopes, orthogonality, lower-tail uniform integrability, arbitrary-measure equation existence or uniqueness is proved here. Native276 and277 remain independent; these new papers were not sent to active campaigns. No supplied/native code execution.\n\n16solved26OPEN97accepted unchanged; compile diagnostics unverified. Protected P16.4 editor OPEN UNCHANGED. NONFORCE Git publication verifies exact native tree, all remote file blobs and branch ref.\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=284,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify284 wholeROOT395/source qualification. Continue genuineformalBIG stable-ideal framework andsurfacecompactness/envelope/equation gates. Native276277 independent atmostTWO, nohotfeedback orclosure/countchange.');write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv');files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation284/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/name;files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+name,bytes=p.stat().st_size,sha256=sha(p)))
assert len({e['path'] for e in files})==len(files)
x=load(R/'active-work.json');write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint whole classical-psh Shilov reconstruction and upper-control draft',scope='Entire ROOT395 UNREVIEWED/source-qualified metadata; no original closure/acceptance/full primary or book publication/editor change.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),native_status={n:x['status'] for n,x in statuses.items()},solved=16,open=26,papers=97),indent=2))
