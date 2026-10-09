from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
R=Path('/workspace/research'); K=R/'root-checks'
A=R/'campaigns/round-275/P16.7-whole390388389-general-E1-operator/artifacts/codex-yAYOpu'
Raw=K/'round275-raw-native-final-REJECTED-support.json'
F=R/'primary-data-LOCALONLY/P16.7-native264-whole-primary-and-retrieval-evidence-20261008/sources/CLD-v2-whole.txt'
U=R/'primary-data-LOCALONLY/P16.7-native275-corrected-CLD-LF-units-20261009'
Q=K/'round275-ROOT-whole-content-and-CLD-LF-unit-correction-audit-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
assert not U.exists() and not Q.exists()
assert sha(F)=='64846cb00926267c6238d1afac61b5eaed0a0e3a6349725738f9b1bf163de085'
r=load(Raw); n=load(A/'final-notes.json'); assert r==n and not r['candidate'] and len(r['notes'])==5
assert (A/'final-notes.json').stat().st_size==Raw.stat().st_size+1
assert list(r['notes'][0])!=list(n['notes'][0])
meta=load(A/'note-metadata.json'); assert len(meta)==5
for note,row in zip(n['notes'],meta):
    assert {k:v for k,v in note.items() if k!='text'}==row
    assert note['text']==(A/(note['id']+'.md')).read_text()
ledger=(A/'source-application-ledger.md').read_text(); companion=(A/'proof-companion.md').read_text()
head='# Generated finite-energy analytic operators on the concrete quotient\n\nUnverified scoped proof draft. Original P16.7 incomplete.\n\n'
assert companion==head+'\n\n'.join(note['text'] for note in n['notes'])+'\n\n'+ledger
# Independent own literal encoding; never import or execute native assembler.
table={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
def esc(s):return ''.join(table.get(c,c) for c in s)
body='\n'.join(r'\section*{'+esc(line[2:])+'}' if line.startswith('# ') else esc(line) for line in companion.splitlines())
tex=(A/'generated-E1-paper.tex').read_text(); start=tex.index(body); prefix=tex[:start];suffix=tex[start+len(body):]
assert suffix=='\n\\end{document}\n' and prefix.endswith('proofs, declared foundations, audit limitations and reproduction evidence.\n')
print('ENTIRE UNIQUE TEX PREAMBLE\n'+prefix+'ENTIRE UNIQUE TEX SUFFIX\n'+suffix)
U.mkdir(); lines=F.read_text().split('\n'); legacy=F.read_text().splitlines(keepends=True); units=[]
for lo,hi,scope in [(9724,9980,'Entire8.1.1-13 and8.2.1-4 including all applied continuouspsh definitions/convexity and immediate proofs'),(10249,10609,'Entire8.5.1/3/5;8.7.1/2/4;8.8.4/5 statements and immediate proofs with surrounding context, continuous multiplier8.6.7 NOT premise'),(6990,7024,'Entire5.11.1 Stokes/Green and immediate proof'),(7978,8088,'Entire7.2.8,7.2.11-13 statements/immediate proofs; read7.2.9 generalstrong-orderunit NOT premise'),(22100,22148,'Entire15.7.1 and immediate proof/15.7.2 context')]:
    p=U/f'CLDv2-real-LF-{lo}-{hi}-LOCALONLY.txt';p.write_text('\n'.join(lines[lo-1:hi])+'\n')
    units.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),source=str(F),source_sha256=sha(F),literal_LF_inclusive=[lo,hi],line_convention="split('\\n') / sed / rg -n; preserves embedded FF as page separator inside line",scope=scope,ROOT_entire_actual_source_range_physically_read_untruncated=True,PRIMARY_pixels_NOT_newly_read=True,deep_recursive_foundations_NOT_all_newly_read=True,LOCALONLY=True))
legacy_units=[]
for lo,hi in [(9724,9864),(9885,9980),(10249,10490),(10494,10574),(6990,7024)]:
    p=R/'primary-data-LOCALONLY/P16.7-ROOT388-bounded-Green-source-units-20261009'/f'ROOT388-CLDv2-full-LF{lo}-{hi}-LOCALONLY.txt'
    assert p.read_text()==''.join(legacy[lo-1:hi])
    legacy_units.append(dict(path=str(p),sha256=sha(p),declared_LF_inclusive=[lo,hi],actual_extractor='Python splitlines(keepends=True), which also counts FF separators',wrong_theorem_content_descriptor=True,not_same_as_literal_LF_source_range=True))
artifacts=[]
for p in sorted(A.rglob('*')):
    if p.is_file():artifacts.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),native_programs_inert=True))
record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),terminal_status='XeanBLOCKED: unknown support string in n2; no retry/import/grant/acceptance',actual_FINAL=dict(path=str(Raw),bytes=Raw.stat().st_size,sha256=sha(Raw),all_FIVE_complete_fields_physically_read_untruncated=True),artifact_final_notes=dict(path=str(A/'final-notes.json'),bytes=(A/'final-notes.json').stat().st_size,sha256=sha(A/'final-notes.json'),semantically_identical_entire_JSON=True,byte_distinction='Note key order differs and artifact has terminal newline; size +1 does NOT mean raw+newline identity',NOT_different_expanded_bodies=True),companion=dict(path=str(A/'proof-companion.md'),bytes=(A/'proof-companion.md').stat().st_size,sha256=sha(A/'proof-companion.md'),exact_entire_FIVE_actual_bodies_plus_entire_ledger=True,duplicate_identity_NOT_extra_physical_reading=True),ledger=dict(path=str(A/'source-application-ledger.md'),bytes=len(ledger.encode()),sha256=sha(A/'source-application-ledger.md'),entire_physically_read=True),TeX=dict(path=str(A/'generated-E1-paper.tex'),bytes=(A/'generated-E1-paper.tex').stat().st_size,sha256=sha(A/'generated-E1-paper.tex'),entire_literal_companion_encoding_independently_verified=True,unique_prefix_and_suffix_physically_read_in_this_audit_output=True,compiled=False),fresh_correct_full_primary_units=units,historical_ROOT388_unit_extractor_error=legacy_units,correction='ROOT388 full-source LF descriptions matched intended literal-LF ranges, but its extractor used splitlines and counted FF page separators, producing other bodies. Old immutable record retained. These correct literal-LF units and fresh full physical source reads supersede its content descriptors/reading linkage, not its proof conclusions. Native275 n5 diagnoses content mismatch; this record identifies concrete cause.',source_boundary='Applied source statements/immediate proof units fully read. FullCLD/geometry/Ducros recursive background/book papers not all fresh whole audited. No inference from identity to correctness. Generalstrong-orderunit/continuousmultiplierclosedness/equalityC1=allP NOT premises.',native_artifact_metadata=artifacts,new_math_scope='All-direction GENERATED E1 bounded-limit MA/mixed operator, finite dual, analytic firstvariation, comparison/maximum locality/exactclamps: UNREVIEWED. Intrinsicrecognition/compactness/envelopes/arbitrary-measure existence/fulluniqueness OPEN.',all_full_primary_bodies_literal_units_pixels_book_context_LOCALONLY=True,supplied_or_native_programs_executed_or_imported=False,other_ACTIVE_math_read_or_hot_feedback=False,original_closed=False,accepted=False,new_correctness_grant=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97))
Q.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(audit=str(Q),audit_sha256=sha(Q),raw_bytes=Raw.stat().st_size,companion_bytes=(A/'proof-companion.md').stat().st_size,TeX_bytes=(A/'generated-E1-paper.tex').stat().st_size,correct_full_primary_units=len(units),no_new_correctness_grant=True),indent=2))
