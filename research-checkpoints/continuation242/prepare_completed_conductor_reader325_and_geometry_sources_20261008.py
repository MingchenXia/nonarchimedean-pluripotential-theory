from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R=Path('/workspace/research'); K=R/'root-checks'
C=next((R/'campaigns/round-236').iterdir()); A=C/'artifacts/codex-JPhTWn'
D=K/'public-P12.2-continuation325-full-ideal-conductor-and-smooth-reconstruction-unreviewed'
Q=R/'primary-data-LOCALONLY/P12.2-relative-geometry-20261008'
B=K/'round236-whole-draft-ROOT-reading-and-relative-geometry-continuation-binding-20261008.json'
M=K/'P12.2-relative-geometry-primary-acquisition-and-ROOT-reading-metadata-20261008.json'
W=K/'P12.2-continuation326-relative-geometry-and-real-Cartier-ample-perturbation-working-proof-20261008.md'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,x):Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists()for p in[D,B,M])
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
x=json.loads((K/'round236-actual-native-final.json').read_text());assert not x['candidate'] and len(x['notes'])==11
known=set()
for n in x['notes']:assert n['id']not in known and all(s in known for s in n['support']);known.add(n['id'])
o=json.loads((A/'reports/own-hashes.json').read_text());assert len(o)==73
for e in o:
    p=A/e['path'];assert p.is_relative_to(A) and p.stat().st_size==e['bytes'] and sha(p)==e['sha256']
i=json.loads((A/'reports/input-hashes.json').read_text());assert len(i)==47
for e in i:
    p=Path(e['path']);assert sha(p)==e['sha256'] and ('bytes'not in e or p.stat().st_size==e['bytes'])
frozen=[]
for name in['mathematical-packet-bindings.json','private-primary-packet-bindings.json']:
    for e in json.loads((C/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes'];frozen.append(e)
assert len(frozen)==42
assert sha(A/'P12.2-paper.tex')=='2103a120ad750bc5b21f2fe3173fdca1d456a46daf8b8f1462a5af8f43f9455f'
assert sha(A/'P12.2-paper.pdf')=='c9bf871825d6c9a4db9d7127a11134a33bd062b49aaa72daecce484ce400a63e'
now=datetime.now(timezone.utc).isoformat()
write(B,dict(recorded_utc=now,round=236,candidate=False,actual_FINAL_path=str(K/'round236-actual-native-final.json'),actual_FINAL_sha256=sha(K/'round236-actual-native-final.json'),whole_eleven_actual_notes_ROOT_read=True,whole_authoritative_paper_ROOT_read=True,paper_display_ranges=['1-100','101-190','191-280','281-370','371-460'],paper_LF_lines=444,source_sha256=sha(A/'P12.2-paper.tex'),pdf_sha256=sha(A/'P12.2-paper.pdf'),pdf_pages=20,source_ledger_scope_coverage_decision_ROOT_read=True,expanded_argument_separate_n_and_native_notes_whole_ROOT_read_not_claimed=True,expanded_native_notes_distinct_from_actual_FINAL=True,own_artifact_hashes_verified=73,input_hash_records_verified=47,frozen_math_and_primary_hashes_verified=42,supplied_programs_not_executed_or_imported=True,mathematical_or_source_acceptance=False,new_accepted_paper=False,original_closed=False,remaining_gate='G1-G3 complete immediate relative geometry primary units; not the reconstructed ideal-level unbounded mixed-zero conductor descent',new_ROOT326_is_separate_unreviewed_DATA=True,active237_private_outputs_not_read=True))
units={
 'Stacks-0B5S':'Complete local text LF1-67, especially all immediate statements/proofs of30.16.1 and30.16.3.',
 'Stacks-0D2N':'Complete local text LF1-42: full immediate30.21.4 statement/proof; cited formal-functions and immersion dependencies disclosed, not recursively all read.',
 'Stacks-01PR':'Complete28.27.2 statement/proof LF20-24 and28.27.5 statement/proof LF34-42 within local reads13-47; complete28.27.13 statement/proof in LF70-116. Earlier official web read also displayed definition and full unit.',
 'Stacks-01XO':'Complete30.17.5 statement/proof local TXT LF55-71. Full section not claimed read.',
 'Stacks-01VG':'Entire local text LF1-104 including29.38.1/4/5 full immediate units and their proofs.',
 'Keeler-ample-filters-corrected-v5':'Local pdftotext-layout LF50-135 (including whole1.5 statement),210-286 (including2.9 and2.13/14),824-888 (whole4.9/4.10 and proofs),1220-1288 (whole1.5 immediate proof and5.19 immediate unit),1780-1845,1846-1959,1960-2080 (ENTIRE appended erratum). Exactv5 corrects false3.3 viaE1.3/E2.4/E2.5. No whole40-page source read or recursive historical dependency certification claimed.'}
sources=[]
for stem in['Stacks-0B5S','Stacks-0D2N','Stacks-01PR','Stacks-01XO','Stacks-01VG','Keeler-ample-filters-corrected-v5']:
    url='https://arxiv.org/pdf/math/0108068v5' if stem.startswith('Keeler') else 'https://stacks.math.columbia.edu/tag/'+stem.split('-')[1]
    for ext in(['pdf','txt']if stem.startswith('Keeler')else['html','txt']):
        p=Q/(stem+'.'+ext);assert p.is_file()
        sources.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),url=url,kind='original primary data'if ext!='txt'else'local text derivative; never executed as code',LOCALONLY=True,correctness_grant=False,complete_immediate_ROOT_reading=units[stem]))
