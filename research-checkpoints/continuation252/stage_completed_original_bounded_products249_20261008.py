from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,shutil

R=Path('/workspace/research');K=R/'root-checks';C=next((R/'campaigns/round-249').iterdir())
A=C/'artifacts/codex-wVmwFP';D=K/'public-P12.4-continuation345-supported-Cartier-products-and-bounded-locality-original-candidate'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists()
actual=K/'round249-actual-native-final.json';final=json.loads(actual.read_text());assert final['candidate'] and len(final['notes'])==9
author_input=json.loads((A/'input.json').read_text());controller_input=json.loads((C/'input.json').read_text());assert author_input==controller_input
audit=json.loads((A/'reports/input-audit.json').read_text());input_checks=[]
for e in audit['files']:
    checks=[]
    for key in ['path','local_path']:
        p=Path(e[key]);checks.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),match=p.stat().st_size==e['bytes'] and sha(p)==e['sha256']))
    assert all(x['match'] for x in checks);input_checks.extend(checks)
assert len(audit['files'])==54 and len(input_checks)==108
own=json.loads((A/'reports/final-audit.json').read_text())['own_files'];own_checks=[]
for e in own:
    p=A/e['file'];assert p.stat().st_size==e['bytes'] and sha(p)==e['sha256'];own_checks.append(dict(path=str(p),**e,match=True))
assert len(own_checks)==15
origin=(A/'P12.4-paper.tex').read_text()
for i in range(1,10): assert (A/f'n{i}.tex').read_text().strip() in origin
G=K/'public-P12.2-continuation331-geometric-primary-model-and-full-conductor-original-candidate'
grant_names=['P12.2-paper.tex','mandatory-source-scope-and-reader-qualifications-after-review240-20261008.json','source-application-ledger.md','exact-scope.md']
for i,n in enumerate(grant_names): assert sha(A/'attachments'/(f'{i:02d}-'+n))==sha(G/n)
supplied_original=json.loads((C/'original-task.json').read_text())['problem']
assert (A/'original-task-statement.txt').read_text().rstrip()==supplied_original.rstrip()
assert json.loads((A/'original-task.json').read_text())==controller_input['task']
D.mkdir();(D/'inert-author-programs-DATA').mkdir();(D/'evidence').mkdir();(D/'attachments').mkdir()
for n in ['source-application-ledger.md','exact-scope.md','whole-proof-coverage.md','original-scope-and-noncircularity-decision.md','native-notes.json','original-task-statement.txt','augmented-assignment.txt','original-task.json','input.json','bounded-evidence-input.json']+[f'n{i}.tex' for i in range(1,10)]:shutil.copyfile(A/n,D/n)
shutil.copyfile(A/'P12.4-paper.tex',D/'native-origin-P12.4-paper.tex');shutil.copyfile(actual,D/'actual-native-FINAL.json');shutil.copyfile(C/'original-task.json',D/'ROOT-exact-original-task.json')
for p in (A/'attachments').iterdir():assert p.suffix in ['.json','.md','.tex'];shutil.copyfile(p,D/'attachments'/p.name)
for n in ['input-audit.json','final-audit.json','exact-diagnostics.json','primary-image-log.json','rerun-commands.json']:shutil.copyfile(A/'reports'/n,D/'evidence'/n)
for n in ['audit_inputs.py','build_delivery.py','exact_diagnostics.py','final_audit.py','inspect_primary.py']:shutil.copyfile(A/n,D/'inert-author-programs-DATA'/n)
pattern=re.compile(r'\\VerbatimInput\[breaklines,fontsize=\\tiny\]\{(attachments/[^}]+)\}')
embedded=[]
def embed(m):
    p=A/m.group(1);s=p.read_text();assert '\\end{Verbatim}' not in s;embedded.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),verbatim_body_unchanged=True))
    return '\\begin{Verbatim}[breaklines,fontsize=\\tiny]\n'+s+('' if s.endswith('\n') else '\n')+'\\end{Verbatim}'
