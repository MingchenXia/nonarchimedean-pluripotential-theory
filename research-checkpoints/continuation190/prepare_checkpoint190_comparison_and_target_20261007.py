from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation190.json';F=G/'continuation190-publication-records';S=K/'small-batch182184-public-status-20261007-continuation190'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation189.json').read_text())
assert prior['commit_sha']=='d3bbf41a0a279a5fd38934b35a8bd553fa4031f6'
assert all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
D=K/'public-P16.4-continuation218-strict-locality-comparison'
accept=json.loads((D/'whole-partial-paper-acceptance181-20261007.json').read_text());assert accept['verdict']=='PASS' and accept['cumulative_accepted_paper_number']==70
F.mkdir();S.mkdir();items=[]
for n in (180,181,182,184):
 c=next((R/f'campaigns/round-{n}').iterdir())
 st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
 items.append(dict(round=n,atom='P05.2' if n==184 else 'P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[x for x in items if x['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),items=items,active_items=active,maximum_concurrent_campaigns=2,
 focus='Whole218 strict mixed Borel/open locality and comparison independentlyPASS181, accepted supporting paper70. Whole220 norming-reference intrinsic target criterion under182 review, unreviewed. Full originalP05.2 author184 replaces schema-rejected183 using explicit lossless visible PDF-control-glyph markers; no183 model call admitted. Completed180 candidate=false with full unreviewed twelve-page manuscript, exact native/frozen result binding established. Originals9/42 remain unchanged.')
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==70 and j['remaining_open_original_atoms']==33
 j.update(updated_utc=datetime.now(timezone.utc).isoformat(),current_small_batch=batch,github_pending_checkpoint=dict(manifest=str(M),continuation=190,status='prepared_for_authorized_push'))
 if name=='checklist-current.json':
  for t in j['targets']:
   if t['id']=='P16.4':
    assert not t['fully_solved'] and t['closure']=='open'
    t['current_focus']='Entire217 operator PASS179/accepted69 and entire218 locality/comparison PASS181/accepted70. Whole220 norming reference criterion under independent182, no acceptance or actual attainment. Completed180 candidate=false; ROOT read all five notes and all1003 source lines, verified exact native/frozen binding; source ledger and all PDF pages not yet independently ROOT read. General compactness/EP/outer derivative/intrinsic target converse/attainment/every-solution uniqueness remain open.'
   if t['id']=='P05.2':
    assert not t['fully_solved'] and t['closure']=='open'
    t['current_focus']='Full original structural classification author184 active, no grants. Schema-rejected183 never admitted a model call. Twenty control glyphs from original PDF-extracted family04 are retained as visible markers; all ordinary mathematical characters and completion criteria preserved. Known narrow graph/product results do not close the classification.'
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=datetime.now(timezone.utc).isoformat(),originals_solved=9,originals_open=33,cumulative_independently_accepted_research_papers=70,new_original_closure=None,new_accepted_partial_review=181,active_batch=[x['round'] for x in active],unreviewed_target_criterion=220,completed_partial_author180_candidate=False,failed183_model_calls=0,repair_round=184,no_hot_feedback=True,protected_editor_unchanged_open=True),indent=2)+'\n')
be=K/'continuation221-reboulet-norms-primary-LOCALONLY';v2=json.loads((be/'retrieval-binding-v2.json').read_text());assert sha(be/'Reboulet2026-v2.pdf')==v2['pdf_sha256'] and sha(be/'Reboulet2026-v2.txt')==v2['text_sha256']
observation=K/'P16.4-continuation221-graded-norm-completion-primary-scope-observation-20261007.json';assert not observation.exists()
observation.write_text(json.dumps(dict(recorded_utc=datetime.now(timezone.utc).isoformat(),atom='P16.4',continuation=221,primary_retrieval=v2,whole_pertinent_unit_root_read=True,unit='Entire Section2.7 plus its section boundary',local_text_lf_ranges=[[1820,1856]],
 scope_observation='This literal v2 section describes metric completions of graded norm spaces. Its interpretation as actual finite-energy non-Archimedean metrics retains continuity of envelopes as a condition, and cites earlier work. This section cannot by itself supply actual all-point E1 realizability over arbitrary complete fields without that condition.',
 whole_paper_independently_reconstructed=False,cited_dependency_chain_independently_verified=False,no_claim_of_exhaustive_literature_absence=True,new_accepted_paper=False,original_closed=False,caller_grant=False,full_third_party_source_uploaded=False),indent=2)+'\n')
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py')
 files.append(dict(local=str(p),path=remote or 'research-checkpoints/continuation190/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in (F,S,D,K/'public-P16.4-continuation220-norming-reference-target-criterion'):
 for p in sorted(folder.iterdir()):
  if p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf'):add(p)
for n,labels in [(181,['actual-canonical-independent-review','native-model-final-review','whole-partial-review-binding']), (180,['completed-actual-author-result','native-model-final-partial-author','settled-partial-author-binding'])]:
 for label in labels:add(K/f'P16.4-round{n}-{label}-20261007.json')
add(observation);add(K/'P05.2-round183-declaration-failure-and-repair184-20261007.json')
for n in (182,183,184):
 c=next((R/f'campaigns/round-{n}').iterdir())
 for p in sorted(c.iterdir()):
  if p.is_file() and p.name in ('task.json','argument.md','input.json','settings.json','freeze.json','original-task.json','mathematical-data-bindings.json','launch-record.json','input-representation-repair.json'):add(p)
author=next((R/'campaigns/round-180').iterdir())/'artifacts/codex-09tHPY'
for name in ('P16.4-paper.tex','P16.4-paper.pdf','P16.4-argument.md','source-application-ledger.json','source-application-ledger.md','structured-notes.json','submission.json','checks.py','check-results.json','build.py','verify.py','final-verification.json','artifact-hashes.json','environment-and-build.json'):add(author/name)
for name in ('bind_completed_review181_20261007.py','accept_locality218_review181_20261007.py','prepare_norming_target220_review182_20261007.py','launch_frozen_partial_review182_20261007.py','prepare_original_polyhedral_orthogonality183_20261007.py','launch_frozen_original_polyhedral_orthogonality183_20261007.py','prepare_polyhedral_input_repair184_20261007.py','launch_frozen_original_polyhedral_orthogonality184_20261007.py','bind_completed_partial_author180_20261007.py','record_verified189_20261007.py'):add(R/name)
add(G/'push-receipt-continuation189.json');add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=datetime.now(timezone.utc).isoformat(),repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=70,
 commit_message='Accept all-field comparison and continue target and polyhedral original research',
 scope='Whole2186-page strict Borel/open mixed locality and mixed/pure comparison independentlyPASS181, complete report7premises12passages ROOT read and exact native/frozen bindings verified; accepted supporting paper70 with source-preserving clarifications. Publish whole2205-page norming reference intrinsic target criterion and frozen182 independent review, unreviewed. Publish full originalP05.2 task183 schema rejection with zero model calls, lossless visible-glyph repair184 and successful native launch. Completed180 candidate=false12-page manuscript/notes/native bindings explicitly unreviewed, no original equation closure. New primary221 wholeSection2.7 scope observation preserves envelope hypothesis and verifies literalv2 retrieval, not full paper/dependency correctness. Originals9/42 unchanged; at most two active campaigns. No private active output, full third-party sources, account/runtime/protected editor changes.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[x['round'] for x in active],accepted_papers=70,originals_solved=9),indent=2))
