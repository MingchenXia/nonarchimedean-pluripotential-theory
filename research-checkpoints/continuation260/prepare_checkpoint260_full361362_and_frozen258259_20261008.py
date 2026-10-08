from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation260-publication-records';S=F/'frozen-status-only';M=G/'upload-manifest-continuation260.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=json.loads((G/'push-receipt-continuation259.json').read_text());assert prior['commit_sha']=='525c3eb34ee595983d5d67693f3d8de5ed7299c7' and all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
 x=json.loads((R/name).read_text());assert len(x['fully_solved_original_atoms'])==15 and x['remaining_open_original_atoms']==27 and x['historical_reviewed_scoped_papers']==96 and x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==259 and set(x['current_active_batch'])=={258,259}
F.mkdir();S.mkdir();now=datetime.now(timezone.utc).isoformat();items=[];campaigns={}
for q in [258,259]:
 C=next((R/f'campaigns/round-{q}').iterdir());campaigns[q]=C;f=json.loads((C/'freeze.json').read_text())
 for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json']:assert sha(C/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
 for name in ['mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json']:
  for e in json.loads((C/name).read_text()):assert Path(e['path']).stat().st_size==e['bytes'] and sha(e['path'])==e['sha256']
 st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 assert not st['error'] and st['status'] in ['running','completed']
 p=S/f'round{q}-public-native-status.json';write(p,st);items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt'],public_status=str(p)))
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
write(F/'publication-qualification.json',dict(recorded_utc=now,formal_originals_solved=15,formal_originals_OPEN=27,accepted_papers=96,new_acceptance=False,whole361='native257 candidateFALSE; entire normalSURFACE/allchar theorem and normalization/closed-BFJ/decreasing-net calculus independently reconstructed by ACTIVE258 alongside entire ROOT359/360; generalnormal residual remainsOPEN.',whole362='native256 candidateTRUE WHOLE P12.6 completion CLAIM, not accepted. Whole58,363-byte proof/all10actualFINALnotes/source/scope readbyROOT; ACTIVE259 independently reconstructs ENTIREproof/source/originalscope beforedecision.',mandatory_actual_expanded_distinction='The locally written native actual-FINAL artifact equals native-notes expanded TeX butDIFFERS fromtrue54839-bytecapturednativeFINAL. Every10actualtext differs andwasreadseparately. Publicactual-native256-final.json istrueFINAL; native-artifact-actual-FINAL-expanded-DATA.json isexplicitlyexpandedDATA.',P12_5_project_qualification='Native256 energyunresolved meansoutsideitsP12.6paper; PROJECTP12.5 alreadyacceptedE350/paper96. NoE350grantaddedtoP12.6review.',native257_duplicate_qualification='Native257 reading-duplicates.json checkssevenHISTORICAL254notes, notits11currentnotes; ROOTindependentfull11proofbindingsseparate.',primary_bodies_pixels_LOCALONLY=True,only_public_primary_metadata=True,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False,supplied_programs_executed=False,protected_editor_open_unchanged=True,compiler='Existing358cell33 andnew361cell99 submitted; no successful compiler result returned atlatest boundedobservation. UNVERIFIED. NoPDFexport/extra tab.'))
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=260,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Continue native258 P12.3 whole-surface/isolatednormal/fullnormalization and259 ENTIREoriginal P12.6 candidate362 independentreview; noACTIVEproofreading/hotfeedback. Verify260exactGit tree/allblobs/freshref;15solved27OPEN96papers untilwholeindependentacceptance. ProtectededitorOPENUNCHANGED.');write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('''Checkpoint260: full normal-surface manuscript and P12.6 original completion candidate

Formal count remains15/42 solved,27 OPEN,96 accepted papers. Full native257 paper361 (candidateFALSE) proves normal-surface geometric envelopes in all characteristics with actual primary-model/nef-matrix geometry, extended obstacles and full-conductor criteria; all-source/domain qualifications retained. Entire ROOT359 normalization formula and ROOT360 isolated algebraically closed characteristic-zero normal theorem are frozen into independent native258 reconstruction, with the general higher-dimensional normal residual still OPEN.

