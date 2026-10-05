from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil
R=Path('/workspace/research');G=R/'github-checkpoint';K=R/'root-checks'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
def save(p,x):
 assert not p.exists(),str(p);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation126.json';r=json.loads(previous.read_text())
assert r['commit_sha']=='f3a0ae771d08f09fc3dbba89977ab49c78bef56f'
assert sha(G/'upload-manifest-continuation126.json')==r['manifest_sha256']
assert all(r[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
P=K/'public-P16.5-round123-main-reader';pub=json.loads((P/'publication-preparation.json').read_text())
assert pub['candidate'] is False and pub['whole_main_math_body_root_read']
assert pub['final_local_build_returns']==[0,0,0] and pub['PDF_pages']==15
for n,k in [('P16.5-argument.md','argument_sha256'),('P16.5-paper.tex','source_sha256'),('P16.5-paper.pdf','pdf_sha256')]:assert sha(P/n)==pub[k]
save(P/'native-compiler-final-source-request-20261005.json',{'requested_utc':now,'source':str(P/'P16.5-paper.tex'),'source_sha256':sha(P/'P16.5-paper.tex'),'tool_cell_id':1660,'status':'PENDING','observed_success':False})
p=K/'P16.5-general-big-minimal-reference-primary-input-and-volume-obstruction-20261005-continuation141.md'
b={'recorded_utc':now,'note':str(p),'note_sha256':sha(p),'whole_saved_own_note_root_read':True,'independently_accepted':False,'original_closed':False,
   'external_primary_url':'https://arxiv.org/pdf/2206.07183v2','version':'v2, September2023',
   'complete_pertinent_primary_units_root_read_rendered_lines':[[80,257],[324,405]],
   'external_published_result_not_equation_grant':True,'entire_recursive_foundations_reproved':False,
   'scope':'Published general numerical envelope/minimal-reference and compactness input with original big nonnef relative-operator gates retained; own Bl_p P2 volume4 versus ordinary top3 example.',
   'frozen124_125_inputs_changed':False,'hot_feedback_sent':False,'extended_third_party_source_transcripts_published':False}
save(K/'P16.5-root-continuation141-primary-reference-and-whole-note-reading-binding-20261005.json',b)
for name in ['active-work.json','checklist-current.json']:
 p=R/name;a=json.loads(p.read_text());assert len(a['fully_solved_original_atoms'])==7 and a['historical_reviewed_scoped_papers']==47
 assert [i['round'] for i in a['current_small_batch']['items']]==[124,125]
 a.update({'updated_utc':now,'P16_5_actual_original_research123':pub,'continuation141_general_big_reference_input':b,'github_pending_checkpoint':'continuation127 frozen'})
 p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
D=G/'continuation127-publication-records';D.mkdir(exist_ok=False)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,D/n)
save(D/'scope-observation.json',{'recorded_utc':now,'fully_solved_original_atoms':r['fully_solved_original_atoms'],'remaining_open_originals':35,'historical_reviewed_scoped_papers':47,
  'native123_original_status':'PARTIAL','native123_candidate':False,'native123_main_reader_pages':15,
  'current_native_small_batch':[124,125],'native125_launched':True,'new_supplements':[139,140,141],
  'new_supplements_independently_accepted':False,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
  'native_compiler_success_asserted':False,'native123_main_reader_pending_cell':1660,
  'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False,'extended_third_party_sources_images_or_private_native_state_uploaded':False})
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
 assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','artifacts','shared-sources','evidence'} for x in rel.parts)
 assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log'} and 'LOCALONLY' not in p.name
 if p.suffix=='.pdf':assert p==P/'P16.5-paper.pdf'
 files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation127/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for n in ['P16.5-argument.md','P16.5-paper.tex','P16.5-paper.pdf','status.json','source-application-ledger.json','publication-preparation.json','native-compiler-final-source-request-20261005.json','pdfinfo.txt','final-build-0.stdout','final-build-0.stderr','final-build-1.stdout','final-build-1.stderr','final-build-2.stdout','final-build-2.stderr']:add(P/n)
for n in ['P16.5-round123-actual-native-result-20261005.json','P16.5-round123-main-body-root-reading-and-publication-binding-20261005.json',
 'P16.5-nef-section-volume-and-canonical-minimal-reference-draft-20261005-continuation139.md',
 'P16.5-intrinsic-nef-strict-comparison-and-domination-draft-20261005-continuation140.md',
 'P16.5-general-big-minimal-reference-primary-input-and-volume-obstruction-20261005-continuation141.md',
 'P16.5-root-continuation139-whole-own-proof-reading-binding-20261005.json',
 'P16.5-root-continuation140-whole-own-proof-reading-binding-20261005.json',
 'P16.5-root-continuation141-primary-reference-and-whole-note-reading-binding-20261005.json']:add(K/n)
for p in sorted((K/'current-small-batch124-125-after-native123-20261005').iterdir()):add(p)
for p in [previous,R/'prepare_native123_main_reader_and_record124_125_20261005.py',G/'prepare_checkpoint_continuation127.py']:add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/n,'manuscript/editorial/xean_research_20261003/'+n)
assert len({x['path'] for x in files})==len(files)
M=G/'upload-manifest-continuation127.json'
save(M,{'generated_utc':now,'repository':r['repository'],'branch':r['branch'],'expected_previous_checkpoint':r['commit_sha'],'files':files,'file_count':len(files),
 'fully_solved_original_atoms':r['fully_solved_original_atoms'],'remaining_open_atoms':35,'historical_reviewed_scoped_papers':47,
 'commit_message':'Preserve original123 partial nef-big paper and volume comparison general-reference supplements',
 'scope':'Original123 returned PARTIAL/candidate=false; public15-page own mathematical main proof and ledger preserved without extended primary appendices. Independent124 and125 active. New139 section-volume,140 comparison/domination and141 published general-big minimal-reference input plus volume obstruction remain unreviewed.7 originals solved35 open47 scoped papers; no new acceptance.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'own_PDFs':1},indent=2))
