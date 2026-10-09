from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation283-publication-records';M=G/'upload-manifest-continuation283.json'
B=K/'P16.7-continuation394-ROOT-whole-proof-source-scope-and-binding-20261009.json'
C276=R/'campaigns/round-276/P12.3-whole391392-formal-BIG-diagonal-and-original-residual'
C277=R/'campaigns/round-277/P16.7-whole393-intrinsic-compactness-and-equation'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def status(c):return json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation282.json')
assert prior['commit_sha']=='8fdefde6823413db47641042e3f7ce87c7f24dc8'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(B)=='25d1004b0ce1bc6139fa6b87245f29b071ba765acdd88d04b1c186208f91f54e'
b=load(B);P=Path(b['paper']['path'])
assert sha(P)==b['paper']['sha256']=='01a17c939bf2cd2b12096f4ed1e6a91b452954372c17c61f35992dbbce6665b6'
assert P.stat().st_size==b['paper']['bytes']==11692 and not b['accepted'] and not b['original_closed']
for e in b['whole_primary_units']:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
launch=load(C277/'launch-record.json');assert launch['frozen_input_sha256']=='dd50b01adf7dbd181765b9128d6f16e04545df85b96fc291bdb689ef125f83b7'
statuses={str(n):status(c) for n,c in [(276,C276),(277,C277)]}
assert all(x['calls']['admitted']==1 for x in statuses.values())
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name);assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==282
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
F.mkdir()
paths=[P,B,R/'bind_ROOT394_curve_restrictions_and_Wanner_scope_20261009.py',C277/'launch-record.json',R/'launch_frozen_native277_whole393_checked_20261009.py',G/'push-receipt-continuation282.json',R/'record_verified_checkpoint282_20261009.py',Path(__file__)]
assert len(paths)==len(set(map(str,paths)))
for p in paths:
    rel=p.relative_to(R);assert p.is_file() and 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    assert p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst);assert sha(dst)==sha(p)
write(F/'native276277-public-status.json',statuses);now=datetime.now(timezone.utc).isoformat()
write(F/'publication-qualification.json',dict(recorded_utc=now,status='Entire ROOT394 curve-test working paper UNREVIEWED; native277 launch retained; no acceptance or original closure',paper=b['paper'],binding_sha256=sha(B),direct_scope=b['direct_scope'],named_source_foundations=b['named_source_foundations'],unproved=b['unproved'],source_reading_boundary=b['source_reading_boundary'],all_full_primary_bodies_literal_units_pixels_and_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,no_ACTIVE_math_read_or_hot_feedback=True,ROOT394_created_after_native277_freeze_and_NOT_sent_to_active_campaign=True,compiler_UNVERIFIED=True,protected_editor_OPEN_UNCHANGED=True,counts=dict(solved=16,open=26,accepted_scoped_papers=97)))
(F/'README.md').write_text('Checkpoint283: whole curve-restriction working paper ROOT394 and native277 launch\n\nThe entire new paper and qualified proof/source binding are retained. It proves a proposed recognition direction for the full minimal continuous-psh sheaf and decreasing generated weights under the exact algebraic curve tests over algebraically closed complete nontrivially valued extensions. Uniform and decreasing limits preserve harmonic comparison; strictly affinoid curve boundary maximum follows. This is UNREVIEWED, with exact ordinary smooth pullback and Wanner source foundations. No converse recognition, surface compactness, higher-dimensional Shilov principle, arbitrary-measure equation or uniqueness is claimed.\n\nThe complete applied Wanner statement/immediate-proof units were physically read from the retained full text. Whole primary bodies, literal units, pixels and whole book contexts remain LOCALONLY. Recursive semistable/model/Thuillier proof trees and actual Wanner PDF pixels are not claimed newly read.\n\nNative276 and277 use the existing signed-in Xean Codex gpt-6.1-sol xhigh path. ROOT394 was created after277 freeze and has not been sent into either active campaign. No active mathematics read, hot feedback or third campaign. Native programs remain inert DATA.\n\n16 solved,26 OPEN,97 accepted scoped papers unchanged. Compilation diagnostics unverified. Protected P16.4 editor remains OPEN UNCHANGED. Authorized NONFORCE publication verifies native Git tree, all remote blobs and branch ref.\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=283,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify283 wholeROOT394 and native277 launch. Continue actual surface compactness and equation uniqueness, independent276 formalBIG and277 intrinsic equation gates; no acceptance/closure/countchange.');write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv');files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation283/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/name;files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+name,bytes=p.stat().st_size,sha256=sha(p)))
assert len({e['path'] for e in files})==len(files)
x=load(R/'active-work.json');write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint whole curve-restriction draft and independent analytic equation launch',scope='Entire ROOT394 UNREVIEWED plus qualified source metadata and277 launch; no original closure/acceptance/full primary or book publication/editor change.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),native_status={n:x['status'] for n,x in statuses.items()},solved=16,open=26,papers=97),indent=2))
