from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil

R=Path('/workspace/research');G=R/'github-checkpoint';K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
previous=G/'push-receipt-continuation122.json';r=json.loads(previous.read_text())
assert r['commit_sha']=='177736a5d84136b7e1d405764b3284250e4d9f7d'
assert sha(G/'upload-manifest-continuation122.json')==r['manifest_sha256']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
D=G/'continuation123-publication-records';assert not D.exists();D.mkdir()
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,D/n)
for n in ['active-work.json','checklist-current.json']:
 a=json.loads((D/n).read_text());assert len(a['fully_solved_original_atoms'])==7
 assert a['historical_reviewed_scoped_papers']==45
 assert [i['round'] for i in a['current_small_batch']['items']]==[119,122]
 assert a['P16_5_actual_original_research121']['original_closed'] is False
P=K/'public-P16.5-round121-final-reader';pub=json.loads((P/'publication-preparation.json').read_text())
assert pub['status']=='PARTIAL' and pub['candidate'] is False
for n,k in [('P16.5-argument.md','argument_sha256'),('P16.5-paper.tex','source_sha256'),('P16.5-paper.pdf','pdf_sha256')]:assert sha(P/n)==pub[k]
assert pub['actual_final_PDF_pages_visually_read']==[1,7,14]
now=datetime.now(timezone.utc).isoformat()
(D/'scope-observation.json').write_text(json.dumps({
 'recorded_utc':now,'fully_solved_original_atoms':r['fully_solved_original_atoms'],'remaining_open_originals':35,
 'historical_reviewed_scoped_papers':45,'native121_status':'PARTIAL','native121_candidate':False,
 'native121_paper_pages':14,'native121_original_closed':False,'proposals132_133_independently_accepted':False,
 'active_native_rounds':[119,122],'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
 'native_compiler_success_asserted':False,'native_compiler_pending_cell':1528,
 'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False,
 'third_party_whole_papers_images_extended_web_responses_or_private_native_state_uploaded':False},indent=2)+'\n')
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
 assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','artifacts','shared-sources','evidence'} for x in rel.parts)
 assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log'} and 'LOCALONLY' not in p.name
 if p.suffix=='.pdf':assert p==P/'P16.5-paper.pdf'
 files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation123/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for n in ['P16.5-argument.md','P16.5-paper.tex','P16.5-paper.pdf','source-application-ledger.json','status.json','canonical-notes.json','run-log.json','environment.json','preservation.json','verification.json','checks-output.json','pdfinfo.txt','publication-preparation.json','pdflatex-pass1.stdout','pdflatex-pass1.stderr','pdflatex-pass2.stdout','pdflatex-pass2.stderr']:add(P/n)
for n in ['P16.5-round121-actual-original-research-result-20261005.json','P16.5-round121-actual-partial-result-root-reading-and-publication-binding.json',
 'P16.5-nef-bounded-products-and-continuous-obstacle-differentiability-draft-20261005-continuation132.md',
 'P16.5-root-continuation132-final-own-proof-reading-and-review-input-binding.json',
 'P16.5-entire-nef-floor-energy-operator-and-weighted-floor-limits-draft-20261005-continuation133.md',
 'P16.5-root-continuation133-final-own-proof-reading-and-source-binding.json']:add(K/n)
for p in sorted((K/'current-small-batch119-122-20261005').iterdir()):add(p)
C=R/'campaigns/round-122/P16.5-nef-bounded-products-and-continuous-obstacle-independent-review'
f=json.loads((C/'freeze.json').read_text());c=json.loads((C/'prelaunch-settings-correction.json').read_text())
assert sha(C/'argument.md')==f['argument_sha256'] and sha(C/'task.json')==f['task_sha256']
assert sha(C/'settings.json')==c['new_settings_sha256']
for n in ['task.json','task-original.json','settings.json','settings-prelaunch-invalid-prefix.json','prelaunch-settings-correction.json','freeze.json','mathematical-data-bindings.json']:add(C/n)
for p in [previous,R/'record_verified122_20261005.py',R/'prepare_scoped_P16_5_nef_bounded_review122_20261005.py',R/'record_partial121_and_nef_proposals132_133_20261005.py',G/'prepare_checkpoint_continuation123.py']:add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/n,'manuscript/editorial/xean_research_20261003/'+n)
assert len({f['path'] for f in files})==len(files)
M=G/'upload-manifest-continuation123.json';assert not M.exists()
M.write_text(json.dumps({'generated_utc':now,'repository':r['repository'],'branch':r['branch'],'expected_previous_checkpoint':r['commit_sha'],
 'files':files,'file_count':len(files),'fully_solved_original_atoms':r['fully_solved_original_atoms'],'remaining_open_atoms':35,'historical_reviewed_scoped_papers':45,
 'commit_message':'Checkpoint nonample partial theorem and nef floor research; continue independent reviews',
 'scope':'Native121 actual candidate=false with complete14-page standalone partial paper. Unreviewed bounded-nef continuous-obstacle proposal132 and entire intrinsic-floor weighted proposal133; native119/122 scoped reviews active. Original counts7 solved35 open remain unchanged.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'own_PDFs':1},indent=2))
