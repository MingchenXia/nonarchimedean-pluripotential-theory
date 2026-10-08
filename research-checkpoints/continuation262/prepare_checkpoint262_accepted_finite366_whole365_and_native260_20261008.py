from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation262-publication-records'; S=F/'frozen-status-only'; M=G/'upload-manifest-continuation262.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not M.exists()
if F.exists():
 assert sorted(str(p.relative_to(F)) for p in F.rglob('*') if p.is_file())==['frozen-status-only/round258-public-native-status.json','frozen-status-only/round259-public-native-status.json']
prior=load(G/'push-receipt-continuation261.json')
assert prior['commit_sha']=='7003bb48ca0a9b0794a6c329d03602695fd0cbe3'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
protected=K/'public-P16-round-46-final-reader/P16.4-paper.tex'
assert sha(protected)=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
D365=K/'public-P12.3-continuation365-normal-surfaces-isolated-normal-germs-and-full-normalization-whole-candidate'
D366=K/'public-P12.6-continuation366-whole-original-finite-map-compatibility-after-independent259'
accept=load(D366/'whole-original-paper-acceptance-after-independent259-ROOT-20261008.json')
assert accept['original_closed'] and accept['cumulative_accepted_paper_number']==97
for key in ['source','whole_proof','source_ledger','review_binding','mandatory_annotation','original_task']:
 e=accept[key];assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
for name in ['active-work.json','checklist-current.json']:
 x=load(R/name);assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26
 assert x['historical_reviewed_scoped_papers']==97 and x['github_pending_checkpoint'] is None
 assert x['latest_verified_github_checkpoint']['continuation']==261 and x['current_active_batch']==[261]