write(M,dict(recorded_utc=now,source_files=sources,source_units_ROOT_read=units,full_source_documents_ROOT_read_not_claimed=True,PDF_formulas_not_separately_pixel_checked=True,Keeler_exact_version='arXiv math/0108068v5;2June2018;PDF40pages;PDFmetadataNov8,2018; originalJAlgebra259(2003)243-283;corrigendum507(2018)592-598',Keeler_original_lemma3_3_false=True,corrected_E1_3_and_E2_5_entire_proofs_read=True,Theorem1_5_survives_erratum=True,new_working_proof=dict(path=str(W),bytes=W.stat().st_size,sha256=sha(W),whole_ROOT_filesystem_read=True,unreviewed=True),ordinary_published_applications_with_disclosed_historical_dependencies=True,source_or_mathematical_grant=False,original_closed=False,primary_HTML_scripts_not_executed=True,missing_bs4_conversion_attempt_failed_without_installation=True,successful_conversion_uses_standard_HTMLParser_DATA_only=True))
D.mkdir();(D/'evidence').mkdir()
for name in['P12.2-paper.tex','P12.2-paper.pdf','argument.md','source-application-ledger.md','exact-scope.md','whole-proof-coverage.md','original-scope-decision.md','native-notes.json']:
    shutil.copyfile(A/name,D/name)
for p in sorted(A.glob('n[0-9]*.md')):shutil.copyfile(p,D/p.name)
for p in sorted((A/'reports').rglob('*')):
    if p.is_file() and p.suffix in['.json','.md','.txt','.log']:
        q=D/'evidence'/p.relative_to(A/'reports');q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
for p in[B,K/'round236-actual-native-final.json']:shutil.copyfile(p,D/'evidence'/p.name)
write(D/'ROOT-public-draft-status-20261008.json',dict(recorded_utc=now,continuation=325,native_round=236,original_status='OPEN',candidate=False,whole_ROOT_TeX_and_eleven_actual_FINAL_notes_read=True,source_scope_coverage_decision_read=True,own_hashes_verified=73,frozen_hashes_verified=42,author_source_and_20_page_PDF_unchanged=True,author_builds_checks_not_ROOT_executions=True,built_in_compiler_status='not requested at staging',expanded_saved_notes_distinct_from_actual_FINAL=True,new_accepted_paper=False,original_closed=False,protected_P16_editor_unchanged_open=True))
(D/'ROOT-README.md').write_text('UNREVIEWED native236 continuation325:20-page P12.2 reconstruction.\n\nOriginal remains OPEN;10/42originals solved,32OPEN,88accepted papers. The whole444LF authoritative TeX and alleleven actualFINAL notes, source/scope/coverage/decision were ROOT-read.73own and42frozen file hashes verified; authorchecks were not ROOTexecutions or mathematics/sourcePASS. Expanded native-notes.json differs from the actualFINAL and is separately preserved.\n\nThe paper reconstructs full bounded and unbounded/mixed-zero finite-injection ideal-conductor descent, including bottom and nonminimal supports, and full smooth BFJ on ALLsemivaluations. Its independently geometric Cartier=ideal comparison remains CONDITIONAL on G1-G3 exact relative-geometry primary units. NEW ROOT326 and newly acquired correctedKeeler/Stacks sources address this gate separately as UNREVIEWED DATA, without retroactively altering this paper. The entire appended2018erratum of exactKeelerv5 was read. Full external primary source bodies/extracts/images remainLOCALONLY. ProtectedP16.4editor staysopenunchanged. Independent wholeoriginal reconstruction and subsequent review remain necessary.\n')
print(json.dumps(dict(public_reader=str(D),reading_binding=str(B),primary_metadata=str(M),new_primary_files=len(sources),original_solved=10,original_open=32,accepted_papers=88),indent=2))
