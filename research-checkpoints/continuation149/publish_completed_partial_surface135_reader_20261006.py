from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks'
W=R/'campaigns/round-135/P16.5-original-entire-big-cone-surface-and-filtered-ideal-research/artifacts/codex-VN2lKc'
C=W.parent.parent;D=K/'public-P16.5-round135-partial-surface-research-reader'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(W/'P16.5-argument.md')=='fe3d0d9636cd00ebd241bf46977358c834b6e78ae92c0b437b789e9b849cfc08'
assert json.loads((C/'input.json').read_text())==json.loads((W/'input-original.json').read_text())
assert (W/'input.json').read_bytes()==(W/'input-original.json').read_bytes()
status=json.loads((W/'status.json').read_text());assert status['status']=='PARTIAL'
assert not D.exists();D.mkdir()
for f in ['P16.5-argument.md','P16.5-paper.tex','P16.5-paper.pdf','status.json']:shutil.copyfile(W/f,D/f)
ledger=json.loads((W/'source-application-ledger.json').read_text())
def redact(x):
    if isinstance(x,dict):return {k:redact(v) for k,v in x.items() if k not in ['literal','complete_preserved_body','quote']}
    if isinstance(x,list):return [redact(v) for v in x]
    return x
public=redact(ledger)
public.update({'canonical_whole_ledger_sha256':sha(W/'source-application-ledger.json'),
               'whole_argument_root_read':True,'whole_ledger_separately_root_read':False,
               'all_source_and_new_result_applications_root_read':True,
               'third_party_literal_bodies_uploaded':False})
(D/'source-application-ledger-PUBLIC.json').write_text(json.dumps(public,ensure_ascii=False,indent=2)+'\n')
log=(W/'P16.5-paper.log').read_text();pdf=D/'P16.5-paper.pdf'
info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
b={'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':135,'status':'PARTIAL',
   'original_closed':False,'accepted_count_change':0,'independently_reviewed':False,
   'whole_mathematical_argument_root_read':True,'whole_final_tex_separately_root_read':False,
   'all_four_canonical_notes_root_read':True,'whole_canonical_ledger_separately_root_read':False,
   'source_and_result_application_fields_root_read':True,
   'files':[{'path':str(D/f),'source_path':str(W/f),'sha256':sha(D/f),'source_sha256':sha(W/f)} for f in ['P16.5-argument.md','P16.5-paper.tex','P16.5-paper.pdf','status.json']],
   'original_campaign_input':{'path':str(C/'input.json'),'sha256':sha(C/'input.json'),'bytes':(C/'input.json').stat().st_size},
   'native_adapter_input':{'sha256':sha(W/'input.json'),'bytes':(W/'input.json').stat().st_size},
   'input_semantic_equality_verified':True,'input_byte_difference_reason':'JSON serialization only; the decoded full task and assignment values are identical.',
   'native_final_log_sha256':sha(W/'P16.5-paper.log'),'overfull':log.count('Overfull'),'undefined':log.count('undefined'),'warnings':log.count('Warning'),
   'pages':int(next(x.split(':')[1] for x in info.splitlines() if x.startswith('Pages:'))),
   'actual_visual_pages':[],'native_editor_compile_success_observed':False,'existing_editor_unchanged':True,
   'scope':'Entire pseudoeffective rational surface cone and precise limited zero-volume/ideal results; no full positive-volume nonample finite-energy equation.'}
assert b['pages']==14 and b['overfull']==b['undefined']==b['warnings']==0
(D/'publication-binding.json').write_text(json.dumps(b,indent=2)+'\n')
for n in [1,7,14]:subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1500','-png','-singlefile',str(pdf),str(D/f'page-{n}-LOCALONLY')],check=True,capture_output=True)
print(json.dumps({'reader':str(D),'pages':b['pages'],'whole_MD_root_read':True,'input_semantic_equality':True,'layout_diagnostics':[b['overfull'],b['undefined'],b['warnings']]},indent=2))
