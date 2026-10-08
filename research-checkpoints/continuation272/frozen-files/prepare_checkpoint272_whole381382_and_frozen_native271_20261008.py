from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation272-publication-records'; M=G/'upload-manifest-continuation272.json'
C=R/'campaigns/round-271/P12.3-whole382380381-independent-proof-and-original-residual'
HH=R/'primary-data-LOCALONLY/P12.3-HH02-Jacobian-normalization-primary-20261008'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation271.json'); assert prior['commit_sha']=='cdabc6a12258ca4bb6d3779feaddac1614943014'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name); assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==271
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
assert not (C/'work.sqlite').exists() and sha(C/'input.json')=='9bf31584728af7c8df71f390c7629bb3f8b07dedf35dbe9afa14dec9be5e770b'
D=K/'public-P12.3-continuation382-isolated-perfect-charp-and-nonisolated-finite-cover-whole-candidate'
B=K/'P12.3-round269-whole-candidate382-ROOT-proof-source-scope-and-binding-20261008.json'
assert sha(B)=='db9c6dc393f9e45ad23939d46e3d3a62c3192b2b860b477d8baf32a75e402f09'
P381=K/'P12.3-continuation381-faithfully-flat-diagonal-Cartier-descent-working-paper-20261008.tex'
B381=K/'P12.3-continuation381-ROOT-whole-proof-source-scope-and-binding-20261008.json'
assert sha(P381)=='a779d03e37aec5c1b8feeda0d8c15b8aa2003e85c816908b55b1a5af2c4a4383' and sha(B381)=='d5938b1a2fa7ed426a905bb88f2b397524855d54308aa35f3ee5733d8fe803b5'
F.mkdir(); S=F/'frozen-status-only'; S.mkdir(); frozen=set(); items=[]
def freeze(p):
    p=Path(p); rel=p.relative_to(R)
    assert p.is_file() and 'LOCALONLY' not in str(rel) and p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    if str(rel) in frozen:return
    dst=F/'frozen-files'/rel; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,dst); assert sha(dst)==sha(p); frozen.add(str(rel))
