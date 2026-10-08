from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,shutil

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-265/P12.3-whole370-and-test-ideal371-independent-completion';A=C/'artifacts/codex-UXzJUG'
D=K/'public-P12.3-continuation376-perfect-characteristic-smooth-primary-envelope-whole-candidate'
P=R/'primary-data-LOCALONLY/P12.3-native265-whole-primary-and-evidence-20261008'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not P.exists()
actual=K/'round265-actual-native-final.json';assert sha(actual)=='c3354bfcbb4a8b61e8d7d9b5ed142c2f35d6ed70efcd28e5db7c342d22fff26b'
returned=load(actual);expanded=load(A/'native-notes.json');assert not returned['candidate'] and not expanded['candidate'] and len(returned['notes'])==len(expanded['notes'])==10
core=(A/'whole-proof.md').read_text(); paper=(A/'P12.3-paper.md').read_text();tex=(A/'P12.3-paper.tex').read_text()
for n in expanded['notes']:assert n['text'] in core and (A/(n['id']+'.md')).read_text()==n['text']
assert all(a['text']!=b['text'] for a,b in zip(returned['notes'],expanded['notes']))
records=['source-application-ledger.md','exact-scope.md','whole-proof-coverage.md','original-scope-and-noncircularity.md','source-search-decision.md']
expected=core+'\n\n'+'\n\n'.join((A/n).read_text() for n in records)+'\n\n# Own original-scope decision\n\n```json\n'+(A/'acceptance-decision.json').read_text()+'```\n'
grants={n['id']:n['text'] for n in load(C/'input.json')['notes']};assert set(grants)=={'G331','B341','E350'}
for g in ['G331','B341','E350']:
    assert (A/'inputs'/('qualified-'+g+'.txt')).read_text()==grants[g]
    expected+='\n\n# Entire qualified correctness grant '+g+'\n\n'+grants[g]
assert paper==expected
special={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}','≤':r'\ensuremath{\leq}','≥':r'\ensuremath{\geq}','∞':r'\ensuremath{\infty}','→':r'\ensuremath{\to}','∈':r'\ensuremath{\in}','Σ':r'\ensuremath{\Sigma}','Γ':r'\ensuremath{\Gamma}','μ':r'\ensuremath{\mu}','τ':r'\ensuremath{\tau}','φ':r'\ensuremath{\phi}','λ':r'\ensuremath{\lambda}','κ':r'\ensuremath{\kappa}','π':r'\ensuremath{\pi}','×':r'\ensuremath{\times}','−':r'\ensuremath{-}','–':'--','—':'---','’':"'",'‘':"'",'“':'``','”':"''"}
def encoded_paragraphs(s):
    out=[]
    def esc(t):return ''.join(special.get(c,c) for c in t)
    for para in s.split('\n\n'):
        if para.startswith('# '):out.append(r'\section{'+esc(para[2:].replace('\n',' '))+'}')
        elif para.startswith('## '):out.append(r'\subsection{'+esc(para[3:].replace('\n',' '))+'}')
        else:out.append(esc(para.replace('\n',' ')))
    return '\n\n'.join(out)
