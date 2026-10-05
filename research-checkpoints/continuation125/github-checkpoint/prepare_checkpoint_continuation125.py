from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil
R=Path('/workspace/research');G=R/'github-checkpoint';K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
previous=G/'push-receipt-continuation124.json';r=json.loads(previous.read_text())
assert r['commit_sha']=='e1eee693fa22737effa804f2f07e220320f7894f'
assert sha(G/'upload-manifest-continuation124.json')==r['manifest_sha256']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
D=G/'continuation125-publication-records';assert not D.exists();D.mkdir()
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,D/n)
for n in ['active-work.json','checklist-current.json']:
 a=json.loads((D/n).read_text());assert len(a['fully_solved_original_atoms'])==7 and a['historical_reviewed_scoped_papers']==47
 assert [i['round'] for i in a['current_small_batch']['items']]==[123,124]
 assert a['P16_5_actual_scoped122']['verdict']=='PASS' and a['P16_5_actual_scoped122']['original_closed'] is False
P=R/'deliverables/scoped-P16.5-round122';pub=json.loads((P/'publication-preparation.json').read_text())
for n,k in [('P16.5-argument.md','argument_sha256'),('P16.5-paper.tex','source_sha256'),('P16.5-paper.pdf','pdf_sha256')]:assert sha(P/n)==pub[k]
assert pub['whole_final_publication_argument_separately_root_read'] and pub['actual_visual_pages']==[1,4,7]
assert pub['PDF_pages']==7 and pub['final_local_build_returns']==[0,0,0]
now=datetime.now(timezone.utc).isoformat()
(D/'scope-observation.json').write_text(json.dumps({'recorded_utc':now,'fully_solved_original_atoms':r['fully_solved_original_atoms'],'remaining_open_originals':35,'historical_reviewed_scoped_papers':47,
 'new_scoped122_verdict':'PASS','new_scoped122_original_closed':False,'standalone_paper_pages':7,'external_premises':17,'external_https_passages':29,'inline_G0_task_URI_passages':1,
 'all_urls_https_claimed':False,'new_polar_proposal136_independently_accepted':False,'active_native_rounds':[123,124],
 'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','native_compiler_success_asserted':False,'native_compiler_final_source_pending_cell':1581,
 'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False,'third_party_full_sources_images_or_private_native_state_uploaded':False},indent=2)+'\n')
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
 assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','artifacts','shared-sources','evidence'} for x in rel.parts)
 assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log'} and 'LOCALONLY' not in p.name
 if p.suffix=='.pdf':assert p==P/'P16.5-paper.pdf'
 files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation125/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for n in ['P16.5-argument.md','P16.5-paper.tex','P16.5-paper.pdf','P16.5-correctness-review.json','publication-preparation.json','native-compiler-final-source-request-20261005.json','final-polished-build-0.stdout','final-polished-build-0.stderr','final-polished-build-1.stdout','final-polished-build-1.stderr','final-polished-build-2.stdout','final-polished-build-2.stderr']:add(P/n)
for n in ['P16.5-round122-actual-scoped-independent-review-20261005.json','P16.5-round122-actual-scoped-review-root-reading-and-publication-binding-20261005.json','P16.5-nef-polar-capacity-and-original-observable-control-draft-20261005-continuation136.md','P16.5-root-continuation136-final-own-proof-reading-and-source-binding.json']:add(K/n)
for p in sorted((K/'current-small-batch123-124-20261005').iterdir()):add(p)
C=R/'campaigns/round-124/P16.5-entire-intrinsic-nef-weighted-outer-and-dual-independent-review';f=json.loads((C/'freeze.json').read_text())
assert sha(C/'task.json')==f['task_sha256'] and sha(C/'argument.md')==f['argument_sha256'] and sha(C/'settings.json')==f['settings_sha256']
for n in ['task.json','task-original.json','original-P16.5-task-data.json','settings.json','freeze.json','mathematical-data-bindings.json']:add(C/n)
for p in [previous,R/'record_verified124_20261005.py',R/'prepare_scoped_P16_5_intrinsic_nef_review124_20261005.py',R/'prepare_scoped_P16_5_publication122_20261005.py',R/'record_scoped122_and_current123_124_20261005.py',G/'prepare_checkpoint_continuation125.py']:add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/n,'manuscript/editorial/xean_research_20261003/'+n)
assert len({x['path'] for x in files})==len(files)
M=G/'upload-manifest-continuation125.json';assert not M.exists()
M.write_text(json.dumps({'generated_utc':now,'repository':r['repository'],'branch':r['branch'],'expected_previous_checkpoint':r['commit_sha'],'files':files,'file_count':len(files),
 'fully_solved_original_atoms':r['fully_solved_original_atoms'],'remaining_open_atoms':35,'historical_reviewed_scoped_papers':47,
 'commit_message':'Publish bounded-nef metric and two-sided variation paper; advance intrinsic polar control',
 'scope':'Exact scoped122 PASS and complete seven-page standalone bounded-nef proof.17 external premises29 HTTPS passages and one legitimate inline G0 grant passage distinguished. Unreviewed intrinsic nef polar capacity and original-observable proposal136. Original123 and scoped124 native work active;7 original solutions35 originals open47 reviewed scoped papers.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'own_PDFs':1},indent=2))