F.mkdir(exist_ok=True);S.mkdir(exist_ok=True);now=datetime.now(timezone.utc).isoformat();items=[];campaigns={}
for q in [258,259,261]:
 C=next((R/f'campaigns/round-{q}').iterdir());campaigns[q]=C;f=load(C/'freeze.json')
 for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:
  assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
 for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
  for e in load(C/name):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
 st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 assert not st['error'] and st['status'] in ['running','completed']
 if q in [258,259]:assert st['status']=='completed' and st['calls']['unsettled']==0
 p=S/f'round{q}-public-native-status.json';write(p,st)
 items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt'],public_status=str(p)))
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2 and set(active)<={261}
failure=load(K/'native260-preinitialization-usagePrefix-schema-failure-and-retry261-20261008.json')
assert failure['status']=='FAILED BEFORE CAMPAIGN INITIALIZATION' and not failure['provider_called']
write(F/'native260-preinitialization-failure-and-verified261-retry.json',failure)
write(F/'publication-qualification.json',dict(recorded_utc=now,formal_originals_solved=16,formal_originals_OPEN=26,accepted_papers=97,
 P12_6='Complete exact original accepted after independent259 and ROOT ENTIRE proof/source/scope/actual-paper reading; full366 is F366/paper97, no formal-proof or PDF success claim.',
 current259_actual='All10actual fields exactly equal expanded/local pair; bytes differ only JSON serialization. Historical256 actualtexts DIFFER from expanded, earlier qualification preserved.',
 P12_3='Whole365 native258 candidateFALSE, ALLchar normalSURFACEs and algclosedchar0isolated normal plus full normalization/extended/net calculations remain UNREVIEWED. Entire ROOT363364 exact correction-bound obstruction/general-normal finite-correctionOPEN continuity UNREVIEWED. Independently reconstructed together in immutable261 retry, generalnormal residual OPEN.',
 native260='FAILED BEFORE initialization: usagePrefix exceeded schema91-character maximum, no database/provider/math output. Full old frozen files/launch history preserved; 15/27/96 immutable historical metadata.',
 native261='Verified initialized short-prefix retry of whole same49math1073558bytes and FULLqualifiedG331/B341/E350,50primary3context, native gpt-6.1-sol xhigh, atmost2; no active output reading/hot feedback. Current count16/26/97.',
 compiler='New366 built-in submitted cell188; environment transition lost the handle: bounded wait returned exec cell188 not found. Older358/361/362 cells33/99/125 had no successful result at last observation. Compilation UNVERIFIED, no new editor tab or PDF export.',
 primary_bodies_pixels_LOCALONLY=True,source_documents_and_programs_DATA=True,supplied_programs_executed_or_imported=False,protected_editor_open_unchanged=True))
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=load(p);x.update(updated_utc=now,current_active_batch=active,
 current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),
 github_pending_checkpoint=dict(continuation=262,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),
 next_work='Verify262 entire accepted F366/P12.6 original and full unreviewed365/current immutable261 inputs; retain260 preinitialization failure. Continue native261 P12.3 and select next remaining original, atmost2 campaigns.16solved26OPEN97papers; compiler unverified; protected editor OPEN UNCHANGED.')
 write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('''Checkpoint262: complete original P12.6 accepted; normal envelope research continues

16/42 original problems solved,26OPEN,97 accepted papers. P12.6/F366 is accepted after independent native259 reconstructed the ENTIRE original proof/source/scope and ROOT read the whole manuscript, all10actualFINALfields, complete source/scope/coverage/decisions, exact immutable original and all fresh TeX bridges. The full standalone356105-bytepaper includes10 reconstructed proofs and14 unchanged ENTIRE qualified G331/G345 components. Actual geometric Cartier pullback/projection precedes ideal comparisons. Selected USC-envelope is explicitly specified on ALL bounded-above extended USC obstacles; exact positive domains and all finite-image/full-conductor rules are given, with necessary node/noninjective/vertical counterexamples. Products retain all reduced generic and closed-residue weights, supported thicknesses, ONE arbitrary source slot, full conductor admissibility, precise tower hypotheses and EXACTLY ONE gauge factor. Current SH quotient-annihilator repair and exact BFJ closed affine algclosedchar0 source scope are mandatory. Separate P12.3 general positive-envelope existence remains OPEN.

Native259 real actual FINAL and expanded notes match in ALL10fields; only JSON serialization differs. Historical256 real actual texts differed from expanded manuscript, and that earlier qualification remains preserved. No candidate/PASS label replaces ROOT mathematical review. No formal verification or successful compilation claim.

Full native258 candidate365 is published as UNREVIEWED, with whole normal-surface/all-characteristic and isolated-normal/algclosedchar0 results, extended/decreasing-net calculus and full-normalization criteria. Native260 failed BEFORE initialization because usagePrefix exceeded91characters; no provider called or mathematical output. Immutable old packet/launch/diagnostic preserved. Verified initialized short-prefix native261 retries the WHOLE same365 and ROOT363364 correction-bound/local continuity proofs; remaining generalnormal infinite-correction stratum and higher-dimensional positive/mixed-characteristic cases remain OPEN. ONLY full qualified grants are supplied, source bodies/pixels remain LOCALONLY, and active campaign mathematical output is not read or fed back. Atmost TWO Xean native Codex gpt-6.1-sol xhigh campaigns. Protected P16.4 editor stays OPEN UNCHANGED; no extra tabs/PDF export. Built-in compiler remains UNVERIFIED until an actual success result.

Regular user-authorized NONFORCE GitHub checkpoint: entire papers, actual outputs, source/scope qualifications, complete frozen260/261 mathematical inputs and independent tree/all-blob/fresh-ref verification.
''')
files=[];seen=set()
def add(p,target=None):
 p=Path(p);rel=p.relative_to(R)
 assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
 target=target or 'research-checkpoints/continuation262/'+str(rel)
 if target in seen:return
 seen.add(target);files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,D365,D366]:
 for p in sorted(folder.rglob('*')):
  if p.is_file():add(p)
for q in [260,261]:
 C=next((R/f'campaigns/round-{q}').iterdir())
 for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json','freeze.json','launch-record.json']:add(C/name)
 for e in load(C/'mathematical-packet-bindings.json'):add(e['path'])
add(K/'native260-preinitialization-usagePrefix-schema-failure-and-retry261-20261008.json')
for pattern in ['P12.3-round258-whole-candidate365-ROOT*.json','P12.6-round259-whole-original366-ROOT*.json']:
 for p in K.glob(pattern):add(p)
for name in ['capture_completed_native258_20261008.py','capture_completed_native259_20261008.py',
 'stage_whole_completed258_surface_isolated_normal365_20261008.py',
 'prepare_native260_entire365_and_general_normal_finite_correction364_review_20261008.py',
 'launch_frozen_native260_whole365_finite_correction_original_20261008.py',
 'stage_whole_independent259_finite_compatibility366_ROOT_20261008.py',
 'accept_whole_original_P12_6_after_independent259_ROOT_20261008.py',
 'record_verified_checkpoint261_20261008.py','retry_native260_as_short_prefix261_20261008.py']:add(R/name)
for p in [G/'push-receipt-continuation261.json',Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
x=load(R/'active-work.json')
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],
 files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,
 commit_message='Accept complete original P12.6 geometric finite-map compatibility and checkpoint full normal-envelope research',
 scope='16solved26OPEN97papers; whole accepted366 with independent259/ROOT qualifications, whole UNREVIEWED365 and immutable261 retry/full math with260 preinit failure. Source bodies/pixels LOCALONLY.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,solved=16,open=26,papers=97),indent=2))
