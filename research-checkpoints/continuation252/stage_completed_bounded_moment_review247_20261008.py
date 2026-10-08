from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,re

R=Path('/workspace/research');K=R/'root-checks'
C=next((R/'campaigns/round-247').iterdir());A=C/'artifacts/codex-FkNfZB'
D=K/'public-P12.4-continuation343-independent-bounded-moment-supporting-paper-unreviewed'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def entry(p):p=Path(p);return dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p))
assert not D.exists()
own=json.loads((A/'evidence/own-artifact-hashes.json').read_text());inputs=json.loads((A/'evidence/input-audit.json').read_text())
assert len(own)==34 and len(inputs)==31
for e in own:
    p=A/e['path'];assert sha(p)==e['sha256'] and p.stat().st_size==e['bytes']
for e in inputs:
    p=Path(e['path']);assert sha(p)==e['sha256'] and p.stat().st_size==e['bytes']
tex=(A/'P12.4-bounded-moment-paper.tex').read_text();core_end=tex.index('\\appendix')
blocks=re.findall(r'\\begin\{Verbatim\}\[[^\n]*\]\n(.*?)\\end\{Verbatim\}',tex[core_end:],re.S)
grants=sorted((A/'inputs/G331').iterdir());assert len(grants)==5 and len(blocks)==6
for block,p in zip(blocks[:5],grants):assert block.strip()==p.read_text().strip()
assert blocks[5].strip()==(A/'whole-source-application-ledger.md').read_text().strip()
current=json.loads((C/'input.json').read_text());native=json.loads((A/'input.json').read_text());assert current==native and [n['id'] for n in current['notes']]==['G331']
actual=json.loads((K/'round247-actual-native-final.json').read_text());expanded=json.loads((A/'native-notes.json').read_text());assert len(actual['notes'])==len(expanded['notes'])==8 and actual['candidate']==expanded['candidate']==False
matrix=[{key:u[key]==v[key] for key in ['id','summary','detailedSummary','text','support']} for u,v in zip(actual['notes'],expanded['notes'])]
D.mkdir();E=D/'evidence';E.mkdir();I=D/'inert-reviewer-programs-DATA';I.mkdir()
for name in ['P12.4-bounded-moment-paper.tex','independent-review.md','whole-proof.md','whole-source-application-ledger.md','whole-proof-coverage.md','original-scope-and-noncircularity.md','acceptance-decision.json','native-notes.json']:shutil.copyfile(A/name,D/name)
for name in ['environment.json','execution-commands.md','final-audit.json','finite-diagnostics.json','input-audit.json','local-task-input.json','own-artifact-hashes.json','page-inspection-commands.json']:shutil.copyfile(A/'evidence'/name,E/name)
for name in ['audit_inputs.py','inspect_primary.py','finite_diagnostics.py','build_delivery.py','final_audit.py']:shutil.copyfile(A/name,I/name)
for name in ['failed-finite-diagnostics-early-window.py','failed-finite-diagnostics-early-window.txt']:
    p=A/'evidence'/name;assert p.exists();shutil.copyfile(p,E/name)
shutil.copyfile(K/'round247-actual-native-final.json',D/'actual-native-FINAL.json');shutil.copyfile(C/'original-task.json',D/'exact-original-task.json')
G=D/'qualified-G331';G.mkdir()
for p in grants:shutil.copyfile(p,G/p.name)
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=247,continuation=343,status='UNREVIEWED standalone supporting paper; originalOPEN',original_closed=False,paper_accepted=False,source=entry(D/'P12.4-bounded-moment-paper.tex'),
    ROOT_every_actual_FINAL_field_and_entire_independent_proof_source_scope_read=True,whole_proof_chunks='0:17000 and17000:end; entire source ledger,coverage,independent review,scope and decision.',
    ROOT_new_TeX_core_physically_read=True,new_core_chars=core_end,new_core_read_chunks='0:16000 and16000:38580',
    full_TeX_appendices_freshly_physically_reread=False,appendix_reading='Five completeG331 components were previously wholeROOT read as qualifiedgrant; current6literalappendix bodies independently checked exactly against those5components and the freshly entire-read source ledger. No new whole144kphysical reread claim.',
    all_current_own_and_input_bindings_match=True,own_records=34,input_bodies=31,current_native_whole_inputs_equal=True,actual_expanded_whole_equal=actual==expanded,actual_expanded_fields_equal=matrix,
    paper_literal_G331_appendices_match=True,source_ledger_literal_appendix_matches=True,primary_bodies_extracts_pixels_private_provider_output_not_copied=True,supplied_programs_ROOT_executed_or_imported=False,
    original_candidate=False,counts_unchanged=dict(solved=13,open=29,papers=93),protected_editor_open_unchanged=True)
(D/'ROOT-whole-reading-and-binding-20261008.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
(D/'ROOT-README.md').write_text('UNREVIEWED native247 standalone algebraic supporting paper. Entire new proofs and source/scopeROOT read; new38kTeX core physically read; full qualifiedG331 attachments previouslywholeROOT read and checked literally unchanged, not claimed freshly physical144k reread. Current34own/31input bindings match. Builtincompilation pending. EntireoriginalP12.4stillOPEN: thispaper supplies no generalCartiercomparison/locality. NewROOT342is separateunreviewedDATA and was not supplied to247.13solved29OPEN93acceptedunchanged. ProtectedP16.4editorOPENUNCHANGED. Primaryacademicbodies/extracts/pixelsandprivateprovideroutputstayLOCALONLY; reviewerprogramsinertDATAonly.\n')
print(json.dumps(dict(directory=str(D),source_sha256=sha(D/'P12.4-bounded-moment-paper.tex'),new_core_chars=core_end,checked_own=len(own),checked_inputs=len(inputs),counts_changed=False),indent=2))
