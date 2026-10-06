from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research'); K=R/'root-checks'
W=R/'campaigns/round-136/P19.2-original-energy-entropy-and-P-singularity-model-approximation-research/artifacts/codex-Hx0s4M'
C=W.parent.parent; D=K/'public-P19.2-round136-partial-approximation-reader'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert json.loads((C/'input.json').read_text())==json.loads((W/'input-original.json').read_text())
assert (W/'input.json').read_bytes()==(W/'input-original.json').read_bytes()
status=json.loads((W/'status.json').read_text()); assert status['status']=='PARTIAL'
assert all(x['exit_code']==0 for x in json.loads((W/'build-output.json').read_text())['results'])
assert not D.exists(); D.mkdir()
for f in ['P19.2-argument.md','P19.2-paper.tex','P19.2-paper.pdf','status.json']: shutil.copyfile(W/f,D/f)
ledger=json.loads((W/'source-application-ledger.json').read_text())
ledger.update({'canonical_whole_ledger_sha256':sha(W/'source-application-ledger.json'),
               'whole_argument_root_read':True,'whole_ledger_root_read':True,
               'all_source_and_new_result_applications_root_read':True,
               'third_party_literal_bodies_uploaded':False})
(D/'source-application-ledger-PUBLIC.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
log=(W/'P19.2-paper.log').read_text(); pdf=D/'P19.2-paper.pdf'
info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
pages=int(next(x.split(':')[1] for x in info.splitlines() if x.startswith('Pages:')))
b={'recorded_utc':datetime.now(timezone.utc).isoformat(),'round':136,'status':'PARTIAL',
   'original_closed':False,'accepted_count_change':0,'independently_reviewed':False,
   'whole_mathematical_argument_root_read':True,'whole_final_tex_separately_root_read':False,
   'all_three_canonical_notes_root_read':True,'whole_canonical_ledger_root_read':True,
   'source_and_result_application_fields_root_read':True,
   'files':[{'path':str(D/f),'source_path':str(W/f),'sha256':sha(D/f),'source_sha256':sha(W/f)} for f in ['P19.2-argument.md','P19.2-paper.tex','P19.2-paper.pdf','status.json']],
   'original_campaign_input':{'path':str(C/'input.json'),'sha256':sha(C/'input.json'),'bytes':(C/'input.json').stat().st_size},
   'native_adapter_input':{'sha256':sha(W/'input.json'),'bytes':(W/'input.json').stat().st_size},
   'input_semantic_equality_verified':True,'input_byte_difference_reason':'JSON serialization only; the decoded full task and assignment values are identical.',
   'native_final_log_sha256':sha(W/'P19.2-paper.log'),'overfull':log.count('Overfull'),'underfull':log.count('Underfull'),'undefined':log.count('undefined'),'warnings':log.count('Warning'),
   'pages':pages,'actual_visual_pages':[],'native_editor_compile_success_observed':False,'existing_editor_unchanged':True,
   'scope':'Original P19.2 partial: usual-datum energy/entropy recovery and interior P levels; endpoints, singular starts and full residual log-discrepancy-model signature remain open.'}
assert b['overfull']==b['undefined']==b['warnings']==0
(D/'publication-binding.json').write_text(json.dumps(b,indent=2)+'\n')
visual=[1,(pages+1)//2,pages]
for n in visual: subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1500','-png','-singlefile',str(pdf),str(D/f'page-{n}-LOCALONLY')],check=True,capture_output=True)
print(json.dumps({'reader':str(D),'pages':pages,'prepared_visual_pages':visual,'whole_MD_and_ledger_root_read':True,'input_semantic_equality':True,'layout_diagnostics':[b['overfull'],b['underfull'],b['undefined'],b['warnings']]},indent=2))
