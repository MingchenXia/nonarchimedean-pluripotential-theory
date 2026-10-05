from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil

R=Path('/workspace/research');G=R/'github-checkpoint';K=R/'root-checks'
D=G/'continuation122-publication-records';P=R/'deliverables/scoped-P15.3-round120'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,a):
 assert not p.exists(),str(p);p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation121.json';r=json.loads(previous.read_text())
assert r['commit_sha']=='1434ad650e5438b64dfc6a1c541ac2a9466385e6'
assert sha(G/'upload-manifest-continuation121.json')==r['manifest_sha256']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
pub=json.loads((P/'publication-preparation.json').read_text())
for n,key in [('P15.3-argument.md','argument_sha256'),('P15.3-paper.tex','source_sha256'),('P15.3-paper.pdf','pdf_sha256')]:assert sha(P/n)==pub[key]
assert pub['original_closed'] is False and pub['whole_final_argument_root_read']
assert pub['local_compilations']==[0,0] and pub['visually_read_final_PDF_pages']==[1,12,16]
binding=K/'P15.3-round120-actual-scoped-review-root-reading-binding-20261005.json'
assert json.loads(binding.read_text())['verdict']=='PASS'
assert not D.exists();D.mkdir()
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
 a=json.loads((R/name).read_text());assert len(a['fully_solved_original_atoms'])==7 and a['historical_reviewed_scoped_papers']==45
 assert a['P15_3_actual_scoped120']['original_closed'] is False
 assert [i['round'] for i in a['current_small_batch']['items']]==[119,121]
shutil.copyfile(R/'active-work.json',D/'active-work.json')
shutil.copyfile(R/'checklist-current.json',D/'checklist-current.json')
shutil.copyfile(R/'checklist-current.tsv',D/'checklist-current.tsv')
save(D/'accepted-original-and-open-scope-observation.json',{
 'recorded_utc':now,'fully_solved_original_atoms':r['fully_solved_original_atoms'],'remaining_open_originals':35,
 'historical_reviewed_scoped_papers':45,'new_scoped120_verdict':'PASS','new_scoped120_original_closed':False,
 'new_scoped120_standalone_paper_pages':16,'local_build_passes':[0,0],'native_compiler_success_asserted':False,
 'active_native_rounds':[119,121],'new_proposals130_131_independently_accepted':False,
 'actual_native121_model':'gpt-6.1-sol','actual_native121_reasoning':'xhigh','native121_role':'codex',
 'native121_prelaunch_invalid_role_rejected_before_database_or_model_call':True,
 'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False,
 'third_party_whole_papers_images_or_extended_web_responses_uploaded':False,
 'active_frozen_inputs_modified_or_hot_feedback_sent':False})
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
 assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','artifacts','shared-sources'} for x in rel.parts)
 assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log'}
 assert 'LOCALONLY' not in p.name
 if p.suffix=='.pdf':assert p==P/'P15.3-paper.pdf'
 files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation122/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for name in ['P15.3-argument.md','P15.3-paper.tex','P15.3-paper.pdf','P15.3-correctness-review.json',
 'author-source-provenance.json','source-application-ledger.json','build_paper.py','build-manifest.json',
 'compile-1.stdout','compile-1.stderr','compile-2.stdout','compile-2.stderr','publication-preparation.json',
 'pdfinfo.txt','native-compiler-final-source-request-20261005.json']:add(P/name)
for name in ['P15.3-round120-actual-scoped-independent-review-20261005.json',binding.name,
 'P16.5-semiample-big-contraction-entire-cone-and-outer-directions-draft-20261005-continuation130.md',
 'P16.5-nonbig-mixed-equation-target-and-two-sign-obstruction-draft-20261005-continuation131.md',
 'P16.5-root-continuation130-final-own-proof-reading-and-input-binding.json',
 'P16.5-root-continuation131-final-own-proof-reading-and-input-binding.json']:add(K/name)
for p in sorted((K/'current-small-batch119-121-20261005').iterdir()):add(p)
C=R/'campaigns/round-121/P16.5-original-minimal-reference-and-nonbig-carrier-research'
freeze=json.loads((C/'freeze.json').read_text());assert sha(C/'input.json')==freeze['input_sha256']
for name in ['settings.json','task.json','task-original.json','freeze.json','mathematical-data-bindings.json']:add(C/name)
for p in [previous,R/'record_verified121_20261005.py',R/'prepare_original_P16_5_minimal_semiample_and_nonbig_research121_20261005.py',
 R/'prepare_scoped_P15_3_publication120_20261005.py',R/'typeset_scoped_P15_3_exact_prose120_20261005.py',
 R/'record_scoped120_and_original_research121_20261005.py',G/'prepare_checkpoint_continuation122.py']:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
manifest=G/'upload-manifest-continuation122.json'
save(manifest,{'generated_utc':now,'repository':r['repository'],'branch':r['branch'],
 'expected_previous_checkpoint':r['commit_sha'],'files':files,'file_count':len(files),
 'fully_solved_original_atoms':r['fully_solved_original_atoms'],'remaining_open_atoms':35,
 'historical_reviewed_scoped_papers':45,
 'commit_message':'Publish reviewed torus collapse and exact exceptional body; continue nonample research',
 'scope':'Scoped120 PASS with complete16-page standalone proof, exact source/application ledger and actual report bindings. New unreviewed semiample-birational and nonbig mixed-target/derivative proposals130/131; unchanged original native121 research and scoped119 review active. Seven original problems solved,35 open,45 reviewed scoped papers.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),'own_PDFs':1},indent=2))
