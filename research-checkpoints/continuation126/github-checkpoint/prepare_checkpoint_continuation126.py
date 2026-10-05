from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil
R=Path('/workspace/research');G=R/'github-checkpoint';K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
previous=G/'push-receipt-continuation125.json';r=json.loads(previous.read_text())
assert r['commit_sha']=='82499c422ea86badb1df47b1d0a49e7e562b7236'
assert sha(G/'upload-manifest-continuation125.json')==r['manifest_sha256']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
D=G/'continuation126-publication-records';assert not D.exists();D.mkdir()
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,D/n)
for n in ['active-work.json','checklist-current.json']:
 a=json.loads((D/n).read_text());assert len(a['fully_solved_original_atoms'])==7 and a['historical_reviewed_scoped_papers']==47
 assert [i['round'] for i in a['current_small_batch']['items']]==[123,124]
 assert a['prepared_scoped125_nef_big_equation']['prepared_only'] is True
P=K/'public-P16.5-own138-candidate-reader';pub=json.loads((P/'publication-preparation.json').read_text())
for n,k in [('P16.5-argument.md','argument_sha256'),('P16.5-paper.tex','source_sha256'),('P16.5-paper.pdf','pdf_sha256')]:assert sha(P/n)==pub[k]
assert pub['all_whole_constituent_math_proofs_root_read'] and pub['actual_visual_pages']==[1,27,39]
assert not pub['whole_assembled_argument_separately_root_read']
assert pub['PDF_pages']==39 and pub['final_local_build_returns']==[0,0] and pub['independently_accepted'] is False
now=datetime.now(timezone.utc).isoformat()
(D/'scope-observation.json').write_text(json.dumps({'recorded_utc':now,'fully_solved_original_atoms':r['fully_solved_original_atoms'],'remaining_open_originals':35,'historical_reviewed_scoped_papers':47,
 'new_nef_big_candidate138_independently_accepted':False,'new_candidate_original_closed':False,'own_candidate_paper_pages':39,'all_constituent_proofs_root_read':True,'whole_assembled_argument_separately_root_read':False,
 'old_unreviewed136_both_small_PL_signs_psh_claim_withdrawn':True,'corrected136_repair2_difference_of_two_ample_psh_inputs':True,
 'active_native_rounds':[123,124],'native125_prepared_only':True,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
 'native_compiler_success_asserted':False,'native_compiler_final_source_pending_cell':1616,'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False,
 'third_party_full_sources_images_or_private_native_state_uploaded':False},indent=2)+'\n')
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
 assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','artifacts','shared-sources','evidence'} for x in rel.parts)
 assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log'} and 'LOCALONLY' not in p.name
 if p.suffix=='.pdf':assert p==P/'P16.5-paper.pdf'
 files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation126/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for n in ['P16.5-argument.md','P16.5-paper.tex','P16.5-paper.pdf','publication-preparation.json','native-compiler-final-source-request-20261005.json','pdfinfo.txt','build-0.stdout','build-0.stderr','final-build-1.stdout','final-build-1.stderr','final-build-2.stdout','final-build-2.stderr']:add(P/n)
for n in ['P16.5-nef-polar-capacity-and-original-observable-control-draft-20261005-continuation136-repair2.md','P16.5-nef-divisorial-atomic-attainment-and-I-separation-draft-20261005-continuation137.md','P16.5-nef-big-full-intrinsic-variational-attainment-draft-20261005-continuation138.md']:add(K/n)
for no in [136,137,138]:add(K/f'P16.5-root-continuation{no}-native125-final-own-proof-reading-and-input-binding.json')
for p in sorted((K/'current-small-batch123-124-own138-update-20261005').iterdir()):add(p)
C=R/'campaigns/round-125/P16.5-entire-nef-big-variational-equation-independent-review';f=json.loads((C/'freeze.json').read_text())
assert sha(C/'task.json')==f['task_sha256'] and sha(C/'argument.md')==f['argument_sha256'] and sha(C/'settings.json')==f['settings_sha256']
for n in ['task.json','task-original.json','original-P16.5-task-data.json','settings.json','freeze.json','mathematical-data-bindings.json']:add(C/n)
for p in [previous,R/'record_verified125_20261005.py',R/'prepare_scoped_P16_5_nef_big_equation_review125_20261005.py',R/'prepare_nef_big_candidate_reader138_20261005.py',G/'prepare_checkpoint_continuation126.py']:add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/n,'manuscript/editorial/xean_research_20261003/'+n)
assert len({x['path'] for x in files})==len(files)
M=G/'upload-manifest-continuation126.json';assert not M.exists()
M.write_text(json.dumps({'generated_utc':now,'repository':r['repository'],'branch':r['branch'],'expected_previous_checkpoint':r['commit_sha'],'files':files,'file_count':len(files),
 'fully_solved_original_atoms':r['fully_solved_original_atoms'],'remaining_open_atoms':35,'historical_reviewed_scoped_papers':47,
 'commit_message':'Preserve corrected polar and atomic proofs plus full intrinsic nef-big variational candidate',
 'scope':'New unreviewed39-page candidate paper includes all indispensable bounded/floor/mixed/weighted/coercivity, corrected polar, atomic/separation and full-nef-big variational proof bodies. Original136 withdrawn PL-sign assumption preserved and explicitly corrected in repair2. Independent125 frozen awaiting one free slot; original123 and intrinsic124 remain active. No new PASS or original closure:7 solved originals35 open47 scoped papers.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'own_PDFs':1},indent=2))
