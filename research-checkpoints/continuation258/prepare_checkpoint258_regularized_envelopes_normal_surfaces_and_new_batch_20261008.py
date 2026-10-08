from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation258.json';F=G/'continuation258-publication-records';S=K/'small-batch256-257-public-status-20261008-continuation258'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not M.exists() and not F.exists() and not S.exists()
prior=json.loads((G/'push-receipt-continuation257.json').read_text());assert prior['commit_sha']=='61b44c17f10a3d9fd2af00cd9775d6b0b0f661c0' and not prior['force_update'] and all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
Ds=[K/'public-P12.3-continuation357-decreasing-completion-finite-cover-and-normal-limit-diagnostics-unreviewed',K/'public-P12.6-continuation358-independent-geometric-projection-full-conductor-trace-and-raw-envelopes-unreviewed']
for D in Ds:assert json.loads((D/'native-notes.json').read_text())['candidate'] is False
campaigns={q:next((R/f'campaigns/round-{q}').iterdir()) for q in [256,257]}
for C in campaigns.values():
 f=json.loads((C/'freeze.json').read_text())
 for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
 for name in ['mathematical-packet-bindings.json','private-primary-packet-bindings.json','book-context-bindings.json']:
  for e in json.loads((C/name).read_text()):assert Path(e['path']).stat().st_size==e['bytes'] and sha(e['path'])==e['sha256']
F.mkdir();S.mkdir();now=datetime.now(timezone.utc).isoformat();items=[]
for q,C in campaigns.items():
 st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout);assert not st['error'] and st['status'] in ['running','completed']
 p=S/f'round{q}-public-native-status.json';write(p,st);items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt'],public_status=str(p)))
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
write(F/'surface-primary-acquisition-metadata-LOCAL-body-excluded.json',json.loads((R/'primary-data-LOCALONLY/P12.3-normal-surface-geometric-envelopes-20261008/acquisition-records.json').read_text()))
write(F/'compiler-observation.json',dict(recorded_utc=now,P12_5_previous_builtin_cell1010='Wait identifier unavailable after resume; no stored result, compilation UNVERIFIED and not asserted still running',P12_6_new_builtin_cell33='Submitted existing staged358 source for built-in compilation; no result at checkpoint freeze, UNVERIFIED',success_or_PDF_claim=False,extra_editor_tabs=False,protected_editor_open_unchanged=True))
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert len(x['fully_solved_original_atoms'])==15 and x['remaining_open_original_atoms']==27 and x['historical_reviewed_scoped_papers']==96 and x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==257
 x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=258,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Continue native256 whole P12.6 specified regularized-envelope and native257 P12.3 excellent normalSURFACE plus residual>=3; do not inspect ACTIVE math/hotfeedback. Verify258 Git exacttree/allblobs/ref.15solved27OPEN96papers; compiler33unverified; protectededitorOPENUNCHANGED.');write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('''Checkpoint 258: regularized geometric envelopes, normal surface construction, and a new two-task batch

15/42 original problems solved, 27 OPEN, 96 accepted papers. No new acceptance. Completed native254 and255 actual FINAL candidate=false remains immutable. ROOT read both ENTIRE new mathematical arguments, all actual FINAL fields, source/scope/coverage/decisions, and all expanded fields outside exact matched whole proof bodies. Entire255 reader bridge/header was read after removing exact already-read proof and full grant duplicates; no fresh whole duplicated-grant or primary-source reading is claimed. Complete staged357/358 manuscripts are UNREVIEWED. Current bound inputs 68/74 matched and native255 output hash bindings matched; diagnostics and bytes are reproducibility, not proof. No supplied program was run.

New353 proves a finite-good-cover normal envelope sector at precisely qualified smooth BFJ source hypotheses. New355 proposes ALL excellent NORMAL LOCAL SURFACES over arbitrary fields/characteristics, including mixed characteristic: resolve finite actual primary models, prove negative-definite connected exceptional intersection matrix explicitly from the reference vector, prove the used regular model IS an actual primary blowup, then push nef potentials to a finite matrix projection dominating EVERY C/D competitor on ALL supports. Coordinate-max-stable compact polytope gives full model-determined obstacle envelopes; dense whole-section profiles give continuous envelopes and a single decreasing C-net gives extended USC ones. Entire proof and full immediate official surface source metadata are retained. This is UNREVIEWED and not a higher-dimensional theorem or catalogue closure.