reader=pattern.sub(embed,origin);assert len(embedded)==4 and '\\VerbatimInput' not in reader
reader=reader.replace('\\usepackage[T1]{fontenc}','\\usepackage{fontspec}\n\\setmainfont{DejaVu Serif}\n\\setmonofont{DejaVu Sans Mono}')
(D/'P12.4-paper.tex').write_text(reader)
expanded=json.loads((A/'native-notes.json').read_text());expanded_notes=expanded['notes'] if isinstance(expanded,dict) else expanded
assert [n['id'] for n in expanded_notes]==[n['id'] for n in final['notes']]
matrix=[dict(id=a['id'],actual_text_bytes=len(a['text'].encode()),actual_text_sha256=hashlib.sha256(a['text'].encode()).hexdigest(),expanded_text_bytes=len(b['text'].encode()),expanded_text_sha256=hashlib.sha256(b['text'].encode()).hexdigest(),text_identical=a['text']==b['text']) for a,b in zip(final['notes'],expanded_notes)]
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),round=249,continuation=345,status='UNREVIEWED WHOLE ORIGINAL P12.4 candidate; counts unchanged',candidate=True,only_grants=['Entire qualifiedG331'],ROOT_whole_reading='All9actualFINAL summary/detailed/text/support fields in groups1--3,4--6,7--9; entire native58826BTeX physically read by character chunks0:20500,19900:40000,39400:end; whole10516Bsourceledger,scope,coverage,decision read. Four entire G331 appendix components were previously fully read as qualifiedgrant, not a new physical144kreader claim.',source_native_origin=dict(path=str(A/'P12.4-paper.tex'),bytes=(A/'P12.4-paper.tex').stat().st_size,sha256=sha(A/'P12.4-paper.tex')),publication_reader=dict(path=str(D/'P12.4-paper.tex'),bytes=(D/'P12.4-paper.tex').stat().st_size,sha256=sha(D/'P12.4-paper.tex'),changes='Only four external VerbatimInput appendix bodies inlined byte-identically and Unicode-capable font declarations; no mathematical proof change.'),embedded_grant_components=embedded,own15_current_physical_checks=own_checks,author54_current_origin_and_local_body_checks=input_checks,controller_and_native_input_decoded_equal=True,actual_vs_expanded_note_prose=matrix,original_task_label_qualification='Native original-task.json is the full augmented suppliedtask, decoded equal to controller task; ROOT-exact-original-task.json and native original-task-statement.txt preserve unchanged original+fullfamily separately.',source_pixels_freshly_ROOT_viewed=False,author_source_pixel_claims_recorded_as_author_only=True,author_programs_executed_by_ROOT=False,compiler_status='NOT YET VERIFIED; unrelated343 builtincompile still pending, no concurrent compiler requested',original_closed=False,new_paper_accepted=False,private_ACTIVE250_output_read_or_supplied=False,protected_P16_editor_unchanged_open=True,source_bodies_and_images_LOCALONLY=True)
write(D/'ROOT-whole-reading-and-binding-20261008.json',record)
(D/'ROOT-README.md').write_text('Complete originalP12.4 candidate from native249, UNREVIEWED.13/42 originals solved;29OPEN;94acceptedpapers, no new acceptance here. All9actualFINAL fields, entire nativepaper and source/scope/coverage/decision ROOT read.15owncurrent bindings and54origin/local input pairs independently match. Nativeorigin and allauthorbodies remain unchanged. Publicationreader only inlines4complete unchanged qualifiedG331 appendix components and uses Unicodefonts; compiledsuccess notyetverified. Exactoriginaltask is separately preserved; nativeoriginal-task.json is augmentedtask, as binding explains. Independent whole-original review required before closure. Sourcepages,pixels and privateprovider/controlleroutput remainLOCALONLY. No source or author program execution. ProtectedP16editor OPENUNCHANGED.\n')
print(json.dumps(dict(continuation=345,native_origin_sha256=sha(A/'P12.4-paper.tex'),reader_bytes=(D/'P12.4-paper.tex').stat().st_size,reader_sha256=sha(D/'P12.4-paper.tex'),own_bindings=len(own_checks),input_body_checks=len(input_checks),original_closed=False),indent=2))
