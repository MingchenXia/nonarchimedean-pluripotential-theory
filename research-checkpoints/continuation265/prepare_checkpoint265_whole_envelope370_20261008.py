from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation265-publication-records';M=G/'upload-manifest-continuation265.json'
D=K/'public-P12.3-continuation370-whole-envelope-and-general-normal-finite-correction-candidate'
B=K/'P12.3-round261-whole-candidate370-ROOT-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation264.json');assert prior['commit_sha']=='888e40107fcf09df083b8b3ba58e12a25b1761e2'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(D/'P12.3-paper.tex')=='a1a231327fb72e18285c801a9353db6f490320c1006fdca9d9af9b6dcc79f5e5'
assert sha(D/'whole-proof.md')=='c8a0b0777954e96c5e06f68708ba6d0ae88c690c5466e6d661b72ce6de35b674'
assert sha(D/'actual-native261-final.json')=='59a5a6f1d825cc2bfee89203a69c25d1b20e1b8871d589a325237fcc04bd20b2'
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
 x=load(R/name);assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==264
 assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
F.mkdir();S=F/'frozen-status-only';S.mkdir();items=[]
for q in [263,264]:
 C=next((R/f'campaigns/round-{q}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 assert not st['error'] and st['status'] in ['running','completed']
 p=S/f'round{q}-public-native-status.json';write(p,st);items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt']))
active=[e['round'] for e in items if e['unsettled_calls']];assert len(active)<=2
now=datetime.now(timezone.utc).isoformat()
write(F/'publication-qualification.json',dict(recorded_utc=now,formal_originals_solved=16,formal_originals_OPEN=26,accepted_papers=97,whole_envelope370_binding=str(B),
 whole370='Entire native261 P12.3 mathematical draft,70730byteTex68431byteproof627130byteMarkdown with literal whole qualified G331/B341/E350 appendices; all14actual FINAL fields separately preserved from all14DIFFERENT expanded texts; all14actual texts EQUAL local actual fields. Full own source ledger/scope/coverage/decision and mandatory ROOT reading/source attribution annotation retained.',
 new_theorem='General NORMAL CLOSED algebraic algclosedchar0 germ dim>=2: GLOBAL finite-continuous raw D/C envelope continuous on OPEN{v(Q)<infinity}, Q=d(K)Jac. Source generalSections1--3/3.17, not isolated4.11. Actual primary truncation, finite trace errors, open-set divisorial density then all-support limits, ONE continuous C majorant per arbitrary D competitor.',
 remaining_original='Infinite-Q CLOSED stratum outside isolated/actual CE-cover sectors, arbitrary excellent/nonalgebraic/nonclosed normal dimension>=3 and higherdim positive/mixedchar remain. No normal counterexample or global D recognition; no count increase.',
 compilation='Stale ROOT367 compiler call46 terminated with NO diagnostics/success; never bound to final repaired version. Fresh standalone370 built-in compiler submitted cell125, source frozen, no response/success at snapshot; does not modify source/open tab/exportPDF.',
 source_attribution='Whole mathematical body/Tex/actual fields and entire application metadata ROOT read. Fresh full immediate published source/PDFimage reading reported by native261; retained ROOT363/364 primary reading remains accurately prior. Duplicate/hash coverage is not fresh physical source reading. Complete primary bodies/pixels LOCALONLY.',
 github264='Nonforce PATCH succeeded but immediate GET disagreed; later ONLY-GET recovery independently verified commit/tree/all138blobs and two fresh references. No second remote mutation. Publisher now permits bounded final old-parent GET retries only, never force/overwrite.',
 primary_bodies_pixels_LOCALONLY=True,source_documents_and_programs_DATA=True,supplied_programs_executed_or_imported=False,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False,protected_editor_open_unchanged=True))
(F/'README.md').write_text('''Checkpoint265: complete P12.3 envelope draft and precise unresolved stratum

16/42 original problems solved,26OPEN,97 accepted papers. No new original closure or accepted-paper increase.

Native261 has settled with original candidateFALSE. Entire paper370 is preserved:70730byteTex,68431bytewholeproof and627130byteMarkdown with ENTIRE inseparable qualified G331/B341/E350 appendices; all14notes plus every actual native FINAL field, separate expanded notes, source application ledger/scope/coverage/decision, finite diagnostics and inert native program DATA. Every actual14text differs from expanded14text; all14actual fields agree with the local actual record. Whole mathematical proof/Tex/actual/metadata ROOT read, expanded entire bodies exactly retained in that read wholeproof; byte duplication is not another source read. Mandatory source attribution distinguishes fresh native reading from retained earlier ROOT primary reading.

The general nonisolated characteristic-zero theorem proves continuity of the GLOBAL finite-continuous raw envelope on OPEN{v(d(K)Jac)<infinity}, retaining ALL semivaluation supports. The proof applies general BdFF3.17, forms ACTUAL primary approximants, uses finite model traces and extends continuous inequalities FIRST on an OPEN set. It never applies isolated4.11 outside its source domain. Exact all-characteristic NORMAL surface CE, smooth/isolated and ACTUAL finite dominating CE-cover sectors, full-fibre constrained reduced normalization, nonnormal double-plane obstruction and complete curve clipping are reconstructed in full. The CLOSED infinite-correction stratum and general higherdim positive/mixedchar/excellent/nonalgebraic residual remain OPEN; failed estimates are not normal counterexamples. No increasing-limit recognition, unconditional pole normalization formula or unproved good-cover existence.

Native263/P21.3 whole independent369/367/368 and original completion, and native264/P16.7 genuinely nonalgebraizable all-support finite-energy equation theory continue on the existing signed-in Xean native Codex gpt-6.1-sol xhigh path, at most TWO concurrent campaigns and ZERO incoming grants. No active math/output reading/hot feedback. Full frozen inputs/launches were published264.

The built-in compiler for370 is pending; no compilation/formal verification claim. Stale367 call terminated without diagnostics. Protected P16.4 editor OPEN UNCHANGED; no new tabs or exported separate PDF. Source bodies/pixels LOCALONLY; supplied programs inert never executed/imported. Regular authorized NONFORCE checkpoint verified by independent native Git tree/all blobs/fresh reference.
''')
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=load(p);x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2),github_pending_checkpoint=dict(continuation=265,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify checkpoint265 ENTIRE370 mathematical draft and mandatory actual/source/scope qualifications. Continue TWO native263/P21.3 and264/P16.7, inspect ONLY complete settled outputs; future whole370 independent reconstruction.16solved26OPEN97papers; protected editor OPEN UNCHANGED; no hot feedback.');write(p,x);shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
files=[];seen=set()
def add(p,target=None):
 p=Path(p);rel=p.relative_to(R);assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
 target=target or 'research-checkpoints/continuation265/'+str(rel)
 if target in seen:return
 seen.add(target);files.append(dict(local=str(p),path=target,bytes=p.stat().st_size,sha256=sha(p)))
for directory in [F,D]:
 for p in sorted(directory.rglob('*')):
  if p.is_file():add(p)
add(B)
for name in ['capture_completed_native261_20261008.py','stage_completed_native261_whole_envelope370_ROOT_20261008.py','verify_and_record_checkpoint264_after_delayed_ref_GET_20261008.py']:add(R/name)
add(G/'push-receipt-continuation264.json');add(G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py');add(Path(__file__))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
x=load(R/'active-work.json');write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint whole P12.3 general-normal finite-correction envelope proof and unresolved stratum',scope='16solved26OPEN97papers. ENTIRE unreviewed37070730Tex/68431proof/627130qualifiedMD, all14actual and separate expanded fields, source/scope/read bindings. Original OPEN, no count increase. Continue263/264 maxTWO; source bodies/pixels LOCALONLY.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,solved=16,open=26,papers=97),indent=2))