New354 gives an actual graded primary-family non-USC pointwise limit despite vanishing energy, capacity and raw product mass. Before freezing the new review, ROOT corrected its signed-pairing convention: accepted E350 uses F=integral(-u)dmu, E=-F/2; hence E(u_j)=-1/(2j) increases to zero and the Cauchy-Schwarz form is F. Entire old bytes and exact mandatory repair are retained. All monomial counts, topology, measures and capacity conclusions are unchanged. Old binding is historical, not current proof bytes.

New356 selects the WHOLE-section USC-regularized geometric envelope E=(sup D minorants)^*. Compact quotient regularization equals the whole-fibre maximum; OPEN maps commute pointwise. Full-support continuous norm/determinant kernels imply openness, giving normal/no-vertical and reduced finite-flat regularized transfer and positive-domain equivalence. Arbitrary injections have the exact constrained full-conductor quotient rule with BOTH positivity and whole-fibre constancy. Entire all-field node calculation shows the regularized downstairs operator can fail geometric positivity although normalized source envelope is positive; at one source lift naive pulled-envelope inequality reverses by ONE. A normal-target vertical injection and a noninjective closed-image example have positive continuous envelopes at BOTH ends and fail unrestricted equality by ONE. All supports and vertical/lower-centre points are kept. New356 is UNREVIEWED; its combined cone/product chain358 must be independently reconstructed.

Two current native Codex gpt-6.1-sol xhigh calls only:256 independently reconstructs ENTIRE P12.6 358+356 and judges exact-original scope;257 independently audits ENTIRE P12.3 357+355/353/corrected354 and attempts the remaining arbitrary normal dimension>=3 problem. Frozen original task objects are byte-identical to completed255/254. Only full qualified G331/G345 or G331/B341/E350 grants; all new proof/verdict/source prose is mathematical DATA. Complete frozen mathematics published; primary literature/book bodies and pixels stay LOCALONLY. No other ACTIVE math read or feedback, no extra agents or account/runtime changes.

Protected P16.4 editor remains OPEN UNCHANGED, no extra tab. Compilation is UNVERIFIED; no PDF success claim. Same explicitly authorized GitHub repository/branch, nonforce compare-and-update, independently built exact Git tree and all remote blob/ref verification required before reporting push success.
''')
files=[];seen=set()
def add(p,target=None):
 p=Path(p);rel=p.relative_to(R);assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html'] and not any(x in rel.parts for x in ['source-pages','source-images','primary-data-LOCALONLY'])
 target=target or 'research-checkpoints/continuation258/'+str(rel)
 if target in seen:return
 seen.add(target);files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S]+Ds:
 for p in sorted(folder.rglob('*')):
  if p.is_file():add(p)
for C in campaigns.values():
 for name in ['task.json','original-task.json','input.json','settings.json','freeze.json','launch-record.json','mathematical-packet-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json','book-context-bindings.json']:add(C/name)
 for e in json.loads((C/'mathematical-packet-bindings.json').read_text()):add(e['path'])
for pattern in ['P12.3-continuation353-*','P12.3-P12.5-continuation354-*','historical-ROOT354-before-energy-sign-correction-20261008.md','P12.3-continuation355-*','P12.6-continuation356-*','P12.3-round254-whole-candidate357-*','P12.6-round255-whole-candidate358-*','round254-actual-native-final.json','round255-actual-native-final.json']:
 for p in K.glob(pattern):
  if p.is_file():add(p)
for name in ['record_whole_normal_finite_cover353_20261008.py','record_whole_graded_energy_counterexample354_and_completed254255_20261008.py','record_whole_normal_surface355_20261008.py','acquire_primary_surface_envelope_packet_20261008.py','capture_completed_native254255_20261008.py','correct_ROOT354_energy_convention_before_independent_review_20261008.py','stage_whole_completed254255_and_bind_regularized356_20261008.py','prepare_native256257_whole_regularized_transfer_and_normal_surfaces_20261008.py','launch_frozen_native256257_whole_original_batch_20261008.py','record_verified257_20261008.py']:add(R/name)
add(G/'push-receipt-continuation257.json');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
x=json.loads((R/'active-work.json').read_text());write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=27,historical_reviewed_scoped_papers=96,commit_message='Record regularized geometric envelopes and normal surface construction; independent whole-original batch',scope='15 solved,27 OPEN,96 papers. Full unreviewed353-358, mandatory354 sign repair, completed254255 and whole frozen256257. All literature/book source bodies and pixels LOCALONLY, no new acceptance.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,solved=15,open=27,papers=96),indent=2))