for q in [269,270]:
    d=next((R/f'campaigns/round-{q}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(d/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert not st['error'] and st['status'] in ['running','completed']
    write(S/f'round{q}-public-native-status.json',st); items.append(dict(round=q,status=st['status'],unsettled_calls=st['calls']['unsettled'],observed_utc=st['observedAt']))
active=[e['round'] for e in items if e['unsettled_calls']]; assert len(active)<=1
for p in sorted(C.glob('*.json')):freeze(p)
for p in sorted((C/'immutable-mathematical-DATA').rglob('*')):
    if p.is_file():freeze(p)
for p in sorted(D.rglob('*')):
    if p.is_file():freeze(p)
for p in [B,P381,B381]:freeze(p)
for name in ['public-HH02-retrieval-metadata.json','public-ROOT-full-HH02-3.4-reading-and-generator-scope.json']:
    p=HH/name; dst=F/'public-primary-metadata'/name; dst.parent.mkdir(exist_ok=True); shutil.copyfile(p,dst)
for name in ['capture_completed_native269_actual_FINAL_20261008.py','stage_completed_native269_whole382_ROOT_20261008.py','bind_ROOT381_whole_diagonal_Cartier_descent_20261008.py','fetch_HH02_primary_for_complete_3_4_20261008.py','record_ROOT_fresh_HH02_complete_3_4_reading_20261008.py','prepare_native271_whole382380381_and_original_P12_3_20261008.py','record_verified_checkpoint271_20261008.py']:freeze(R/name)
freeze(G/'push-receipt-continuation271.json'); freeze(G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py'); freeze(Path(__file__))
now=datetime.now(timezone.utc).isoformat()
qual=dict(recorded_utc=now,formal_originals_solved=16,formal_originals_OPEN=26,accepted_papers=97,
    whole381='ENTIRE10074-byte ROOT independent faithfully-flat diagonal-Cartier kernel/image descent lemma saved and ROOT physically read. Any finite-type ring over PERFECT charp and perfect extension; no reduced/normal premise for module lemma. Application to Jacobian inclusion explicitly conditional. Complete finite-presentations/twisted Frobenius/Hom/kernel/image/cokernel argument. UNREVIEWED, not subadditivity or full original closure.',
    whole382='ENTIRE57471-byte nine-note proof plus every DIFFERENT actualFINAL41879bytes and all expanded outside fields ROOT physically read, full source/scope/coverage/verdict. Complete633002-byteTeX and630608MD exact verified bodies plus entire qualified incoming grants, no invented fresh repeat reading. Isolated normal AFFINE finite-type CLOSED perfect-charp all-support CE and actual nonisolated quadratic finite-cover family are scoped UNREVIEWED claims. WHOLE376 reconstruction and original residual retained; no acceptance/count increase.',
    HLS_correction='PreviousROOT377 literal captures13/14 were incomplete and prior full7.5/wholeSection8 completeness-reading labels superseded. Full corrected immediate units freshly ROOT read, source bodies LOCALONLY, correction public. Frozen earlier evidence unchanged.',
    HH_primary='Full publicHH02math0211174v1 PDF/text and entire immediate3.4 statement/proof newly ROOT physically read LF472-504 with3.2/3.3 context. Generatorwise versus every-element statement and K(t) imperfect/perfect-descent distinctions explicit. Full primary units/pixels LOCALONLY; recursiveLS/HH2/HH6/Kunz not newly whole-read. New source is data, no imported correctness grant.',
    frozen271='ENTIRE212 mathematical files6743791bytes, exact task/original/input/settings/freeze with onlyENTIREG331/B341/E350 grants. THREE whole book contexts and392 primary/evidence records retained LOCALONLY; their manifest metadata published. Prepared, NOT YET launched; launch requires verified272 and no more than TWO simultaneous calls. Independent entire382380381 and preciseHH proof gate then fulloriginalP12.3 residual.',
    compiler='ROOT382 request138 pending. ROOT381115 and finalROOT380105 pending; other requests unverified. No success/PDF/export/install/new editor tab claimed. Protected P16.4 editor OPEN UNCHANGED.',
    supplied_or_native_programs_executed_or_imported=False,all_full_primary_bodies_literal_units_source_pixels_and_new_full_book_context_LOCALONLY=True,no_other_ACTIVE_math_read_or_feedback=True,no_count_increase=True)
write(F/'publication-qualification.json',qual)
(F/'README.md').write_text('Checkpoint272: entire isolated perfect-charp reconstruction and diagonal descent\n\n16/42 original problems solved,26 OPEN,97 accepted papers unchanged. Whole381 module lemma and whole382 independent isolated normal perfect-charp/all-support envelope reconstruction are UNREVIEWED complete drafts. All9 distinct actual/expanded texts and full surrounding chain retained. The entire original P12.3 remains OPEN.\n\nPrior HLS source completeness labels were wrong for two literal captures; complete repaired units now ROOT physically read and correction recorded. Fresh complete HH02 immediate3.4 reading distinguishes Jacobian generators, transcendental-field extension and perfect-Frobenius descent. All full primary sources/units/pixels and new book context bodies LOCALONLY. Native programs inert DATA.\n\nFrozen native271 contains212 whole mathematical records and exact initialization data for independent382380381/HH source verification then original residual. Prepared but unlaunched at this checkpoint. Native270 continues; maximumTWO after launch. Compiler requests pending, no success claim; protected editor unchanged. Authorized NONFORCE push verified by independent tree, every blob and fresh branch ref.\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,items=items,maximum_concurrent_campaigns=2,prepared_next_round=271),github_pending_checkpoint=dict(continuation=272,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify272 then launch frozen271 independent entire382380381/HH02 and originalP12.3. Native270 continues; maxTWO. Inspect completed only; no active feedback. Whole original16solved26OPEN97accepted unchanged. Protected editor unchanged.'); write(p,x); shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation272/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/name; files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+name,bytes=p.stat().st_size,sha256=sha(p)))
assert len({x['path'] for x in files})==len(files)
x=load(R/'active-work.json')
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint entire isolated perfect-charp envelope proof and diagonal descent',scope='16solved26OPEN97accepted unchanged. ENTIRE381382 unreviewed; prepared frozen271 full212math. HLS completeness correction and exact HH02 generator/field scope. All primary and new full book context bodies LOCALONLY; no active feedback/editor change.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,prepared_round=271,solved=16,open=26,papers=97),indent=2))
