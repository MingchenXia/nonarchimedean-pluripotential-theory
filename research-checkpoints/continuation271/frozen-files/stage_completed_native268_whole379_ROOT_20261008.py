from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,shutil

R=Path('/workspace/research');K=R/'root-checks'
C=R/'campaigns/round-268/P21.3-whole372-and-original-arbitrary-BT-current'
A=C/'artifacts/codex-2gyFKH'
D=K/'public-P21.3-continuation379-middle-cone-analytic-trace-and-original-BT-whole-candidate'
P=R/'primary-data-LOCALONLY/P21.3-native268-whole-primary-and-evidence-20261008'
B=K/'P21.3-round268-whole-candidate379-ROOT-proof-source-scope-and-binding-20261008.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not P.exists() and not B.exists()
actual=K/'round268-actual-native-final.json';assert sha(actual)=='6f1cc1e1fee173caa9ffd4c845349c5e775ac61ebec93078d3de806fbcbd2d3b'
j=load(actual);e=load(A/'actual-mathematical-notes.json');src=load(A/'source-ledger-independent.json')
assert not j['candidate'] and not e['candidate'] and len(j['notes'])==len(e['notes'])==4
assert (A/'final.json').read_bytes()==(A/'actual-mathematical-notes.json').read_bytes()
proof=(A/'P21.3-proof-companion.md').read_text();tex=(A/'P21.3-review-paper.tex').read_text();ledger=(A/'source-ledger-independent.md').read_text()
assert len(proof)==65250 and proof.endswith(ledger)
comparisons=[]
for x,y in zip(j['notes'],e['notes']):
    assert x['id']==y['id'] and x['text']!=y['text']
    assert y['text'] in proof and (A/(y['id']+'.md')).read_text()==y['text']
    comparisons.append(dict(id=x['id'],actual_text_sha256=hashlib.sha256(x['text'].encode()).hexdigest(),expanded_text_sha256=hashlib.sha256(y['text'].encode()).hexdigest(),actual_DIFFERS_expanded=True,expanded_entire_literal_proof_substring=True))
