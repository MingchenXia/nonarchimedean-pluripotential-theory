from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation191.json';F=G/'continuation191-publication-records';S=K/'small-batch184185-public-status-20261007-continuation191'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not any(p.exists() for p in (M,F,S))
prior=json.loads((G/'push-receipt-continuation190.json').read_text());assert prior['commit_sha']=='24da23bdfa4f351fad46e8e2756dce1ad587111d'
assert all(prior[q] for q in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
accept=json.loads((K/'public-P16.4-continuation220-norming-reference-target-criterion/whole-partial-paper-acceptance182-20261007.json').read_text());assert accept['verdict']=='PASS' and accept['cumulative_accepted_paper_number']==71
F.mkdir();S.mkdir();items=[]
for n in (182,184,185):
 c=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(st,indent=2)+'\n')
 items.append(dict(round=n,atom='P05.2' if n==184 else 'P16.4',directory=str(c),observed_status=st['status'],observed_utc=st['observedAt'],public_status=str(p),public_status_sha256=sha(p),unsettled_calls=st['calls']['unsettled'],private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
active=[x for x in items if x['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),items=items,active_items=active,maximum_concurrent_campaigns=2,
 focus='Whole220 norming atomic reference criterion independentlyPASS182 with exact native/frozen/source bindings, accepted supporting paper71; concrete P^n_K domain every complete char0K and arbitrary target, no equation attainment. Entire222 seven-page all-complete-field P^1_K actual kernel equation under independent185 review using only whole accepted O217/D214/N220/T171 grants. Full originalP05.2 classification author184 continues unchanged, no hot feedback. Originals9/42 unchanged.')
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert len(j['fully_solved_original_atoms'])==9 and j['historical_reviewed_scoped_papers']==71 and j['remaining_open_original_atoms']==33
 j.update(updated_utc=datetime.now(timezone.utc).isoformat(),current_small_batch=batch,github_pending_checkpoint=dict(manifest=str(M),continuation=191,status='prepared_for_authorized_push'))
 if name=='checklist-current.json':
  for t in j['targets']:
   if t['id']=='P16.4':
    assert not t['fully_solved'] and t['closure']=='open'
    t['current_focus']='Whole217 operator PASS179/accepted69, whole218 locality/comparison PASS181/accepted70, whole220 norming reference target criterion PASS182/accepted71. Entire222 seven-page actual projective-line equation allK/allampleQ, including intrinsic target/existence/every-solution allpoint uniqueness/variational value, is under independent185 review, not yet accepted. General varieties and higher-genus/non-split curves remain open. Full originalP05.2 author184 continues unchanged.'
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps(dict(recorded_utc=datetime.now(timezone.utc).isoformat(),originals_solved=9,originals_open=33,cumulative_independently_accepted_research_papers=71,new_original_closure=None,new_accepted_partial_review=182,active_batch=[x['round'] for x in active],new_unreviewed_projective_line_equation=222,no_hot_feedback=True,protected_editor_unchanged_open=True),indent=2)+'\n')
author=next((R/'campaigns/round-180').iterdir())/'artifacts/codex-09tHPY';addendum=K/'P16.4-round180-native-compiler-success-source-addendum-20261007.json';assert not addendum.exists()
addendum.write_text(json.dumps(dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=180,path=str(author/'P16.4-paper.tex'),source_sha256=sha(author/'P16.4-paper.tex'),native_result=dict(path=str(author/'P16.4-paper.tex'),kind='success',message="The current source compiled successfully with the desktop editor's compiler."),source_unchanged_since_applicable_compile_request=True,native_compiler_success=True,mathematical_acceptance_implied=False,existing_author_pdf_not_replaced=True,protected_editor_unchanged_open=True),indent=2)+'\n')
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf','.py')
 files.append(dict(local=str(p),path=remote or 'research-checkpoints/continuation191/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in (F,S,K/'public-P16.4-continuation220-norming-reference-target-criterion',K/'public-P16.4-continuation222-projective-line-kernel-equation'):
 for p in sorted(folder.iterdir()):
  if p.is_file() and 'LOCALONLY' not in p.name and p.suffix in ('.json','.md','.tsv','.tex','.pdf'):add(p)
for label in ('actual-canonical-independent-review','native-model-final-review','whole-partial-review-binding'):add(K/f'P16.4-round182-{label}-20261007.json')
add(addendum)
C=next((R/'campaigns/round-185').iterdir())
for name in ('task.json','argument.md','settings.json','freeze.json','original-task.json','mathematical-data-bindings.json','launch-record.json'):add(C/name)
for name in ('bind_completed_review182_20261007.py','accept_norming_target220_review182_20261007.py','prepare_projective_line222_review185_20261007.py','launch_frozen_partial_review185_20261007.py','record_verified190_20261007.py'):add(R/name)
add(G/'push-receipt-continuation190.json');add(Path(__file__))
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
j=json.loads((R/'active-work.json').read_text())
M.write_text(json.dumps(dict(generated_utc=datetime.now(timezone.utc).isoformat(),repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=71,
 commit_message='Accept norming-reference target criterion and audit all-field projective-line equation',
 scope='Whole2205-page norming atomic reference intrinsic target criterion independentlyPASS182, complete10353-char report/all5premises/7passages ROOT read, exact native/frozen/source bindings verified; accepted supporting paper71 with source-preserving citation/indexing clarifications. Publish whole2227-page actual projective-line kernel equation, ROOT467-source-line read/two clean final local builds/exact native compiler SUCCESS/first+last PDF pages only. New allK existence/every-solution allpoint uniqueness/intrinsic target/actual maximizer/rational bundle statements unreviewed under frozen185 independent review with four complete accepted grants O217/D214/N220/T171. P^1 sector does not close originalP16.4 or non-split/higher-genus curves. Full originalP05.2 author184 continues unchanged. Original atoms9/42 unchanged, maximum2 active campaigns. Exact-source native compile success of unreviewed candidate=false180 added, without replacing its original PDF or mathematical acceptance. No private active outputs, full third-party sources, account/runtime/protected editor changes.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(manifest=str(M),sha256=sha(M),listed_files=len(files),active_batch=[x['round'] for x in active],accepted_papers=71,originals_solved=9),indent=2))
