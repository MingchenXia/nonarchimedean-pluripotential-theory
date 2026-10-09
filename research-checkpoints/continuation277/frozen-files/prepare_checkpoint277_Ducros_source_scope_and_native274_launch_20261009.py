from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation277-publication-records'; M=G/'upload-manifest-continuation277.json'
S=R/'primary-data-LOCALONLY/P16.7-Ducros2012-local-tropical-dimension-20261009'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation276.json')
assert prior['commit_sha']=='cad97c40d2fe51c35bd86d937312460ba95e068e'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==276
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
Q=K/'P16.7-Ducros2012-local-dimension-ROOT-primary-reading-and-version-scope-20261009.json'
assert sha(Q)=='24b3d447aa522fa6d49cc80697d45bb9f19cae45c36cc174118496c70eeb7b48'
q=load(Q)
assert not q['original_closed'] and not q['accepted_paper'] and not q['new_correctness_grant']
for key in ['full_read_units','primary_PDF_pixels','full_erratum_texts']:
    for e in q[key]:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
campaigns={273:R/'campaigns/round-273/P16.7-whole385387-full-bounded-dual-and-intrinsic-E1',274:R/'campaigns/round-274/P12.3-whole386-Jensen-completion-and-original-residual'}
states={}
for n,c in campaigns.items():
    states[n]=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    assert states[n]['error'] is None and states[n]['status'] in ['running','completed']
la=load(campaigns[274]/'launch-record.json')
assert la['round']==274 and la['frozen_input_sha256']=='6d0d003dc2d964a9154146398ac8b10a9a7f8940ccbfd0539c104cb8d97126b3'
assert la['model']=='gpt-6.1-sol' and la['reasoning']=='xhigh' and la['only_grants']==['G331','B341','E350']
active=[n for n,s in states.items() if s['calls']['unsettled']]
assert sum(s['calls']['unsettled'] for s in states.values())<=2
F.mkdir()
def freeze(p):
    p=Path(p); rel=p.relative_to(R)
    assert p.is_file() and 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel) and 'immutable-book-context' not in str(rel)
    assert p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    dst=F/'frozen-files'/rel; dst.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(p,dst); assert sha(dst)==sha(p)
for p in [Q,R/'record_Ducros2012_local_dimension_ROOT_source_scope_20261009.py',R/'fetch_Ducros2012_local_dimension_and_erratum_primary_20261009.py',R/'fetch_official_Ducros2013_erratum_and_version_metadata_20261009.py',campaigns[274]/'launch-record.json',R/'launch_frozen_native274_whole386_checked_20261009.py',R/'record_verified_checkpoint276_20261009.py',G/'push-receipt-continuation276.json',G/'push_frozen_checkpoint_bulk_fresh_GET_20261008.py',Path(__file__)]:freeze(p)
for name in ['public-primary-retrieval-metadata.json','public-official-erratum-and-version-retrieval-metadata.json']:
    p=S/name; dst=F/'source-retrieval-metadata'/name; dst.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(p,dst); assert sha(dst)==sha(p)
for n,s in states.items():write(F/('native%d-public-status.json'%n),s)
now=datetime.now(timezone.utc).isoformat()
write(F/'publication-qualification.json',dict(recorded_utc=now,solved=16,open=26,accepted_papers=97,status='Native274 launched; new ROOT whole local-dimension immediate dependency proof and complete erratum readings. No original closure or draft acceptance.',source_reading_record=str(Q),source_version_correction_authoritative_over_earlier_retrieval_description=True,qualified_application=q['qualified_application'],source_boundary=q['deeper_background_not_newly_full_proof_read'],printed_typos=q['printed_typographical_errors'],version_metadata_correction=q['version_metadata_correction'],active_rounds=active,maximum_concurrent_campaigns=2,no_active_native_math_read_or_hot_feedback=True,supplied_or_native_programs_executed_or_imported=False,all_full_primary_bodies_literal_units_pixels_and_book_context_LOCALONLY=True,compiler='Native385/386/387 editor compiler requests remain UNVERIFIED. Protected editor OPEN UNCHANGED; no newtabs.'))
(F/'README.md').write_text('Checkpoint277: local tropical dimension source audit and native274 launch\n\n16/42 original problems solved,26 OPEN,97 accepted scoped papers unchanged. Both native campaigns use Xean native signed-in Codex gpt-6.1-sol xhigh; at most TWO. The P12.3 campaign now runs with whole386 and only the entire qualified G331/B341/E350. P16.7 investigates full bounded tangent and dual formulas and original finite-energy scope. No active native mathematics was read or fed back.\n\nROOT physically read the complete local dimension theorem and its immediate graded/Zariski-Riemann dependency proofs, plus both entire 2013 erratum texts. Full original PDF pages27-29 and39-41 were viewed. Two printed author-version typographical errors are explicitly recorded, with restricted interpretations and the applied upper-bound proof chain. The erratum repairs a separate section2 valuation-separation argument, which this upper-bound chain does not use. Deep Temkin/ACVF foundations are disclosed background, not newly completed recursive proof trees.\n\nThe version correction in the ROOT reading record supersedes any contradictory inference in the earlier retrieval metadata: the actual official and author erratum PDFs print identical received/revised dates, while the web metadata differs. All full primary bodies, literal units, source pixels and book contexts stay LOCALONLY. No draft acceptance, original closure, supplied-program execution or editor change. Publication is NONFORCE with independent Git tree and fresh remote verification.\n')
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p)
    x.update(updated_utc=now,current_active_batch=active,current_small_batch=dict(recorded_utc=now,maximum_concurrent_campaigns=2,items=[dict(round=n,status=s['status'],unsettled_calls=s['calls']['unsettled']) for n,s in states.items()]),github_pending_checkpoint=dict(continuation=277,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify277 source-reading and native274 launch checkpoint. Continue independent fullbounded Green/tangent analysis forP16.7 and primary/model completion scope forP12.3 while at mostTWO native campaigns run. Capture completed FINAL only after completed/errornull/unsettled0; entireprooffreshread before classification.16solved26OPEN97accepted unchanged; protected editor unchanged.')
    write(p,x); shutil.copyfile(p,F/name)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
files=[]
for p in sorted(F.rglob('*')):
    if p.is_file():files.append(dict(local=str(p),path='research-checkpoints/continuation277/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    p=F/name; files.append(dict(local=str(p),path='manuscript/editorial/xean_research_20261003/'+name,bytes=p.stat().st_size,sha256=sha(p)))
assert len({e['path'] for e in files})==len(files)
x=load(R/'active-work.json')
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint local tropical dimension primary proof audit and formal completion launch',scope='Complete source immediate proofs and errata read, exact printed typo/version qualifications, native274 launch. No closure, acceptance, fullprimary/book publication or activefeedback/editor change.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=active,solved=16,open=26,papers=97),indent=2))
