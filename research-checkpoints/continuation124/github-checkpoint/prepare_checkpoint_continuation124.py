from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil

R=Path('/workspace/research');G=R/'github-checkpoint';K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
previous=G/'push-receipt-continuation123.json';r=json.loads(previous.read_text())
assert r['commit_sha']=='a0b0209b9a98cd5756328b003228e5c62544c13f'
assert sha(G/'upload-manifest-continuation123.json')==r['manifest_sha256']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
D=G/'continuation124-publication-records';assert not D.exists();D.mkdir()
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,D/n)
for n in ['active-work.json','checklist-current.json']:
 a=json.loads((D/n).read_text());assert len(a['fully_solved_original_atoms'])==7 and a['historical_reviewed_scoped_papers']==46
 assert [i['round'] for i in a['current_small_batch']['items']]==[122,123]
 assert a['P16_5_actual_scoped119']['original_closed'] is False and a['P16_5_actual_scoped119']['verdict']=='PASS'
P=R/'deliverables/scoped-P16.5-round119';pub=json.loads((P/'publication-preparation.json').read_text())
for n,k in [('P16.5-argument.md','argument_sha256'),('P16.5-paper.tex','source_sha256'),('P16.5-paper.pdf','pdf_sha256')]:assert sha(P/n)==pub[k]
assert pub['whole_final_publication_argument_separately_reread'] and pub['actually_visually_read_final_PDF_pages']==[1,8,15]
assert pub['PDF_pages']==15 and pub['local_compilations']==[0,0]
now=datetime.now(timezone.utc).isoformat()
(D/'scope-observation.json').write_text(json.dumps({'recorded_utc':now,'fully_solved_original_atoms':r['fully_solved_original_atoms'],'remaining_open_originals':35,
 'historical_reviewed_scoped_papers':46,'new_scoped119_verdict':'PASS','new_scoped119_original_closed':False,'standalone_paper_pages':15,
 'actual_external_premises':10,'actual_passage_records':2694,'distinct_lossless_passage_groups_root_read':156,
 'report_minus_one_sentence_has_no_actual_minus_one_passage_preserved':True,'new_proposals134_135_independently_accepted':False,
 'active_native_rounds':[122,123],'native123_role':'codex','route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
 'native_compiler_success_asserted':False,'native_compiler_final_source_pending_cell':1553,
 'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False,'third_party_full_sources_images_or_private_native_state_uploaded':False},indent=2)+'\n')
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
 assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','artifacts','shared-sources','evidence'} for x in rel.parts)
 assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log'} and 'LOCALONLY' not in p.name
 if p.suffix=='.pdf':assert p==P/'P16.5-paper.pdf'
 files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation124/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for n in ['P16.5-argument.md','P16.5-paper.tex','P16.5-paper.pdf','P16.5-correctness-review.json','lossless-review-passage-groups.json','author-source-application-ledger.json','publication-preparation.json','pdfinfo.txt','native-compiler-final-source-request-20261005.json','pandoc-final.stdout','pandoc-final.stderr','compile-final-1.stdout','compile-final-1.stderr','compile-final-2.stdout','compile-final-2.stderr']:add(P/n)
for n in ['P16.5-round119-actual-scoped-independent-review-20261005.json','P16.5-round119-lossless-unique-passage-reading-groups-20261005.json','P16.5-round119-actual-scoped-review-root-reading-and-publication-binding-20261005.json',
 'P16.5-nef-entire-mixed-weighted-nets-and-two-sign-outer-draft-20261005-continuation134.md',
 'P16.5-nef-weak-energy-usc-intrinsic-targets-and-coercivity-draft-20261005-continuation135.md',
 'P16.5-root-continuation134-final-own-proof-reading-and-native-input-binding.json','P16.5-root-continuation135-final-own-proof-reading-and-native-input-binding.json']:add(K/n)
for p in sorted((K/'current-small-batch122-123-20261005').iterdir()):add(p)
C=R/'campaigns/round-123/P16.5-original-intrinsic-nef-variational-and-general-reference-research';f=json.loads((C/'freeze.json').read_text())
assert sha(C/'input.json')==f['input_sha256'] and sha(C/'task.json')==f['unchanged_original_task_sha256']
for n in ['task.json','task-original.json','settings.json','freeze.json','mathematical-data-bindings.json']:add(C/n)
for p in [previous,R/'record_verified123_20261005.py',R/'prepare_original_P16_5_nef_variational_and_general_reference_research123_20261005.py',R/'prepare_scoped_P16_5_publication119_20261005.py',R/'record_scoped119_and_original_research123_20261005.py',G/'prepare_checkpoint_continuation124.py']:add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/n,'manuscript/editorial/xean_research_20261003/'+n)
assert len({f['path'] for f in files})==len(files)
M=G/'upload-manifest-continuation124.json';assert not M.exists()
M.write_text(json.dumps({'generated_utc':now,'repository':r['repository'],'branch':r['branch'],'expected_previous_checkpoint':r['commit_sha'],'files':files,'file_count':len(files),
 'fully_solved_original_atoms':r['fully_solved_original_atoms'],'remaining_open_atoms':35,'historical_reviewed_scoped_papers':46,
 'commit_message':'Publish reviewed bounded-reference and numerical-zero equations; pursue intrinsic nef variation',
 'scope':'Exact scoped119 PASS and complete15-page standalone proof with all actual report passages preserved and lossless repeated-passage reading groups. New unreviewed entire-nef mixed/weighted/two-sign and weak-usc/intrinsic-dual/coercivity proposals134/135. Independent scoped122 and unchanged original123 native research active;7 original solutions35 original open46 reviewed scoped papers.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'own_PDFs':1},indent=2))