intro=proof.split('\n\n',1)[1].split(e['notes'][0]['text'],1)[0]
assert intro.endswith('\n\n');intro=intro[:-2]
special={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
def esc(s):return ''.join(special.get(c,c) for c in s)
def prose(s):return ''.join(c if c.startswith((r'\(',r'\[')) else esc(c) for c in re.split(r'(\\\(.*?\\\)|\\\[.*?\\\])',s,flags=re.S))
def section(s):
    lines=s.splitlines();return r'\section{'+esc(lines[0].removeprefix('# '))+'}\n\n'+prose('\n'.join(lines[1:]))
body=prose(intro)+'\n\n'+'\n\n'.join(section(n['text']) for n in e['notes'])
body+='\n\n'+r'\section{Exact primary source application ledger}'+'\n\n'
ledger_head=ledger.split('\n## ',1)[0].split('\n',1)[1]
assert ledger_head.startswith('\n');ledger_head=ledger_head[1:]
body+=prose(ledger_head)+'\n\n'
for u in src['units']:
    lo,hi=u['inclusive_LF_interval'];body+=r'\subsection*{'+esc(f"{u['id']}: CLD {u['label']}, LF {lo}--{hi}")+'}\n\n'
    body+=prose(u['exact_applied_statement']+'\n\n'+u['application_and_hypothesis_check']+'\n\n'+u['independent_source_qualification'])+'\n\n'
f=src['supplemental_source_units'][0]
body+=r'\subsection*{Additional F01: CLD 13.3.1--3, LF 19181--19231}'+'\n\n'
body+=prose(f['exact_applied_statement']+'\n\n'+f['application_and_hypothesis_check']+'\n\n'+f['independent_source_qualification'])+'\n\n'
body+=r'\subsection*{Imported deeper foundations}'+'\n\n'+prose('\n\n'.join(src['recursive_foundations']))+'\n\n'
body+=r'\section{Rerun and integrity evidence}'+'\n\n'+esc('Run python audit.py and python build_review.py in this workspace. checks-output.json records 157 matching bound inputs, 31 exact source units, four field-identical actual/expanded372 notes, three differing actual/expanded369 texts, and the 6561-pair finite Plucker diagnostic. No supplied program was executed, no resource-heavy computation or additional model was used, and the TeX is intentionally uncompiled. Execution success and structural checks do not establish mathematical correctness.')+'\n'+r'\end{document}'+'\n'
assert tex.split('\\maketitle\n',1)[1]==body
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
D.mkdir();P.mkdir();shutil.copytree(A/'inputs-LOCALONLY',P/'native-inputs');shutil.copyfile(A/'full-literal-source-ledger-LOCALONLY.json',P/'full-literal-source-ledger-LOCALONLY.json')
for n in ['P21.3-review-paper.tex','P21.3-proof-companion.md','source-ledger-independent.md','source-ledger-independent.json','actual-mathematical-notes.json','whole-proof-coverage.json','original-decision.json','independent-whole372-verdict.json','review-structural-checks.json','environment.json','checks-output.json','deliverable-bindings.json','source-unit-bindings.json','audit-output.txt','build-output.txt','commands.json']:
    shutil.copyfile(A/n,D/n)
shutil.copyfile(actual,D/'actual-settled-native268-FINAL.json');shutil.copyfile(C/'original-task.json',D/'original-task.json')
for n in j['notes']:(D/(n['id']+'-actual-settled.md')).write_text(n['text'])
for n in e['notes']:shutil.copyfile(A/(n['id']+'.md'),D/(n['id']+'-expanded.md'))
Q=D/'native-programs-INERT-DATA';Q.mkdir()
for p in sorted(A.glob('*.py')):shutil.copyfile(p,Q/(p.name+'.DATA.txt'))
now=datetime.now(timezone.utc).isoformat()
qual=dict(recorded_utc=now,status='UNREVIEWED full independent mathematical reconstruction, candidateFALSE; no original closure or new accepted paper.',counts=dict(solved=16,open=26,papers=97),whole_original_solved=False,new_accepted_paper=False,
    actual_FINAL=dict(path=str(actual),sha256=sha(actual),all_four_complete_actual_fields_ROOT_physically_read=True,intermediate_messages_excluded=7),actual_expanded_comparisons=comparisons,
    ROOT_whole_reading=dict(entire_65250_character_proof_ROOT_physically_read=True,untruncated_overlapping_intervals=[[0,18500],[18100,36900],[36500,52500],[52100,65250]],entire_source_application_ledger_in_that_read=True,all_four_expanded_bodies_physically_read_within_proof=True,all_expanded_outside_fields_ROOT_read=True,entire_original_decision_independent_whole372_verdict_coverage_environment_structural_checks_ROOT_read=True,TeX_preamble_ROOT_physically_read=True,entire62483byteTeX_mathematical_body_exact_verified_encoding_of_read_intro_notes_and_full_source_scope_fields=True,encoding_identity_NOT_new_separate_fresh_physical_TeX_reading=True),
    current_new_scope='Every original allowed p including r=0: analytic-trace removability when continuous h is locally uniformly approximable off the actual ordinary locally analytic Z by ordinary smooth zero-Hessian functions and has an ordinary smooth harmonic trace on Z. Genuine refined-unit-chart FIRST-JET PSD domination, exact inactive-coordinate omission, mass<=4LM, energy<=24L^2M and moving mass<=C(F+28M). Actual analytic-dimension finite-fibre foundation for isolated points.',
    whole_scope='All ten369 cutoff/dimension statements; complete scalar367 and relative368 transfer with INITIAL BT/actual positivity/double closedness; full graded Leibniz and both cross terms; fixed-current scalar nets and common-chart SMOOTH form limits; nonclosedness detector ineligible for original; actual coordinate-saturated torus convolution sector.',
    primary_reading=dict(native268_complete_immediate_units='31 CLD-v2 full literal applied units and additional F01 reading attributed native268, not inferred ROOT reading.',ROOT_previous='Complete directly applied ROOT372 CLD units and source pixels retain their previous exact historical coverage; no fabricated new full-book reading.',ROOT_new_F01_full_literal_statement_and_immediate_proof_physically_read=True,F01_bytes=f['bytes'],F01_sha256=f['sha256'],full_CLD_book_freshly_read=False,all_new_full_primary_bodies_literal_units_and_pixels_LOCALONLY=True,deeper_recursive_foundations_not_rebuilt=True),
    original_remaining='Universal original differences U-V with exact D[U]=D[V] have not been shown to satisfy ordinary harmonic approximation/analytic Z/ordinary harmonic trace, nor product-compatible harmonic lifting or arbitrary positive doubly-closed BT-current exhaustion. No original analytic counterexample.',
    qualifications='Middle PSD, not strong-positive ambient domination; original generic Artinian weights; ALL complete fields/trivial allowed; singular/reducible/nonreduced good separated strict boundaryless category; every ordinary open. Cover is not every-open basis, generated CPsh not all original individual psh.',
    supplied_or_native_programs_executed_or_imported=False,native_programs_inert_DATA_only=True,finite_diagnostics_not_analytic_proof=True,compiler='Saved standalone source retained; built-in compiler check follows staging, success not yet verified. No new editor tab or installation.',protected_editor_open_unchanged=True)
write(D/'mandatory-ROOT-whole-proof-source-scope-qualifications-20261008.json',qual)
(D/'README.md').write_text('Whole independent candidate379 for P21.3\n\nUNREVIEWED; candidateFALSE. Counts remain16/42 solved,26 OPEN,97 accepted papers.\n\nThe entire independent reconstruction retains the complete middle-cone calculus, ten cutoff/dimension results, scalar and smooth-form transfers, logarithmic analytic-trace removability and exact original gaps. The harmonic-approximation extension and refined ordinary-chart details are explicit. This does not establish the required hypotheses for all original pairs or currents.\n\nAll four different actual FINAL and expanded texts are retained. The entire proof and source/scope ledger were physically read; the full TeX is verified an exact encoding of that read material, with duplicate-reading qualifications. Additional F01 full source statement/proof was freshly read by ROOT; other new source reading stays attributed native268 and previous ROOT scopes stay unchanged. All full primary bodies, literal units and pixels LOCALONLY. Native programs inert DATA never executed/imported. Protected editor remains unchanged. Compiler success unverified.\n')
binding=dict(recorded_utc=now,round=268,paper=379,atom='P21.3',public_directory=str(D),private_directory=str(P),whole_original_solved=False,new_accepted_paper=False,counts=dict(solved=16,open=26,papers=97),qualified_whole_reading=qual,public_whole_body_bindings=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(D.rglob('*')) if p.is_file()],private_retention_bindings=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(P.rglob('*')) if p.is_file()]);write(B,binding)
for n in ['active-work.json','checklist-current.json']:
    p=R/n;x=load(p);assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x['native268_complete379']=dict(public_directory=str(D),whole_binding=str(B),whole_binding_sha256=sha(B),actual_FINAL_sha256=sha(actual),candidate=False,original_closed=False,new_accepted_paper=False,independent_whole_reconstruction_of372=True);x['updated_utc']=now;write(p,x)
print(json.dumps(dict(round=268,paper=379,public_files=len(binding['public_whole_body_bindings']),private_files=len(binding['private_retention_bindings']),whole_TeX_sha256=sha(D/'P21.3-review-paper.tex'),whole_proof_sha256=sha(D/'P21.3-proof-companion.md'),binding_sha256=sha(B),candidate=False,solved=16,open=26,papers=97),indent=2))