Full native256 paper362 (candidateTRUE) is a CLAIM to resolve entire original P12.6: geometric finite-map cone/selected USC-regularized-envelope/product compatibility, exact positive domains, full-fibre constrained regularization, sharp node/noninjective/vertical counterexamples, actual geometric-before-module product projection, conductor-admissible ONE-source-slot traces, determinant-flat compatibility, exact towers and ONE primary-gauge factor. ROOT has physically read the whole proof, every real actual FINAL note, source/scope/coverage/decision, and verified exact manuscript body bindings. Independent native259 audits the ENTIRE original proof/source/scope before any acceptance or count increase. Family6.2 keeps general positive-envelope existence P12.3 separate; no manuscript label is accepted as proof.

Important documentary correction: the native locally written actual-FINAL.json is expanded TeX, not the real captured Xean settled FINAL; every ten real note texts differs. Both complete texts are public under explicit distinct names and mandatory qualifications. P12.5 is already accepted projectwide as E350/paper96; native256's unresolved-energy phrasing is qualified as outside this P12.6 paper. Native257's seven-note duplicate report concerns historical254, not its current eleven notes; ROOT's current eleven bindings are separate.

At most two native Xean campaigns, both signed-in native Codex gpt-6.1-sol xhigh, immutable complete mathematical packets, only full qualified grants. ACTIVE campaign proof output is not read or fed back. Primary source bodies/pixels remain LOCALONLY with public metadata bindings; source documents and supplied programs are mathematical/inert DATA. Protected P16.4 editor remains OPEN UNCHANGED; no new tabs or PDF exports. Compilation remains UNVERIFIED until built-in compiler actually succeeds.

Regular explicitly authorized nonforce GitHub checkpoint; fresh cache-qualified ref/tree reads, independent local Git-tree reproduction and every file/blob binding checked before reporting completion.
''')
files=[];seen=set()
def add(p,target=None):
 p=Path(p);rel=p.relative_to(R);assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
 target=target or 'research-checkpoints/continuation260/'+str(rel)
 if target in seen:return
 seen.add(target);files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,K/'public-P12.3-continuation361-excellent-normal-surfaces-and-full-conductor-envelopes-unreviewed',K/'public-P12.6-continuation362-specified-regularized-geometric-envelope-and-full-finite-compatibility-original-candidate']:
 for p in sorted(folder.rglob('*')):
  if p.is_file():add(p)
for q,C in campaigns.items():
 for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','book-context-bindings.json','private-primary-packet-bindings.json','qualified-imported-note-bindings.json','freeze.json','launch-record.json']:add(C/name)
 for e in json.loads((C/'mathematical-packet-bindings.json').read_text()):add(e['path'])
for pattern in ['P12.3-round257-whole-candidate361-ROOT*.json','P12.6-round256-whole-candidate362-ROOT*.json']:
 for p in K.glob(pattern):add(p)
for name in ['capture_completed_native256_20261008.py','capture_completed_native257_20261008.py','stage_whole_completed257_surface361_for_future_independent_review_20261008.py','stage_whole_completed256_finite_compatibility362_for_independent_review_20261008.py','prepare_native258_whole_surface_and_isolated_normal_envelopes_20261008.py','launch_frozen_native258_whole_original_20261008.py','prepare_native259_entire_P12_6_original_candidate362_independent_review_20261008.py','launch_frozen_native259_entire_original_candidate362_review_20261008.py','recover_final_remote_verification_checkpoint259_20261008.py']:add(R/name)
for p in [G/'push-receipt-continuation259.json',G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py',Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
x=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=27,historical_reviewed_scoped_papers=96,commit_message='Checkpoint full normal-surface and P12.6 original candidate manuscripts with independent native reviews',scope='15solved27OPEN96papers; whole361362 proofs pendingindependentreview; fullfrozen258259 math, actual-expanded/source/scope qualifications; noacceptance, primarybodiespixelsLOCALONLY.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,solved=15,open=27,papers=96),indent=2))