body=encoded_paragraphs(core)
for n in records:body+='\n\n'+encoded_paragraphs((A/n).read_text())
body+='\n'+r'\section{Own original-scope decision}'+'\n'+r'\begin{ImportedGrantText}'+'\n'+(A/'acceptance-decision.json').read_text()+'\n'+r'\end{ImportedGrantText}'+'\n'
for g in ['G331','B341','E350']:body+='\n'+r'\section{Entire qualified correctness grant '+g+'}'+'\n'+r'\begin{ImportedGrantText}'+'\n'+grants[g]+'\n'+r'\end{ImportedGrantText}'+'\n'
body+='\n'+r'\end{document}'+'\n'
assert tex.split('\\tableofcontents\n',1)[1]==body
assert sha(C/'original-task.json')=='d524b816c1462a6909a85bd0e39b84ab34ca04be27ec99eccbfde7ffcc0316a8'
D.mkdir();P.mkdir();shutil.copytree(A/'inputs',P/'inputs');shutil.copytree(A/'review-data',P/'review-data');shutil.copytree(A/'evidence',P/'evidence')
for n in ['P12.3-paper.tex','P12.3-paper.md','whole-proof.md','native-notes.json','acceptance-decision.json','README.md']+records:shutil.copyfile(A/n,D/n)
shutil.copyfile(actual,D/'actual-settled-native265-FINAL.json');shutil.copyfile(C/'original-task.json',D/'original-task.json')
for n in returned['notes']:(D/(n['id']+'-actual-settled.md')).write_text(n['text'])
for n in expanded['notes']:shutil.copyfile(A/(n['id']+'.md'),D/(n['id']+'-expanded.md'))
Q=D/'native-programs-INERT-DATA';Q.mkdir()
for p in sorted(A.glob('*.py')):shutil.copyfile(p,Q/(p.name+'.DATA.txt'))
for n in ['environment.json','execution-history.json','public-retrieval-status.json','literal-unit-checks.json','duplicate-comparison.json','final-commands-output.json','finite-diagnostics.json','individual-proof-data-duplicates.json','tex-body-identity.json','final-audit.json']:shutil.copyfile(A/'evidence'/n,D/n)
now=datetime.now(timezone.utc).isoformat()
qual=dict(recorded_utc=now,status='UNREVIEWED whole mathematical draft, candidateFALSE; original remains OPEN; no new correctness grant or accepted paper',whole_original_solved=False,new_accepted_paper=False,
    actual_FINAL=dict(path=str(actual),bytes=actual.stat().st_size,sha256=sha(actual),ALL_ten_complete_actual_fields_ROOT_physically_read=True,intermediate_messages_excluded=10),
    expanded_notes=dict(ALL_ten_texts_DIFFER_from_actual_settled=True,each_ENTIRE_text_exact_literal_substring_of_full_physically_read_proof=True,all_expanded_outside_fields_ROOT_physically_read=True,separate_md_files_exact_identical=True,no_duplicate_fresh_physical_reading_claim=True),
    whole_ROOT_reading=dict(entire_new_whole_proof_physically_read=True,entire_source_application_scope_coverage_decision_search_READ=True,bounded_overlapping_untruncated_chunks=True,entire_new_manuscript_body_exact_core_and_fully_read_records=True,ENTIRE649388byte_TeX_mathematical_body_exact_verified_encoding_of_read_material_and_literal_qualified_grants=True,TeX_preamble_ROOT_physically_read=True,whole_large_grant_reproductions_previous_complete_qualified_reading_not_new_physical_reading=True,full_paper_retained_unmodified=True),
    qualified_grants=[dict(id=g,bytes=len(grants[g].encode()),sha256=hashlib.sha256(grants[g].encode()).hexdigest(),entire_literal_input_note_body_in_paper_and_TeX=True) for g in ['G331','B341','E350']],
    source_reading=dict(native265_complete_immediate_units='All applied immediate units in ENTIRE current source ledger attributed native265; ROOT does not infer new physical reading from its claims/hashes',ROOT_previous_complete_primary_reading='Preserved WHOLE370 scopes and wholeROOT371 complete GJKM4/Mustata3+4.1/Keeler1.5+entirev5erratum immediate reading; source bodies retained with unchanged hash; no new fresh whole reading claim',ROOT_new_native265_primary_body_or_PDF_pixels_freshly_read=False,deeper_recursive_foundations_not_freshly_reconstructed=True,full_primary_and_literal_unit_evidence_LOCALONLY=True,private_directory=str(P)),
    new_scope='PERFECT charp, normal integral affine finiteTYPE B, CLOSED x codim>=2, FIXED ACTUAL smooth primaryY=Bl_J isooffx/principalizesgauge. Integral fibreCartier C: actual sectionIDEALS/all-indexFekete, asymptotictestideals and corrected affine-basegeneration yield 0<=p(f_C)-g_m<=c v(J)/m<=cN/m on ALL support quotients BEFORE increasingrecognition/energy.',
    model_gate='SM quantified over EVERY finite primarycollection/gauge implies allCONTCE; provednormal perfect-field surfaces. No universalhigherdim smoothprimarymodel, arbitraryresolution/alteration/smallresolution/cofinality grant.',
    old_scope='Whole generalNORMALexcellent surfaces; isolatedclosedalgclosedchar0 and exactsmoothBFJ; actualdominatingfiniteCEcovers; generalnormalchar0FINITE-Q OPENlocus only; fullconductor finiteCONTpositivedomain; genuineNONNORMAL doubleplanefailure; completecurve geometric/idealclipping; energy/capacity signs and increasingnonDdiagnostics.',
    original_gaps=['General normal excellent dimension>=3 beyond explicit proved sectors','General closednormalalgclosedchar0 infinite d(K)Jac support stratum','Higherdim positive/mixed characteristic without required actual smooth primarymodels','Nonalgebraic/nonclosed excellent residual scope'],
    threefold_literature='CossartPiltant1412.0868v2 displayed1.1/Remark1.4 partlyinspected DATA only; whole320pageproof notread/applied, no primarymodelgrant or impossibility assertion',
    source_limits='GJKM4.6 PROJECTIVEoverAFFINE/perfectcharp exacthypotheses; Mustata4.1 PROJECTIVEalgclosedalone insufficient. FullcorrectedKeelererratum retained, falseold3.3notused. KYonlyONsmoothY; no singularKB-Cartier, Jacobian-error or increasingD-recognition shortcut.',
    compiler='Standalonefontspec/fvextra/DejaVusource retained uncompiled; built-incheck pending after staging. No success or PDFexport claim.',
    supplied_or_native_programs_executed_or_imported=False,protected_editor_open_unchanged=True,other_ACTIVE_math_read_or_supplied=False,hot_feedback_sent=False)
write(D/'mandatory-ROOT-whole-proof-source-scope-qualifications-20261008.json',qual)
B=K/'P12.3-round265-whole-candidate376-ROOT-proof-source-scope-and-binding-20261008.json'
binding=dict(recorded_utc=now,round=265,paper=376,atom='P12.3',public_directory=str(D),private_directory=str(P),whole_original_solved=False,new_accepted_paper=False,counts=dict(solved=16,open=26,papers=97),qualified_whole_reading=qual,public_whole_body_bindings=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file()],private_retention_bindings=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(P.rglob('*')) if p.is_file()]);write(B,binding)
for n in ['active-work.json','checklist-current.json']:
    p=R/n;x=load(p);assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x['native265_complete376']=dict(public_directory=str(D),whole_binding=str(B),whole_binding_sha256=sha(B),actual_FINAL_sha256=sha(actual),candidate=False,original_closed=False,new_accepted_paper=False,independent_whole_reconstruction_pending=True);x['updated_utc']=now;write(p,x)
print(json.dumps(dict(round=265,paper=376,whole_public_files=len(binding['public_whole_body_bindings']),private_retention_files=len(binding['private_retention_bindings']),whole_TeX=dict(bytes=(D/'P12.3-paper.tex').stat().st_size,sha256=sha(D/'P12.3-paper.tex')),whole_proof=dict(bytes=(D/'whole-proof.md').stat().st_size,sha256=sha(D/'whole-proof.md')),whole_binding_sha256=sha(B),candidate=False,new_accepted_paper=False,solved=16,open=26,papers=97),indent=2))
